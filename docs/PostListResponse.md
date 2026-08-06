# PostListResponse

Paginated list of posts in a session.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**session_id** | **UUID** | ID of the session (UUIDv4). | 
**page_index** | **int** | Zero-based index of the returned page. | [optional] 
**items** | [**List[Post]**](Post.md) | Posts contained in this page, newest first. | [optional] 

## Example

```python
from verbatim_client.models.post_list_response import PostListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PostListResponse from a JSON string
post_list_response_instance = PostListResponse.from_json(json)
# print the JSON string representation of the object
print(PostListResponse.to_json())

# convert the object into a dict
post_list_response_dict = post_list_response_instance.to_dict()
# create an instance of PostListResponse from a dict
post_list_response_from_dict = PostListResponse.from_dict(post_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


