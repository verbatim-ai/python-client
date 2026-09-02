# Corpus

Knowledge base inside an organization: the container documents are ingested into and the scope a query is answered from.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Unique identifier of the corpus (UUIDv4). | 
**created_at** | **datetime** | Creation timestamp (ISO-8601, UTC). | 
**updated_at** | **datetime** | Last update timestamp (ISO-8601, UTC). | 
**name** | **str** | Human-readable name of the corpus. | 
**description** | **str** | Free-form description of the corpus. | 
**metadata** | **Dict[str, Optional[object]]** | Arbitrary JSON metadata attached to the corpus. Stored as JSONB. | [optional] 

## Example

```python
from verbatim_client.models.corpus import Corpus

# TODO update the JSON string below
json = "{}"
# create an instance of Corpus from a JSON string
corpus_instance = Corpus.from_json(json)
# print the JSON string representation of the object
print(Corpus.to_json())

# convert the object into a dict
corpus_dict = corpus_instance.to_dict()
# create an instance of Corpus from a dict
corpus_from_dict = Corpus.from_dict(corpus_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


