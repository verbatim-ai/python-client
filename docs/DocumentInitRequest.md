# DocumentInitRequest

Body of POST /v1/doc/init. Declares a document and requests a presigned PUT URL for direct-to-storage upload.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**corpus_id** | **UUID** | ID of the corpus the document will be ingested into. | 
**filename** | **str** | Original filename, including extension. | 
**content_type** | **str** | MIME content type the client will PUT. Must be in the platform-supported list (see GET /v1/doc/accept). The client MUST send the exact same value in the PUT &#x60;Content-Type&#x60; header. | 
**lang** | **str** | ISO-639 language code used by the LLM during summarization. Defaults to &#x60;en&#x60;. | [optional] 
**provider** | **str** | Free-form label identifying the source of the document. | [optional] 
**user_id** | **str** | Identifier of the user uploading the document. When the caller&#39;s JWT carries a &#x60;userId&#x60; claim, the value MUST match it — uploads on behalf of a different user are rejected with 403. May be omitted; in that case the JWT&#39;s &#x60;userId&#x60; is used when present. | [optional] 
**doc_create** | **datetime** | Original creation date of the source document (ISO-8601, UTC). | [optional] 
**doc_update** | **datetime** | Original last-modified date of the source document (ISO-8601, UTC). | [optional] 
**metadata** | **Dict[str, Optional[object]]** | Arbitrary key/value metadata attached to the document. Stored as JSONB. | [optional] 

## Example

```python
from verbatim_client.models.document_init_request import DocumentInitRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentInitRequest from a JSON string
document_init_request_instance = DocumentInitRequest.from_json(json)
# print the JSON string representation of the object
print(DocumentInitRequest.to_json())

# convert the object into a dict
document_init_request_dict = document_init_request_instance.to_dict()
# create an instance of DocumentInitRequest from a dict
document_init_request_from_dict = DocumentInitRequest.from_dict(document_init_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


