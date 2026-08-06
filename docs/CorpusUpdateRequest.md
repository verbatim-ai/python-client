# CorpusUpdateRequest

Payload to patch a corpus. Only the fields you set are updated; omit a field to leave it unchanged. Changing the embedding or summary model does **not** re-process already-ingested documents.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | New name of the corpus. Omit to keep the current name. | [optional] 
**description** | **str** | New description of the corpus. Omit to keep the current description. | [optional] 
**metadata** | **Dict[str, Optional[object]]** | New JSON metadata. When provided, **replaces** the existing metadata map; omit to keep it unchanged. | [optional] 

## Example

```python
from verbatim_client.models.corpus_update_request import CorpusUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CorpusUpdateRequest from a JSON string
corpus_update_request_instance = CorpusUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(CorpusUpdateRequest.to_json())

# convert the object into a dict
corpus_update_request_dict = corpus_update_request_instance.to_dict()
# create an instance of CorpusUpdateRequest from a dict
corpus_update_request_from_dict = CorpusUpdateRequest.from_dict(corpus_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


