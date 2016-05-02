# vericred_client
Vericred's API allows you to search for Health Plans that a specific doctor
accepts.

## Getting Started

Visit our [Developer Portal](https://vericred.3scale.net/access_code?access_code=vericred&cms_token=3545ca52af07bde85b7c0c3aa9d1985e) to
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

- API version: 
- Package version: 0.0.1
- Build date: 2016-05-02T15:29:54.262-04:00
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
api_instance = vericred_client.DrugCoverageApi
ndc = 'ndc_example' # str | NDC for a drug

try:
    # Find Drug Coverages for a given NDC
    api_response = api_instance.drugs_ndc_coverages_get(ndc)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DrugCoverageApi->drugs_ndc_coverages_get: %s\n" % e

```

## Documentation for API Endpoints

All URIs are relative to *https://api.vericred.com/*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DrugCoverageApi* | [**drugs_ndc_coverages_get**](docs/DrugCoverageApi.md#drugs_ndc_coverages_get) | **GET** /drugs/{ndc}/coverages | Find Drug Coverages for a given NDC
*PlansApi* | [**plans_find_post**](docs/PlansApi.md#plans_find_post) | **POST** /plans/find | Find a set of plans for a Zip Code and County
*ProvidersApi* | [**providers_get**](docs/ProvidersApi.md#providers_get) | **GET** /providers | Find providers by term and zip code
*ProvidersApi* | [**providers_npi_get**](docs/ProvidersApi.md#providers_npi_get) | **GET** /providers/{npi} | Find a specific Provider
*ZipCountiesApi* | [**zip_counties_get**](docs/ZipCountiesApi.md#zip_counties_get) | **GET** /zip_counties | Find Zip Counties by Zip Code


## Documentation For Models

 - [Applicant](docs/Applicant.md)
 - [Carrier](docs/Carrier.md)
 - [CarrierSubsidiary](docs/CarrierSubsidiary.md)
 - [County](docs/County.md)
 - [Drug](docs/Drug.md)
 - [DrugCoverage](docs/DrugCoverage.md)
 - [InlineResponse200](docs/InlineResponse200.md)
 - [InlineResponse2001](docs/InlineResponse2001.md)
 - [InlineResponse2002](docs/InlineResponse2002.md)
 - [Plan](docs/Plan.md)
 - [PlanCounty](docs/PlanCounty.md)
 - [PlanSearchResult](docs/PlanSearchResult.md)
 - [Pricing](docs/Pricing.md)
 - [Provider](docs/Provider.md)
 - [Query](docs/Query.md)
 - [RatingArea](docs/RatingArea.md)
 - [State](docs/State.md)
 - [ZipCode](docs/ZipCode.md)
 - [ZipCounty](docs/ZipCounty.md)


## Documentation For Authorization

 All endpoints do not require authorization.


## Author



