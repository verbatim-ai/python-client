# verbatim_client.SessionApi

All URIs are relative to *https://api.verbatim-ai.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](SessionApi.md#create) | **POST** /v1/session/ | Create a session
[**delete**](SessionApi.md#delete) | **DELETE** /v1/session/{sessionId} | Delete a session
[**get**](SessionApi.md#get) | **GET** /v1/session/{sessionId} | Get a session
[**list**](SessionApi.md#list) | **GET** /v1/session/ | List sessions
[**search**](SessionApi.md#search) | **GET** /v1/session/q | Search sessions
[**update**](SessionApi.md#update) | **PATCH** /v1/session/{sessionId} | Update a session


# **create**
> SessionCreateResponse create(session_create_request)

Create a session

Open a new conversation session against one or more corpora. The session is attached to the user carried by the caller's JWT. How its queries are answered is not decided here: the agent named on each query decides, so a session carries the corpora, the owner and whatever metadata you attach to it.

### Example

* Bearer (JWT) Authentication (JWT):
* Api Key Authentication (AccessToken):

```python
import verbatim_client
from verbatim_client.models.session_create_request import SessionCreateRequest
from verbatim_client.models.session_create_response import SessionCreateResponse
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
    api_instance = verbatim_client.SessionApi(api_client)
    session_create_request = {"corpusIds":["550e8400-e29b-41d4-a716-446655440000"],"metadata":{"customer_id":"42"}} # SessionCreateRequest | 

    try:
        # Create a session
        api_response = api_instance.create(session_create_request)
        print("The response of SessionApi->create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SessionApi->create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_create_request** | [**SessionCreateRequest**](SessionCreateRequest.md)|  | 

### Return type

[**SessionCreateResponse**](SessionCreateResponse.md)

### Authorization

[JWT](../README.md#JWT), [AccessToken](../README.md#AccessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**415** | Content type not accepted by the platform. See &#x60;GET /v1/doc/accept&#x60; for the list of supported types. |  -  |
**500** | Internal error. Check body to get more info |  -  |
**403** | Not authorized. Access not granted for this request |  -  |
**404** | The resource referenced by the request does not exist. |  -  |
**400** | The request is malformed or contains invalid parameters. |  -  |
**409** | The request conflicts with the current state of the resource. |  -  |
**200** | Session created. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete**
> AckResponse delete(session_id)

Delete a session

Soft-delete a session. **Cascades** to every post in the session (also soft-deleted). Documents and embeddings are **not** affected.

### Example

* Bearer (JWT) Authentication (JWT):
* Api Key Authentication (AccessToken):

```python
import verbatim_client
from verbatim_client.models.ack_response import AckResponse
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
    api_instance = verbatim_client.SessionApi(api_client)
    session_id = UUID('123e4567-e89b-12d3-a456-426614174000') # UUID | ID of the session to delete.

    try:
        # Delete a session
        api_response = api_instance.delete(session_id)
        print("The response of SessionApi->delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SessionApi->delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **UUID**| ID of the session to delete. | 

### Return type

[**AckResponse**](AckResponse.md)

### Authorization

[JWT](../README.md#JWT), [AccessToken](../README.md#AccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**415** | Content type not accepted by the platform. See &#x60;GET /v1/doc/accept&#x60; for the list of supported types. |  -  |
**500** | Internal error. Check body to get more info |  -  |
**403** | Not authorized. Access not granted for this request |  -  |
**404** | The resource referenced by the request does not exist. |  -  |
**400** | The request is malformed or contains invalid parameters. |  -  |
**409** | The request conflicts with the current state of the resource. |  -  |
**200** | Session and posts deleted. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get**
> Session get(session_id)

Get a session

Fetch a session's metadata (user, corpora, model, system prompt, parameters). Use `GET /v1/post` to retrieve its posts.

### Example

* Bearer (JWT) Authentication (JWT):
* Api Key Authentication (AccessToken):

```python
import verbatim_client
from verbatim_client.models.session import Session
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
    api_instance = verbatim_client.SessionApi(api_client)
    session_id = UUID('123e4567-e89b-12d3-a456-426614174000') # UUID | ID of the session.

    try:
        # Get a session
        api_response = api_instance.get(session_id)
        print("The response of SessionApi->get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SessionApi->get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **UUID**| ID of the session. | 

### Return type

[**Session**](Session.md)

### Authorization

[JWT](../README.md#JWT), [AccessToken](../README.md#AccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**415** | Content type not accepted by the platform. See &#x60;GET /v1/doc/accept&#x60; for the list of supported types. |  -  |
**500** | Internal error. Check body to get more info |  -  |
**403** | Not authorized. Access not granted for this request |  -  |
**404** | The resource referenced by the request does not exist. |  -  |
**400** | The request is malformed or contains invalid parameters. |  -  |
**409** | The request conflicts with the current state of the resource. |  -  |
**200** | Session found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list**
> SessionListResponse list(page_size=page_size, page_index=page_index)

List sessions

Paginate every session of the caller's organization, newest first.

The organization is resolved from the JWT, so there is nothing to pass and no
way to ask for another tenant's sessions. A session belongs to an organization
as soon as one of its corpora does.

The ordering is closed by the session id, so walking `pageIndex` never shows the
same session twice nor skips one when several were opened in the same
millisecond. `total` counts every session in the organization, not just those
returned here.

To narrow the result — by user, by corpus, by metadata, or by any combination of
the three — use `GET /v1/session/q`, which takes the same paging parameters.


### Example

* Bearer (JWT) Authentication (JWT):
* Api Key Authentication (AccessToken):

```python
import verbatim_client
from verbatim_client.models.session_list_response import SessionListResponse
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
    api_instance = verbatim_client.SessionApi(api_client)
    page_size = 25 # int | Number of items per page, 1-100. (optional) (default to 25)
    page_index = 0 # int | Zero-based page index. (optional) (default to 0)

    try:
        # List sessions
        api_response = api_instance.list(page_size=page_size, page_index=page_index)
        print("The response of SessionApi->list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SessionApi->list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_size** | **int**| Number of items per page, 1-100. | [optional] [default to 25]
 **page_index** | **int**| Zero-based page index. | [optional] [default to 0]

### Return type

[**SessionListResponse**](SessionListResponse.md)

### Authorization

[JWT](../README.md#JWT), [AccessToken](../README.md#AccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**415** | Content type not accepted by the platform. See &#x60;GET /v1/doc/accept&#x60; for the list of supported types. |  -  |
**500** | Internal error. Check body to get more info |  -  |
**403** | Not authorized. Access not granted for this request |  -  |
**404** | The resource referenced by the request does not exist. |  -  |
**400** | The request is malformed or contains invalid parameters. |  -  |
**409** | The request conflicts with the current state of the resource. |  -  |
**200** | Page of sessions. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search**
> SessionListResponse search(user_id=user_id, corpus_id=corpus_id, key=key, value=value, var_json=var_json, page_size=page_size, page_index=page_index)

Search sessions

Find sessions of the caller's organization by owner, corpus and metadata.

Every filter is optional and they **narrow together**: a request carrying none of
them returns the whole organization — the same answer as `GET /v1/session/` —
and one carrying several returns only the sessions matching all of them. That is
what this endpoint adds over the `by…` listings it replaces, which each answer
one fixed combination.

The organization is never a parameter. It comes from the JWT and is always
applied, so no combination of filters reaches another tenant's sessions.

### Owner — `userId`

Exact match on the identifier carried by the JWT when the session was opened.
Sent empty (`&userId=`) it is treated as absent rather than as a match on the
empty string.

### Corpus — `corpusId`

Keeps sessions bound to that corpus. A session may be bound to several, and it
matches as soon as one of them is the requested one. The corpus must belong to
the caller's organization.

### Metadata — `key`/`value`, or `json`

Matches sessions whose metadata **contains** the fragment (PostgreSQL's `@>`
operator), extra keys on the session being fine. Pass `key` and `value` for a
single pair — they go together, one without the other is a `400` — or `json`
for a raw object when the filter is nested or has several keys. `json` wins when
both are supplied.

### Ordering and paging

Newest first, closed by the session id, so walking `pageIndex` never shows the
same session twice nor skips one. `total` counts every match across all pages.

### Examples

* `?userId=user_42` — every session that user opened, across corpora
* `?corpusId=…` — every session opened against one corpus, whoever opened it
* `?userId=user_42&corpusId=…` — both, which `GET /v1/session/byUser` also did
* `?userId=user_42&key=customer_id&value=42` — the combination none of the
  `by…` endpoints could express
* `?json={"channel":{"kind":"web"}}` — a nested metadata fragment


### Example

* Bearer (JWT) Authentication (JWT):
* Api Key Authentication (AccessToken):

```python
import verbatim_client
from verbatim_client.models.session_list_response import SessionListResponse
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
    api_instance = verbatim_client.SessionApi(api_client)
    user_id = 'user_42' # str | Exact identifier of the user who opened the session. Blank or omitted, the owner is not filtered. (optional)
    corpus_id = UUID('123e4567-e89b-12d3-a456-426614174000') # UUID | Keep sessions bound to this corpus. Must belong to the caller's organization. (optional)
    key = 'customer_id' # str | Metadata key to filter on. Goes together with `value`. (optional)
    value = '42' # str | Metadata value matching `key`. (optional)
    var_json = '{\"customer_id\":\"42\"}' # str | Raw JSON object used as the containment filter. Wins over `key`/`value` when set. (optional)
    page_size = 25 # int | Number of items per page, 1-100. (optional) (default to 25)
    page_index = 0 # int | Zero-based page index. (optional) (default to 0)

    try:
        # Search sessions
        api_response = api_instance.search(user_id=user_id, corpus_id=corpus_id, key=key, value=value, var_json=var_json, page_size=page_size, page_index=page_index)
        print("The response of SessionApi->search:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SessionApi->search: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| Exact identifier of the user who opened the session. Blank or omitted, the owner is not filtered. | [optional] 
 **corpus_id** | **UUID**| Keep sessions bound to this corpus. Must belong to the caller&#39;s organization. | [optional] 
 **key** | **str**| Metadata key to filter on. Goes together with &#x60;value&#x60;. | [optional] 
 **value** | **str**| Metadata value matching &#x60;key&#x60;. | [optional] 
 **var_json** | **str**| Raw JSON object used as the containment filter. Wins over &#x60;key&#x60;/&#x60;value&#x60; when set. | [optional] 
 **page_size** | **int**| Number of items per page, 1-100. | [optional] [default to 25]
 **page_index** | **int**| Zero-based page index. | [optional] [default to 0]

### Return type

[**SessionListResponse**](SessionListResponse.md)

### Authorization

[JWT](../README.md#JWT), [AccessToken](../README.md#AccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**415** | Content type not accepted by the platform. See &#x60;GET /v1/doc/accept&#x60; for the list of supported types. |  -  |
**500** | Internal error. Check body to get more info |  -  |
**403** | Not authorized. Access not granted for this request |  -  |
**404** | The resource referenced by the request does not exist. |  -  |
**400** | A metadata filter is malformed, or a paging parameter is out of bounds. |  -  |
**409** | The request conflicts with the current state of the resource. |  -  |
**200** | Page of matching sessions. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update**
> Session update(session_id, session_update_request)

Update a session

Patch one or more session attributes. Only the fields provided in the request body are updated; omitted fields keep their current value. Returns the full updated session.

### Example

* Bearer (JWT) Authentication (JWT):
* Api Key Authentication (AccessToken):

```python
import verbatim_client
from verbatim_client.models.session import Session
from verbatim_client.models.session_update_request import SessionUpdateRequest
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
    api_instance = verbatim_client.SessionApi(api_client)
    session_id = UUID('123e4567-e89b-12d3-a456-426614174000') # UUID | ID of the session to update.
    session_update_request = {"metadata":{"customer_id":"42","ticket":"SUPP-999"}} # SessionUpdateRequest | 

    try:
        # Update a session
        api_response = api_instance.update(session_id, session_update_request)
        print("The response of SessionApi->update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SessionApi->update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **UUID**| ID of the session to update. | 
 **session_update_request** | [**SessionUpdateRequest**](SessionUpdateRequest.md)|  | 

### Return type

[**Session**](Session.md)

### Authorization

[JWT](../README.md#JWT), [AccessToken](../README.md#AccessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**415** | Content type not accepted by the platform. See &#x60;GET /v1/doc/accept&#x60; for the list of supported types. |  -  |
**500** | Internal error. Check body to get more info |  -  |
**403** | Not authorized. Access not granted for this request |  -  |
**404** | The resource referenced by the request does not exist. |  -  |
**400** | The request is malformed or contains invalid parameters. |  -  |
**409** | The request conflicts with the current state of the resource. |  -  |
**200** | Session updated. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

