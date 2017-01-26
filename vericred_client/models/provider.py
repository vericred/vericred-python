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


class Provider(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, city=None, email=None, gender=None, first_name=None, id=None, last_name=None, latitude=None, longitude=None, middle_name=None, network_ids=None, organization_name=None, personal_phone=None, phone=None, presentation_name=None, specialty=None, state=None, state_id=None, street_line_1=None, street_line_2=None, suffix=None, title=None, type=None, zip_code=None):
        """
        Provider - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'city': 'str',
            'email': 'str',
            'gender': 'str',
            'first_name': 'str',
            'id': 'int',
            'last_name': 'str',
            'latitude': 'float',
            'longitude': 'float',
            'middle_name': 'str',
            'network_ids': 'list[int]',
            'organization_name': 'str',
            'personal_phone': 'str',
            'phone': 'str',
            'presentation_name': 'str',
            'specialty': 'str',
            'state': 'str',
            'state_id': 'int',
            'street_line_1': 'str',
            'street_line_2': 'str',
            'suffix': 'str',
            'title': 'str',
            'type': 'str',
            'zip_code': 'str'
        }

        self.attribute_map = {
            'city': 'city',
            'email': 'email',
            'gender': 'gender',
            'first_name': 'first_name',
            'id': 'id',
            'last_name': 'last_name',
            'latitude': 'latitude',
            'longitude': 'longitude',
            'middle_name': 'middle_name',
            'network_ids': 'network_ids',
            'organization_name': 'organization_name',
            'personal_phone': 'personal_phone',
            'phone': 'phone',
            'presentation_name': 'presentation_name',
            'specialty': 'specialty',
            'state': 'state',
            'state_id': 'state_id',
            'street_line_1': 'street_line_1',
            'street_line_2': 'street_line_2',
            'suffix': 'suffix',
            'title': 'title',
            'type': 'type',
            'zip_code': 'zip_code'
        }

        self._city = city
        self._email = email
        self._gender = gender
        self._first_name = first_name
        self._id = id
        self._last_name = last_name
        self._latitude = latitude
        self._longitude = longitude
        self._middle_name = middle_name
        self._network_ids = network_ids
        self._organization_name = organization_name
        self._personal_phone = personal_phone
        self._phone = phone
        self._presentation_name = presentation_name
        self._specialty = specialty
        self._state = state
        self._state_id = state_id
        self._street_line_1 = street_line_1
        self._street_line_2 = street_line_2
        self._suffix = suffix
        self._title = title
        self._type = type
        self._zip_code = zip_code


    @property
    def city(self):
        """
        Gets the city of this Provider.
        City name (e.g. Springfield).

        :return: The city of this Provider.
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """
        Sets the city of this Provider.
        City name (e.g. Springfield).

        :param city: The city of this Provider.
        :type: str
        """

        self._city = city

    @property
    def email(self):
        """
        Gets the email of this Provider.
        Primary email address to contact the provider.

        :return: The email of this Provider.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """
        Sets the email of this Provider.
        Primary email address to contact the provider.

        :param email: The email of this Provider.
        :type: str
        """

        self._email = email

    @property
    def gender(self):
        """
        Gets the gender of this Provider.
        Provider's gender (M or F)

        :return: The gender of this Provider.
        :rtype: str
        """
        return self._gender

    @gender.setter
    def gender(self, gender):
        """
        Sets the gender of this Provider.
        Provider's gender (M or F)

        :param gender: The gender of this Provider.
        :type: str
        """

        self._gender = gender

    @property
    def first_name(self):
        """
        Gets the first_name of this Provider.
        Given name for the provider.

        :return: The first_name of this Provider.
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """
        Sets the first_name of this Provider.
        Given name for the provider.

        :param first_name: The first_name of this Provider.
        :type: str
        """

        self._first_name = first_name

    @property
    def id(self):
        """
        Gets the id of this Provider.
        National Provider Index (NPI) number

        :return: The id of this Provider.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Provider.
        National Provider Index (NPI) number

        :param id: The id of this Provider.
        :type: int
        """

        self._id = id

    @property
    def last_name(self):
        """
        Gets the last_name of this Provider.
        Family name for the provider.

        :return: The last_name of this Provider.
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """
        Sets the last_name of this Provider.
        Family name for the provider.

        :param last_name: The last_name of this Provider.
        :type: str
        """

        self._last_name = last_name

    @property
    def latitude(self):
        """
        Gets the latitude of this Provider.
        Latitude of provider

        :return: The latitude of this Provider.
        :rtype: float
        """
        return self._latitude

    @latitude.setter
    def latitude(self, latitude):
        """
        Sets the latitude of this Provider.
        Latitude of provider

        :param latitude: The latitude of this Provider.
        :type: float
        """

        self._latitude = latitude

    @property
    def longitude(self):
        """
        Gets the longitude of this Provider.
        Longitude of provider

        :return: The longitude of this Provider.
        :rtype: float
        """
        return self._longitude

    @longitude.setter
    def longitude(self, longitude):
        """
        Sets the longitude of this Provider.
        Longitude of provider

        :param longitude: The longitude of this Provider.
        :type: float
        """

        self._longitude = longitude

    @property
    def middle_name(self):
        """
        Gets the middle_name of this Provider.
        Middle name for the provider.

        :return: The middle_name of this Provider.
        :rtype: str
        """
        return self._middle_name

    @middle_name.setter
    def middle_name(self, middle_name):
        """
        Sets the middle_name of this Provider.
        Middle name for the provider.

        :param middle_name: The middle_name of this Provider.
        :type: str
        """

        self._middle_name = middle_name

    @property
    def network_ids(self):
        """
        Gets the network_ids of this Provider.
        Array of network ids

        :return: The network_ids of this Provider.
        :rtype: list[int]
        """
        return self._network_ids

    @network_ids.setter
    def network_ids(self, network_ids):
        """
        Sets the network_ids of this Provider.
        Array of network ids

        :param network_ids: The network_ids of this Provider.
        :type: list[int]
        """

        self._network_ids = network_ids

    @property
    def organization_name(self):
        """
        Gets the organization_name of this Provider.
        name for the providers of type: organization.

        :return: The organization_name of this Provider.
        :rtype: str
        """
        return self._organization_name

    @organization_name.setter
    def organization_name(self, organization_name):
        """
        Sets the organization_name of this Provider.
        name for the providers of type: organization.

        :param organization_name: The organization_name of this Provider.
        :type: str
        """

        self._organization_name = organization_name

    @property
    def personal_phone(self):
        """
        Gets the personal_phone of this Provider.
        Personal contact phone for the provider.

        :return: The personal_phone of this Provider.
        :rtype: str
        """
        return self._personal_phone

    @personal_phone.setter
    def personal_phone(self, personal_phone):
        """
        Sets the personal_phone of this Provider.
        Personal contact phone for the provider.

        :param personal_phone: The personal_phone of this Provider.
        :type: str
        """

        self._personal_phone = personal_phone

    @property
    def phone(self):
        """
        Gets the phone of this Provider.
        Office phone for the provider

        :return: The phone of this Provider.
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """
        Sets the phone of this Provider.
        Office phone for the provider

        :param phone: The phone of this Provider.
        :type: str
        """

        self._phone = phone

    @property
    def presentation_name(self):
        """
        Gets the presentation_name of this Provider.
        Preferred name for display (e.g. Dr. Francis White may prefer Dr. Frank White)

        :return: The presentation_name of this Provider.
        :rtype: str
        """
        return self._presentation_name

    @presentation_name.setter
    def presentation_name(self, presentation_name):
        """
        Sets the presentation_name of this Provider.
        Preferred name for display (e.g. Dr. Francis White may prefer Dr. Frank White)

        :param presentation_name: The presentation_name of this Provider.
        :type: str
        """

        self._presentation_name = presentation_name

    @property
    def specialty(self):
        """
        Gets the specialty of this Provider.
        Name of the primary Specialty

        :return: The specialty of this Provider.
        :rtype: str
        """
        return self._specialty

    @specialty.setter
    def specialty(self, specialty):
        """
        Sets the specialty of this Provider.
        Name of the primary Specialty

        :param specialty: The specialty of this Provider.
        :type: str
        """

        self._specialty = specialty

    @property
    def state(self):
        """
        Gets the state of this Provider.
        State code for the provider's address (e.g. NY).

        :return: The state of this Provider.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """
        Sets the state of this Provider.
        State code for the provider's address (e.g. NY).

        :param state: The state of this Provider.
        :type: str
        """

        self._state = state

    @property
    def state_id(self):
        """
        Gets the state_id of this Provider.
        Foreign key to States

        :return: The state_id of this Provider.
        :rtype: int
        """
        return self._state_id

    @state_id.setter
    def state_id(self, state_id):
        """
        Sets the state_id of this Provider.
        Foreign key to States

        :param state_id: The state_id of this Provider.
        :type: int
        """

        self._state_id = state_id

    @property
    def street_line_1(self):
        """
        Gets the street_line_1 of this Provider.
        First line of the provider's street address.

        :return: The street_line_1 of this Provider.
        :rtype: str
        """
        return self._street_line_1

    @street_line_1.setter
    def street_line_1(self, street_line_1):
        """
        Sets the street_line_1 of this Provider.
        First line of the provider's street address.

        :param street_line_1: The street_line_1 of this Provider.
        :type: str
        """

        self._street_line_1 = street_line_1

    @property
    def street_line_2(self):
        """
        Gets the street_line_2 of this Provider.
        Second line of the provider's street address.

        :return: The street_line_2 of this Provider.
        :rtype: str
        """
        return self._street_line_2

    @street_line_2.setter
    def street_line_2(self, street_line_2):
        """
        Sets the street_line_2 of this Provider.
        Second line of the provider's street address.

        :param street_line_2: The street_line_2 of this Provider.
        :type: str
        """

        self._street_line_2 = street_line_2

    @property
    def suffix(self):
        """
        Gets the suffix of this Provider.
        Suffix for the provider's name (e.g. Jr)

        :return: The suffix of this Provider.
        :rtype: str
        """
        return self._suffix

    @suffix.setter
    def suffix(self, suffix):
        """
        Sets the suffix of this Provider.
        Suffix for the provider's name (e.g. Jr)

        :param suffix: The suffix of this Provider.
        :type: str
        """

        self._suffix = suffix

    @property
    def title(self):
        """
        Gets the title of this Provider.
        Professional title for the provider (e.g. Dr).

        :return: The title of this Provider.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """
        Sets the title of this Provider.
        Professional title for the provider (e.g. Dr).

        :param title: The title of this Provider.
        :type: str
        """

        self._title = title

    @property
    def type(self):
        """
        Gets the type of this Provider.
        Type of NPI number (individual provider vs organization).

        :return: The type of this Provider.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this Provider.
        Type of NPI number (individual provider vs organization).

        :param type: The type of this Provider.
        :type: str
        """

        self._type = type

    @property
    def zip_code(self):
        """
        Gets the zip_code of this Provider.
        Postal code for the provider's address (e.g. 11215)

        :return: The zip_code of this Provider.
        :rtype: str
        """
        return self._zip_code

    @zip_code.setter
    def zip_code(self, zip_code):
        """
        Sets the zip_code of this Provider.
        Postal code for the provider's address (e.g. 11215)

        :param zip_code: The zip_code of this Provider.
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
