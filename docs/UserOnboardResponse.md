# UserOnboardResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **str** | ID of the organization the caller belongs to (UUIDv4). | [optional] 
**user_id** | **str** | Unique identifier of the authenticated user (UUIDv4). | [optional] 
**email** | **str** | Email address of the authenticated user. | [optional] 
**name** | **str** | Display name of the authenticated user. | [optional] 
**timestamp** | **datetime** | Reference timestamp the response were computed at (ISO-8601, UTC). | [optional] 

## Example

```python
from verbatim_client.models.user_onboard_response import UserOnboardResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UserOnboardResponse from a JSON string
user_onboard_response_instance = UserOnboardResponse.from_json(json)
# print the JSON string representation of the object
print(UserOnboardResponse.to_json())

# convert the object into a dict
user_onboard_response_dict = user_onboard_response_instance.to_dict()
# create an instance of UserOnboardResponse from a dict
user_onboard_response_from_dict = UserOnboardResponse.from_dict(user_onboard_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


