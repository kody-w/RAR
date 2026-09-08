---
name: "rar-cowork-cookbook-scheduled-brief-develop-training-strategy"
description: "Builds a morning brief on develop training strategy from Dynamics 365 ERP data for legal entity USMF: top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions; drafts an email to the re"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_develop_training_strategy", "rar_sha256": "45ebb9ea19ac2079e905de797bff064cd03bc2d962e13c8d639510e031c9627e", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_develop_training_strategy`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_develop_training_strategy_agent.py` and in the RCI capsule.

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

Develop training strategy Scheduled Email Brief — Builds a morning brief on develop training strategy from Dynamics 365 ERP data for legal entity USMF: top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions; drafts an email to the re

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-develop-training-strategy
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
      "description": "Dynamics 365 legal entity to query; the recipe uses USMF.",
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
    "responsible_owner": {
      "description": "Person the brief is written for and whose email draft is addressed to them.",
      "type": "string"
    },
    "schedule": {
      "description": "Optional cadence for running it, e.g. weekday mornings at 7am.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_develop_training_strategy_agent.py` and embedded as the fenced Python below (sha256 45ebb9ea19ac2079…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_develop_training_strategy_agent.py` first:

```bash
python3 scheduled_brief_develop_training_strategy_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_develop_training_strategy_agent.py   # or on stdin
python3 scheduled_brief_develop_training_strategy_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop training strategy Scheduled Email Brief — Builds a morning brief on develop training strategy from Dynamics 365 ERP data for legal entity USMF: top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions; drafts an email to the re

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-develop-training-strategy
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_develop_training_strategy',
    "version": '3.0.3',
    "display_name": 'Develop training strategy Scheduled Email Brief',
    "description": 'Builds a morning brief on develop training strategy from Dynamics 365 ERP data for legal entity USMF: top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions; drafts an email to the re',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-develop-training-strategy',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-develop-training-strategy',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '620f281d0c5a76c7',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/train-users-and-increase-adoption/develop-training-strategy'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/scheduled-brief-develop-training-strategy', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to query; the recipe uses USMF.', 'responsible_owner': 'Person the brief is written for and whose email draft is addressed to them.', 'schedule': 'Optional cadence for running it, e.g. weekday mornings at 7am.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Replaces a daily manual spreadsheet stitch with an automatic brief so owners walk into standup already knowing where develop training strategy stands.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': 'Using the Dynamics 365 ERP plugin against legal entity USMF, build a short morning brief on develop training strategy for the responsible owner. Include: (a) top 5 items by impact today, (b) any anomalies vs the 7-day rolling average, (c) recommended next actions. Draft an email to the owner (save to drafts, do not send). Also produce a Communications-ready summary suitable for a Teams channel post. This recipe is a strong candidate for a Cowork scheduled task - schedule for weekday mornings at 7am.', 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads develop training strategy, computes a short brief, drafts an email, and is a strong candidate for a Cowork scheduled task.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a morning brief on develop training strategy from Dynamics 365 ERP data for legal entity USMF: top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions; drafts an email to the re', 'example_request': 'Give me the 7am training strategy morning brief for USMF and draft the email to the owner.', 'inputs': [{'description': 'Dynamics 365 legal entity to query; the recipe uses USMF.', 'name': 'legal_entity'}, {'description': 'Person the brief is written for and whose email draft is addressed to them.', 'name': 'responsible_owner'}, {'description': 'Optional cadence for running it, e.g. weekday mornings at 7am.', 'name': 'schedule'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a daily or weekly training-strategy brief for the responsible owner, as an email draft and Teams post summary, from D365 ERP data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ScheduledBriefDevelopTrainingStrategy(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefDevelopTrainingStrategy'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to query; the recipe uses USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'responsible_owner': {'description': 'Person the brief is written for and whose email draft is addressed to them.', 'type': 'string'}, 'schedule': {'description': 'Optional cadence for running it, e.g. weekday mornings at 7am.', 'type': 'string'}},
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
    print(ScheduledBriefDevelopTrainingStrategy().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
