# vericred_client.FormulariesApi

All URIs are relative to *https://api.vericred.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_formularies**](FormulariesApi.md#list_formularies) | **GET** /formularies | Formulary Search


# **list_formularies**
> FormularyResponse list_formularies(search_term=search_term, rx_bin=rx_bin, rx_group=rx_group, rx_pcn=rx_pcn)

Formulary Search

Search for drugs by proprietary name

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
api_instance = vericred_client.FormulariesApi()
search_term = 'HIX PPO' # str | Full or partial name of the formulary (optional)
rx_bin = '123456' # str | RX BIN Number (found on an insurance card) (optional)
rx_group = 'HEALTH' # str | RX Group String (found on an insurance card) (optional)
rx_pcn = '9999' # str | RX PCN Number (found on an insurance card) (optional)

try: 
    # Formulary Search
    api_response = api_instance.list_formularies(search_term=search_term, rx_bin=rx_bin, rx_group=rx_group, rx_pcn=rx_pcn)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FormulariesApi->list_formularies: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_term** | **str**| Full or partial name of the formulary | [optional] 
 **rx_bin** | **str**| RX BIN Number (found on an insurance card) | [optional] 
 **rx_group** | **str**| RX Group String (found on an insurance card) | [optional] 
 **rx_pcn** | **str**| RX PCN Number (found on an insurance card) | [optional] 

### Return type

[**FormularyResponse**](FormularyResponse.md)

### Authorization

[Vericred-Api-Key](../README.md#Vericred-Api-Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

