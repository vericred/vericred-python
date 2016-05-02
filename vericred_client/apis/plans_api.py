# coding: utf-8

"""
PlansApi.py
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
"""

from __future__ import absolute_import

import sys
import os

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class PlansApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def plans_find_post(self, query, **kwargs):
        """
        Find a set of plans for a Zip Code and County
        ### Location Information

Searching for a set of plans requires a `zip_code` and `fips_code`
code.  These are used to determine pricing and availabity
of health plans.

Optionally, you may provide a list of Applicants or Providers

### Applicants

This is a list of people who will be covered by the plan.  We
use this list to calculate the premium.  You must include `age`
and can include `smoker`, which also factors into pricing in some
states.

Applicants *must* include an age.  If smoker is omitted, its value is assumed
to be false.

#### Multiple Applicants

To get pricing for multiple applicants, just append multiple sets
of data to the URL with the age and smoking status of each applicant
next to each other.

For example, given two applicants - one age 32 and a non-smoker and one
age 29 and a smoker, you could use the following request

`GET /plans?zip_code=07451&fips_code=33025&applicants[][age]=32&applicants[][age]=29&applicants[][smoker]=true`

It would also be acceptible to include `applicants[][smoker]=false` after the
first applicant's age.

### Providers

We identify Providers (Doctors) by their National Practitioner
Index number (NPI).  If you pass a list of Providers, keyed by
their NPI number, we will return a list of which Providers are
in and out of network for each plan returned.

For example, if we had two providers with the NPI numbers `12345` and `23456`
you would make the following request

`GET /plans?zip_code=07451&fips_code=33025&providers[][npi]=12345&providers[][npi]=23456`

### Enrollment Date

To calculate plan pricing and availability, we default to the current date
as the enrollment date.  To specify a date in the future (or the past), pass
a string with the format `YYYY-MM-DD` in the `enrollment_date` parameter.

`GET /plans?zip_code=07451&fips_code=33025&enrollment_date=2016-01-01`

### Subsidy

On-marketplace plans are eligible for a subsidy based on the
`household_size` and `household_income` of the applicants.  If you
pass those values, we will calculate the `subsidized_premium`
and return it for each plan.  If no values are provided, the
`subsidized_premium` will be the same as the `premium`

`GET /plans?zip_code=07451&fips_code=33025&household_size=4&household_income=40000`



        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.plans_find_post(query, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param Query query: Plan query (required)
        :return: list[Plan]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['query']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method plans_find_post" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'query' is set
        if ('query' not in params) or (params['query'] is None):
            raise ValueError("Missing the required parameter `query` when calling `plans_find_post`")

        resource_path = '/plans/find'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'query' in params:
            body_params = params['query']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept([])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type([])

        # Authentication setting
        auth_settings = []

        response = self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='list[Plan]',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response
