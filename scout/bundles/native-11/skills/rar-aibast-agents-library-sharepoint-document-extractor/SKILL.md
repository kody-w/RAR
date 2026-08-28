---
name: "rar-aibast-agents-library-sharepoint-document-extractor"
description: "Extracts and searches document links from live records in a simulated Dynamics 365 tenant, with metadata seams and offline fallback."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@aibast-agents-library/sharepoint_document_extractor", "rar_sha256": "fb734ed12acc2be467930af21e236788687c37f4ba4d1d9a08c10abe1ca7e418", "source_kind": "rar-agent", "source_commit": "bfb52cb1f078e974e5106ed916b5fde9869b395e", "version": "1.1.0", "author": "AIBAST", "tags": ["sharepoint", "documents", "url-extraction", "metadata", "search"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@aibast-agents-library/sharepoint_document_extractor`. The original RAPP
agent is preserved byte-for-byte in `extract_sharepoint_document_url_agent.py` and in the RCI capsule.

When Scout can execute local files, resolve this skill directory and run:

```bash
python3 scripts/run_agent.py --preflight
echo '{}' | python3 scripts/run_agent.py
```

Pass the real JSON arguments instead of `{}`. The runner verifies the linked
agent SHA-256 before importing it. If preflight reports a host dependency that
Scout cannot satisfy, use the `brainstem_chat` MCP tool to run the canonical
agent in the user's Brainstem. Never paraphrase the factory or agent into a new
implementation. The generic direct-file commands in the generated Toaster
section are recovery guidance; Scout should prefer the verified runner.

SharePoint Document Extractor Agent — a template you are meant to mutate.

Searches document libraries, extracts URLs, enriches metadata, and
validates document links for accessibility.

The live tenant has no SharePoint document library, so in this template
the URL-bearing fields of live Dynamics ACCOUNT records (websiteurl)
stand in for extractable document links — the search/extract seam runs
end-to-end against real records until you point it at a real
SharePoint/Graph endpoint. Say the same in your own mutation if you
reinterpret an entity.

HOW THIS TEMPLATE WORKS
  1. Out of the box it pulls live account records over real HTTP from
     the globally hosted Static Dynamics 365 tenant (Aster Lane Office
     Systems — synthetic data, no credentials, works from anywhere):
     https://kody-w.github.io/static-dynamics-365/api/data/v9.2/
     Try: perform(operation="url_extraction", search_query="granite")
     — extracts the real seeded link for Granite Peak Manufacturing
     from the live tenant.
  2. No network? Everything falls back to the embedded demo layer below
     (_DOCUMENT_LIBRARY) — the agent never crashes offline.
  3. Make it yours at the LIVE DATA SEAM below: set
     SHAREPOINT_DOCUMENT_EXTRACTOR_DATA_URL to any OData-shaped
     endpoint, or replace _fetch_collection() with a Microsoft Graph /
     SharePoint REST client. The fields the rest of the file needs are
     listed in _normalize_live_document() — file size, type, and
     permissions are labeled "n/a — enrichment seam"; wire your
     SharePoint metadata there.

OPERATIONS
  document_search | url_extraction | metadata_enrichment
  | link_validation
  kwargs: operation (required), search_query

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "operation": {
      "description": "The SharePoint operation to perform",
      "enum": [
        "document_search",
        "url_extraction",
        "metadata_enrichment",
        "link_validation"
      ],
      "type": "string"
    },
    "search_query": {
      "description": "Search query for documents",
      "type": "string"
    }
  },
  "required": [
    "operation"
  ],
  "type": "object"
}
```

<!-- toaster:generated:end -->

<!-- toaster:generated:begin -->

## Run this — do not improvise

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `extract_sharepoint_document_url_agent.py` and embedded as the fenced Python below (sha256 fb734ed12acc2be4…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `extract_sharepoint_document_url_agent.py` first:

```bash
python3 extract_sharepoint_document_url_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 extract_sharepoint_document_url_agent.py   # or on stdin
python3 extract_sharepoint_document_url_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
SharePoint Document Extractor Agent — a template you are meant to mutate.

Searches document libraries, extracts URLs, enriches metadata, and
validates document links for accessibility.

The live tenant has no SharePoint document library, so in this template
the URL-bearing fields of live Dynamics ACCOUNT records (websiteurl)
stand in for extractable document links — the search/extract seam runs
end-to-end against real records until you point it at a real
SharePoint/Graph endpoint. Say the same in your own mutation if you
reinterpret an entity.

HOW THIS TEMPLATE WORKS
  1. Out of the box it pulls live account records over real HTTP from
     the globally hosted Static Dynamics 365 tenant (Aster Lane Office
     Systems — synthetic data, no credentials, works from anywhere):
     https://kody-w.github.io/static-dynamics-365/api/data/v9.2/
     Try: perform(operation="url_extraction", search_query="granite")
     — extracts the real seeded link for Granite Peak Manufacturing
     from the live tenant.
  2. No network? Everything falls back to the embedded demo layer below
     (_DOCUMENT_LIBRARY) — the agent never crashes offline.
  3. Make it yours at the LIVE DATA SEAM below: set
     SHAREPOINT_DOCUMENT_EXTRACTOR_DATA_URL to any OData-shaped
     endpoint, or replace _fetch_collection() with a Microsoft Graph /
     SharePoint REST client. The fields the rest of the file needs are
     listed in _normalize_live_document() — file size, type, and
     permissions are labeled "n/a — enrichment seam"; wire your
     SharePoint metadata there.

OPERATIONS
  document_search | url_extraction | metadata_enrichment
  | link_validation
  kwargs: operation (required), search_query
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "templates"))

from basic_agent import BasicAgent
import json
import urllib.request

# ═══════════════════════════════════════════════════════════════
# RAPP AGENT MANIFEST
# ═══════════════════════════════════════════════════════════════
__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@aibast-agents-library/sharepoint_document_extractor",
    "version": "1.1.0",
    "display_name": "SharePoint Document Extractor",
    "description": "Extracts and searches document links from live records in a simulated Dynamics 365 tenant, with metadata seams and offline fallback.",
    "author": "AIBAST",
    "tags": ["sharepoint", "documents", "url-extraction", "metadata", "search"],
    "category": "general",
    "quality_tier": "community",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
}


# ═══════════════════════════════════════════════════════════════
# LIVE DATA SEAM — swap this for your real system
#
# Default: the globally hosted Static Dynamics 365 tenant (synthetic
# Aster Lane Office Systems data served as OData-shaped JSON from
# GitHub Pages). To hook your own world, either:
#   export SHAREPOINT_DOCUMENT_EXTRACTOR_DATA_URL=https://your-org/api/data/v9.2
# or replace _fetch_collection() with a Graph/SharePoint client.
# Downstream code only needs the fields produced by
# _normalize_live_document().
# ═══════════════════════════════════════════════════════════════

DATA_SOURCE_URL = os.environ.get(
    "SHAREPOINT_DOCUMENT_EXTRACTOR_DATA_URL",
    "https://kody-w.github.io/static-dynamics-365/api/data/v9.2",
)
_LIVE_CACHE = {}


def _fetch_collection(collection, timeout=6):
    """One bounded GET per collection per process. Returns [] on ANY
    failure — offline, DNS, bad JSON — so the demo layer takes over."""
    if collection in _LIVE_CACHE:
        return _LIVE_CACHE[collection]
    try:
        req = urllib.request.Request(
            f"{DATA_SOURCE_URL}/{collection}.json",
            headers={"User-Agent": "rapp-agent-template/1.0"},
        )
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            rows = json.loads(resp.read().decode("utf-8")).get("value", [])
    except Exception:
        rows = []
    _LIVE_CACHE[collection] = rows
    return rows


def _normalize_live_document(row):
    """Project a URL-bearing Dynamics account record onto the document
    shape this agent uses. THIS is the contract your replacement data
    source must meet — a dict with these keys. None means 'not
    available from the record alone' and renderers label it as an
    enrichment seam (a real SharePoint client fills these)."""
    name = row.get("name", "Unknown")
    return {
        "id": row.get("accountnumber", row.get("accountid", "")),
        "title": f"{name} — company website link",
        "file_name": None,        # enrichment seam — not a file in this stand-in
        "library": "Dynamics 365 accounts (live tenant)",
        "folder": None,           # enrichment seam
        "size_kb": None,          # enrichment seam
        "type": "Web link",
        "modified": str(row.get("modifiedon", ""))[:10],
        "modified_by": row.get("owneridname", ""),
        "url": row.get("websiteurl", ""),
        "tags": [str(row.get("industrycode", "")).lower(), name.lower()],
        "_live": True,
    }


def _live_documents(query=""):
    """Live tenant link records matching query; [] when offline."""
    rows = _fetch_collection("accounts")
    docs = [_normalize_live_document(r) for r in rows if r.get("websiteurl")]
    if not query:
        return docs
    q = query.lower()
    return [d for d in docs if q in d["title"].lower() or any(q in t for t in d["tags"])]


# ═══════════════════════════════════════════════════════════════
# EMBEDDED DEMO LAYER (offline fallback)
# ═══════════════════════════════════════════════════════════════

_DOCUMENT_LIBRARY = {
    "DOC-001": {"id": "DOC-001", "title": "Enterprise Platform - Product Brief", "file_name": "Enterprise_Platform_Brief_v3.pdf", "library": "Sales Collateral", "folder": "/Products/Platform", "size_kb": 2450, "type": "PDF", "modified": "2025-10-28", "modified_by": "Marketing Team", "url": "https://contoso.sharepoint.com/sites/sales/Shared%20Documents/Products/Platform/Enterprise_Platform_Brief_v3.pdf", "tags": ["product", "platform", "enterprise", "brief"]},
    "DOC-002": {"id": "DOC-002", "title": "Q3 2025 Sales Playbook", "file_name": "Q3_2025_Sales_Playbook.pptx", "library": "Sales Enablement", "folder": "/Playbooks/2025", "size_kb": 8900, "type": "PowerPoint", "modified": "2025-09-15", "modified_by": "Sales Ops", "url": "https://contoso.sharepoint.com/sites/sales/Shared%20Documents/Playbooks/2025/Q3_2025_Sales_Playbook.pptx", "tags": ["playbook", "sales", "q3", "2025"]},
    "DOC-003": {"id": "DOC-003", "title": "Competitive Analysis - Competitor B", "file_name": "Competitive_Analysis_CompB_2025.xlsx", "library": "Competitive Intel", "folder": "/Competitors", "size_kb": 1200, "type": "Excel", "modified": "2025-11-05", "modified_by": "Product Marketing", "url": "https://contoso.sharepoint.com/sites/sales/Shared%20Documents/Competitors/Competitive_Analysis_CompB_2025.xlsx", "tags": ["competitive", "analysis", "competitor-b"]},
    "DOC-004": {"id": "DOC-004", "title": "ROI Calculator Template", "file_name": "ROI_Calculator_Template_v2.xlsx", "library": "Sales Tools", "folder": "/Calculators", "size_kb": 350, "type": "Excel", "modified": "2025-08-20", "modified_by": "Finance Team", "url": "https://contoso.sharepoint.com/sites/sales/Shared%20Documents/Calculators/ROI_Calculator_Template_v2.xlsx", "tags": ["roi", "calculator", "template", "pricing"]},
    "DOC-005": {"id": "DOC-005", "title": "Customer Reference - Meridian Corp Case Study", "file_name": "Meridian_Corp_Case_Study.pdf", "library": "Customer Success", "folder": "/Case Studies/Technology", "size_kb": 1800, "type": "PDF", "modified": "2025-10-10", "modified_by": "Customer Success", "url": "https://contoso.sharepoint.com/sites/sales/Shared%20Documents/Case%20Studies/Technology/Meridian_Corp_Case_Study.pdf", "tags": ["case-study", "meridian", "technology", "reference"]},
    "DOC-006": {"id": "DOC-006", "title": "MSA Template - Enterprise Agreement", "file_name": "MSA_Enterprise_Template_2025.docx", "library": "Legal Templates", "folder": "/Contracts/Templates", "size_kb": 420, "type": "Word", "modified": "2025-07-01", "modified_by": "Legal Team", "url": "https://contoso.sharepoint.com/sites/legal/Shared%20Documents/Contracts/Templates/MSA_Enterprise_Template_2025.docx", "tags": ["contract", "msa", "enterprise", "template", "legal"]},
    "DOC-007": {"id": "DOC-007", "title": "HIPAA Compliance Whitepaper", "file_name": "HIPAA_Compliance_Whitepaper.pdf", "library": "Compliance", "folder": "/Healthcare", "size_kb": 3200, "type": "PDF", "modified": "2025-09-20", "modified_by": "Compliance Team", "url": "https://contoso.sharepoint.com/sites/compliance/Shared%20Documents/Healthcare/HIPAA_Compliance_Whitepaper.pdf", "tags": ["hipaa", "compliance", "healthcare", "whitepaper"]},
}

_METADATA_FIELDS = {
    "standard": ["Title", "File Name", "Modified", "Modified By", "File Size", "Content Type"],
    "custom": ["Document Category", "Target Audience", "Approval Status", "Expiration Date", "Confidentiality Level"],
    "search": ["Tags", "Full Text Index", "Associated Account", "Deal Stage"],
}

_URL_PATTERNS = {
    "direct_download": "https://{tenant}.sharepoint.com/sites/{site}/_layouts/15/download.aspx?SourceUrl={encoded_path}",
    "web_view": "https://{tenant}.sharepoint.com/sites/{site}/_layouts/15/Doc.aspx?sourcedoc={doc_id}",
    "sharing_link": "https://{tenant}.sharepoint.com/:b:/s/{site}/{share_id}",
    "embed": "https://{tenant}.sharepoint.com/sites/{site}/_layouts/15/embed.aspx?UniqueId={doc_id}",
}

_LINK_VALIDATION_RESULTS = [
    {"doc_id": "DOC-001", "status": "Valid", "http_code": 200, "accessible": True, "permissions": "Organization", "last_checked": "2025-11-14T10:00:00Z"},
    {"doc_id": "DOC-002", "status": "Valid", "http_code": 200, "accessible": True, "permissions": "Sales Team", "last_checked": "2025-11-14T10:00:01Z"},
    {"doc_id": "DOC-003", "status": "Valid", "http_code": 200, "accessible": True, "permissions": "Sales Team", "last_checked": "2025-11-14T10:00:02Z"},
    {"doc_id": "DOC-004", "status": "Valid", "http_code": 200, "accessible": True, "permissions": "Organization", "last_checked": "2025-11-14T10:00:03Z"},
    {"doc_id": "DOC-005", "status": "Valid", "http_code": 200, "accessible": True, "permissions": "Organization", "last_checked": "2025-11-14T10:00:04Z"},
    {"doc_id": "DOC-006", "status": "Restricted", "http_code": 403, "accessible": False, "permissions": "Legal Team Only", "last_checked": "2025-11-14T10:00:05Z"},
    {"doc_id": "DOC-007", "status": "Valid", "http_code": 200, "accessible": True, "permissions": "Organization", "last_checked": "2025-11-14T10:00:06Z"},
]


# ═══════════════════════════════════════════════════════════════
# HELPERS
# ═══════════════════════════════════════════════════════════════

def _search_documents(query):
    if not query:
        return list(_DOCUMENT_LIBRARY.values())
    q = query.lower()
    results = []
    for doc in _DOCUMENT_LIBRARY.values():
        if (q in doc["title"].lower() or q in doc["file_name"].lower() or
                any(q in tag for tag in doc["tags"])):
            results.append(doc)
    return results


def _get_validation_status(doc_id):
    for v in _LINK_VALIDATION_RESULTS:
        if v["doc_id"] == doc_id:
            return v
    return {"status": "Unknown", "http_code": 0, "accessible": False, "permissions": "Unknown"}


def _na(value, suffix=""):
    return "n/a — enrichment seam" if value in (None, "") else f"{value}{suffix}"


# ═══════════════════════════════════════════════════════════════
# AGENT CLASS
# ═══════════════════════════════════════════════════════════════

class SharePointDocumentExtractorAgent(BasicAgent):
    """
    SharePoint document search and URL extraction agent.

    Operations:
        document_search      - search SharePoint for documents
        url_extraction       - extract shareable URLs for documents
        metadata_enrichment  - enrich document metadata
        link_validation      - validate document link accessibility
    """

    def __init__(self):
        self.name = "SharePointDocumentExtractorAgent"
        self.metadata = {
            "name": self.name,
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {
                    "operation": {
                        "type": "string",
                        "enum": [
                            "document_search", "url_extraction",
                            "metadata_enrichment", "link_validation",
                        ],
                        "description": "The SharePoint operation to perform",
                    },
                    "search_query": {
                        "type": "string",
                        "description": "Search query for documents",
                    },
                },
                "required": ["operation"],
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, **kwargs) -> str:
        op = kwargs.get("operation", "document_search")
        query = kwargs.get("search_query", "")
        dispatch = {
            "document_search": self._document_search,
            "url_extraction": self._url_extraction,
            "metadata_enrichment": self._metadata_enrichment,
            "link_validation": self._link_validation,
        }
        handler = dispatch.get(op)
        if not handler:
            return f"Unknown operation: {op}"
        return handler(query)

    def _document_search(self, query):
        embedded = _search_documents(query)
        live = _live_documents(query)
        rows = ""
        for doc in embedded:
            rows += f"| {doc['id']} | {doc['title'][:35]} | {doc['type']} | {doc['library']} | {doc['modified']} | {doc['size_kb']:,} KB |\n"
        for doc in live[:12]:
            rows += f"| {doc['id']} | {doc['title'][:35]} | {doc['type']} | live tenant | {doc['modified']} | {_na(doc['size_kb'])} |\n"
        if not rows:
            rows = "| - | No matches | - | - | - | - |\n"
        live_note = (
            f"Live results come from URL-bearing account records in the Aster Lane "
            f"Dynamics 365 tenant (a stand-in for a document library).\n"
            if live else
            "Live tenant unreachable or no live matches — embedded demo library only.\n"
        )
        return (
            f"**Document Search**\n"
            f"Query: \"{query or 'all documents'}\"\n\n"
            f"| ID | Title | Type | Library | Modified | Size |\n|---|---|---|---|---|---|\n"
            f"{rows}\n"
            f"**Results:** {len(embedded)} embedded (simulated) + {len(live)} live\n"
            f"{live_note}\n"
            f"Source: [Document Search + Live Dynamics 365 Tenant]\nAgents: SharePointDocumentExtractorAgent"
        )

    def _url_extraction(self, query):
        live = _live_documents(query)
        embedded = _search_documents(query)
        url_rows = ""
        for doc in live[:12]:
            url_rows += f"| {doc['id']} | {doc['title'][:30]} | {doc['url']} | live tenant |\n"
        for doc in embedded:
            url_rows += f"| {doc['id']} | {doc['title'][:30]} | {doc['url']} | embedded (simulated) |\n"
        if not url_rows:
            url_rows = "| - | No matches | - | - |\n"
        pattern_rows = ""
        for pattern_name, template in _URL_PATTERNS.items():
            pattern_rows += f"| {pattern_name.replace('_', ' ').title()} | `{template[:60]}...` |\n"
        return (
            f"**URL Extraction Results**\n"
            f"Query: \"{query or 'all documents'}\"\n\n"
            f"| ID | Document | URL | Origin |\n|---|---|---|---|\n"
            f"{url_rows}\n"
            f"**SharePoint URL Patterns (for your real tenant):**\n\n"
            f"| Type | Pattern |\n|---|---|\n"
            f"{pattern_rows}\n\n"
            f"Source: [Live Dynamics 365 Tenant + Document Library]\nAgents: SharePointDocumentExtractorAgent"
        )

    def _metadata_enrichment(self, query):
        live = _live_documents(query)
        results = live or _search_documents(query) or list(_DOCUMENT_LIBRARY.values())
        doc = results[0]
        origin = "LIVE Dynamics 365 tenant record" if doc.get("_live") else "embedded demo layer (simulated)"
        meta_rows = ""
        meta_rows += f"| Title | {doc['title']} |\n"
        meta_rows += f"| File Name | {_na(doc['file_name'])} |\n"
        meta_rows += f"| Library | {doc['library']} |\n"
        meta_rows += f"| Folder | {_na(doc['folder'])} |\n"
        meta_rows += f"| Type | {doc['type']} |\n"
        meta_rows += f"| Size | {_na(doc['size_kb'], ' KB')} |\n"
        meta_rows += f"| Modified | {doc['modified']} |\n"
        meta_rows += f"| Modified By | {doc['modified_by']} |\n"
        meta_rows += f"| Tags | {', '.join(t for t in doc['tags'] if t)} |\n"
        field_rows = ""
        for cat, fields in _METADATA_FIELDS.items():
            field_rows += f"| {cat.title()} | {', '.join(fields)} |\n"
        return (
            f"**Metadata Enrichment** ({origin})\n\n"
            f"**Document Metadata:**\n\n"
            f"| Field | Value |\n|---|---|\n"
            f"{meta_rows}\n"
            f"**Available Metadata Fields (wire your SharePoint schema here):**\n\n"
            f"| Category | Fields |\n|---|---|\n"
            f"{field_rows}\n\n"
            f"Source: [Metadata API + Live Dynamics 365 Tenant]\nAgents: SharePointDocumentExtractorAgent"
        )

    def _link_validation(self, query):
        rows = ""
        valid_count = 0
        for v in _LINK_VALIDATION_RESULTS:
            doc = _DOCUMENT_LIBRARY.get(v["doc_id"], {})
            status_icon = "Pass" if v["accessible"] else "Fail"
            rows += f"| {v['doc_id']} | {doc.get('title', 'Unknown')[:30]} | {v['status']} | {v['http_code']} | {status_icon} | {v['permissions']} |\n"
            if v["accessible"]:
                valid_count += 1
        total = len(_LINK_VALIDATION_RESULTS)
        live = _live_documents("")
        live_note = (
            f"**Live links awaiting validation:** {len(live)} URLs extracted from the "
            "live tenant. Actually probing them is an enrichment seam — wire your "
            "HTTP checker or SharePoint permissions API.\n\n"
            if live else
            "**Live links awaiting validation:** live tenant unreachable.\n\n"
        )
        return (
            f"**Link Validation Report** (embedded demo results — simulated)\n\n"
            f"| Metric | Value |\n|---|---|\n"
            f"| Total Links | {total} |\n"
            f"| Valid | {valid_count} |\n"
            f"| Invalid/Restricted | {total - valid_count} |\n\n"
            f"**Validation Results:**\n\n"
            f"| ID | Document | Status | HTTP | Accessible | Permissions |\n|---|---|---|---|---|---|\n"
            f"{rows}\n"
            f"{live_note}"
            f"**Alerts:**\n"
            f"- DOC-006 (MSA Template) is restricted to Legal Team Only - request access if needed\n\n"
            f"Source: [Link Validator]\nAgents: SharePointDocumentExtractorAgent"
        )


if __name__ == "__main__":
    agent = SharePointDocumentExtractorAgent()
    print("=" * 60)
    print("EMBEDDED DEMO LIBRARY (works offline)")
    print(agent.perform(operation="document_search", search_query="product"))
    print()
    print("=" * 60)
    print("LIVE TENANT LINK EXTRACTION (fetched over HTTP; falls back offline)")
    print(agent.perform(operation="url_extraction", search_query="granite"))
    print()
    print("=" * 60)
    print(agent.perform(operation="link_validation"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
