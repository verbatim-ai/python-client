# SessionUpdateRequest

Payload to patch a session. Only the fields you set are updated; omit a field to leave it unchanged.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model** | **str** | New LLM for the session. Must be installed on the Ollama runtime. Omit to keep the current model. | [optional] 
**system** | **str** | New system prompt. Omit to keep the current prompt. | [optional] 
**temperature** | **float** | New sampling temperature. Omit to keep the current value. | [optional] 
**thinking** | **bool** | Enable or disable thinking mode. Omit to keep the current value. | [optional] 
**metadata** | **Dict[str, Optional[object]]** | New JSON metadata. When provided, **replaces** the existing metadata map; omit to keep it unchanged. | [optional] 

## Example

```python
from verbatim_client.models.session_update_request import SessionUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SessionUpdateRequest from a JSON string
session_update_request_instance = SessionUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(SessionUpdateRequest.to_json())

# convert the object into a dict
session_update_request_dict = session_update_request_instance.to_dict()
# create an instance of SessionUpdateRequest from a dict
session_update_request_from_dict = SessionUpdateRequest.from_dict(session_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


