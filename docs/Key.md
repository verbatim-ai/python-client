# Key

RSA public key owned by an organization and used to verify JWT signatures.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the key (UUIDv4). Use this value as the &#x60;kid&#x60; JWT header when signing tokens. | 
**org_id** | **str** | ID of the owning organization (UUIDv4). | 
**name** | **str** | Human-readable name of the key. | 
**description** | **str** | Free-form description of the key, set at creation. | [optional] 
**format** | **str** | Format of the key content. | 
**preview** | **str** | Preview of the key, only the 100 first characters of the real key content | [optional] 
**state** | **str** | Lifecycle state. A key is &#x60;INACTIVE&#x60; at creation, becomes &#x60;ACTIVE&#x60; once published, and can be toggled back and forth via activate/deactivate. Only &#x60;ACTIVE&#x60; keys verify JWTs. | 
**created_at** | **datetime** | Creation timestamp (ISO-8601, UTC). | 
**updated_at** | **datetime** | Last update timestamp (ISO-8601, UTC). | 

## Example

```python
from verbatim_client.models.key import Key

# TODO update the JSON string below
json = "{}"
# create an instance of Key from a JSON string
key_instance = Key.from_json(json)
# print the JSON string representation of the object
print(Key.to_json())

# convert the object into a dict
key_dict = key_instance.to_dict()
# create an instance of Key from a dict
key_from_dict = Key.from_dict(key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


