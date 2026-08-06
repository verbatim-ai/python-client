# CorpusCreateResponse

Acknowledgement returned after creating a corpus.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID of the newly created corpus (UUIDv4). | 
**created_at** | **datetime** | Creation timestamp (ISO-8601, UTC). | 
**name** | **str** | Name of the corpus. | 
**description** | **str** | Description of the corpus. | [optional] 
**metadata** | **Dict[str, Optional[object]]** | JSON metadata attached to the corpus. | [optional] 

## Example

```python
from verbatim_client.models.corpus_create_response import CorpusCreateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CorpusCreateResponse from a JSON string
corpus_create_response_instance = CorpusCreateResponse.from_json(json)
# print the JSON string representation of the object
print(CorpusCreateResponse.to_json())

# convert the object into a dict
corpus_create_response_dict = corpus_create_response_instance.to_dict()
# create an instance of CorpusCreateResponse from a dict
corpus_create_response_from_dict = CorpusCreateResponse.from_dict(corpus_create_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


