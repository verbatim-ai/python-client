# UsageCount

Lifetime count and per-window create/remove deltas. For `storage`, the values are bytes rather than item counts.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** | Lifetime count, all-time. Includes soft-deleted items. | 
**created** | **int** | Items whose &#x60;created_at&#x60; falls inside the rolling window &#x60;[from, to)&#x60;. | 
**removed** | **int** | Items whose &#x60;deleted_at&#x60; falls inside the rolling window &#x60;[from, to)&#x60; (soft-deletes only — a hard delete leaves no trace). | 

## Example

```python
from verbatim_client.models.usage_count import UsageCount

# TODO update the JSON string below
json = "{}"
# create an instance of UsageCount from a JSON string
usage_count_instance = UsageCount.from_json(json)
# print the JSON string representation of the object
print(UsageCount.to_json())

# convert the object into a dict
usage_count_dict = usage_count_instance.to_dict()
# create an instance of UsageCount from a dict
usage_count_from_dict = UsageCount.from_dict(usage_count_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


