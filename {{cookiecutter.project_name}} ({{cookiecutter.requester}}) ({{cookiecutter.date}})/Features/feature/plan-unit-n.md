# Data Modeling

## Data Model N - (Conceptual Model Name)

- Model Name: ++Model Name++
- Dataset Name: ++Database Name++
- Model Type: [Source Model, Table Model, Report Model]
- Status: [Complete, In Progress]
- Grain: *(column_1) + (column_2) + (column_3)*
- Load Frequency: [Monthly, Weekly, Daily, Intraday, Ad hoc]
- Historical Model: [Yes, No]
- Columns
  - column_1
    - Description: *short description*
		- Data Category: [Qualitative, Quantitative]
    - Data Type: [string, float, integer, boolean, date, datetime]
    - Data Object Type: [struct, single-valued,array]
  - column_2
    - ...
  - ...

__Scope__

*What is the scope of this model, and equivalently what **doesn't** it include?*

### Additional Details

```
Notes on any of the following:

- Missing value treatment
- Unexpected values
```

# Data Pipeline Design - Procedural-level

- (final)
  - Model 1 - Conceptual Model Name 1
  <!-- 
  - Description - 
  - Name - 
  -->
  - Model 2 - Conceptual Model Name 2
  - Model 3 - Conceptual Model Name 3

# Data Pipeline Design - Job-level

Pipeline Data Stores:
- 1. VOC Attribute Values dbt Model - `analytics-idmreporting-thd.pr_reports.bqe_idm_voc_items_attribute_data_update`
- 2. Attribute Values Staging - Regulation_Compliance.dbo.BigQueryExports_IDM_VOC_ITEM_DATA_STAGE_ALL_SIZE
- 3. Attribute Values - Regulation_Compliance.dbo.IDM_VOC_ITEM_DATA_STAGE_ALL_SIZE
- 4. VOC Values Base Table - Regulation_Compliance.dbo.IDM_VOC_ITEM_DATA_FINAL
- 5. Report Base Table - DBO.VOC_IDM_VALUES_VOC_CHECK_STR

Pipeline Jobs:
- 1. [Attribute Values Export Job](https://dashboard-edw.homedepot.com/export/jobDetail?id=92bd0804_36e0_4291_baec_e5131d02ef82)
- 2. MS SQL Server - Load Attribute Values from Staging - `csp_IDM_VOC_ITEMS_ATTRIBUTE_DATA_UPDATE.sql`
- 3. Merge global and VOC-specific attribute values - DAILY_IDM_VOC_TABLES_SCORECARD10_DATA_UPDATE
- 4. Load Report Base Table - Regulation_Compliance.dbo.sp_VOC_COMPLIANCE_UPDATE

  
__Data Pipeline 1__
- (final)
  - (...)
  - Data Store 5 - Report Base Table
    - Job 4 - Load Report Base Table
      - (...)
        - Data Store 4 - VOC Values Base Table
          - Job 3 - Merge Values
            - Data Store 2 - Attribute Values
              - Job 2 - MS SQL Server - Load Attribute Values from Staging
                - Data Store 1 - Attribute Values Staging
                  - Job 1  - Attribute Values Export Job
                    - Data Store 1- VOC Attribute Values dbt Model

__Data Pipeline 2__
- (final)
  - (...)
  - Data Store 5 - Report Base Table
    - Job 4 - Load Report Base Table
      - (...)
        - Data Store 4 - VOC Values Base Table
          - Job 3 - Merge Values
            - Data Store 2 - Attribute Values
              - Job 2 - MS SQL Server - Load Attribute Values from Staging
                - Data Store 1 - Attribute Values Staging
                  - Job 1  - Attribute Values Export Job
                    - Data Store 1- VOC Attribute Values dbt Model

## Job 1 - Attribute Values Export Job

...

## Data Store 1 - VOC Attribute Values dbt Model

...

# Dashboard

## Component N - (Component Name)

__Worksheets__

__Parameters__

__Field Names__

__Filters__

__Actions__

### Field - (Field Name)

### Action - (Action Name)

### Parameter - (Parameter Name)
