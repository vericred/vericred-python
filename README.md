# vericred_client
Vericred's API allows you to search for Health Plans that a specific doctor
accepts.

## Getting Started

Visit our [Developer Portal](https://developers.vericred.com) to
create an account.

Once you have created an account, you can create one Application for
Production and another for our Sandbox (select the appropriate Plan when
you create the Application).

## SDKs

Our API follows standard REST conventions, so you can use any HTTP client
to integrate with us. You will likely find it easier to use one of our
[autogenerated SDKs](https://github.com/vericred/?query=vericred-),
which we make available for several common programming languages.

## Authentication

To authenticate, pass the API Key you created in the Developer Portal as
a `Vericred-Api-Key` header.

`curl -H 'Vericred-Api-Key: YOUR_KEY' "https://api.vericred.com/providers?search_term=Foo&zip_code=11215"`

## Versioning

Vericred's API default to the latest version.  However, if you need a specific
version, you can request it with an `Accept-Version` header.

The current version is `v3`.  Previous versions are `v1` and `v2`.

`curl -H 'Vericred-Api-Key: YOUR_KEY' -H 'Accept-Version: v2' "https://api.vericred.com/providers?search_term=Foo&zip_code=11215"`

## Pagination

Endpoints that accept `page` and `per_page` parameters are paginated. They expose
four additional fields that contain data about your position in the response,
namely `Total`, `Per-Page`, `Link`, and `Page` as described in [RFC-5988](https://tools.ietf.org/html/rfc5988).

For example, to display 5 results per page and view the second page of a
`GET` to `/networks`, your final request would be `GET /networks?....page=2&per_page=5`.

## Sideloading

When we return multiple levels of an object graph (e.g. `Provider`s and their `State`s
we sideload the associated data.  In this example, we would provide an Array of
`State`s and a `state_id` for each provider.  This is done primarily to reduce the
payload size since many of the `Provider`s will share a `State`

```
{
  providers: [{ id: 1, state_id: 1}, { id: 2, state_id: 1 }],
  states: [{ id: 1, code: 'NY' }]
}
```

If you need the second level of the object graph, you can just match the
corresponding id.

## Selecting specific data

All endpoints allow you to specify which fields you would like to return.
This allows you to limit the response to contain only the data you need.

For example, let's take a request that returns the following JSON by default

```
{
  provider: {
    id: 1,
    name: 'John',
    phone: '1234567890',
    field_we_dont_care_about: 'value_we_dont_care_about'
  },
  states: [{
    id: 1,
    name: 'New York',
    code: 'NY',
    field_we_dont_care_about: 'value_we_dont_care_about'
  }]
}
```

To limit our results to only return the fields we care about, we specify the
`select` query string parameter for the corresponding fields in the JSON
document.

In this case, we want to select `name` and `phone` from the `provider` key,
so we would add the parameters `select=provider.name,provider.phone`.
We also want the `name` and `code` from the `states` key, so we would
add the parameters `select=states.name,states.code`.  The id field of
each document is always returned whether or not it is requested.

Our final request would be `GET /providers/12345?select=provider.name,provider.phone,states.name,states.code`

The response would be

```
{
  provider: {
    id: 1,
    name: 'John',
    phone: '1234567890'
  },
  states: [{
    id: 1,
    name: 'New York',
    code: 'NY'
  }]
}
```

## Benefits summary format
Benefit cost-share strings are formatted to capture:
 * Network tiers
 * Compound or conditional cost-share
 * Limits on the cost-share
 * Benefit-specific maximum out-of-pocket costs

**Example #1**
As an example, we would represent [this Summary of Benefits &amp; Coverage](https://s3.amazonaws.com/vericred-data/SBC/2017/33602TX0780032.pdf) as:

* **Hospital stay facility fees**:
  - Network Provider: `$400 copay/admit plus 20% coinsurance`
  - Out-of-Network Provider: `$1,500 copay/admit plus 50% coinsurance`
  - Vericred's format for this benefit: `In-Network: $400 before deductible then 20% after deductible / Out-of-Network: $1,500 before deductible then 50% after deductible`

* **Rehabilitation services:**
  - Network Provider: `20% coinsurance`
  - Out-of-Network Provider: `50% coinsurance`
  - Limitations & Exceptions: `35 visit maximum per benefit period combined with Chiropractic care.`
  - Vericred's format for this benefit: `In-Network: 20% after deductible / Out-of-Network: 50% after deductible | limit: 35 visit(s) per Benefit Period`

**Example #2**
In [this other Summary of Benefits &amp; Coverage](https://s3.amazonaws.com/vericred-data/SBC/2017/40733CA0110568.pdf), the **specialty_drugs** cost-share has a maximum out-of-pocket for in-network pharmacies.
* **Specialty drugs:**
  - Network Provider: `40% coinsurance up to a $500 maximum for up to a 30 day supply`
  - Out-of-Network Provider `Not covered`
  - Vericred's format for this benefit: `In-Network: 40% after deductible, up to $500 per script / Out-of-Network: 100%`

**BNF**

Here's a description of the benefits summary string, represented as a context-free grammar:

```
root                      ::= coverage

coverage                  ::= (simple_coverage | tiered_coverage) (space pipe space coverage_modifier)?
tiered_coverage           ::= tier (space slash space tier)*
tier                      ::= tier_name colon space (tier_coverage | not_applicable)
tier_coverage             ::= simple_coverage (space (then | or | and) space simple_coverage)* tier_limitation?
simple_coverage           ::= (pre_coverage_limitation space)? coverage_amount (space post_coverage_limitation)? (comma? space coverage_condition)?
coverage_modifier         ::= limit_condition colon space (((simple_coverage | simple_limitation) (semicolon space see_carrier_documentation)?) | see_carrier_documentation | waived_if_admitted | shared_across_tiers)
waived_if_admitted        ::= ("copay" space)? "waived if admitted"
simple_limitation         ::= pre_coverage_limitation space "copay applies"
tier_name                 ::= "In-Network-Tier-2" | "Out-of-Network" | "In-Network"
limit_condition           ::= "limit" | "condition"
tier_limitation           ::= comma space "up to" space (currency | (integer space time_unit plural?)) (space post_coverage_limitation)?
coverage_amount           ::= currency | unlimited | included | unknown | percentage | (digits space (treatment_unit | time_unit) plural?)
pre_coverage_limitation   ::= first space digits space time_unit plural?
post_coverage_limitation  ::= (((then space currency) | "per condition") space)? "per" space (treatment_unit | (integer space time_unit) | time_unit) plural?
coverage_condition        ::= ("before deductible" | "after deductible" | "penalty" | allowance | "in-state" | "out-of-state") (space allowance)?
allowance                 ::= upto_allowance | after_allowance
upto_allowance            ::= "up to" space (currency space)? "allowance"
after_allowance           ::= "after" space (currency space)? "allowance"
see_carrier_documentation ::= "see carrier documentation for more information"
shared_across_tiers       ::= "shared across all tiers"
unknown                   ::= "unknown"
unlimited                 ::= /[uU]nlimited/
included                  ::= /[iI]ncluded in [mM]edical/
time_unit                 ::= /[hH]our/ | (((/[cC]alendar/ | /[cC]ontract/) space)? /[yY]ear/) | /[mM]onth/ | /[dD]ay/ | /[wW]eek/ | /[vV]isit/ | /[lL]ifetime/ | ((((/[bB]enefit/ plural?) | /[eE]ligibility/) space)? /[pP]eriod/)
treatment_unit            ::= /[pP]erson/ | /[gG]roup/ | /[cC]ondition/ | /[sS]cript/ | /[vV]isit/ | /[eE]xam/ | /[iI]tem/ | /[sS]tay/ | /[tT]reatment/ | /[aA]dmission/ | /[eE]pisode/
comma                     ::= ","
colon                     ::= ":"
semicolon                 ::= ";"
pipe                      ::= "|"
slash                     ::= "/"
plural                    ::= "(s)" | "s"
then                      ::= "then" | ("," space) | space
or                        ::= "or"
and                       ::= "and"
not_applicable            ::= "Not Applicable" | "N/A" | "NA"
first                     ::= "first"
currency                  ::= "$" number
percentage                ::= number "%"
number                    ::= float | integer
float                     ::= digits "." digits
integer                   ::= /[0-9]/+ (comma_int | under_int)*
comma_int                 ::= ("," /[0-9]/*3) !"_"
under_int                 ::= ("_" /[0-9]/*3) !","
digits                    ::= /[0-9]/+ ("_" /[0-9]/+)*
space                     ::= /[ \t]/+
```



This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 1.0.0
- Package version: 0.0.11
- Build package: class io.swagger.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import vericred_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import vericred_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import vericred_client
from vericred_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Vericred-Api-Key
vericred_client.configuration.api_key['Vericred-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# vericred_client.configuration.api_key_prefix['Vericred-Api-Key'] = 'Bearer'
# create an instance of the API class
api_instance = vericred_client.DrugCoveragesApi
ndc_package_code = '07777-3105-01' # str | NDC package code
audience = 'individual' # str | Plan Audience (individual or small_group)
state_code = 'CA' # str | Two-character state code

try:
    # Search for DrugCoverages
    api_response = api_instance.get_drug_coverages(ndc_package_code, audience, state_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DrugCoveragesApi->get_drug_coverages: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://api.vericred.com/*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DrugCoveragesApi* | [**get_drug_coverages**](docs/DrugCoveragesApi.md#get_drug_coverages) | **GET** /drug_packages/{ndc_package_code}/coverages | Search for DrugCoverages
*DrugPackagesApi* | [**show_formulary_drug_package_coverage**](docs/DrugPackagesApi.md#show_formulary_drug_package_coverage) | **GET** /formularies/{formulary_id}/drug_packages/{ndc_package_code} | Formulary Drug Package Search
*DrugsApi* | [**list_drugs**](docs/DrugsApi.md#list_drugs) | **GET** /drugs | Drug Search
*FormulariesApi* | [**list_formularies**](docs/FormulariesApi.md#list_formularies) | **GET** /formularies | Formulary Search
*NetworkSizesApi* | [**list_state_network_sizes**](docs/NetworkSizesApi.md#list_state_network_sizes) | **GET** /states/{state_id}/network_sizes | State Network Sizes
*NetworkSizesApi* | [**search_network_sizes**](docs/NetworkSizesApi.md#search_network_sizes) | **POST** /network_sizes/search | Network Sizes
*NetworksApi* | [**create_network_comparisons**](docs/NetworksApi.md#create_network_comparisons) | **POST** /networks/{id}/network_comparisons | Network Comparisons
*NetworksApi* | [**list_networks**](docs/NetworksApi.md#list_networks) | **GET** /networks | Networks
*NetworksApi* | [**show_network**](docs/NetworksApi.md#show_network) | **GET** /networks/{id} | Network Details
*PlansApi* | [**find_plans**](docs/PlansApi.md#find_plans) | **POST** /plans/search | Find Plans
*PlansApi* | [**show_plan**](docs/PlansApi.md#show_plan) | **GET** /plans/{id} | Show Plan
*ProviderNotificationSubscriptionsApi* | [**create_provider_notification_subscription**](docs/ProviderNotificationSubscriptionsApi.md#create_provider_notification_subscription) | **POST** /providers/subscription | Subscribe
*ProviderNotificationSubscriptionsApi* | [**delete_provider_notification_subscription**](docs/ProviderNotificationSubscriptionsApi.md#delete_provider_notification_subscription) | **DELETE** /providers/subscription/{nonce} | Unsubscribe
*ProviderNotificationSubscriptionsApi* | [**notify_provider_notification_subscription**](docs/ProviderNotificationSubscriptionsApi.md#notify_provider_notification_subscription) | **POST** /CALLBACK_URL | Webhook
*ProvidersApi* | [**get_provider**](docs/ProvidersApi.md#get_provider) | **GET** /providers/{npi} | Find a Provider
*ProvidersApi* | [**get_providers**](docs/ProvidersApi.md#get_providers) | **POST** /providers/search | Find Providers
*ProvidersApi* | [**get_providers_0**](docs/ProvidersApi.md#get_providers_0) | **POST** /providers/search/geocode | Find Providers
*ZipCountiesApi* | [**get_zip_counties**](docs/ZipCountiesApi.md#get_zip_counties) | **GET** /zip_counties | Search for Zip Counties
*ZipCountiesApi* | [**show_zip_county**](docs/ZipCountiesApi.md#show_zip_county) | **GET** /zip_counties/{id} | Show an individual ZipCounty


## Documentation For Models

 - [ACAPlan](docs/ACAPlan.md)
 - [ACAPlan2018](docs/ACAPlan2018.md)
 - [ACAPlan2018SearchResponse](docs/ACAPlan2018SearchResponse.md)
 - [ACAPlan2018SearchResult](docs/ACAPlan2018SearchResult.md)
 - [ACAPlan2018ShowResponse](docs/ACAPlan2018ShowResponse.md)
 - [ACAPlanPre2018](docs/ACAPlanPre2018.md)
 - [ACAPlanPre2018SearchResponse](docs/ACAPlanPre2018SearchResponse.md)
 - [ACAPlanPre2018SearchResult](docs/ACAPlanPre2018SearchResult.md)
 - [ACAPlanPre2018ShowResponse](docs/ACAPlanPre2018ShowResponse.md)
 - [Applicant](docs/Applicant.md)
 - [Base](docs/Base.md)
 - [BasePlanSearchResponse](docs/BasePlanSearchResponse.md)
 - [Carrier](docs/Carrier.md)
 - [CarrierSubsidiary](docs/CarrierSubsidiary.md)
 - [County](docs/County.md)
 - [CountyBulk](docs/CountyBulk.md)
 - [Drug](docs/Drug.md)
 - [DrugCoverage](docs/DrugCoverage.md)
 - [DrugCoverageResponse](docs/DrugCoverageResponse.md)
 - [DrugPackage](docs/DrugPackage.md)
 - [DrugSearchResponse](docs/DrugSearchResponse.md)
 - [Formulary](docs/Formulary.md)
 - [FormularyDrugPackageResponse](docs/FormularyDrugPackageResponse.md)
 - [FormularyResponse](docs/FormularyResponse.md)
 - [Meta](docs/Meta.md)
 - [MetaPlanSearchResponse](docs/MetaPlanSearchResponse.md)
 - [Network](docs/Network.md)
 - [NetworkComparison](docs/NetworkComparison.md)
 - [NetworkComparisonRequest](docs/NetworkComparisonRequest.md)
 - [NetworkComparisonResponse](docs/NetworkComparisonResponse.md)
 - [NetworkDetails](docs/NetworkDetails.md)
 - [NetworkDetailsResponse](docs/NetworkDetailsResponse.md)
 - [NetworkSearchResponse](docs/NetworkSearchResponse.md)
 - [NetworkSize](docs/NetworkSize.md)
 - [NotificationSubscription](docs/NotificationSubscription.md)
 - [NotificationSubscriptionResponse](docs/NotificationSubscriptionResponse.md)
 - [Plan](docs/Plan.md)
 - [PlanCounty](docs/PlanCounty.md)
 - [PlanCountyBulk](docs/PlanCountyBulk.md)
 - [PlanDeleted](docs/PlanDeleted.md)
 - [PlanIdentifier](docs/PlanIdentifier.md)
 - [PlanMedicare](docs/PlanMedicare.md)
 - [PlanMedicareBulk](docs/PlanMedicareBulk.md)
 - [PlanPricingMedicare](docs/PlanPricingMedicare.md)
 - [PlanSearchResponse](docs/PlanSearchResponse.md)
 - [PlanShowResponse](docs/PlanShowResponse.md)
 - [Provider](docs/Provider.md)
 - [ProviderDetails](docs/ProviderDetails.md)
 - [ProviderGeocode](docs/ProviderGeocode.md)
 - [ProviderNetworkEventNotification](docs/ProviderNetworkEventNotification.md)
 - [ProviderShowResponse](docs/ProviderShowResponse.md)
 - [ProvidersGeocodeResponse](docs/ProvidersGeocodeResponse.md)
 - [ProvidersSearchResponse](docs/ProvidersSearchResponse.md)
 - [RatingArea](docs/RatingArea.md)
 - [RequestPlanFind](docs/RequestPlanFind.md)
 - [RequestPlanFindApplicant](docs/RequestPlanFindApplicant.md)
 - [RequestPlanFindDrugPackage](docs/RequestPlanFindDrugPackage.md)
 - [RequestPlanFindProvider](docs/RequestPlanFindProvider.md)
 - [RequestProviderNotificationSubscription](docs/RequestProviderNotificationSubscription.md)
 - [RequestProvidersSearch](docs/RequestProvidersSearch.md)
 - [RxCuiIdentifier](docs/RxCuiIdentifier.md)
 - [RxCuiIdentifierSearchResponse](docs/RxCuiIdentifierSearchResponse.md)
 - [ServiceArea](docs/ServiceArea.md)
 - [ServiceAreaZipCounty](docs/ServiceAreaZipCounty.md)
 - [State](docs/State.md)
 - [StateNetworkSizeRequest](docs/StateNetworkSizeRequest.md)
 - [StateNetworkSizeResponse](docs/StateNetworkSizeResponse.md)
 - [ZipCode](docs/ZipCode.md)
 - [ZipCountiesResponse](docs/ZipCountiesResponse.md)
 - [ZipCounty](docs/ZipCounty.md)
 - [ZipCountyBulk](docs/ZipCountyBulk.md)
 - [ZipCountyResponse](docs/ZipCountyResponse.md)


## Documentation For Authorization


## Vericred-Api-Key

- **Type**: API key
- **API key parameter name**: Vericred-Api-Key
- **Location**: HTTP header


## Author



