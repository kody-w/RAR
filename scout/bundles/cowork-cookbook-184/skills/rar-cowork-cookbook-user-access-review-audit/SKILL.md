---
name: "rar-cowork-cookbook-user-access-review-audit"
description: "Runs a read-only Dynamics 365 user access review that lists users, security roles, and last sign-in dates, flags SoD conflicts, stale privileged accounts, and disabled users with roles, then returns an Excel workbook and"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/user_access_review_audit", "rar_sha256": "1c57319c138e7c8c44ad40e97ac4ef142628c8e9875b54c38b48195d8c890796", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
