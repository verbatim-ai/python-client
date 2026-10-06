# AccessTokenItem

One access token as a listing shows it: every stored attribute, except that the token value is cut down to its first characters. The full value is only ever returned once, by the create call.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Id of the token. Pass it to &#x60;DELETE /v1/auth/access-token/id/{id}&#x60; to revoke the token. | [optional] 
**token** | **str** | First characters of the token value followed by &#x60;...&#x60; — enough to recognise a token, never enough to use it. | [optional] 
**org_id** | **UUID** | Organization the token belongs to. | [optional] 
**created_at** | **datetime** | Creation timestamp (ISO-8601, UTC). | [optional] 
**expires_at** | **datetime** | Expiry timestamp (ISO-8601, UTC). An expired token stays listed until revoked, but no longer authenticates. | [optional] 
**issuer** | **str** | Label of the system that requested the token, as given at creation. | [optional] 
**email** | **str** | Email of the end-user the token was issued for, as given at creation. | [optional] 
**user_id** | **str** | User identifier the token was issued for, as given at creation. | [optional] 
**scope** | **List[str]** | Permission scopes the token carries. | [optional] 

## Example

```python
from verbatim_client.models.access_token_item import AccessTokenItem

# TODO update the JSON string below
json = "{}"
# create an instance of AccessTokenItem from a JSON string
access_token_item_instance = AccessTokenItem.from_json(json)
# print the JSON string representation of the object
print(AccessTokenItem.to_json())

# convert the object into a dict
access_token_item_dict = access_token_item_instance.to_dict()
# create an instance of AccessTokenItem from a dict
access_token_item_from_dict = AccessTokenItem.from_dict(access_token_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


