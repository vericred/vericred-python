# Provider

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accepting_change_of_payor_patients** | **bool** | Is this provider accepting patients with a change of insurance? | [optional] 
**accepting_medicaid_patients** | **bool** | Is this provider accepting new Medicaid patients? | [optional] 
**accepting_medicare_patients** | **bool** | Is this provider accepting new Medicare patients? | [optional] 
**accepting_private_patients** | **bool** | Is this provider accepting new patients with private insurance? | [optional] 
**accepting_referral_patients** | **bool** | Is this provider accepting new patients via referrals? | [optional] 
**city** | **str** | City name (e.g. Springfield). | [optional] 
**email** | **str** | Primary email address to contact the provider. | [optional] 
**gender** | **str** | Provider&#39;s gender (M or F) | [optional] 
**first_name** | **str** | Given name for the provider. | [optional] 
**hios_ids** | **list[str]** | List of HIOS ids for this provider | [optional] 
**id** | **int** | National Provider Index (NPI) number | [optional] 
**last_name** | **str** | Family name for the provider. | [optional] 
**latitude** | **float** | Latitude of provider | [optional] 
**longitude** | **float** | Longitude of provider | [optional] 
**middle_name** | **str** | Middle name for the provider. | [optional] 
**personal_phone** | **str** | Personal contact phone for the provider. | [optional] 
**phone** | **str** | Office phone for the provider | [optional] 
**presentation_name** | **str** | Preferred name for display (e.g. Dr. Francis White may prefer Dr. Frank White) | [optional] 
**specialty** | **str** | Name of the primary Specialty | [optional] 
**state** | **str** | State code for the provider&#39;s address (e.g. NY). | [optional] 
**state_id** | **int** | Foreign key to States | [optional] 
**street_line_1** | **str** | First line of the provider&#39;s street address. | [optional] 
**street_line_2** | **str** | Second line of the provider&#39;s street address. | [optional] 
**suffix** | **str** | Suffix for the provider&#39;s name (e.g. Jr) | [optional] 
**title** | **str** | Professional title for the provider (e.g. Dr). | [optional] 
**type** | **str** | Type of NPI number (individual provider vs organization). | [optional] 
**zip_code** | **str** | Postal code for the provider&#39;s address (e.g. 11215) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


