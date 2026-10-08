# AccessTokenCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ttl** | **int** | Token validity in seconds. Defaults to 3600 (1 hour); at least 10, and at most the platform ceiling (&#x60;app.access-token.max-ttl-seconds&#x60;, 86400 by default). | [optional] 
**issuer** | **str** | Optional label identifying the system that requested the token. | [optional] 
**scope** | **List[str]** | Mandatory, non-empty list of permission scopes the token carries, each &#x60;DOMAIN:ACTION&#x60;. &#x60;GET /v1/auth/access-token/scopes&#x60; lists every valid entry. | 

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


