---
name: "rar-cowork-cookbook-scheduled-brief-manage-formulas"
description: "Builds a manage-formulas morning brief from Dynamics 365 F&SCM (legal entity USMF) with top 5 items by impact, anomalies vs the 7-day rolling average, and next actions; drafts an email to the owner and a Teams-ready summ"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_manage_formulas", "rar_sha256": "28b6d0a589716c8fe905397d01a432b7179269bb0af5b56643c383ca6264b237", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_manage_formulas`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_manage_formulas_agent.py` and in the RCI capsule.

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

Manage formulas Scheduled Email Brief — Builds a manage-formulas morning brief from Dynamics 365 F&SCM (legal entity USMF) with top 5 items by impact, anomalies vs the 7-day rolling average, and next actions; drafts an email to the owner and a Teams-ready summ

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-manage-formulas
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
    "owner": {
      "description": "Responsible owner who receives the drafted email brief.",
      "type": "string"
    },
    "schedule": {
      "description": "When to run, e.g. weekday mornings at 7am, daily or weekly.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_manage_formulas_agent.py` and embedded as the fenced Python below (sha256 28b6d0a589716c8f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_manage_formulas_agent.py` first:

```bash
python3 scheduled_brief_manage_formulas_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_manage_formulas_agent.py   # or on stdin
python3 scheduled_brief_manage_formulas_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage formulas Scheduled Email Brief — Builds a manage-formulas morning brief from Dynamics 365 F&SCM (legal entity USMF) with top 5 items by impact, anomalies vs the 7-day rolling average, and next actions; drafts an email to the owner and a Teams-ready summ

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-manage-formulas
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_manage_formulas',
    "version": '3.0.3',
    "display_name": 'Manage formulas Scheduled Email Brief',
    "description": 'Builds a manage-formulas morning brief from Dynamics 365 F&SCM (legal entity USMF) with top 5 items by impact, anomalies vs the 7-day rolling average, and next actions; drafts an email to the owner and a Teams-ready summ',
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
        "upstream_slug": 'scheduled-brief-manage-formulas',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-manage-formulas',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '195b68de26619f61',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['design-to-retire'], 'process_tags': ['design-to-retire/manage-active-products/manage-formulas'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'design-to-retire/scheduled-brief-manage-formulas', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to query; the recipe uses USMF.', 'owner': 'Responsible owner who receives the drafted email brief.', 'schedule': 'When to run, e.g. weekday mornings at 7am, daily or weekly.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Replaces a daily manual spreadsheet stitch with an automatic brief so owners walk into standup already knowing where manage formulas stands.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': 'Using the Dynamics 365 ERP plugin against legal entity USMF, build a short morning brief on manage formulas for the responsible owner. Include: (a) top 5 items by impact today, (b) any anomalies vs the 7-day rolling average, (c) recommended next actions. Draft an email to the owner (save to drafts, do not send). Also produce a Communications-ready summary suitable for a Teams channel post. This recipe is a strong candidate for a Cowork scheduled task - schedule for weekday mornings at 7am.', 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads manage formulas, computes a short brief, drafts an email, and is a strong candidate for a Cowork scheduled task.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a manage-formulas morning brief from Dynamics 365 F&SCM (legal entity USMF) with top 5 items by impact, anomalies vs the 7-day rolling average, and next actions; drafts an email to the owner and a Teams-ready summ', 'example_request': 'Give me the manage formulas morning brief for USMF and draft it to the owner.', 'inputs': [{'description': 'Dynamics 365 legal entity to query; the recipe uses USMF.', 'name': 'legal_entity'}, {'description': 'Responsible owner who receives the drafted email brief.', 'name': 'owner'}, {'description': 'When to run, e.g. weekday mornings at 7am, daily or weekly.', 'name': 'schedule'}], 'model': 'claude-opus-5', 'when_to_use': 'Call for a daily or weekly manage-formulas brief for the responsible owner, drafted as an unsent email plus a Teams channel post summary.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ScheduledBriefManageFormulas(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefManageFormulas'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to query; the recipe uses USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'owner': {'description': 'Responsible owner who receives the drafted email brief.', 'type': 'string'}, 'schedule': {'description': 'When to run, e.g. weekday mornings at 7am, daily or weekly.', 'type': 'string'}},
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
    print(ScheduledBriefManageFormulas().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
