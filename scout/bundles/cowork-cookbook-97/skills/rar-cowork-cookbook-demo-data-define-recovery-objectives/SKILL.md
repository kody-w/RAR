---
name: "rar-cowork-cookbook-demo-data-define-recovery-objectives"
description: "Generates 25 realistic demo records for define recovery objectives in a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook, creates them, and returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_define_recovery_objectives", "rar_sha256": "a3bcd226ec0272b7a1bce86470e7f2f1d48158be6118a95aa1292de1d14deb4f", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
