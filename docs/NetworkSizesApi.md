# vericred_client.NetworkSizesApi

All URIs are relative to *https://api.vericred.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_state_network_sizes**](NetworkSizesApi.md#list_state_network_sizes) | **GET** /states/{state_id}/network_sizes | State Network Sizes


# **list_state_network_sizes**
> StateNetworkSizeResponse list_state_network_sizes(state_id, page=page, per_page=per_page)

State Network Sizes

The number of in-network Providers for each network in a given state. This data is recalculated nightly.  The endpoint is paginated.

### Example 
```python
from __future__ import print_statement
import time
import vericred_client
from vericred_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Vericred-Api-Key
vericred_client.configuration.api_key['Vericred-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# vericred_client.configuration.api_key_prefix['Vericred-Api-Key'] = 'Bearer'

# create an instance of the API class
api_instance = vericred_client.NetworkSizesApi()
state_id = 'CA' # str | State code
page = 1 # int | Page of paginated response (optional)
per_page = 1 # int | Responses per page (optional)

try: 
    # State Network Sizes
    api_response = api_instance.list_state_network_sizes(state_id, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkSizesApi->list_state_network_sizes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **state_id** | **str**| State code | 
 **page** | **int**| Page of paginated response | [optional] 
 **per_page** | **int**| Responses per page | [optional] 

### Return type

[**StateNetworkSizeResponse**](StateNetworkSizeResponse.md)

### Authorization

[Vericred-Api-Key](../README.md#Vericred-Api-Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

