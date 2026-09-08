---
name: "rar-cowork-cookbook-demo-data-configure-and-maintain-cloud-based-printing"
description: "Generates 25 realistic demo records for cloud-based printing configuration in a Dynamics 365 F&SCM sandbox legal entity, stages them in an Excel workbook, creates them, and returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_configure_and_maintain_cloud_based_printing", "rar_sha256": "35a2b4a979fe7072705d84652645c9a7624ddfe44a2d53fdb92699e2baf7bce8", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
