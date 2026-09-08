---
name: "rar-cowork-cookbook-scheduled-brief-maintain-quality-certifications"
description: "Builds a quality-certification morning brief from Dynamics 365 ERP (legal entity USMF): top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, then saves a draft email to the owner p"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_maintain_quality_certifications", "rar_sha256": "da8f9e02cc680d9bf17af8db31662d36094bf53d7c18d3aff3b732757ef8dfb4", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_maintain_quality_certifications`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_maintain_quality_certifications_agent.py` and in the RCI capsule.

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

Maintain quality certifications Scheduled Email Brief — Builds a quality-certification morning brief from Dynamics 365 ERP (legal entity USMF): top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, then saves a draft email to the owner p

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-maintain-quality-certifications
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
      "description": "D365 F&SCM legal entity to query; defaults to USMF.",
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
      "description": "Responsible owner who receives the drafted email.",
      "type": "string"
    },
    "schedule": {
      "description": "Optional cadence for the scheduled task, e.g. weekday mornings at 7am.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_maintain_quality_certifications_agent.py` and embedded as the fenced Python below (sha256 da8f9e02cc680d9b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_maintain_quality_certifications_agent.py` first:

```bash
python3 scheduled_brief_maintain_quality_certifications_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_maintain_quality_certifications_agent.py   # or on stdin
python3 scheduled_brief_maintain_quality_certifications_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Maintain quality certifications Scheduled Email Brief — Builds a quality-certification morning brief from Dynamics 365 ERP (legal entity USMF): top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, then saves a draft email to the owner p

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-maintain-quality-certifications
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_maintain_quality_certifications',
    "version": '3.0.3',
    "display_name": 'Maintain quality certifications Scheduled Email Brief',
    "description": 'Builds a quality-certification morning brief from Dynamics 365 ERP (legal entity USMF): top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, then saves a draft email to the owner p',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'inventory_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'community',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'scheduled-brief-maintain-quality-certifications',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-maintain-quality-certifications',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '9e48c53cac85f616',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/manage-inventory-quality/maintain-quality-certifications'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/scheduled-brief-maintain-quality-certifications', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 F&SCM legal entity to query; defaults to USMF.', 'owner': 'Responsible owner who receives the drafted email.', 'schedule': 'Optional cadence for the scheduled task, e.g. weekday mornings at 7am.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Replaces a daily manual spreadsheet stitch with an automatic brief so owners walk into standup already knowing where maintain quality certifications stands.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': 'Using the Dynamics 365 ERP plugin against legal entity USMF, build a short morning brief on maintain quality certifications for the responsible owner. Include: (a) top 5 items by impact today, (b) any anomalies vs the 7-day rolling average, (c) recommended next actions. Draft an email to the owner (save to drafts, do not send). Also produce a Communications-ready summary suitable for a Teams channel post. This recipe is a strong candidate for a Cowork scheduled task - schedule for weekday mornings at 7am.', 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads maintain quality certifications, computes a short brief, drafts an email, and is a strong candidate for a Cowork scheduled task.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a quality-certification morning brief from Dynamics 365 ERP (legal entity USMF): top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, then saves a draft email to the owner p', 'example_request': 'Give me the quality certifications morning brief for USMF and draft the email to the owner.', 'inputs': [{'description': 'D365 F&SCM legal entity to query; defaults to USMF.', 'name': 'legal_entity'}, {'description': 'Responsible owner who receives the drafted email.', 'name': 'owner'}, {'description': 'Optional cadence for the scheduled task, e.g. weekday mornings at 7am.', 'name': 'schedule'}], 'model': 'claude-opus-5', 'when_to_use': 'Use for a daily or weekly (weekday 7am) morning brief on maintain quality certifications for the responsible owner, delivered as an unsent email draft and Teams post text.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ScheduledBriefMaintainQualityCertifications(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefMaintainQualityCertifications'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 F&SCM legal entity to query; defaults to USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'owner': {'description': 'Responsible owner who receives the drafted email.', 'type': 'string'}, 'schedule': {'description': 'Optional cadence for the scheduled task, e.g. weekday mornings at 7am.', 'type': 'string'}},
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
    print(ScheduledBriefMaintainQualityCertifications().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
