# WidgetSessionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**widget_name** | **str** | Name of the widget | 
**display_name** | **str** | Display name of the session (session history). When not set, a default display name is set from Widget name | [optional] 
**corpus** | **List[UUID]** | List of Corpus UID used by the session. Check Corpus domain to learn how init a Corpus | 

## Example

```python
from verbatim_client.models.widget_session_request import WidgetSessionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WidgetSessionRequest from a JSON string
widget_session_request_instance = WidgetSessionRequest.from_json(json)
# print the JSON string representation of the object
print(WidgetSessionRequest.to_json())

# convert the object into a dict
widget_session_request_dict = widget_session_request_instance.to_dict()
# create an instance of WidgetSessionRequest from a dict
widget_session_request_from_dict = WidgetSessionRequest.from_dict(widget_session_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


