---
name: "rar-cowork-cookbook-scheduled-brief-develop-training-strategy"
description: "Builds a morning brief on develop training strategy from Dynamics 365 ERP data for legal entity USMF: top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions; drafts an email to the re"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_develop_training_strategy", "rar_sha256": "45ebb9ea19ac2079e905de797bff064cd03bc2d962e13c8d639510e031c9627e", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
