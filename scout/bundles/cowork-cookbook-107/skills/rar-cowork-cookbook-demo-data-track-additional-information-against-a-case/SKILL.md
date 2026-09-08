---
name: "rar-cowork-cookbook-demo-data-track-additional-information-against-a-case"
description: "Generates 25 realistic demo case-additional-information records in a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook first, creates them, and returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_track_additional_information_against_a_case", "rar_sha256": "678d021f0cd1e666d0ab3f0b1e9903af7cdfc7773f675d00d6f8294ef2acab75", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_track_additional_information_against_a_case`. The original RAPP
agent is preserved byte-for-byte in `demo_data_track_additional_information_against_a_case_agent.py` and in the RCI capsule.

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

Track additional information against a case Demo Data Generator — Generates 25 realistic demo case-additional-information records in a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook first, creates them, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-track-additional-information-against-a-case
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
      "description": "Sandbox D365 legal entity to create records in (default USMF).",
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
      "description": "Excel staging file name, e.g. demo-data-track-additional-information-against-a-case-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_track_additional_information_against_a_case_agent.py` and embedded as the fenced Python below (sha256 678d021f0cd1e666…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_track_additional_information_against_a_case_agent.py` first:

```bash
python3 demo_data_track_additional_information_against_a_case_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_track_additional_information_against_a_case_agent.py   # or on stdin
python3 demo_data_track_additional_information_against_a_case_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Track additional information against a case Demo Data Generator — Generates 25 realistic demo case-additional-information records in a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook first, creates them, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-track-additional-information-against-a-case
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_track_additional_information_against_a_case',
    "version": '3.0.3',
    "display_name": 'Track additional information against a case Demo Data Generator',
    "description": "Generates 25 realistic demo case-additional-information records in a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook first, creates them, and returns each new record's primary key.",
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
        "upstream_slug": 'demo-data-track-additional-information-against-a-case',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-track-additional-information-against-a-case',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'a1d6d67f357c4387',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/manage-and-work-on-cases/track-additional-information-against-a-case'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/demo-data-track-additional-information-against-a-case', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Sandbox D365 legal entity to create records in (default USMF).', 'record_count': 'How many demo records to generate (default 25).', 'workbook_name': 'Excel staging file name, e.g. demo-data-track-additional-information-against-a-case-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Eliminates the 'no data to demo with' blocker for trainers, implementation partners, and pilot programs by populating realistic but synthetic track additional information against a case data in minutes.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against a SANDBOX legal entity (default USMF), generate 25 realistic demo records for track additional information against a case. Use plausible values for every required field, vary the data so it looks organic, and stage them in an Excel workbook 'demo-data-track-additional-information-against-a-case-2026-05-24.xlsx' BEFORE creating. Then create the records in D365. After creation, output a confirmation list with each new record's primary key. WARNING: this recipe creates data - run in sandbox only, and never against a production legal entity.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates a configurable number of realistic track additional information against a case records and creates them via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Generates 25 realistic demo case-additional-information records in a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook first, creates them, and returns each new record's primary key.", 'example_request': "Generate 25 demo 'additional info against a case' records in USMF sandbox, stage to Excel first, then create them.", 'inputs': [{'description': 'Sandbox D365 legal entity to create records in (default USMF).', 'name': 'legal_entity'}, {'description': 'How many demo records to generate (default 25).', 'name': 'record_count'}, {'description': 'Excel staging file name, e.g. demo-data-track-additional-information-against-a-case-2026-05-24.xlsx.', 'name': 'workbook_name'}], 'model': 'claude-opus-5', 'when_to_use': 'Use when you need sandbox demo/training data for tracking additional information against a case in Dynamics 365 F&SCM. Never run against production.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DemoDataTrackAdditionalInformationAgainstACase(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataTrackAdditionalInformationAgainstACase'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Sandbox D365 legal entity to create records in (default USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_count': {'description': 'How many demo records to generate (default 25).', 'type': 'string'}, 'workbook_name': {'description': 'Excel staging file name, e.g. demo-data-track-additional-information-against-a-case-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(DemoDataTrackAdditionalInformationAgainstACase().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
