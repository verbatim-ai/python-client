# DocumentConvertResponse

A document converted to Markdown by `POST /v1/doc/convert`. Nothing is stored: this payload is the whole result. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content_type** | **str** | Format the document was recognised as, detected from its content (and the extension of &#x60;filename&#x60;, when sent). | 
**filename** | **str** | The &#x60;filename&#x60; sent, echoed back. Absent when none was sent. | [optional] 
**size** | **int** | Size of the converted document, in bytes. | 
**pages** | **int** | Number of pages, for formats that have pages (PDF, Word, PowerPoint, …). Absent otherwise. | [optional] 
**markdown** | **str** | The document as Markdown. Tables are pipe tables, a spreadsheet gives one section per sheet. Images are not described — a scanned PDF yields no text. | 
**warnings** | **List[str]** | Problems the converter recovered from — an embedded file it could not read, a damaged part it skipped — and a note when no text could be extracted at all. Empty when the conversion was clean. | [optional] 

## Example

```python
from verbatim_client.models.document_convert_response import DocumentConvertResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentConvertResponse from a JSON string
document_convert_response_instance = DocumentConvertResponse.from_json(json)
# print the JSON string representation of the object
print(DocumentConvertResponse.to_json())

# convert the object into a dict
document_convert_response_dict = document_convert_response_instance.to_dict()
# create an instance of DocumentConvertResponse from a dict
document_convert_response_from_dict = DocumentConvertResponse.from_dict(document_convert_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


