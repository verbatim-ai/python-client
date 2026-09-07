# Thread

Conversation thread bound to a user and to one or more corpora.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Unique identifier of the thread (UUIDv4). | 
**user_id** | **str** | Identifier of the user who opened the thread, as carried by the JWT. Stored as a free-form string so non-UUID identity providers are supported. | [optional] 
**corpus_ids** | **List[UUID]** | IDs of the corpora the thread is bound to (UUIDv4). | 
**metadata** | **Dict[str, Optional[object]]** | Arbitrary JSON metadata attached to the thread. | [optional] 
**created_at** | **datetime** | Creation timestamp of the thread (ISO-8601, UTC). | 
**updated_at** | **datetime** | Last modification of the thread (ISO-8601, UTC) — moved by &#x60;PATCH /v1/thread/{sessionId}&#x60;. Equal to &#x60;createdAt&#x60; on a thread nobody has patched. | 
**model** | **str** |  | [optional] 

## Example

```python
from verbatim_client.models.thread import Thread

# TODO update the JSON string below
json = "{}"
# create an instance of Thread from a JSON string
thread_instance = Thread.from_json(json)
# print the JSON string representation of the object
print(Thread.to_json())

# convert the object into a dict
thread_dict = thread_instance.to_dict()
# create an instance of Thread from a dict
thread_from_dict = Thread.from_dict(thread_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


