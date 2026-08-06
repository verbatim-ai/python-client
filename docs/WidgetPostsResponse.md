# WidgetPostsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamp** | **datetime** | Timestamp when the answer was generated | [optional] 
**session_id** | **UUID** | Id of the session the query belongs to | [optional] 
**items** | [**List[WidgetPost]**](WidgetPost.md) | Chronological list of all posts in the session (user queries and AI answers interleaved) | [optional] 

## Example

```python
from verbatim_client.models.widget_posts_response import WidgetPostsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WidgetPostsResponse from a JSON string
widget_posts_response_instance = WidgetPostsResponse.from_json(json)
# print the JSON string representation of the object
print(WidgetPostsResponse.to_json())

# convert the object into a dict
widget_posts_response_dict = widget_posts_response_instance.to_dict()
# create an instance of WidgetPostsResponse from a dict
widget_posts_response_from_dict = WidgetPostsResponse.from_dict(widget_posts_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


