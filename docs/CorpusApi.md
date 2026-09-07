# verbatim_client.CorpusApi

All URIs are relative to *https://api.verbatim-ai.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create2**](CorpusApi.md#create2) | **POST** /v1/corpus/ | Create a corpus
[**delete3**](CorpusApi.md#delete3) | **DELETE** /v1/corpus/{corpusId} | Delete a corpus
[**get3**](CorpusApi.md#get3) | **GET** /v1/corpus/{corpusId} | Get a corpus
[**list2**](CorpusApi.md#list2) | **GET** /v1/corpus/ | List corpora
[**update3**](CorpusApi.md#update3) | **PATCH** /v1/corpus/{corpusId} | Update a corpus


# **create2**
> CorpusCreateResponse create2(corpus_create_request)

Create a corpus

Create a new corpus inside an organization. The organization is taken from your token, so there is nothing to pass: a corpus needs only a name, and optionally a description and metadata.

### Example

* Bearer (JWT) Authentication (JWT):
* Api Key Authentication (AccessToken):

```python
import verbatim_client
from verbatim_client.models.corpus_create_request import CorpusCreateRequest
from verbatim_client.models.corpus_create_response import CorpusCreateResponse
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
    api_instance = verbatim_client.CorpusApi(api_client)
    corpus_create_request = {"name":"Support knowledge base","description":"Tickets, FAQs and runbooks used by the support team.","metadata":{"owner":"support-team","language":"fr"}} # CorpusCreateRequest | 

    try:
        # Create a corpus
        api_response = api_instance.create2(corpus_create_request)
        print("The response of CorpusApi->create2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CorpusApi->create2: %s\n" % e)
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
**415** | Content type not accepted by the platform. See &#x60;GET /v1/doc/accept&#x60; for the list of supported types. |  -  |
**403** | Not authorized. Access not granted for this request |  -  |
**404** | The resource referenced by the request does not exist. |  -  |
**400** | The request is malformed or contains invalid parameters. |  -  |
**409** | The request conflicts with the current state of the resource. |  -  |
**200** | Corpus created. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete3**
> AckResponse delete3(corpus_id)

Delete a corpus

Delete a corpus.

**This is a soft delete, and it cascades** to every document owned by this
corpus and to every chunk those documents were split into. All of it disappears
from the API together and stops being retrievable, while nothing is destroyed
underneath: archived files and chunk texts are kept. There is no endpoint that
undoes it.


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
    api_instance = verbatim_client.CorpusApi(api_client)
    corpus_id = UUID('123e4567-e89b-12d3-a456-426614174000') # UUID | ID of the corpus to delete.

    try:
        # Delete a corpus
        api_response = api_instance.delete3(corpus_id)
        print("The response of CorpusApi->delete3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CorpusApi->delete3: %s\n" % e)
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
**415** | Content type not accepted by the platform. See &#x60;GET /v1/doc/accept&#x60; for the list of supported types. |  -  |
**403** | Not authorized. Access not granted for this request |  -  |
**404** | The resource referenced by the request does not exist. |  -  |
**400** | The request is malformed or contains invalid parameters. |  -  |
**409** | The request conflicts with the current state of the resource. |  -  |
**200** | Corpus and dependencies deleted. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get3**
> CorpusItemResponse get3(corpus_id)

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
    api_instance = verbatim_client.CorpusApi(api_client)
    corpus_id = UUID('123e4567-e89b-12d3-a456-426614174000') # UUID | ID of the corpus.

    try:
        # Get a corpus
        api_response = api_instance.get3(corpus_id)
        print("The response of CorpusApi->get3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CorpusApi->get3: %s\n" % e)
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
**415** | Content type not accepted by the platform. See &#x60;GET /v1/doc/accept&#x60; for the list of supported types. |  -  |
**403** | Not authorized. Access not granted for this request |  -  |
**404** | The resource referenced by the request does not exist. |  -  |
**400** | The request is malformed or contains invalid parameters. |  -  |
**409** | The request conflicts with the current state of the resource. |  -  |
**200** | Corpus found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list2**
> CorpusListResponse list2(page_size=page_size, page_index=page_index)

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
    api_instance = verbatim_client.CorpusApi(api_client)
    page_size = 25 # int | Number of items per page. (optional) (default to 25)
    page_index = 0 # int | Zero-based page index. (optional) (default to 0)

    try:
        # List corpora
        api_response = api_instance.list2(page_size=page_size, page_index=page_index)
        print("The response of CorpusApi->list2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CorpusApi->list2: %s\n" % e)
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
**415** | Content type not accepted by the platform. See &#x60;GET /v1/doc/accept&#x60; for the list of supported types. |  -  |
**403** | Not authorized. Access not granted for this request |  -  |
**404** | The resource referenced by the request does not exist. |  -  |
**400** | The request is malformed or contains invalid parameters. |  -  |
**409** | The request conflicts with the current state of the resource. |  -  |
**200** | Page of corpora. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update3**
> CorpusUpdateResponse update3(corpus_id, corpus_update_request)

Update a corpus

Patch the name, description or metadata of an existing corpus. Only the fields present
in the request body are updated; omitted fields keep their current value.

`metadata` **replaces** the stored map when provided — merge client-side if you want to
preserve existing keys.

Nothing patchable here changes how the corpus behaves: retrieval and the models that
answer belong to the agent named on each query, so no edit re-processes documents or
affects queries already running.


### Example

* Bearer (JWT) Authentication (JWT):
* Api Key Authentication (AccessToken):

```python
import verbatim_client
from verbatim_client.models.corpus_update_request import CorpusUpdateRequest
from verbatim_client.models.corpus_update_response import CorpusUpdateResponse
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
    api_instance = verbatim_client.CorpusApi(api_client)
    corpus_id = UUID('123e4567-e89b-12d3-a456-426614174000') # UUID | ID of the corpus to update.
    corpus_update_request = {"description":"Tickets, FAQs and runbooks used by the support team (v2)."} # CorpusUpdateRequest | 

    try:
        # Update a corpus
        api_response = api_instance.update3(corpus_id, corpus_update_request)
        print("The response of CorpusApi->update3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CorpusApi->update3: %s\n" % e)
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
**415** | Content type not accepted by the platform. See &#x60;GET /v1/doc/accept&#x60; for the list of supported types. |  -  |
**403** | Not authorized. Access not granted for this request |  -  |
**404** | The resource referenced by the request does not exist. |  -  |
**400** | The request is malformed or contains invalid parameters. |  -  |
**409** | The request conflicts with the current state of the resource. |  -  |
**200** | Corpus updated. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

