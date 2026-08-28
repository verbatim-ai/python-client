# Post

Single user query or system answer inside a session.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Unique identifier of the post (UUIDv4). | 
**session_id** | **UUID** | ID of the session this post belongs to. | 
**agent_id** | **UUID** | Agent this answer was produced under | 
**body** | **str** | Text content of the post — the user query when &#x60;owner &#x3D; USER&#x60;, the LLM answer when &#x60;owner &#x3D; SYSTEM&#x60;. | 
**owner** | **str** | Who produced the post. | 
**token** | **int** | Token count of &#x60;body&#x60;, as measured by the model. | [optional] 
**lang** | **str** | ISO-639 language code used for the post. | [optional] 
**metadata** | **Dict[str, Optional[object]]** | Arbitrary JSON metadata attached to the post. Stored as JSONB. | [optional] 
**created_at** | **datetime** | Creation timestamp of the post (ISO-8601, UTC). | 
**attachment** | **int** | Number of attachment used in the post. Used /post/attachment to get details. Filled only when post have more than one attachment. Zero when no attachment. | [optional] 

## Example

```python
from verbatim_client.models.post import Post

# TODO update the JSON string below
json = "{}"
# create an instance of Post from a JSON string
post_instance = Post.from_json(json)
# print the JSON string representation of the object
print(Post.to_json())

# convert the object into a dict
post_dict = post_instance.to_dict()
# create an instance of Post from a dict
post_from_dict = Post.from_dict(post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


