# ModelListResponse

LLM models supported by the platform, everything a client needs to let someone choose one.  Not paginated — the catalog is a handful of entries and `models` always holds all of them, in the order the platform means them to be offered. `total` is their number, so a client can size a picker without walking the list.  `items` is the same list reduced to its identifiers, kept for clients written against the first version of this endpoint. It is deprecated and derived from `models`, so the two can never disagree: read `models[].id` instead. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** | Number of models in &#x60;models&#x60;. | 
**models** | [**List[Model]**](Model.md) | Supported models, in the order they are meant to be offered. The first is the one to preselect. | [optional] 
**items** | **List[str]** | **Deprecated** — identifiers of the supported models, without the display fields. Superseded by &#x60;models[].id&#x60;, which carries the same values in the same order. Still served for existing clients; it will be removed in a future release. | [optional] 

## Example

```python
from verbatim_client.models.model_list_response import ModelListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ModelListResponse from a JSON string
model_list_response_instance = ModelListResponse.from_json(json)
# print the JSON string representation of the object
print(ModelListResponse.to_json())

# convert the object into a dict
model_list_response_dict = model_list_response_instance.to_dict()
# create an instance of ModelListResponse from a dict
model_list_response_from_dict = ModelListResponse.from_dict(model_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


