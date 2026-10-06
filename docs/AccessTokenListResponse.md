# AccessTokenListResponse

Paginated list of the access tokens of the caller's organization.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page_index** | **int** | Zero-based index of the returned page. | [optional] 
**items** | [**List[AccessTokenItem]**](AccessTokenItem.md) | Access tokens contained in this page, newest first, expired ones included. | [optional] 

## Example

```python
from verbatim_client.models.access_token_list_response import AccessTokenListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AccessTokenListResponse from a JSON string
access_token_list_response_instance = AccessTokenListResponse.from_json(json)
# print the JSON string representation of the object
print(AccessTokenListResponse.to_json())

# convert the object into a dict
access_token_list_response_dict = access_token_list_response_instance.to_dict()
# create an instance of AccessTokenListResponse from a dict
access_token_list_response_from_dict = AccessTokenListResponse.from_dict(access_token_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


