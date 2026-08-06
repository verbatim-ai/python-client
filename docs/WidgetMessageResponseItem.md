# WidgetMessageResponseItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**input** | [**WidgetSessionRequestBody**](WidgetSessionRequestBody.md) |  | [optional] 
**output** | [**WidgetSessionRequestBody**](WidgetSessionRequestBody.md) |  | [optional] 
**session_uuid** | **str** |  | [optional] 

## Example

```python
from verbatim_client.models.widget_message_response_item import WidgetMessageResponseItem

# TODO update the JSON string below
json = "{}"
# create an instance of WidgetMessageResponseItem from a JSON string
widget_message_response_item_instance = WidgetMessageResponseItem.from_json(json)
# print the JSON string representation of the object
print(WidgetMessageResponseItem.to_json())

# convert the object into a dict
widget_message_response_item_dict = widget_message_response_item_instance.to_dict()
# create an instance of WidgetMessageResponseItem from a dict
widget_message_response_item_from_dict = WidgetMessageResponseItem.from_dict(widget_message_response_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


