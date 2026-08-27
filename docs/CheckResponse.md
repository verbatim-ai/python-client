# CheckResponse

Aggregated health of the platform subsystems.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | &#x60;UP&#x60; when every probe succeeded, &#x60;DOWN&#x60; as soon as one failed. Mirrors the HTTP status: &#x60;UP&#x60; is returned with 200, &#x60;DOWN&#x60; with 500. | [optional] 
**message** | **str** | Reason of the failure, prefixed by the subsystem it comes from. Absent when every probe succeeded. | [optional] 
**checks** | [**List[CheckItem]**](CheckItem.md) | One entry per subsystem, whatever the outcome. | [optional] 

## Example

```python
from verbatim_client.models.check_response import CheckResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CheckResponse from a JSON string
check_response_instance = CheckResponse.from_json(json)
# print the JSON string representation of the object
print(CheckResponse.to_json())

# convert the object into a dict
check_response_dict = check_response_instance.to_dict()
# create an instance of CheckResponse from a dict
check_response_from_dict = CheckResponse.from_dict(check_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


