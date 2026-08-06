# verbatim_client.DocumentApi

All URIs are relative to *https://api.verbatim-ai.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**commit_upload**](DocumentApi.md#commit_upload) | **POST** /v1/doc/{id}/commit | Commit a previously initialized upload
[**delete1**](DocumentApi.md#delete1) | **DELETE** /v1/doc/{id} | Delete a document
[**download_url1**](DocumentApi.md#download_url1) | **GET** /v1/doc/{id}/download-url | Get a presigned download URL
[**get1**](DocumentApi.md#get1) | **GET** /v1/doc/{id} | Get a document
[**init_upload**](DocumentApi.md#init_upload) | **POST** /v1/doc/init | Initialize a direct-to-storage upload
[**list3**](DocumentApi.md#list3) | **GET** /v1/doc/ | List documents
[**list_supported_documents**](DocumentApi.md#list_supported_documents) | **GET** /v1/doc/accept | List accepted content types
[**preview_urls1**](DocumentApi.md#preview_urls1) | **GET** /v1/doc/{id}/preview-urls | Get presigned preview URLs
[**reinit_upload**](DocumentApi.md#reinit_upload) | **PUT** /v1/doc/{id}/init | Re-initialize a document for a new upload
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
**500** | Internal error. Check body to get more info |  -  |
**403** | Not authorized. Access not granted for this request |  -  |
**404** | The resource referenced by the request does not exist. |  -  |
**415** | Content type not accepted by the platform. See &#x60;GET /v1/doc/accept&#x60; for the list of supported types. |  -  |
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
**500** | Internal error. Check body to get more info |  -  |
**403** | Not authorized. Access not granted for this request |  -  |
**404** | The resource referenced by the request does not exist. |  -  |
**415** | Content type not accepted by the platform. See &#x60;GET /v1/doc/accept&#x60; for the list of supported types. |  -  |
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
**500** | Internal error. Check body to get more info |  -  |
**403** | Not authorized. Access not granted for this request |  -  |
**404** | The resource referenced by the request does not exist. |  -  |
**415** | Content type not accepted by the platform. See &#x60;GET /v1/doc/accept&#x60; for the list of supported types. |  -  |
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
**500** | Internal error. Check body to get more info |  -  |
**403** | Not authorized. Access not granted for this request |  -  |
**404** | The resource referenced by the request does not exist. |  -  |
**415** | Content type not accepted by the platform. See &#x60;GET /v1/doc/accept&#x60; for the list of supported types. |  -  |
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
**500** | Internal error. Check body to get more info |  -  |
**403** | Not authorized. Access not granted for this request |  -  |
**404** | The resource referenced by the request does not exist. |  -  |
**415** | Content type not accepted by the platform. See &#x60;GET /v1/doc/accept&#x60; for the list of supported types. |  -  |
**400** | The request is malformed or contains invalid parameters. |  -  |
**409** | The request conflicts with the current state of the resource. |  -  |
**200** | Document created in AWAITING_UPLOAD status. PUT the file to &#x60;uploadUrl&#x60;. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list3**
> DocumentListResponse list3(corpus_id, status=status, page_size=page_size, page_index=page_index)

List documents

Paginate documents stored in a corpus, newest first. Pass the optional `status` filter to narrow down by lifecycle state — e.g. `status=PENDING` returns the ingestion backlog, `status=FAILED` returns documents that need attention.

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
    page_size = 25 # int | Number of items per page. (optional) (default to 25)
    page_index = 0 # int | Zero-based page index. (optional) (default to 0)

    try:
        # List documents
        api_response = api_instance.list3(corpus_id, status=status, page_size=page_size, page_index=page_index)
        print("The response of DocumentApi->list3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentApi->list3: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **corpus_id** | **UUID**| ID of the corpus. | 
 **status** | **str**| Optional lifecycle filter. When omitted, documents of all statuses are returned. | [optional] 
 **page_size** | **int**| Number of items per page. | [optional] [default to 25]
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
**500** | Internal error. Check body to get more info |  -  |
**403** | Not authorized. Access not granted for this request |  -  |
**404** | The resource referenced by the request does not exist. |  -  |
**415** | Content type not accepted by the platform. See &#x60;GET /v1/doc/accept&#x60; for the list of supported types. |  -  |
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
**500** | Internal error. Check body to get more info |  -  |
**403** | Not authorized. Access not granted for this request |  -  |
**404** | The resource referenced by the request does not exist. |  -  |
**415** | Content type not accepted by the platform. See &#x60;GET /v1/doc/accept&#x60; for the list of supported types. |  -  |
**400** | The request is malformed or contains invalid parameters. |  -  |
**409** | The request conflicts with the current state of the resource. |  -  |
**200** | List of accepted MIME types. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **preview_urls1**
> DocumentPreviewUrls preview_urls1(id, pages=pages)

Get presigned preview URLs

Return time-limited presigned URLs for the rendered preview images of the document.
One entry is issued per (page, size): by default the first 4 pages × {SMALL, MEDIUM},
so up to 8 entries per call.

Pass `pages` to restrict the response to specific page indices (e.g. `pages=0&pages=2`).
When omitted, pages 0–3 are used. Duplicate values are preserved as supplied.

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
    pages = [56] # List[int] | Page indices to include. When omitted, pages 0–3 are returned. Repeat for multiple values: `pages=0&pages=2`. (optional)

    try:
        # Get presigned preview URLs
        api_response = api_instance.preview_urls1(id, pages=pages)
        print("The response of DocumentApi->preview_urls1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentApi->preview_urls1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**| ID of the document. | 
 **pages** | [**List[int]**](int.md)| Page indices to include. When omitted, pages 0–3 are returned. Repeat for multiple values: &#x60;pages&#x3D;0&amp;pages&#x3D;2&#x60;. | [optional] 

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
**500** | Internal error. Check body to get more info |  -  |
**403** | Not authorized. Access not granted for this request |  -  |
**404** | The resource referenced by the request does not exist. |  -  |
**415** | Content type not accepted by the platform. See &#x60;GET /v1/doc/accept&#x60; for the list of supported types. |  -  |
**400** | The request is malformed or contains invalid parameters. |  -  |
**409** | The request conflicts with the current state of the resource. |  -  |
**200** | Presigned preview URLs issued. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reinit_upload**
> DocumentInit reinit_upload(id)

Re-initialize a document for a new upload

Replace the **content** of an existing document while keeping its identity: same
`id`, same `filename`, `userId`, `provider`, `lang`, `metadata` and source dates.
Use `PATCH /v1/doc/{id}` to change those attributes — this endpoint only touches
the file behind them.

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
**500** | Internal error. Check body to get more info |  -  |
**403** | Not authorized. Access not granted for this request |  -  |
**404** | The resource referenced by the request does not exist. |  -  |
**415** | The document&#39;s content type is no longer accepted — see &#x60;GET /v1/doc/accept&#x60;. |  -  |
**400** | The request is malformed or contains invalid parameters. |  -  |
**409** | Document is not in &#x60;READY&#x60; or &#x60;FAILED&#x60; status — nothing to replace, or an ingestion is in flight. |  -  |
**200** | Document reset to AWAITING_UPLOAD status. PUT the new file to &#x60;uploadUrl&#x60;. |  -  |

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
**500** | Internal error. Check body to get more info |  -  |
**403** | Not authorized. Access not granted for this request |  -  |
**404** | The resource referenced by the request does not exist. |  -  |
**415** | Content type not accepted by the platform. See &#x60;GET /v1/doc/accept&#x60; for the list of supported types. |  -  |
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
**500** | Internal error. Check body to get more info |  -  |
**403** | Not authorized. Access not granted for this request |  -  |
**404** | The resource referenced by the request does not exist. |  -  |
**415** | Content type not accepted by the platform. See &#x60;GET /v1/doc/accept&#x60; for the list of supported types. |  -  |
**400** | The request is malformed or contains invalid parameters. |  -  |
**409** | The request conflicts with the current state of the resource. |  -  |
**200** | Summary returned (may be empty). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update1**
> Document update1(id, document_update_request)

Update a document

Patch the editable attributes of a document — `filename`, `docCreate`, `docUpdate`
and `metadata`. Only the fields present in the request body are updated; omitted
fields keep their current value.

`metadata` **replaces** the stored map when provided — merge client-side if you want
to preserve existing keys.

`docCreate` and `docUpdate` describe the **source** document, not the platform row:
they are yours to correct, while `createdAt` and `updatedAt` remain server-managed
and cannot be set here.

Every attribute is descriptive: renaming a document does not move the stored file
nor re-trigger ingestion, so embeddings and previews are left untouched. Available
in any lifecycle status.


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
**500** | Internal error. Check body to get more info |  -  |
**403** | Not authorized. Access not granted for this request |  -  |
**404** | The resource referenced by the request does not exist. |  -  |
**415** | Content type not accepted by the platform. See &#x60;GET /v1/doc/accept&#x60; for the list of supported types. |  -  |
**400** | &#x60;filename&#x60; is blank or longer than 256 characters. |  -  |
**409** | The request conflicts with the current state of the resource. |  -  |
**200** | Document updated. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

