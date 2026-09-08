---
name: "rar-cowork-cookbook-demo-data-manage-and-implement-encryption"
description: "Generates 25 realistic demo records for manage-and-implement-encryption in a sandbox D365 F&SCM legal entity, stages them in an Excel workbook, creates them, and returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_manage_and_implement_encryption", "rar_sha256": "192db70408c63f7132062a8617e527e1a4f56a2147a2447bfe587d67109e7dab", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_manage_and_implement_encryption`. The original RAPP
agent is preserved byte-for-byte in `demo_data_manage_and_implement_encryption_agent.py` and in the RCI capsule.

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

Manage and implement encryption Demo Data Generator — Generates 25 realistic demo records for manage-and-implement-encryption in a sandbox D365 F&SCM legal entity, stages them in an Excel workbook, creates them, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-manage-and-implement-encryption
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
      "description": "Excel staging file name, e.g. demo-data-manage-and-implement-encryption-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_manage_and_implement_encryption_agent.py` and embedded as the fenced Python below (sha256 192db70408c63f71…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_manage_and_implement_encryption_agent.py` first:

```bash
python3 demo_data_manage_and_implement_encryption_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_manage_and_implement_encryption_agent.py   # or on stdin
python3 demo_data_manage_and_implement_encryption_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage and implement encryption Demo Data Generator — Generates 25 realistic demo records for manage-and-implement-encryption in a sandbox D365 F&SCM legal entity, stages them in an Excel workbook, creates them, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-manage-and-implement-encryption
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_manage_and_implement_encryption',
    "version": '3.0.3',
    "display_name": 'Manage and implement encryption Demo Data Generator',
    "description": "Generates 25 realistic demo records for manage-and-implement-encryption in a sandbox D365 F&SCM legal entity, stages them in an Excel workbook, creates them, and returns each new record's primary key.",
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
        "upstream_slug": 'demo-data-manage-and-implement-encryption',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-manage-and-implement-encryption',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'fab08f66b8bff4de',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-system-access-and-security/manage-and-implement-encryption'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/demo-data-manage-and-implement-encryption', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Sandbox D365 legal entity to target (default USMF); must not be production.', 'record_count': 'Number of demo records to generate (default 25).', 'workbook_name': 'Excel staging file name, e.g. demo-data-manage-and-implement-encryption-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Eliminates the 'no data to demo with' blocker for trainers, implementation partners, and pilot programs by populating realistic but synthetic manage and implement encryption data in minutes.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against a SANDBOX legal entity (default USMF), generate 25 realistic demo records for manage and implement encryption. Use plausible values for every required field, vary the data so it looks organic, and stage them in an Excel workbook 'demo-data-manage-and-implement-encryption-2026-05-24.xlsx' BEFORE creating. Then create the records in D365. After creation, output a confirmation list with each new record's primary key. WARNING: this recipe creates data - run in sandbox only, and never against a production legal entity.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates a configurable number of realistic manage and implement encryption records and creates them via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Generates 25 realistic demo records for manage-and-implement-encryption in a sandbox D365 F&SCM legal entity, stages them in an Excel workbook, creates them, and returns each new record's primary key.", 'example_request': 'Generate 25 encryption demo records in sandbox USMF, stage them in Excel first, then create them.', 'inputs': [{'description': 'Sandbox D365 legal entity to target (default USMF); must not be production.', 'name': 'legal_entity'}, {'description': 'Number of demo records to generate (default 25).', 'name': 'record_count'}, {'description': 'Excel staging file name, e.g. demo-data-manage-and-implement-encryption-2026-05-24.xlsx.', 'name': 'workbook_name'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need demo/training data for encryption management created in a sandbox D365 legal entity. Never run against production.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DemoDataManageAndImplementEncryption(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataManageAndImplementEncryption'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Sandbox D365 legal entity to target (default USMF); must not be production.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_count': {'description': 'Number of demo records to generate (default 25).', 'type': 'string'}, 'workbook_name': {'description': 'Excel staging file name, e.g. demo-data-manage-and-implement-encryption-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(DemoDataManageAndImplementEncryption().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
