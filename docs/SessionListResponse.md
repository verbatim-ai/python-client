# SessionListResponse

Paginated list of sessions. Echoes the filter that produced it.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**corpus_id** | **UUID** | Echo of the corpus filter, when the listing was filtered by corpus. | [optional] 
**user_id** | **str** | Echo of the user filter, when the listing was filtered by user. | [optional] 
**metadata** | **Dict[str, Optional[object]]** | Echo of the metadata fragment used to filter the listing, when applicable. | [optional] 
**page_index** | **int** | Zero-based index of the returned page. | 
**page_size** | **int** | Number of items requested per page. | 
**total** | **int** | Total number of sessions matching the filter across every page. | 
**items** | [**List[Session]**](Session.md) | Sessions contained in this page, newest first. | [optional] 

## Example

```python
from verbatim_client.models.session_list_response import SessionListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SessionListResponse from a JSON string
session_list_response_instance = SessionListResponse.from_json(json)
# print the JSON string representation of the object
print(SessionListResponse.to_json())

# convert the object into a dict
session_list_response_dict = session_list_response_instance.to_dict()
# create an instance of SessionListResponse from a dict
session_list_response_from_dict = SessionListResponse.from_dict(session_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


