# ThreadUpdateRequest

Payload to patch a session. Only the fields you set are updated; omit a field to leave it unchanged.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | **Dict[str, Optional[object]]** | New JSON metadata. When provided, **replaces** the existing metadata map; omit to keep it unchanged. | [optional] 

## Example

```python
from verbatim_client.models.thread_update_request import ThreadUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ThreadUpdateRequest from a JSON string
thread_update_request_instance = ThreadUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(ThreadUpdateRequest.to_json())

# convert the object into a dict
thread_update_request_dict = thread_update_request_instance.to_dict()
# create an instance of ThreadUpdateRequest from a dict
thread_update_request_from_dict = ThreadUpdateRequest.from_dict(thread_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


