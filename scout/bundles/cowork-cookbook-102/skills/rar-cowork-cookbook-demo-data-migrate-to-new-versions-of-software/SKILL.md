---
name: "rar-cowork-cookbook-demo-data-migrate-to-new-versions-of-software"
description: "Generates 25 realistic demo records for software-version migration in a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook, creates them, and returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_migrate_to_new_versions_of_software", "rar_sha256": "d7facdf8523ba5f4ad60f5375fd353a180e5ae4c6b34da591b9cc22df389b3cf", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_migrate_to_new_versions_of_software`. The original RAPP
agent is preserved byte-for-byte in `demo_data_migrate_to_new_versions_of_software_agent.py` and in the RCI capsule.

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

Migrate to new versions of software Demo Data Generator — Generates 25 realistic demo records for software-version migration in a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook, creates them, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-migrate-to-new-versions-of-software
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
      "description": "Sandbox D365 legal entity to write into (default USMF); must not be production.",
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
    "scenario": {
      "description": "The demo topic/scope, here: migrate to new versions of software.",
      "type": "string"
    },
    "workbook_name": {
      "description": "Excel staging file name, e.g. demo-data-migrate-to-new-versions-of-software-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_migrate_to_new_versions_of_software_agent.py` and embedded as the fenced Python below (sha256 d7facdf8523ba5f4…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_migrate_to_new_versions_of_software_agent.py` first:

```bash
python3 demo_data_migrate_to_new_versions_of_software_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_migrate_to_new_versions_of_software_agent.py   # or on stdin
python3 demo_data_migrate_to_new_versions_of_software_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Migrate to new versions of software Demo Data Generator — Generates 25 realistic demo records for software-version migration in a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook, creates them, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-migrate-to-new-versions-of-software
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_migrate_to_new_versions_of_software',
    "version": '3.0.3',
    "display_name": 'Migrate to new versions of software Demo Data Generator',
    "description": "Generates 25 realistic demo records for software-version migration in a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook, creates them, and returns each new record's primary key.",
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
        "upstream_slug": 'demo-data-migrate-to-new-versions-of-software',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-migrate-to-new-versions-of-software',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'fc3e7311aee0b567',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/uptake-software-releases/migrate-to-new-versions-of-software'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/demo-data-migrate-to-new-versions-of-software', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Sandbox D365 legal entity to write into (default USMF); must not be production.', 'record_count': 'Number of demo records to generate (default 25).', 'scenario': 'The demo topic/scope, here: migrate to new versions of software.', 'workbook_name': 'Excel staging file name, e.g. demo-data-migrate-to-new-versions-of-software-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Eliminates the 'no data to demo with' blocker for trainers, implementation partners, and pilot programs by populating realistic but synthetic migrate to new versions of software data in minutes.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against a SANDBOX legal entity (default USMF), generate 25 realistic demo records for migrate to new versions of software. Use plausible values for every required field, vary the data so it looks organic, and stage them in an Excel workbook 'demo-data-migrate-to-new-versions-of-software-2026-05-24.xlsx' BEFORE creating. Then create the records in D365. After creation, output a confirmation list with each new record's primary key. WARNING: this recipe creates data - run in sandbox only, and never against a production legal entity.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates a configurable number of realistic migrate to new versions of software records and creates them via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Generates 25 realistic demo records for software-version migration in a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook, creates them, and returns each new record's primary key.", 'example_request': 'Generate 25 demo records for software version migration in sandbox USMF, stage them in Excel, then create them in D365.', 'inputs': [{'description': 'Sandbox D365 legal entity to write into (default USMF); must not be production.', 'name': 'legal_entity'}, {'description': 'Number of demo records to generate (default 25).', 'name': 'record_count'}, {'description': 'Excel staging file name, e.g. demo-data-migrate-to-new-versions-of-software-2026-05-24.xlsx.', 'name': 'workbook_name'}, {'description': 'The demo topic/scope, here: migrate to new versions of software.', 'name': 'scenario'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need sandbox-only demo/training data for a migrate-to-new-software-versions scenario in Dynamics 365 F&SCM. Never run against production.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DemoDataMigrateToNewVersionsOfSoftware(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataMigrateToNewVersionsOfSoftware'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Sandbox D365 legal entity to write into (default USMF); must not be production.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_count': {'description': 'Number of demo records to generate (default 25).', 'type': 'string'}, 'scenario': {'description': 'The demo topic/scope, here: migrate to new versions of software.', 'type': 'string'}, 'workbook_name': {'description': 'Excel staging file name, e.g. demo-data-migrate-to-new-versions-of-software-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(DemoDataMigrateToNewVersionsOfSoftware().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916ebObWJbnV9G8jpjMbNlmEyC5oiIGBEgCLawCKV3hZN/3nez67nOR9OzMqqzuyZ75a+TwE8u9Zz+/c47g1zezbYK8evv8prhmttiZSRIGbrUwM2exzfu8isFXHlvg/8LOs6YKrbbJq/rtw5vj1nYVFk2YZ2D7zs3cymzceoHii8o1k7BuQnvhuGkOTu28cuqFl1eLOvea3qzcj51b1WDrIg19sG8+CrOFuagBZysfFgxG4Avufyrb0yJxfTNZuFkTNuPiR8f1zDZpFppy4n76sKgb0wdMm8BNHwSyBTvYbrKYRZ+l/rCwgTTNa8mHh2KV27RVVi9c0w4Wmdu/BPyhXhRVmJrVuIjd8RNQ0R3MtEjc+u3zz3/78BaC47fPv77ZiVmDS28M0I0xG/P00MBV87PbX59a1RdPeSkKyCRm5oP1xQhMnYHzwq2AKVJwCSizeJ39WLuJ92Hx7/8eg11+/dPnL9ni9fnyNv+T22zWYdHkZt24zsI2C9MKE2CUTwsq6c2x/qYYMCPwVOZ/eu78TikvFn+d7/34ZPLJd5sfv7zlhft0wZe3nxbAR1/eqnY+/jRTKX786VOS927140/f6dStFbl2MxMDUn/6+jp/kQULvy8NvcVXRWS3L17A1GHhAuK/0W/+PEV/kXuZ5Otz8Y958WHxx5Rnff4K5H3GogXo/jFZYAOw8+1TlIfZjy8eVd65mZnZ7o8//SuyduDa8RzJ/0d0f34SDlzTAdZ6mQSE6OyCvy2WL92+0fzXbAsQMH9GE7D8nd03Q/0r2g/P/gPpJMxAfrz78g/J/dGG5V8XP/9L3f6zDR8W3heQPUkIMMC0Evfz4tdHiPz8g/P94g9/+zsg/V+SUfK2sh8UvqZmFnpu3Xz9+vMP9ePyD3/7+Ye2AFHsmunXtkr+iOYf2fXB53cWfK368fd7AX8ti7O8zxbfcmjxa178j+rvnxZXgIHO9+v158VvM3H+LBezEu9Mnyb4TTbWQNbf2PGnt78DDMqANq39uA3w49/+bXEK7SqfUXWh2HnbLICDmzB1Z+HVIKwX4QP5gAIPwAWGfa0D8T97eJY49xa//C/7gfYf7RfaQzNyf3UAvH19IrT7tcm/ArD8+gLu+mvufX1H818+LVTAJK9CP8wAWMuUKH7JADJnzSxAUbm1W3UAtKyxcT+C3P44H8yA/cuf4vP1QfJTMf7yAPLwiYjy9jCjYd0m7qdZbz1ws5eWNigI7uDaLeCW5DYQzQsBoH8A9qjzpANoOtuojsMkWTghwBtQ3MZnkWizzzOxX375xTLr4Ev2hG9s8ax6NQQWfBNn8fEj0NFLQj9ovmSuHeSLH379+w+L/1j8Z7sexGceIigoLy8BCXnlcl6ArGtTsAw4ELgcQMrDS7/+/WVpQAbU2wWwUeiFz+I2Z0fsOu9mV/bURxQnFpYLzA1MnRZ51YCasAibT4uDt/gmL2A635qrRpDXDSjZhZs5bmaPgKoJ1PlmySxvQH1uwtobPyza2n1w/cWqzIeIKUh/s/llcdqKoEblCfgzi/lYBDbnWQjM/y0ontcBkQqUXfqdxKfFeY7TRWFWZhFU5ouHZz79AmrT+3ZA3Jxr95dsLsvubKpH0jzN48/dyNx+PFz6cfY5aF9SgBBO/c7bf3UszkJ9VNTqS1a/EgJE2qMnAKKMC78NnblM/OUVUnWQt4nzsB+QdKb08oLz8sojBl9NwWyEucN4D+bZi+/BvJgbiMXcQSxe3dNce1sURlaL///aqdko1G4nsztKZZkFe1bl29NZc185O/XZis5SzZo9EvN7j/OOY+9w/iVLQhB51fiX58qHi19rnhDZVsAjMiU/6IP4As6a6T7Cfw7nqpoTx/ySvdcNoM27n2asALk0e++d4Xz3XdIAAMJ8/r2HeOk82wOE+KJorQS4y3NdxzLtGEhVzSn8ci7IBXcOhD4IgcV+q9XsFmAvQH8xexAkJagtn75h+fPuu+i/2/hsleYtjzayBRlcPQgAOdxZwNlTfdgAIDObZxsP9Pz8IALUSItm1t0CoQM0fV50K7dswzpsZrx82tUtAHB/nL+fms5X3aEAaQOMBZKjaIF1H+k0I00KGiEgA4hakF1pmD1j+GWEB0EznbEBYO8rhp4UH5dfCrmPHJwr2vvGWZF5z9wkLDwgOrgy/hZC1D8KE0AvnVc8+P5jpH3jNtOeYbQGUAg4vt99dhOfng3Bs+NYvNP9/E9z0o9/bpR6lHjt9wHweRE0TVF/hqBnWX6vyp8AiEFPWetHhf44V86Pr8r5sck/gvx7x4L6Y+59fAeI3zF56v958ecE/R2JF4/PC+QT/Amebx1fgfb6ALtsP9K3j6v57pdMdr/jLWCfpyDSZi+OoCX4Vhzfl4AK6VcApsDiZ7Gs5xrbg7L+qA7AJV+y30b+nHmg+GT+HKl1/htEeHQJIAueHvxWxMCtrAG8nbnb9N151nvkSe2+fc7aJPnwloEY/DMz3lyx0jnO63lEBBkFurgmdB9nD9gYmvnw90Pz5XFgJp9AKQAQldS/jcVXnZnr7G9S5qkt0NIGHD4snAcWgzAF2s7M53Qz6/hRHGatmrGY1XiOg3MD+UD/r0/0/2eBlN+Wi98VCoCEPcgY91l6f182/rJIW9A4zJa1HmjiPDvUPxTgW3v7z9x10D/MjJz881xKP7yACXyDkQRUnvfpAqj9mvceQ3rWglH653mymf3w2DIfgD3g69umb79YWO7b3/5Arqdhv4ISn/2Bp85taoHIA6D9uxIMhH2P2e82QfGf/lDzGgSYWYX5P1OfEetBt8mL0IZevgU5CQab9L9uJP6Q23vF/vqM5H9k+Szrc7mfkfqRK/PCDwv3k/9p8aeg5SMKo8RHGP+Irj4NST38gTgP+4JiAkry7KrvMfDdE/lj4JwlB55rnr+P/PoGUsqc5Xgl1WtiAcsB9n6s534MAgAEGILzJ1SAe/93s8yLWB2YoH2ef6MhQfvpeGscxSwT91amQ8AejpG452A4ZiJr2MVNd2UTFrZyTHyDWBvbRlHHw9YbC7M9QO+JPl/nDjScBcQ3pAdvNqi3QlDYAXGDrhxnTawJGydR2NwAPha+Ma3vW+Mwc15aP7WcTfptrJqt81L+1zeLWIGV+1V9oJ6fLbRELAIlLYW3lhXh5rhEHwXlLBOeEtMIhYYwXvO939vSgcQs+BwRtHRnkzAdj/fu7MsMJU6seGHXo0pm1/P1zu9Ca2tPxB2+WzRDsUmCEI2CexdH4W1noNNl5LiEoRVKoVwUpOV5nDWv/MERrsKZv7oulmnBdLSU8gI5B6NCtfCkTufBgZbrxJtU2QrH60VWpuUljA6CzEaMPaSxew0PnH0zpeB8NvQB17xc4+2DEdyX7Agp6kUk0ZbwQsRYunsSvtbXiazvNL+7a+RJmpKxhEKtG3qos67mdhTgZBPBxiFq4N5nFdejgvRITApkCFaBX312JViatL7d2IPg1XU5HJfxfrchiltDNTJ/3+sT5IVai697k+GIjZfh6Nrr9gHOhXa2X62Wm1jdT3eF3iWKH2TBdaml0y3O0MTFQymXl3wKRTue4LrdNq9LgW2bjsZ28MTu8VQuV2HKF0FKU9yNCna3cuJQ54Tla1/d3qzkjq+0Fd9nsXfzJ+i2jFM4jnU+k30uVP3zMWItMxKP8LVj8PWtO3fSZtycqtQL+IN4XSryjRGFpX5SFSSOeHtZs4lLCVzM62ZxiGPyuukOcSRg/rKgsMPW0namAO2zS74/iA3TIkzH2GhtXvPVqMjnuKPLo+AnydSItB+qusJAhmbF9+VOv8vrVjjuxN35xEDnsClguLttSTPf14UNJQUnS9I1IrX1Xb3fydCCE9I5MEs9U6lbEvCyfr/e6ZLeKPveNKuToTOr2NN3ebFGUU04tgmmngavb89LjKuj3V0SN1cr1umcX28lnM1YcYVhyYbpt+EUjRqxngROOR3lK98oyLZhTNin3TptjI1WsJecUEaYr7VySLHgXiSSrdSBF2bMWpAwLY2S40hBA4/KGbvmpq2EEEyH+kwvixwZUONuuK/TwI5gcQwqb3dHeTm51mMKr6iMzkqXI1Sr1AU45Y+GCgvUwMp4gwOpJOVyL8ZlKihVqLFbt0eRDZ6tRObebLOSS71o5y77zVDUkGmLCjRu1XydHbPRgfpTR6fXoUKpoiAM6diPx4S05ZFf5X5ECmPK58EWW24mn+N2h1GMWSu4q+2KTvBIux65nrlPdkX7q9Gp6ho0/N7oNvEprQZpb8Kp0tASZ4RakvirKOYaJpdWvmvRt91h4x1P8mSrF19VA45imCm7J70dQUe+ni4c06BDW2woX+R0yCELU+Fhma/u8c7U9eh8PBUwZcPAZzed0IvgfDmXZpc7rNfrWofpIrWMDnm3wWyh3uTGkI+3LLGjq1YTkAFLA5pwuhocSZGpMd8XGFq/ey3HKtdqu9qrkn5CBOK2ZNuyPwb56OvUqae8ZXrvY5K40jXleRxDG/7IT+fDCb9h3c1XqPh0l5s7drxKaZ2LQk7QN0mQjqnutcb+pN/EnpgMFz6jzWXy0i7RINm+cru4s0X4HOjbO3GjpCltlV4H2RYebbxC1358izXlIBwle+mQp24q4HAZSvs0ylfeUq3GjsLhTGzzvKX8SDga6y21ZOWlJW27ATtOMn23oVu+3Hlp4+sNE/Y6x5IWSjEC3Kf2yfLZUt0I3A1OEE0LBunWT4OZ3ElUN+7YSdisdS7ZMkqygsJdhx8DvACYkCcUXwKtyG4FPpJDLfO77moDY/XMsER4OSKOh5LUz5fl1B9RA+7gk8exPnHFjn1IXLYigJ4oFnhVU7l95bIrJOc8o9iyMSPcUY0oKpnaiwVVQZfrWUJNOarxNjh04nC/0exwZG5s0Kq91/pRSew0GfGLCfYTNs0OdOehk+SI/M0mClSwNY0Po+2+22euetBKalta6miQ5X5XdLqMFtuTIO8TTuPPNphqrhO74oPOXU36PlaGRGioi6KjIpwWVqAvq86sJJrIg9uZu2xA472JNnrFb8M1ANr27G8uURJzpwTbERnHL88ipqbERYWhk+qXtH0PM3RrTvipLNgckqBCSwnMFKUbTsc+cpqwrk0oinT1zJLkIB5Lzugrb4qazWa9gjvcFTO4nTZluxHUjC5xF4xhcQgfDpR3Z4OSShFnabDRFk1DJPSPbIHDJNp76W5XlqRxoqvUCjk2JrF0rOJc0PqsaEDcsPZFOMiNdhP93U7tI+Z6D/3wuD9oy0gupEiVqWgU6VOAN/fbNjb3AUxUlSh1dxeNYmTawSHko/5mIJi4SsuhuSnC0RwvEkr2nTMkeCYbhelHB2jPMxWU3yF2PFBXpO9Gv82nMPWc5YqSlbuVwJdrLXA4f6uZeGUmgnKatpvWYCB/x5ZWvpVBkh2OU6z6yJJ0dlXpYKhAwZlF+YZGG2Nb+bGXQWUOy11MHqOLlPHGIT7eOWOZ6MvYH2Og7BXh3IQ/UUkpg7SyBVpCr0dU1LzxdjqGna/GEc5Ssj3ysRCKAdR53BHnLkl/cxB5dztLtYacgnJvjCLD6RuW5By+Pu/h28kubomkD1qwmdZ1GXGH4Wxn4pXv99I294MxXzsmt+60JApCerUfLCmhw0Cgz922tZPgUG7C7TU47hqBxDNlkJg1N5yiXXgwrL3CVq3BjY5hhYf7dn07KPL6Ut0KVslA+b9R2/CEE5UQIVfuGvDhLUT1e2msQm3jxpxIBzxK2TSUru7XIwup60QTdgzG27i0Udm4yIu4LxF255rF7bhjtgKl78qMAFPsWtdhKTiVjnzCrSUsb0W5pNucgcjjGmEZhvJqJUnE7W17ZtBzrYcl78h7DFmmKx0fRV2jjxu1N3aYxY5Lduh6UFvHxNttrPyAH3sIWe22ut8wAeRhPLwyo2Dq+nuy628ZIfFh6aE7P7wfMzs1z1LKGMaZ4c8sdILjLcdPFFTB2p4T7ml2dAMu2OUUQviQxJ1F6MaLGF33HKdf2mwUsdNmG60mzk7o8za4VV1199fs2jML7aqCEKZ7MxQGblreIarHBUdTLlrvAlDlS2ETXNp7TIqYFLK7JsYvu81x5YzVKcd7jl/rNVYMbe4oDoVKHL3V+4oPBbXIoSNrSfsI1HFVTzrJsM/oHoKw0KYbXWc4ZI8IiSCUN49wUVKmySy/aMMa9FTXgUtIRfIKbmN7G/nYXnsKAgMFq+XTcn9OpLjYes2ljXOKVUzkIETDldBUhLgKe3GCsGbKqZKmLyiW7RGz9lwimEYyt+GzeSaFYKvfmJVmucb1hNLVtqZk9CTbSczvdDqyBXO7TPilbSfIsRPPgQmScuj5aYmZTWJcqYTobDw8Sk2BRl5zsujdtD3DdKKoRH0RevySrLaFKSWIBCaHFEZDgi6NrXZttXMe30TG0zIVdk75iqmWWKrB2bQFYHWn4h1TOquCjfjburOWgb9XT4SGcVPCXjkjvgrpFCK8U5S05KaN6HH3QzYNOHRRyNG9ZDHoadYMyQ2KJ3YmOm0Tsysb0GpaaulYJtM25XLdXoQ1RKgXVnBvcs72MaL0cnhUrYM9ns9O7SpppVdjEmX7o6nWW9odePqsQ1J9083EjQ9pRVEyUtkZvD0I01mopRr2d+rtxPrbVDBuAkI4NSML0y0kgiFOZD9Fzqg2HeqEgjZ7qCxDMH86eNSGp6zurzduoCtSqpUNjYoZcy2o1bTWCooNkWt1Tlu3a73l0d4by1WnrnCrg1qr5q5Gp2N3tAvIUFwKe1+m6VQJkKJJDog+6a1jX7jN9hwdzuz1bDa5gPag+t1oSeXsCKULUnHkfDfKKarsXVTxUMXIlyVVGQWxdjMHzaOiYbcENsmi4x4vUk0wV0VL+ybQJA1e+lJiGm3WX+q8GivvkLOloUBzc9Pt1ZAU1TPhdo4pVKzTw1Dio+xYHk0DU2+CxMpssnduklWotoRuDuRlKAxCH0tyAv2z3LplR9zXan0OkWPkHNELb7mWIqBkcyplTNY5ylOxhA+RPe+MyA0qQ9I+iwToLq1Tr+SSlWVaWo1HIkrTMzO0d7vpQm6VB8zFPWh3v5aGbERYVzTios8DrAqzkZliWrtwBw6mfaVy0/1Sx8FsNWmnJSQfILOLs2LFSyUk9KGTnZdNOEBtfzz3k3EpT8P9EJ0uGuTgTVp7JnW+XSn8fCAyRr+c78zpfLztxm5HdEuhXAfGLi2qIVdk7k5tjG2P6+EFqWCBB3BS8jHkLCODzoWuhMicJjvCOtdUUYu+htM3VuQOxfqocU7vYDxWYHfovqsOa7IE6bvGUz+SJ2sX8dptqHeGGZkdaOArnLNSD4C0bdFqZ+lQIcTjQHe8QW+G46Zcp9IA16S5jCJcXiq7e6URONkna5a6gy7GzQgRFQsEPVBotoEduKnrxuupLMfDQbheJTZrVLWhDzo1re+8viTYMCNWCneixqFzkeRwX61whab7nb0NdLgJaJxr2FuTa7UWxdupiFUZPvHS0lsPoPCeBLNKjnAQceQOQi6mb1bGBbbKy/GsrOz1RtoifCVD14A4hooadgjsmvsNJ7sQ4SPQDkeqQlta5xxpfS+6nFZ3czDFIdM62Vnv2RM6qIRd4dDubqHLaUCrFj3AzgZl7TY/M9F9aV2T7pDRk6GsJquamn3XWcWGNUjc6ska0wkUT/LO7S4rWLDI9KZV5mVaRghiLMPVZXcFba+4Ye+qM5KDxq8ctLWIvQwaFo9xnUNzNW+gpbiCUUyW1XJlHtsAUoY1fUImISBU3WavSzHtqOy65w80PF5oaq/sA96VlaO+bI6d0qNCdoRYcXuPNyMSNiGxVqqs1Mn9DfO6C4W5RtHULq/y2CFYLpHWUDbIvcDRkb4E7p6JHXd76rXWUiWTMWQRQjcQJHVLieQHOSXiDnT60NGj9LXtYmYKBaJqBJIRcoedxAIsO+1VWL+oeyZ14w3LOrBIZafIzeANlikBuWJM7cwZrNivbP+iHA52McoyVIGWSdSbXZjcaxK9CoPiilcU3me3MM4t4uZI5bk08GYIo/TUnEzLPdErAsL1eBXfEXJqaNfAj3Rx5IRLtUSXadtixxNPkeIaaVY0vCQbOVPCPX6As/B6IJvVMSRBb3k07n1Z5m53uiPIAFtMNsF6k2Og2fAKWavTrgRDCyOt+VibtgdFYrRQEvcZWUXHctSWQBZ5XzeVoR+I8dYWcSxA1klvHHOEzpvcLAbZ102sZkDnUt2xfGPinnMbQpYREWG6r3Eb4nAwJveBVVERYmohp8TKer2jCRdkIlPW1Ol8wYYw5TYIscqt8c7CmNbZUcrkW05yD7l649TSpi33YJlr8ba9QqqGH1YNj2xWl4lXOOvirvPmbGaZR6xcESPHQTytNzduOzL81q1Hp1hPtWrQIAglqRzaPhimEwH6HBLPhTW6JhPgQswe1Ijc9IYvw2GdGqFzDRJCJ7cTa5xXO91Gt3hKV8V0cVHNMY3GM0eMGSnX0lTZQPdmhXdVfkHVHW6ukZ48jQa7u+II3Qa30HCjqNoS22xY4U15b/fCJW27wBNXq3Iy9Gx72V5Me7Ic3843mlrxF+Rct2eTr1SIvGm7m1nXKLHLV62eO3bnriebopnrGVNxF7WaHX2noDbaxLHF19vbuPOx1r7LG81CeKlL+Cs8lIHc3Sh4JFt33EXu5mwiGz1rDJUUmsxZg84Qp7lhIrU1hBaGvXLaUruePJHD0vV2eZmYTKQ0j3JumVZDK7QMK88jtkW7gnBh1WXrrjy0UgmP0PpYwS1zpexlfGm9rbFm2uteueAYoXBdibSYEnWNWWwGIVLPbnsTCV7F8ZUKVRziWZtp5eH+PtVaao8sYwaMjVSi8KFYba/Cpj4T53Z3kyK22NSl2ErTRfBIYi1RzQ3R3T3O12pYyZ2xHBl7TwbCtmTXkj0GN5BLBMHm9som1C1oR+CWXLfrKNZVFxIO1JITazRwRCgN0b1ijMIKE5wVeuPj6nq+Z5NkqkttQ3IGgnm7NWiEt7lVQJeBQemYye/xGT4vBXZnSdAOtJnRWauAWPt+tQQDWT21stPoOJg2AsluLB3BTM+8N4XLJHuiks+hXSp+AZpWsymuaXZqKgHFrFRIEKgY8sKSTteq3d9zsh5RdjJ7dFT1G0wk9e1iRep9U9oFTk7RFR4RDExXoRXy1SaP6ru84+Lxco+WepV0F2h/ZkZl0+lHuThuTtT+WrqaL0Qpudai1mWQ6GilRaFlwQULkrFiz9AOy+CxKbFLZJttd4WZNeih15BH7AY/SCFkXdDkBjuwljhUYz3Cg08cVNAPs226GamdpzFCz0RQi0GQsLxlF9kNssBQo3V/145JteexzmoKr8xE0emcSXCvnE0k0i4aoQq3SrDWbkuJnPYlcztj0v5wIIqL3aBBrjUHWNTCLW6Tej5B6QHDL9Yu3ADSgnzfEEzSuOuDqE39BT+yXGnSfaru5MbFTU+m0mU78WR0vUkDIZ0ov9kM+wMt1DbssxsQzJgkUBJp7ybI49HMmowC2TPqaZm7vO4e3A7WhgHJdNKIKSjZq7fjzSRkAHT5vhK32caTDRhb368Tdp7OZllcliOZil5RGba5mnAHQngbJtrB2xkMKcVe5/vOsB53VKnYYkteHXv+BfUqYZV9Pacd4N1gG+LkyCgzAmi+TnurNcF40dFRN93ba7tCKkeqV301qNDJR6rsBhXyZZJzEoZVflMkFWr0y5TASB04orQOR1waQItT7JIDS9GIMEDVmeWuEgUaXnkfD26MZPJq3QrhtDaJK5cdw8ulOC8NibUUN76GOeHuA0ksaBZtdniyGYNuF4pGtomaHOlVb9l65M49ipKEbfqJzJSji8YuExaYxhS3FWS0d4M2xn1/6GusKzjKOLnwoTzlgUPiHjL1NdTh0+oM6vlhF11E9LIXy1DVLP5W7q5DtTzsVbJva/EARji5ghy7dZF8fVwfe547KppEUdRf//r24W1+SPd6LP3fe2lufpz0/+yp1vMB1Pv7L48HsK7pfH7w+vzflO9vH94qOwTSPZ/p1Unrvx56/cMTvY9/6gHlTGp8vqH2/iT++ZC/Mf353e63MHNa0BmMQKTk8V4M2GG19fwWaD2/KGyD798+W/6mHjg2neebLW416/h8sjlzDLP5pRfXCb+fvt7MmgmMwJGhXX/FCPyrWxWz5i/JgcLYJ/gT9vb3/w0GrBWUnS8AAA== -->
