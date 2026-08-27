# AgentUpdateRequest

Patch a custom agent. Every field is optional; the ones you omit keep their current value.  Because an omitted field means \"leave alone\", it cannot also mean \"put this back to the platform default\". That is what `reset` is for: list the names of the nullable fields you want to un-set, and they go back to tracking the platform default instead of holding the value you gave them earlier. `reset` is applied after the rest of the body, so naming a field in both wins for `reset`.  Core agents (`lock: true`) are not writable — patching one answers `400`. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Human-readable name of the agent. Max 128 characters. Renaming onto a name another of your agents holds, or one a platform agent (&#x60;lock: true&#x60;) carries, answers &#x60;409&#x60;. Re-sending this agent&#39;s own current name is not a rename and is never a conflict. | [optional] 
**description** | **str** | Free-form description of what this agent is for. | [optional] 
**top_k** | **int** | Chunks the vector search returns, before re-ranking narrows them down. | [optional] 
**rerank** | **bool** | Whether retrieved chunks are re-ranked by an LLM before the answer is generated. | [optional] 
**rerank_top_k** | **int** | Chunks kept after re-ranking. | [optional] 
**context** | **str** | First third of the system instruction — what the model is looking at. | [optional] 
**behaviour** | **str** | Second third of the system instruction — how the model should act. | [optional] 
**spirit** | **str** | Last third of the system instruction — the tone it should take. | [optional] 
**use_history** | **bool** | When &#x60;false&#x60;, previous posts of the session are not replayed. | [optional] 
**history_size** | **int** | Number of trailing posts replayed. | [optional] 
**thinking_mode** | **str** | Reasoning budget the model spends before answering. | [optional] 
**temperature** | **float** | Model temperature. Temperature must match model range. | [optional] 
**rerank_model** | **str** | Model used for re-ranking. Must be one of the names &#x60;GET /v1/config/model&#x60; advertises. | [optional] 
**base_model** | **str** | Model used to generate the answer. Must be one of the names &#x60;GET /v1/config/model&#x60; advertises. | [optional] 
**reset** | **List[str]** | Fields to un-set, so they go back to tracking the platform default. Only the nullable fields can be reset; anything else answers &#x60;400&#x60;. Applied after the rest of the body. | [optional] 

## Example

```python
from verbatim_client.models.agent_update_request import AgentUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AgentUpdateRequest from a JSON string
agent_update_request_instance = AgentUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(AgentUpdateRequest.to_json())

# convert the object into a dict
agent_update_request_dict = agent_update_request_instance.to_dict()
# create an instance of AgentUpdateRequest from a dict
agent_update_request_from_dict = AgentUpdateRequest.from_dict(agent_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


