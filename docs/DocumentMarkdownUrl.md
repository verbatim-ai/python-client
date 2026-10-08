# DocumentMarkdownUrl

Presigned URL granting direct client GET access to the Markdown conversion of a document. The content is served by the storage backend (S3), not by this server.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | Presigned URL to GET the Markdown conversion (&#x60;text/markdown&#x60;, UTF-8). Time-limited: anyone holding it can read the file until &#x60;expiresAt&#x60;, without a token. | 
**timestamp** | **datetime** | When &#x60;url&#x60; was issued (ISO-8601, UTC). | 
**expires_at** | **datetime** | Wall-clock expiration of &#x60;url&#x60; (ISO-8601, UTC). After this, a fresh request is required. | 

## Example

```python
from verbatim_client.models.document_markdown_url import DocumentMarkdownUrl

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentMarkdownUrl from a JSON string
document_markdown_url_instance = DocumentMarkdownUrl.from_json(json)
# print the JSON string representation of the object
print(DocumentMarkdownUrl.to_json())

# convert the object into a dict
document_markdown_url_dict = document_markdown_url_instance.to_dict()
# create an instance of DocumentMarkdownUrl from a dict
document_markdown_url_from_dict = DocumentMarkdownUrl.from_dict(document_markdown_url_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


