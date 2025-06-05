# Template

[Analysis](<./Audit Notes Template.md>)

# Analysis N (Template)

## N.N

- __Analysis Complete__ - [ ]

(See N.N.1) - *Description...*

```sql

```

(See N.N.2) - *Description...*

```sql

```

# 1.1

 - __Description__ - products in old table that are not in new table, specifically for vendor enrich

```sql
with new_wf as
(
select distinct product_id
from pr_staging.stg_itm__workflow_state_entries
where workflow_state_id = 'ENRICH_STARTENRICH'
  -- and entry_date < '2025-05-15'
)
, old_wf as
(
select distinct omsid
from IDM.WFH_Full_Parsed
where wf_state = 'DOTCOM_VENRITEM'
and wf_date_enter > '2017-01-01'
  -- and wf_date_enter < '2025-05-15'
)


select omsid
from new_wf as n
  full join old_wf as o
    on o.omsid = n.product_id
where n.product_id is null
```


# Analysis 2

```sql
with new_wf as
(
select distinct product_id
from pr_staging.stg_itm__workflow_state_entries
where workflow_state_id = 'ENRICH_STARTENRICH'
  and entry_date > '2017-01-01'
  and entry_date < '2025-05-15'
)
, old_wf as
(
select distinct omsid
from IDM.WFH_Full_Parsed
where lower(wf_state) like '%venritem%'
and wf_date_enter > '2017-01-01'
  and wf_date_enter < '2025-05-15'
)


select coalesce(omsid,product_id) as product_id
  , omsid is null as missing_from_old
  , product_id is null as missing_from_new
from new_wf as n
  full join old_wf as o
    on o.omsid = n.product_id
where (
  n.product_id is null
  or o.omsid is null
  )
```

- ~~542 discrepancies records observed~~
- 

## 2.2

```sql
select *
from IDM.WFH_Full_Parsed
where omsid = '300808919'
  and wf_state = 'DOTCOM_VENRITEM';

select *
from pr_staging.stg_itm__workflow_state_entries
where workflow_state_id = 'ENRICH_STARTENRICH'
  and product_id = '300808919'
```

The remaining states are in an 'error' state 

```sql
select *
from IDM.WFH_Full_Parsed 
where omsid = '300808919'
  and lower(wf_state) like '%venritem%'
```

## 2.3

```sql
select *
from IDM.WFH_Full_Parsed
where omsid = '302649162'
  and wf_state = 'DOTCOM_VENRITEM';

select *
from pr_staging.stg_itm__workflow_state_entries
where workflow_state_id = 'ENRICH_STARTENRICH'
  and product_id = '302649162'
```
TODO - for the ~180 items remaining in the base set, not sure where this discrepancy is generally coming from.

# Workflow Entries Data Integrity


```sql
select count(*)
from pr_staging.stg_itm__workflow_state_entries
where state_id is null
```


# Analysis 3

```sql
with new_wf as
(
select count(*) as count_records
from pr_staging.stg_itm__workflow_state_entries
where workflow_state_id = 'ENRICH_STARTENRICH'
  and entry_date > '2017-01-01'
  and entry_date < '2025-05-15'
)
, old_wf as
(
select count(*) as count_records
from IDM.WFH_Full_Parsed
where lower(wf_state) like '%venritem%'
and wf_date_enter > '2017-01-01'
  and wf_date_enter < '2025-05-15'
)

select n.count_records as new_count_records
  , o.count_records as old_count_records
  , abs(o.count_records - n.count_records) as count_difference
from old_wf as o
  cross join new_wf as n
```

There is hardly a record count difference after adjusting for primary causes of discrepancies such as the entry date


# Analysis 4 - Column Value Population

```sql
select sum(case when state_id is null then 1 else 0 end)/count(*) as perc_null
  , sum(case when state_id is not null then 1 else 0 end)/count(*) as perc_complete
from pr_staging.stg_itm__workflow_state_entries
```


TODO - Scenarios where the state_id IS NULL - I think this is often where the product exited from the workflow and has no TOSTATEID value; may need to COALESCE upstream.


## 4.2

```sql
select *
from pr_staging.stg_itm__workflow_state_entries
where state_id is null
limit 1000;

select *
from pr-mit-product.idm_step_replication.stepsys_transitionlog
where seqno = 762036972;
```

## 4.3

 - __Analysis Complete__ - [x]

NULL stateid analysis for single product. 

 - Why is this product lacking a state and should it have one?
 - Should the timestamp be placed on the exit_date column rather than entry_date?


```sql
  with nodes as 
  (
  select *
  from `analytics-idmreporting-thd`.`pr_staging`.`fnl_itm__nodes`
  )
  , transition_log as 
  (
  select * except(logtime)
    , parse_datetime('%Y-%m-%d %H:%M:%S.0',logtime) as logtime 
  from `pr-mit-product`.`idm_step_replication`.`stepsys_transitionlog`
  where logtype = 0
  )
  , entries as 
  (
  select stateflowid
    , tostateid as stateid
    , nodename
    , seqno
    , logtime
    , executorname 
    , dense_rank() over (partition by stateflowid, tostateid, nodename order by seqno) as trank
  from transition_log

  )
  , exits as 
  (
  select stateflowid
    , fromstateid as stateid
    , nodename
    , seqno
    , logtime
    , executorname 
    , dense_rank() over (partition by stateflowid, fromstateid, nodename order by seqno) as trank
  from transition_log
  )
  , final as 
  (
  select 
    entries.stateflowid as workflow_id_internal
    , coalesce(entries.stateid,exits.stateid,'(Workflow Exit)') as state_id
    , entries.nodename as product_id
    , entries.logtime as entry_date
    , exits.logtime as exit_date
    , entries.trank as cycle_rank
    , exits.executorname as exit_user_id
    , entries.executorname as entry_user_id
    , entries.seqno as seqno
  from entries
    left join exits
      on entries.stateflowid = exits.stateflowid
      and entries.stateid = exits.stateid
      and entries.nodename = exits.nodename
      and entries.trank = exits.trank
  )

  select *
  from final
  where product_id = '300666224'
    and seqno = 762036972
```


(See 4.3.1) This query results in two TOSTATEID and two FROMSTATEID records for 'QCSTEP'. The PARTITION BY in previous query includes stateflowid in ranking logic, but perhaps this shouldn't be factored in? Are the State ID values unique across all of IDM?

```sql
  with nodes as 
  (
  select *
  from `analytics-idmreporting-thd`.`pr_staging`.`fnl_itm__nodes`
  )
  , transition_log as 
  (
  select * except(logtime)
    , parse_datetime('%Y-%m-%d %H:%M:%S.0',logtime) as logtime 
  from `pr-mit-product`.`idm_step_replication`.`stepsys_transitionlog`
  where logtype = 0
    and nodename = '300666224'
  )
  , entries as 
  (
  select stateflowid
    , tostateid as stateid
    , nodename
    , seqno
    , logtime
    , executorname 
    , dense_rank() over (partition by stateflowid, tostateid, nodename order by seqno) as trank
  from transition_log

  )
  , exits as 
  (
  select stateflowid
    , fromstateid as stateid
    , nodename
    , seqno
    , logtime
    , executorname 
    , dense_rank() over (partition by stateflowid, fromstateid, nodename order by seqno) as trank
  from transition_log
  )

  select *
  from transition_log
  where tostateid = 'QCSTEP' or fromstateid = 'QCSTEP'
```

```sql

```

## 4.4

General NULL column analysis and validation.

- __Analysis Complete__ - [ ]

(See N.N.1) - *Description...*

```sql

```

(See 4.4.1) - NULL value analysis for Workflow State Entries

```sql
select count(*) as count_records
  , count(workflow_state_id) as count_workflow_state_id
  , count(workflow_id) as count_workflow_id
  , count(state_id) as count_state_id
  , count(product_id) as count_state_id
  , count(entry_date) as count_entry_date
  , count(entry_user_id) as count_entry_users
  , count(exit_date) as count_exit_date
  , count(exit_user_id) as count_exit_users
  , count(entry_user_id) as count_entries
  , count(cycle_rank) as count_cycles
  , count(entry_id) as count_entries
from pr_staging.stg_itm__workflow_state_entries;
```


(See 4.4.2) - NULL value analysis for Workflow States

```sql
select count(workflow_id) as workflow_id
, count(workflow_name) as workflow_name
, count(state_id) as state_id
, count(state_name) as state_name
, count(workflow_state_id) as workflow_state_id
, count(is_initial_state) as is_initial_state
, count(is_final_state) as is_final_state
, sum(case when array_length(required_attr_ids) > 0 then 1 else 0 end) as required_attr_ids
, sum(case when array_length(required_attr_groups) > 0 then 1 else 0 end) as required_attr_groups
, sum(case when array_length(required_link_types) > 0 then 1 else 0 end) as required_link_types
, count(workspace_id) as workspace_id
from pr_staging.fnl_itm__workflow_states
```

# Analysis 5 - Record Uniqueness

## 5.1

- __Analysis Complete__ - [x]

(See 5.1.1) - Workflow State Entries

```sql
select entry_id, count(*) 
from pr_staging.stg_itm__workflow_state_entries
group by entry_id
having count(*) > 1
```

(See 5.1.2) - Workflow States

```sql
select workflow_state_id, workspace_id, count(*)
from pr_staging.fnl_itm__workflow_states
group by workflow_state_id, workspace_id
having count(*) > 1
```