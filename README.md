# vericred_client
Vericred's API allows you to search for Health Plans that a specific doctor
accepts.

## Getting Started

Visit our [Developer Portal](https://vericred.3scale.net) to
create an account.

Once you have created an account, you can create one Application for
Production and another for our Sandbox (select the appropriate Plan when
you create the Application).

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

Most endpoints are not paginated.  It will be noted in the documentation if/when
an endpoint is paginated.

When pagination is present, a `meta` stanza will be present in the response
with the total number of records

```
{
  things: [{ id: 1 }, { id: 2 }],
  meta: { total: 500 }
}
```

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
add the parameters `select=states.name,staes.code`.  The id field of
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



This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 1.0.0
- Package version: 0.0.2
- Build date: 2016-05-31T08:54:08.247-04:00
- Build package: class io.swagger.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/YOUR_GIT_USR_ID/YOUR_GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/YOUR_GIT_USR_ID/YOUR_GIT_REPO_ID.git`)

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
import time
import vericred_client
from vericred_client.rest import ApiException
from pprint import pprint
# create an instance of the API class
api_instance = vericred_client.DrugsApi
ndc_package_code = '12345-4321-11' # str | NDC package code
audience = 'individual' # str | Two-character state code
state_code = 'NY' # str | Two-character state code
vericred_api_key = 'api-doc-key' # str | API Key (optional)

try:
    # Search for DrugCoverages
    api_response = api_instance.get_drug_coverages(ndc_package_code, audience, state_code, vericred_api_key=vericred_api_key)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DrugsApi->get_drug_coverages: %s\n" % e

```

## Documentation for API Endpoints

All URIs are relative to *https://api.vericred.com/*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DrugsApi* | [**get_drug_coverages**](docs/DrugsApi.md#get_drug_coverages) | **GET** /drug_packages/{ndc_package_code}/coverages | Search for DrugCoverages
*DrugsApi* | [**list_drugs**](docs/DrugsApi.md#list_drugs) | **GET** /drugs | Drug Search
*NetworksApi* | [**list_networks**](docs/NetworksApi.md#list_networks) | **GET** /networks | Networks
*PlansApi* | [**find_plans**](docs/PlansApi.md#find_plans) | **POST** /plans/search | Find Plans
*ProvidersApi* | [**get_provider**](docs/ProvidersApi.md#get_provider) | **GET** /providers/{npi} | Find a Provider
*ProvidersApi* | [**get_providers**](docs/ProvidersApi.md#get_providers) | **POST** /providers/search | Find Providers
*ZipCountiesApi* | [**get_zip_counties**](docs/ZipCountiesApi.md#get_zip_counties) | **GET** /zip_counties | Search for Zip Counties


## Documentation For Models

 - [Applicant](docs/Applicant.md)
 - [Base](docs/Base.md)
 - [Carrier](docs/Carrier.md)
 - [CarrierSubsidiary](docs/CarrierSubsidiary.md)
 - [County](docs/County.md)
 - [CountyBulk](docs/CountyBulk.md)
 - [Drug](docs/Drug.md)
 - [DrugCoverage](docs/DrugCoverage.md)
 - [DrugCoverageResponse](docs/DrugCoverageResponse.md)
 - [DrugPackage](docs/DrugPackage.md)
 - [DrugSearchResponse](docs/DrugSearchResponse.md)
 - [Meta](docs/Meta.md)
 - [Network](docs/Network.md)
 - [NetworkSearchResponse](docs/NetworkSearchResponse.md)
 - [Plan](docs/Plan.md)
 - [PlanCounty](docs/PlanCounty.md)
 - [PlanCountyBulk](docs/PlanCountyBulk.md)
 - [PlanSearchResponse](docs/PlanSearchResponse.md)
 - [PlanSearchResult](docs/PlanSearchResult.md)
 - [Pricing](docs/Pricing.md)
 - [Provider](docs/Provider.md)
 - [ProvidersSearchResponse](docs/ProvidersSearchResponse.md)
 - [RatingArea](docs/RatingArea.md)
 - [RequestPlanFind](docs/RequestPlanFind.md)
 - [RequestPlanFindApplicant](docs/RequestPlanFindApplicant.md)
 - [RequestPlanFindProvider](docs/RequestPlanFindProvider.md)
 - [RequestProvidersSearch](docs/RequestProvidersSearch.md)
 - [State](docs/State.md)
 - [ZipCode](docs/ZipCode.md)
 - [ZipCountiesResponse](docs/ZipCountiesResponse.md)
 - [ZipCounty](docs/ZipCounty.md)
 - [ZipCountyBulk](docs/ZipCountyBulk.md)
 - [ZipCountyResponse](docs/ZipCountyResponse.md)


## Documentation For Authorization

 All endpoints do not require authorization.


## Author



