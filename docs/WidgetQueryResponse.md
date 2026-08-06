# WidgetQueryResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamp** | **datetime** | Timestamp when the answer was generated | [optional] 
**session_id** | **UUID** | Id of the session the query belongs to | [optional] 
**query** | **str** | The user query that was submitted | [optional] 
**body** | **str** | The AI-generated answer, may include markdown and source citations | [optional] 
**attachment** | **int** | Number of source document chunks cited in the answer | [optional] 

## Example

```python
from verbatim_client.models.widget_query_response import WidgetQueryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WidgetQueryResponse from a JSON string
widget_query_response_instance = WidgetQueryResponse.from_json(json)
# print the JSON string representation of the object
print(WidgetQueryResponse.to_json())

# convert the object into a dict
widget_query_response_dict = widget_query_response_instance.to_dict()
# create an instance of WidgetQueryResponse from a dict
widget_query_response_from_dict = WidgetQueryResponse.from_dict(widget_query_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


