# Usage

Aggregated usage metrics over a timeframe, with a per-bucket time series. Returned by `GET /v1/usage/all` (organization scope), `GET /v1/usage/user/{userId}` (user scope) and `GET /v1/usage/corpus/{corpusId}` (corpus scope).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timeframe** | **str** | Bucket size the metrics are aggregated by. &#x60;Day&#x60; yields 30 buckets, &#x60;Week&#x60; 12, &#x60;Month&#x60; 12 and &#x60;Year&#x60; 5. | 
**var_from** | **datetime** | Inclusive start of the range (ISO-8601, UTC). Start of the oldest bucket, aligned to a calendar boundary. | 
**to** | **datetime** | Exclusive end of the range (ISO-8601, UTC). End of the newest **completed** bucket, i.e. the instant the bucket in progress starts at — never in the future, and always earlier than &#x60;timestamp&#x60;. | 
**organization_id** | **str** | ID of the organization the caller belongs to (UUIDv4). | 
**corpus_id** | **str** | ID of the queried corpus (UUIDv4). &#x60;null&#x60; at organization and user scopes. | [optional] 
**user_id** | **str** | ID of the queried user, as carried by the JWT or supplied at upload. &#x60;null&#x60; at organization and corpus scopes. | [optional] 
**tokens** | [**UsageTokens**](UsageTokens.md) | Token usage. At organization and user scope, sum of &#x60;post.token&#x60; + &#x60;document.token&#x60;. At corpus scope, sum of &#x60;post.token&#x60; only (vectorization tokens are billed at organization level). | 
**corpora** | [**UsageCount**](UsageCount.md) | Corpus counts. Populated at organization scope only; &#x60;null&#x60; at corpus and user scopes. | 
**sessions** | [**UsageCount**](UsageCount.md) | Session counts within the scope. | 
**threads** | [**UsageCount**](UsageCount.md) | Thread counts within the scope. | 
**posts** | [**UsageCount**](UsageCount.md) | Post counts within the scope. | 
**storage** | [**UsageCount**](UsageCount.md) | Storage footprint of documents within the scope. &#x60;total&#x60;/&#x60;created&#x60;/&#x60;removed&#x60; are **bytes**, not item counts. | 
**series** | [**List[UsageBucket]**](UsageBucket.md) | Per-bucket breakdown over &#x60;[from, to)&#x60;, oldest first — 30 daily, 12 weekly, 12 monthly or 5 yearly entries depending on &#x60;timeframe&#x60;. Contiguous and gapless: a bucket with no activity is present with zeros, and the last entry is the newest **completed** bucket — the one in progress is not reported. The buckets sum to the top-level &#x60;created&#x60;/&#x60;removed&#x60;/&#x60;inPeriod&#x60;. | 
**timestamp** | **datetime** | Server-side timestamp the metrics were computed at (ISO-8601, UTC). Falls inside the bucket in progress, which the report excludes — so it is later than &#x60;to&#x60;. | 

## Example

```python
from verbatim_client.models.usage import Usage

# TODO update the JSON string below
json = "{}"
# create an instance of Usage from a JSON string
usage_instance = Usage.from_json(json)
# print the JSON string representation of the object
print(Usage.to_json())

# convert the object into a dict
usage_dict = usage_instance.to_dict()
# create an instance of Usage from a dict
usage_from_dict = Usage.from_dict(usage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


