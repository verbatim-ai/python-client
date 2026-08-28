# CorpusItemResponse

Single corpus wrapped with its parent organization id.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**org_id** | **str** |  | [optional] 
**item** | [**Corpus**](Corpus.md) | The corpus payload. | [optional] 

## Example

```python
from verbatim_client.models.corpus_item_response import CorpusItemResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CorpusItemResponse from a JSON string
corpus_item_response_instance = CorpusItemResponse.from_json(json)
# print the JSON string representation of the object
print(CorpusItemResponse.to_json())

# convert the object into a dict
corpus_item_response_dict = corpus_item_response_instance.to_dict()
# create an instance of CorpusItemResponse from a dict
corpus_item_response_from_dict = CorpusItemResponse.from_dict(corpus_item_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


