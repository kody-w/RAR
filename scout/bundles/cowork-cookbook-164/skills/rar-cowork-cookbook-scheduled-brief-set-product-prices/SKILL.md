---
name: "rar-cowork-cookbook-scheduled-brief-set-product-prices"
description: "Builds a morning brief on set product prices from Dynamics 365 ERP (legal entity USMF): top 5 items by impact, anomalies vs the 7-day rolling average, and recommended actions, plus an email draft and a Teams-ready summar"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_set_product_prices", "rar_sha256": "57201d2d4f19497a46d880002d12ca955fc2f061ea664d07c2e5f7fc9512df5a", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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
