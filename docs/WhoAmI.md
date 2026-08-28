# WhoAmI

Identity of the authenticated caller, as resolved from the Bearer token.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **UUID** | ID of the organization the caller belongs to (UUIDv4). | [optional] 
**user_id** | **str** | Unique identifier of the authenticated user (UUIDv4). | [optional] 
**email** | **str** | Email address of the authenticated user. | [optional] 
**name** | **str** | Display name of the authenticated user. | [optional] 
**timestamp** | **datetime** | Reference timestamp the metadata were computed at (ISO-8601, UTC). | [optional] 

## Example

```python
from verbatim_client.models.who_am_i import WhoAmI

# TODO update the JSON string below
json = "{}"
# create an instance of WhoAmI from a JSON string
who_am_i_instance = WhoAmI.from_json(json)
# print the JSON string representation of the object
print(WhoAmI.to_json())

# convert the object into a dict
who_am_i_dict = who_am_i_instance.to_dict()
# create an instance of WhoAmI from a dict
who_am_i_from_dict = WhoAmI.from_dict(who_am_i_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


