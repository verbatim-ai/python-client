# Error

Standard error payload returned for non-2xx responses.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamp** | **datetime** | Server-side timestamp the error was produced (ISO-8601, UTC). | [optional] 
**status** | **int** | HTTP status code returned to the client. | [optional] 
**error** | **str** | HTTP status reason phrase. | [optional] 
**message** | **str** | Human-readable error message — safe to surface to API consumers. | [optional] 
**path** | **str** | Servlet path of the request that produced the error. | [optional] 

## Example

```python
from verbatim_client.models.error import Error

# TODO update the JSON string below
json = "{}"
# create an instance of Error from a JSON string
error_instance = Error.from_json(json)
# print the JSON string representation of the object
print(Error.to_json())

# convert the object into a dict
error_dict = error_instance.to_dict()
# create an instance of Error from a dict
error_from_dict = Error.from_dict(error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


