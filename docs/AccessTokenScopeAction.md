# AccessTokenScopeAction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Action name, the &#x60;ACTION&#x60; part of a scope entry. | [optional] 
**methods** | **List[str]** | HTTP methods the action opens on the domain&#39;s API. | [optional] 

## Example

```python
from verbatim_client.models.access_token_scope_action import AccessTokenScopeAction

# TODO update the JSON string below
json = "{}"
# create an instance of AccessTokenScopeAction from a JSON string
access_token_scope_action_instance = AccessTokenScopeAction.from_json(json)
# print the JSON string representation of the object
print(AccessTokenScopeAction.to_json())

# convert the object into a dict
access_token_scope_action_dict = access_token_scope_action_instance.to_dict()
# create an instance of AccessTokenScopeAction from a dict
access_token_scope_action_from_dict = AccessTokenScopeAction.from_dict(access_token_scope_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


