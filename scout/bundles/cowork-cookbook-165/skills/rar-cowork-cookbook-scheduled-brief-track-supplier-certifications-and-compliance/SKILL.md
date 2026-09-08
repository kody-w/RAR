---
name: "rar-cowork-cookbook-scheduled-brief-track-supplier-certifications-and-compliance"
description: "Builds a supplier certification and compliance morning brief from Dynamics 365 ERP data for a legal entity, with top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, plus an email"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_track_supplier_certifications_and_compliance", "rar_sha256": "77a78d5080ac352329e1146f2a0e7ad0a9e00f4b0fe784284379351df7792106", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_track_supplier_certifications_and_compliance`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_track_supplier_certifications_and_compliance_agent.py` and in the RCI capsule.

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

Track supplier certifications and compliance Scheduled Email Brief — Builds a supplier certification and compliance morning brief from Dynamics 365 ERP data for a legal entity, with top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, plus an email

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-track-supplier-certifications-and-compliance
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
    "legal_entity": {
      "description": "Dynamics 365 legal entity to query, e.g. USMF.",
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
    "owner": {
      "description": "Responsible owner who receives the drafted email brief.",
      "type": "string"
    },
    "schedule": {
      "description": "Optional cadence for the brief, e.g. weekday mornings at 7am.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_track_supplier_certifications_and_compliance_agent.py` and embedded as the fenced Python below (sha256 77a78d5080ac3523…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_track_supplier_certifications_and_compliance_agent.py` first:

```bash
python3 scheduled_brief_track_supplier_certifications_and_compliance_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_track_supplier_certifications_and_compliance_agent.py   # or on stdin
python3 scheduled_brief_track_supplier_certifications_and_compliance_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Track supplier certifications and compliance Scheduled Email Brief — Builds a supplier certification and compliance morning brief from Dynamics 365 ERP data for a legal entity, with top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, plus an email

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-track-supplier-certifications-and-compliance
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_track_supplier_certifications_and_compliance',
    "version": '3.0.3',
    "display_name": 'Track supplier certifications and compliance Scheduled Email Brief',
    "description": 'Builds a supplier certification and compliance morning brief from Dynamics 365 ERP data for a legal entity, with top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, plus an email',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-track-supplier-certifications-and-compliance',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-track-supplier-certifications-and-compliance',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'ef6ce885ae7cafbb',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/manage-supplier-relationships/track-supplier-certifications-and-compliance'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/scheduled-brief-track-supplier-certifications-and-compliance', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to query, e.g. USMF.', 'owner': 'Responsible owner who receives the drafted email brief.', 'schedule': 'Optional cadence for the brief, e.g. weekday mornings at 7am.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Replaces a daily manual spreadsheet stitch with an automatic brief so owners walk into standup already knowing where track supplier certifications and compliance stands.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': 'Using the Dynamics 365 ERP plugin against legal entity USMF, build a short morning brief on track supplier certifications and compliance for the responsible owner. Include: (a) top 5 items by impact today, (b) any anomalies vs the 7-day rolling average, (c) recommended next actions. Draft an email to the owner (save to drafts, do not send). Also produce a Communications-ready summary suitable for a Teams channel post. This recipe is a strong candidate for a Cowork scheduled task - schedule for weekday mornings at 7am.', 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-25', 'what_it_does': 'Reads track supplier certifications and compliance, computes a short brief, drafts an email, and is a strong candidate for a Cowork scheduled task.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a supplier certification and compliance morning brief from Dynamics 365 ERP data for a legal entity, with top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, plus an email', 'example_request': 'Give me the supplier certification and compliance morning brief for USMF and draft it to the owner.', 'inputs': [{'description': 'Dynamics 365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Responsible owner who receives the drafted email brief.', 'name': 'owner'}, {'description': 'Optional cadence for the brief, e.g. weekday mornings at 7am.', 'name': 'schedule'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when someone wants a daily or weekly supplier certification/compliance brief for the responsible owner, drafted as an email and a Teams channel post.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ScheduledBriefTrackSupplierCertificationsAndCompliance(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefTrackSupplierCertificationsAndCompliance'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'owner': {'description': 'Responsible owner who receives the drafted email brief.', 'type': 'string'}, 'schedule': {'description': 'Optional cadence for the brief, e.g. weekday mornings at 7am.', 'type': 'string'}},
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
    print(ScheduledBriefTrackSupplierCertificationsAndCompliance().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
