# Chunk

One embeddable piece of a document: the text that was vectorised, where it came from, and the metadata the ingestion pipeline attached to it.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Unique identifier of the chunk (UUIDv4). Same id the &#x60;attachment&#x60; records of a post point at. | 
**document_id** | **UUID** | Document the chunk was cut from. | 
**corpus_id** | **UUID** | Corpus owning the document. Not stored on the chunk — resolved through the document — and reported here because it is half of the storage key of &#x60;body&#x60;. | 
**pages** | **List[int]** | 1-based page numbers the chunk spans, ascending. A chunk is built from consecutive elements and may cross page boundaries, so this is a span rather than a single page. **Empty** for a chunk that belongs to no page in particular — the document summary is the usual case. | [optional] 
**hash** | **str** | MD5 of the chunk body as it was pushed to storage. Equal hashes mean equal text, which is how duplicated content is found across documents. Read-only — it is computed by the ingestion pipeline. | [optional] 
**metadata** | **Dict[str, Optional[object]]** | Arbitrary JSON metadata attached by the ingestion pipeline. &#x60;kind&#x60; is the key the platform itself sets — &#x60;chunk&#x60; for a piece of the document, &#x60;summary&#x60; for the generated summary. | [optional] 
**body** | **str** | The chunk text, read from object storage. Present on &#x60;GET /v1/chunk/{chunkId}&#x60;, and on the listings only when &#x60;body&#x3D;true&#x60; was passed. An empty string means the row exists but its stored body does not — a broken chunk, which is one of the things this API exists to surface. | [optional] 

## Example

```python
from verbatim_client.models.chunk import Chunk

# TODO update the JSON string below
json = "{}"
# create an instance of Chunk from a JSON string
chunk_instance = Chunk.from_json(json)
# print the JSON string representation of the object
print(Chunk.to_json())

# convert the object into a dict
chunk_dict = chunk_instance.to_dict()
# create an instance of Chunk from a dict
chunk_from_dict = Chunk.from_dict(chunk_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


