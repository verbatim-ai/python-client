# verbatim_client.CorpusApi

All URIs are relative to *http://localhost:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create1**](CorpusApi.md#create1) | **POST** /v1/corpus/ | Create a corpus
[**delete**](CorpusApi.md#delete) | **DELETE** /v1/corpus/{corpusId} | Delete a corpus
[**get**](CorpusApi.md#get) | **GET** /v1/corpus/{corpusId} | Get a corpus
[**list1**](CorpusApi.md#list1) | **GET** /v1/corpus/ | List corpora
[**update**](CorpusApi.md#update) | **PATCH** /v1/corpus/{corpusId} | Update a corpus
[**update_legacy**](CorpusApi.md#update_legacy) | **PUT** /v1/corpus/{corpusId} | Update a corpus (deprecated)


# **create1**
> CorpusCreateResponse create1(corpus_create_request)

Create a corpus

Create a new corpus inside an organization. The embedding model and summary LLM are locked at creation time and used for every document ingested afterwards.

### Example

* Bearer (JWT) Authentication (JWT):
* Api Key Authentication (AccessToken):

```python
import verbatim_client
from verbatim_client.models.corpus_create_request import CorpusCreateRequest
from verbatim_client.models.corpus_create_response import CorpusCreateResponse
from verbatim_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = verbatim_client.Configuration(
    host = "http://localhost:8080"
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
    api_instance = verbatim_client.CorpusApi(api_client)
    corpus_create_request = {"name":"Support knowledge base","description":"Tickets, FAQs and runbooks used by the support team.","metadata":{"owner":"support-team","language":"fr"}} # CorpusCreateRequest | 

    try:
        # Create a corpus
        api_response = api_instance.create1(corpus_create_request)
        print("The response of CorpusApi->create1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CorpusApi->create1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **corpus_create_request** | [**CorpusCreateRequest**](CorpusCreateRequest.md)|  | 

### Return type

[**CorpusCreateResponse**](CorpusCreateResponse.md)

### Authorization

[JWT](../README.md#JWT), [AccessToken](../README.md#AccessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**500** | Internal error. Check body to get more info |  -  |
**403** | Not authorized. Access not granted for this request |  -  |
**404** | The resource referenced by the request does not exist. |  -  |
**400** | The request is malformed or contains invalid parameters. |  -  |
**409** | The request conflicts with the current state of the resource. |  -  |
**415** | Content type not accepted by the platform. See &#x60;GET /v1/doc/accept&#x60; for the list of supported types. |  -  |
**200** | Corpus created. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete**
> AckResponse delete(corpus_id)

Delete a corpus

Permanently delete a corpus. **Cascades** to every session, post, document and embedding owned by this corpus. This operation cannot be undone.

### Example

* Bearer (JWT) Authentication (JWT):
* Api Key Authentication (AccessToken):

```python
import verbatim_client
from verbatim_client.models.ack_response import AckResponse
from verbatim_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = verbatim_client.Configuration(
    host = "http://localhost:8080"
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
    api_instance = verbatim_client.CorpusApi(api_client)
    corpus_id = UUID('123e4567-e89b-12d3-a456-426614174000') # UUID | ID of the corpus to delete.

    try:
        # Delete a corpus
        api_response = api_instance.delete(corpus_id)
        print("The response of CorpusApi->delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CorpusApi->delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **corpus_id** | **UUID**| ID of the corpus to delete. | 

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
**403** | Not authorized. Access not granted for this request |  -  |
**404** | The resource referenced by the request does not exist. |  -  |
**400** | The request is malformed or contains invalid parameters. |  -  |
**409** | The request conflicts with the current state of the resource. |  -  |
**415** | Content type not accepted by the platform. See &#x60;GET /v1/doc/accept&#x60; for the list of supported types. |  -  |
**200** | Corpus and dependencies deleted. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get**
> CorpusItemResponse get(corpus_id)

Get a corpus

Fetch a corpus by its identifier.

### Example

* Bearer (JWT) Authentication (JWT):
* Api Key Authentication (AccessToken):

```python
import verbatim_client
from verbatim_client.models.corpus_item_response import CorpusItemResponse
from verbatim_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = verbatim_client.Configuration(
    host = "http://localhost:8080"
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
    api_instance = verbatim_client.CorpusApi(api_client)
    corpus_id = UUID('123e4567-e89b-12d3-a456-426614174000') # UUID | ID of the corpus.

    try:
        # Get a corpus
        api_response = api_instance.get(corpus_id)
        print("The response of CorpusApi->get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CorpusApi->get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **corpus_id** | **UUID**| ID of the corpus. | 

### Return type

[**CorpusItemResponse**](CorpusItemResponse.md)

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
**400** | The request is malformed or contains invalid parameters. |  -  |
**409** | The request conflicts with the current state of the resource. |  -  |
**415** | Content type not accepted by the platform. See &#x60;GET /v1/doc/accept&#x60; for the list of supported types. |  -  |
**200** | Corpus found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list1**
> CorpusListResponse list1(page_size=page_size, page_index=page_index)

List corpora

Paginate corpora belonging to an organization.

### Example

* Bearer (JWT) Authentication (JWT):
* Api Key Authentication (AccessToken):

```python
import verbatim_client
from verbatim_client.models.corpus_list_response import CorpusListResponse
from verbatim_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = verbatim_client.Configuration(
    host = "http://localhost:8080"
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
    api_instance = verbatim_client.CorpusApi(api_client)
    page_size = 25 # int | Number of items per page. (optional) (default to 25)
    page_index = 0 # int | Zero-based page index. (optional) (default to 0)

    try:
        # List corpora
        api_response = api_instance.list1(page_size=page_size, page_index=page_index)
        print("The response of CorpusApi->list1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CorpusApi->list1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_size** | **int**| Number of items per page. | [optional] [default to 25]
 **page_index** | **int**| Zero-based page index. | [optional] [default to 0]

### Return type

[**CorpusListResponse**](CorpusListResponse.md)

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
**400** | The request is malformed or contains invalid parameters. |  -  |
**409** | The request conflicts with the current state of the resource. |  -  |
**415** | Content type not accepted by the platform. See &#x60;GET /v1/doc/accept&#x60; for the list of supported types. |  -  |
**200** | Page of corpora. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update**
> CorpusUpdateResponse update(corpus_id, corpus_update_request)

Update a corpus

Patch the name, description or metadata of an existing corpus. Only the fields present
in the request body are updated; omitted fields keep their current value.

`metadata` **replaces** the stored map when provided — merge client-side if you want to
preserve existing keys.

Changing models does **not** re-process already-ingested documents.


### Example

* Bearer (JWT) Authentication (JWT):
* Api Key Authentication (AccessToken):

```python
import verbatim_client
from verbatim_client.models.corpus_update_request import CorpusUpdateRequest
from verbatim_client.models.corpus_update_response import CorpusUpdateResponse
from verbatim_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = verbatim_client.Configuration(
    host = "http://localhost:8080"
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
    api_instance = verbatim_client.CorpusApi(api_client)
    corpus_id = UUID('123e4567-e89b-12d3-a456-426614174000') # UUID | ID of the corpus to update.
    corpus_update_request = {"description":"Tickets, FAQs and runbooks used by the support team (v2)."} # CorpusUpdateRequest | 

    try:
        # Update a corpus
        api_response = api_instance.update(corpus_id, corpus_update_request)
        print("The response of CorpusApi->update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CorpusApi->update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **corpus_id** | **UUID**| ID of the corpus to update. | 
 **corpus_update_request** | [**CorpusUpdateRequest**](CorpusUpdateRequest.md)|  | 

### Return type

[**CorpusUpdateResponse**](CorpusUpdateResponse.md)

### Authorization

[JWT](../README.md#JWT), [AccessToken](../README.md#AccessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**500** | Internal error. Check body to get more info |  -  |
**403** | Not authorized. Access not granted for this request |  -  |
**404** | The resource referenced by the request does not exist. |  -  |
**400** | The request is malformed or contains invalid parameters. |  -  |
**409** | The request conflicts with the current state of the resource. |  -  |
**415** | Content type not accepted by the platform. See &#x60;GET /v1/doc/accept&#x60; for the list of supported types. |  -  |
**200** | Corpus updated. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_legacy**
> CorpusUpdateResponse update_legacy(corpus_id, corpus_update_request)

Update a corpus (deprecated)

**Deprecated — use `PATCH /v1/corpus/{corpusId}` instead.**

Kept for backward compatibility and strictly equivalent to the `PATCH` operation:
despite the `PUT` verb, omitted fields are **not** reset, they keep their current
value. That partial-update semantic is what `PATCH` expresses correctly, hence the
move. This operation will be removed in a future release.


### Example

* Bearer (JWT) Authentication (JWT):
* Api Key Authentication (AccessToken):

```python
import verbatim_client
from verbatim_client.models.corpus_update_request import CorpusUpdateRequest
from verbatim_client.models.corpus_update_response import CorpusUpdateResponse
from verbatim_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = verbatim_client.Configuration(
    host = "http://localhost:8080"
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
    api_instance = verbatim_client.CorpusApi(api_client)
    corpus_id = UUID('123e4567-e89b-12d3-a456-426614174000') # UUID | ID of the corpus to update.
    corpus_update_request = verbatim_client.CorpusUpdateRequest() # CorpusUpdateRequest | 

    try:
        # Update a corpus (deprecated)
        api_response = api_instance.update_legacy(corpus_id, corpus_update_request)
        print("The response of CorpusApi->update_legacy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CorpusApi->update_legacy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **corpus_id** | **UUID**| ID of the corpus to update. | 
 **corpus_update_request** | [**CorpusUpdateRequest**](CorpusUpdateRequest.md)|  | 

### Return type

[**CorpusUpdateResponse**](CorpusUpdateResponse.md)

### Authorization

[JWT](../README.md#JWT), [AccessToken](../README.md#AccessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**500** | Internal error. Check body to get more info |  -  |
**403** | Not authorized. Access not granted for this request |  -  |
**404** | The resource referenced by the request does not exist. |  -  |
**400** | The request is malformed or contains invalid parameters. |  -  |
**409** | The request conflicts with the current state of the resource. |  -  |
**415** | Content type not accepted by the platform. See &#x60;GET /v1/doc/accept&#x60; for the list of supported types. |  -  |
**200** | Corpus updated. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

