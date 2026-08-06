# Attachment

Document used as context to produce a system answer.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**post_id** | **str** | ID of the post (UUIDv4). | 
**doc_id** | **UUID** | ID of the document (UUIDv4). | 
**summary** | **str** | Summary of the document (markdown) | 
**pages** | **List[int]** | Sorted list of page indexes (1-based) retrieved from this document. User endpoint /{id}/preview-urls get secured preview image of the page | 
**metadata** | **Dict[str, Optional[object]]** | Metadata of the source document. | [optional] 

## Example

```python
from verbatim_client.models.attachment import Attachment

# TODO update the JSON string below
json = "{}"
# create an instance of Attachment from a JSON string
attachment_instance = Attachment.from_json(json)
# print the JSON string representation of the object
print(Attachment.to_json())

# convert the object into a dict
attachment_dict = attachment_instance.to_dict()
# create an instance of Attachment from a dict
attachment_from_dict = Attachment.from_dict(attachment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


