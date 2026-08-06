# SessionCreateRequest

Payload to open a new conversation session. The model, system prompt, temperature and thinking flag are locked at creation time and apply to every post in the session.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**corpus_ids** | **List[UUID]** | IDs of the corpora the session is bound to (UUIDv4). A session may search across several corpora. | 
**model** | **str** | Name of the LLM used to answer queries in this session. Must be installed on the Ollama runtime. | 
**system** | **str** | System prompt sent to the LLM as the first message. Falls back to a default RAG prompt when omitted. | [optional] 
**temperature** | **float** | Sampling temperature. Range and meaning depend on the model — refer to the model&#39;s documentation. | [optional] 
**thinking** | **bool** | Enable the model&#39;s *thinking* mode. Only honored by models that support it. | [optional] 
**metadata** | **Dict[str, Optional[object]]** | Arbitrary JSON metadata attached to the session. Stored as JSONB. | [optional] 

## Example

```python
from verbatim_client.models.session_create_request import SessionCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SessionCreateRequest from a JSON string
session_create_request_instance = SessionCreateRequest.from_json(json)
# print the JSON string representation of the object
print(SessionCreateRequest.to_json())

# convert the object into a dict
session_create_request_dict = session_create_request_instance.to_dict()
# create an instance of SessionCreateRequest from a dict
session_create_request_from_dict = SessionCreateRequest.from_dict(session_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


