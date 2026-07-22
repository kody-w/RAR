"""
Staff Credentialing Agent — a template you are meant to mutate.

Manages healthcare staff credential tracking, expiration alerts,
verification audits, and onboarding checklists for licenses, certifications,
DEA registrations, and continuing education requirements.

HOW THIS TEMPLATE WORKS
  1. Out of the box it pulls live records over real HTTP from the
     globally hosted Static Dynamics 365 tenant (Aster Lane Office
     Systems — synthetic data, no credentials, works from anywhere):
     https://kody-w.github.io/static-dynamics-365/api/data/v9.2/
     In this template the tenant's system users are reinterpreted as the
     staff roster awaiting credential verification — e.g. user
     "Morgan Ellis, Customer Service Manager".
     Try: perform(operation="credential_status")
  2. No network? Everything falls back to the embedded demo layer below
     (STAFF_CREDENTIALS / ONBOARDING_CHECKLIST_TEMPLATE) — the agent
     never crashes offline.
  3. Make it yours at the LIVE DATA SEAM below: set
     STAFF_CREDENTIALING_DATA_URL to any OData-shaped endpoint (your real
     Dynamics org, or JSON exported from your HRIS), or replace
     _fetch_collection() with a primary-source verification API client
     (NPDB, DEA, state boards). Fields the rest of the file needs are
     listed in _normalize_live_staff() — licenses, CME, and malpractice
     render as "n/a — enrichment seam" until you wire those systems.

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
    "version": "1.1.0",
    "display_name": "Staff Credentialing Agent",
    "description": "Tracks staff credentials, expirations, audits, and onboarding against a live simulated Dynamics 365 tenant, with an offline demo fallback.",
    "author": "AIBAST",
    "tags": ["credentialing", "licenses", "certifications", "dea", "compliance", "healthcare"],
    "category": "healthcare",
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
#   export STAFF_CREDENTIALING_DATA_URL=https://your-org/api/data/v9.2
# or replace _fetch_collection() with your HRIS / primary-source
# verification client. Downstream code only needs the fields produced
# by _normalize_live_staff().
# ═══════════════════════════════════════════════════════════════

DATA_SOURCE_URL = os.environ.get(
    "STAFF_CREDENTIALING_DATA_URL",
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
    print("EMBEDDED DEMO + LIVE TENANT STAFF ROSTER")
    print("(live section fetched over HTTP; falls back offline)")
    print("=" * 60)
    print(agent.perform(operation="credential_status"))
    for op in ["expiration_alerts", "verification_audit", "onboarding_checklist"]:
        print(f"\n{'='*60}")
        print(f"Operation: {op}")
        print("=" * 60)
        print(agent.perform(operation=op))
