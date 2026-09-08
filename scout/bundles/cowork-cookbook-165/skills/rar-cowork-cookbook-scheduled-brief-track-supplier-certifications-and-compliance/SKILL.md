---
name: "rar-cowork-cookbook-scheduled-brief-track-supplier-certifications-and-compliance"
description: "Builds a supplier certification and compliance morning brief from Dynamics 365 ERP data for a legal entity, with top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, plus an email"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_track_supplier_certifications_and_compliance", "rar_sha256": "77a78d5080ac352329e1146f2a0e7ad0a9e00f4b0fe784284379351df7792106", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
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
