# coding: utf-8

"""
    Vericred API

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


class RequestProvidersSearch(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, accepts_insurance=None, min_score=None, network_ids=None, page=None, per_page=None, polygon=None, radius=None, search_term=None, sort=None, sort_seed=None, type=None, zip_code=None):
        """
        RequestProvidersSearch - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'accepts_insurance': 'bool',
            'min_score': 'float',
            'network_ids': 'list[int]',
            'page': 'int',
            'per_page': 'int',
            'polygon': 'int',
            'radius': 'int',
            'search_term': 'str',
            'sort': 'str',
            'sort_seed': 'int',
            'type': 'str',
            'zip_code': 'str'
        }

        self.attribute_map = {
            'accepts_insurance': 'accepts_insurance',
            'min_score': 'min_score',
            'network_ids': 'network_ids',
            'page': 'page',
            'per_page': 'per_page',
            'polygon': 'polygon',
            'radius': 'radius',
            'search_term': 'search_term',
            'sort': 'sort',
            'sort_seed': 'sort_seed',
            'type': 'type',
            'zip_code': 'zip_code'
        }

        self._accepts_insurance = accepts_insurance
        self._min_score = min_score
        self._network_ids = network_ids
        self._page = page
        self._per_page = per_page
        self._polygon = polygon
        self._radius = radius
        self._search_term = search_term
        self._sort = sort
        self._sort_seed = sort_seed
        self._type = type
        self._zip_code = zip_code


    @property
    def accepts_insurance(self):
        """
        Gets the accepts_insurance of this RequestProvidersSearch.
        Limit results to Providers who accept at least one insurance         plan.  Note that the inverse of this filter is not supported and         any value will evaluate to true

        :return: The accepts_insurance of this RequestProvidersSearch.
        :rtype: bool
        """
        return self._accepts_insurance

    @accepts_insurance.setter
    def accepts_insurance(self, accepts_insurance):
        """
        Sets the accepts_insurance of this RequestProvidersSearch.
        Limit results to Providers who accept at least one insurance         plan.  Note that the inverse of this filter is not supported and         any value will evaluate to true

        :param accepts_insurance: The accepts_insurance of this RequestProvidersSearch.
        :type: bool
        """

        self._accepts_insurance = accepts_insurance

    @property
    def min_score(self):
        """
        Gets the min_score of this RequestProvidersSearch.
        Minimum search threshold to be included in the results

        :return: The min_score of this RequestProvidersSearch.
        :rtype: float
        """
        return self._min_score

    @min_score.setter
    def min_score(self, min_score):
        """
        Sets the min_score of this RequestProvidersSearch.
        Minimum search threshold to be included in the results

        :param min_score: The min_score of this RequestProvidersSearch.
        :type: float
        """

        self._min_score = min_score

    @property
    def network_ids(self):
        """
        Gets the network_ids of this RequestProvidersSearch.
        List of Vericred network ids

        :return: The network_ids of this RequestProvidersSearch.
        :rtype: list[int]
        """
        return self._network_ids

    @network_ids.setter
    def network_ids(self, network_ids):
        """
        Sets the network_ids of this RequestProvidersSearch.
        List of Vericred network ids

        :param network_ids: The network_ids of this RequestProvidersSearch.
        :type: list[int]
        """

        self._network_ids = network_ids

    @property
    def page(self):
        """
        Gets the page of this RequestProvidersSearch.
        Page number

        :return: The page of this RequestProvidersSearch.
        :rtype: int
        """
        return self._page

    @page.setter
    def page(self, page):
        """
        Sets the page of this RequestProvidersSearch.
        Page number

        :param page: The page of this RequestProvidersSearch.
        :type: int
        """

        self._page = page

    @property
    def per_page(self):
        """
        Gets the per_page of this RequestProvidersSearch.
        Number of records to return per page

        :return: The per_page of this RequestProvidersSearch.
        :rtype: int
        """
        return self._per_page

    @per_page.setter
    def per_page(self, per_page):
        """
        Sets the per_page of this RequestProvidersSearch.
        Number of records to return per page

        :param per_page: The per_page of this RequestProvidersSearch.
        :type: int
        """

        self._per_page = per_page

    @property
    def polygon(self):
        """
        Gets the polygon of this RequestProvidersSearch.
        Define a custom search polygon, mutually exclusive with zip_code search

        :return: The polygon of this RequestProvidersSearch.
        :rtype: int
        """
        return self._polygon

    @polygon.setter
    def polygon(self, polygon):
        """
        Sets the polygon of this RequestProvidersSearch.
        Define a custom search polygon, mutually exclusive with zip_code search

        :param polygon: The polygon of this RequestProvidersSearch.
        :type: int
        """

        self._polygon = polygon

    @property
    def radius(self):
        """
        Gets the radius of this RequestProvidersSearch.
        Radius (in miles) to use to limit results

        :return: The radius of this RequestProvidersSearch.
        :rtype: int
        """
        return self._radius

    @radius.setter
    def radius(self, radius):
        """
        Sets the radius of this RequestProvidersSearch.
        Radius (in miles) to use to limit results

        :param radius: The radius of this RequestProvidersSearch.
        :type: int
        """

        self._radius = radius

    @property
    def search_term(self):
        """
        Gets the search_term of this RequestProvidersSearch.
        String to search by

        :return: The search_term of this RequestProvidersSearch.
        :rtype: str
        """
        return self._search_term

    @search_term.setter
    def search_term(self, search_term):
        """
        Sets the search_term of this RequestProvidersSearch.
        String to search by

        :param search_term: The search_term of this RequestProvidersSearch.
        :type: str
        """

        self._search_term = search_term

    @property
    def sort(self):
        """
        Gets the sort of this RequestProvidersSearch.
        specify sort mode (distance or random)

        :return: The sort of this RequestProvidersSearch.
        :rtype: str
        """
        return self._sort

    @sort.setter
    def sort(self, sort):
        """
        Sets the sort of this RequestProvidersSearch.
        specify sort mode (distance or random)

        :param sort: The sort of this RequestProvidersSearch.
        :type: str
        """

        self._sort = sort

    @property
    def sort_seed(self):
        """
        Gets the sort_seed of this RequestProvidersSearch.
        Seed value for random sort. Randomly-ordered searches with the same seed return results in consistent order.

        :return: The sort_seed of this RequestProvidersSearch.
        :rtype: int
        """
        return self._sort_seed

    @sort_seed.setter
    def sort_seed(self, sort_seed):
        """
        Sets the sort_seed of this RequestProvidersSearch.
        Seed value for random sort. Randomly-ordered searches with the same seed return results in consistent order.

        :param sort_seed: The sort_seed of this RequestProvidersSearch.
        :type: int
        """

        self._sort_seed = sort_seed

    @property
    def type(self):
        """
        Gets the type of this RequestProvidersSearch.
        Either organization or individual

        :return: The type of this RequestProvidersSearch.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this RequestProvidersSearch.
        Either organization or individual

        :param type: The type of this RequestProvidersSearch.
        :type: str
        """

        self._type = type

    @property
    def zip_code(self):
        """
        Gets the zip_code of this RequestProvidersSearch.
        Zip Code to search near

        :return: The zip_code of this RequestProvidersSearch.
        :rtype: str
        """
        return self._zip_code

    @zip_code.setter
    def zip_code(self, zip_code):
        """
        Sets the zip_code of this RequestProvidersSearch.
        Zip Code to search near

        :param zip_code: The zip_code of this RequestProvidersSearch.
        :type: str
        """

        self._zip_code = zip_code

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
