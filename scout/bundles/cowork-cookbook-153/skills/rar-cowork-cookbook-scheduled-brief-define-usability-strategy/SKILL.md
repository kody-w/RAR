---
name: "rar-cowork-cookbook-scheduled-brief-define-usability-strategy"
description: "Builds a morning brief on define usability strategy from Dynamics 365 ERP data for a legal entity, with top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then saves an email draft to the ow"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_define_usability_strategy", "rar_sha256": "0f562bac797e3e32ad4318efe1317b9a100a6f8bfe588825a6eb77fd1ef771cb", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
