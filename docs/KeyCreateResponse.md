# KeyCreateResponse

Acknowledgement returned after registering a new key slot. The key starts in `INACTIVE` state with no content.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID of the newly created key (UUIDv4). Use this value as the &#x60;kid&#x60; JWT header when signing tokens. | 
**org_id** | **str** | ID of the owning organization (UUIDv4). | 
**name** | **str** | Name of the key. | 
**description** | **str** | Description of the key. | [optional] 
**format** | **str** | Format of the key content. | 
**state** | **str** | Initial lifecycle state — always &#x60;INACTIVE&#x60; right after creation. | 
**created_at** | **datetime** | Creation timestamp (ISO-8601, UTC). | 

## Example

```python
from verbatim_client.models.key_create_response import KeyCreateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of KeyCreateResponse from a JSON string
key_create_response_instance = KeyCreateResponse.from_json(json)
# print the JSON string representation of the object
print(KeyCreateResponse.to_json())

# convert the object into a dict
key_create_response_dict = key_create_response_instance.to_dict()
# create an instance of KeyCreateResponse from a dict
key_create_response_from_dict = KeyCreateResponse.from_dict(key_create_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


