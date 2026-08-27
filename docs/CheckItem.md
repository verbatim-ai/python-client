# CheckItem

Outcome of one subsystem probe.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Subsystem probed. | [optional] 
**status** | **str** | &#x60;UP&#x60; when the subsystem answered the probe, &#x60;DOWN&#x60; otherwise. | [optional] 
**duration_ms** | **int** | Wall-clock duration of the probe, in milliseconds. | [optional] 
**error** | **str** | Failure reason. Absent when the probe succeeded. | [optional] 

## Example

```python
from verbatim_client.models.check_item import CheckItem

# TODO update the JSON string below
json = "{}"
# create an instance of CheckItem from a JSON string
check_item_instance = CheckItem.from_json(json)
# print the JSON string representation of the object
print(CheckItem.to_json())

# convert the object into a dict
check_item_dict = check_item_instance.to_dict()
# create an instance of CheckItem from a dict
check_item_from_dict = CheckItem.from_dict(check_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


