# vericred_client.DrugsApi

All URIs are relative to *https://api.vericred.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_drug_coverages**](DrugsApi.md#get_drug_coverages) | **GET** /drug_packages/{ndc_package_code}/coverages | Search for DrugCoverages
[**list_drugs**](DrugsApi.md#list_drugs) | **GET** /drugs | Drug Search


# **get_drug_coverages**
> DrugCoverageResponse get_drug_coverages(ndc_package_code, audience, state_code, vericred_api_key=vericred_api_key)

Search for DrugCoverages

Drug Coverages are the specific tier level, quantity limit, prior authorization and step therapy for a given Drug/Plan combination. This endpoint returns all DrugCoverages for a given Drug

### Example 
```python
import time
import vericred_client
from vericred_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vericred_client.DrugsApi()
ndc_package_code = '12345-4321-11' # str | NDC package code
audience = 'individual' # str | Two-character state code
state_code = 'NY' # str | Two-character state code
vericred_api_key = 'api-doc-key' # str | API Key (optional)

try: 
    # Search for DrugCoverages
    api_response = api_instance.get_drug_coverages(ndc_package_code, audience, state_code, vericred_api_key=vericred_api_key)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DrugsApi->get_drug_coverages: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ndc_package_code** | **str**| NDC package code | 
 **audience** | **str**| Two-character state code | 
 **state_code** | **str**| Two-character state code | 
 **vericred_api_key** | **str**| API Key | [optional] 

### Return type

[**DrugCoverageResponse**](DrugCoverageResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_drugs**
> DrugSearchResponse list_drugs(search_term, vericred_api_key=vericred_api_key)

Drug Search

Search for drugs by proprietary name

### Example 
```python
import time
import vericred_client
from vericred_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vericred_client.DrugsApi()
search_term = 'Zyrtec' # str | Full or partial proprietary name of drug
vericred_api_key = 'api-doc-key' # str | API Key (optional)

try: 
    # Drug Search
    api_response = api_instance.list_drugs(search_term, vericred_api_key=vericred_api_key)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DrugsApi->list_drugs: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_term** | **str**| Full or partial proprietary name of drug | 
 **vericred_api_key** | **str**| API Key | [optional] 

### Return type

[**DrugSearchResponse**](DrugSearchResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

