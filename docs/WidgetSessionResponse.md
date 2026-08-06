# WidgetSessionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamp** | **datetime** | Timestamp when the session was created | [optional] 
**session_id** | **UUID** | Id of the session | [optional] 
**display_name** | **str** | Display name of the session (session history in the backoffice | [optional] 
**widget_name** | **str** | Name of the widget of init the session | [optional] 
**corpus** | **List[UUID]** | a list of corpus attach to the session | [optional] 

## Example

```python
from verbatim_client.models.widget_session_response import WidgetSessionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WidgetSessionResponse from a JSON string
widget_session_response_instance = WidgetSessionResponse.from_json(json)
# print the JSON string representation of the object
print(WidgetSessionResponse.to_json())

# convert the object into a dict
widget_session_response_dict = widget_session_response_instance.to_dict()
# create an instance of WidgetSessionResponse from a dict
widget_session_response_from_dict = WidgetSessionResponse.from_dict(widget_session_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


