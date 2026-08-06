# DocumentPreviewUrl

Presigned URL granting direct client GET access to a single rendered preview image of one page of a document, at one rendering size.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **int** | Zero-based page index this preview represents. | [optional] 
**size** | **str** | Rendering size of the preview image. | 
**url** | **str** | Presigned URL to GET the preview image. Single-use, time-limited. | 
**expires_at** | **datetime** | Wall-clock expiration of &#x60;url&#x60; (ISO-8601, UTC). After this, a fresh request is required. | 

## Example

```python
from verbatim_client.models.document_preview_url import DocumentPreviewUrl

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentPreviewUrl from a JSON string
document_preview_url_instance = DocumentPreviewUrl.from_json(json)
# print the JSON string representation of the object
print(DocumentPreviewUrl.to_json())

# convert the object into a dict
document_preview_url_dict = document_preview_url_instance.to_dict()
# create an instance of DocumentPreviewUrl from a dict
document_preview_url_from_dict = DocumentPreviewUrl.from_dict(document_preview_url_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


