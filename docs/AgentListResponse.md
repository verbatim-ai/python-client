# AgentListResponse

Paginated list of the agents an organization can use: its own custom agents plus the platform's core agents, core first.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page_index** | **int** | Zero-based index of the returned page. | [optional] 
**items** | [**List[Agent]**](Agent.md) | Agents contained in this page. Core agents (&#x60;lock: true&#x60;) sort first, then custom agents by name. | [optional] 

## Example

```python
from verbatim_client.models.agent_list_response import AgentListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AgentListResponse from a JSON string
agent_list_response_instance = AgentListResponse.from_json(json)
# print the JSON string representation of the object
print(AgentListResponse.to_json())

# convert the object into a dict
agent_list_response_dict = agent_list_response_instance.to_dict()
# create an instance of AgentListResponse from a dict
agent_list_response_from_dict = AgentListResponse.from_dict(agent_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


