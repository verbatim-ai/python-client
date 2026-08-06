# WidgetAttachmentPage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**index** | **int** | Index of the page (1-based) | 
**preview_small_url** | **str** |  | [optional] 
**preview_small_large** | **str** |  | [optional] 

## Example

```python
from verbatim_client.models.widget_attachment_page import WidgetAttachmentPage

# TODO update the JSON string below
json = "{}"
# create an instance of WidgetAttachmentPage from a JSON string
widget_attachment_page_instance = WidgetAttachmentPage.from_json(json)
# print the JSON string representation of the object
print(WidgetAttachmentPage.to_json())

# convert the object into a dict
widget_attachment_page_dict = widget_attachment_page_instance.to_dict()
# create an instance of WidgetAttachmentPage from a dict
widget_attachment_page_from_dict = WidgetAttachmentPage.from_dict(widget_attachment_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


