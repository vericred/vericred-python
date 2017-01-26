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
<cost-share>     ::= <tier> <opt-num-prefix> <value> <opt-per-unit> <deductible> <tier-limit> "/" <tier> <opt-num-prefix> <value> <opt-per-unit> <deductible> "|" <benefit-limit>
<tier>           ::= "In-Network:" | "In-Network-Tier-2:" | "Out-of-Network:"
<opt-num-prefix> ::= "first" <num> <unit> | ""
<unit>           ::= "day(s)" | "visit(s)" | "exam(s)" | "item(s)"
<value>          ::= <ddct_moop> | <copay> | <coinsurance> | <compound> | "unknown" | "Not Applicable"
<compound>       ::= <copay> <deductible> "then" <coinsurance> <deductible> | <copay> <deductible> "then" <copay> <deductible> | <coinsurance> <deductible> "then" <coinsurance> <deductible>
<copay>          ::= "$" <num>
<coinsurace>     ::= <num> "%"
<ddct_moop>      ::= <copay> | "Included in Medical" | "Unlimited"
<opt-per-unit>   ::= "per day" | "per visit" | "per stay" | ""
<deductible>     ::= "before deductible" | "after deductible" | ""
<tier-limit>     ::= ", " <limit> | ""
<benefit-limit>  ::= <limit> | ""
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


class Pricing(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, age=None, effective_date=None, expiration_date=None, plan_id=None, premium_child_only=None, premium_family=None, premium_single=None, premium_single_and_children=None, premium_single_and_spouse=None, premium_single_smoker=None, rating_area_id=None, premium_source=None, updated_at=None):
        """
        Pricing - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'age': 'int',
            'effective_date': 'date',
            'expiration_date': 'date',
            'plan_id': 'int',
            'premium_child_only': 'float',
            'premium_family': 'float',
            'premium_single': 'float',
            'premium_single_and_children': 'float',
            'premium_single_and_spouse': 'float',
            'premium_single_smoker': 'float',
            'rating_area_id': 'str',
            'premium_source': 'str',
            'updated_at': 'str'
        }

        self.attribute_map = {
            'age': 'age',
            'effective_date': 'effective_date',
            'expiration_date': 'expiration_date',
            'plan_id': 'plan_id',
            'premium_child_only': 'premium_child_only',
            'premium_family': 'premium_family',
            'premium_single': 'premium_single',
            'premium_single_and_children': 'premium_single_and_children',
            'premium_single_and_spouse': 'premium_single_and_spouse',
            'premium_single_smoker': 'premium_single_smoker',
            'rating_area_id': 'rating_area_id',
            'premium_source': 'premium_source',
            'updated_at': 'updated_at'
        }

        self._age = age
        self._effective_date = effective_date
        self._expiration_date = expiration_date
        self._plan_id = plan_id
        self._premium_child_only = premium_child_only
        self._premium_family = premium_family
        self._premium_single = premium_single
        self._premium_single_and_children = premium_single_and_children
        self._premium_single_and_spouse = premium_single_and_spouse
        self._premium_single_smoker = premium_single_smoker
        self._rating_area_id = rating_area_id
        self._premium_source = premium_source
        self._updated_at = updated_at


    @property
    def age(self):
        """
        Gets the age of this Pricing.
        Age of applicant

        :return: The age of this Pricing.
        :rtype: int
        """
        return self._age

    @age.setter
    def age(self, age):
        """
        Sets the age of this Pricing.
        Age of applicant

        :param age: The age of this Pricing.
        :type: int
        """

        self._age = age

    @property
    def effective_date(self):
        """
        Gets the effective_date of this Pricing.
        Effective date of plan

        :return: The effective_date of this Pricing.
        :rtype: date
        """
        return self._effective_date

    @effective_date.setter
    def effective_date(self, effective_date):
        """
        Sets the effective_date of this Pricing.
        Effective date of plan

        :param effective_date: The effective_date of this Pricing.
        :type: date
        """

        self._effective_date = effective_date

    @property
    def expiration_date(self):
        """
        Gets the expiration_date of this Pricing.
        Plan expiration date

        :return: The expiration_date of this Pricing.
        :rtype: date
        """
        return self._expiration_date

    @expiration_date.setter
    def expiration_date(self, expiration_date):
        """
        Sets the expiration_date of this Pricing.
        Plan expiration date

        :param expiration_date: The expiration_date of this Pricing.
        :type: date
        """

        self._expiration_date = expiration_date

    @property
    def plan_id(self):
        """
        Gets the plan_id of this Pricing.
        Foreign key to plans

        :return: The plan_id of this Pricing.
        :rtype: int
        """
        return self._plan_id

    @plan_id.setter
    def plan_id(self, plan_id):
        """
        Sets the plan_id of this Pricing.
        Foreign key to plans

        :param plan_id: The plan_id of this Pricing.
        :type: int
        """

        self._plan_id = plan_id

    @property
    def premium_child_only(self):
        """
        Gets the premium_child_only of this Pricing.
        Child-only premium

        :return: The premium_child_only of this Pricing.
        :rtype: float
        """
        return self._premium_child_only

    @premium_child_only.setter
    def premium_child_only(self, premium_child_only):
        """
        Sets the premium_child_only of this Pricing.
        Child-only premium

        :param premium_child_only: The premium_child_only of this Pricing.
        :type: float
        """

        self._premium_child_only = premium_child_only

    @property
    def premium_family(self):
        """
        Gets the premium_family of this Pricing.
        Family premium

        :return: The premium_family of this Pricing.
        :rtype: float
        """
        return self._premium_family

    @premium_family.setter
    def premium_family(self, premium_family):
        """
        Sets the premium_family of this Pricing.
        Family premium

        :param premium_family: The premium_family of this Pricing.
        :type: float
        """

        self._premium_family = premium_family

    @property
    def premium_single(self):
        """
        Gets the premium_single of this Pricing.
        Single-person premium

        :return: The premium_single of this Pricing.
        :rtype: float
        """
        return self._premium_single

    @premium_single.setter
    def premium_single(self, premium_single):
        """
        Sets the premium_single of this Pricing.
        Single-person premium

        :param premium_single: The premium_single of this Pricing.
        :type: float
        """

        self._premium_single = premium_single

    @property
    def premium_single_and_children(self):
        """
        Gets the premium_single_and_children of this Pricing.
        Single person including children premium

        :return: The premium_single_and_children of this Pricing.
        :rtype: float
        """
        return self._premium_single_and_children

    @premium_single_and_children.setter
    def premium_single_and_children(self, premium_single_and_children):
        """
        Sets the premium_single_and_children of this Pricing.
        Single person including children premium

        :param premium_single_and_children: The premium_single_and_children of this Pricing.
        :type: float
        """

        self._premium_single_and_children = premium_single_and_children

    @property
    def premium_single_and_spouse(self):
        """
        Gets the premium_single_and_spouse of this Pricing.
        Person with spouse premium

        :return: The premium_single_and_spouse of this Pricing.
        :rtype: float
        """
        return self._premium_single_and_spouse

    @premium_single_and_spouse.setter
    def premium_single_and_spouse(self, premium_single_and_spouse):
        """
        Sets the premium_single_and_spouse of this Pricing.
        Person with spouse premium

        :param premium_single_and_spouse: The premium_single_and_spouse of this Pricing.
        :type: float
        """

        self._premium_single_and_spouse = premium_single_and_spouse

    @property
    def premium_single_smoker(self):
        """
        Gets the premium_single_smoker of this Pricing.
        Premium for single smoker

        :return: The premium_single_smoker of this Pricing.
        :rtype: float
        """
        return self._premium_single_smoker

    @premium_single_smoker.setter
    def premium_single_smoker(self, premium_single_smoker):
        """
        Sets the premium_single_smoker of this Pricing.
        Premium for single smoker

        :param premium_single_smoker: The premium_single_smoker of this Pricing.
        :type: float
        """

        self._premium_single_smoker = premium_single_smoker

    @property
    def rating_area_id(self):
        """
        Gets the rating_area_id of this Pricing.
        Foreign key to rating areas

        :return: The rating_area_id of this Pricing.
        :rtype: str
        """
        return self._rating_area_id

    @rating_area_id.setter
    def rating_area_id(self, rating_area_id):
        """
        Sets the rating_area_id of this Pricing.
        Foreign key to rating areas

        :param rating_area_id: The rating_area_id of this Pricing.
        :type: str
        """

        self._rating_area_id = rating_area_id

    @property
    def premium_source(self):
        """
        Gets the premium_source of this Pricing.
        Where was this pricing data extracted from?

        :return: The premium_source of this Pricing.
        :rtype: str
        """
        return self._premium_source

    @premium_source.setter
    def premium_source(self, premium_source):
        """
        Sets the premium_source of this Pricing.
        Where was this pricing data extracted from?

        :param premium_source: The premium_source of this Pricing.
        :type: str
        """

        self._premium_source = premium_source

    @property
    def updated_at(self):
        """
        Gets the updated_at of this Pricing.
        Time when pricing was last updated

        :return: The updated_at of this Pricing.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """
        Sets the updated_at of this Pricing.
        Time when pricing was last updated

        :param updated_at: The updated_at of this Pricing.
        :type: str
        """

        self._updated_at = updated_at

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
