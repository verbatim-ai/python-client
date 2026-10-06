# AccessTokenScopeDomain


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Domain name, the &#x60;DOMAIN&#x60; part of a scope entry. | [optional] 
**path** | **str** | Base path of the API the domain covers. | [optional] 
**description** | **str** | What the domain gives access to. | [optional] 
**scopes** | **List[str]** | The scope entries of this domain, one per action. | [optional] 

## Example

```python
from verbatim_client.models.access_token_scope_domain import AccessTokenScopeDomain

# TODO update the JSON string below
json = "{}"
# create an instance of AccessTokenScopeDomain from a JSON string
access_token_scope_domain_instance = AccessTokenScopeDomain.from_json(json)
# print the JSON string representation of the object
print(AccessTokenScopeDomain.to_json())

# convert the object into a dict
access_token_scope_domain_dict = access_token_scope_domain_instance.to_dict()
# create an instance of AccessTokenScopeDomain from a dict
access_token_scope_domain_from_dict = AccessTokenScopeDomain.from_dict(access_token_scope_domain_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


