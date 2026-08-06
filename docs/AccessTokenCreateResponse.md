# AccessTokenCreateResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | **str** | The opaque access token value. Pass this as the X-Access-Token header on API calls. | [optional] 
**created_at** | **datetime** | Creation timestamp (ISO-8601, UTC). | [optional] 
**expires_at** | **datetime** | Expiry timestamp (ISO-8601, UTC). Token is invalid after this date. | [optional] 
**scope** | **List[str]** | Permission scopes associated with the token, if any. | [optional] 

## Example

```python
from verbatim_client.models.access_token_create_response import AccessTokenCreateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AccessTokenCreateResponse from a JSON string
access_token_create_response_instance = AccessTokenCreateResponse.from_json(json)
# print the JSON string representation of the object
print(AccessTokenCreateResponse.to_json())

# convert the object into a dict
access_token_create_response_dict = access_token_create_response_instance.to_dict()
# create an instance of AccessTokenCreateResponse from a dict
access_token_create_response_from_dict = AccessTokenCreateResponse.from_dict(access_token_create_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


