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

import sys
from setuptools import setup, find_packages

NAME = "vericred_client"
VERSION = "0.0.8"

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]

setup(
    name=NAME,
    version=VERSION,
    description="Vericred API",
    author_email="",
    url="",
    keywords=["Swagger", "Vericred API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    Vericred&#39;s API allows you to search for Health Plans that a specific doctor
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
[autogenerated SDKs](https://github.com/vericred/?query&#x3D;vericred-),
which we make available for several common programming languages.

## Authentication

To authenticate, pass the API Key you created in the Developer Portal as
a &#x60;Vericred-Api-Key&#x60; header.

&#x60;curl -H &#39;Vericred-Api-Key: YOUR_KEY&#39; &quot;https://api.vericred.com/providers?search_term&#x3D;Foo&amp;zip_code&#x3D;11215&quot;&#x60;

## Versioning

Vericred&#39;s API default to the latest version.  However, if you need a specific
version, you can request it with an &#x60;Accept-Version&#x60; header.

The current version is &#x60;v3&#x60;.  Previous versions are &#x60;v1&#x60; and &#x60;v2&#x60;.

&#x60;curl -H &#39;Vericred-Api-Key: YOUR_KEY&#39; -H &#39;Accept-Version: v2&#39; &quot;https://api.vericred.com/providers?search_term&#x3D;Foo&amp;zip_code&#x3D;11215&quot;&#x60;

## Pagination

Endpoints that accept &#x60;page&#x60; and &#x60;per_page&#x60; parameters are paginated. They expose
four additional fields that contain data about your position in the response,
namely &#x60;Total&#x60;, &#x60;Per-Page&#x60;, &#x60;Link&#x60;, and &#x60;Page&#x60; as described in [RFC-5988](https://tools.ietf.org/html/rfc5988).

For example, to display 5 results per page and view the second page of a
&#x60;GET&#x60; to &#x60;/networks&#x60;, your final request would be &#x60;GET /networks?....page&#x3D;2&amp;per_page&#x3D;5&#x60;.

## Sideloading

When we return multiple levels of an object graph (e.g. &#x60;Provider&#x60;s and their &#x60;State&#x60;s
we sideload the associated data.  In this example, we would provide an Array of
&#x60;State&#x60;s and a &#x60;state_id&#x60; for each provider.  This is done primarily to reduce the
payload size since many of the &#x60;Provider&#x60;s will share a &#x60;State&#x60;

&#x60;&#x60;&#x60;
{
  providers: [{ id: 1, state_id: 1}, { id: 2, state_id: 1 }],
  states: [{ id: 1, code: &#39;NY&#39; }]
}
&#x60;&#x60;&#x60;

If you need the second level of the object graph, you can just match the
corresponding id.

## Selecting specific data

All endpoints allow you to specify which fields you would like to return.
This allows you to limit the response to contain only the data you need.

For example, let&#39;s take a request that returns the following JSON by default

&#x60;&#x60;&#x60;
{
  provider: {
    id: 1,
    name: &#39;John&#39;,
    phone: &#39;1234567890&#39;,
    field_we_dont_care_about: &#39;value_we_dont_care_about&#39;
  },
  states: [{
    id: 1,
    name: &#39;New York&#39;,
    code: &#39;NY&#39;,
    field_we_dont_care_about: &#39;value_we_dont_care_about&#39;
  }]
}
&#x60;&#x60;&#x60;

To limit our results to only return the fields we care about, we specify the
&#x60;select&#x60; query string parameter for the corresponding fields in the JSON
document.

In this case, we want to select &#x60;name&#x60; and &#x60;phone&#x60; from the &#x60;provider&#x60; key,
so we would add the parameters &#x60;select&#x3D;provider.name,provider.phone&#x60;.
We also want the &#x60;name&#x60; and &#x60;code&#x60; from the &#x60;states&#x60; key, so we would
add the parameters &#x60;select&#x3D;states.name,staes.code&#x60;.  The id field of
each document is always returned whether or not it is requested.

Our final request would be &#x60;GET /providers/12345?select&#x3D;provider.name,provider.phone,states.name,states.code&#x60;

The response would be

&#x60;&#x60;&#x60;
{
  provider: {
    id: 1,
    name: &#39;John&#39;,
    phone: &#39;1234567890&#39;
  },
  states: [{
    id: 1,
    name: &#39;New York&#39;,
    code: &#39;NY&#39;
  }]
}
&#x60;&#x60;&#x60;

## Benefits summary format
Benefit cost-share strings are formatted to capture:
 * Network tiers
 * Compound or conditional cost-share
 * Limits on the cost-share
 * Benefit-specific maximum out-of-pocket costs

**Example #1**
As an example, we would represent [this Summary of Benefits &amp;amp; Coverage](https://s3.amazonaws.com/vericred-data/SBC/2017/33602TX0780032.pdf) as:

* **Hospital stay facility fees**:
  - Network Provider: &#x60;$400 copay/admit plus 20% coinsurance&#x60;
  - Out-of-Network Provider: &#x60;$1,500 copay/admit plus 50% coinsurance&#x60;
  - Vericred&#39;s format for this benefit: &#x60;In-Network: $400 before deductible then 20% after deductible / Out-of-Network: $1,500 before deductible then 50% after deductible&#x60;

* **Rehabilitation services:**
  - Network Provider: &#x60;20% coinsurance&#x60;
  - Out-of-Network Provider: &#x60;50% coinsurance&#x60;
  - Limitations &amp; Exceptions: &#x60;35 visit maximum per benefit period combined with Chiropractic care.&#x60;
  - Vericred&#39;s format for this benefit: &#x60;In-Network: 20% after deductible / Out-of-Network: 50% after deductible | limit: 35 visit(s) per Benefit Period&#x60;

**Example #2**
In [this other Summary of Benefits &amp;amp; Coverage](https://s3.amazonaws.com/vericred-data/SBC/2017/40733CA0110568.pdf), the **specialty_drugs** cost-share has a maximum out-of-pocket for in-network pharmacies.
* **Specialty drugs:**
  - Network Provider: &#x60;40% coinsurance up to a $500 maximum for up to a 30 day supply&#x60;
  - Out-of-Network Provider &#x60;Not covered&#x60;
  - Vericred&#39;s format for this benefit: &#x60;In-Network: 40% after deductible, up to $500 per script / Out-of-Network: 100%&#x60;

**BNF**

Here&#39;s a description of the benefits summary string, represented as a context-free grammar:

&#x60;&#x60;&#x60;
&lt;cost-share&gt;     ::&#x3D; &lt;tier&gt; &lt;opt-num-prefix&gt; &lt;value&gt; &lt;opt-per-unit&gt; &lt;deductible&gt; &lt;tier-limit&gt; &quot;/&quot; &lt;tier&gt; &lt;opt-num-prefix&gt; &lt;value&gt; &lt;opt-per-unit&gt; &lt;deductible&gt; &quot;|&quot; &lt;benefit-limit&gt;
&lt;tier&gt;           ::&#x3D; &quot;In-Network:&quot; | &quot;In-Network-Tier-2:&quot; | &quot;Out-of-Network:&quot;
&lt;opt-num-prefix&gt; ::&#x3D; &quot;first&quot; &lt;num&gt; &lt;unit&gt; | &quot;&quot;
&lt;unit&gt;           ::&#x3D; &quot;day(s)&quot; | &quot;visit(s)&quot; | &quot;exam(s)&quot; | &quot;item(s)&quot;
&lt;value&gt;          ::&#x3D; &lt;ddct_moop&gt; | &lt;copay&gt; | &lt;coinsurance&gt; | &lt;compound&gt; | &quot;unknown&quot; | &quot;Not Applicable&quot;
&lt;compound&gt;       ::&#x3D; &lt;copay&gt; &lt;deductible&gt; &quot;then&quot; &lt;coinsurance&gt; &lt;deductible&gt; | &lt;copay&gt; &lt;deductible&gt; &quot;then&quot; &lt;copay&gt; &lt;deductible&gt; | &lt;coinsurance&gt; &lt;deductible&gt; &quot;then&quot; &lt;coinsurance&gt; &lt;deductible&gt;
&lt;copay&gt;          ::&#x3D; &quot;$&quot; &lt;num&gt;
&lt;coinsurace&gt;     ::&#x3D; &lt;num&gt; &quot;%&quot;
&lt;ddct_moop&gt;      ::&#x3D; &lt;copay&gt; | &quot;Included in Medical&quot; | &quot;Unlimited&quot;
&lt;opt-per-unit&gt;   ::&#x3D; &quot;per day&quot; | &quot;per visit&quot; | &quot;per stay&quot; | &quot;&quot;
&lt;deductible&gt;     ::&#x3D; &quot;before deductible&quot; | &quot;after deductible&quot; | &quot;&quot;
&lt;tier-limit&gt;     ::&#x3D; &quot;, &quot; &lt;limit&gt; | &quot;&quot;
&lt;benefit-limit&gt;  ::&#x3D; &lt;limit&gt; | &quot;&quot;
&#x60;&#x60;&#x60;


    """
)
