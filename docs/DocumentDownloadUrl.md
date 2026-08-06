# DocumentDownloadUrl

Presigned URL granting direct client download access to the archived document. The content is served by the storage backend (S3), not by this server.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**download_url** | **str** | Presigned URL to GET the document content. Single-use, time-limited. | [optional] 
**expires_at** | **datetime** | Wall-clock expiration of &#x60;downloadUrl&#x60; (ISO-8601, UTC). After this, a fresh request is required. | [optional] 
**filename** | **str** | Original filename of the document. The client can use it for the local save name. | [optional] 
**content_type** | **str** | MIME content type of the document. | [optional] 

## Example

```python
from verbatim_client.models.document_download_url import DocumentDownloadUrl

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentDownloadUrl from a JSON string
document_download_url_instance = DocumentDownloadUrl.from_json(json)
# print the JSON string representation of the object
print(DocumentDownloadUrl.to_json())

# convert the object into a dict
document_download_url_dict = document_download_url_instance.to_dict()
# create an instance of DocumentDownloadUrl from a dict
document_download_url_from_dict = DocumentDownloadUrl.from_dict(document_download_url_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


