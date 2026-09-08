---
name: "rar-cowork-cookbook-demo-data-manage-and-implement-encryption"
description: "Generates 25 realistic demo records for manage-and-implement-encryption in a sandbox D365 F&SCM legal entity, stages them in an Excel workbook, creates them, and returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_manage_and_implement_encryption", "rar_sha256": "192db70408c63f7132062a8617e527e1a4f56a2147a2447bfe587d67109e7dab", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
