# verbatim_client.ThreadApi

All URIs are relative to *https://api.verbatim-ai.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](ThreadApi.md#create) | **POST** /v1/session/ | Create a thread
[**create1**](ThreadApi.md#create1) | **POST** /v1/thread/ | Create a thread
[**delete**](ThreadApi.md#delete) | **DELETE** /v1/session/{threadId} | Delete a thread
[**delete1**](ThreadApi.md#delete1) | **DELETE** /v1/thread/{threadId} | Delete a thread
[**get**](ThreadApi.md#get) | **GET** /v1/session/{threadId} | Get a thread
[**get1**](ThreadApi.md#get1) | **GET** /v1/thread/{threadId} | Get a thread
[**list**](ThreadApi.md#list) | **GET** /v1/session/ | List threads
[**list1**](ThreadApi.md#list1) | **GET** /v1/thread/ | List threads
[**search**](ThreadApi.md#search) | **GET** /v1/thread/q | Search threads
[**search1**](ThreadApi.md#search1) | **GET** /v1/session/q | Search threads
[**update**](ThreadApi.md#update) | **PATCH** /v1/session/{threadId} | Update a thread
[**update1**](ThreadApi.md#update1) | **PATCH** /v1/thread/{threadId} | Update a thread


# **create**
> ThreadCreateResponse create(session_create_request)

Create a thread

Open a new conversation thread against one or more corpora. The thread is attached to the user carried by the caller's JWT. How its queries are answered is not decided here: the agent named on each query decides, so a thread carries the corpora, the owner and whatever metadata you attach to it.

### Example

* Bearer (JWT) Authentication (JWT):
* Api Key Authentication (AccessToken):

```python
import verbatim_client
from verbatim_client.models.session_create_request import SessionCreateRequest
from verbatim_client.models.thread_create_response import ThreadCreateResponse
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
    api_instance = verbatim_client.ThreadApi(api_client)
    session_create_request = {"corpusIds":["550e8400-e29b-41d4-a716-446655440000"],"metadata":{"customer_id":"42"}} # SessionCreateRequest | 

    try:
        # Create a thread
        api_response = api_instance.create(session_create_request)
        print("The response of ThreadApi->create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThreadApi->create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_create_request** | [**SessionCreateRequest**](SessionCreateRequest.md)|  | 

### Return type

[**ThreadCreateResponse**](ThreadCreateResponse.md)

### Authorization

[JWT](../README.md#JWT), [AccessToken](../README.md#AccessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**500** | Internal error. Check body to get more info |  -  |
**415** | Content type not accepted by the platform. See &#x60;GET /v1/doc/accept&#x60; for the list of supported types. |  -  |
**403** | Not authorized. Access not granted for this request |  -  |
**404** | The resource referenced by the request does not exist. |  -  |
**400** | The request is malformed or contains invalid parameters. |  -  |
**409** | The request conflicts with the current state of the resource. |  -  |
**200** | Thread created. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create1**
> ThreadCreateResponse create1(session_create_request)

Create a thread

Open a new conversation thread against one or more corpora. The thread is attached to the user carried by the caller's JWT. How its queries are answered is not decided here: the agent named on each query decides, so a thread carries the corpora, the owner and whatever metadata you attach to it.

### Example

* Bearer (JWT) Authentication (JWT):
* Api Key Authentication (AccessToken):

```python
import verbatim_client
from verbatim_client.models.session_create_request import SessionCreateRequest
from verbatim_client.models.thread_create_response import ThreadCreateResponse
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
    api_instance = verbatim_client.ThreadApi(api_client)
    session_create_request = {corpusIds=[550e8400-e29b-41d4-a716-446655440000], metadata={customer_id=42}} # SessionCreateRequest | 

    try:
        # Create a thread
        api_response = api_instance.create1(session_create_request)
        print("The response of ThreadApi->create1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThreadApi->create1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_create_request** | [**SessionCreateRequest**](SessionCreateRequest.md)|  | 

### Return type

[**ThreadCreateResponse**](ThreadCreateResponse.md)

### Authorization

[JWT](../README.md#JWT), [AccessToken](../README.md#AccessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**500** | Internal error. Check body to get more info |  -  |
**415** | Content type not accepted by the platform. See &#x60;GET /v1/doc/accept&#x60; for the list of supported types. |  -  |
**403** | Not authorized. Access not granted for this request |  -  |
**404** | The resource referenced by the request does not exist. |  -  |
**400** | The request is malformed or contains invalid parameters. |  -  |
**409** | The request conflicts with the current state of the resource. |  -  |
**200** | Thread created. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete**
> AckResponse delete(thread_id)

Delete a thread

Soft-delete a thread. **Cascades** to every post in the thread (also soft-deleted). Documents and embeddings are **not** affected.

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
    api_instance = verbatim_client.ThreadApi(api_client)
    thread_id = UUID('123e4567-e89b-12d3-a456-426614174000') # UUID | ID of the thread to delete.

    try:
        # Delete a thread
        api_response = api_instance.delete(thread_id)
        print("The response of ThreadApi->delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThreadApi->delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **thread_id** | **UUID**| ID of the thread to delete. | 

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
**500** | Internal error. Check body to get more info |  -  |
**415** | Content type not accepted by the platform. See &#x60;GET /v1/doc/accept&#x60; for the list of supported types. |  -  |
**403** | Not authorized. Access not granted for this request |  -  |
**404** | The resource referenced by the request does not exist. |  -  |
**400** | The request is malformed or contains invalid parameters. |  -  |
**409** | The request conflicts with the current state of the resource. |  -  |
**200** | Thread and posts deleted. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete1**
> AckResponse delete1(thread_id)

Delete a thread

Soft-delete a thread. **Cascades** to every post in the thread (also soft-deleted). Documents and embeddings are **not** affected.

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
    api_instance = verbatim_client.ThreadApi(api_client)
    thread_id = UUID('123e4567-e89b-12d3-a456-426614174000') # UUID | ID of the thread to delete.

    try:
        # Delete a thread
        api_response = api_instance.delete1(thread_id)
        print("The response of ThreadApi->delete1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThreadApi->delete1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **thread_id** | **UUID**| ID of the thread to delete. | 

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
**500** | Internal error. Check body to get more info |  -  |
**415** | Content type not accepted by the platform. See &#x60;GET /v1/doc/accept&#x60; for the list of supported types. |  -  |
**403** | Not authorized. Access not granted for this request |  -  |
**404** | The resource referenced by the request does not exist. |  -  |
**400** | The request is malformed or contains invalid parameters. |  -  |
**409** | The request conflicts with the current state of the resource. |  -  |
**200** | Thread and posts deleted. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get**
> Thread get(thread_id)

Get a thread

Fetch a thread's metadata (user, corpora, model, system prompt, parameters). Use `GET /v1/post` to retrieve its posts.

### Example

* Bearer (JWT) Authentication (JWT):
* Api Key Authentication (AccessToken):

```python
import verbatim_client
from verbatim_client.models.thread import Thread
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
    api_instance = verbatim_client.ThreadApi(api_client)
    thread_id = UUID('123e4567-e89b-12d3-a456-426614174000') # UUID | ID of the thread.

    try:
        # Get a thread
        api_response = api_instance.get(thread_id)
        print("The response of ThreadApi->get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThreadApi->get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **thread_id** | **UUID**| ID of the thread. | 

### Return type

[**Thread**](Thread.md)

### Authorization

[JWT](../README.md#JWT), [AccessToken](../README.md#AccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**500** | Internal error. Check body to get more info |  -  |
**415** | Content type not accepted by the platform. See &#x60;GET /v1/doc/accept&#x60; for the list of supported types. |  -  |
**403** | Not authorized. Access not granted for this request |  -  |
**404** | The resource referenced by the request does not exist. |  -  |
**400** | The request is malformed or contains invalid parameters. |  -  |
**409** | The request conflicts with the current state of the resource. |  -  |
**200** | Thread found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get1**
> Thread get1(thread_id)

Get a thread

Fetch a thread's metadata (user, corpora, model, system prompt, parameters). Use `GET /v1/post` to retrieve its posts.

### Example

* Bearer (JWT) Authentication (JWT):
* Api Key Authentication (AccessToken):

```python
import verbatim_client
from verbatim_client.models.thread import Thread
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
    api_instance = verbatim_client.ThreadApi(api_client)
    thread_id = UUID('123e4567-e89b-12d3-a456-426614174000') # UUID | ID of the thread.

    try:
        # Get a thread
        api_response = api_instance.get1(thread_id)
        print("The response of ThreadApi->get1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThreadApi->get1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **thread_id** | **UUID**| ID of the thread. | 

### Return type

[**Thread**](Thread.md)

### Authorization

[JWT](../README.md#JWT), [AccessToken](../README.md#AccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**500** | Internal error. Check body to get more info |  -  |
**415** | Content type not accepted by the platform. See &#x60;GET /v1/doc/accept&#x60; for the list of supported types. |  -  |
**403** | Not authorized. Access not granted for this request |  -  |
**404** | The resource referenced by the request does not exist. |  -  |
**400** | The request is malformed or contains invalid parameters. |  -  |
**409** | The request conflicts with the current state of the resource. |  -  |
**200** | Thread found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list**
> ThreadListResponse list(page_size=page_size, page_index=page_index)

List threads

Paginate every thread of the caller's organization, newest first.

The organization is resolved from the JWT, so there is nothing to pass and no
way to ask for another tenant's threads. A thread belongs to an organization
as soon as one of its corpora does.

The ordering is closed by the thread id, so walking `pageIndex` never shows the
same thread twice nor skips one when several were opened in the same
millisecond. `total` counts every thread in the organization, not just those
returned here.

To narrow the result — by user, by corpus, by metadata, or by any combination of
the three — use `GET /v1/thread/q`, which takes the same paging parameters.


### Example

* Bearer (JWT) Authentication (JWT):
* Api Key Authentication (AccessToken):

```python
import verbatim_client
from verbatim_client.models.thread_list_response import ThreadListResponse
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
    api_instance = verbatim_client.ThreadApi(api_client)
    page_size = 25 # int | Number of items per page, 1-100. (optional) (default to 25)
    page_index = 0 # int | Zero-based page index. (optional) (default to 0)

    try:
        # List threads
        api_response = api_instance.list(page_size=page_size, page_index=page_index)
        print("The response of ThreadApi->list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThreadApi->list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_size** | **int**| Number of items per page, 1-100. | [optional] [default to 25]
 **page_index** | **int**| Zero-based page index. | [optional] [default to 0]

### Return type

[**ThreadListResponse**](ThreadListResponse.md)

### Authorization

[JWT](../README.md#JWT), [AccessToken](../README.md#AccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**500** | Internal error. Check body to get more info |  -  |
**415** | Content type not accepted by the platform. See &#x60;GET /v1/doc/accept&#x60; for the list of supported types. |  -  |
**403** | Not authorized. Access not granted for this request |  -  |
**404** | The resource referenced by the request does not exist. |  -  |
**400** | The request is malformed or contains invalid parameters. |  -  |
**409** | The request conflicts with the current state of the resource. |  -  |
**200** | Page of threads. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list1**
> ThreadListResponse list1(page_size=page_size, page_index=page_index)

List threads

Paginate every thread of the caller's organization, newest first.

The organization is resolved from the JWT, so there is nothing to pass and no
way to ask for another tenant's threads. A thread belongs to an organization
as soon as one of its corpora does.

The ordering is closed by the thread id, so walking `pageIndex` never shows the
same thread twice nor skips one when several were opened in the same
millisecond. `total` counts every thread in the organization, not just those
returned here.

To narrow the result — by user, by corpus, by metadata, or by any combination of
the three — use `GET /v1/thread/q`, which takes the same paging parameters.


### Example

* Bearer (JWT) Authentication (JWT):
* Api Key Authentication (AccessToken):

```python
import verbatim_client
from verbatim_client.models.thread_list_response import ThreadListResponse
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
    api_instance = verbatim_client.ThreadApi(api_client)
    page_size = 25 # int | Number of items per page, 1-100. (optional) (default to 25)
    page_index = 0 # int | Zero-based page index. (optional) (default to 0)

    try:
        # List threads
        api_response = api_instance.list1(page_size=page_size, page_index=page_index)
        print("The response of ThreadApi->list1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThreadApi->list1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_size** | **int**| Number of items per page, 1-100. | [optional] [default to 25]
 **page_index** | **int**| Zero-based page index. | [optional] [default to 0]

### Return type

[**ThreadListResponse**](ThreadListResponse.md)

### Authorization

[JWT](../README.md#JWT), [AccessToken](../README.md#AccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**500** | Internal error. Check body to get more info |  -  |
**415** | Content type not accepted by the platform. See &#x60;GET /v1/doc/accept&#x60; for the list of supported types. |  -  |
**403** | Not authorized. Access not granted for this request |  -  |
**404** | The resource referenced by the request does not exist. |  -  |
**400** | The request is malformed or contains invalid parameters. |  -  |
**409** | The request conflicts with the current state of the resource. |  -  |
**200** | Page of threads. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search**
> ThreadListResponse search(user_id=user_id, corpus_id=corpus_id, key=key, value=value, var_json=var_json, page_size=page_size, page_index=page_index)

Search threads

Find threads of the caller's organization by owner, corpus and metadata.

Every filter is optional and they **narrow together**: a request carrying none of
them returns the whole organization — the same answer as `GET /v1/thread/` —
and one carrying several returns only the threads matching all of them. That is
what this endpoint adds over the `by…` listings it replaces, which each answer
one fixed combination.

The organization is never a parameter. It comes from the JWT and is always
applied, so no combination of filters reaches another tenant's threads.

### Owner — `userId`

Exact match on the identifier carried by the JWT when the thread was opened.
Sent empty (`&userId=`) it is treated as absent rather than as a match on the
empty string.

### Corpus — `corpusId`

Keeps threads bound to that corpus. A thread may be bound to several, and it
matches as soon as one of them is the requested one. The corpus must belong to
the caller's organization.

### Metadata — `key`/`value`, or `json`

Matches threads whose metadata **contains** the fragment (PostgreSQL's `@>`
operator), extra keys on the thread being fine. Pass `key` and `value` for a
single pair — they go together, one without the other is a `400` — or `json`
for a raw object when the filter is nested or has several keys. `json` wins when
both are supplied.

### Ordering and paging

Newest first, closed by the thread id, so walking `pageIndex` never shows the
same thread twice nor skips one. `total` counts every match across all pages.

### Examples

* `?userId=user_42` — every thread that user opened, across corpora
* `?corpusId=…` — every thread opened against one corpus, whoever opened it
* `?userId=user_42&corpusId=…` — both, which `GET /v1/thread/byUser` also did
* `?userId=user_42&key=customer_id&value=42` — the combination none of the
  `by…` endpoints could express
* `?json={"channel":{"kind":"web"}}` — a nested metadata fragment


### Example

* Bearer (JWT) Authentication (JWT):
* Api Key Authentication (AccessToken):

```python
import verbatim_client
from verbatim_client.models.thread_list_response import ThreadListResponse
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
    api_instance = verbatim_client.ThreadApi(api_client)
    user_id = 'user_42' # str | Exact identifier of the user who opened the thread. Blank or omitted, the owner is not filtered. (optional)
    corpus_id = UUID('123e4567-e89b-12d3-a456-426614174000') # UUID | Keep threads bound to this corpus. Must belong to the caller's organization. (optional)
    key = 'customer_id' # str | Metadata key to filter on. Goes together with `value`. (optional)
    value = '42' # str | Metadata value matching `key`. (optional)
    var_json = '{\"customer_id\":\"42\"}' # str | Raw JSON object used as the containment filter. Wins over `key`/`value` when set. (optional)
    page_size = 25 # int | Number of items per page, 1-100. (optional) (default to 25)
    page_index = 0 # int | Zero-based page index. (optional) (default to 0)

    try:
        # Search threads
        api_response = api_instance.search(user_id=user_id, corpus_id=corpus_id, key=key, value=value, var_json=var_json, page_size=page_size, page_index=page_index)
        print("The response of ThreadApi->search:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThreadApi->search: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| Exact identifier of the user who opened the thread. Blank or omitted, the owner is not filtered. | [optional] 
 **corpus_id** | **UUID**| Keep threads bound to this corpus. Must belong to the caller&#39;s organization. | [optional] 
 **key** | **str**| Metadata key to filter on. Goes together with &#x60;value&#x60;. | [optional] 
 **value** | **str**| Metadata value matching &#x60;key&#x60;. | [optional] 
 **var_json** | **str**| Raw JSON object used as the containment filter. Wins over &#x60;key&#x60;/&#x60;value&#x60; when set. | [optional] 
 **page_size** | **int**| Number of items per page, 1-100. | [optional] [default to 25]
 **page_index** | **int**| Zero-based page index. | [optional] [default to 0]

### Return type

[**ThreadListResponse**](ThreadListResponse.md)

### Authorization

[JWT](../README.md#JWT), [AccessToken](../README.md#AccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**500** | Internal error. Check body to get more info |  -  |
**415** | Content type not accepted by the platform. See &#x60;GET /v1/doc/accept&#x60; for the list of supported types. |  -  |
**403** | Not authorized. Access not granted for this request |  -  |
**404** | The resource referenced by the request does not exist. |  -  |
**400** | A metadata filter is malformed, or a paging parameter is out of bounds. |  -  |
**409** | The request conflicts with the current state of the resource. |  -  |
**200** | Page of matching threads. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search1**
> ThreadListResponse search1(user_id=user_id, corpus_id=corpus_id, key=key, value=value, var_json=var_json, page_size=page_size, page_index=page_index)

Search threads

Find threads of the caller's organization by owner, corpus and metadata.

Every filter is optional and they **narrow together**: a request carrying none of
them returns the whole organization — the same answer as `GET /v1/thread/` —
and one carrying several returns only the threads matching all of them. That is
what this endpoint adds over the `by…` listings it replaces, which each answer
one fixed combination.

The organization is never a parameter. It comes from the JWT and is always
applied, so no combination of filters reaches another tenant's threads.

### Owner — `userId`

Exact match on the identifier carried by the JWT when the thread was opened.
Sent empty (`&userId=`) it is treated as absent rather than as a match on the
empty string.

### Corpus — `corpusId`

Keeps threads bound to that corpus. A thread may be bound to several, and it
matches as soon as one of them is the requested one. The corpus must belong to
the caller's organization.

### Metadata — `key`/`value`, or `json`

Matches threads whose metadata **contains** the fragment (PostgreSQL's `@>`
operator), extra keys on the thread being fine. Pass `key` and `value` for a
single pair — they go together, one without the other is a `400` — or `json`
for a raw object when the filter is nested or has several keys. `json` wins when
both are supplied.

### Ordering and paging

Newest first, closed by the thread id, so walking `pageIndex` never shows the
same thread twice nor skips one. `total` counts every match across all pages.

### Examples

* `?userId=user_42` — every thread that user opened, across corpora
* `?corpusId=…` — every thread opened against one corpus, whoever opened it
* `?userId=user_42&corpusId=…` — both, which `GET /v1/thread/byUser` also did
* `?userId=user_42&key=customer_id&value=42` — the combination none of the
  `by…` endpoints could express
* `?json={"channel":{"kind":"web"}}` — a nested metadata fragment


### Example

* Bearer (JWT) Authentication (JWT):
* Api Key Authentication (AccessToken):

```python
import verbatim_client
from verbatim_client.models.thread_list_response import ThreadListResponse
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
    api_instance = verbatim_client.ThreadApi(api_client)
    user_id = 'user_42' # str | Exact identifier of the user who opened the thread. Blank or omitted, the owner is not filtered. (optional)
    corpus_id = UUID('123e4567-e89b-12d3-a456-426614174000') # UUID | Keep threads bound to this corpus. Must belong to the caller's organization. (optional)
    key = 'customer_id' # str | Metadata key to filter on. Goes together with `value`. (optional)
    value = '42' # str | Metadata value matching `key`. (optional)
    var_json = '{customer_id=42}' # str | Raw JSON object used as the containment filter. Wins over `key`/`value` when set. (optional)
    page_size = 25 # int | Number of items per page, 1-100. (optional) (default to 25)
    page_index = 0 # int | Zero-based page index. (optional) (default to 0)

    try:
        # Search threads
        api_response = api_instance.search1(user_id=user_id, corpus_id=corpus_id, key=key, value=value, var_json=var_json, page_size=page_size, page_index=page_index)
        print("The response of ThreadApi->search1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThreadApi->search1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| Exact identifier of the user who opened the thread. Blank or omitted, the owner is not filtered. | [optional] 
 **corpus_id** | **UUID**| Keep threads bound to this corpus. Must belong to the caller&#39;s organization. | [optional] 
 **key** | **str**| Metadata key to filter on. Goes together with &#x60;value&#x60;. | [optional] 
 **value** | **str**| Metadata value matching &#x60;key&#x60;. | [optional] 
 **var_json** | **str**| Raw JSON object used as the containment filter. Wins over &#x60;key&#x60;/&#x60;value&#x60; when set. | [optional] 
 **page_size** | **int**| Number of items per page, 1-100. | [optional] [default to 25]
 **page_index** | **int**| Zero-based page index. | [optional] [default to 0]

### Return type

[**ThreadListResponse**](ThreadListResponse.md)

### Authorization

[JWT](../README.md#JWT), [AccessToken](../README.md#AccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**500** | Internal error. Check body to get more info |  -  |
**415** | Content type not accepted by the platform. See &#x60;GET /v1/doc/accept&#x60; for the list of supported types. |  -  |
**403** | Not authorized. Access not granted for this request |  -  |
**404** | The resource referenced by the request does not exist. |  -  |
**400** | A metadata filter is malformed, or a paging parameter is out of bounds. |  -  |
**409** | The request conflicts with the current state of the resource. |  -  |
**200** | Page of matching threads. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update**
> Thread update(thread_id, thread_update_request)

Update a thread

Patch one or more thread attributes. Only the fields provided in the request body are updated; omitted fields keep their current value. Returns the full updated thread.

### Example

* Bearer (JWT) Authentication (JWT):
* Api Key Authentication (AccessToken):

```python
import verbatim_client
from verbatim_client.models.thread import Thread
from verbatim_client.models.thread_update_request import ThreadUpdateRequest
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
    api_instance = verbatim_client.ThreadApi(api_client)
    thread_id = UUID('123e4567-e89b-12d3-a456-426614174000') # UUID | ID of the thread to update.
    thread_update_request = {"metadata":{"customer_id":"42","ticket":"SUPP-999"}} # ThreadUpdateRequest | 

    try:
        # Update a thread
        api_response = api_instance.update(thread_id, thread_update_request)
        print("The response of ThreadApi->update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThreadApi->update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **thread_id** | **UUID**| ID of the thread to update. | 
 **thread_update_request** | [**ThreadUpdateRequest**](ThreadUpdateRequest.md)|  | 

### Return type

[**Thread**](Thread.md)

### Authorization

[JWT](../README.md#JWT), [AccessToken](../README.md#AccessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**500** | Internal error. Check body to get more info |  -  |
**415** | Content type not accepted by the platform. See &#x60;GET /v1/doc/accept&#x60; for the list of supported types. |  -  |
**403** | Not authorized. Access not granted for this request |  -  |
**404** | The resource referenced by the request does not exist. |  -  |
**400** | The request is malformed or contains invalid parameters. |  -  |
**409** | The request conflicts with the current state of the resource. |  -  |
**200** | Thread updated. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update1**
> Thread update1(thread_id, thread_update_request)

Update a thread

Patch one or more thread attributes. Only the fields provided in the request body are updated; omitted fields keep their current value. Returns the full updated thread.

### Example

* Bearer (JWT) Authentication (JWT):
* Api Key Authentication (AccessToken):

```python
import verbatim_client
from verbatim_client.models.thread import Thread
from verbatim_client.models.thread_update_request import ThreadUpdateRequest
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
    api_instance = verbatim_client.ThreadApi(api_client)
    thread_id = UUID('123e4567-e89b-12d3-a456-426614174000') # UUID | ID of the thread to update.
    thread_update_request = {metadata={customer_id=42, ticket=SUPP-999}} # ThreadUpdateRequest | 

    try:
        # Update a thread
        api_response = api_instance.update1(thread_id, thread_update_request)
        print("The response of ThreadApi->update1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThreadApi->update1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **thread_id** | **UUID**| ID of the thread to update. | 
 **thread_update_request** | [**ThreadUpdateRequest**](ThreadUpdateRequest.md)|  | 

### Return type

[**Thread**](Thread.md)

### Authorization

[JWT](../README.md#JWT), [AccessToken](../README.md#AccessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**500** | Internal error. Check body to get more info |  -  |
**415** | Content type not accepted by the platform. See &#x60;GET /v1/doc/accept&#x60; for the list of supported types. |  -  |
**403** | Not authorized. Access not granted for this request |  -  |
**404** | The resource referenced by the request does not exist. |  -  |
**400** | The request is malformed or contains invalid parameters. |  -  |
**409** | The request conflicts with the current state of the resource. |  -  |
**200** | Thread updated. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

