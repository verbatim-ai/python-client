# DocumentPreviewUrls

Presigned URLs for the rendered preview images of a document. Each entry pairs a page index with a rendering size; the client picks the (page, size) it needs.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID of the document the previews belong to. | [optional] 
**items** | [**List[DocumentPreviewUrl]**](DocumentPreviewUrl.md) | Presigned preview URLs, one per (page, size). May be empty when no preview pages have been generated yet. | [optional] 

## Example

```python
from verbatim_client.models.document_preview_urls import DocumentPreviewUrls

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentPreviewUrls from a JSON string
document_preview_urls_instance = DocumentPreviewUrls.from_json(json)
# print the JSON string representation of the object
print(DocumentPreviewUrls.to_json())

# convert the object into a dict
document_preview_urls_dict = document_preview_urls_instance.to_dict()
# create an instance of DocumentPreviewUrls from a dict
document_preview_urls_from_dict = DocumentPreviewUrls.from_dict(document_preview_urls_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


