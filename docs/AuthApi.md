# verbatim_client.AuthApi

All URIs are relative to *https://api.verbatim-ai.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create3**](AuthApi.md#create3) | **POST** /v1/auth/access-token/ | Create an access token
[**list3**](AuthApi.md#list3) | **GET** /v1/auth/access-token/ | List access tokens
[**revoke**](AuthApi.md#revoke) | **DELETE** /v1/auth/access-token/{token} | Revoke an access token by value
[**revoke_by_id**](AuthApi.md#revoke_by_id) | **DELETE** /v1/auth/access-token/id/{id} | Revoke an access token by id
[**scopes**](AuthApi.md#scopes) | **GET** /v1/auth/access-token/scopes | List the available scopes
[**whoami**](AuthApi.md#whoami) | **GET** /v1/auth/whoami | Who am I


# **create3**
> AccessTokenCreateResponse create3(access_token_create_request)

Create an access token

Mint a short-lived opaque access token for the caller's organization. Send it as the
`X-Access-Token` header on `/v1/` API calls.

**The `token` value is only ever returned here.** Store it or hand it over now: the
listing shows only its first characters, and no call returns it again.

- `scope` is mandatory and non-empty — a list of `DOMAIN:ACTION` entries such as
  `corpus:read`. `GET /v1/auth/access-token/scopes` lists every valid entry.
- `ttl` is in seconds: 3600 (1 hour) when omitted, at least 10, and no more than the
  ceiling the platform sets (`app.access-token.max-ttl-seconds`, 86400 — 24 hours — by
  default). A longer `ttl` is refused with a 400, not shortened.
- `issuer` is a free label stored with the token and shown in the listing.
- the token's `userId` and `email` are not inputs: they are the caller's own, and
  what `GET /v1/auth/whoami` answers for the token. A token minted by a root user
  is a root token.

Only reachable with a JWT: an access token cannot mint another.


### Example

* Bearer (JWT) Authentication (JWT):

```python
import verbatim_client
from verbatim_client.models.access_token_create_request import AccessTokenCreateRequest
from verbatim_client.models.access_token_create_response import AccessTokenCreateResponse
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

# Enter a context with an instance of the API client
with verbatim_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = verbatim_client.AuthApi(api_client)
    access_token_create_request = {"scope":["doc:create"]} # AccessTokenCreateRequest | 

    try:
        # Create an access token
        api_response = api_instance.create3(access_token_create_request)
        print("The response of AuthApi->create3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->create3: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token_create_request** | [**AccessTokenCreateRequest**](AccessTokenCreateRequest.md)|  | 

### Return type

[**AccessTokenCreateResponse**](AccessTokenCreateResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**500** | Internal error. Check body to get more info |  -  |
**403** | No JWT, or the call was made with an access token. |  -  |
**404** | The resource referenced by the request does not exist. |  -  |
**415** | Content type not accepted by the platform. See &#x60;GET /v1/doc/accept&#x60; for the list of supported types. |  -  |
**400** | Missing or invalid &#x60;scope&#x60;, or &#x60;ttl&#x60; below 10 seconds or above the platform ceiling. |  -  |
**409** | The request conflicts with the current state of the resource. |  -  |
**413** | The request body exceeds the size accepted by the endpoint. |  -  |
**200** | Access token created. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list3**
> AccessTokenListResponse list3(page_size=page_size, page_index=page_index)

List access tokens

List the access tokens of the caller's organization, newest first, with every attribute
stored for them — **except the token value**, which is cut down to its first characters
followed by `...`. The full value is only returned by the create call.

Expired tokens stay listed (compare `expiresAt` with the current time) until they are
revoked. Use an item's `id` with `DELETE /v1/auth/access-token/id/{id}` to revoke it.

Tokens minted by a platform administrator, impersonation tokens included, are not
listed.

Only reachable with a JWT.


### Example

* Bearer (JWT) Authentication (JWT):

```python
import verbatim_client
from verbatim_client.models.access_token_list_response import AccessTokenListResponse
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

# Enter a context with an instance of the API client
with verbatim_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = verbatim_client.AuthApi(api_client)
    page_size = 25 # int | Number of items per page. (optional) (default to 25)
    page_index = 0 # int | Zero-based page index. (optional) (default to 0)

    try:
        # List access tokens
        api_response = api_instance.list3(page_size=page_size, page_index=page_index)
        print("The response of AuthApi->list3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->list3: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_size** | **int**| Number of items per page. | [optional] [default to 25]
 **page_index** | **int**| Zero-based page index. | [optional] [default to 0]

### Return type

[**AccessTokenListResponse**](AccessTokenListResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**500** | Internal error. Check body to get more info |  -  |
**403** | No JWT, or the call was made with an access token. |  -  |
**404** | The resource referenced by the request does not exist. |  -  |
**415** | Content type not accepted by the platform. See &#x60;GET /v1/doc/accept&#x60; for the list of supported types. |  -  |
**400** | &#x60;pageSize&#x60; below 1 or &#x60;pageIndex&#x60; below 0. |  -  |
**409** | The request conflicts with the current state of the resource. |  -  |
**413** | The request body exceeds the size accepted by the endpoint. |  -  |
**200** | One page of access tokens. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revoke**
> AckResponse revoke(token)

Revoke an access token by value

Permanently delete an access token, given its full value. Any request using this token fails immediately after revocation. An unknown value is acknowledged all the same. When you only have the listing, revoke by id instead. Only reachable with a JWT.

### Example

* Bearer (JWT) Authentication (JWT):

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

# Enter a context with an instance of the API client
with verbatim_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = verbatim_client.AuthApi(api_client)
    token = 'abcdf1234abcdf567' # str | access token to revoke.

    try:
        # Revoke an access token by value
        api_response = api_instance.revoke(token)
        print("The response of AuthApi->revoke:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->revoke: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| access token to revoke. | 

### Return type

[**AckResponse**](AckResponse.md)

### Authorization

[JWT](../README.md#JWT)

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
**413** | The request body exceeds the size accepted by the endpoint. |  -  |
**200** | Token revoked. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revoke_by_id**
> AckResponse revoke_by_id(id)

Revoke an access token by id

Permanently delete one of the organization's access tokens, identified by the `id` the
listing returns. Revocation is immediate: the next request carrying the token is refused.

An id that names no token of the caller's organization — unknown, already revoked, or
another organization's — is a 404.

Only reachable with a JWT.


### Example

* Bearer (JWT) Authentication (JWT):

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

# Enter a context with an instance of the API client
with verbatim_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = verbatim_client.AuthApi(api_client)
    id = UUID('123e4567-e89b-12d3-a456-426614174000') # UUID | Id of the access token to revoke, as listed.

    try:
        # Revoke an access token by id
        api_response = api_instance.revoke_by_id(id)
        print("The response of AuthApi->revoke_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->revoke_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**| Id of the access token to revoke, as listed. | 

### Return type

[**AckResponse**](AckResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**500** | Internal error. Check body to get more info |  -  |
**403** | No JWT, or the call was made with an access token. |  -  |
**404** | No access token with this id in the caller&#39;s organization. |  -  |
**415** | Content type not accepted by the platform. See &#x60;GET /v1/doc/accept&#x60; for the list of supported types. |  -  |
**400** | The request is malformed or contains invalid parameters. |  -  |
**409** | The request conflicts with the current state of the resource. |  -  |
**413** | The request body exceeds the size accepted by the endpoint. |  -  |
**200** | Token revoked. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **scopes**
> AccessTokenScopesResponse scopes()

List the available scopes

Every scope an access token can be created with — the values accepted in the `scope`
of `POST /v1/auth/access-token/`. Use it to build a scope picker rather than hard-coding
the list.

A scope entry is `DOMAIN:ACTION`, and every domain combines with every action:

- `domains` — each domain with the API path it covers, what it gives access to, and its
  scope entries, ready to group in a UI;
- `actions` — each action with the HTTP methods it opens (`read` is `GET`, so running a
  RAG query, `GET /v1/post/q`, needs `post:read`);
- `scopes` — the flat list of every valid entry.

The catalog is the same for every organization and every caller.


### Example

* Bearer (JWT) Authentication (JWT):

```python
import verbatim_client
from verbatim_client.models.access_token_scopes_response import AccessTokenScopesResponse
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

# Enter a context with an instance of the API client
with verbatim_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = verbatim_client.AuthApi(api_client)

    try:
        # List the available scopes
        api_response = api_instance.scopes()
        print("The response of AuthApi->scopes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->scopes: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**AccessTokenScopesResponse**](AccessTokenScopesResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**500** | Internal error. Check body to get more info |  -  |
**403** | No credential, or an access token whose scope lacks &#x60;auth:read&#x60;. |  -  |
**404** | The resource referenced by the request does not exist. |  -  |
**415** | Content type not accepted by the platform. See &#x60;GET /v1/doc/accept&#x60; for the list of supported types. |  -  |
**400** | The request is malformed or contains invalid parameters. |  -  |
**409** | The request conflicts with the current state of the resource. |  -  |
**413** | The request body exceeds the size accepted by the endpoint. |  -  |
**200** | The scope catalog. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **whoami**
> WhoAmI whoami()

Who am I

Return the identity of the caller as resolved from the Bearer token:
organization, user id, email and display name.

Typical use cases:

- Bootstrap a UI session after sign-in.
- Verify that a token is still valid and which user it belongs to.


### Example

* Bearer (JWT) Authentication (JWT):

```python
import verbatim_client
from verbatim_client.models.who_am_i import WhoAmI
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

# Enter a context with an instance of the API client
with verbatim_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = verbatim_client.AuthApi(api_client)

    try:
        # Who am I
        api_response = api_instance.whoami()
        print("The response of AuthApi->whoami:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->whoami: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**WhoAmI**](WhoAmI.md)

### Authorization

[JWT](../README.md#JWT)

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
**413** | The request body exceeds the size accepted by the endpoint. |  -  |
**200** | Identity of the authenticated user. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

