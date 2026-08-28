# PostItemResponse

Pair of posts produced by a query: the user message and the corresponding system answer.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**session_id** | **UUID** | ID of the session the posts belong to (UUIDv4). | 
**query** | [**Post**](Post.md) | User post (the query). &#x60;owner &#x3D; USER&#x60;. | [optional] 
**answer** | [**Post**](Post.md) | System post (the LLM answer). &#x60;owner &#x3D; SYSTEM&#x60;, with attachments pointing to the chunks used as context. | [optional] 

## Example

```python
from verbatim_client.models.post_item_response import PostItemResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PostItemResponse from a JSON string
post_item_response_instance = PostItemResponse.from_json(json)
# print the JSON string representation of the object
print(PostItemResponse.to_json())

# convert the object into a dict
post_item_response_dict = post_item_response_instance.to_dict()
# create an instance of PostItemResponse from a dict
post_item_response_from_dict = PostItemResponse.from_dict(post_item_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


