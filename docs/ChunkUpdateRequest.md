# ChunkUpdateRequest

Patch a chunk. Only the fields present in the body are applied; the rest keep their current value. `id`, `documentId`, `corpusId` and `hash` are not patchable — a chunk cannot be moved to another document, and `hash` describes the text the pipeline embedded.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pages** | **List[int]** | Replacement page span: 1-based page numbers the chunk covers. Sent empty (&#x60;[]&#x60;) it clears the span, which is what a chunk belonging to no page in particular carries. Values are sorted and de-duplicated server-side, and a value below 1 is refused. | [optional] 
**metadata** | **Dict[str, Optional[object]]** | Replacement metadata. This **replaces** the object rather than merging into it — send the full map you want stored, and &#x60;{}&#x60; to clear it. | [optional] 
**body** | **str** | Replacement chunk text, written to object storage. **The vector is not recomputed**: after this call the stored embedding still describes the previous text, so the chunk keeps being retrieved for the old wording and answers with the new one. That is the intended behaviour for a typo or a redaction, and the wrong tool for a rewrite — re-ingest the document for that. | [optional] 

## Example

```python
from verbatim_client.models.chunk_update_request import ChunkUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ChunkUpdateRequest from a JSON string
chunk_update_request_instance = ChunkUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(ChunkUpdateRequest.to_json())

# convert the object into a dict
chunk_update_request_dict = chunk_update_request_instance.to_dict()
# create an instance of ChunkUpdateRequest from a dict
chunk_update_request_from_dict = ChunkUpdateRequest.from_dict(chunk_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


