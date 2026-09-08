---
name: "rar-cowork-cookbook-demo-data-track-campaign-expenses"
description: "Generates 25 realistic demo campaign-expense records against a sandbox D365 legal entity (default USMF), stages them in an Excel workbook first, creates them, then returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_track_campaign_expenses", "rar_sha256": "4c837c7c312d6c148f44aeb108cd483ff13b6c2612d15a2468bcf69334cb1320", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_track_campaign_expenses`. The original RAPP
agent is preserved byte-for-byte in `demo_data_track_campaign_expenses_agent.py` and in the RCI capsule.

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

Track campaign expenses Demo Data Generator — Generates 25 realistic demo campaign-expense records against a sandbox D365 legal entity (default USMF), stages them in an Excel workbook first, creates them, then returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-track-campaign-expenses
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
      "description": "Sandbox D365 legal entity to target (default USMF); must not be production.",
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
    "record_count": {
      "description": "Number of demo records to generate (default 25).",
      "type": "string"
    },
    "workbook_name": {
      "description": "Excel staging file name, e.g. demo-data-track-campaign-expenses-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_track_campaign_expenses_agent.py` and embedded as the fenced Python below (sha256 4c837c7c312d6c14…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_track_campaign_expenses_agent.py` first:

```bash
python3 demo_data_track_campaign_expenses_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_track_campaign_expenses_agent.py   # or on stdin
python3 demo_data_track_campaign_expenses_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Track campaign expenses Demo Data Generator — Generates 25 realistic demo campaign-expense records against a sandbox D365 legal entity (default USMF), stages them in an Excel workbook first, creates them, then returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-track-campaign-expenses
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_track_campaign_expenses',
    "version": '3.0.3',
    "display_name": 'Track campaign expenses Demo Data Generator',
    "description": "Generates 25 realistic demo campaign-expense records against a sandbox D365 legal entity (default USMF), stages them in an Excel workbook first, creates them, then returns each new record's primary key.",
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'concept_to_market', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-track-campaign-expenses',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-track-campaign-expenses',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '2ce9b6ee152ea7ce',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/manage-marketing-campaigns/track-campaign-expenses'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/demo-data-track-campaign-expenses', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Sandbox D365 legal entity to target (default USMF); must not be production.', 'record_count': 'Number of demo records to generate (default 25).', 'workbook_name': 'Excel staging file name, e.g. demo-data-track-campaign-expenses-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Eliminates the 'no data to demo with' blocker for trainers, implementation partners, and pilot programs by populating realistic but synthetic track campaign expenses data in minutes.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against a SANDBOX legal entity (default USMF), generate 25 realistic demo records for track campaign expenses. Use plausible values for every required field, vary the data so it looks organic, and stage them in an Excel workbook 'demo-data-track-campaign-expenses-2026-05-24.xlsx' BEFORE creating. Then create the records in D365. After creation, output a confirmation list with each new record's primary key. WARNING: this recipe creates data - run in sandbox only, and never against a production legal entity.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates a configurable number of realistic track campaign expenses records and creates them via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Generates 25 realistic demo campaign-expense records against a sandbox D365 legal entity (default USMF), stages them in an Excel workbook first, creates them, then returns each new record's primary key.", 'example_request': 'Generate 25 demo campaign expense records in the USMF sandbox, stage them in Excel first, then create them in D365.', 'inputs': [{'description': 'Sandbox D365 legal entity to target (default USMF); must not be production.', 'name': 'legal_entity'}, {'description': 'Number of demo records to generate (default 25).', 'name': 'record_count'}, {'description': 'Excel staging file name, e.g. demo-data-track-campaign-expenses-2026-05-24.xlsx.', 'name': 'workbook_name'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need demo/training campaign expense data created in a D365 F&SCM sandbox legal entity — never against production.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DemoDataTrackCampaignExpenses(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataTrackCampaignExpenses'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Sandbox D365 legal entity to target (default USMF); must not be production.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_count': {'description': 'Number of demo records to generate (default 25).', 'type': 'string'}, 'workbook_name': {'description': 'Excel staging file name, e.g. demo-data-track-campaign-expenses-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(DemoDataTrackCampaignExpenses().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
