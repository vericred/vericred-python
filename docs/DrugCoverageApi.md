# vericred_client.DrugCoverageApi

All URIs are relative to *https://api.vericred.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**drugs_ndc_coverages_get**](DrugCoverageApi.md#drugs_ndc_coverages_get) | **GET** /drugs/{ndc}/coverages | Find Drug Coverages for a given NDC


# **drugs_ndc_coverages_get**
> list[DrugCoverage] drugs_ndc_coverages_get(ndc)

Find Drug Coverages for a given NDC

Drug Coverages are the specific tier level, quantity limit, prior authorization
and step therapy for a given Drug/Plan combination.  This endpoint returns
all DrugCoverages for a given Drug



### Example 
```python
import time
import vericred_client
from vericred_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vericred_client.DrugCoverageApi()
ndc = 'ndc_example' # str | NDC for a drug

try: 
    # Find Drug Coverages for a given NDC
    api_response = api_instance.drugs_ndc_coverages_get(ndc)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DrugCoverageApi->drugs_ndc_coverages_get: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ndc** | **str**| NDC for a drug | 

### Return type

[**list[DrugCoverage]**](DrugCoverage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

