# AccessTokenScopesResponse

Every scope an access token can be created with. A scope entry is `DOMAIN:ACTION`; any domain combines with any action.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domains** | [**List[AccessTokenScopeDomain]**](AccessTokenScopeDomain.md) | Domains a scope entry may name, each with the scopes it makes up. | [optional] 
**actions** | [**List[AccessTokenScopeAction]**](AccessTokenScopeAction.md) | Actions a scope entry may ask for, each with the HTTP methods it opens. | [optional] 
**scopes** | **List[str]** | Every valid scope entry, as accepted in the &#x60;scope&#x60; of &#x60;POST /v1/auth/access-token/&#x60;. | [optional] 

## Example

```python
from verbatim_client.models.access_token_scopes_response import AccessTokenScopesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AccessTokenScopesResponse from a JSON string
access_token_scopes_response_instance = AccessTokenScopesResponse.from_json(json)
# print the JSON string representation of the object
print(AccessTokenScopesResponse.to_json())

# convert the object into a dict
access_token_scopes_response_dict = access_token_scopes_response_instance.to_dict()
# create an instance of AccessTokenScopesResponse from a dict
access_token_scopes_response_from_dict = AccessTokenScopesResponse.from_dict(access_token_scopes_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


