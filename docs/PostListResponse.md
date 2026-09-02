# PostListResponse

Paginated list of posts in a session.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**session_id** | **UUID** | ID of the session (UUIDv4). | 
**page_index** | **int** | Zero-based index of the returned page. | 
**page_size** | **int** | Number of items requested per page. The last page may carry fewer. | 
**total** | **int** | Total number of posts in the session, across every page. Divide by &#x60;pageSize&#x60; to know how many pages to walk. Soft-deleted posts are not counted. | 
**order** | **str** | Ordering this page was built under — the &#x60;order&#x60; that was asked for, or &#x60;DESC&#x60; when it was omitted. | 
**items** | [**List[Post]**](Post.md) | Posts contained in this page, in the requested order — newest first unless &#x60;order&#x3D;ASC&#x60; was passed. | [optional] 

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


