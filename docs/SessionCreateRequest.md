# SessionCreateRequest

Payload to open a new conversation session. A session needs only the corpora it searches: how its queries are answered is decided per query by the agent they name, not here. The owner is taken from your token.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**corpus_ids** | **List[UUID]** | IDs of the corpora the session is bound to (UUIDv4). A session may search across several corpora. | 
**metadata** | **Dict[str, Optional[object]]** | Arbitrary JSON metadata attached to the session. Stored as JSONB. | [optional] 

## Example

```python
from verbatim_client.models.session_create_request import SessionCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SessionCreateRequest from a JSON string
session_create_request_instance = SessionCreateRequest.from_json(json)
# print the JSON string representation of the object
print(SessionCreateRequest.to_json())

# convert the object into a dict
session_create_request_dict = session_create_request_instance.to_dict()
# create an instance of SessionCreateRequest from a dict
session_create_request_from_dict = SessionCreateRequest.from_dict(session_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


