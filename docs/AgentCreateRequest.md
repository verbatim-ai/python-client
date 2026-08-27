# AgentCreateRequest

Payload to create a custom agent inside your organization.  Only `name` is required. Every other field falls back to a documented default, so the smallest useful body is `{\"name\": \"...\"}` — and each field left out stays tied to the platform default rather than being frozen at today's value.  The created agent is always a custom one: it is attached to the organization carried by your credentials, `lock` is `false` and `default` is `false`. Core agents are seeded by the platform and cannot be created over the API. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Human-readable name of the agent. Max 128 characters, and unique in the listing you see — a name one of your own agents uses, or one a platform agent (&#x60;lock: true&#x60;) carries, answers &#x60;409&#x60;. Compared exactly, so &#x60;Support&#x60; and &#x60;support&#x60; are two names and &#x60;Verbatim Default v2&#x60; is free. | 
**description** | **str** | Free-form description of what this agent is for. | [optional] 
**top_k** | **int** | Chunks the vector search returns, before re-ranking narrows them down. Defaults to &#x60;5&#x60;. | [optional] 
**rerank** | **bool** | Whether retrieved chunks are re-ranked by an LLM before the answer is generated. Defaults to &#x60;true&#x60;. | [optional] 
**rerank_top_k** | **int** | Chunks kept after re-ranking. Omit to track the platform default. | [optional] 
**context** | **str** | First third of the system instruction — what the model is looking at. Omit to track the platform default. | [optional] 
**behaviour** | **str** | Second third of the system instruction — how the model should act. Omit to track the platform default. | [optional] 
**spirit** | **str** | Last third of the system instruction — the tone it should take. Omit to track the platform default. | [optional] 
**use_history** | **bool** | When &#x60;false&#x60;, previous posts of the session are not replayed. Defaults to &#x60;true&#x60;. | [optional] 
**history_size** | **int** | Number of trailing posts replayed. Omit to replay the whole session. | [optional] 
**thinking_mode** | **str** | Reasoning budget the model spends before answering. Defaults to &#x60;HIGH&#x60;. | [optional] 
**temperature** | **float** | Sampling temperature, between 0 and 1. Omit to leave the model default untouched. | [optional] 
**rerank_model** | **str** | Model used for re-ranking. Must be one of the names &#x60;GET /v1/config/model&#x60; advertises. | [optional] 
**base_model** | **str** | Model used to generate the answer. Must be one of the names &#x60;GET /v1/config/model&#x60; advertises. Omit to keep whatever model the session was created with. | [optional] 

## Example

```python
from verbatim_client.models.agent_create_request import AgentCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AgentCreateRequest from a JSON string
agent_create_request_instance = AgentCreateRequest.from_json(json)
# print the JSON string representation of the object
print(AgentCreateRequest.to_json())

# convert the object into a dict
agent_create_request_dict = agent_create_request_instance.to_dict()
# create an instance of AgentCreateRequest from a dict
agent_create_request_from_dict = AgentCreateRequest.from_dict(agent_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


