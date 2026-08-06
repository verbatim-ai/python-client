# DocumentStatus

Lightweight view of a document's ingestion lifecycle. Cheaper than fetching the full document, and intended for polling loops between commit and the final READY/FAILED status.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID of the document (UUIDv4). | [optional] 
**status** | **str** | Current lifecycle status of the document. | [optional] 
**status_msg** | **str** | Optional human-readable detail attached to the status — typically a failure reason when &#x60;status &#x3D;&#x3D; FAILED&#x60;. &#x60;null&#x60; otherwise. | [optional] 
**updated_at** | **datetime** | Wall-clock timestamp of the last status update (ISO-8601, UTC). | [optional] 

## Example

```python
from verbatim_client.models.document_status import DocumentStatus

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentStatus from a JSON string
document_status_instance = DocumentStatus.from_json(json)
# print the JSON string representation of the object
print(DocumentStatus.to_json())

# convert the object into a dict
document_status_dict = document_status_instance.to_dict()
# create an instance of DocumentStatus from a dict
document_status_from_dict = DocumentStatus.from_dict(document_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


