---
name: "rar-cowork-cookbook-scheduled-brief-develop-product-strategy"
description: "Builds a morning brief on develop product strategy from Dynamics 365 ERP data for a legal entity, with top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then saves a draft email to the owne"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_develop_product_strategy", "rar_sha256": "66b8e6adc5eb1d1ff1a021c5a418212f1313e1cb5b4c50d7c5b5cf67b108a1ee", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
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
