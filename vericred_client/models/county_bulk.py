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


class CountyBulk(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, name=None, state_id=None, rating_area_count=None, service_area_count=None):
        """
        CountyBulk - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'state_id': 'str',
            'rating_area_count': 'str',
            'service_area_count': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'state_id': 'state_id',
            'rating_area_count': 'rating_area_count',
            'service_area_count': 'service_area_count'
        }

        self._id = id
        self._name = name
        self._state_id = state_id
        self._rating_area_count = rating_area_count
        self._service_area_count = service_area_count


    @property
    def id(self):
        """
        Gets the id of this CountyBulk.
        FIPs code for the county

        :return: The id of this CountyBulk.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this CountyBulk.
        FIPs code for the county

        :param id: The id of this CountyBulk.
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """
        Gets the name of this CountyBulk.
        Name of the county

        :return: The name of this CountyBulk.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this CountyBulk.
        Name of the county

        :param name: The name of this CountyBulk.
        :type: str
        """

        self._name = name

    @property
    def state_id(self):
        """
        Gets the state_id of this CountyBulk.
        State code

        :return: The state_id of this CountyBulk.
        :rtype: str
        """
        return self._state_id

    @state_id.setter
    def state_id(self, state_id):
        """
        Sets the state_id of this CountyBulk.
        State code

        :param state_id: The state_id of this CountyBulk.
        :type: str
        """

        self._state_id = state_id

    @property
    def rating_area_count(self):
        """
        Gets the rating_area_count of this CountyBulk.
        Count of unique rating areas in the county

        :return: The rating_area_count of this CountyBulk.
        :rtype: str
        """
        return self._rating_area_count

    @rating_area_count.setter
    def rating_area_count(self, rating_area_count):
        """
        Sets the rating_area_count of this CountyBulk.
        Count of unique rating areas in the county

        :param rating_area_count: The rating_area_count of this CountyBulk.
        :type: str
        """

        self._rating_area_count = rating_area_count

    @property
    def service_area_count(self):
        """
        Gets the service_area_count of this CountyBulk.
        Count of unique service areas in the county

        :return: The service_area_count of this CountyBulk.
        :rtype: str
        """
        return self._service_area_count

    @service_area_count.setter
    def service_area_count(self, service_area_count):
        """
        Sets the service_area_count of this CountyBulk.
        Count of unique service areas in the county

        :param service_area_count: The service_area_count of this CountyBulk.
        :type: str
        """

        self._service_area_count = service_area_count

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
