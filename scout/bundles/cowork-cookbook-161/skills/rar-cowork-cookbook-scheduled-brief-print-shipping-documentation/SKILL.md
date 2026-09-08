---
name: "rar-cowork-cookbook-scheduled-brief-print-shipping-documentation"
description: "Builds a morning brief on print shipping documentation from Dynamics 365 ERP (legal entity USMF): top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, then saves an email draft to"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_print_shipping_documentation", "rar_sha256": "8823a76d8ebee8a724d3f05f0614317a6744d61cae932eab0517cefcb73dd5d3", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_print_shipping_documentation`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_print_shipping_documentation_agent.py` and in the RCI capsule.

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

Print shipping documentation Scheduled Email Brief — Builds a morning brief on print shipping documentation from Dynamics 365 ERP (legal entity USMF): top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, then saves an email draft to

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-print-shipping-documentation
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
      "description": "Dynamics 365 legal entity to query; defaults to USMF.",
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
      "description": "When the brief should run, e.g. weekday mornings at 7am.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_print_shipping_documentation_agent.py` and embedded as the fenced Python below (sha256 8823a76d8ebee8a7…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_print_shipping_documentation_agent.py` first:

```bash
python3 scheduled_brief_print_shipping_documentation_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_print_shipping_documentation_agent.py   # or on stdin
python3 scheduled_brief_print_shipping_documentation_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Print shipping documentation Scheduled Email Brief — Builds a morning brief on print shipping documentation from Dynamics 365 ERP (legal entity USMF): top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, then saves an email draft to

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-print-shipping-documentation
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_print_shipping_documentation',
    "version": '3.0.3',
    "display_name": 'Print shipping documentation Scheduled Email Brief',
    "description": 'Builds a morning brief on print shipping documentation from Dynamics 365 ERP (legal entity USMF): top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, then saves an email draft to',
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
        "upstream_slug": 'scheduled-brief-print-shipping-documentation',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-print-shipping-documentation',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '336927e1a5715cf9',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/manage-freight-and-transportation/print-shipping-documentation'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/scheduled-brief-print-shipping-documentation', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to query; defaults to USMF.', 'owner': 'Responsible owner who receives the drafted email brief.', 'schedule': 'When the brief should run, e.g. weekday mornings at 7am.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Replaces a daily manual spreadsheet stitch with an automatic brief so owners walk into standup already knowing where print shipping documentation stands.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': 'Using the Dynamics 365 ERP plugin against legal entity USMF, build a short morning brief on print shipping documentation for the responsible owner. Include: (a) top 5 items by impact today, (b) any anomalies vs the 7-day rolling average, (c) recommended next actions. Draft an email to the owner (save to drafts, do not send). Also produce a Communications-ready summary suitable for a Teams channel post. This recipe is a strong candidate for a Cowork scheduled task - schedule for weekday mornings at 7am.', 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads print shipping documentation, computes a short brief, drafts an email, and is a strong candidate for a Cowork scheduled task.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a morning brief on print shipping documentation from Dynamics 365 ERP (legal entity USMF): top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, then saves an email draft to', 'example_request': 'Draft my daily print shipping documentation brief from USMF and email it to the owner as a draft.', 'inputs': [{'description': 'Dynamics 365 legal entity to query; defaults to USMF.', 'name': 'legal_entity'}, {'description': 'Responsible owner who receives the drafted email brief.', 'name': 'owner'}, {'description': 'When the brief should run, e.g. weekday mornings at 7am.', 'name': 'schedule'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when someone wants a daily or weekly print shipping documentation brief for the responsible owner, as an unsent email draft plus a Teams channel summary.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ScheduledBriefPrintShippingDocumentation(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefPrintShippingDocumentation'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to query; defaults to USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'owner': {'description': 'Responsible owner who receives the drafted email brief.', 'type': 'string'}, 'schedule': {'description': 'When the brief should run, e.g. weekday mornings at 7am.', 'type': 'string'}},
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
    print(ScheduledBriefPrintShippingDocumentation().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
