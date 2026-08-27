# verbatim_client.PublicApi

All URIs are relative to *http://localhost:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**assert_email**](PublicApi.md#assert_email) | **GET** /pub/v1/user/assert/email/{email} | Assert an email free from registration
[**check**](PublicApi.md#check) | **GET** /pub/check | Deep health check
[**check_verification_code**](PublicApi.md#check_verification_code) | **GET** /pub/v1/user/assert/code/{email}/{code} | Assert email verification code
[**ping**](PublicApi.md#ping) | **GET** /pub/ping | Basic ping


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
    api_instance = verbatim_client.PublicApi(api_client)
    email = 'email_example' # str | Email to assert
    turnstile_token = 'gfhFs45fdg6-6575fdgg...' # str | turnstileToken owned by web client. Token delivered throw CloudFare Turnstile service
    language_code = 'en' # str | Email verification code language code  (optional) (default to 'en')

    try:
        # Assert an email free from registration
        api_response = api_instance.assert_email(email, turnstile_token, language_code=language_code)
        print("The response of PublicApi->assert_email:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApi->assert_email: %s\n" % e)
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

# **check**
> CheckResponse check()

Deep health check

Probe every subsystem the platform depends on and report each outcome:

- **S3** — read an object back from the archive storage
- **DB** — run a query on a pooled connection
- **LLM** — send a prompt to the inference endpoint and require an answer

Every probe runs on every call, so one failure never hides another. The response
is `200` when all of them pass and `500` as soon as one fails, which is the
signal a monitoring tool alerts on; the body names the failing subsystem and
carries its reason.

### Example


```python
import verbatim_client
from verbatim_client.models.check_response import CheckResponse
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
    api_instance = verbatim_client.PublicApi(api_client)

    try:
        # Deep health check
        api_response = api_instance.check()
        print("The response of PublicApi->check:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApi->check: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**CheckResponse**](CheckResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**500** | At least one subsystem failed its probe. |  -  |
**403** | Not authorized. Access not granted for this request |  -  |
**404** | The resource referenced by the request does not exist. |  -  |
**400** | The request is malformed or contains invalid parameters. |  -  |
**409** | The request conflicts with the current state of the resource. |  -  |
**415** | Content type not accepted by the platform. See &#x60;GET /v1/doc/accept&#x60; for the list of supported types. |  -  |
**200** | Every subsystem answered. |  -  |

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
    api_instance = verbatim_client.PublicApi(api_client)
    email = 'email_example' # str | Email to assert
    code = 'code_example' # str | Email verification code
    turnstile_token = 'gfhFs45fdg6-6575fdgg' # str | turnstileToken owned by web client. Token delivered throw CloudFare Turnstile service

    try:
        # Assert email verification code
        api_response = api_instance.check_verification_code(email, code, turnstile_token)
        print("The response of PublicApi->check_verification_code:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApi->check_verification_code: %s\n" % e)
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

# **ping**
> ping()

Basic ping

Simple open API to ping platform. Easy to use for an healthy check

### Example


```python
import verbatim_client
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
    api_instance = verbatim_client.PublicApi(api_client)

    try:
        # Basic ping
        api_instance.ping()
    except Exception as e:
        print("Exception when calling PublicApi->ping: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

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
**200** | Pong. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

