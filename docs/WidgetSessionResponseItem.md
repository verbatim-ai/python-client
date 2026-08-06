# WidgetSessionResponseItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** |  | [optional] 
**messages** | [**List[SessionMessage]**](SessionMessage.md) |  | [optional] 
**session_uuid** | **str** |  | [optional] 

## Example

```python
from verbatim_client.models.widget_session_response_item import WidgetSessionResponseItem

# TODO update the JSON string below
json = "{}"
# create an instance of WidgetSessionResponseItem from a JSON string
widget_session_response_item_instance = WidgetSessionResponseItem.from_json(json)
# print the JSON string representation of the object
print(WidgetSessionResponseItem.to_json())

# convert the object into a dict
widget_session_response_item_dict = widget_session_response_item_instance.to_dict()
# create an instance of WidgetSessionResponseItem from a dict
widget_session_response_item_from_dict = WidgetSessionResponseItem.from_dict(widget_session_response_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


