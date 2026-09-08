---
name: "rar-cowork-cookbook-scheduled-brief-define-usability-strategy"
description: "Builds a morning brief on define usability strategy from Dynamics 365 ERP data for a legal entity, with top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then saves an email draft to the ow"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_define_usability_strategy", "rar_sha256": "0f562bac797e3e32ad4318efe1317b9a100a6f8bfe588825a6eb77fd1ef771cb", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_define_usability_strategy`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_define_usability_strategy_agent.py` and in the RCI capsule.

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

Define usability strategy Scheduled Email Brief — Builds a morning brief on define usability strategy from Dynamics 365 ERP data for a legal entity, with top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then saves an email draft to the ow

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-define-usability-strategy
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
      "description": "D365 F&SCM legal entity to query, e.g. USMF.",
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
      "description": "When to run it, e.g. weekday mornings at 7am or weekly.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_define_usability_strategy_agent.py` and embedded as the fenced Python below (sha256 0f562bac797e3e32…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_define_usability_strategy_agent.py` first:

```bash
python3 scheduled_brief_define_usability_strategy_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_define_usability_strategy_agent.py   # or on stdin
python3 scheduled_brief_define_usability_strategy_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define usability strategy Scheduled Email Brief — Builds a morning brief on define usability strategy from Dynamics 365 ERP data for a legal entity, with top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then saves an email draft to the ow

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-define-usability-strategy
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_define_usability_strategy',
    "version": '3.0.3',
    "display_name": 'Define usability strategy Scheduled Email Brief',
    "description": 'Builds a morning brief on define usability strategy from Dynamics 365 ERP data for a legal entity, with top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then saves an email draft to the ow',
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
        "upstream_slug": 'scheduled-brief-define-usability-strategy',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-define-usability-strategy',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '3d5861e029e8791d',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/implement-solutions/define-usability-strategy'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/scheduled-brief-define-usability-strategy', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 F&SCM legal entity to query, e.g. USMF.', 'owner': 'Responsible owner who receives the drafted email brief.', 'schedule': 'When to run it, e.g. weekday mornings at 7am or weekly.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Replaces a daily manual spreadsheet stitch with an automatic brief so owners walk into standup already knowing where define usability strategy stands.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': 'Using the Dynamics 365 ERP plugin against legal entity USMF, build a short morning brief on define usability strategy for the responsible owner. Include: (a) top 5 items by impact today, (b) any anomalies vs the 7-day rolling average, (c) recommended next actions. Draft an email to the owner (save to drafts, do not send). Also produce a Communications-ready summary suitable for a Teams channel post. This recipe is a strong candidate for a Cowork scheduled task - schedule for weekday mornings at 7am.', 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads define usability strategy, computes a short brief, drafts an email, and is a strong candidate for a Cowork scheduled task.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a morning brief on define usability strategy from Dynamics 365 ERP data for a legal entity, with top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then saves an email draft to the ow', 'example_request': 'Draft my weekday 7am usability strategy brief from D365 USMF and email it to the owner as a draft.', 'inputs': [{'description': 'D365 F&SCM legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Responsible owner who receives the drafted email brief.', 'name': 'owner'}, {'description': 'When to run it, e.g. weekday mornings at 7am or weekly.', 'name': 'schedule'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when someone wants a recurring (daily/weekday 7am or weekly) D365 ERP usability-strategy brief drafted as an unsent email and a Teams channel post summary.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ScheduledBriefDefineUsabilityStrategy(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefDefineUsabilityStrategy'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 F&SCM legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'owner': {'description': 'Responsible owner who receives the drafted email brief.', 'type': 'string'}, 'schedule': {'description': 'When to run it, e.g. weekday mornings at 7am or weekly.', 'type': 'string'}},
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
    print(ScheduledBriefDefineUsabilityStrategy().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
