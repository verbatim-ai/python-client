# verbatim_client.AgentApi

All URIs are relative to *http://localhost:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create3**](AgentApi.md#create3) | **POST** /v1/agent/ | Create an agent
[**delete4**](AgentApi.md#delete4) | **DELETE** /v1/agent/{agentId} | Delete an agent
[**get4**](AgentApi.md#get4) | **GET** /v1/agent/{agentId} | Get an agent
[**list2**](AgentApi.md#list2) | **GET** /v1/agent/ | List agents
[**update4**](AgentApi.md#update4) | **PATCH** /v1/agent/{agentId} | Update an agent


# **create3**
> Agent create3(agent_create_request)

Create an agent

Create a custom agent owned by your organization.

Only `name` is required — the smallest useful body is `{"name": "..."}`, which
produces an agent identical in behaviour to the platform default and free to
diverge from it later. Every field you leave out either takes its column default
(`topK` 5, `rerank` true, `useHistory` true, `thinkingMode` HIGH) or stays unset
and tracks the platform value.

`name` must be free: not one of your own agents' names, and not one carried by a
platform agent (`lock: true`) either — both answer `409`. Core agents appear in
your listing, so `Verbatim Default` there and `Verbatim Default` of your own
would be two entries you could only tell apart by `lock`. Names are compared
exactly, so `Support` and `support` are two names and `Verbatim Default v2` is
free. Deleting an agent puts its name back into circulation.

`rerankModel` and `baseModel` are checked against `GET /v1/config/model` here
rather than at query time, so a typo is a `400` on this request instead of a
failure on every query the agent later runs.

The result is always `lock: false` and `default: false`. Core agents are seeded
by the platform and cannot be created over the API.


### Example

* Bearer (JWT) Authentication (JWT):
* Api Key Authentication (AccessToken):

```python
import verbatim_client
from verbatim_client.models.agent import Agent
from verbatim_client.models.agent_create_request import AgentCreateRequest
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
    api_instance = verbatim_client.AgentApi(api_client)
    agent_create_request = {"name":"Support assistant"} # AgentCreateRequest | 

    try:
        # Create an agent
        api_response = api_instance.create3(agent_create_request)
        print("The response of AgentApi->create3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentApi->create3: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_create_request** | [**AgentCreateRequest**](AgentCreateRequest.md)|  | 

### Return type

[**Agent**](Agent.md)

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
**400** | Missing or over-long &#x60;name&#x60;, a non-positive &#x60;topK&#x60; / &#x60;rerankTopK&#x60; / &#x60;historySize&#x60;, a &#x60;temperature&#x60; outside 0–1, or a model name &#x60;GET /v1/config/model&#x60; does not advertise. |  -  |
**409** | This &#x60;name&#x60; is taken — by one of your agents, or by a platform agent. |  -  |
**415** | Content type not accepted by the platform. See &#x60;GET /v1/doc/accept&#x60; for the list of supported types. |  -  |
**200** | Agent created. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete4**
> AckResponse delete4(agent_id)

Delete an agent

Delete a custom agent. From here on it is gone: absent from `GET /v1/agent/`,
`404` on get, update and delete, and `404` on any query naming it — a deleted
agent is indistinguishable from one that never existed.

What it does **not** do is rewrite the past. Answers already produced under this
agent keep naming it in their `agentId`, so a conversation stays readable exactly
as it happened. Deleting an agent changes what you can use from now on, not what
already ran.

Sessions are unaffected: an agent is resolved per query, so a conversation that
used this one simply carries on under the platform default.

Its `name` goes back into circulation, so a replacement can be created under the
same name straight away.

Core agents (`lock: true`) cannot be deleted — that answers `400`.


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
    api_instance = verbatim_client.AgentApi(api_client)
    agent_id = UUID('123e4567-e89b-12d3-a456-426614174000') # UUID | ID of the agent to delete.

    try:
        # Delete an agent
        api_response = api_instance.delete4(agent_id)
        print("The response of AgentApi->delete4:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentApi->delete4: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_id** | **UUID**| ID of the agent to delete. | 

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
**404** | No agent with this id is visible to your organization. |  -  |
**400** | The agent is a core agent (&#x60;lock: true&#x60;). |  -  |
**409** | The request conflicts with the current state of the resource. |  -  |
**415** | Content type not accepted by the platform. See &#x60;GET /v1/doc/accept&#x60; for the list of supported types. |  -  |
**200** | Agent deleted. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get4**
> Agent get4(agent_id)

Get an agent

Fetch one agent by its identifier — yours or a core one.

An id belonging to another organization answers `404`, the same as an id that
does not exist: the two are deliberately indistinguishable.


### Example

* Bearer (JWT) Authentication (JWT):
* Api Key Authentication (AccessToken):

```python
import verbatim_client
from verbatim_client.models.agent import Agent
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
    api_instance = verbatim_client.AgentApi(api_client)
    agent_id = UUID('123e4567-e89b-12d3-a456-426614174000') # UUID | ID of the agent.

    try:
        # Get an agent
        api_response = api_instance.get4(agent_id)
        print("The response of AgentApi->get4:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentApi->get4: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_id** | **UUID**| ID of the agent. | 

### Return type

[**Agent**](Agent.md)

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
**404** | No agent with this id is visible to your organization. |  -  |
**400** | The request is malformed or contains invalid parameters. |  -  |
**409** | The request conflicts with the current state of the resource. |  -  |
**415** | Content type not accepted by the platform. See &#x60;GET /v1/doc/accept&#x60; for the list of supported types. |  -  |
**200** | Agent found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list2**
> AgentListResponse list2(page_size=page_size, page_index=page_index)

List agents

Paginate every agent your organization can query with: the platform's core agents
merged with your own custom ones, **core first**, then by name.

There is no separate endpoint for the core catalogue — the merge is the point.
Tell the two apart by `lock`: `true` is a platform agent you can read and use but
not modify. A brand-new organization sees six of them, one per use case, and the
single agent carrying `default: true` is the one a query that names no agent runs
on.


### Example

* Bearer (JWT) Authentication (JWT):
* Api Key Authentication (AccessToken):

```python
import verbatim_client
from verbatim_client.models.agent_list_response import AgentListResponse
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
    api_instance = verbatim_client.AgentApi(api_client)
    page_size = 25 # int | Number of items per page. (optional) (default to 25)
    page_index = 0 # int | Zero-based page index. (optional) (default to 0)

    try:
        # List agents
        api_response = api_instance.list2(page_size=page_size, page_index=page_index)
        print("The response of AgentApi->list2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentApi->list2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_size** | **int**| Number of items per page. | [optional] [default to 25]
 **page_index** | **int**| Zero-based page index. | [optional] [default to 0]

### Return type

[**AgentListResponse**](AgentListResponse.md)

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
**200** | Page of agents. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update4**
> Agent update4(agent_id, agent_update_request)

Update an agent

Patch a custom agent. Fields absent from the body keep their current value.

Because "absent" already means "leave alone", it cannot also mean "put this back
to the platform default" — that is what `reset` is for. List the nullable fields
you want un-set and they go back to tracking the platform value:

```json
{ "topK": 12, "reset": ["spirit", "temperature"] }
```

`reset` runs after the rest of the body, so a field named in both ends up cleared.

Renaming onto a name another of your agents holds, or one a platform agent
carries, answers `409`. Sending this agent's own current name does not — an
unchanged name is not a rename, so a client that echoes the whole object back is
unaffected.

Core agents (`lock: true`) belong to the platform and every organization sees the
same row — patching one answers `400`.


### Example

* Bearer (JWT) Authentication (JWT):
* Api Key Authentication (AccessToken):

```python
import verbatim_client
from verbatim_client.models.agent import Agent
from verbatim_client.models.agent_update_request import AgentUpdateRequest
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
    api_instance = verbatim_client.AgentApi(api_client)
    agent_id = UUID('123e4567-e89b-12d3-a456-426614174000') # UUID | ID of the agent to update.
    agent_update_request = {"topK":12,"rerankTopK":5} # AgentUpdateRequest | 

    try:
        # Update an agent
        api_response = api_instance.update4(agent_id, agent_update_request)
        print("The response of AgentApi->update4:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentApi->update4: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_id** | **UUID**| ID of the agent to update. | 
 **agent_update_request** | [**AgentUpdateRequest**](AgentUpdateRequest.md)|  | 

### Return type

[**Agent**](Agent.md)

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
**404** | No agent with this id is visible to your organization. |  -  |
**400** | The agent is a core agent (&#x60;lock: true&#x60;), &#x60;reset&#x60; names a field that has no platform default, or a value fails validation. |  -  |
**409** | The requested &#x60;name&#x60; is carried by another of your agents, or by a platform agent. |  -  |
**415** | Content type not accepted by the platform. See &#x60;GET /v1/doc/accept&#x60; for the list of supported types. |  -  |
**200** | Agent updated. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

