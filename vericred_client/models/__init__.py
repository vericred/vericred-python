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

from __future__ import absolute_import

# import models into model package
from .aca_plan import ACAPlan
from .aca_plan2018 import ACAPlan2018
from .aca_plan2018_search_response import ACAPlan2018SearchResponse
from .aca_plan2018_search_result import ACAPlan2018SearchResult
from .aca_plan2018_show_response import ACAPlan2018ShowResponse
from .aca_plan_pre2018 import ACAPlanPre2018
from .aca_plan_pre2018_search_response import ACAPlanPre2018SearchResponse
from .aca_plan_pre2018_search_result import ACAPlanPre2018SearchResult
from .aca_plan_pre2018_show_response import ACAPlanPre2018ShowResponse
from .base import Base
from .base_plan_search_response import BasePlanSearchResponse
from .carrier import Carrier
from .carrier_group_request import CarrierGroupRequest
from .carrier_request import CarrierRequest
from .carrier_subsidiary import CarrierSubsidiary
from .county import County
from .county_bulk import CountyBulk
from .dental_plan import DentalPlan
from .dental_plan_benefits import DentalPlanBenefits
from .dental_plan_search_applicant import DentalPlanSearchApplicant
from .dental_plan_search_request import DentalPlanSearchRequest
from .dental_plan_search_response import DentalPlanSearchResponse
from .dental_plan_show_response import DentalPlanShowResponse
from .dental_plan_update import DentalPlanUpdate
from .dental_plan_update_request import DentalPlanUpdateRequest
from .drug import Drug
from .drug_coverage import DrugCoverage
from .drug_coverage_response import DrugCoverageResponse
from .drug_package import DrugPackage
from .drug_search_response import DrugSearchResponse
from .embargo_request import EmbargoRequest
from .formulary import Formulary
from .formulary_drug_package_response import FormularyDrugPackageResponse
from .formulary_response import FormularyResponse
from .issuer_request import IssuerRequest
from .meta import Meta
from .meta_plan_search_response import MetaPlanSearchResponse
from .network import Network
from .network_comparison import NetworkComparison
from .network_comparison_request import NetworkComparisonRequest
from .network_comparison_response import NetworkComparisonResponse
from .network_details import NetworkDetails
from .network_details_response import NetworkDetailsResponse
from .network_search_response import NetworkSearchResponse
from .network_size import NetworkSize
from .notification_subscription import NotificationSubscription
from .notification_subscription_response import NotificationSubscriptionResponse
from .plan import Plan
from .plan_county import PlanCounty
from .plan_county_bulk import PlanCountyBulk
from .plan_deleted import PlanDeleted
from .plan_identifier import PlanIdentifier
from .plan_medicare import PlanMedicare
from .plan_medicare_bulk import PlanMedicareBulk
from .plan_pricing_medicare import PlanPricingMedicare
from .plan_search_response import PlanSearchResponse
from .plan_show_response import PlanShowResponse
from .provider import Provider
from .provider_details import ProviderDetails
from .provider_geocode import ProviderGeocode
from .provider_network_event_notification import ProviderNetworkEventNotification
from .provider_show_response import ProviderShowResponse
from .providers_geocode_response import ProvidersGeocodeResponse
from .providers_search_response import ProvidersSearchResponse
from .rate_request import RateRequest
from .rating_area import RatingArea
from .request_plan_find import RequestPlanFind
from .request_plan_find_applicant import RequestPlanFindApplicant
from .request_plan_find_carrier_verification import RequestPlanFindCarrierVerification
from .request_plan_find_drug_package import RequestPlanFindDrugPackage
from .request_plan_find_provider import RequestPlanFindProvider
from .request_provider_notification_subscription import RequestProviderNotificationSubscription
from .request_providers_search import RequestProvidersSearch
from .rx_cui_identifier import RxCuiIdentifier
from .rx_cui_identifier_search_response import RxCuiIdentifierSearchResponse
from .service_area import ServiceArea
from .service_area_zip_county import ServiceAreaZipCounty
from .state import State
from .state_network_size_request import StateNetworkSizeRequest
from .state_network_size_response import StateNetworkSizeResponse
from .vision_plan import VisionPlan
from .vision_plan_benefits import VisionPlanBenefits
from .vision_plan_search_applicant import VisionPlanSearchApplicant
from .vision_plan_search_request import VisionPlanSearchRequest
from .vision_plan_search_response import VisionPlanSearchResponse
from .vision_plan_show_response import VisionPlanShowResponse
from .vision_plan_update import VisionPlanUpdate
from .vision_plan_update_request import VisionPlanUpdateRequest
from .zip_code import ZipCode
from .zip_counties_response import ZipCountiesResponse
from .zip_county import ZipCounty
from .zip_county_bulk import ZipCountyBulk
from .zip_county_response import ZipCountyResponse
