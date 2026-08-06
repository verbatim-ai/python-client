# KeyCreateRequest

Register a new key slot. The PEM content is uploaded later via `POST /_/v1/key/{id}/publish`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Human-readable name of the key. | 
**description** | **str** | Free-form description of the key. | [optional] 

## Example

```python
from verbatim_client.models.key_create_request import KeyCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of KeyCreateRequest from a JSON string
key_create_request_instance = KeyCreateRequest.from_json(json)
# print the JSON string representation of the object
print(KeyCreateRequest.to_json())

# convert the object into a dict
key_create_request_dict = key_create_request_instance.to_dict()
# create an instance of KeyCreateRequest from a dict
key_create_request_from_dict = KeyCreateRequest.from_dict(key_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


