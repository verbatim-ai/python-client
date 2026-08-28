# PostAttachmentResponse

Attachment details for a Post

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**post_id** | **UUID** | ID of the post (UUIDv4). | 
**items** | [**List[Attachment]**](Attachment.md) | All the attachments of the post | 

## Example

```python
from verbatim_client.models.post_attachment_response import PostAttachmentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PostAttachmentResponse from a JSON string
post_attachment_response_instance = PostAttachmentResponse.from_json(json)
# print the JSON string representation of the object
print(PostAttachmentResponse.to_json())

# convert the object into a dict
post_attachment_response_dict = post_attachment_response_instance.to_dict()
# create an instance of PostAttachmentResponse from a dict
post_attachment_response_from_dict = PostAttachmentResponse.from_dict(post_attachment_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


