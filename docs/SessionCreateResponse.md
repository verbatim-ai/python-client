# SessionCreateResponse

Acknowledgement returned after opening a new session.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | ID of the newly created session (UUIDv4). | 
**user_id** | **str** | Identifier of the user who opened the session (echo of the JWT subject). | [optional] 
**corpus_id** | **List[UUID]** | IDs of the corpora the session is bound to (UUIDv4). | 
**model** | **str** |  | [optional] 
**metadata** | **Dict[str, Optional[object]]** | Arbitrary JSON metadata attached to the session. | [optional] 
**created_at** | **datetime** | Creation timestamp of the session (ISO-8601, UTC). | 
**updated_at** | **datetime** | Last modification of the session (ISO-8601, UTC). Equal to &#x60;createdAt&#x60; on a session that has just been created. | 

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


