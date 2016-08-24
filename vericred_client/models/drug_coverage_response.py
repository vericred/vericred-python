# coding: utf-8

"""
    Vericred API

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



    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from pprint import pformat
from six import iteritems
import re


class DrugCoverageResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, meta=None, drug_coverages=None, drugs=None, drug_packages=None):
        """
        DrugCoverageResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'meta': 'Meta',
            'drug_coverages': 'list[DrugCoverage]',
            'drugs': 'list[Drug]',
            'drug_packages': 'list[DrugPackage]'
        }

        self.attribute_map = {
            'meta': 'meta',
            'drug_coverages': 'drug_coverages',
            'drugs': 'drugs',
            'drug_packages': 'drug_packages'
        }

        self._meta = meta
        self._drug_coverages = drug_coverages
        self._drugs = drugs
        self._drug_packages = drug_packages


    @property
    def meta(self):
        """
        Gets the meta of this DrugCoverageResponse.
        Metadata for query

        :return: The meta of this DrugCoverageResponse.
        :rtype: Meta
        """
        return self._meta

    @meta.setter
    def meta(self, meta):
        """
        Sets the meta of this DrugCoverageResponse.
        Metadata for query

        :param meta: The meta of this DrugCoverageResponse.
        :type: Meta
        """

        self._meta = meta

    @property
    def drug_coverages(self):
        """
        Gets the drug_coverages of this DrugCoverageResponse.
        DrugCoverage search results

        :return: The drug_coverages of this DrugCoverageResponse.
        :rtype: list[DrugCoverage]
        """
        return self._drug_coverages

    @drug_coverages.setter
    def drug_coverages(self, drug_coverages):
        """
        Sets the drug_coverages of this DrugCoverageResponse.
        DrugCoverage search results

        :param drug_coverages: The drug_coverages of this DrugCoverageResponse.
        :type: list[DrugCoverage]
        """

        self._drug_coverages = drug_coverages

    @property
    def drugs(self):
        """
        Gets the drugs of this DrugCoverageResponse.
        Drug

        :return: The drugs of this DrugCoverageResponse.
        :rtype: list[Drug]
        """
        return self._drugs

    @drugs.setter
    def drugs(self, drugs):
        """
        Sets the drugs of this DrugCoverageResponse.
        Drug

        :param drugs: The drugs of this DrugCoverageResponse.
        :type: list[Drug]
        """

        self._drugs = drugs

    @property
    def drug_packages(self):
        """
        Gets the drug_packages of this DrugCoverageResponse.
        Drug Packages

        :return: The drug_packages of this DrugCoverageResponse.
        :rtype: list[DrugPackage]
        """
        return self._drug_packages

    @drug_packages.setter
    def drug_packages(self, drug_packages):
        """
        Sets the drug_packages of this DrugCoverageResponse.
        Drug Packages

        :param drug_packages: The drug_packages of this DrugCoverageResponse.
        :type: list[DrugPackage]
        """

        self._drug_packages = drug_packages

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
