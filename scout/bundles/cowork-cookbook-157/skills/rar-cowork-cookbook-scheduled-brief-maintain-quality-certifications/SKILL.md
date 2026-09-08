---
name: "rar-cowork-cookbook-scheduled-brief-maintain-quality-certifications"
description: "Builds a quality-certification morning brief from Dynamics 365 ERP (legal entity USMF): top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, then saves a draft email to the owner p"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_maintain_quality_certifications", "rar_sha256": "da8f9e02cc680d9bf17af8db31662d36094bf53d7c18d3aff3b732757ef8dfb4", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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
