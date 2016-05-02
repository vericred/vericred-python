# vericred_client.ProvidersApi

All URIs are relative to *https://api.vericred.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**providers_get**](ProvidersApi.md#providers_get) | **GET** /providers | Find providers by term and zip code
[**providers_npi_get**](ProvidersApi.md#providers_npi_get) | **GET** /providers/{npi} | Find a specific Provider


# **providers_get**
> InlineResponse200 providers_get(search_term, zip_code, accepts_insurance=accepts_insurance, hios_ids=hios_ids, page=page, per_page=per_page, radius=radius)

Find providers by term and zip code

All `Provider` searches require a `zip_code`, which we use for weighting
the search results to favor `Provider`s that are near the user.  For example,
we would want "Dr. John Smith" who is 5 miles away to appear before
"Dr. John Smith" who is 100 miles away.

The weighting also allows for non-exact matches.  In our prior example, we
would want "Dr. Jon Smith" who is 2 miles away to appear before the exact
match "Dr. John Smith" who is 100 miles away because it is more likely that
the user just entered an incorrect name.

The free text search also supports Specialty name search and "body part"
Specialty name search.  So, searching "John Smith nose" would return
"Dr. John Smith", the ENT Specialist before "Dr. John Smith" the Internist.



### Example 
```python
import time
import vericred_client
from vericred_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vericred_client.ProvidersApi()
search_term = 'search_term_example' # str | String to search by
zip_code = 'zip_code_example' # str | Zip Code to search near
accepts_insurance = 'accepts_insurance_example' # str | Limit results to Providers who accept at least one insurance plan.  Note that the inverse of this filter is not supported and any value will evaluate to true (optional)
hios_ids = ['hios_ids_example'] # list[str] | HIOS id of one or more plans (optional)
page = 'page_example' # str | Page number (optional)
per_page = 'per_page_example' # str | Number of records to return per page (optional)
radius = 'radius_example' # str | Radius (in miles) to use to limit results (optional)

try: 
    # Find providers by term and zip code
    api_response = api_instance.providers_get(search_term, zip_code, accepts_insurance=accepts_insurance, hios_ids=hios_ids, page=page, per_page=per_page, radius=radius)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ProvidersApi->providers_get: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_term** | **str**| String to search by | 
 **zip_code** | **str**| Zip Code to search near | 
 **accepts_insurance** | **str**| Limit results to Providers who accept at least one insurance plan.  Note that the inverse of this filter is not supported and any value will evaluate to true | [optional] 
 **hios_ids** | [**list[str]**](str.md)| HIOS id of one or more plans | [optional] 
 **page** | **str**| Page number | [optional] 
 **per_page** | **str**| Number of records to return per page | [optional] 
 **radius** | **str**| Radius (in miles) to use to limit results | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **providers_npi_get**
> InlineResponse2001 providers_npi_get(npi)

Find a specific Provider

To retrieve a specific provider, just perform a GET using his NPI number



### Example 
```python
import time
import vericred_client
from vericred_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vericred_client.ProvidersApi()
npi = 'npi_example' # str | NPI number

try: 
    # Find a specific Provider
    api_response = api_instance.providers_npi_get(npi)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ProvidersApi->providers_npi_get: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **npi** | **str**| NPI number | 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

