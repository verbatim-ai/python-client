# verbatim_client.DocumentApi

All URIs are relative to *https://api.verbatim-ai.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**commit_upload**](DocumentApi.md#commit_upload) | **POST** /v1/doc/{id}/commit | Commit a previously initialized upload
[**delete1**](DocumentApi.md#delete1) | **DELETE** /v1/doc/{id} | Delete a document
[**download_url1**](DocumentApi.md#download_url1) | **GET** /v1/doc/{id}/download-url | Get a presigned download URL
[**get1**](DocumentApi.md#get1) | **GET** /v1/doc/{id} | Get a document
[**init_upload**](DocumentApi.md#init_upload) | **POST** /v1/doc/init | Initialize a direct-to-storage upload
[**list4**](DocumentApi.md#list4) | **GET** /v1/doc/ | List documents
[**list_supported_documents**](DocumentApi.md#list_supported_documents) | **GET** /v1/doc/accept | List accepted content types
[**preview_urls1**](DocumentApi.md#preview_urls1) | **GET** /v1/doc/{id}/preview-urls | Get presigned preview URLs
[**reinit_upload**](DocumentApi.md#reinit_upload) | **PUT** /v1/doc/{id}/init | Re-initialize a document for a new upload
[**search1**](DocumentApi.md#search1) | **GET** /v1/doc/q | Search documents
[**status**](DocumentApi.md#status) | **GET** /v1/doc/{id}/status | Get a document&#39;s status
[**summary**](DocumentApi.md#summary) | **GET** /v1/doc/{id}/summary | Get a document summary
[**update1**](DocumentApi.md#update1) | **PATCH** /v1/doc/{id} | Update a document


# **commit_upload**
> Document commit_upload(id)

Commit a previously initialized upload

Step 2 of the upload flow. Confirms that the file has been PUT to the presigned URL returned
by `POST /v1/doc/init` and **asynchronously** triggers ingestion (markdown conversion,
summarization, chunking, embedding).

Before queuing, the server validates the uploaded object: it must exist, declare a supported
content type, fit under the per-document size limit, and not already be present in the same
corpus (duplicate detection by content hash).

The response is returned as soon as the document is moved to `PROCESSING`. Poll
`GET /v1/doc/{id}/status` to observe the final `READY` or `FAILED` status.

Idempotent: committing a document already in `READY` status returns the current state unchanged.


### Example

* Bearer (JWT) Authentication (JWT):
* Api Key Authentication (AccessToken):

```python
import verbatim_client
from verbatim_client.models.document import Document
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
    api_instance = verbatim_client.DocumentApi(api_client)
    id = UUID('123e4567-e89b-12d3-a456-426614174000') # UUID | ID of the document returned by `POST /v1/doc/init`.

    try:
        # Commit a previously initialized upload
        api_response = api_instance.commit_upload(id)
        print("The response of DocumentApi->commit_upload:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentApi->commit_upload: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**| ID of the document returned by &#x60;POST /v1/doc/init&#x60;. | 

### Return type

[**Document**](Document.md)

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
**202** | Ingestion queued. Document moved to PROCESSING. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete1**
> AckResponse delete1(id)

Delete a document

Permanently remove a document from its corpus. **Cascades** to all embeddings and attachments referencing this document. This operation cannot be undone.

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
    api_instance = verbatim_client.DocumentApi(api_client)
    id = UUID('123e4567-e89b-12d3-a456-426614174000') # UUID | ID of the document to delete.

    try:
        # Delete a document
        api_response = api_instance.delete1(id)
        print("The response of DocumentApi->delete1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentApi->delete1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**| ID of the document to delete. | 

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
**200** | Document and dependencies deleted. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_url1**
> DocumentDownloadUrl download_url1(id)

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
    api_instance = verbatim_client.DocumentApi(api_client)
    id = UUID('123e4567-e89b-12d3-a456-426614174000') # UUID | ID of the document.

    try:
        # Get a presigned download URL
        api_response = api_instance.download_url1(id)
        print("The response of DocumentApi->download_url1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentApi->download_url1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**| ID of the document. | 

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

# **get1**
> Document get1(id)

Get a document

Return the metadata of a document by its ID, including provider, language and arbitrary metadata.

### Example

* Bearer (JWT) Authentication (JWT):
* Api Key Authentication (AccessToken):

```python
import verbatim_client
from verbatim_client.models.document import Document
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
    api_instance = verbatim_client.DocumentApi(api_client)
    id = UUID('123e4567-e89b-12d3-a456-426614174000') # UUID | ID of the document.

    try:
        # Get a document
        api_response = api_instance.get1(id)
        print("The response of DocumentApi->get1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentApi->get1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**| ID of the document. | 

### Return type

[**Document**](Document.md)

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
**200** | Document found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **init_upload**
> DocumentInit init_upload(document_init_request)

Initialize a direct-to-storage upload

Step 1 of the upload flow. Validates inputs, creates a document in `AWAITING_UPLOAD` status,
and returns a single-use presigned PUT URL the client must use to push the file bytes
directly to S3 — no content flows through this server.

The returned `uploadUrl` is bound to the requested `contentType`: the client MUST send a
matching `Content-Type` header in the PUT request, or S3 will reject it.

After the PUT succeeds, call `POST /v1/doc/{id}/commit` to trigger ingestion.

Accepted content types are listed by `GET /v1/doc/accept`.

Two optional fields shape what happens later: `tags` classifies the document so
`GET /v1/doc/?tags=…` can find it, and `chunk` overrides how ingestion splits it
into embeddable pieces. `chunk` accepts the Unstructured chunking options
(`strategy`, `max_characters`, `overlap`, …) — see the request schema for the
full key reference, and the *Chunking* examples below for the three shapes that
cover most documents. Omit `chunk` and the platform default applies
(`by_title`, `max_characters: 10000`, `combine_text_under_n_chars: 1000`).


### Example

* Bearer (JWT) Authentication (JWT):
* Api Key Authentication (AccessToken):

```python
import verbatim_client
from verbatim_client.models.document_init import DocumentInit
from verbatim_client.models.document_init_request import DocumentInitRequest
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
    api_instance = verbatim_client.DocumentApi(api_client)
    document_init_request = {"corpusId":"550e8400-e29b-41d4-a716-446655440001","filename":"annual-report-2025.pdf","contentType":"application/pdf"} # DocumentInitRequest | 

    try:
        # Initialize a direct-to-storage upload
        api_response = api_instance.init_upload(document_init_request)
        print("The response of DocumentApi->init_upload:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentApi->init_upload: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_init_request** | [**DocumentInitRequest**](DocumentInitRequest.md)|  | 

### Return type

[**DocumentInit**](DocumentInit.md)

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
**200** | Document created in AWAITING_UPLOAD status. PUT the file to &#x60;uploadUrl&#x60;. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list4**
> DocumentListResponse list4(corpus_id, status=status, tags=tags, page_size=page_size, page_index=page_index)

List documents

Paginate documents stored in a corpus. Pass the optional `status` filter to narrow
down by lifecycle state — e.g. `status=PENDING` returns the ingestion backlog,
`status=FAILED` returns documents that need attention.

Pass `tags` to keep only documents carrying **at least one** of the given tags
(repeat the parameter for several: `tags=legal&tags=2026`). Combining `status` and
`tags` narrows on both.


### Example

* Bearer (JWT) Authentication (JWT):
* Api Key Authentication (AccessToken):

```python
import verbatim_client
from verbatim_client.models.document_list_response import DocumentListResponse
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
    api_instance = verbatim_client.DocumentApi(api_client)
    corpus_id = UUID('123e4567-e89b-12d3-a456-426614174000') # UUID | ID of the corpus.
    status = 'PENDING' # str | Optional lifecycle filter. When omitted, documents of all statuses are returned. (optional)
    tags = ['legal'] # List[str] | Optional tag filter. Returns documents carrying at least one of the given tags. Repeat for multiple values: `tags=legal&tags=2026`. When omitted, tags are ignored. (optional)
    page_size = 25 # int | Number of items per page, 1-100. (optional) (default to 25)
    page_index = 0 # int | Zero-based page index. (optional) (default to 0)

    try:
        # List documents
        api_response = api_instance.list4(corpus_id, status=status, tags=tags, page_size=page_size, page_index=page_index)
        print("The response of DocumentApi->list4:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentApi->list4: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **corpus_id** | **UUID**| ID of the corpus. | 
 **status** | **str**| Optional lifecycle filter. When omitted, documents of all statuses are returned. | [optional] 
 **tags** | [**List[str]**](str.md)| Optional tag filter. Returns documents carrying at least one of the given tags. Repeat for multiple values: &#x60;tags&#x3D;legal&amp;tags&#x3D;2026&#x60;. When omitted, tags are ignored. | [optional] 
 **page_size** | **int**| Number of items per page, 1-100. | [optional] [default to 25]
 **page_index** | **int**| Zero-based page index. | [optional] [default to 0]

### Return type

[**DocumentListResponse**](DocumentListResponse.md)

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
**200** | Page of documents. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_supported_documents**
> str list_supported_documents()

List accepted content types

Return the MIME types accepted by `POST /v1/doc/init`. Use this to validate files client-side before initializing an upload.

### Example

* Bearer (JWT) Authentication (JWT):
* Api Key Authentication (AccessToken):

```python
import verbatim_client
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
    api_instance = verbatim_client.DocumentApi(api_client)

    try:
        # List accepted content types
        api_response = api_instance.list_supported_documents()
        print("The response of DocumentApi->list_supported_documents:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentApi->list_supported_documents: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**str**

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
**200** | List of accepted MIME types. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **preview_urls1**
> DocumentPreviewUrls preview_urls1(id, pages)

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
    api_instance = verbatim_client.DocumentApi(api_client)
    id = UUID('123e4567-e89b-12d3-a456-426614174000') # UUID | ID of the document.
    pages = [[1]] # List[int] | One-based page indices to issue preview URLs for. Required: 1 to 10 values per request, each within the document's page range. Repeat for multiple values: `pages=1&pages=2`.

    try:
        # Get presigned preview URLs
        api_response = api_instance.preview_urls1(id, pages)
        print("The response of DocumentApi->preview_urls1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentApi->preview_urls1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**| ID of the document. | 
 **pages** | [**List[int]**](int.md)| One-based page indices to issue preview URLs for. Required: 1 to 10 values per request, each within the document&#39;s page range. Repeat for multiple values: &#x60;pages&#x3D;1&amp;pages&#x3D;2&#x60;. | 

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

# **reinit_upload**
> DocumentInit reinit_upload(id)

Re-initialize a document for a new upload

Replace the **content** of an existing document while keeping its identity: same
`id`, same `filename`, `userId`, `provider`, `lang`, `metadata`, `tags`, `chunk`
and source dates. Use `PATCH /v1/doc/{id}` to change those attributes — this
endpoint only touches the file behind them.

The document must be in `READY` or `FAILED` status; any other status is rejected
with `409`, since there is either nothing ingested yet or an ingestion in flight.

Everything derived from the previous content is dropped: its embeddings, its
summary, and the counters filled in by ingestion (`size`, `tokens`, `nbWords`).
The document moves back to `AWAITING_UPLOAD` and the response carries a fresh
presigned PUT URL — the same payload as `POST /v1/doc/init`. From there the flow
is unchanged: PUT the new bytes, then call `POST /v1/doc/{id}/commit`.

Two things to be aware of:

- Posts that cited this document **lose their attachments to it**, because the
  citations point at the embeddings being deleted. Answers already returned to
  users are not modified.
- The previously uploaded file **stays in storage** until your PUT overwrites it.
  Committing without uploading first therefore re-ingests the old content.


### Example

* Bearer (JWT) Authentication (JWT):
* Api Key Authentication (AccessToken):

```python
import verbatim_client
from verbatim_client.models.document_init import DocumentInit
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
    api_instance = verbatim_client.DocumentApi(api_client)
    id = UUID('123e4567-e89b-12d3-a456-426614174000') # UUID | ID of the document whose content is being replaced.

    try:
        # Re-initialize a document for a new upload
        api_response = api_instance.reinit_upload(id)
        print("The response of DocumentApi->reinit_upload:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentApi->reinit_upload: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**| ID of the document whose content is being replaced. | 

### Return type

[**DocumentInit**](DocumentInit.md)

### Authorization

[JWT](../README.md#JWT), [AccessToken](../README.md#AccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**415** | The document&#39;s content type is no longer accepted — see &#x60;GET /v1/doc/accept&#x60;. |  -  |
**500** | Internal error. Check body to get more info |  -  |
**403** | Not authorized. Access not granted for this request |  -  |
**404** | The resource referenced by the request does not exist. |  -  |
**400** | The request is malformed or contains invalid parameters. |  -  |
**409** | Document is not in &#x60;READY&#x60; or &#x60;FAILED&#x60; status — nothing to replace, or an ingestion is in flight. |  -  |
**200** | Document reset to AWAITING_UPLOAD status. PUT the new file to &#x60;uploadUrl&#x60;. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search1**
> DocumentSearchResponse search1(corpus_id, q=q, tags=tags, tags_match=tags_match, status=status, content_type=content_type, lang=lang, provider=provider, created_after=created_after, created_before=created_before, min_size=min_size, max_size=max_size, sort=sort, order=order, page_size=page_size, page_index=page_index)

Search documents

Find documents in a corpus by filename, tags, lifecycle status, content type,
language, provider or ingestion date, sorted the way you need them.

Every filter is optional and they **narrow together**: a request carrying none of
them returns the whole corpus, one carrying several returns only the documents
matching all of them. For a plain corpus listing, `GET /v1/doc/` is the simpler
endpoint — this one is for finding a document you cannot scroll to.

### Filename — `q`

Case-insensitive, and **anchored at the start** of the filename: `q=annual`
finds `Annual-Report-2025.pdf`, `q=report` does not. Put a `*` anywhere to
match elsewhere — `q=*report` searches any position, `q=*report*` a substring,
`q=2025-*.pdf` a name that starts with `2025-` and ends in `.pdf`.

The default is anchored because that is the shape the index can serve: an
anchored pattern is a range scan, a leading `*` is a filter over the corpus.
Both are correct, the first is cheaper — prefer it when your client knows how
the filename begins.

`%` and `_` carry no special meaning here: they match themselves.

### Tags — `tags`, `tagsMatch`

Repeat the parameter for several tags (`tags=legal&tags=2026`). By default
(`tagsMatch=ANY`) a document matches when it carries **at least one** of them,
which is what `GET /v1/doc/?tags=…` does; `tagsMatch=ALL` requires **every** one
of them, extra tags on the document being fine.

### Status — `status`

Repeatable as well, and any of the listed states matches:
`status=PENDING&status=FAILED` returns everything that is not ingested yet or
needs attention.

### Content type — `contentType`

Repeatable too, and any of the listed types matches:
`contentType=application/pdf&contentType=text/plain`. Values are taken as they
come — nothing is checked against `GET /v1/doc/accept`, so a type the platform
does not ingest is not an error, it simply matches no document.

### Size — `minSize`, `maxSize`

A range on the stored size in bytes, **inclusive at both ends** and each bound
independent: `minSize=1048576` alone is "at least 1 MB", `maxSize` alone "at
most", and `minSize=maxSize=N` the documents of exactly that many bytes.
`minSize` above `maxSize` is refused with `400` rather than answering an empty
page.

A document only has a size once its upload is committed, so setting either
bound also excludes everything still `AWAITING_UPLOAD` — the same documents
`sort=SIZE` pushes to the end of the result.

### Dates — `createdAfter`, `createdBefore`

A half-open window on the ingestion date: `createdAfter` is inclusive,
`createdBefore` exclusive, so consecutive windows tile the timeline without
returning a document twice. Supplying `createdAfter` at or after `createdBefore`
is refused with `400` rather than answering an empty page.

### Ordering and paging

`sort` defaults to `CREATED_AT` and `order` to `DESC` — newest first. The
ordering is closed by the document id, so walking `pageIndex` never shows the
same document twice nor skips one, even when many documents share a sort key.
Documents whose `size` is not known yet sort last whatever the direction.

`total` counts every match across all pages, not just the ones returned here.

### Examples

* `?corpusId=…&q=annual-report` — every document whose name starts with it
* `?corpusId=…&q=*report*` — anywhere in the name, at the cost of a scan
* `?corpusId=…&q=2025-*.pdf` — starts with `2025-`, ends in `.pdf`
* `?corpusId=…&status=FAILED&status=PENDING&sort=UPDATED_AT&order=ASC` — the
  ingestion backlog, longest-waiting first
* `?corpusId=…&tags=legal&tags=2026&tagsMatch=ALL` — documents carrying both tags
* `?corpusId=…&contentType=application/pdf&createdAfter=2026-07-01T00:00:00Z&createdBefore=2026-10-01T00:00:00Z&sort=SIZE&order=DESC`
  — last quarter's PDFs, biggest first
* `?corpusId=…&contentType=application/pdf&contentType=text/plain&minSize=1048576`
  — PDFs and plain text over 1 MB
* `?corpusId=…&maxSize=0` — documents that were uploaded empty


### Example

* Bearer (JWT) Authentication (JWT):
* Api Key Authentication (AccessToken):

```python
import verbatim_client
from verbatim_client.models.document_search_response import DocumentSearchResponse
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
    api_instance = verbatim_client.DocumentApi(api_client)
    corpus_id = UUID('123e4567-e89b-12d3-a456-426614174000') # UUID | ID of the corpus to search.
    q = 'annual-report' # str | Filename pattern, case-insensitive and anchored at the start of the name: `annual` matches `Annual-Report-2025.pdf`, `report` does not. Add `*` anywhere to match elsewhere (`*report*`), at the cost of a scan over the corpus. `%` and `_` match themselves. Blank or omitted, filenames are not filtered. (optional)
    tags = ['legal'] # List[str] | Tag filter. Repeat for multiple values: `tags=legal&tags=2026`. When omitted, tags are ignored. (optional)
    tags_match = 'ANY' # str | How `tags` combine: `ANY` keeps documents carrying at least one of them, `ALL` only those carrying every one. Ignored without `tags`. (optional)
    status = ['READY'] # List[str] | Lifecycle filter. Repeat for several: `status=PENDING&status=FAILED` matches either. When omitted, documents of all statuses are returned. (optional)
    content_type = ['application/pdf'] # List[str] | MIME type filter. Repeat for several: `contentType=application/pdf&contentType=text/plain` matches either. Values are not checked against `GET /v1/doc/accept` — an unsupported one simply matches nothing. When omitted, content types are not filtered. (optional)
    lang = 'fr' # str | Exact ISO-639 language code of the document. (optional)
    provider = 'user' # str | Exact provider identifier, as supplied at upload time. (optional)
    created_after = '2026-07-01T00:00:00Z' # datetime | Keep documents ingested at or after this instant (ISO-8601, inclusive). (optional)
    created_before = '2026-10-01T00:00:00Z' # datetime | Keep documents ingested strictly before this instant (ISO-8601, exclusive). (optional)
    min_size = 1048576 # int | Keep documents of at least this many bytes (inclusive). Documents still awaiting upload have no size and drop out. (optional)
    max_size = 10485760 # int | Keep documents of at most this many bytes (inclusive). (optional)
    sort = 'CREATED_AT' # str | Column to sort on. Defaults to `CREATED_AT`. (optional)
    order = 'DESC' # str | Sort direction. Defaults to `DESC` — newest, largest or alphabetically last first. (optional)
    page_size = 25 # int | Number of items per page, 1-100. (optional) (default to 25)
    page_index = 0 # int | Zero-based page index. (optional) (default to 0)

    try:
        # Search documents
        api_response = api_instance.search1(corpus_id, q=q, tags=tags, tags_match=tags_match, status=status, content_type=content_type, lang=lang, provider=provider, created_after=created_after, created_before=created_before, min_size=min_size, max_size=max_size, sort=sort, order=order, page_size=page_size, page_index=page_index)
        print("The response of DocumentApi->search1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentApi->search1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **corpus_id** | **UUID**| ID of the corpus to search. | 
 **q** | **str**| Filename pattern, case-insensitive and anchored at the start of the name: &#x60;annual&#x60; matches &#x60;Annual-Report-2025.pdf&#x60;, &#x60;report&#x60; does not. Add &#x60;*&#x60; anywhere to match elsewhere (&#x60;*report*&#x60;), at the cost of a scan over the corpus. &#x60;%&#x60; and &#x60;_&#x60; match themselves. Blank or omitted, filenames are not filtered. | [optional] 
 **tags** | [**List[str]**](str.md)| Tag filter. Repeat for multiple values: &#x60;tags&#x3D;legal&amp;tags&#x3D;2026&#x60;. When omitted, tags are ignored. | [optional] 
 **tags_match** | **str**| How &#x60;tags&#x60; combine: &#x60;ANY&#x60; keeps documents carrying at least one of them, &#x60;ALL&#x60; only those carrying every one. Ignored without &#x60;tags&#x60;. | [optional] 
 **status** | [**List[str]**](str.md)| Lifecycle filter. Repeat for several: &#x60;status&#x3D;PENDING&amp;status&#x3D;FAILED&#x60; matches either. When omitted, documents of all statuses are returned. | [optional] 
 **content_type** | [**List[str]**](str.md)| MIME type filter. Repeat for several: &#x60;contentType&#x3D;application/pdf&amp;contentType&#x3D;text/plain&#x60; matches either. Values are not checked against &#x60;GET /v1/doc/accept&#x60; — an unsupported one simply matches nothing. When omitted, content types are not filtered. | [optional] 
 **lang** | **str**| Exact ISO-639 language code of the document. | [optional] 
 **provider** | **str**| Exact provider identifier, as supplied at upload time. | [optional] 
 **created_after** | **datetime**| Keep documents ingested at or after this instant (ISO-8601, inclusive). | [optional] 
 **created_before** | **datetime**| Keep documents ingested strictly before this instant (ISO-8601, exclusive). | [optional] 
 **min_size** | **int**| Keep documents of at least this many bytes (inclusive). Documents still awaiting upload have no size and drop out. | [optional] 
 **max_size** | **int**| Keep documents of at most this many bytes (inclusive). | [optional] 
 **sort** | **str**| Column to sort on. Defaults to &#x60;CREATED_AT&#x60;. | [optional] 
 **order** | **str**| Sort direction. Defaults to &#x60;DESC&#x60; — newest, largest or alphabetically last first. | [optional] 
 **page_size** | **int**| Number of items per page, 1-100. | [optional] [default to 25]
 **page_index** | **int**| Zero-based page index. | [optional] [default to 0]

### Return type

[**DocumentSearchResponse**](DocumentSearchResponse.md)

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
**400** | A filter or paging parameter is out of bounds, or the date window is empty. |  -  |
**409** | The request conflicts with the current state of the resource. |  -  |
**200** | Page of matching documents. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **status**
> DocumentStatus status(id)

Get a document's status

Lightweight polling endpoint. Returns the current lifecycle status, an optional message (typically a failure reason when `status == FAILED`), and the last update timestamp. Cheaper than `GET /v1/doc/{id}` for polling between commit and the final `READY` or `FAILED` status.

### Example

* Bearer (JWT) Authentication (JWT):
* Api Key Authentication (AccessToken):

```python
import verbatim_client
from verbatim_client.models.document_status import DocumentStatus
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
    api_instance = verbatim_client.DocumentApi(api_client)
    id = UUID('123e4567-e89b-12d3-a456-426614174000') # UUID | ID of the document.

    try:
        # Get a document's status
        api_response = api_instance.status(id)
        print("The response of DocumentApi->status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentApi->status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**| ID of the document. | 

### Return type

[**DocumentStatus**](DocumentStatus.md)

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
**200** | Status returned. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **summary**
> str summary(id)

Get a document summary

Return the Markdown summary generated during ingestion. Returns an empty body if the document has not been ingested yet or has no summary.

### Example

* Bearer (JWT) Authentication (JWT):
* Api Key Authentication (AccessToken):

```python
import verbatim_client
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
    api_instance = verbatim_client.DocumentApi(api_client)
    id = UUID('123e4567-e89b-12d3-a456-426614174000') # UUID | ID of the document.

    try:
        # Get a document summary
        api_response = api_instance.summary(id)
        print("The response of DocumentApi->summary:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentApi->summary: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**| ID of the document. | 

### Return type

**str**

### Authorization

[JWT](../README.md#JWT), [AccessToken](../README.md#AccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/markdown

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**415** | Content type not accepted by the platform. See &#x60;GET /v1/doc/accept&#x60; for the list of supported types. |  -  |
**500** | Internal error. Check body to get more info |  -  |
**403** | Not authorized. Access not granted for this request |  -  |
**404** | The resource referenced by the request does not exist. |  -  |
**400** | The request is malformed or contains invalid parameters. |  -  |
**409** | The request conflicts with the current state of the resource. |  -  |
**200** | Summary returned (may be empty). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update1**
> Document update1(id, document_update_request)

Update a document

Patch the editable attributes of a document — `filename`, `docCreate`, `docUpdate`,
`metadata`, `tags` and `chunk`. Only the fields present in the request body are
updated; omitted fields keep their current value.

`metadata`, `tags` and `chunk` **replace** the stored value when provided — merge
client-side if you want to preserve existing entries. Send `"tags": []` to clear
every tag, and `"chunk": {}` to drop the chunking override and fall back to the
platform default.

`docCreate` and `docUpdate` describe the **source** document, not the platform row:
they are yours to correct, while `createdAt` and `updatedAt` remain server-managed
and cannot be set here.

Every attribute is descriptive: renaming a document does not move the stored file
nor re-trigger ingestion, so embeddings and previews are left untouched. Changing
`chunk` likewise applies to the **next** ingestion — it does not re-chunk an already
ingested document. Available in any lifecycle status.


### Example

* Bearer (JWT) Authentication (JWT):
* Api Key Authentication (AccessToken):

```python
import verbatim_client
from verbatim_client.models.document import Document
from verbatim_client.models.document_update_request import DocumentUpdateRequest
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
    api_instance = verbatim_client.DocumentApi(api_client)
    id = UUID('123e4567-e89b-12d3-a456-426614174000') # UUID | ID of the document to update.
    document_update_request = {"filename":"annual-report-2025-final.pdf"} # DocumentUpdateRequest | 

    try:
        # Update a document
        api_response = api_instance.update1(id, document_update_request)
        print("The response of DocumentApi->update1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentApi->update1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**| ID of the document to update. | 
 **document_update_request** | [**DocumentUpdateRequest**](DocumentUpdateRequest.md)|  | 

### Return type

[**Document**](Document.md)

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
**400** | &#x60;filename&#x60; is blank or longer than 256 characters. |  -  |
**409** | The request conflicts with the current state of the resource. |  -  |
**200** | Document updated. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

