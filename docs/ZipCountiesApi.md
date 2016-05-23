# vericred_client.ZipCountiesApi

All URIs are relative to *https://api.vericred.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_zip_counties**](ZipCountiesApi.md#get_zip_counties) | **GET** /zip_counties | Search for Zip Counties


# **get_zip_counties**
> ZipCountyResponse get_zip_counties(zip_prefix, vericred_api_key=vericred_api_key)

Search for Zip Counties

Our `Plan` endpoints require a zip code and a fips (county) code.  This is because plan pricing requires both of these elements.  Users are unlikely to know their fips code, so we provide this endpoint to look up a `ZipCounty` by zip code and return both the selected zip and fips codes.

### Example 
```python
import time
import vericred_client
from vericred_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vericred_client.ZipCountiesApi()
zip_prefix = '1002' # str | Partial five-digit Zip
vericred_api_key = 'api-doc-key' # str | API Key (optional)

try: 
    # Search for Zip Counties
    api_response = api_instance.get_zip_counties(zip_prefix, vericred_api_key=vericred_api_key)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ZipCountiesApi->get_zip_counties: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zip_prefix** | **str**| Partial five-digit Zip | 
 **vericred_api_key** | **str**| API Key | [optional] 

### Return type

[**ZipCountyResponse**](ZipCountyResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

