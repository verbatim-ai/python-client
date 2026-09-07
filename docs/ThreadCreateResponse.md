# ThreadCreateResponse

Acknowledgement returned after opening a new thread.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | ID of the newly created thread (UUIDv4). | 
**user_id** | **str** | Identifier of the user who opened the thread (echo of the JWT subject). | [optional] 
**corpus_id** | **List[UUID]** | IDs of the corpora the thread is bound to (UUIDv4). | 
**model** | **str** |  | [optional] 
**metadata** | **Dict[str, Optional[object]]** | Arbitrary JSON metadata attached to the thread. | [optional] 
**created_at** | **datetime** | Creation timestamp of the thread (ISO-8601, UTC). | 
**updated_at** | **datetime** | Last modification of the thread (ISO-8601, UTC). Equal to &#x60;createdAt&#x60; on a thread that has just been created. | 

## Example

```python
from verbatim_client.models.thread_create_response import ThreadCreateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ThreadCreateResponse from a JSON string
thread_create_response_instance = ThreadCreateResponse.from_json(json)
# print the JSON string representation of the object
print(ThreadCreateResponse.to_json())

# convert the object into a dict
thread_create_response_dict = thread_create_response_instance.to_dict()
# create an instance of ThreadCreateResponse from a dict
thread_create_response_from_dict = ThreadCreateResponse.from_dict(thread_create_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


