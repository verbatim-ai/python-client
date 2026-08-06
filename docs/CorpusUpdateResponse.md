# CorpusUpdateResponse

Acknowledgement returned after updating a corpus.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID of the corpus (UUIDv4). | 
**created_at** | **datetime** | Original creation timestamp (ISO-8601, UTC). | 
**updated_at** | **datetime** | Timestamp of this update (ISO-8601, UTC). | 
**name** | **str** | Name of the corpus. | 
**description** | **str** | Description of the corpus. | 

## Example

```python
from verbatim_client.models.corpus_update_response import CorpusUpdateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CorpusUpdateResponse from a JSON string
corpus_update_response_instance = CorpusUpdateResponse.from_json(json)
# print the JSON string representation of the object
print(CorpusUpdateResponse.to_json())

# convert the object into a dict
corpus_update_response_dict = corpus_update_response_instance.to_dict()
# create an instance of CorpusUpdateResponse from a dict
corpus_update_response_from_dict = CorpusUpdateResponse.from_dict(corpus_update_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


