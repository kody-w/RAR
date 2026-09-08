---
name: "rar-cowork-cookbook-scheduled-brief-manage-formulas"
description: "Builds a manage-formulas morning brief from Dynamics 365 F&SCM (legal entity USMF) with top 5 items by impact, anomalies vs the 7-day rolling average, and next actions; drafts an email to the owner and a Teams-ready summ"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_manage_formulas", "rar_sha256": "28b6d0a589716c8fe905397d01a432b7179269bb0af5b56643c383ca6264b237", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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
