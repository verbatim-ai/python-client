"""Hand-written smoke tests for the generated client.

The `test/` directory holds generator stubs with empty bodies — they assert
nothing. These tests exercise the parts of the client that the spec-to-code
pipeline actually gets wrong: camelCase aliasing, optional-field defaults, enum
validation and operation signatures. Several of them are regression guards for
springdoc emitting `"default": ""` and `additionalProperties` into the spec
(see openapi/client/sanitize-spec.py in the genai-server repo).
"""

import inspect
from datetime import datetime, timezone

import pytest
from pydantic import ValidationError

from verbatim_client.api.auth_api import AuthApi
from verbatim_client.api.corpus_api import CorpusApi
from verbatim_client.models.access_token_create_request import AccessTokenCreateRequest
from verbatim_client.models.access_token_create_response import AccessTokenCreateResponse
from verbatim_client.models.corpus_create_request import CorpusCreateRequest
from verbatim_client.models.corpus_list_response import CorpusListResponse
from verbatim_client.models.document import Document
from verbatim_client.models.document_status import DocumentStatus
from verbatim_client.models.document_update_request import DocumentUpdateRequest


def test_unset_optionals_are_omitted_from_payload():
    """Optional fields left unset must not appear in the request body.

    They previously defaulted to `""` and were serialized, so a partial update
    would blank out fields server-side.
    """
    assert DocumentUpdateRequest().to_dict() == {}
    assert AccessTokenCreateRequest().ttl is None

    partial = DocumentUpdateRequest(filename="report.pdf")
    assert partial.to_dict() == {"filename": "report.pdf"}


def test_camel_case_aliases_round_trip():
    """Wire format is camelCase; the Python attributes are snake_case."""
    doc = Document.from_json(
        """
        {
          "id": "550e8400-e29b-41d4-a716-446655440000",
          "corpusId": "550e8400-e29b-41d4-a716-446655440001",
          "filename": "annual-report-2025.pdf",
          "contentType": "application/pdf",
          "status": "READY",
          "createdAt": "2026-04-23T04:06:51Z",
          "updatedAt": "2026-04-23T04:06:51Z",
          "nbWords": 1200
        }
        """
    )

    assert doc.corpus_id == "550e8400-e29b-41d4-a716-446655440001"
    assert doc.nb_words == 1200
    assert doc.created_at == datetime(2026, 4, 23, 4, 6, 51, tzinfo=timezone.utc)
    assert doc.size is None

    payload = doc.to_dict()
    assert payload["nbWords"] == 1200
    assert payload["corpusId"] == doc.corpus_id
    assert "nb_words" not in payload


def test_required_fields_are_enforced():
    with pytest.raises(ValidationError):
        CorpusCreateRequest(name="Support knowledge base")  # description missing


def test_constraints_are_enforced():
    with pytest.raises(ValidationError):
        AccessTokenCreateRequest(ttl=0)  # minimum is 1

    assert AccessTokenCreateRequest(ttl=3600).ttl == 3600


def test_status_enum_is_validated():
    assert DocumentStatus(status="PROCESSING").status == "PROCESSING"

    with pytest.raises(ValidationError):
        DocumentStatus(status="NOT_A_STATUS")


def test_free_form_metadata_stays_a_dict():
    """`metadata` is a genuine JSONB map and must survive a round trip."""
    metadata = {"owner": "support-team", "language": "fr", "tags": ["a", "b"]}
    request = CorpusCreateRequest(name="KB", description="d", metadata=metadata)

    assert CorpusCreateRequest.from_json(request.to_json()).metadata == metadata


def test_nested_list_response_deserializes():
    response = CorpusListResponse.from_json(
        """
        {
          "orgId": "550e8400-e29b-41d4-a716-446655440000",
          "pageIndex": 0,
          "items": [
            {
              "id": "550e8400-e29b-41d4-a716-446655440002",
              "createdAt": "2026-04-23T04:06:51Z",
              "updatedAt": "2026-04-23T04:06:51Z",
              "name": "Support knowledge base",
              "description": "Tickets and runbooks"
            }
          ]
        }
        """
    )

    assert response.org_id == "550e8400-e29b-41d4-a716-446655440000"
    assert response.page_index == 0
    assert len(response.items) == 1
    assert response.items[0].name == "Support knowledge base"


@pytest.mark.parametrize(
    "api, method, param, expected_type, expected_return",
    [
        (
            AuthApi,
            "create2",
            "access_token_create_request",
            AccessTokenCreateRequest,
            AccessTokenCreateResponse,
        ),
        (
            CorpusApi,
            "create1",
            "corpus_create_request",
            CorpusCreateRequest,
            None,
        ),
    ],
)
def test_operations_are_typed_with_models(api, method, param, expected_type, expected_return):
    """Bodies and responses must be typed models, not free-form dicts.

    A stray `additionalProperties` in the spec made these `Dict[str, Any]` and
    produced unresolvable `Model[str, object]` return annotations.
    """
    signature = inspect.signature(getattr(api, method))

    assert signature.parameters[param].annotation is expected_type
    if expected_return is not None:
        assert signature.return_annotation is expected_return


def test_package_exports_every_api():
    import verbatim_client

    for name in ("AuthApi", "CorpusApi", "DocumentApi", "SessionApi", "PostApi"):
        assert hasattr(verbatim_client, name), f"{name} missing from package exports"
