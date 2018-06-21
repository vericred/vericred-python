# DentalPlanSearchRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**applicants** | [**list[DentalPlanSearchApplicant]**](DentalPlanSearchApplicant.md) | Applicants for desired plans. | [optional] 
**issuer_id** | **int** | National-level issuer id | [optional] 
**enrollment_date** | **str** | Date of enrollment | [optional] 
**fips_code** | **str** | County code to determine eligibility | [optional] 
**zip_code** | **str** | 5-digit zip code - this helps determine pricing. | [optional] 
**market** | **str** | The audience of plan to search for. Possible values are individual, small_group | [optional] 
**page** | **int** | Selected page of paginated response. | [optional] 
**per_page** | **int** | Results per page of response. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


