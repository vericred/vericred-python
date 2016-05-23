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


class PlanCounty(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        PlanCounty - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'plan_id': 'int',
            'county_id': 'int'
        }

        self.attribute_map = {
            'id': 'id',
            'plan_id': 'plan_id',
            'county_id': 'county_id'
        }

        self._id = None
        self._plan_id = None
        self._county_id = None

    @property
    def id(self):
        """
        Gets the id of this PlanCounty.
        Primary key

        :return: The id of this PlanCounty.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this PlanCounty.
        Primary key

        :param id: The id of this PlanCounty.
        :type: int
        """
        self._id = id

    @property
    def plan_id(self):
        """
        Gets the plan_id of this PlanCounty.
        Foreign key to plan

        :return: The plan_id of this PlanCounty.
        :rtype: int
        """
        return self._plan_id

    @plan_id.setter
    def plan_id(self, plan_id):
        """
        Sets the plan_id of this PlanCounty.
        Foreign key to plan

        :param plan_id: The plan_id of this PlanCounty.
        :type: int
        """
        self._plan_id = plan_id

    @property
    def county_id(self):
        """
        Gets the county_id of this PlanCounty.
        Foreign key to county

        :return: The county_id of this PlanCounty.
        :rtype: int
        """
        return self._county_id

    @county_id.setter
    def county_id(self, county_id):
        """
        Sets the county_id of this PlanCounty.
        Foreign key to county

        :param county_id: The county_id of this PlanCounty.
        :type: int
        """
        self._county_id = county_id

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

