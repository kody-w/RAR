---
name: "rar-aibast-agents-library-staff-credentialing"
description: "Tracks staff credentials and onboarding, joining a live simulated FHIR practitioner registry with the Dynamics 365 CRM directory; offline fallback."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@aibast-agents-library/staff_credentialing", "rar_sha256": "f4e2302fd9589e02d08547a24c276c52493a853a3556a6a077ad87bcb50a701e", "source_kind": "rar-agent", "source_commit": "019464ea325329b5de69b4af699769f5151e2212", "version": "1.2.0", "author": "AIBAST", "tags": ["credentialing", "licenses", "certifications", "dea", "compliance", "healthcare"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@aibast-agents-library/staff_credentialing`. The original RAPP
agent is preserved byte-for-byte in `staff_credentialing_agent.py` and in the RCI capsule.

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

Staff Credentialing Agent — a template you are meant to mutate.

Manages healthcare staff credential tracking, expiration alerts,
verification audits, and onboarding checklists for licenses, certifications,
DEA registrations, and continuing education requirements.

HOW THIS TEMPLATE WORKS
  1. Out of the box it pulls live records over real HTTP from TWO
     globally hosted simulated systems (synthetic data, no credentials,
     works from anywhere):
       CRM  — the Static Dynamics 365 tenant (Aster Lane Office Systems):
              https://kody-w.github.io/static-dynamics-365/api/data/v9.2/
              The tenant's system users are reinterpreted as the staff
              roster awaiting credential verification — e.g. user
              "Morgan Ellis, Customer Service Manager".
       FHIR — the Static FHIR R4 server (Riverbend Medical Group):
              https://kody-w.github.io/static-fhir/fhir/
              14 live Practitioner resources with clinician IDs and
              qualification codes (RN, NP, PA, MD, DO...), 10 of whom
              are the same Aster Lane identities found in the CRM
              directory.
     Try: perform(operation="credential_status")
     — one output renders the FHIR Practitioner registry joined to the
     CRM system-user directory by full name (e.g. Jordan Lee is both
     RMG-CL-1001 Care Coordinator and a CRM Customer Service Rep).
  2. No network? Everything falls back to the embedded demo layer below
     (STAFF_CREDENTIALS / ONBOARDING_CHECKLIST_TEMPLATE) — the agent
     never crashes offline.
  3. Make it yours at the LIVE DATA SEAM below: set
     STAFF_CREDENTIALING_DATA_URL (CRM side) to any OData-shaped
     endpoint and STAFF_CREDENTIALING_FHIR_URL (clinical side) to any
     FHIR R4 searchset-bundle host — or replace _fetch_collection() /
     _fetch_fhir_bundle() with a primary-source verification API client
     (NPDB, DEA, state boards). Fields the rest of the file needs are
     listed in _normalize_live_staff() — license numbers, CME, and
     malpractice render as "n/a — enrichment seam" until you wire those
     systems.

OPERATIONS
  credential_status | expiration_alerts | verification_audit
  | onboarding_checklist
  kwargs: operation (required), staff_id

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "operation": {
      "description": "The credentialing operation to perform.",
      "enum": [
        "credential_status",
        "expiration_alerts",
        "verification_audit",
        "onboarding_checklist"
      ],
      "type": "string"
    },
    "staff_id": {
      "description": "Optional staff ID to filter results.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `staff_credentialing_agent.py` and embedded as the fenced Python below (sha256 f4e2302fd9589e02…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `staff_credentialing_agent.py` first:

```bash
python3 staff_credentialing_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 staff_credentialing_agent.py   # or on stdin
python3 staff_credentialing_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Staff Credentialing Agent — a template you are meant to mutate.

Manages healthcare staff credential tracking, expiration alerts,
verification audits, and onboarding checklists for licenses, certifications,
DEA registrations, and continuing education requirements.

HOW THIS TEMPLATE WORKS
  1. Out of the box it pulls live records over real HTTP from TWO
     globally hosted simulated systems (synthetic data, no credentials,
     works from anywhere):
       CRM  — the Static Dynamics 365 tenant (Aster Lane Office Systems):
              https://kody-w.github.io/static-dynamics-365/api/data/v9.2/
              The tenant's system users are reinterpreted as the staff
              roster awaiting credential verification — e.g. user
              "Morgan Ellis, Customer Service Manager".
       FHIR — the Static FHIR R4 server (Riverbend Medical Group):
              https://kody-w.github.io/static-fhir/fhir/
              14 live Practitioner resources with clinician IDs and
              qualification codes (RN, NP, PA, MD, DO...), 10 of whom
              are the same Aster Lane identities found in the CRM
              directory.
     Try: perform(operation="credential_status")
     — one output renders the FHIR Practitioner registry joined to the
     CRM system-user directory by full name (e.g. Jordan Lee is both
     RMG-CL-1001 Care Coordinator and a CRM Customer Service Rep).
  2. No network? Everything falls back to the embedded demo layer below
     (STAFF_CREDENTIALS / ONBOARDING_CHECKLIST_TEMPLATE) — the agent
     never crashes offline.
  3. Make it yours at the LIVE DATA SEAM below: set
     STAFF_CREDENTIALING_DATA_URL (CRM side) to any OData-shaped
     endpoint and STAFF_CREDENTIALING_FHIR_URL (clinical side) to any
     FHIR R4 searchset-bundle host — or replace _fetch_collection() /
     _fetch_fhir_bundle() with a primary-source verification API client
     (NPDB, DEA, state boards). Fields the rest of the file needs are
     listed in _normalize_live_staff() — license numbers, CME, and
     malpractice render as "n/a — enrichment seam" until you wire those
     systems.

OPERATIONS
  credential_status | expiration_alerts | verification_audit
  | onboarding_checklist
  kwargs: operation (required), staff_id
"""

import sys
import os
import json
import urllib.request
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "templates"))
from basic_agent import BasicAgent


__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@aibast-agents-library/staff_credentialing",
    "version": "1.2.0",
    "display_name": "Staff Credentialing Agent",
    "description": "Tracks staff credentials and onboarding, joining a live simulated FHIR practitioner registry with the Dynamics 365 CRM directory; offline fallback.",
    "author": "AIBAST",
    "tags": ["credentialing", "licenses", "certifications", "dea", "compliance", "healthcare"],
    "category": "healthcare",
    "quality_tier": "community",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
}


# ═══════════════════════════════════════════════════════════════
# LIVE DATA SEAM — swap this for your real systems
#
# Two live sources, both synthetic and hosted on GitHub Pages:
#   CRM  (OData-shaped Dynamics 365, Aster Lane Office Systems):
#     export STAFF_CREDENTIALING_DATA_URL=https://your-org/api/data/v9.2
#   FHIR (R4 searchset bundles, Riverbend Medical Group):
#     export STAFF_CREDENTIALING_FHIR_URL=https://your-fhir-host/fhir
# or replace _fetch_collection() / _fetch_fhir_bundle() with your
# HRIS / primary-source verification client. Downstream code only
# needs the fields produced by _normalize_live_staff() and
# _live_practitioner_registry().
# ═══════════════════════════════════════════════════════════════

DATA_SOURCE_URL = os.environ.get(
    "STAFF_CREDENTIALING_DATA_URL",
    "https://kody-w.github.io/static-dynamics-365/api/data/v9.2",
)
FHIR_SOURCE_URL = os.environ.get(
    "STAFF_CREDENTIALING_FHIR_URL",
    "https://kody-w.github.io/static-fhir/fhir",
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


def _normalize_live_staff(row):
    """Project a Dynamics system user onto the roster row this agent
    renders. THIS is the contract your replacement data source must meet —
    a dict with these keys. None means 'not knowable from the directory
    record alone' and the renderer labels it as an enrichment seam (wire
    your credentialing database, CME tracker, and malpractice carrier)."""
    return {
        "id": row.get("systemuserid", "")[:8] or "live",
        "name": row.get("fullname", "Unknown"),
        "role": row.get("title") or "n/a",
        "email": row.get("internalemailaddress", ""),
        "active": not row.get("isdisabled", False),
        "credentials": None,          # enrichment seam — wire primary-source verification
        "cme": None,                  # enrichment seam — wire your CME tracker
        "malpractice_expires": None,  # enrichment seam — wire your carrier feed
        "_live": True,
    }


def _live_staff_roster():
    """Tenant system users reinterpreted as the staff roster awaiting
    credential verification; [] when offline."""
    return [_normalize_live_staff(r) for r in _fetch_collection("systemusers")]


def _fetch_fhir_bundle(resource, timeout=6):
    """Sibling helper for the FHIR side: one bounded GET per resource
    type per process (cached by full URL). Returns the list of entry
    resources from the R4 searchset Bundle; [] on ANY failure."""
    url = f"{FHIR_SOURCE_URL}/{resource}.json"
    if url in _LIVE_CACHE:
        return _LIVE_CACHE[url]
    try:
        req = urllib.request.Request(
            url, headers={"User-Agent": "rapp-agent-template/1.0"}
        )
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            bundle = json.loads(resp.read().decode("utf-8"))
        rows = [e.get("resource", {}) for e in bundle.get("entry", [])]
    except Exception:
        rows = []
    _LIVE_CACHE[url] = rows
    return rows


def _live_practitioner_registry():
    """FHIR Practitioner resources joined to the CRM system-user
    directory by full name — 10 of the 14 Riverbend clinicians are the
    same Aster Lane identities that appear in the CRM. License numbers,
    expirations, CME, and malpractice remain enrichment seams (wire
    primary-source verification). [] when the FHIR feed is unreachable."""
    practitioners = _fetch_fhir_bundle("Practitioner")
    if not practitioners:
        return []
    crm_by_name = {
        u.get("fullname"): u for u in _fetch_collection("systemusers")
    }
    registry = []
    for res in practitioners:
        name = (res.get("name") or [{}])[0]
        full = " ".join(list(name.get("given", [])) + [name.get("family", "")]).strip() or "Unknown"
        qual = (res.get("qualification") or [{}])[0].get("code", {})
        crm = crm_by_name.get(full)
        registry.append({
            "clinician_id": (res.get("identifier") or [{}])[0].get(
                "value", res.get("id", "")[:8]
            ),
            "name": full,
            "credential_code": (qual.get("coding") or [{}])[0].get("code", "n/a"),
            "role": qual.get("text", "n/a"),
            "active": res.get("active", True),
            "email": next(
                (t.get("value") for t in res.get("telecom", [])
                 if t.get("system") == "email"),
                "n/a",
            ),
            "crm_title": crm.get("title") if crm else None,
        })
    return registry


# ---------------------------------------------------------------------------
# EMBEDDED DEMO LAYER (offline fallback)
# ---------------------------------------------------------------------------

STAFF_CREDENTIALS = {
    "STAFF-001": {
        "name": "Dr. Anita Patel",
        "role": "Physician - Internal Medicine",
        "npi": "1234567890",
        "hire_date": "2019-06-15",
        "credentials": [
            {"type": "Medical License", "issuer": "Illinois DFPR", "number": "036-123456", "issued": "2023-07-01", "expires": "2026-06-30", "status": "active", "verified": True},
            {"type": "DEA Registration", "issuer": "DEA", "number": "AP1234567", "issued": "2024-01-15", "expires": "2027-01-14", "status": "active", "verified": True},
            {"type": "Board Certification - Internal Medicine", "issuer": "ABIM", "number": "ABIM-884210", "issued": "2020-09-01", "expires": "2030-08-31", "status": "active", "verified": True},
            {"type": "BLS Certification", "issuer": "AHA", "number": "BLS-29401", "issued": "2025-03-10", "expires": "2027-03-10", "status": "active", "verified": True},
            {"type": "ACLS Certification", "issuer": "AHA", "number": "ACLS-18822", "issued": "2024-11-05", "expires": "2026-11-05", "status": "active", "verified": True},
        ],
        "cme_required_hrs": 50,
        "cme_completed_hrs": 38,
        "malpractice_insurance": {"carrier": "ProAssurance", "policy": "PA-2025-44821", "expires": "2026-12-31", "coverage_mm": 1.0},
    },
    "STAFF-002": {
        "name": "Dr. James Wright",
        "role": "Physician - Family Medicine",
        "npi": "9876543210",
        "hire_date": "2021-01-10",
        "credentials": [
            {"type": "Medical License", "issuer": "Illinois DFPR", "number": "036-654321", "issued": "2024-07-01", "expires": "2027-06-30", "status": "active", "verified": True},
            {"type": "DEA Registration", "issuer": "DEA", "number": "JW9876543", "issued": "2023-05-20", "expires": "2026-05-19", "status": "active", "verified": True},
            {"type": "Board Certification - Family Medicine", "issuer": "ABFM", "number": "ABFM-552104", "issued": "2021-12-01", "expires": "2031-11-30", "status": "active", "verified": True},
            {"type": "BLS Certification", "issuer": "AHA", "number": "BLS-30218", "issued": "2024-08-22", "expires": "2026-08-22", "status": "active", "verified": True},
        ],
        "cme_required_hrs": 50,
        "cme_completed_hrs": 52,
        "malpractice_insurance": {"carrier": "Coverys", "policy": "COV-2025-91024", "expires": "2026-12-31", "coverage_mm": 1.0},
    },
    "STAFF-003": {
        "name": "Lisa Chen, RN",
        "role": "Registered Nurse",
        "npi": "5551234567",
        "hire_date": "2022-08-01",
        "credentials": [
            {"type": "RN License", "issuer": "Illinois DFPR", "number": "041-789012", "issued": "2024-05-31", "expires": "2026-05-31", "status": "active", "verified": True},
            {"type": "BLS Certification", "issuer": "AHA", "number": "BLS-41092", "issued": "2025-01-15", "expires": "2027-01-15", "status": "active", "verified": True},
            {"type": "ACLS Certification", "issuer": "AHA", "number": "ACLS-22104", "issued": "2024-06-10", "expires": "2026-06-10", "status": "active", "verified": True},
            {"type": "PALS Certification", "issuer": "AHA", "number": "PALS-15580", "issued": "2023-09-20", "expires": "2025-09-20", "status": "expired", "verified": False},
        ],
        "cme_required_hrs": 20,
        "cme_completed_hrs": 14,
        "malpractice_insurance": {"carrier": "NSO", "policy": "NSO-2025-67210", "expires": "2026-06-30", "coverage_mm": 0.5},
    },
    "STAFF-004": {
        "name": "Mark Johnson, PA-C",
        "role": "Physician Assistant",
        "npi": "4449876543",
        "hire_date": "2023-03-15",
        "credentials": [
            {"type": "PA License", "issuer": "Illinois DFPR", "number": "085-345678", "issued": "2023-03-01", "expires": "2026-02-28", "status": "expired", "verified": False},
            {"type": "NCCPA Certification", "issuer": "NCCPA", "number": "NCCPA-778410", "issued": "2023-01-01", "expires": "2033-12-31", "status": "active", "verified": True},
            {"type": "DEA Registration", "issuer": "DEA", "number": "MJ3456789", "issued": "2023-04-01", "expires": "2026-03-31", "status": "active", "verified": True},
            {"type": "BLS Certification", "issuer": "AHA", "number": "BLS-52201", "issued": "2025-06-20", "expires": "2027-06-20", "status": "active", "verified": True},
        ],
        "cme_required_hrs": 100,
        "cme_completed_hrs": 68,
        "malpractice_insurance": {"carrier": "HPSO", "policy": "HPSO-2025-33104", "expires": "2026-09-30", "coverage_mm": 0.5},
    },
}

ONBOARDING_CHECKLIST_TEMPLATE = [
    {"item": "Background check completed", "category": "compliance"},
    {"item": "License verification (primary source)", "category": "credentialing"},
    {"item": "DEA verification (if applicable)", "category": "credentialing"},
    {"item": "Board certification verification", "category": "credentialing"},
    {"item": "Malpractice insurance verification", "category": "compliance"},
    {"item": "NPI validation", "category": "credentialing"},
    {"item": "Payer enrollment initiated", "category": "billing"},
    {"item": "EHR access provisioned", "category": "it"},
    {"item": "HIPAA training completed", "category": "compliance"},
    {"item": "Orientation completed", "category": "hr"},
    {"item": "Privileges approved by medical staff committee", "category": "credentialing"},
    {"item": "Malpractice tail coverage confirmed", "category": "compliance"},
]


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _credential_status():
    statuses = []
    for sid, staff in STAFF_CREDENTIALS.items():
        active = sum(1 for c in staff["credentials"] if c["status"] == "active")
        expired = sum(1 for c in staff["credentials"] if c["status"] == "expired")
        total = len(staff["credentials"])
        cme_pct = round(staff["cme_completed_hrs"] / staff["cme_required_hrs"] * 100, 1) if staff["cme_required_hrs"] else 0
        statuses.append({
            "id": sid, "name": staff["name"], "role": staff["role"],
            "total_credentials": total, "active": active, "expired": expired,
            "cme_pct": cme_pct, "cme_completed": staff["cme_completed_hrs"],
            "cme_required": staff["cme_required_hrs"],
            "malpractice_expires": staff["malpractice_insurance"]["expires"],
        })
    return {"staff": statuses}


def _expiration_alerts():
    alerts = []
    for sid, staff in STAFF_CREDENTIALS.items():
        for cred in staff["credentials"]:
            if cred["status"] == "expired":
                alerts.append({
                    "staff_id": sid, "name": staff["name"],
                    "credential": cred["type"], "expired": cred["expires"],
                    "severity": "critical", "action": "Immediate renewal required",
                })
            elif cred["expires"] <= "2026-06-30":
                alerts.append({
                    "staff_id": sid, "name": staff["name"],
                    "credential": cred["type"], "expired": cred["expires"],
                    "severity": "warning", "action": "Renewal due within 90 days",
                })
        mal = staff["malpractice_insurance"]
        if mal["expires"] <= "2026-06-30":
            alerts.append({
                "staff_id": sid, "name": staff["name"],
                "credential": "Malpractice Insurance", "expired": mal["expires"],
                "severity": "warning", "action": "Policy renewal needed",
            })
    alerts.sort(key=lambda x: (0 if x["severity"] == "critical" else 1, x["expired"]))
    return {"alerts": alerts, "total": len(alerts),
            "critical": sum(1 for a in alerts if a["severity"] == "critical")}


def _verification_audit():
    audit_items = []
    for sid, staff in STAFF_CREDENTIALS.items():
        for cred in staff["credentials"]:
            audit_items.append({
                "staff_id": sid, "name": staff["name"],
                "credential": cred["type"], "number": cred["number"],
                "issuer": cred["issuer"], "verified": cred["verified"],
                "status": cred["status"],
            })
    verified = sum(1 for a in audit_items if a["verified"])
    total = len(audit_items)
    return {"items": audit_items, "total": total, "verified": verified,
            "verification_rate": round(verified / total * 100, 1) if total else 0}


def _onboarding_checklist():
    return {"checklist": ONBOARDING_CHECKLIST_TEMPLATE,
            "total_items": len(ONBOARDING_CHECKLIST_TEMPLATE),
            "categories": list(set(item["category"] for item in ONBOARDING_CHECKLIST_TEMPLATE))}


# ---------------------------------------------------------------------------
# Agent
# ---------------------------------------------------------------------------

class StaffCredentialingAgent(BasicAgent):
    """Staff credential tracking and compliance management agent."""

    def __init__(self):
        self.name = "StaffCredentialingAgent"
        self.metadata = {
            "name": self.name,
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {
                    "operation": {
                        "type": "string",
                        "enum": [
                            "credential_status",
                            "expiration_alerts",
                            "verification_audit",
                            "onboarding_checklist",
                        ],
                        "description": "The credentialing operation to perform.",
                    },
                    "staff_id": {
                        "type": "string",
                        "description": "Optional staff ID to filter results.",
                    },
                },
                "required": ["operation"],
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, **kwargs) -> str:
        op = kwargs.get("operation", "credential_status")
        if op == "credential_status":
            return self._credential_status()
        elif op == "expiration_alerts":
            return self._expiration_alerts()
        elif op == "verification_audit":
            return self._verification_audit()
        elif op == "onboarding_checklist":
            return self._onboarding_checklist()
        return f"**Error:** Unknown operation `{op}`."

    def _credential_status(self) -> str:
        data = _credential_status()
        lines = [
            "# Staff Credential Status",
            "",
            "| Staff Member | Role | Credentials | Active | Expired | CME Progress | Malpractice Exp. |",
            "|-------------|------|------------|--------|---------|-------------|-----------------|",
        ]
        for s in data["staff"]:
            lines.append(
                f"| {s['name']} | {s['role']} | {s['total_credentials']} "
                f"| {s['active']} | {s['expired']} | {s['cme_completed']}/{s['cme_required']} ({s['cme_pct']}%) "
                f"| {s['malpractice_expires']} |"
            )
        live = _live_staff_roster()
        if live:
            seam = "n/a — enrichment seam"
            lines += [
                "",
                "## Live Tenant Staff Roster (Dynamics system users, awaiting credential verification)",
                "",
                "| Staff Member | Role | Directory Status | Credentials | CME Progress | Malpractice Exp. |",
                "|-------------|------|------------------|-------------|-------------|-----------------|",
            ]
            for s in live:
                status = "Active" if s["active"] else "Disabled"
                lines.append(
                    f"| {s['name']} | {s['role']} | {status} | {s['credentials'] or seam} "
                    f"| {s['cme'] or seam} | {s['malpractice_expires'] or seam} |"
                )
        else:
            lines += ["", "_Live tenant unreachable — showing embedded demo staff only._"]
        registry = _live_practitioner_registry()
        if registry:
            seam = "n/a — enrichment seam"
            matched = sum(1 for p in registry if p["crm_title"])
            lines += [
                "",
                f"## Live FHIR Practitioner Registry ({len(registry)} Practitioner "
                "resources — Riverbend Medical Group, joined to the CRM directory)",
                "",
                f"{matched} of {len(registry)} practitioners are the same Aster Lane "
                "identities found in the CRM system-user directory above (joined on "
                "full name) — clinical credential on the FHIR side, business role on "
                "the CRM side, in one view:",
                "",
                "| Clinician ID | Practitioner | Credential | Clinical Role | Active | CRM Directory Role (Aster Lane) | License Exp. |",
                "|--------------|--------------|-----------|---------------|--------|--------------------------------|--------------|",
            ]
            for p in registry:
                active = "Yes" if p["active"] else "No"
                crm_role = p["crm_title"] or "no CRM match — clinical-only hire"
                lines.append(
                    f"| {p['clinician_id']} | {p['name']} | {p['credential_code']} "
                    f"| {p['role']} | {active} | {crm_role} | {seam} |"
                )
            lines += [
                "",
                "_License numbers, expirations, CME, and malpractice are enrichment "
                "seams on both sides — wire primary-source verification (NPDB, DEA, "
                "state boards) to fill them._",
            ]
        else:
            lines += ["", "_Live FHIR server unreachable — practitioner registry unavailable offline._"]
        return "\n".join(lines)

    def _expiration_alerts(self) -> str:
        data = _expiration_alerts()
        if data["total"] == 0:
            return "# Expiration Alerts\n\nNo credentials expiring within the alert window."
        lines = [
            "# Credential Expiration Alerts",
            "",
            f"**Total Alerts:** {data['total']} | **Critical:** {data['critical']}",
            "",
            "| Severity | Staff Member | Credential | Expires | Action Required |",
            "|----------|-------------|------------|---------|----------------|",
        ]
        for a in data["alerts"]:
            lines.append(
                f"| {a['severity'].upper()} | {a['name']} | {a['credential']} "
                f"| {a['expired']} | {a['action']} |"
            )
        return "\n".join(lines)

    def _verification_audit(self) -> str:
        data = _verification_audit()
        lines = [
            "# Verification Audit Report",
            "",
            f"**Total Credentials:** {data['total']} | **Verified:** {data['verified']} "
            f"| **Verification Rate:** {data['verification_rate']}%",
            "",
            "| Staff Member | Credential | Number | Issuer | Verified | Status |",
            "|-------------|------------|--------|--------|----------|--------|",
        ]
        for item in data["items"]:
            v = "YES" if item["verified"] else "NO"
            lines.append(
                f"| {item['name']} | {item['credential']} | {item['number']} "
                f"| {item['issuer']} | {v} | {item['status'].upper()} |"
            )
        return "\n".join(lines)

    def _onboarding_checklist(self) -> str:
        data = _onboarding_checklist()
        lines = [
            "# New Staff Onboarding Checklist",
            "",
            f"**Total Items:** {data['total_items']}",
            f"**Categories:** {', '.join(sorted(data['categories']))}",
            "",
            "| # | Item | Category |",
            "|---|------|----------|",
        ]
        for i, item in enumerate(data["checklist"], 1):
            lines.append(f"| {i} | {item['item']} | {item['category'].upper()} |")
        return "\n".join(lines)


# ---------------------------------------------------------------------------
if __name__ == "__main__":
    agent = StaffCredentialingAgent()
    print("=" * 60)
    print("EMBEDDED DEMO + LIVE CRM ROSTER + LIVE FHIR PRACTITIONERS")
    print("(sibling-live demo: 14 FHIR Practitioner resources join the")
    print("CRM system-user directory by full name — 10 shared identities;")
    print("both feeds fetched over HTTP and fall back offline)")
    print("=" * 60)
    print(agent.perform(operation="credential_status"))
    for op in ["expiration_alerts", "verification_audit", "onboarding_checklist"]:
        print(f"\n{'='*60}")
        print(f"Operation: {op}")
        print("=" * 60)
        print(agent.perform(operation=op))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
