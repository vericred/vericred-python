# vericred_client.PlansApi

All URIs are relative to *https://api.vericred.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**find_plans**](PlansApi.md#find_plans) | **POST** /plans/search | Find Plans


# **find_plans**
> PlanSearchResponse find_plans(body=body)

Find Plans

### Location Information  Searching for a set of plans requires a `zip_code` and `fips_code` code.  These are used to determine pricing and availabity of health plans. This endpoint is paginated.  Optionally, you may provide a list of Applicants or Providers  ### Applicants  This is a list of people who will be covered by the plan.  We use this list to calculate the premium.  You must include `age` and can include `smoker`, which also factors into pricing in some states.  Applicants *must* include an age.  If smoker is omitted, its value is assumed to be false.  #### Multiple Applicants To get pricing for multiple applicants, just append multiple sets of data to the URL with the age and smoking status of each applicant next to each other.  For example, given two applicants - one age 32 and a non-smoker and one age 29 and a smoker, you could use the following request  `GET /plans?zip_code=07451&fips_code=33025&applicants[][age]=32&applicants[][age]=29&applicants[][smoker]=true`  It would also be acceptible to include `applicants[][smoker]=false` after the first applicant's age.  ### Providers  We identify Providers (Doctors) by their National Practitioner Index number (NPI).  If you pass a list of Providers, keyed by their NPI number, we will return a list of which Providers are in and out of network for each plan returned.  For example, if we had two providers with the NPI numbers `12345` and `23456` you would make the following request  `GET /plans?zip_code=07451&fips_code=33025&providers[][npi]=12345&providers[][npi]=23456`  ### Enrollment Date  To calculate plan pricing and availability, we default to the current date as the enrollment date.  To specify a date in the future (or the past), pass a string with the format `YYYY-MM-DD` in the `enrollment_date` parameter.  `GET /plans?zip_code=07451&fips_code=33025&enrollment_date=2016-01-01`  ### Subsidy  On-marketplace plans are eligible for a subsidy based on the `household_size` and `household_income` of the applicants.  If you pass those values, we will calculate the `subsidized_premium` and return it for each plan.  If no values are provided, the `subsidized_premium` will be the same as the `premium`  `GET /plans?zip_code=07451&fips_code=33025&household_size=4&household_income=40000`   ### Sorting  Plans can be sorted by the `premium`, `carrier_name`, `level`, and `plan_type` fields, by either ascending (as `asc`) or descending (as `dsc) sort under the `sort` field.  For example, to sort plans by level, the sort parameter would be `level:asc`. 

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
api_instance = vericred_client.PlansApi()
body = vericred_client.RequestPlanFind() # RequestPlanFind |  (optional)

try: 
    # Find Plans
    api_response = api_instance.find_plans(body=body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling PlansApi->find_plans: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RequestPlanFind**](RequestPlanFind.md)|  | [optional] 

### Return type

[**PlanSearchResponse**](PlanSearchResponse.md)

### Authorization

[Vericred-Api-Key](../README.md#Vericred-Api-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

