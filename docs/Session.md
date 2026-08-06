# Session

Conversation thread bound to a user and to one or more corpora.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the session (UUIDv4). | 
**user_id** | **str** | Identifier of the user who opened the session, as carried by the JWT. Stored as a free-form string so non-UUID identity providers are supported. | [optional] 
**corpus_ids** | **List[str]** | IDs of the corpora the session is bound to (UUIDv4). | 
**model** | **str** | LLM bound to the session. | 
**system** | **str** | System prompt the LLM was initialised with. | [optional] 
**temperature** | **float** | Sampling temperature configured on the session. | [optional] 
**thinking** | **bool** | Whether the model&#39;s *thinking* mode is enabled on this session. | [optional] 
**metadata** | **Dict[str, Optional[object]]** | Arbitrary JSON metadata attached to the session. | [optional] 
**created_at** | **datetime** | Creation timestamp of the session (ISO-8601, UTC). | 

## Example

```python
from verbatim_client.models.session import Session

# TODO update the JSON string below
json = "{}"
# create an instance of Session from a JSON string
session_instance = Session.from_json(json)
# print the JSON string representation of the object
print(Session.to_json())

# convert the object into a dict
session_dict = session_instance.to_dict()
# create an instance of Session from a dict
session_from_dict = Session.from_dict(session_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


