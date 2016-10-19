# vericred_client.DrugPackagesApi

All URIs are relative to *https://api.vericred.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**show_formulary_drug_package_coverage**](DrugPackagesApi.md#show_formulary_drug_package_coverage) | **GET** /formularies/{formulary_id}/drug_packages/{ndc_package_code} | Formulary Drug Package Search


# **show_formulary_drug_package_coverage**
> FormularyDrugPackageResponse show_formulary_drug_package_coverage(formulary_id, ndc_package_code)

Formulary Drug Package Search

Search for coverage by Formulary and DrugPackage ID

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
api_instance = vericred_client.DrugPackagesApi()
formulary_id = '123' # str | ID of the Formulary in question
ndc_package_code = '07777-3105-01' # str | ID of the DrugPackage in question

try: 
    # Formulary Drug Package Search
    api_response = api_instance.show_formulary_drug_package_coverage(formulary_id, ndc_package_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DrugPackagesApi->show_formulary_drug_package_coverage: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **formulary_id** | **str**| ID of the Formulary in question | 
 **ndc_package_code** | **str**| ID of the DrugPackage in question | 

### Return type

[**FormularyDrugPackageResponse**](FormularyDrugPackageResponse.md)

### Authorization

[Vericred-Api-Key](../README.md#Vericred-Api-Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

