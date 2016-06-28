# vericred_client.NetworksApi

All URIs are relative to *https://api.vericred.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_networks**](NetworksApi.md#list_networks) | **GET** /networks | Networks


# **list_networks**
> NetworkSearchResponse list_networks(carrier_id, page=page, per_page=per_page)

Networks

A network is a list of the doctors, other health care providers, and hospitals that a plan has contracted with to provide medical care to its members. This endpoint is paginated.

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
api_instance = vericred_client.NetworksApi()
carrier_id = '33333' # str | Carrier HIOS Issuer ID
page = 1 # int | Page of paginated response (optional)
per_page = 1 # int | Responses per page (optional)

try: 
    # Networks
    api_response = api_instance.list_networks(carrier_id, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling NetworksApi->list_networks: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **carrier_id** | **str**| Carrier HIOS Issuer ID | 
 **page** | **int**| Page of paginated response | [optional] 
 **per_page** | **int**| Responses per page | [optional] 

### Return type

[**NetworkSearchResponse**](NetworkSearchResponse.md)

### Authorization

[Vericred-Api-Key](../README.md#Vericred-Api-Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

