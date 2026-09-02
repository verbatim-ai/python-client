# ChunkListResponse

Paginated list of chunks. Echoes the filters that were actually applied — a filter that was dropped as empty does not appear here.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**corpus_id** | **UUID** | Echo of the corpus filter, when one was applied. | [optional] 
**document_id** | **UUID** | Echo of the document filter, when one was applied. | [optional] 
**hash** | **str** | Echo of the hash filter, when one was applied. | [optional] 
**page** | **int** | Echo of the page filter, when one was applied. | [optional] 
**metadata** | **Dict[str, Optional[object]]** | Echo of the metadata fragment used to filter the listing, when applicable. | [optional] 
**page_index** | **int** | Zero-based index of the returned page. | 
**page_size** | **int** | Number of items requested per page. | 
**total** | **int** | Total number of chunks matching the filters across every page. | 
**items** | [**List[Chunk]**](Chunk.md) | Chunks contained in this page, in reading order: by document, then by the first page each chunk covers, then by id. &#x60;body&#x60; is present only when &#x60;body&#x3D;true&#x60; was passed. | [optional] 

## Example

```python
from verbatim_client.models.chunk_list_response import ChunkListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ChunkListResponse from a JSON string
chunk_list_response_instance = ChunkListResponse.from_json(json)
# print the JSON string representation of the object
print(ChunkListResponse.to_json())

# convert the object into a dict
chunk_list_response_dict = chunk_list_response_instance.to_dict()
# create an instance of ChunkListResponse from a dict
chunk_list_response_from_dict = ChunkListResponse.from_dict(chunk_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


