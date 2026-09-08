---
name: "rar-cowork-cookbook-scheduled-brief-hire-for-open-positions"
description: "Builds a morning brief on hire for open positions from Dynamics 365 ERP data for a legal entity, returning top 5 items by impact, anomalies vs the 7-day rolling average, recommended next actions, an email saved to drafts"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_hire_for_open_positions", "rar_sha256": "e81607dec21e66306c81f8f66ec38e4212b29c9ae9e63f86516baccc0ea17f3a", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_hire_for_open_positions`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_hire_for_open_positions_agent.py` and in the RCI capsule.

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

Hire for open positions Scheduled Email Brief — Builds a morning brief on hire for open positions from Dynamics 365 ERP data for a legal entity, returning top 5 items by impact, anomalies vs the 7-day rolling average, recommended next actions, an email saved to drafts

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-hire-for-open-positions
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
      "description": "D365 legal entity to query, e.g. USMF.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_hire_for_open_positions_agent.py` and embedded as the fenced Python below (sha256 e81607dec21e6630…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_hire_for_open_positions_agent.py` first:

```bash
python3 scheduled_brief_hire_for_open_positions_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_hire_for_open_positions_agent.py   # or on stdin
python3 scheduled_brief_hire_for_open_positions_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Hire for open positions Scheduled Email Brief — Builds a morning brief on hire for open positions from Dynamics 365 ERP data for a legal entity, returning top 5 items by impact, anomalies vs the 7-day rolling average, recommended next actions, an email saved to drafts

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-hire-for-open-positions
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_hire_for_open_positions',
    "version": '3.0.3',
    "display_name": 'Hire for open positions Scheduled Email Brief',
    "description": 'Builds a morning brief on hire for open positions from Dynamics 365 ERP data for a legal entity, returning top 5 items by impact, anomalies vs the 7-day rolling average, recommended next actions, an email saved to drafts',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'hire_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-hire-for-open-positions',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-hire-for-open-positions',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '3c55090618bf5c87',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/recruit-and-onboard-talent/hire-for-open-positions'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/scheduled-brief-hire-for-open-positions', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'owner': 'Responsible owner who receives the drafted email brief.', 'schedule': 'When the brief should run, e.g. weekday mornings at 7am.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Replaces a daily manual spreadsheet stitch with an automatic brief so owners walk into standup already knowing where hire for open positions stands.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': 'Using the Dynamics 365 ERP plugin against legal entity USMF, build a short morning brief on hire for open positions for the responsible owner. Include: (a) top 5 items by impact today, (b) any anomalies vs the 7-day rolling average, (c) recommended next actions. Draft an email to the owner (save to drafts, do not send). Also produce a Communications-ready summary suitable for a Teams channel post. This recipe is a strong candidate for a Cowork scheduled task - schedule for weekday mornings at 7am.', 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads hire for open positions, computes a short brief, drafts an email, and is a strong candidate for a Cowork scheduled task.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a morning brief on hire for open positions from Dynamics 365 ERP data for a legal entity, returning top 5 items by impact, anomalies vs the 7-day rolling average, recommended next actions, an email saved to drafts', 'example_request': 'Draft my 7am weekday hiring brief for open positions in USMF and email it to the owner as a draft.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Responsible owner who receives the drafted email brief.', 'name': 'owner'}, {'description': 'When the brief should run, e.g. weekday mornings at 7am.', 'name': 'schedule'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when an owner wants a recurring (daily/weekly, e.g. weekday 7am) hiring-for-open-positions brief drafted from D365 F&SCM data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ScheduledBriefHireForOpenPositions(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefHireForOpenPositions'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'owner': {'description': 'Responsible owner who receives the drafted email brief.', 'type': 'string'}, 'schedule': {'description': 'When the brief should run, e.g. weekday mornings at 7am.', 'type': 'string'}},
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
    print(ScheduledBriefHireForOpenPositions().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
