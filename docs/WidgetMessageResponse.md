# WidgetMessageResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**WidgetMessageResponseItem**](WidgetMessageResponseItem.md) |  | [optional] 

## Example

```python
from verbatim_client.models.widget_message_response import WidgetMessageResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WidgetMessageResponse from a JSON string
widget_message_response_instance = WidgetMessageResponse.from_json(json)
# print the JSON string representation of the object
print(WidgetMessageResponse.to_json())

# convert the object into a dict
widget_message_response_dict = widget_message_response_instance.to_dict()
# create an instance of WidgetMessageResponse from a dict
widget_message_response_from_dict = WidgetMessageResponse.from_dict(widget_message_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


