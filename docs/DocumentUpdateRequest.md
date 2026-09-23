# DocumentUpdateRequest

Payload to patch a document. Only the fields you set are updated; omit a field to leave it unchanged.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filename** | **str** | New filename, including extension. 1–256 characters. Display only — it does not move the stored object nor re-trigger ingestion. Omit to keep the current filename. | [optional] 
**doc_create** | **datetime** | New creation date of the **source** document (ISO-8601, UTC). Describes the original file, not the platform row — &#x60;createdAt&#x60; is not affected. Omit to keep the current value. This is how you correct a date the platform had to guess at: a document uploaded without &#x60;docCreate&#x60; carries the upload instant, not null. &#x60;null&#x60; cannot be stored — sending it means *leave it alone*, not *clear it*. | [optional] 
**doc_update** | **datetime** | New last-modified date of the **source** document (ISO-8601, UTC). Describes the original file, not the platform row — &#x60;updatedAt&#x60; is not affected. Omit to keep the current value; it cannot be cleared, on the same terms as &#x60;docCreate&#x60;. Note that &#x60;PUT /v1/doc/{id}/init&#x60; re-stamps it on its own, so patch it *after* replacing the content, not before. | [optional] 
**metadata** | **Dict[str, Optional[object]]** | New JSON metadata. When provided, **replaces** the existing metadata map; omit to keep it unchanged. | [optional] 
**tags** | **List[str]** | New tag list. When provided, **replaces** the existing tags; omit to keep them unchanged. Send &#x60;[]&#x60; to clear every tag. Blanks are dropped and duplicates collapsed; at most 32 tags of 64 characters each. | [optional] 
**chunk** | **Dict[str, Optional[object]]** | New chunking configuration — an Unstructured chunking option set (&#x60;strategy&#x60;, &#x60;max_characters&#x60;, &#x60;new_after_n_chars&#x60;, &#x60;overlap&#x60;, &#x60;overlap_all&#x60;, &#x60;combine_text_under_n_chars&#x60;, &#x60;multipage_sections&#x60;). See &#x60;DocumentInitRequest.chunk&#x60; for the full key reference.  When provided it **replaces** the stored object wholesale — there is no per-key merge, so resend every key you want to keep. Omit the field to leave the configuration untouched, or send &#x60;{}&#x60; to drop it and fall back to the platform default.  Applies to the **next** ingestion. Changing it does not re-chunk an already ingested document: call &#x60;PUT /v1/doc/{id}/init&#x60; and re-commit to rebuild the embeddings with the new configuration.  | [optional] 

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


