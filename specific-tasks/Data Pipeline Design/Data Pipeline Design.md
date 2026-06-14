__Tasks__

- [ ] Complete the Job Specifications section
- [ ] Create Data Pipeline design diagram


__Job Specifications__

>  Describe any logic container artifacts such as stored procedures etc.
> 
>  Details:
>    - A 'Component' could be any one of the following: Job, View, Report (or more)
>    - The load time is optional and not applicable to the 'View' component type (for example)
> 
>  __Job Specifications__
>  
>  *Describe any logic container artifacts such as stored procedures etc. *
>  
>  1.  Data Exports Job @ 6 AM
>      - Details
>        - Job URL: https://dashboard-edw.homedepot.com/export/jobDetail?id=e47aeeca_caec_4bf9_826b_eb2ef6658d8f 
>        - Exports from combined IDM BI and `pr-edw-views-thd` sources to MS SQL IdmReporting4f
>  2. View `StepView.dbo.BuypackItem_Quantity` reads `StepView.dbo.BigQueryExports_MuomItem_Quantity`
>  3. View `StepView.dbo.vw_COMBOMULTIBOXREPORT_ComboItem_Quantity` reads `StepView.dbo.BuypackItem_Quantity`
>  4. Execute MS SQL Job DAILY_COMBOMULTIBOX_REPORT_PRELOAD @ 9 AM
>     1. Execute Load Procedure `StepView.dbo.SP_COMBOMULTIBOXREPORT_PRELOAD`
>  1. Reports
>     1. ComboOrMultiboxAttributesByOMSID
>       2. http://idmreporting4b/ReportServer/Pages/ReportViewer.aspx?/IDM Reports/IDM Projects/Combo/ComboOrMultiboxAttributesByOMSID


1. Operation: ++Operation Name++ @ HH:MM AM/PM
      1. Operation Step 1 @ HH:MM AM/PM
         - Detail 1
         - Detail 2
      2. Operation: ++Operation Name++ @ HH:MM AM/PM
2. Data Store: ++Data Store Name++
3. Operation: 

