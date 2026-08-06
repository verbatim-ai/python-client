# WidgetSessionRequestBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** |  | [optional] 
**session_uuid** | **str** |  | [optional] 

## Example

```python
from verbatim_client.models.widget_session_request_body import WidgetSessionRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of WidgetSessionRequestBody from a JSON string
widget_session_request_body_instance = WidgetSessionRequestBody.from_json(json)
# print the JSON string representation of the object
print(WidgetSessionRequestBody.to_json())

# convert the object into a dict
widget_session_request_body_dict = widget_session_request_body_instance.to_dict()
# create an instance of WidgetSessionRequestBody from a dict
widget_session_request_body_from_dict = WidgetSessionRequestBody.from_dict(widget_session_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


