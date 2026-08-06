# UsageTokens

Token consumption — lifetime and during the rolling window. Soft-deleted posts and documents are still counted (the tokens were billed at production time).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** | Lifetime token count, all-time. Includes posts and documents that were since soft-deleted. | 
**in_period** | **int** | Tokens produced inside the rolling window — posts (and, at organization-scope, documents) whose &#x60;created_at&#x60; falls in &#x60;[from, to)&#x60;. | 

## Example

```python
from verbatim_client.models.usage_tokens import UsageTokens

# TODO update the JSON string below
json = "{}"
# create an instance of UsageTokens from a JSON string
usage_tokens_instance = UsageTokens.from_json(json)
# print the JSON string representation of the object
print(UsageTokens.to_json())

# convert the object into a dict
usage_tokens_dict = usage_tokens_instance.to_dict()
# create an instance of UsageTokens from a dict
usage_tokens_from_dict = UsageTokens.from_dict(usage_tokens_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


