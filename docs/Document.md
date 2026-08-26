# Document

A file ingested into a corpus. Holds metadata; the binary content is streamed via the download endpoint.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the document (UUIDv4). | 
**corpus_id** | **str** | ID of the corpus this document belongs to. | 
**user_id** | **str** | Identifier of the user who uploaded the document. May be null when no user identity was provided at upload time. | [optional] 
**filename** | **str** | Original filename, as provided at upload time. | 
**content_type** | **str** | MIME content type of the file. | 
**status** | **str** | Lifecycle status of the document. AWAITING_UPLOAD: created via init, file not yet uploaded. READY: ingestion completed. | 
**path** | **str** | Internal storage path of the file. Opaque — use the download endpoint instead. | [optional] 
**provider** | **str** | Free-form label identifying the source of the document. | [optional] 
**lang** | **str** | ISO-639 language code used during ingestion. | [optional] 
**metadata** | **Dict[str, Optional[object]]** | Arbitrary JSON metadata attached to the document. Stored as JSONB. | [optional] 
**tags** | **List[str]** | Free-form labels used to classify the document. Filter on them with &#x60;GET /v1/doc/?tags&#x3D;…&#x60;. Null when the document carries no tag. | [optional] 
**chunk** | **Dict[str, Optional[object]]** | Chunking configuration used when ingesting this document — an Unstructured chunking option set (&#x60;strategy&#x60;, &#x60;max_characters&#x60;, &#x60;overlap&#x60;, …). Null means the platform default was used (&#x60;by_title&#x60;, &#x60;max_characters: 10000&#x60;, &#x60;combine_text_under_n_chars: 1000&#x60;). See &#x60;DocumentInitRequest.chunk&#x60; for the full key reference. | [optional] 
**doc_create** | **datetime** | Original creation date of the source document (ISO-8601, UTC). Falls back to upload time when unknown. | [optional] 
**doc_update** | **datetime** | Original last-modified date of the source document (ISO-8601, UTC). Falls back to upload time when unknown. | [optional] 
**created_at** | **datetime** | Date the document was uploaded to the platform (ISO-8601, UTC). | 
**updated_at** | **datetime** | Last update timestamp of the document row (ISO-8601, UTC). | 
**size** | **int** | Size of the source file in bytes. Set after ingestion. | [optional] 
**tokens** | **int** | Number of LLM tokens consumed to produce the summary. Set after ingestion. | [optional] 
**nb_words** | **int** | Number of words in the source document. Set after ingestion. | [optional] 
**nb_pages** | **int** | Number of pages of the source document. &#x60;0&#x60; means *not counted yet* — the rendering pipeline reports it during ingestion, so it stays &#x60;0&#x60; until then (and for formats that have no pages). Use it to bound the &#x60;pages&#x60; indices of &#x60;GET /v1/doc/{id}/preview-urls&#x60;, whose valid range is &#x60;0..nbPages-1&#x60;. | [optional] 

## Example

```python
from verbatim_client.models.document import Document

# TODO update the JSON string below
json = "{}"
# create an instance of Document from a JSON string
document_instance = Document.from_json(json)
# print the JSON string representation of the object
print(Document.to_json())

# convert the object into a dict
document_dict = document_instance.to_dict()
# create an instance of Document from a dict
document_from_dict = Document.from_dict(document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


