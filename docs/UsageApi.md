# verbatim_client.UsageApi

All URIs are relative to *https://api.verbatim-ai.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**usage**](UsageApi.md#usage) | **GET** /v1/usage/all | Organization usage
[**usage_by_corpus**](UsageApi.md#usage_by_corpus) | **GET** /v1/usage/corpus/{corpusId} | Corpus usage
[**usage_by_user**](UsageApi.md#usage_by_user) | **GET** /v1/usage/user/{userId} | User usage


# **usage**
> Usage usage(timeframe=timeframe)

Organization usage

Return the aggregated usage report for the caller's organization over a rolling timeframe.

Each dimension is reported as:
- **tokens** — `total` (lifetime, soft-deleted included) and `inPeriod` (window). At organization scope this sums `post.token` AND `document.token` (vectorization tokens are billed at organization level).
- **corpora / sessions / posts / storage** — `total`, `created` (in window), `removed` (in window).
- **storage** values are bytes.

The `timeframe` parameter selects a rolling window ending at `timestamp`:

- `Day` — last 24 hours
- `Week` — last 7 days
- `Month` — last 30 days
- `Year` — last 365 days

The window is half-open: `from` inclusive, `to` exclusive.


### Example

* Bearer (JWT) Authentication (JWT):
* Api Key Authentication (AccessToken):

```python
import verbatim_client
from verbatim_client.models.usage import Usage
from verbatim_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.verbatim-ai.com
# See configuration.py for a list of all supported configuration parameters.
configuration = verbatim_client.Configuration(
    host = "https://api.verbatim-ai.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWT
configuration = verbatim_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Enter a context with an instance of the API client
with verbatim_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = verbatim_client.UsageApi(api_client)
    timeframe = 'Day' # str | Rolling window to aggregate over. Defaults to `Day`. (optional)

    try:
        # Organization usage
        api_response = api_instance.usage(timeframe=timeframe)
        print("The response of UsageApi->usage:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsageApi->usage: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeframe** | **str**| Rolling window to aggregate over. Defaults to &#x60;Day&#x60;. | [optional] 

### Return type

[**Usage**](Usage.md)

### Authorization

[JWT](../README.md#JWT), [AccessToken](../README.md#AccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**500** | Internal error. Check body to get more info |  -  |
**403** | Not authorized. Access not granted for this request |  -  |
**404** | The resource referenced by the request does not exist. |  -  |
**415** | Content type not accepted by the platform. See &#x60;GET /v1/doc/accept&#x60; for the list of supported types. |  -  |
**400** | The request is malformed or contains invalid parameters. |  -  |
**409** | The request conflicts with the current state of the resource. |  -  |
**200** | Organization usage report. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **usage_by_corpus**
> Usage usage_by_corpus(corpus_id, timeframe=timeframe)

Corpus usage

Return the aggregated usage report for a single corpus over a rolling timeframe.

Differences with the organization-scope report:
- **tokens** sums `post.token` only — vectorization tokens (`document.token`) are reported only at organization scope, because they are billed against the org.
- **corpora** is `null` — cardinality is always 1 at corpus scope.

Sessions, posts and storage are restricted to the requested corpus.


### Example

* Bearer (JWT) Authentication (JWT):
* Api Key Authentication (AccessToken):

```python
import verbatim_client
from verbatim_client.models.usage import Usage
from verbatim_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.verbatim-ai.com
# See configuration.py for a list of all supported configuration parameters.
configuration = verbatim_client.Configuration(
    host = "https://api.verbatim-ai.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWT
configuration = verbatim_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Enter a context with an instance of the API client
with verbatim_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = verbatim_client.UsageApi(api_client)
    corpus_id = UUID('550e8400-e29b-41d4-a716-446655440001') # UUID | ID of the corpus to compute usage for.
    timeframe = 'Day' # str | Rolling window to aggregate over. Defaults to `Day`. (optional)

    try:
        # Corpus usage
        api_response = api_instance.usage_by_corpus(corpus_id, timeframe=timeframe)
        print("The response of UsageApi->usage_by_corpus:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsageApi->usage_by_corpus: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **corpus_id** | **UUID**| ID of the corpus to compute usage for. | 
 **timeframe** | **str**| Rolling window to aggregate over. Defaults to &#x60;Day&#x60;. | [optional] 

### Return type

[**Usage**](Usage.md)

### Authorization

[JWT](../README.md#JWT), [AccessToken](../README.md#AccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**500** | Internal error. Check body to get more info |  -  |
**403** | Not authorized. Access not granted for this request |  -  |
**404** | The resource referenced by the request does not exist. |  -  |
**415** | Content type not accepted by the platform. See &#x60;GET /v1/doc/accept&#x60; for the list of supported types. |  -  |
**400** | The request is malformed or contains invalid parameters. |  -  |
**409** | The request conflicts with the current state of the resource. |  -  |
**200** | Corpus usage report. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **usage_by_user**
> Usage usage_by_user(user_id, timeframe=timeframe)

User usage

Return the aggregated usage report for a single user within the caller's organization over a rolling timeframe.

Scope:
- **tokens** sums `post.token` of sessions where `session.user_id = userId` AND `document.token` of documents where `document.user_id = userId`, both restricted to corpora of `orgId`.
- **sessions** counts distinct sessions owned by `userId` in the organization.
- **posts** counts posts in those sessions.
- **storage** sums `document.size` of documents uploaded by `userId` in the organization.
- **corpora** is `null` — cardinality is not meaningful at user scope.

Soft-deleted rows count toward lifetime totals; the `removed` deltas detect cleanup.


### Example

* Bearer (JWT) Authentication (JWT):
* Api Key Authentication (AccessToken):

```python
import verbatim_client
from verbatim_client.models.usage import Usage
from verbatim_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.verbatim-ai.com
# See configuration.py for a list of all supported configuration parameters.
configuration = verbatim_client.Configuration(
    host = "https://api.verbatim-ai.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWT
configuration = verbatim_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Enter a context with an instance of the API client
with verbatim_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = verbatim_client.UsageApi(api_client)
    user_id = 'user-42' # str | ID of the user to compute usage for. Free-form string (max 256 chars), matched against `session.user_id` and `document.user_id`.
    timeframe = 'Day' # str | Rolling window to aggregate over. Defaults to `Day`. (optional)

    try:
        # User usage
        api_response = api_instance.usage_by_user(user_id, timeframe=timeframe)
        print("The response of UsageApi->usage_by_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsageApi->usage_by_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| ID of the user to compute usage for. Free-form string (max 256 chars), matched against &#x60;session.user_id&#x60; and &#x60;document.user_id&#x60;. | 
 **timeframe** | **str**| Rolling window to aggregate over. Defaults to &#x60;Day&#x60;. | [optional] 

### Return type

[**Usage**](Usage.md)

### Authorization

[JWT](../README.md#JWT), [AccessToken](../README.md#AccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**500** | Internal error. Check body to get more info |  -  |
**403** | Not authorized. Access not granted for this request |  -  |
**404** | The resource referenced by the request does not exist. |  -  |
**415** | Content type not accepted by the platform. See &#x60;GET /v1/doc/accept&#x60; for the list of supported types. |  -  |
**400** | The request is malformed or contains invalid parameters. |  -  |
**409** | The request conflicts with the current state of the resource. |  -  |
**200** | User usage report. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

