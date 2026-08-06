# WidgetAttachmentResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamp** | **datetime** | Timestamp when the answer was generated | [optional] 
**post_id** | **UUID** | Id of the post related to the context | [optional] 
**items** | [**List[WidgetAttachment]**](WidgetAttachment.md) | Attachments of the post | [optional] 

## Example

```python
from verbatim_client.models.widget_attachment_response import WidgetAttachmentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WidgetAttachmentResponse from a JSON string
widget_attachment_response_instance = WidgetAttachmentResponse.from_json(json)
# print the JSON string representation of the object
print(WidgetAttachmentResponse.to_json())

# convert the object into a dict
widget_attachment_response_dict = widget_attachment_response_instance.to_dict()
# create an instance of WidgetAttachmentResponse from a dict
widget_attachment_response_from_dict = WidgetAttachmentResponse.from_dict(widget_attachment_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


