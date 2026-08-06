# DocumentInit

Result of initializing a direct-to-storage upload. The client MUST PUT the file content to `uploadUrl` with the matching `Content-Type` header before calling the commit endpoint.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**document** | [**Document**](Document.md) | Created document, in AWAITING_UPLOAD status until commit is called. | [optional] 
**upload_url** | **str** | Presigned URL to PUT the file content to. Single-use, time-limited. | [optional] 
**expires_at** | **datetime** | Wall-clock expiration of &#x60;uploadUrl&#x60; (ISO-8601, UTC). After this, a fresh init is required. | [optional] 

## Example

```python
from verbatim_client.models.document_init import DocumentInit

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentInit from a JSON string
document_init_instance = DocumentInit.from_json(json)
# print the JSON string representation of the object
print(DocumentInit.to_json())

# convert the object into a dict
document_init_dict = document_init_instance.to_dict()
# create an instance of DocumentInit from a dict
document_init_from_dict = DocumentInit.from_dict(document_init_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


