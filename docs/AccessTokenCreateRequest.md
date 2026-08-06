# AccessTokenCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ttl** | **int** | Token validity in seconds. Defaults to 3600 (1 hour). | [optional] 
**issuer** | **str** | Optional label identifying the system that requested the token. | [optional] 
**email** | **str** | Optional email of the end-user the token is issued for. | [optional] 
**user_id** | **str** | Optional user identifier. | [optional] 
**scope** | **List[str]** | Optional list of permission scopes to associate with the token. Pattern is DOMAIN:ACTION, where DOMAIN must be one of the values [doc|corpus|session|post|config] and ACTION one of the values [create|read|update|delete] | [optional] 

## Example

```python
from verbatim_client.models.access_token_create_request import AccessTokenCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AccessTokenCreateRequest from a JSON string
access_token_create_request_instance = AccessTokenCreateRequest.from_json(json)
# print the JSON string representation of the object
print(AccessTokenCreateRequest.to_json())

# convert the object into a dict
access_token_create_request_dict = access_token_create_request_instance.to_dict()
# create an instance of AccessTokenCreateRequest from a dict
access_token_create_request_from_dict = AccessTokenCreateRequest.from_dict(access_token_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


