# UsageDelta

Per-bucket create/remove deltas. For `storage`, the values are bytes rather than item counts.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **int** | Items whose &#x60;created_at&#x60; falls inside this bucket. | 
**removed** | **int** | Items whose &#x60;deleted_at&#x60; falls inside this bucket (soft-deletes only — a hard delete leaves no trace). | 

## Example

```python
from verbatim_client.models.usage_delta import UsageDelta

# TODO update the JSON string below
json = "{}"
# create an instance of UsageDelta from a JSON string
usage_delta_instance = UsageDelta.from_json(json)
# print the JSON string representation of the object
print(UsageDelta.to_json())

# convert the object into a dict
usage_delta_dict = usage_delta_instance.to_dict()
# create an instance of UsageDelta from a dict
usage_delta_from_dict = UsageDelta.from_dict(usage_delta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


