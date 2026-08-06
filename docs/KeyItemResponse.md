# KeyItemResponse

Single key wrapped with its owning organization id.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**org_id** | **str** | ID of the owning organization (UUIDv4). | 
**item** | [**Key**](Key.md) | The key payload (raw RSA content is never returned). | [optional] 

## Example

```python
from verbatim_client.models.key_item_response import KeyItemResponse

# TODO update the JSON string below
json = "{}"
# create an instance of KeyItemResponse from a JSON string
key_item_response_instance = KeyItemResponse.from_json(json)
# print the JSON string representation of the object
print(KeyItemResponse.to_json())

# convert the object into a dict
key_item_response_dict = key_item_response_instance.to_dict()
# create an instance of KeyItemResponse from a dict
key_item_response_from_dict = KeyItemResponse.from_dict(key_item_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


