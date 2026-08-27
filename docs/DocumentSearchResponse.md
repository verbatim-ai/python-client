# DocumentSearchResponse

Page of documents matching a search, with the total number of matches.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**corpus_id** | **str** | ID of the searched corpus (UUIDv4). | 
**page_index** | **int** | Zero-based index of the returned page. | [default to 0]
**page_size** | **int** | Number of documents this page can hold — the requested &#x60;pageSize&#x60;. The last page may carry fewer items. | [default to 25]
**total** | **int** | Total number of documents matching the filters, across every page. Divide by &#x60;pageSize&#x60; to know how many pages to walk. | 
**items** | [**List[Document]**](Document.md) | Documents contained in this page, in the requested sort order. | 

## Example

```python
from verbatim_client.models.document_search_response import DocumentSearchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentSearchResponse from a JSON string
document_search_response_instance = DocumentSearchResponse.from_json(json)
# print the JSON string representation of the object
print(DocumentSearchResponse.to_json())

# convert the object into a dict
document_search_response_dict = document_search_response_instance.to_dict()
# create an instance of DocumentSearchResponse from a dict
document_search_response_from_dict = DocumentSearchResponse.from_dict(document_search_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


