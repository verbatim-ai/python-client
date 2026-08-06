# WidgetPost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Unique identifier of the post | [optional] 
**text** | **str** | Message text; AI answers may contain markdown and a Sources section | [optional] 
**owner** | **str** | Who sent this message: USER for end-user queries, SYSTEM for AI-generated answers | [optional] 
**lang** | **str** | ISO language code used when generating the answer | [optional] 
**sent_at** | **datetime** | Timestamp when the message was created | [optional] 
**attachment** | **int** | Number of source document chunks cited in this answer (0 for user messages) | [optional] 

## Example

```python
from verbatim_client.models.widget_post import WidgetPost

# TODO update the JSON string below
json = "{}"
# create an instance of WidgetPost from a JSON string
widget_post_instance = WidgetPost.from_json(json)
# print the JSON string representation of the object
print(WidgetPost.to_json())

# convert the object into a dict
widget_post_dict = widget_post_instance.to_dict()
# create an instance of WidgetPost from a dict
widget_post_from_dict = WidgetPost.from_dict(widget_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


