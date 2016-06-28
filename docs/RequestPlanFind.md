# RequestPlanFind

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**applicants** | [**list[RequestPlanFindApplicant]**](RequestPlanFindApplicant.md) | Applicants for desired plans. | [optional] 
**enrollment_date** | **str** | Date of enrollment | [optional] 
**drug_packages** | [**list[DrugPackage]**](DrugPackage.md) | National Drug Code Package Id | [optional] 
**fips_code** | **str** | County code to determine eligibility | [optional] 
**household_income** | **int** | Total household income. | [optional] 
**household_size** | **int** | Number of people living in household. | [optional] 
**market** | **str** | Type of plan to search for. | [optional] 
**providers** | [**list[RequestPlanFindProvider]**](RequestPlanFindProvider.md) | List of providers to search for. | [optional] 
**page** | **int** | Selected page of paginated response. | [optional] 
**per_page** | **int** | Results per page of response. | [optional] 
**sort** | **str** | Sort responses by plan field. | [optional] 
**zip_code** | **str** | 5-digit zip code - this helps determine pricing. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


