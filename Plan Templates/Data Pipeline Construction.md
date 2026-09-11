# Tasks

- [ ] Generic Task 1
- [ ] Generic Task 2
- [ ] Generic Task 3

# Data Models

*Sample copied from previous implementation*

```md
- Models
  - `df_reports.idm_factbook_attributes_metrics`
    - Grain
        - attr_id + attr_metric_key
    - Description
      - Attributes + dimension roll-up key and the corresponding metrics for each; removes node_id from contents/grain
  - `df_reports.idm_factbook_attributes`
    - Grain
        - attr_id
    - Description
  - `df_reports.idm_factbook_attributes_metrics_multivalued`
    - Grain
      - attr_metric_key + attr_id + dimension + dimension_attribute + dimension_value
    - Description
  - `df_staging.stg_rpt__idm_factbook_attributes_metrics`
    - Grain
      - attr_id + node_id
    - Description
      - Links attributes to products via value presence OR attribute-to-product mappings (for Category Specific attributes)
  - `stg_rpt__idm_factbook_attributes_metrics_key_bridge`
    - Description
      - Retrieves the hierarchical rollup dimension columns to add context to reporting and 'bridge' to the attr_metric_key
  - `df_reports.idm_factbook_attributes_rollup_key_attr_bridge`
    - Grain
      - attr_metric_key + attr_id
  - `df_reports.idm_factbook_attributes_rollup_key_dim_bridge`
    - Description
      - Distinct set of `attr_metric_key` values and associated rollup dimensions 
    - Grain
      - attr_metric_key
- Data Sources
```

# Data Pipeline

*Sample copied from previous implementation*

```md
- Data Sources
  - Attributes Metrics
    - `reports__idm_factbook_attributes_metrics`
    - `reports__idm_factbook_attributes`
  - Attributes Metrics > Multivalued
    - `reports__idm_factbook_attributes_metrics_multivalued`
  - Attributes Cross-reference
    - `reports__idm_factbook_attributes`
- Models
    - `reports__idm_factbook_attributes_metrics`
    - `reports__idm_factbook_attributes_metrics_multivalued`
    - `reports__idm_factbook_attributes`
    - `df_reports.idm_factbook_attributes_rollup_key_attr_bridge`
      - 
```