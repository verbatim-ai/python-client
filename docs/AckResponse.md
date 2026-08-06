# AckResponse

Acknowledgement response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamp** | **datetime** | Creation timestamp (ISO-8601, UTC). | 
**message** | **str** | Message content. | 

## Example

```python
from verbatim_client.models.ack_response import AckResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AckResponse from a JSON string
ack_response_instance = AckResponse.from_json(json)
# print the JSON string representation of the object
print(AckResponse.to_json())

# convert the object into a dict
ack_response_dict = ack_response_instance.to_dict()
# create an instance of AckResponse from a dict
ack_response_from_dict = AckResponse.from_dict(ack_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


