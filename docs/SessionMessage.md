# SessionMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**text** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**sent_at** | **datetime** |  | [optional] 

## Example

```python
from verbatim_client.models.session_message import SessionMessage

# TODO update the JSON string below
json = "{}"
# create an instance of SessionMessage from a JSON string
session_message_instance = SessionMessage.from_json(json)
# print the JSON string representation of the object
print(SessionMessage.to_json())

# convert the object into a dict
session_message_dict = session_message_instance.to_dict()
# create an instance of SessionMessage from a dict
session_message_from_dict = SessionMessage.from_dict(session_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


