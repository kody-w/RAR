---
name: "rar-cowork-cookbook-scheduled-brief-set-product-prices"
description: "Builds a morning brief on set product prices from Dynamics 365 ERP (legal entity USMF): top 5 items by impact, anomalies vs the 7-day rolling average, and recommended actions, plus an email draft and a Teams-ready summar"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_set_product_prices", "rar_sha256": "57201d2d4f19497a46d880002d12ca955fc2f061ea664d07c2e5f7fc9512df5a", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_set_product_prices`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_set_product_prices_agent.py` and in the RCI capsule.

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

Set product prices Scheduled Email Brief — Builds a morning brief on set product prices from Dynamics 365 ERP (legal entity USMF): top 5 items by impact, anomalies vs the 7-day rolling average, and recommended actions, plus an email draft and a Teams-ready summar

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-set-product-prices
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_set_product_prices_agent.py` and embedded as the fenced Python below (sha256 57201d2d4f19497a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_set_product_prices_agent.py` first:

```bash
python3 scheduled_brief_set_product_prices_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_set_product_prices_agent.py   # or on stdin
python3 scheduled_brief_set_product_prices_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Set product prices Scheduled Email Brief — Builds a morning brief on set product prices from Dynamics 365 ERP (legal entity USMF): top 5 items by impact, anomalies vs the 7-day rolling average, and recommended actions, plus an email draft and a Teams-ready summar

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-set-product-prices
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_set_product_prices',
    "version": '3.0.3',
    "display_name": 'Set product prices Scheduled Email Brief',
    "description": 'Builds a morning brief on set product prices from Dynamics 365 ERP (legal entity USMF): top 5 items by impact, anomalies vs the 7-day rolling average, and recommended actions, plus an email draft and a Teams-ready summar',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'design_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-set-product-prices',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-set-product-prices',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '6d082c3bbd31dfba',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['design-to-retire'], 'process_tags': ['design-to-retire/introduce-products/set-product-prices'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'design-to-retire/scheduled-brief-set-product-prices', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to query; defaults to USMF.', 'owner': 'Responsible owner who receives the drafted email brief.', 'schedule': 'When the brief should run, e.g. weekday mornings at 7am.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Replaces a daily manual spreadsheet stitch with an automatic brief so owners walk into standup already knowing where set product prices stands.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': 'Using the Dynamics 365 ERP plugin against legal entity USMF, build a short morning brief on set product prices for the responsible owner. Include: (a) top 5 items by impact today, (b) any anomalies vs the 7-day rolling average, (c) recommended next actions. Draft an email to the owner (save to drafts, do not send). Also produce a Communications-ready summary suitable for a Teams channel post. This recipe is a strong candidate for a Cowork scheduled task - schedule for weekday mornings at 7am.', 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads set product prices, computes a short brief, drafts an email, and is a strong candidate for a Cowork scheduled task.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a morning brief on set product prices from Dynamics 365 ERP (legal entity USMF): top 5 items by impact, anomalies vs the 7-day rolling average, and recommended actions, plus an email draft and a Teams-ready summar', 'example_request': 'Give me the 7am morning brief on set product prices in USMF and draft it to the owner.', 'inputs': [{'description': 'Dynamics 365 legal entity to query; defaults to USMF.', 'name': 'legal_entity'}, {'description': 'Responsible owner who receives the drafted email brief.', 'name': 'owner'}, {'description': 'When the brief should run, e.g. weekday mornings at 7am.', 'name': 'schedule'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when someone wants a daily or weekly product-pricing brief for the responsible owner, drafted as an email and a Teams channel post.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ScheduledBriefSetProductPrices(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefSetProductPrices'
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
    print(ScheduledBriefSetProductPrices().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
