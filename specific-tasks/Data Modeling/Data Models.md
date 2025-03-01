# About

This is the companion file to the `Data Models.xlsx` document and intended to be a lower-fidelity alternative to that document.

- Table List:
   - Table 1
   - Table 2
   - Table 3

# Table Models

# ++Model 1++

- Model Name: ++Model Name++
- Dataset Name: ++Database Name++
- Model Type: [Source Model, Table Model, Report Model]
- Status: [Complete, In Progress]
- Grain: *(column_1) + (column_2) + (column_3)*
- Load Frequency: [Monthly,Weekly,Daily,Intraday,Ad hoc]
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

## Additional Details

```
Notes on any of the following:

- Missing value treatment
- Unexpected values
```

# ++Non-Relational Model++

{
	"first_name":""
	"last_name":"",
	"title":"",
	"organization:"",
	"education":{
			{},
			{}
		},
	"missions"	
}

__Scope__

*What is the scope of this model, and equivalently what **doesn't** it include?*

## Additional Details

*See [additional details](#additional-details)