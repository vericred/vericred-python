# vericred_client.ProvidersApi

All URIs are relative to *https://api.vericred.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_provider**](ProvidersApi.md#get_provider) | **GET** /providers/{npi} | Find a Provider
[**get_providers**](ProvidersApi.md#get_providers) | **POST** /providers/search | Find Providers


# **get_provider**
> ProviderShowResponse get_provider(npi)

Find a Provider

To retrieve a specific provider, just perform a GET using his NPI number

### Example 
```python
import time
import vericred_client
from vericred_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Vericred-Api-Key
vericred_client.configuration.api_key['Vericred-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# vericred_client.configuration.api_key_prefix['Vericred-Api-Key'] = 'Bearer'

# create an instance of the API class
api_instance = vericred_client.ProvidersApi()
npi = '1234567890' # str | NPI number

try: 
    # Find a Provider
    api_response = api_instance.get_provider(npi)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ProvidersApi->get_provider: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **npi** | **str**| NPI number | 

### Return type

[**ProviderShowResponse**](ProviderShowResponse.md)

### Authorization

[Vericred-Api-Key](../README.md#Vericred-Api-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_providers**
> ProvidersSearchResponse get_providers(body=body)

Find Providers

All `Provider` searches require a `zip_code`, which we use for weighting the search results to favor `Provider`s that are near the user.  For example, we would want \"Dr. John Smith\" who is 5 miles away to appear before \"Dr. John Smith\" who is 100 miles away.  The weighting also allows for non-exact matches.  In our prior example, we would want \"Dr. Jon Smith\" who is 2 miles away to appear before the exact match \"Dr. John Smith\" who is 100 miles away because it is more likely that the user just entered an incorrect name.  The free text search also supports Specialty name search and \"body part\" Specialty name search.  So, searching \"John Smith nose\" would return \"Dr. John Smith\", the ENT Specialist before \"Dr. John Smith\" the Internist. 

### Example 
```python
import time
import vericred_client
from vericred_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Vericred-Api-Key
vericred_client.configuration.api_key['Vericred-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# vericred_client.configuration.api_key_prefix['Vericred-Api-Key'] = 'Bearer'

# create an instance of the API class
api_instance = vericred_client.ProvidersApi()
body = vericred_client.RequestProvidersSearch() # RequestProvidersSearch |  (optional)

try: 
    # Find Providers
    api_response = api_instance.get_providers(body=body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ProvidersApi->get_providers: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RequestProvidersSearch**](RequestProvidersSearch.md)|  | [optional] 

### Return type

[**ProvidersSearchResponse**](ProvidersSearchResponse.md)

### Authorization

[Vericred-Api-Key](../README.md#Vericred-Api-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

