# verbatim_client.AuthApi

All URIs are relative to *https://api.verbatim-ai.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create2**](AuthApi.md#create2) | **POST** /v1/auth/access-token | Create an access token
[**revoke**](AuthApi.md#revoke) | **DELETE** /v1/auth/access-token/{token} | Revoke an access token
[**whoami**](AuthApi.md#whoami) | **GET** /v1/auth/whoami | Who am I


# **create2**
> AccessTokenCreateResponse create2(access_token_create_request)

Create an access token

Generate a new short-lived opaque access token for the caller's organization. The token can be used as the `X-Access-Token` header on `/v1/` API calls. Default TTL is 3600 seconds (1 hour).By default, token inherit privileges over all the domains. To limit access, defined a list of scope, where each must be compliant with the regex (config|auth|session|doc|corpus|post|usage|agent):(create|read|update|delete)

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
        api_response = api_instance.create2(access_token_create_request)
        print("The response of AuthApi->create2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->create2: %s\n" % e)
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
**415** | Content type not accepted by the platform. See &#x60;GET /v1/doc/accept&#x60; for the list of supported types. |  -  |
**500** | Internal error. Check body to get more info |  -  |
**403** | Not authorized. Access not granted for this request |  -  |
**404** | The resource referenced by the request does not exist. |  -  |
**400** | The request is malformed or contains invalid parameters. |  -  |
**409** | The request conflicts with the current state of the resource. |  -  |
**200** | Access token created. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revoke**
> AckResponse revoke(token)

Revoke an access token

Permanently delete an access token. Any in-flight request using this token will fail immediately after revocation.

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
        # Revoke an access token
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
**415** | Content type not accepted by the platform. See &#x60;GET /v1/doc/accept&#x60; for the list of supported types. |  -  |
**500** | Internal error. Check body to get more info |  -  |
**403** | Not authorized. Access not granted for this request |  -  |
**404** | The resource referenced by the request does not exist. |  -  |
**400** | The request is malformed or contains invalid parameters. |  -  |
**409** | The request conflicts with the current state of the resource. |  -  |
**200** | Token revoked. |  -  |

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
**415** | Content type not accepted by the platform. See &#x60;GET /v1/doc/accept&#x60; for the list of supported types. |  -  |
**500** | Internal error. Check body to get more info |  -  |
**403** | Not authorized. Access not granted for this request |  -  |
**404** | The resource referenced by the request does not exist. |  -  |
**400** | The request is malformed or contains invalid parameters. |  -  |
**409** | The request conflicts with the current state of the resource. |  -  |
**200** | Identity of the authenticated user. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

