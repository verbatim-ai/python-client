# verbatim_client.ChunkApi

All URIs are relative to *https://api.verbatim-ai.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete3**](ChunkApi.md#delete3) | **DELETE** /v1/chunk/{chunkId} | Delete a chunk
[**get3**](ChunkApi.md#get3) | **GET** /v1/chunk/{chunkId} | Get a chunk
[**list6**](ChunkApi.md#list6) | **GET** /v1/chunk/ | List chunks
[**search2**](ChunkApi.md#search2) | **GET** /v1/chunk/q | Search chunks
[**update3**](ChunkApi.md#update3) | **PATCH** /v1/chunk/{chunkId} | Update a chunk


# **delete3**
> AckResponse delete3(chunk_id)

Delete a chunk

Take a chunk out of the index.

**This is a soft delete, like deleting a document or a session.** The chunk
stops existing as far as this API and every answer built from now on is
concerned: it disappears from `GET /v1/chunk/`, `GET /v1/chunk/q` and
`GET /v1/chunk/{chunkId}`, and it can no longer be retrieved as context for a
query. Nothing is destroyed underneath — neither the row nor the archived text —
which is what makes it a decision about what may be retrieved rather than an
erasure of what was. There is no endpoint that undoes it.

Past answers that cited this chunk keep their text and **lose the citation**
pointing here.

The document itself is untouched: its file, its summary and its other chunks
stay exactly as they were. That is what makes this usable for taking one passage
out of the index without destroying the document it came from.

Deleting the document (`DELETE /v1/doc/{docId}`) does the same thing to every
chunk at once, and re-ingesting it (`PUT /v1/doc/{docId}/content`) rebuilds
every chunk from the file, this one included.


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
    api_instance = verbatim_client.ChunkApi(api_client)
    chunk_id = UUID('123e4567-e89b-12d3-a456-426614174000') # UUID | ID of the chunk to delete.

    try:
        # Delete a chunk
        api_response = api_instance.delete3(chunk_id)
        print("The response of ChunkApi->delete3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChunkApi->delete3: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chunk_id** | **UUID**| ID of the chunk to delete. | 

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
**200** | Chunk deleted. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get3**
> Chunk get3(chunk_id)

Get a chunk

Fetch one chunk with its text.

Unlike the listings, `body` is always read here — a single storage round-trip,
which is what this endpoint is for. An **empty** `body` on a row that exists is
not an error and is worth acting on: it means the stored object is missing, so
the chunk still matches vector searches and then contributes nothing to the
answer.

`hash` is the MD5 of the text as it was pushed to storage. Comparing it against
the body you just read is the cheapest integrity check there is, and searching
it with `GET /v1/chunk/q?hash=…` finds every copy of the same passage in your
organization.


### Example

* Bearer (JWT) Authentication (JWT):
* Api Key Authentication (AccessToken):

```python
import verbatim_client
from verbatim_client.models.chunk import Chunk
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
    api_instance = verbatim_client.ChunkApi(api_client)
    chunk_id = UUID('123e4567-e89b-12d3-a456-426614174000') # UUID | ID of the chunk.

    try:
        # Get a chunk
        api_response = api_instance.get3(chunk_id)
        print("The response of ChunkApi->get3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChunkApi->get3: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chunk_id** | **UUID**| ID of the chunk. | 

### Return type

[**Chunk**](Chunk.md)

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
**404** | No chunk with this id, or its document has been deleted. |  -  |
**400** | The request is malformed or contains invalid parameters. |  -  |
**409** | The request conflicts with the current state of the resource. |  -  |
**200** | Chunk found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list6**
> ChunkListResponse list6(body=body, page_size=page_size, page_index=page_index)

List chunks

Paginate every chunk of the caller's organization.

The organization is resolved from the JWT, so there is nothing to pass and no
way to ask for another tenant's chunks. A chunk belongs to an organization
through its document's corpus, and it is visible exactly as long as that
document is: deleting a document takes its chunks out of this API too.

Chunks come back in reading order — by document, then by the first page each
one covers, then by id — so a document's chunks arrive as a contiguous block in
the order they appear in the file, with its summary chunk (the one covering no
page) heading the block. The id closes the ordering, so walking `pageIndex`
never shows the same chunk twice nor skips one when a page split into several.

`body` is **not** included: it lives in object storage and would cost one read
per row. Pass `body=true` if you want it — the page size is then capped at 25 —
or use `GET /v1/chunk/{chunkId}`, which always carries it.

To narrow the result — by corpus, document, hash, page or metadata — use
`GET /v1/chunk/q`, which takes the same paging parameters.


### Example

* Bearer (JWT) Authentication (JWT):
* Api Key Authentication (AccessToken):

```python
import verbatim_client
from verbatim_client.models.chunk_list_response import ChunkListResponse
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
    api_instance = verbatim_client.ChunkApi(api_client)
    body = False # bool | Include each chunk's text, read from object storage. One storage read per row — off by default. (optional) (default to False)
    page_size = 25 # int | Number of items per page, 1-100 — or 1-25 when `body=true`. (optional) (default to 25)
    page_index = 0 # int | Zero-based page index. (optional) (default to 0)

    try:
        # List chunks
        api_response = api_instance.list6(body=body, page_size=page_size, page_index=page_index)
        print("The response of ChunkApi->list6:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChunkApi->list6: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **bool**| Include each chunk&#39;s text, read from object storage. One storage read per row — off by default. | [optional] [default to False]
 **page_size** | **int**| Number of items per page, 1-100 — or 1-25 when &#x60;body&#x3D;true&#x60;. | [optional] [default to 25]
 **page_index** | **int**| Zero-based page index. | [optional] [default to 0]

### Return type

[**ChunkListResponse**](ChunkListResponse.md)

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
**200** | Page of chunks. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search2**
> ChunkListResponse search2(corpus_id=corpus_id, document_id=document_id, hash=hash, page=page, key=key, value=value, var_json=var_json, body=body, page_size=page_size, page_index=page_index)

Search chunks

Find chunks of the caller's organization by corpus, document, hash, page and
metadata.

Every filter is optional and they **narrow together**: a request carrying none
of them returns the whole organization — the same answer as `GET /v1/chunk/` —
and one carrying several returns only the chunks matching all of them.

The organization is never a parameter. It comes from the JWT and is always
applied, so no combination of filters reaches another tenant's chunks.

### Corpus and document — `corpusId`, `documentId`

Both must belong to the caller's organization, and both are checked *before*
the search runs — naming one you cannot see answers `403` on the request rather
than an empty page.

### Hash — `hash`

Exact match on the MD5 of the chunk text. Equal hashes mean equal text, so this
is how the same passage is found across documents: read a chunk, then search
its hash with no `documentId` to see every copy of it in your organization.
Sent empty (`&hash=`) it is treated as absent.

### Page — `page`

Keeps chunks whose span **covers** that page. A chunk is built from consecutive
elements and can cross page boundaries, so one covering pages 3 to 5 answers to
`page=3`, `page=4` and `page=5` alike. Pages are 1-based; `page=0` is a `400`,
not an empty page. Chunks belonging to no page in particular — the document
summary — carry an empty span and match no `page` filter at all.

### Metadata — `key`/`value`, or `json`

Matches chunks whose metadata **contains** the fragment (PostgreSQL's `@>`
operator), extra keys on the chunk being fine. Pass `key` and `value` for a
single pair — they go together, one without the other is a `400` — or `json`
for a raw object when the filter is nested or has several keys. `json` wins
when both are supplied. `kind` is the key the platform sets: `chunk` for a
piece of the document, `summary` for the generated summary.

### Bodies — `body`

Off by default, because including them costs one storage read per row. With
`body=true` the page size is capped at 25.

### Examples

* `?documentId=…` — everything one document was split into, in reading order
* `?documentId=…&body=true&pageSize=10` — the same, with the text, ten at a time
* `?documentId=…&page=4` — every chunk covering page 4, including one that
  starts on page 3
* `?hash=9e107d9d372bb6826bd81d3542a419d6` — every copy of one passage in the
  organization, across documents
* `?corpusId=…&key=kind&value=summary` — the summary chunk of every document in
  a corpus
* `?json={"section":"Article 4"}` — a metadata fragment


### Example

* Bearer (JWT) Authentication (JWT):
* Api Key Authentication (AccessToken):

```python
import verbatim_client
from verbatim_client.models.chunk_list_response import ChunkListResponse
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
    api_instance = verbatim_client.ChunkApi(api_client)
    corpus_id = UUID('123e4567-e89b-12d3-a456-426614174000') # UUID | Keep chunks whose document belongs to this corpus. Must belong to the caller's organization. (optional)
    document_id = UUID('123e4567-e89b-12d3-a456-426614174000') # UUID | Keep chunks of this document. Must belong to the caller's organization. (optional)
    hash = '9e107d9d372bb6826bd81d3542a419d6' # str | Exact MD5 of the chunk text. Blank or omitted, the hash is not filtered. (optional)
    page = 4 # int | Keep chunks whose page span covers this page. 1-based. (optional)
    key = 'kind' # str | Metadata key to filter on. Goes together with `value`. (optional)
    value = 'summary' # str | Metadata value matching `key`. (optional)
    var_json = '{\"section\":\"Article 4\"}' # str | Raw JSON object used as the containment filter. Wins over `key`/`value` when set. (optional)
    body = False # bool | Include each chunk's text, read from object storage. One storage read per row — off by default. (optional) (default to False)
    page_size = 25 # int | Number of items per page, 1-100 — or 1-25 when `body=true`. (optional) (default to 25)
    page_index = 0 # int | Zero-based page index. (optional) (default to 0)

    try:
        # Search chunks
        api_response = api_instance.search2(corpus_id=corpus_id, document_id=document_id, hash=hash, page=page, key=key, value=value, var_json=var_json, body=body, page_size=page_size, page_index=page_index)
        print("The response of ChunkApi->search2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChunkApi->search2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **corpus_id** | **UUID**| Keep chunks whose document belongs to this corpus. Must belong to the caller&#39;s organization. | [optional] 
 **document_id** | **UUID**| Keep chunks of this document. Must belong to the caller&#39;s organization. | [optional] 
 **hash** | **str**| Exact MD5 of the chunk text. Blank or omitted, the hash is not filtered. | [optional] 
 **page** | **int**| Keep chunks whose page span covers this page. 1-based. | [optional] 
 **key** | **str**| Metadata key to filter on. Goes together with &#x60;value&#x60;. | [optional] 
 **value** | **str**| Metadata value matching &#x60;key&#x60;. | [optional] 
 **var_json** | **str**| Raw JSON object used as the containment filter. Wins over &#x60;key&#x60;/&#x60;value&#x60; when set. | [optional] 
 **body** | **bool**| Include each chunk&#39;s text, read from object storage. One storage read per row — off by default. | [optional] [default to False]
 **page_size** | **int**| Number of items per page, 1-100 — or 1-25 when &#x60;body&#x3D;true&#x60;. | [optional] [default to 25]
 **page_index** | **int**| Zero-based page index. | [optional] [default to 0]

### Return type

[**ChunkListResponse**](ChunkListResponse.md)

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
**400** | A filter is malformed, or a paging parameter is out of bounds. |  -  |
**409** | The request conflicts with the current state of the resource. |  -  |
**200** | Page of matching chunks. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update3**
> Chunk update3(chunk_id, chunk_update_request)

Update a chunk

Patch a chunk's page span, metadata or text. Only the fields present in the
body are applied; omitted fields keep their current value. Returns the full
updated chunk, text included.

This is a **repair** endpoint. It exists so a chunk that ingestion got wrong
can be corrected without re-processing the document, and it is worth knowing
exactly what it does and does not do before reaching for it.

### Rewriting `body` does not re-embed the chunk

The vector is the search index and it is not recomputed here. After patching
the text, the chunk is still **retrieved for the text it used to hold** and is
then handed to the model as the text it holds now. For a mangled character or a
name to redact, that is exactly right — the passage means the same thing and is
found the same way. For a rewrite, it is wrong: re-ingest the document instead
(`PUT /v1/doc/{docId}/content`), which re-splits and re-embeds it.

`hash` is deliberately **not** recomputed either. It records the MD5 of what
was embedded, so leaving it alone is what makes the divergence visible
afterwards: a chunk whose `hash` no longer matches its `body` is one that has
been patched.

### `metadata` replaces, it does not merge

Send the whole object you want stored. `{}` clears it.

### `pages` is a span

1-based page numbers, sorted and de-duplicated server-side. `[]` clears the
span, which is what a chunk belonging to no page in particular carries. A value
below 1 is a `400`.


### Example

* Bearer (JWT) Authentication (JWT):
* Api Key Authentication (AccessToken):

```python
import verbatim_client
from verbatim_client.models.chunk import Chunk
from verbatim_client.models.chunk_update_request import ChunkUpdateRequest
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
    api_instance = verbatim_client.ChunkApi(api_client)
    chunk_id = UUID('123e4567-e89b-12d3-a456-426614174000') # UUID | ID of the chunk to update.
    chunk_update_request = {"pages":[2,3,4]} # ChunkUpdateRequest | 

    try:
        # Update a chunk
        api_response = api_instance.update3(chunk_id, chunk_update_request)
        print("The response of ChunkApi->update3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChunkApi->update3: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chunk_id** | **UUID**| ID of the chunk to update. | 
 **chunk_update_request** | [**ChunkUpdateRequest**](ChunkUpdateRequest.md)|  | 

### Return type

[**Chunk**](Chunk.md)

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
**400** | A page number is below 1. |  -  |
**409** | The request conflicts with the current state of the resource. |  -  |
**200** | Chunk updated. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

