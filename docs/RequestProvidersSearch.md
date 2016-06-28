# RequestProvidersSearch

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accepts_insurance** | **bool** | Limit results to Providers who accept at least one insurance         plan.  Note that the inverse of this filter is not supported and         any value will evaluate to true | [optional] 
**hios_ids** | **list[str]** | List of HIOS ids | [optional] 
**page** | **int** | Page number | [optional] 
**per_page** | **int** | Number of records to return per page | [optional] 
**radius** | **int** | Radius (in miles) to use to limit results | [optional] 
**search_term** | **str** | String to search by | [optional] 
**zip_code** | **str** | Zip Code to search near | [optional] 
**type** | **str** | Either organization or individual | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


