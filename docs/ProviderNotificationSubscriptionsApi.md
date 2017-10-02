# vericred_client.ProviderNotificationSubscriptionsApi

All URIs are relative to *https://api.vericred.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_provider_notification_subscription**](ProviderNotificationSubscriptionsApi.md#create_provider_notification_subscription) | **POST** /providers/subscription | Subscribe
[**delete_provider_notification_subscription**](ProviderNotificationSubscriptionsApi.md#delete_provider_notification_subscription) | **DELETE** /providers/subscription/{nonce} | Unsubscribe
[**notify_provider_notification_subscription**](ProviderNotificationSubscriptionsApi.md#notify_provider_notification_subscription) | **POST** /CALLBACK_URL | Webhook


# **create_provider_notification_subscription**
> NotificationSubscriptionResponse create_provider_notification_subscription(root=root)

Subscribe

Subscribe to receive webhook notifications when providers join or leave a network.  The request must include a list of National Provider Index (NPI) numbers for providers, a callback URL where notifications should be sent, and either a plan ID or a network ID. The response will include a `nonce` value. The `nonce` will be included in all webhook notifications originating from this subscription and will be used as the identifier for all subsequent requests.  The `network_id` and `plan_id` are mutually exclusive. The request must include a value for one of the fields, but cannot include both.  Examples of valid request bodies are as follows:  ``` {   \"npis\": [\"2712589\", \"8498549\", \"19528190\"],   \"plan_id\": 1,   \"callback_url\": \"https://example.com/webhook\" }  ```  ``` {   \"npis\": [\"2712589\", \"8498549\", \"19528190\"],   \"network_id\": 1,   \"callback_url\": \"https://example.com/webhook\" }  ```

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
api_instance = vericred_client.ProviderNotificationSubscriptionsApi()
root = vericred_client.RequestProviderNotificationSubscription() # RequestProviderNotificationSubscription |  (optional)

try: 
    # Subscribe
    api_response = api_instance.create_provider_notification_subscription(root=root)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProviderNotificationSubscriptionsApi->create_provider_notification_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **root** | [**RequestProviderNotificationSubscription**](RequestProviderNotificationSubscription.md)|  | [optional] 

### Return type

[**NotificationSubscriptionResponse**](NotificationSubscriptionResponse.md)

### Authorization

[Vericred-Api-Key](../README.md#Vericred-Api-Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_provider_notification_subscription**
> delete_provider_notification_subscription(nonce)

Unsubscribe

Unsubscribe from an existing webhook notification.

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
api_instance = vericred_client.ProviderNotificationSubscriptionsApi()
nonce = '7d28bda02e69ca1ebfdfe628a9bb2d4f' # str | The nonce value that was included in the response when the subscription was created

try: 
    # Unsubscribe
    api_instance.delete_provider_notification_subscription(nonce)
except ApiException as e:
    print("Exception when calling ProviderNotificationSubscriptionsApi->delete_provider_notification_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nonce** | **str**| The nonce value that was included in the response when the subscription was created | 

### Return type

void (empty response body)

### Authorization

[Vericred-Api-Key](../README.md#Vericred-Api-Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **notify_provider_notification_subscription**
> notify_provider_notification_subscription(root=root)

Webhook

Webhook notifications are sent when there are events relevant to a subscription. Notifications will be sent to the callback URL that was provided in the original request.  The endpoint handling this request should respond with a successful status code (200 <= Status Code < 300). If a successful status code is not returned the notification will be sent again at a regular interval.

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
api_instance = vericred_client.ProviderNotificationSubscriptionsApi()
root = vericred_client.ProviderNetworkEventNotification() # ProviderNetworkEventNotification |  (optional)

try: 
    # Webhook
    api_instance.notify_provider_notification_subscription(root=root)
except ApiException as e:
    print("Exception when calling ProviderNotificationSubscriptionsApi->notify_provider_notification_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **root** | [**ProviderNetworkEventNotification**](ProviderNetworkEventNotification.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[Vericred-Api-Key](../README.md#Vericred-Api-Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

