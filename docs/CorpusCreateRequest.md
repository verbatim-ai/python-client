# CorpusCreateRequest

Payload to create a new corpus inside an organization.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Human-readable name of the corpus. | 
**description** | **str** | Free-form description of the corpus. | 
**metadata** | **Dict[str, Optional[object]]** | Arbitrary JSON metadata attached to the corpus. Stored as JSONB. | [optional] 

## Example

```python
from verbatim_client.models.corpus_create_request import CorpusCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CorpusCreateRequest from a JSON string
corpus_create_request_instance = CorpusCreateRequest.from_json(json)
# print the JSON string representation of the object
print(CorpusCreateRequest.to_json())

# convert the object into a dict
corpus_create_request_dict = corpus_create_request_instance.to_dict()
# create an instance of CorpusCreateRequest from a dict
corpus_create_request_from_dict = CorpusCreateRequest.from_dict(corpus_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


