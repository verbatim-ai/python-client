# WidgetAttachment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**doc_id** | **UUID** | ID of the document (UUIDv4). | 
**summary** | **str** | Summary of the document (markdown) | 
**pages** | [**List[WidgetAttachmentPage]**](WidgetAttachmentPage.md) | Sorted list of page (1-based) retrieved from this document with preview image url. | 
**metadata** | **Dict[str, Optional[object]]** | Metadata of the source document. | [optional] 
**preview_expiration_date** | **datetime** |  | [optional] 

## Example

```python
from verbatim_client.models.widget_attachment import WidgetAttachment

# TODO update the JSON string below
json = "{}"
# create an instance of WidgetAttachment from a JSON string
widget_attachment_instance = WidgetAttachment.from_json(json)
# print the JSON string representation of the object
print(WidgetAttachment.to_json())

# convert the object into a dict
widget_attachment_dict = widget_attachment_instance.to_dict()
# create an instance of WidgetAttachment from a dict
widget_attachment_from_dict = WidgetAttachment.from_dict(widget_attachment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


