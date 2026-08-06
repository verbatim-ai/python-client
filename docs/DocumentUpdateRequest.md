# DocumentUpdateRequest

Payload to patch a document. Only the fields you set are updated; omit a field to leave it unchanged.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filename** | **str** | New filename, including extension. 1–256 characters. Display only — it does not move the stored object nor re-trigger ingestion. Omit to keep the current filename. | [optional] 
**doc_create** | **datetime** | New creation date of the **source** document (ISO-8601, UTC). Describes the original file, not the platform row — &#x60;createdAt&#x60; is not affected. Omit to keep the current value. | [optional] 
**doc_update** | **datetime** | New last-modified date of the **source** document (ISO-8601, UTC). Describes the original file, not the platform row — &#x60;updatedAt&#x60; is not affected. Omit to keep the current value. | [optional] 
**metadata** | **Dict[str, Optional[object]]** | New JSON metadata. When provided, **replaces** the existing metadata map; omit to keep it unchanged. | [optional] 

## Example

```python
from verbatim_client.models.document_update_request import DocumentUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentUpdateRequest from a JSON string
document_update_request_instance = DocumentUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(DocumentUpdateRequest.to_json())

# convert the object into a dict
document_update_request_dict = document_update_request_instance.to_dict()
# create an instance of DocumentUpdateRequest from a dict
document_update_request_from_dict = DocumentUpdateRequest.from_dict(document_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


