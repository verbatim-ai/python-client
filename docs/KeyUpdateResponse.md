# KeyUpdateResponse

Acknowledgement returned after updating a key's name or description.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID of the key (UUIDv4). | 
**org_id** | **str** | ID of the owning organization (UUIDv4). | 
**name** | **str** | Name of the key. | 
**description** | **str** | Description of the key. | [optional] 
**state** | **str** | Lifecycle state. | 
**created_at** | **datetime** | Original creation timestamp (ISO-8601, UTC). | 
**updated_at** | **datetime** | Timestamp of this update (ISO-8601, UTC). | 

## Example

```python
from verbatim_client.models.key_update_response import KeyUpdateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of KeyUpdateResponse from a JSON string
key_update_response_instance = KeyUpdateResponse.from_json(json)
# print the JSON string representation of the object
print(KeyUpdateResponse.to_json())

# convert the object into a dict
key_update_response_dict = key_update_response_instance.to_dict()
# create an instance of KeyUpdateResponse from a dict
key_update_response_from_dict = KeyUpdateResponse.from_dict(key_update_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


