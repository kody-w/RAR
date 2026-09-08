---
name: "rar-cowork-cookbook-scheduled-brief-develop-product-strategy"
description: "Builds a morning brief on develop product strategy from Dynamics 365 ERP data for a legal entity, with top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then saves a draft email to the owne"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_develop_product_strategy", "rar_sha256": "66b8e6adc5eb1d1ff1a021c5a418212f1313e1cb5b4c50d7c5b5cf67b108a1ee", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_develop_product_strategy`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_develop_product_strategy_agent.py` and in the RCI capsule.

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

Develop product strategy Scheduled Email Brief — Builds a morning brief on develop product strategy from Dynamics 365 ERP data for a legal entity, with top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then saves a draft email to the owne

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-develop-product-strategy
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
      "description": "Responsible owner who receives the drafted brief email.",
      "type": "string"
    },
    "schedule": {
      "description": "When to run the brief, e.g. weekday mornings at 7am, daily or weekly.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_develop_product_strategy_agent.py` and embedded as the fenced Python below (sha256 66b8e6adc5eb1d1f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_develop_product_strategy_agent.py` first:

```bash
python3 scheduled_brief_develop_product_strategy_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_develop_product_strategy_agent.py   # or on stdin
python3 scheduled_brief_develop_product_strategy_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop product strategy Scheduled Email Brief — Builds a morning brief on develop product strategy from Dynamics 365 ERP data for a legal entity, with top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then saves a draft email to the owne

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-develop-product-strategy
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_develop_product_strategy',
    "version": '3.0.3',
    "display_name": 'Develop product strategy Scheduled Email Brief',
    "description": 'Builds a morning brief on develop product strategy from Dynamics 365 ERP data for a legal entity, with top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then saves a draft email to the owne',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'forecast_to_plan', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-develop-product-strategy',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-develop-product-strategy',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'c951ca2aac7fd60a',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/develop-business-strategy/develop-product-strategy'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/scheduled-brief-develop-product-strategy', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to query, e.g. USMF.', 'owner': 'Responsible owner who receives the drafted brief email.', 'schedule': 'When to run the brief, e.g. weekday mornings at 7am, daily or weekly.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Replaces a daily manual spreadsheet stitch with an automatic brief so owners walk into standup already knowing where develop product strategy stands.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': 'Using the Dynamics 365 ERP plugin against legal entity USMF, build a short morning brief on develop product strategy for the responsible owner. Include: (a) top 5 items by impact today, (b) any anomalies vs the 7-day rolling average, (c) recommended next actions. Draft an email to the owner (save to drafts, do not send). Also produce a Communications-ready summary suitable for a Teams channel post. This recipe is a strong candidate for a Cowork scheduled task - schedule for weekday mornings at 7am.', 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads develop product strategy, computes a short brief, drafts an email, and is a strong candidate for a Cowork scheduled task.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a morning brief on develop product strategy from Dynamics 365 ERP data for a legal entity, with top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then saves a draft email to the owne', 'example_request': 'Draft my 7am weekday product strategy brief from D365 USMF and email it to the owner as a draft.', 'inputs': [{'description': 'Dynamics 365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Responsible owner who receives the drafted brief email.', 'name': 'owner'}, {'description': 'When to run the brief, e.g. weekday mornings at 7am, daily or weekly.', 'name': 'schedule'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when someone wants a daily or weekly scheduled product-strategy brief from D365 ERP, drafted as an email to the responsible owner plus a Teams channel post summary.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ScheduledBriefDevelopProductStrategy(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefDevelopProductStrategy'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'owner': {'description': 'Responsible owner who receives the drafted brief email.', 'type': 'string'}, 'schedule': {'description': 'When to run the brief, e.g. weekday mornings at 7am, daily or weekly.', 'type': 'string'}},
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
    print(ScheduledBriefDevelopProductStrategy().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
