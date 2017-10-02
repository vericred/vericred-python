# vericred_client.NetworksApi

All URIs are relative to *https://api.vericred.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_network_comparisons**](NetworksApi.md#create_network_comparisons) | **POST** /networks/{id}/network_comparisons | Network Comparisons
[**list_networks**](NetworksApi.md#list_networks) | **GET** /networks | Networks
[**show_network**](NetworksApi.md#show_network) | **GET** /networks/{id} | Network Details


# **create_network_comparisons**
> NetworkComparisonResponse create_network_comparisons(id, body)

Network Comparisons

Compare provider counts in a given area between a base network and one or more comparison networks.  #### Comparing Networks Comparison of provider counts within a radius requires that you provide a `zip_code` and `radius` to use as a search area.  The response returns the total number of unique `Providers` in the Base `Network` (i.e. those who are not present in the Comparison `Network`), The number of unique `Provider`s in the Comparison `Network` (i.e. those who are not present in the Base `Network`), and the count of `Provider`s who are in *both* `Network`s

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
api_instance = vericred_client.NetworksApi()
id = 100001 # int | Primary key of the base network
body = vericred_client.NetworkComparisonRequest() # NetworkComparisonRequest | 

try: 
    # Network Comparisons
    api_response = api_instance.create_network_comparisons(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworksApi->create_network_comparisons: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Primary key of the base network | 
 **body** | [**NetworkComparisonRequest**](NetworkComparisonRequest.md)|  | 

### Return type

[**NetworkComparisonResponse**](NetworkComparisonResponse.md)

### Authorization

[Vericred-Api-Key](../README.md#Vericred-Api-Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_networks**
> NetworkSearchResponse list_networks(carrier_id, page=page, per_page=per_page)

Networks

A network is a list of the doctors, other health care providers, and hospitals that a plan has contracted with to provide medical care to its members. This endpoint is paginated.

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
api_instance = vericred_client.NetworksApi()
carrier_id = '33333' # str | Carrier HIOS Issuer ID
page = 1 # int | Page of paginated response (optional)
per_page = 1 # int | Responses per page (optional)

try: 
    # Networks
    api_response = api_instance.list_networks(carrier_id, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworksApi->list_networks: %s\n" % e)
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

# **show_network**
> NetworkDetailsResponse show_network(id)

Network Details

A network is a list of the doctors, other health care providers, and hospitals that a plan has contracted with to provide medical care to its members.

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
api_instance = vericred_client.NetworksApi()
id = 100001 # int | Primary key of the network

try: 
    # Network Details
    api_response = api_instance.show_network(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworksApi->show_network: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Primary key of the network | 

### Return type

[**NetworkDetailsResponse**](NetworkDetailsResponse.md)

### Authorization

[Vericred-Api-Key](../README.md#Vericred-Api-Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

