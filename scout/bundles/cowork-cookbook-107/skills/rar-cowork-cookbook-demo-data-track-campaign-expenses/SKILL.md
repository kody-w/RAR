---
name: "rar-cowork-cookbook-demo-data-track-campaign-expenses"
description: "Generates 25 realistic demo campaign-expense records against a sandbox D365 legal entity (default USMF), stages them in an Excel workbook first, creates them, then returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_track_campaign_expenses", "rar_sha256": "4c837c7c312d6c148f44aeb108cd483ff13b6c2612d15a2468bcf69334cb1320", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
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
