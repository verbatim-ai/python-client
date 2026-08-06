# KeyUpdateRequest

Patch the name and/or description of an existing key. Raw RSA content, format, and state are not editable here.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | New name of the key. Omit to keep the current name. | [optional] 
**description** | **str** | New description of the key. Omit to keep the current description. | [optional] 

## Example

```python
from verbatim_client.models.key_update_request import KeyUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of KeyUpdateRequest from a JSON string
key_update_request_instance = KeyUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(KeyUpdateRequest.to_json())

# convert the object into a dict
key_update_request_dict = key_update_request_instance.to_dict()
# create an instance of KeyUpdateRequest from a dict
key_update_request_from_dict = KeyUpdateRequest.from_dict(key_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


