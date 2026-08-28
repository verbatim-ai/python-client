# verbatim_client.PostApi

All URIs are relative to *https://api.verbatim-ai.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**attachment**](PostApi.md#attachment) | **GET** /v1/post/attachment/{postId} | Attachments from a post
[**delete4**](PostApi.md#delete4) | **DELETE** /v1/post/{postId} | Delete a post
[**download_url**](PostApi.md#download_url) | **GET** /v1/post/attachment/{docId}/download-url | Get a presigned download URL
[**get4**](PostApi.md#get4) | **GET** /v1/post/{postId} | Get a post
[**list3**](PostApi.md#list3) | **GET** /v1/post/ | List posts
[**preview_urls**](PostApi.md#preview_urls) | **GET** /v1/post/attachment/{docId}/preview-urls | Get presigned preview URLs
[**query**](PostApi.md#query) | **GET** /v1/post/q | Send a query


# **attachment**
> PostAttachmentResponse attachment(post_id)

Attachments from a post

List the attachments from a post.

### Example

* Bearer (JWT) Authentication (JWT):
* Api Key Authentication (AccessToken):

```python
import verbatim_client
from verbatim_client.models.post_attachment_response import PostAttachmentResponse
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
    api_instance = verbatim_client.PostApi(api_client)
    post_id = UUID('123e4567-e89b-12d3-a456-426614174000') # UUID | ID of the post.

    try:
        # Attachments from a post
        api_response = api_instance.attachment(post_id)
        print("The response of PostApi->attachment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PostApi->attachment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_id** | **UUID**| ID of the post. | 

### Return type

[**PostAttachmentResponse**](PostAttachmentResponse.md)

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
**200** | Attachments found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete4**
> AckResponse delete4(post_id)

Delete a post

Permanently delete a post and its attachments. Documents and embeddings referenced by the attachments are **not** affected.

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
    api_instance = verbatim_client.PostApi(api_client)
    post_id = UUID('123e4567-e89b-12d3-a456-426614174000') # UUID | ID of the post to delete.

    try:
        # Delete a post
        api_response = api_instance.delete4(post_id)
        print("The response of PostApi->delete4:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PostApi->delete4: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_id** | **UUID**| ID of the post to delete. | 

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
**200** | Post deleted. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_url**
> DocumentDownloadUrl download_url(doc_id)

Get a presigned download URL

Return a time-limited presigned URL the client can use to GET the document content directly
from the storage backend (S3) — no content flows through this server.

The URL is bound to the document's content type; clients SHOULD use the returned
`filename` for the local save name.


### Example

* Bearer (JWT) Authentication (JWT):
* Api Key Authentication (AccessToken):

```python
import verbatim_client
from verbatim_client.models.document_download_url import DocumentDownloadUrl
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
    api_instance = verbatim_client.PostApi(api_client)
    doc_id = UUID('123e4567-e89b-12d3-a456-426614174000') # UUID | ID of the document.

    try:
        # Get a presigned download URL
        api_response = api_instance.download_url(doc_id)
        print("The response of PostApi->download_url:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PostApi->download_url: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **doc_id** | **UUID**| ID of the document. | 

### Return type

[**DocumentDownloadUrl**](DocumentDownloadUrl.md)

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
**200** | Presigned URL issued. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get4**
> Post get4(post_id)

Get a post

Fetch a single post by its identifier. The response carries `attachment`, the number of source chunks behind it; the sources themselves come from `GET /v1/post/attachment/{postId}`.

### Example

* Bearer (JWT) Authentication (JWT):
* Api Key Authentication (AccessToken):

```python
import verbatim_client
from verbatim_client.models.post import Post
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
    api_instance = verbatim_client.PostApi(api_client)
    post_id = UUID('123e4567-e89b-12d3-a456-426614174000') # UUID | ID of the post.

    try:
        # Get a post
        api_response = api_instance.get4(post_id)
        print("The response of PostApi->get4:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PostApi->get4: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_id** | **UUID**| ID of the post. | 

### Return type

[**Post**](Post.md)

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
**200** | Post found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list3**
> PostListResponse list3(session_id, page_size=page_size, page_index=page_index)

List posts

Paginate every post (user queries and system answers) in a session, newest first.

### Example

* Bearer (JWT) Authentication (JWT):
* Api Key Authentication (AccessToken):

```python
import verbatim_client
from verbatim_client.models.post_list_response import PostListResponse
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
    api_instance = verbatim_client.PostApi(api_client)
    session_id = UUID('123e4567-e89b-12d3-a456-426614174000') # UUID | ID of the session.
    page_size = 25 # int | Number of items per page. (optional) (default to 25)
    page_index = 0 # int | Zero-based page index. (optional) (default to 0)

    try:
        # List posts
        api_response = api_instance.list3(session_id, page_size=page_size, page_index=page_index)
        print("The response of PostApi->list3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PostApi->list3: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **UUID**| ID of the session. | 
 **page_size** | **int**| Number of items per page. | [optional] [default to 25]
 **page_index** | **int**| Zero-based page index. | [optional] [default to 0]

### Return type

[**PostListResponse**](PostListResponse.md)

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
**200** | Page of posts. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **preview_urls**
> DocumentPreviewUrls preview_urls(doc_id, pages)

Get presigned preview URLs

Return time-limited presigned URLs for the rendered preview images of the document.

`pages` is **required** and selects the zero-based page indices to issue URLs for:
at least one, at most 10 per request — `400` otherwise. Repeat the parameter for
several values (`pages=0&pages=2`) or send them comma-separated (`pages=0,2`).
Duplicates are preserved as supplied and count towards the limit. Paginate over a
long document with several calls rather than asking for every page at once.

Every index must address a page of *that* document: negatives are rejected, and
so is anything at or past its page count once that count is known (`nbPages` from
`GET /v1/doc/{id}`, `0` while the rendering pipeline has not reported it).

One entry is issued per (page, size) over {SMALL, MEDIUM}, so a call returns
`2 × pages` entries — at most 20.

The URLs point at preview images produced asynchronously by the rendering pipeline.
No existence check is performed — individual URLs MAY return 404 when fetched if the
corresponding (page, size) hasn't been generated yet; clients SHOULD fall back per-tile.


### Example

* Bearer (JWT) Authentication (JWT):
* Api Key Authentication (AccessToken):

```python
import verbatim_client
from verbatim_client.models.document_preview_urls import DocumentPreviewUrls
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
    api_instance = verbatim_client.PostApi(api_client)
    doc_id = UUID('123e4567-e89b-12d3-a456-426614174000') # UUID | ID of the document.
    pages = [[0]] # List[int] | Zero-based page indices to issue preview URLs for. Required: 1 to 10 values per request, each within the document's page range. Repeat for multiple values: `pages=0&pages=2`.

    try:
        # Get presigned preview URLs
        api_response = api_instance.preview_urls(doc_id, pages)
        print("The response of PostApi->preview_urls:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PostApi->preview_urls: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **doc_id** | **UUID**| ID of the document. | 
 **pages** | [**List[int]**](int.md)| Zero-based page indices to issue preview URLs for. Required: 1 to 10 values per request, each within the document&#39;s page range. Repeat for multiple values: &#x60;pages&#x3D;0&amp;pages&#x3D;2&#x60;. | 

### Return type

[**DocumentPreviewUrls**](DocumentPreviewUrls.md)

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
**400** | &#x60;pages&#x60; is missing, empty, carries more than 10 indices, or names a page outside the document. |  -  |
**409** | The request conflicts with the current state of the resource. |  -  |
**200** | Presigned preview URLs issued. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query**
> PostItemResponse query(session_id, body, lang=lang, agent_id=agent_id)

Send a query

Submit a user message to a session and run the full RAG pipeline:

1. Persist the query as a post with `owner = USER`.
2. Vectorize the query and run a cosine-similarity search against the session's corpora.
3. Feed the top chunks to the session's LLM as context.
4. Persist the answer as a post with `owner = SYSTEM`, with attachments pointing to the chunks used.

The response contains both the user post (`query`) and the system post (`answer`).

### Choosing an agent

How much of that pipeline runs, and how, is decided by an **agent** — retrieval width,
whether the chunks are re-ranked, the system instruction, how much of the conversation is
replayed, and which model answers. See `GET /v1/agent/`.

Omit `agentId` and the query runs on the platform default agent, which is what every query
did before agents existed. Pass one to run this single query under a different setup:

```
GET /v1/post/q?sessionId=$SESSION_ID&body=What+is+the+refund+policy%3F&agentId=$AGENT_ID
```

The choice is **per query, not per session** — the next query on the same session is
independent, so a client can escalate one question to a wider, slower agent without
changing the conversation it belongs to.

The agent is then recorded on the answer as `agentId`, and only on the answer: the user's
question is not something an agent produced. A missing `agentId` on an answer therefore
means "ran on the default agent", not "unknown". Deleting an agent does not rewrite the
answers it produced, so this still names an agent you have since deleted — resolving that
id through `GET /v1/agent/{agentId}` answers `404`, which is the honest reading.

An `agentId` your organization cannot see — someone else's, or one that never existed —
answers `404` and no post is written.


### Example

* Bearer (JWT) Authentication (JWT):
* Api Key Authentication (AccessToken):

```python
import verbatim_client
from verbatim_client.models.post_item_response import PostItemResponse
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
    api_instance = verbatim_client.PostApi(api_client)
    session_id = UUID('123e4567-e89b-12d3-a456-426614174000') # UUID | ID of the session to post the query into.
    body = 'What is the main topic of the corpus?' # str | User message to send to the LLM.
    lang = 'fr' # str | ISO-639 language code used by the LLM. Defaults to `en`. (optional)
    agent_id = UUID('123e4567-e89b-12d3-a456-426614174000') # UUID | Agent to run this query under. Omit to use the platform default agent. Must be one of the agents `GET /v1/agent/` lists for your organization. (optional)

    try:
        # Send a query
        api_response = api_instance.query(session_id, body, lang=lang, agent_id=agent_id)
        print("The response of PostApi->query:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PostApi->query: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **UUID**| ID of the session to post the query into. | 
 **body** | **str**| User message to send to the LLM. | 
 **lang** | **str**| ISO-639 language code used by the LLM. Defaults to &#x60;en&#x60;. | [optional] 
 **agent_id** | **UUID**| Agent to run this query under. Omit to use the platform default agent. Must be one of the agents &#x60;GET /v1/agent/&#x60; lists for your organization. | [optional] 

### Return type

[**PostItemResponse**](PostItemResponse.md)

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
**200** | Query processed and answer returned. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

