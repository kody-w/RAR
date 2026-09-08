---
name: "rar-cowork-cookbook-demo-data-create-a-case-from-a-channel"
description: "Generates 25 realistic demo 'create a case from a channel' records in a sandbox D365 legal entity (default USMF), stages them in an Excel workbook, creates them, and returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_create_a_case_from_a_channel", "rar_sha256": "e098a5645d8f82bd0129f54143556909bacc21fece2a840a1c6a0a69b98c5927", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_create_a_case_from_a_channel`. The original RAPP
agent is preserved byte-for-byte in `demo_data_create_a_case_from_a_channel_agent.py` and in the RCI capsule.

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

Create a case from a channel Demo Data Generator — Generates 25 realistic demo 'create a case from a channel' records in a sandbox D365 legal entity (default USMF), stages them in an Excel workbook, creates them, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-create-a-case-from-a-channel
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
      "description": "How many demo records to generate (default 25).",
      "type": "string"
    },
    "workbook_name": {
      "description": "Excel staging file name, e.g. demo-data-create-a-case-from-a-channel-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_create_a_case_from_a_channel_agent.py` and embedded as the fenced Python below (sha256 e098a5645d8f82bd…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_create_a_case_from_a_channel_agent.py` first:

```bash
python3 demo_data_create_a_case_from_a_channel_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_create_a_case_from_a_channel_agent.py   # or on stdin
python3 demo_data_create_a_case_from_a_channel_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Create a case from a channel Demo Data Generator — Generates 25 realistic demo 'create a case from a channel' records in a sandbox D365 legal entity (default USMF), stages them in an Excel workbook, creates them, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-create-a-case-from-a-channel
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_create_a_case_from_a_channel',
    "version": '3.0.3',
    "display_name": 'Create a case from a channel Demo Data Generator',
    "description": "Generates 25 realistic demo 'create a case from a channel' records in a sandbox D365 legal entity (default USMF), stages them in an Excel workbook, creates them, and returns each new record's primary key.",
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'case_to_resolution', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-create-a-case-from-a-channel',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-create-a-case-from-a-channel',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '6df4dc91c227fb54',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/intake-cases/create-a-case-from-a-channel'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/demo-data-create-a-case-from-a-channel', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Sandbox D365 legal entity to target (default USMF); must not be production.', 'record_count': 'How many demo records to generate (default 25).', 'workbook_name': 'Excel staging file name, e.g. demo-data-create-a-case-from-a-channel-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Eliminates the 'no data to demo with' blocker for trainers, implementation partners, and pilot programs by populating realistic but synthetic create a case from a channel data in minutes.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against a SANDBOX legal entity (default USMF), generate 25 realistic demo records for create a case from a channel. Use plausible values for every required field, vary the data so it looks organic, and stage them in an Excel workbook 'demo-data-create-a-case-from-a-channel-2026-05-24.xlsx' BEFORE creating. Then create the records in D365. After creation, output a confirmation list with each new record's primary key. WARNING: this recipe creates data - run in sandbox only, and never against a production legal entity.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates a configurable number of realistic create a case from a channel records and creates them via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Generates 25 realistic demo 'create a case from a channel' records in a sandbox D365 legal entity (default USMF), stages them in an Excel workbook, creates them, and returns each new record's primary key.", 'example_request': 'Generate 25 demo case-from-channel records in USMF sandbox, stage them in Excel, then create them in D365.', 'inputs': [{'description': 'Sandbox D365 legal entity to target (default USMF); must not be production.', 'name': 'legal_entity'}, {'description': 'How many demo records to generate (default 25).', 'name': 'record_count'}, {'description': 'Excel staging file name, e.g. demo-data-create-a-case-from-a-channel-2026-05-24.xlsx.', 'name': 'workbook_name'}], 'model': 'claude-opus-5', 'when_to_use': 'Use when you need demo/training data for case-from-channel scenarios in a sandbox D365 F&SCM tenant. Never run against production.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DemoDataCreateACaseFromAChannel(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataCreateACaseFromAChannel'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Sandbox D365 legal entity to target (default USMF); must not be production.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_count': {'description': 'How many demo records to generate (default 25).', 'type': 'string'}, 'workbook_name': {'description': 'Excel staging file name, e.g. demo-data-create-a-case-from-a-channel-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(DemoDataCreateACaseFromAChannel().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
