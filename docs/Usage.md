# Usage

Aggregated usage metrics over a rolling timeframe. Returned by `GET /v1/usage/all` (organization scope) and `GET /v1/usage/corpus/{corpusId}` (corpus scope).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timeframe** | **str** | Rolling window the metrics are aggregated over. | 
**var_from** | **datetime** | Inclusive start of the rolling window (ISO-8601, UTC). | 
**to** | **datetime** | Exclusive end of the rolling window (ISO-8601, UTC). Equal to &#x60;timestamp&#x60;. | 
**organization_id** | **str** | ID of the organization the caller belongs to (UUIDv4). | 
**corpus_id** | **str** | ID of the queried corpus (UUIDv4). &#x60;null&#x60; at organization and user scopes. | [optional] 
**user_id** | **str** | ID of the queried user, as carried by the JWT or supplied at upload. &#x60;null&#x60; at organization and corpus scopes. | [optional] 
**tokens** | [**UsageTokens**](UsageTokens.md) | Token usage. At organization scope, sum of &#x60;post.token&#x60; + &#x60;document.token&#x60;. At corpus scope, sum of &#x60;post.token&#x60; only (vectorization tokens are billed at organization level). | 
**corpora** | [**UsageCount**](UsageCount.md) | Corpus counts. Populated at organization scope only; &#x60;null&#x60; at corpus scope. | 
**sessions** | [**UsageCount**](UsageCount.md) | Session counts within the scope. | 
**posts** | [**UsageCount**](UsageCount.md) | Post counts within the scope. | 
**storage** | [**UsageCount**](UsageCount.md) | Storage footprint of documents within the scope. &#x60;total&#x60;/&#x60;created&#x60;/&#x60;removed&#x60; are **bytes**, not item counts. | 
**timestamp** | **datetime** | Server-side timestamp the metrics were computed at (ISO-8601, UTC). Equal to &#x60;to&#x60;. | 

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


