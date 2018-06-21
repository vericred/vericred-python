# DentalPlan

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The dental plan identifier | [optional] 
**name** | **str** | The dental plan name | [optional] 
**issuer_name** | **str** | Name of the insurance carrier | [optional] 
**audience** | **str** | The dental plan audience | [optional] 
**benefits_summary_url** | **str** | Link to the summary of benefits and coverage (SBC) document. | [optional] 
**logo_url** | **str** | Link to a copy of the insurance carrier&#39;s logo | [optional] 
**plan_type** | **str** | Category of the plan (e.g. EPO, HMO, PPO, POS, Indemnity, PACE,HMO w/POS, Cost, FFS, MSA) | [optional] 
**stand_alone** | **bool** | Stand alone flag for dental plan | [optional] 
**source** | **str** | Source of the plan benefit data | [optional] 
**identifiers** | [**list[PlanIdentifier]**](PlanIdentifier.md) | List of identifiers of this Plan | [optional] 
**benefits** | [**DentalPlanBenefits**](DentalPlanBenefits.md) | Dental Plan Benefits | [optional] 
**premium** | **float** | Cumulative premium amount | [optional] 
**premium_source** | **str** | Source of the base pricing data | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


