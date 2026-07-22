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
