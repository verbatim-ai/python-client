# SessionCreateResponse

Acknowledgement returned after opening a new session.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID of the newly created session (UUIDv4). | 
**user_id** | **str** | Identifier of the user who opened the session (echo of the JWT subject). | [optional] 
**corpus_id** | **List[str]** | IDs of the corpora the session is bound to (UUIDv4). | 
**model** | **str** | LLM bound to the session. | 
**system** | **str** | System prompt the LLM was initialised with. | [optional] 
**temperature** | **float** | Sampling temperature configured on the session. | [optional] 
**thinking** | **bool** | Whether the model&#39;s *thinking* mode is enabled on this session. | [optional] 
**metadata** | **Dict[str, Optional[object]]** | Arbitrary JSON metadata attached to the session. | [optional] 
**created_at** | **datetime** | Creation timestamp of the session (ISO-8601, UTC). | 

## Example

```python
from verbatim_client.models.session_create_response import SessionCreateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SessionCreateResponse from a JSON string
session_create_response_instance = SessionCreateResponse.from_json(json)
# print the JSON string representation of the object
print(SessionCreateResponse.to_json())

# convert the object into a dict
session_create_response_dict = session_create_response_instance.to_dict()
# create an instance of SessionCreateResponse from a dict
session_create_response_from_dict = SessionCreateResponse.from_dict(session_create_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


