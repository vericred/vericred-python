# coding: utf-8

"""
Copyright 2016 SmartBear Software

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

    Ref: https://github.com/swagger-api/swagger-codegen
"""

from pprint import pformat
from six import iteritems


class Pricing(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
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
            'rating_area_id': 'int'
        }

        self.attribute_map = {
            'age': 'age',
            'effective_date': 'effective_date',
            'expiration_date': 'expiration_date',
            'plan_id': 'plan_id',
            'rating_area_id': 'rating_area_id'
        }

        self._age = None
        self._effective_date = None
        self._expiration_date = None
        self._plan_id = None
        self._rating_area_id = None

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
    def rating_area_id(self):
        """
        Gets the rating_area_id of this Pricing.
        Foreign key to rating areas

        :return: The rating_area_id of this Pricing.
        :rtype: int
        """
        return self._rating_area_id

    @rating_area_id.setter
    def rating_area_id(self, rating_area_id):
        """
        Sets the rating_area_id of this Pricing.
        Foreign key to rating areas

        :param rating_area_id: The rating_area_id of this Pricing.
        :type: int
        """
        self._rating_area_id = rating_area_id

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

