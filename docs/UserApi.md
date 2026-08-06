# verbatim_client.UserApi

All URIs are relative to *http://localhost:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**assert_email**](UserApi.md#assert_email) | **GET** /pub/v1/user/assert/email/{email} | Assert an email free from registration
[**check_verification_code**](UserApi.md#check_verification_code) | **GET** /pub/v1/user/assert/code/{email}/{code} | Assert email verification code
[**onboard**](UserApi.md#onboard) | **PUT** /_/v1/user/onboard | Onboard the authenticated user


# **assert_email**
> AckResponse assert_email(email, turnstile_token, language_code=language_code)

Assert an email free from registration

Check if the email is unknown and can be go throw signin process

### Example


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


# Enter a context with an instance of the API client
with verbatim_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = verbatim_client.UserApi(api_client)
    email = 'email_example' # str | Email to assert
    turnstile_token = 'gfhFs45fdg6-6575fdgg...' # str | turnstileToken owned by web client. Token delivered throw CloudFare Turnstile service
    language_code = 'en' # str | Email verification code language code  (optional) (default to 'en')

    try:
        # Assert an email free from registration
        api_response = api_instance.assert_email(email, turnstile_token, language_code=language_code)
        print("The response of UserApi->assert_email:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->assert_email: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| Email to assert | 
 **turnstile_token** | **str**| turnstileToken owned by web client. Token delivered throw CloudFare Turnstile service | 
 **language_code** | **str**| Email verification code language code  | [optional] [default to &#39;en&#39;]

### Return type

[**AckResponse**](AckResponse.md)

### Authorization

No authorization required

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
**200** | Email is free from registration. Email with a verification code is fired. User can go throw signin process |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **check_verification_code**
> AckResponse check_verification_code(email, code, turnstile_token)

Assert email verification code

Assert the code sent to the email

### Example


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


# Enter a context with an instance of the API client
with verbatim_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = verbatim_client.UserApi(api_client)
    email = 'email_example' # str | Email to assert
    code = 'code_example' # str | Email verification code
    turnstile_token = 'gfhFs45fdg6-6575fdgg' # str | turnstileToken owned by web client. Token delivered throw CloudFare Turnstile service

    try:
        # Assert email verification code
        api_response = api_instance.check_verification_code(email, code, turnstile_token)
        print("The response of UserApi->check_verification_code:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->check_verification_code: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| Email to assert | 
 **code** | **str**| Email verification code | 
 **turnstile_token** | **str**| turnstileToken owned by web client. Token delivered throw CloudFare Turnstile service | 

### Return type

[**AckResponse**](AckResponse.md)

### Authorization

No authorization required

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
**200** | Code is valid |  -  |

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
    api_instance = verbatim_client.UserApi(api_client)

    try:
        # Onboard the authenticated user
        api_response = api_instance.onboard()
        print("The response of UserApi->onboard:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->onboard: %s\n" % e)
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

