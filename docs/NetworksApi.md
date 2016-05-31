# vericred_client.NetworksApi

All URIs are relative to *https://api.vericred.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_networks**](NetworksApi.md#list_networks) | **GET** /networks | Networks


# **list_networks**
> NetworkSearchResponse list_networks(carrier_id)

Networks

A network is a list of the doctors, other health care providers,
and hospitals that a plan has contracted with to provide medical care to
its members.

### Example 
```python
import time
import vericred_client
from vericred_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vericred_client.NetworksApi()
carrier_id = '33333' # str | Carrier HIOS Issuer ID

try: 
    # Networks
    api_response = api_instance.list_networks(carrier_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling NetworksApi->list_networks: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **carrier_id** | **str**| Carrier HIOS Issuer ID | 

### Return type

[**NetworkSearchResponse**](NetworkSearchResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

