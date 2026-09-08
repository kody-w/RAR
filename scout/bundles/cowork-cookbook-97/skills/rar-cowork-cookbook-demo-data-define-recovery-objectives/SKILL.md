---
name: "rar-cowork-cookbook-demo-data-define-recovery-objectives"
description: "Generates 25 realistic demo records for define recovery objectives in a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook, creates them, and returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_define_recovery_objectives", "rar_sha256": "a3bcd226ec0272b7a1bce86470e7f2f1d48158be6118a95aa1292de1d14deb4f", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_define_recovery_objectives`. The original RAPP
agent is preserved byte-for-byte in `demo_data_define_recovery_objectives_agent.py` and in the RCI capsule.

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

Define recovery objectives Demo Data Generator — Generates 25 realistic demo records for define recovery objectives in a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook, creates them, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-define-recovery-objectives
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
      "description": "Sandbox D365 legal entity to write into; defaults to USMF.",
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
      "description": "How many demo records to generate; defaults to 25.",
      "type": "string"
    },
    "workbook_name": {
      "description": "Excel staging file name, e.g. demo-data-define-recovery-objectives-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_define_recovery_objectives_agent.py` and embedded as the fenced Python below (sha256 a3bcd226ec0272b7…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_define_recovery_objectives_agent.py` first:

```bash
python3 demo_data_define_recovery_objectives_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_define_recovery_objectives_agent.py   # or on stdin
python3 demo_data_define_recovery_objectives_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define recovery objectives Demo Data Generator — Generates 25 realistic demo records for define recovery objectives in a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook, creates them, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-define-recovery-objectives
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_define_recovery_objectives',
    "version": '3.0.3',
    "display_name": 'Define recovery objectives Demo Data Generator',
    "description": "Generates 25 realistic demo records for define recovery objectives in a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook, creates them, and returns each new record's primary key.",
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-define-recovery-objectives',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-define-recovery-objectives',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'e804a3e8de4f9f1b',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/define-business-continuity-plan/define-recovery-objectives'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/demo-data-define-recovery-objectives', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Sandbox D365 legal entity to write into; defaults to USMF.', 'record_count': 'How many demo records to generate; defaults to 25.', 'workbook_name': 'Excel staging file name, e.g. demo-data-define-recovery-objectives-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Eliminates the 'no data to demo with' blocker for trainers, implementation partners, and pilot programs by populating realistic but synthetic define recovery objectives data in minutes.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against a SANDBOX legal entity (default USMF), generate 25 realistic demo records for define recovery objectives. Use plausible values for every required field, vary the data so it looks organic, and stage them in an Excel workbook 'demo-data-define-recovery-objectives-2026-05-24.xlsx' BEFORE creating. Then create the records in D365. After creation, output a confirmation list with each new record's primary key. WARNING: this recipe creates data - run in sandbox only, and never against a production legal entity.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates a configurable number of realistic define recovery objectives records and creates them via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Generates 25 realistic demo records for define recovery objectives in a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook, creates them, and returns each new record's primary key.", 'example_request': 'Generate 25 demo records for define recovery objectives in the USMF sandbox and stage them in Excel first.', 'inputs': [{'description': 'Sandbox D365 legal entity to write into; defaults to USMF.', 'name': 'legal_entity'}, {'description': 'How many demo records to generate; defaults to 25.', 'name': 'record_count'}, {'description': 'Excel staging file name, e.g. demo-data-define-recovery-objectives-2026-05-24.xlsx.', 'name': 'workbook_name'}], 'model': 'claude-opus-5', 'when_to_use': 'Use when you need seeded demo data for define recovery objectives in a sandbox tenant for training or pilot scenarios. Never run against production.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DemoDataDefineRecoveryObjectives(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataDefineRecoveryObjectives'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Sandbox D365 legal entity to write into; defaults to USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_count': {'description': 'How many demo records to generate; defaults to 25.', 'type': 'string'}, 'workbook_name': {'description': 'Excel staging file name, e.g. demo-data-define-recovery-objectives-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(DemoDataDefineRecoveryObjectives().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
