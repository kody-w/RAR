---
name: "rar-cowork-cookbook-user-access-review-audit"
description: "Runs a read-only Dynamics 365 user access review that lists users, security roles, and last sign-in dates, flags SoD conflicts, stale privileged accounts, and disabled users with roles, then returns an Excel workbook and"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/user_access_review_audit", "rar_sha256": "1c57319c138e7c8c44ad40e97ac4ef142628c8e9875b54c38b48195d8c890796", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/user_access_review_audit`. The original RAPP
agent is preserved byte-for-byte in `user_access_review_audit_agent.py` and in the RCI capsule.

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

User Access Review & SoD Audit — Runs a read-only Dynamics 365 user access review that lists users, security roles, and last sign-in dates, flags SoD conflicts, stale privileged accounts, and disabled users with roles, then returns an Excel workbook and

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

This entry carries the upstream recipe itself, under its licence and with
attribution: the prompt verbatim, the prerequisites, the step-by-step and
the expected output. Toasting made it deterministic — the same call returns
the same recipe every time — and callable from any Brainstem. The upstream
library remains the authority for the recipe and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/user-access-review-audit
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "inactivity_window_days": {
      "description": "Days without sign-in that mark a privileged account as stale; defaults to 90.",
      "type": "string"
    },
    "legal_entity": {
      "description": "The active Dynamics 365 legal entity to audit (e.g. USMF).",
      "type": "string"
    },
    "operation": {
      "description": "What to do: run, prompt, plan, checklist, describe.",
      "enum": [
        "run",
        "prompt",
        "plan",
        "checklist",
        "describe"
      ],
      "type": "string"
    },
    "report_date": {
      "description": "Date used in the output filename Access-review-<YYYY-MM-DD>.xlsx.",
      "type": "string"
    },
    "security_lead_email": {
      "description": "Recipient of the drafted summary email (the IT security lead).",
      "type": "string"
    },
    "sod_role_pair": {
      "description": "Conflicting role pair to flag; defaults to AP-vendor-maintenance plus AP-payment-release.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `user_access_review_audit_agent.py` and embedded as the fenced Python below (sha256 1c57319c138e7c8c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `user_access_review_audit_agent.py` first:

```bash
python3 user_access_review_audit_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 user_access_review_audit_agent.py   # or on stdin
python3 user_access_review_audit_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
User Access Review & SoD Audit — Runs a read-only Dynamics 365 user access review that lists users, security roles, and last sign-in dates, flags SoD conflicts, stale privileged accounts, and disabled users with roles, then returns an Excel workbook and

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

This entry carries the upstream recipe itself, under its licence and with
attribution: the prompt verbatim, the prerequisites, the step-by-step and
the expected output. Toasting made it deterministic — the same call returns
the same recipe every time — and callable from any Brainstem. The upstream
library remains the authority for the recipe and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/user-access-review-audit
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/user_access_review_audit',
    "version": '3.0.3',
    "display_name": 'User Access Review & SoD Audit',
    "description": 'Runs a read-only Dynamics 365 user access review that lists users, security roles, and last sign-in dates, flags SoD conflicts, stale privileged accounts, and disabled users with roles, then returns an Excel workbook and',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'verified',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'user-access-review-audit',
        "upstream_url": 'https://coworkcookbook.com/recipes/user-access-review-audit',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '5cbbbfcc8b58dc4a',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-23', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-system-access-and-security'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/user-access-review-audit', 'uses_skills': {'custom': [], 'ootb': ['Excel', 'Email'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
    # The platforms the upstream entry targets. First-class and queryable, not
    # buried in prose: this is what lets the registry answer "what can I launch
    # into Copilot Studio / Cowork / Scout", which is the whole reason an
    # agent.py container beats a bare skill entry for cross-platform reach.
    "platforms": ['Microsoft 365 Copilot Cowork'],
}


try:
    from agents.basic_agent import BasicAgent
except ModuleNotFoundError:
    class BasicAgent:
        def __init__(self, name, metadata):
            self.name = name
            self.metadata = metadata


# The toasted capability, generated by @kody-w/skill_toaster_agent. A licensed
# recipe entry carries the upstream recipe verbatim (with attribution) in
# _SPEC["recipe"]; a metadata-only entry carries RAR's own method for that shape
# of work. See the module docstring for which this is.
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the System administrator or Security administrator role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: Workbook with categorized access findings and a draft summary email.'], 'confidence': 1.0, 'deliverable': 'Workbook with categorized access findings and a draft summary email.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'inactivity_window_days': 'Days without sign-in that mark a privileged account as stale; defaults to 90.', 'legal_entity': 'The active Dynamics 365 legal entity to audit (e.g. USMF).', 'report_date': 'Date used in the output filename Access-review-<YYYY-MM-DD>.xlsx.', 'security_lead_email': 'Recipient of the drafted summary email (the IT security lead).', 'sod_role_pair': 'Conflicting role pair to flag; defaults to AP-vendor-maintenance plus AP-payment-release.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Reduces audit findings and insider-risk exposure by surfacing access drift (over-privileged accounts, ghost users, SoD conflicts) before the IT auditors do.', 'expected_output': 'Workbook with categorized access findings and a draft summary email.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the System administrator or Security administrator role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin, list every user in the active legal entity with their assigned security roles and the date they last signed in. Flag: (a) users with both AP-vendor-maintenance AND AP-payment-release roles (SoD conflict), (b) users with no sign-in in the last 90 days who still have privileged roles, (c) users disabled in the directory but still holding D365 roles. Output an Excel workbook 'Access-review-<YYYY-MM-DD>.xlsx' with a sheet per finding category, and draft an email to the IT security lead summarizing the counts. Do not change any role assignments. (Tenant note: in the USMF demo tenant, demo accounts may have stale sign-in data — focus on the SoD conflict signal.) This recipe is a strong candidate for a Cowork scheduled task: run weekly and email the report.", 'steps': ['Paste the prompt in Cowork.', 'Review the workbook with the IT security lead before remediating in D365.', '(Optional) Schedule this task in Cowork to run weekly.'], 'tenant_caveat': "Validated against a live Cowork tenant on 2026-05-23 with USMF. This recipe is a textbook example of Cowork's honest-degrade behavior: the agent engaged the D365 ERP plugin, pulled the user list from SystemUsers (25+ users), then surfaced a constraint table explaining exactly why the full SoD audit isn't possible from the plugin alone: SecurityUserRoles + SecurityRoles are blocked at the entity layer ('Access to entity is restricted for security reasons'), last-sign-in date isn't in F&O (lives in Entra/Azure AD audit logs), and disabled-in-directory state requires Microsoft Graph. Rather than fabricate, Cowork offered three actionable next steps: (1) admin exports SecurityUserRole + SecurityRole to CSV via Data management, (2) add Entra/Graph access for sign-in + account-state, or (3) ship a scoped workbook with just the F&O user roster + Enabled flag and an explanation of what's missing. The screenshot captures the honesty-constraint table - itself a deliverable that an IT security lead can use to scope the next iteration of the audit.", 'verified_against': 'm365.cloud.microsoft 2026-05-23', 'what_it_does': 'Identifies user access risks (SoD conflicts, stale accounts, orphaned roles) and produces an auditor-ready workbook.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Runs a read-only Dynamics 365 user access review that lists users, security roles, and last sign-in dates, flags SoD conflicts, stale privileged accounts, and disabled users with roles, then returns an Excel workbook and', 'example_request': 'Run a D365 access review for USMF — flag SoD conflicts and stale privileged roles, and draft the email to our security lead.', 'inputs': [{'description': 'The active Dynamics 365 legal entity to audit (e.g. USMF).', 'name': 'legal_entity'}, {'description': 'Days without sign-in that mark a privileged account as stale; defaults to 90.', 'name': 'inactivity_window_days'}, {'description': 'Conflicting role pair to flag; defaults to AP-vendor-maintenance plus AP-payment-release.', 'name': 'sod_role_pair'}, {'description': 'Recipient of the drafted summary email (the IT security lead).', 'name': 'security_lead_email'}, {'description': 'Date used in the output filename Access-review-<YYYY-MM-DD>.xlsx.', 'name': 'report_date'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when someone needs a periodic D365 access review or segregation-of-duties audit report; no role changes are made.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Paste the prompt in Cowork.', 'Review the workbook with the IT security lead before remediating in D365.', '(Optional) Schedule this task in Cowork to run weekly.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class UserAccessReviewAudit(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'UserAccessReviewAudit'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'inactivity_window_days': {'description': 'Days without sign-in that mark a privileged account as stale; defaults to 90.', 'type': 'string'}, 'legal_entity': {'description': 'The active Dynamics 365 legal entity to audit (e.g. USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'report_date': {'description': 'Date used in the output filename Access-review-<YYYY-MM-DD>.xlsx.', 'type': 'string'}, 'security_lead_email': {'description': 'Recipient of the drafted summary email (the IT security lead).', 'type': 'string'}, 'sod_role_pair': {'description': 'Conflicting role pair to flag; defaults to AP-vendor-maintenance plus AP-payment-release.', 'type': 'string'}},
                "required": ["operation"],
            },
        }
        super().__init__(self.name, self.metadata)

    # ── helpers ─────────────────────────────────────────────────────────

    def _subject(self, kwargs):
        for key in ("subject", "input", "target", "topic"):
            value = str(kwargs.get(key) or "").strip()
            if value:
                return value
        return ""

    def _header(self, subject):
        label = subject or f"<no {_SPEC['subject_label']} supplied>"
        return f"{_SPEC['verb']}: {label}"

    def _context(self, kwargs):
        extras = []
        for key in _SPEC["params"]:
            if key == "subject":
                continue
            value = str(kwargs.get(key) or "").strip()
            if value:
                extras.append(f"{key}: {value}")
        return extras

    def _plan(self, subject, kwargs):
        lines = [self._header(subject)]
        extras = self._context(kwargs)
        if extras:
            lines += ["", "Context:"] + [f"  {e}" for e in extras]
        lines += ["", "Procedure:"]
        lines += [f"  {i}. {step}" for i, step in enumerate(_SPEC["steps"], 1)]
        if not subject:
            lines += [
                "",
                f"Pass subject=\u0022...\u0022 to bind this procedure to a "
                f"specific {_SPEC['subject_label']}.",
            ]
        return lines

    def _checklist(self):
        return ["Acceptance checks:"] + [f"  [ ] {c}" for c in _SPEC["checks"]]

    def _provenance(self):
        src = __manifest__["source"]
        lines = [
            f"{__manifest__['display_name']} (v{__manifest__['version']})",
            "",
            __manifest__["description"],
            "",
            f"Capability shape: {_SPEC['archetype']} "
            f"(confidence {_SPEC['confidence']})",
        ]
        platforms = __manifest__.get("platforms") or []
        if platforms:
            lines.append("Runs on:          " + ", ".join(platforms))
        lines += [
            "",
            f"Indexed from:     {src['source_name']}",
            f"Upstream entry:   {src['upstream_url']}",
            f"Upstream author:  {__manifest__['author']}",
            "",
            "RAR indexes this capability and implements its method; the "
            "upstream library remains the authority for its own instructions. "
            "Open the link above to get those from the source.",
        ]
        return lines

    # ── recipe entries: the upstream recipe, verbatim, deterministic ─────

    def _recipe_context(self, kwargs):
        extras = []
        subject = self._subject(kwargs)
        if subject:
            extras.append(f"subject: {subject}")
        for key in _SPEC["params"]:
            value = str(kwargs.get(key) or "").strip()
            if value:
                extras.append(f"{key}: {value}")
        return extras

    def _recipe_prompt(self, kwargs):
        r = _SPEC["recipe"]
        lines = [r["prompt"]]
        extras = self._recipe_context(kwargs)
        if extras:
            lines += ["", "Context supplied by the caller:"] + [f"- {e}" for e in extras]
        return lines

    def _recipe_attribution(self):
        src = __manifest__["source"]
        r = _SPEC["recipe"]
        who = ", ".join(r.get("authors") or []) or __manifest__["author"]
        return [
            f"Recipe: {__manifest__['display_name']} — by {who}, {src['source_name']} "
            f"({src['license']}). Source: {src['upstream_url']}",
        ]

    def _perform_recipe(self, op, kwargs):
        r = _SPEC["recipe"]
        ref = _SPEC.get("refinement") or {}
        if op == "prompt":
            return "\n".join(self._recipe_prompt(kwargs) + [""] + self._recipe_attribution())
        if op == "plan":
            lines = [f"Steps for {__manifest__['display_name']} on {r['platform']}:"]
            lines += [f"  {i}. {s}" for i, s in enumerate(r["steps"], 1)]
            return "\n".join(lines + [""] + self._recipe_attribution())
        if op == "checklist":
            lines = ["Before you run it:"] + [f"  [ ] {p}" for p in r["prerequisites"]]
            if r.get("expected_output"):
                lines += ["", "Done when:", f"  [ ] {r['expected_output']}"]
            return "\n".join(lines + [""] + self._recipe_attribution())
        if op == "describe":
            lines = self._provenance()
            if ref.get("when_to_use"):
                lines += ["", f"When to use: {ref['when_to_use']}"]
            if ref.get("example_request"):
                lines += [f"Ask for it like: {ref['example_request']}"]
            if ref.get("inputs"):
                lines += ["", "It will ask you for:"] + [f"  - {i['name']}: {i['description']}" for i in ref["inputs"]]
            if r.get("business_value"):
                lines += ["", f"Why it matters: {r['business_value']}"]
            return "\n".join(lines)
        if op == "run":
            lines = [f"{__manifest__['display_name']} — run on {r['platform']}", ""]
            if r.get("what_it_does"):
                lines += [r["what_it_does"], ""]
            lines += [f"Prompt (paste into {r['platform']}):", ""] + self._recipe_prompt(kwargs) + [""]
            lines += ["Procedure:"] + [f"  {i}. {s}" for i, s in enumerate(r["steps"], 1)] + [""]
            lines += ["Acceptance checks:"] + [f"  [ ] {c}" for c in _SPEC["checks"]] + [""]
            lines += [f"Deliverable: {_SPEC['deliverable']}", ""]
            if r.get("tenant_caveat"):
                lines += [f"Verified upstream: {r['tenant_caveat']}", ""]
            return "\n".join(lines + self._recipe_attribution())
        return (
            f"Unknown operation {op!r}. Valid operations: "
            + ", ".join(_SPEC["operations"])
        )

    # ── entry point ─────────────────────────────────────────────────────

    def perform(self, **kwargs):
        """Run the toasted capability. Always returns a string."""
        op = str(kwargs.get("operation") or "run").strip().lower()
        subject = self._subject(kwargs)

        if _SPEC.get("recipe"):
            return self._perform_recipe(op, kwargs)

        if op == "describe":
            return "\n".join(self._provenance())

        if op == "checklist":
            return "\n".join([self._header(subject), ""] + self._checklist())

        if op == "plan":
            return "\n".join(self._plan(subject, kwargs))

        if op == "run":
            lines = self._plan(subject, kwargs)
            lines += [""] + self._checklist()
            lines += ["", f"Deliverable: {_SPEC['deliverable']}"]
            lines += ["", f"Source: {__manifest__['source']['upstream_url']}"]
            return "\n".join(lines)

        return (
            f"Unknown operation {op!r}. Valid operations: "
            + ", ".join(_SPEC["operations"])
        )


if __name__ == "__main__":
    print(UserAccessReviewAudit().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
