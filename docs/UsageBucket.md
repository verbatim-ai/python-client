# UsageBucket

Metrics for one calendar bucket of the series (UTC). Every bucket is complete; the one currently in progress is not reported.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_from** | **datetime** | Inclusive start of the bucket (ISO-8601, UTC). | 
**to** | **datetime** | Exclusive end of the bucket (ISO-8601, UTC). Equal to the &#x60;from&#x60; of the next bucket. | 
**tokens** | **int** | Tokens produced inside this bucket. At organization and user scope, posts **and** documents; at corpus scope, posts only. | 
**corpora** | [**UsageDelta**](UsageDelta.md) | Corpus deltas for this bucket. Populated at organization scope only; &#x60;null&#x60; at corpus and user scopes, as it is at the top level. | [optional] 
**sessions** | [**UsageDelta**](UsageDelta.md) | Session deltas for this bucket. | 
**posts** | [**UsageDelta**](UsageDelta.md) | Post deltas for this bucket. | 
**storage** | [**UsageDelta**](UsageDelta.md) | Storage deltas for this bucket, in **bytes** — not item counts. | 

## Example

```python
from verbatim_client.models.usage_bucket import UsageBucket

# TODO update the JSON string below
json = "{}"
# create an instance of UsageBucket from a JSON string
usage_bucket_instance = UsageBucket.from_json(json)
# print the JSON string representation of the object
print(UsageBucket.to_json())

# convert the object into a dict
usage_bucket_dict = usage_bucket_instance.to_dict()
# create an instance of UsageBucket from a dict
usage_bucket_from_dict = UsageBucket.from_dict(usage_bucket_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


