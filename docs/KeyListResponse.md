# KeyListResponse

Paginated list of keys belonging to the caller's organization.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**org_id** | **str** | ID of the owning organization (UUIDv4). | 
**page_index** | **int** | Zero-based index of the returned page. | [optional] 
**items** | [**List[Key]**](Key.md) | Keys contained in this page. | [optional] 

## Example

```python
from verbatim_client.models.key_list_response import KeyListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of KeyListResponse from a JSON string
key_list_response_instance = KeyListResponse.from_json(json)
# print the JSON string representation of the object
print(KeyListResponse.to_json())

# convert the object into a dict
key_list_response_dict = key_list_response_instance.to_dict()
# create an instance of KeyListResponse from a dict
key_list_response_from_dict = KeyListResponse.from_dict(key_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


