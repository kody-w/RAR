---
name: "rar-cowork-cookbook-demo-data-configure-and-maintain-cloud-based-printing"
description: "Generates 25 realistic demo records for cloud-based printing configuration in a Dynamics 365 F&SCM sandbox legal entity, stages them in an Excel workbook, creates them, and returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_configure_and_maintain_cloud_based_printing", "rar_sha256": "35a2b4a979fe7072705d84652645c9a7624ddfe44a2d53fdb92699e2baf7bce8", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_configure_and_maintain_cloud_based_printing`. The original RAPP
agent is preserved byte-for-byte in `demo_data_configure_and_maintain_cloud_based_printing_agent.py` and in the RCI capsule.

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

Configure and maintain cloud-based printing Demo Data Generator — Generates 25 realistic demo records for cloud-based printing configuration in a Dynamics 365 F&SCM sandbox legal entity, stages them in an Excel workbook, creates them, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-configure-and-maintain-cloud-based-printing
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
      "description": "Excel staging file name, e.g. demo-data-configure-and-maintain-cloud-based-printing-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_configure_and_maintain_cloud_based_printing_agent.py` and embedded as the fenced Python below (sha256 35a2b4a979fe7072…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_configure_and_maintain_cloud_based_printing_agent.py` first:

```bash
python3 demo_data_configure_and_maintain_cloud_based_printing_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_configure_and_maintain_cloud_based_printing_agent.py   # or on stdin
python3 demo_data_configure_and_maintain_cloud_based_printing_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Configure and maintain cloud-based printing Demo Data Generator — Generates 25 realistic demo records for cloud-based printing configuration in a Dynamics 365 F&SCM sandbox legal entity, stages them in an Excel workbook, creates them, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-configure-and-maintain-cloud-based-printing
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_configure_and_maintain_cloud_based_printing',
    "version": '3.0.3',
    "display_name": 'Configure and maintain cloud-based printing Demo Data Generator',
    "description": "Generates 25 realistic demo records for cloud-based printing configuration in a Dynamics 365 F&SCM sandbox legal entity, stages them in an Excel workbook, creates them, and returns each new record's primary key.",
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
        "upstream_slug": 'demo-data-configure-and-maintain-cloud-based-printing',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-configure-and-maintain-cloud-based-printing',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '2f1e0a814249be92',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/administer-system-features/configure-and-maintain-cloud-based-printing'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/demo-data-configure-and-maintain-cloud-based-printing', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Sandbox D365 legal entity to target (default USMF); must not be production.', 'record_count': 'Number of demo records to generate (default 25).', 'workbook_name': 'Excel staging file name, e.g. demo-data-configure-and-maintain-cloud-based-printing-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Eliminates the 'no data to demo with' blocker for trainers, implementation partners, and pilot programs by populating realistic but synthetic configure and maintain cloud-based printing data in minutes.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against a SANDBOX legal entity (default USMF), generate 25 realistic demo records for configure and maintain cloud-based printing. Use plausible values for every required field, vary the data so it looks organic, and stage them in an Excel workbook 'demo-data-configure-and-maintain-cloud-based-printing-2026-05-24.xlsx' BEFORE creating. Then create the records in D365. After creation, output a confirmation list with each new record's primary key. WARNING: this recipe creates data - run in sandbox only, and never against a production legal entity.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates a configurable number of realistic configure and maintain cloud-based printing records and creates them via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Generates 25 realistic demo records for cloud-based printing configuration in a Dynamics 365 F&SCM sandbox legal entity, stages them in an Excel workbook, creates them, and returns each new record's primary key.", 'example_request': 'Generate 25 demo cloud-based printing records in USMF sandbox, stage them in Excel, then create them in D365.', 'inputs': [{'description': 'Sandbox D365 legal entity to target (default USMF); must not be production.', 'name': 'legal_entity'}, {'description': 'Number of demo records to generate (default 25).', 'name': 'record_count'}, {'description': 'Excel staging file name, e.g. demo-data-configure-and-maintain-cloud-based-printing-2026-05-24.xlsx.', 'name': 'workbook_name'}], 'model': 'claude-opus-5', 'when_to_use': 'Use when you need demo/training data for cloud-based printing setup in a D365 sandbox tenant; never run against a production legal entity.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DemoDataConfigureAndMaintainCloudBasedPrinting(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataConfigureAndMaintainCloudBasedPrinting'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Sandbox D365 legal entity to target (default USMF); must not be production.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_count': {'description': 'Number of demo records to generate (default 25).', 'type': 'string'}, 'workbook_name': {'description': 'Excel staging file name, e.g. demo-data-configure-and-maintain-cloud-based-printing-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(DemoDataConfigureAndMaintainCloudBasedPrinting().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
