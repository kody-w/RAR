---
name: "rar-cowork-cookbook-scheduled-brief-print-shipping-documentation"
description: "Builds a morning brief on print shipping documentation from Dynamics 365 ERP (legal entity USMF): top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, then saves an email draft to"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_print_shipping_documentation", "rar_sha256": "8823a76d8ebee8a724d3f05f0614317a6744d61cae932eab0517cefcb73dd5d3", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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
