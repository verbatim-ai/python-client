# verbatim_client.PrivateApi

All URIs are relative to *http://localhost:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activate**](PrivateApi.md#activate) | **PUT** /_/v1/key/{keyId}/activate | Activate a key
[**create4**](PrivateApi.md#create4) | **POST** /_/v1/key/ | Register a new key slot
[**deactivate**](PrivateApi.md#deactivate) | **PUT** /_/v1/key/{keyId}/deactivate | Deactivate a key
[**delete1**](PrivateApi.md#delete1) | **DELETE** /_/v1/key/{keyId} | Delete a key
[**get1**](PrivateApi.md#get1) | **GET** /_/v1/key/{keyId} | Get a key
[**get_migration_info**](PrivateApi.md#get_migration_info) | **GET** /_/v1/flyway/info | 
[**list3**](PrivateApi.md#list3) | **GET** /_/v1/key/ | List keys
[**onboard**](PrivateApi.md#onboard) | **PUT** /_/v1/user/onboard | Onboard the authenticated user
[**publish**](PrivateApi.md#publish) | **POST** /_/v1/key/{keyId}/publish | Publish PEM content for a key
[**update1**](PrivateApi.md#update1) | **PUT** /_/v1/key/{keyId} | Update a key


# **activate**
> Key activate(key_id)

Activate a key

Flip an `INACTIVE` key back to `ACTIVE`. Only keys that have been published (content set) will actually verify JWTs.

### Example

* Bearer (JWT) Authentication (JWT):
* Api Key Authentication (AccessToken):

```python
import verbatim_client
from verbatim_client.models.key import Key
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
    api_instance = verbatim_client.PrivateApi(api_client)
    key_id = UUID('123e4567-e89b-12d3-a456-426614174000') # UUID | ID of the key to activate.

    try:
        # Activate a key
        api_response = api_instance.activate(key_id)
        print("The response of PrivateApi->activate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PrivateApi->activate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key_id** | **UUID**| ID of the key to activate. | 

### Return type

[**Key**](Key.md)

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
**200** | Key activated. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create4**
> KeyCreateResponse create4(key_create_request)

Register a new key slot

Create an empty key entry with a name and an optional description. The key starts in `INACTIVE` state with no content — call `POST /_/v1/key/{id}/publish` to upload the PEM and activate it.

### Example

* Bearer (JWT) Authentication (JWT):
* Api Key Authentication (AccessToken):

```python
import verbatim_client
from verbatim_client.models.key_create_request import KeyCreateRequest
from verbatim_client.models.key_create_response import KeyCreateResponse
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
    api_instance = verbatim_client.PrivateApi(api_client)
    key_create_request = {"name":"support-backend-prod","description":"Production signing key for the support backend."} # KeyCreateRequest | 

    try:
        # Register a new key slot
        api_response = api_instance.create4(key_create_request)
        print("The response of PrivateApi->create4:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PrivateApi->create4: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key_create_request** | [**KeyCreateRequest**](KeyCreateRequest.md)|  | 

### Return type

[**KeyCreateResponse**](KeyCreateResponse.md)

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
**200** | Key created. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deactivate**
> Key deactivate(key_id)

Deactivate a key

Flip an `ACTIVE` key to `INACTIVE`. Tokens signed with this key will no longer be accepted until it is reactivated.

### Example

* Bearer (JWT) Authentication (JWT):
* Api Key Authentication (AccessToken):

```python
import verbatim_client
from verbatim_client.models.key import Key
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
    api_instance = verbatim_client.PrivateApi(api_client)
    key_id = UUID('123e4567-e89b-12d3-a456-426614174000') # UUID | ID of the key to deactivate.

    try:
        # Deactivate a key
        api_response = api_instance.deactivate(key_id)
        print("The response of PrivateApi->deactivate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PrivateApi->deactivate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key_id** | **UUID**| ID of the key to deactivate. | 

### Return type

[**Key**](Key.md)

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
**200** | Key deactivated. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete1**
> AckResponse delete1(key_id)

Delete a key

Soft-delete a key. JWT tokens signed with the deleted key will no longer be accepted.

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
    api_instance = verbatim_client.PrivateApi(api_client)
    key_id = UUID('123e4567-e89b-12d3-a456-426614174000') # UUID | ID of the key to delete.

    try:
        # Delete a key
        api_response = api_instance.delete1(key_id)
        print("The response of PrivateApi->delete1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PrivateApi->delete1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key_id** | **UUID**| ID of the key to delete. | 

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
**200** | Key deleted. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get1**
> KeyItemResponse get1(key_id)

Get a key

Fetch a single key by its identifier. The raw RSA content is never returned.

### Example

* Bearer (JWT) Authentication (JWT):
* Api Key Authentication (AccessToken):

```python
import verbatim_client
from verbatim_client.models.key_item_response import KeyItemResponse
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
    api_instance = verbatim_client.PrivateApi(api_client)
    key_id = UUID('123e4567-e89b-12d3-a456-426614174000') # UUID | ID of the key.

    try:
        # Get a key
        api_response = api_instance.get1(key_id)
        print("The response of PrivateApi->get1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PrivateApi->get1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key_id** | **UUID**| ID of the key. | 

### Return type

[**KeyItemResponse**](KeyItemResponse.md)

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
**200** | Key found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_migration_info**
> List[Dict[str, Optional[object]]] get_migration_info()

### Example

* Bearer (JWT) Authentication (JWT):
* Api Key Authentication (AccessToken):

```python
import verbatim_client
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
    api_instance = verbatim_client.PrivateApi(api_client)

    try:
        api_response = api_instance.get_migration_info()
        print("The response of PrivateApi->get_migration_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PrivateApi->get_migration_info: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**List[Dict[str, Optional[object]]]**

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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list3**
> KeyListResponse list3(page_size=page_size, page_index=page_index)

List keys

Paginate keys belonging to the caller's organization. The raw RSA content is never returned.

### Example

* Bearer (JWT) Authentication (JWT):
* Api Key Authentication (AccessToken):

```python
import verbatim_client
from verbatim_client.models.key_list_response import KeyListResponse
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
    api_instance = verbatim_client.PrivateApi(api_client)
    page_size = 25 # int | Number of items per page. (optional) (default to 25)
    page_index = 0 # int | Zero-based page index. (optional) (default to 0)

    try:
        # List keys
        api_response = api_instance.list3(page_size=page_size, page_index=page_index)
        print("The response of PrivateApi->list3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PrivateApi->list3: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_size** | **int**| Number of items per page. | [optional] [default to 25]
 **page_index** | **int**| Zero-based page index. | [optional] [default to 0]

### Return type

[**KeyListResponse**](KeyListResponse.md)

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
**200** | Page of keys. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **onboard**
> UserOnboardResponse onboard()

Onboard the authenticated user

Bootstrap the caller into a Verbatim organization.
Must be called with a Firebase JWT that does **not** yet carry an `oid` claim
tokens already bound to an organization are rejected at the security layer (403).
On success the user is provisioned, an organization is created (or joined), and
the caller should refresh their Firebase token to pick up the new `oid` claim before
calling any `/v1/*` endpoint.


### Example

* Bearer (JWT) Authentication (JWT):

```python
import verbatim_client
from verbatim_client.models.user_onboard_response import UserOnboardResponse
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

# Enter a context with an instance of the API client
with verbatim_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = verbatim_client.PrivateApi(api_client)

    try:
        # Onboard the authenticated user
        api_response = api_instance.onboard()
        print("The response of PrivateApi->onboard:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PrivateApi->onboard: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**UserOnboardResponse**](UserOnboardResponse.md)

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
**400** | The request is malformed or contains invalid parameters. |  -  |
**409** | The request conflicts with the current state of the resource. |  -  |
**415** | Content type not accepted by the platform. See &#x60;GET /v1/doc/accept&#x60; for the list of supported types. |  -  |
**200** | User onboarded; organization and identity returned. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **publish**
> Key publish(key_id, body)

Publish PEM content for a key

Upload the PEM-encoded RSA 2048-bit public key for a previously created slot. The content is validated and stored, and the key transitions to `ACTIVE`. Content is write-once — to rotate, create a new key and delete the old one.

### Example

* Bearer (JWT) Authentication (JWT):
* Api Key Authentication (AccessToken):

```python
import verbatim_client
from verbatim_client.models.key import Key
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
    api_instance = verbatim_client.PrivateApi(api_client)
    key_id = UUID('123e4567-e89b-12d3-a456-426614174000') # UUID | ID of the key to publish.
    body = ----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFA...\n-----END PUBLIC KEY-----
 # str | 

    try:
        # Publish PEM content for a key
        api_response = api_instance.publish(key_id, body)
        print("The response of PrivateApi->publish:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PrivateApi->publish: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key_id** | **UUID**| ID of the key to publish. | 
 **body** | **str**|  | 

### Return type

[**Key**](Key.md)

### Authorization

[JWT](../README.md#JWT), [AccessToken](../README.md#AccessToken)

### HTTP request headers

 - **Content-Type**: text/plain
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
**200** | Key published and activated. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update1**
> KeyUpdateResponse update1(key_id, key_update_request)

Update a key

Patch the name and/or description of an existing key. Raw RSA content, format, and state are not editable through this endpoint.

### Example

* Bearer (JWT) Authentication (JWT):
* Api Key Authentication (AccessToken):

```python
import verbatim_client
from verbatim_client.models.key_update_request import KeyUpdateRequest
from verbatim_client.models.key_update_response import KeyUpdateResponse
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
    api_instance = verbatim_client.PrivateApi(api_client)
    key_id = UUID('123e4567-e89b-12d3-a456-426614174000') # UUID | ID of the key to update.
    key_update_request = {"name":"support-backend-prod","description":"Production signing key, rotated 2026-05."} # KeyUpdateRequest | 

    try:
        # Update a key
        api_response = api_instance.update1(key_id, key_update_request)
        print("The response of PrivateApi->update1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PrivateApi->update1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key_id** | **UUID**| ID of the key to update. | 
 **key_update_request** | [**KeyUpdateRequest**](KeyUpdateRequest.md)|  | 

### Return type

[**KeyUpdateResponse**](KeyUpdateResponse.md)

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
**200** | Key updated. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

