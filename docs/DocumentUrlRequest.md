# DocumentUrlRequest

Body of POST /v1/doc/url. Names a web page to print to PDF and ingest into a corpus.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**corpus_id** | **UUID** | ID of the corpus the document will be ingested into. | 
**url** | **str** | Absolute &#x60;https&#x60; URL of an HTML page, at most 2048 characters. It may not carry credentials (&#x60;user:password@&#x60;) — send those in &#x60;headers&#x60;. Stored in the document&#39;s &#x60;metadata.url&#x60;. | 
**scale** | **float** | Rendering scale of the page, from &#x60;0.1&#x60; to &#x60;2&#x60;. Below 1 fits more of the page on each PDF page. Defaults to &#x60;1&#x60;. | [optional] 
**headers** | **Dict[str, str]** | HTTP headers sent when loading the page — typically &#x60;Authorization&#x60; or &#x60;Cookie&#x60; for a page behind a login. Sent only to the page&#39;s own origin (scheme, host and port of &#x60;url&#x60;), never to the third-party assets it loads; never stored. At most 20. | [optional] 

## Example

```python
from verbatim_client.models.document_url_request import DocumentUrlRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentUrlRequest from a JSON string
document_url_request_instance = DocumentUrlRequest.from_json(json)
# print the JSON string representation of the object
print(DocumentUrlRequest.to_json())

# convert the object into a dict
document_url_request_dict = document_url_request_instance.to_dict()
# create an instance of DocumentUrlRequest from a dict
document_url_request_from_dict = DocumentUrlRequest.from_dict(document_url_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


