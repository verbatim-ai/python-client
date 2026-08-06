# verbatim_client.WidgetApi

All URIs are relative to *http://localhost:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**attachment**](WidgetApi.md#attachment) | **GET** /v1/webhook/widget/attachment/{postId} | Get source attachments of a post
[**get_session**](WidgetApi.md#get_session) | **GET** /webhook/v1/widget/{lang} | 
[**init**](WidgetApi.md#init) | **GET** /v1/webhook/widget/init | Init a session
[**post_message**](WidgetApi.md#post_message) | **POST** /webhook/v1/widget/{lang} | 
[**posts**](WidgetApi.md#posts) | **GET** /v1/webhook/widget/ | List posts in a session
[**query**](WidgetApi.md#query) | **GET** /v1/webhook/widget/q | Post a query in a session


# **attachment**
> WidgetAttachmentResponse attachment(post_id)

Get source attachments of a post

Returns every source document that the AI cited when generating a SYSTEM post. For each document the response includes its summary, metadata, and **presigned preview URLs** for every page that was actually retrieved (1-based index). Two sizes are provided per page — `previewSmallUrl` (SMALL) and `previewSmallLarge` (MEDIUM) — so the widget can render a thumbnail and a full-size lightbox view without additional round-trips. All presigned URLs share the same `previewExpirationDate`; refresh by calling this endpoint again after expiry. The post must belong to the organisation identified by the Access Token.

### Example

* Api Key Authentication (AccessToken):

```python
import verbatim_client
from verbatim_client.models.widget_attachment_response import WidgetAttachmentResponse
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

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Enter a context with an instance of the API client
with verbatim_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = verbatim_client.WidgetApi(api_client)
    post_id = UUID('c2e5f3a1-4d6b-5c7e-9f8a-0b1c2d3e4f5a') # UUID | Id of the post whose source attachments are fetched

    try:
        # Get source attachments of a post
        api_response = api_instance.attachment(post_id)
        print("The response of WidgetApi->attachment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WidgetApi->attachment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_id** | **UUID**| Id of the post whose source attachments are fetched | 

### Return type

[**WidgetAttachmentResponse**](WidgetAttachmentResponse.md)

### Authorization

[AccessToken](../README.md#AccessToken)

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
**200** | Attachments resolved with presigned preview URLs |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_session**
> WidgetSessionResponseLegacy get_session(lang, cid, sid)

### Example


```python
import verbatim_client
from verbatim_client.models.widget_session_response_legacy import WidgetSessionResponseLegacy
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
    api_instance = verbatim_client.WidgetApi(api_client)
    lang = 'lang_example' # str | 
    cid = 'cid_example' # str | 
    sid = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        api_response = api_instance.get_session(lang, cid, sid)
        print("The response of WidgetApi->get_session:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WidgetApi->get_session: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lang** | **str**|  | 
 **cid** | **str**|  | 
 **sid** | **UUID**|  | 

### Return type

[**WidgetSessionResponseLegacy**](WidgetSessionResponseLegacy.md)

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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **init**
> WidgetSessionResponse init(widget_session_request)

Init a session

Init a new session with a context : name and a search context, defined by a list of Corpus UID

### Example

* Api Key Authentication (AccessToken):

```python
import verbatim_client
from verbatim_client.models.widget_session_request import WidgetSessionRequest
from verbatim_client.models.widget_session_response import WidgetSessionResponse
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

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Enter a context with an instance of the API client
with verbatim_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = verbatim_client.WidgetApi(api_client)
    widget_session_request = {"widgetName":"BCorp widget","corpus":["12345-ABCDE"]} # WidgetSessionRequest | 

    try:
        # Init a session
        api_response = api_instance.init(widget_session_request)
        print("The response of WidgetApi->init:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WidgetApi->init: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **widget_session_request** | [**WidgetSessionRequest**](WidgetSessionRequest.md)|  | 

### Return type

[**WidgetSessionResponse**](WidgetSessionResponse.md)

### Authorization

[AccessToken](../README.md#AccessToken)

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
**200** | session is ready |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_message**
> WidgetMessageResponse post_message(lang, cid, sid, widget_session_request_body)

### Example


```python
import verbatim_client
from verbatim_client.models.widget_message_response import WidgetMessageResponse
from verbatim_client.models.widget_session_request_body import WidgetSessionRequestBody
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
    api_instance = verbatim_client.WidgetApi(api_client)
    lang = 'lang_example' # str | 
    cid = 'cid_example' # str | 
    sid = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    widget_session_request_body = verbatim_client.WidgetSessionRequestBody() # WidgetSessionRequestBody | 

    try:
        api_response = api_instance.post_message(lang, cid, sid, widget_session_request_body)
        print("The response of WidgetApi->post_message:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WidgetApi->post_message: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lang** | **str**|  | 
 **cid** | **str**|  | 
 **sid** | **UUID**|  | 
 **widget_session_request_body** | [**WidgetSessionRequestBody**](WidgetSessionRequestBody.md)|  | 

### Return type

[**WidgetMessageResponse**](WidgetMessageResponse.md)

### Authorization

No authorization required

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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **posts**
> WidgetPostsResponse posts(session_id)

List posts in a session

Returns the full chronological history of a session — both user queries (`owner: USER`) and AI answers (`owner: SYSTEM`). Each item includes the message text, language, timestamp, and the number of source document chunks cited (`attachment` count). The session must belong to the organisation identified by the Access Token.

### Example

* Api Key Authentication (AccessToken):

```python
import verbatim_client
from verbatim_client.models.widget_posts_response import WidgetPostsResponse
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

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Enter a context with an instance of the API client
with verbatim_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = verbatim_client.WidgetApi(api_client)
    session_id = UUID('8f3e9c7a-2b14-4d6e-9c1a-7a5b8e3f1d2c') # UUID | Id of the session where the posts are fetched

    try:
        # List posts in a session
        api_response = api_instance.posts(session_id)
        print("The response of WidgetApi->posts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WidgetApi->posts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **UUID**| Id of the session where the posts are fetched | 

### Return type

[**WidgetPostsResponse**](WidgetPostsResponse.md)

### Authorization

[AccessToken](../README.md#AccessToken)

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
**200** | Post history retrieved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query**
> WidgetQueryResponse query(session_id, query, lang=lang)

Post a query in a session

User query is posted in the session. AI backend system answer to this query

### Example

* Api Key Authentication (AccessToken):

```python
import verbatim_client
from verbatim_client.models.widget_query_response import WidgetQueryResponse
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

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Enter a context with an instance of the API client
with verbatim_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = verbatim_client.WidgetApi(api_client)
    session_id = UUID('abcd-1234-efjk-5678') # UUID | Id of the session where the query is fired
    query = 'What is the address of our customer BCorp. ' # str | The user's query
    lang = 'fr' # str | ISO language code use by the model  (optional) (default to 'fr')

    try:
        # Post a query in a session
        api_response = api_instance.query(session_id, query, lang=lang)
        print("The response of WidgetApi->query:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WidgetApi->query: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **UUID**| Id of the session where the query is fired | 
 **query** | **str**| The user&#39;s query | 
 **lang** | **str**| ISO language code use by the model  | [optional] [default to &#39;fr&#39;]

### Return type

[**WidgetQueryResponse**](WidgetQueryResponse.md)

### Authorization

[AccessToken](../README.md#AccessToken)

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
**200** | Answer is ready |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

