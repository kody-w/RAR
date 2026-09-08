---
name: "rar-cowork-cookbook-demo-data-manage-promissory-notes"
description: "Generates 25 realistic promissory note demo records for a sandbox D365 F&SCM legal entity (default USMF), stages them in a dated Excel workbook, creates them, and returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_manage_promissory_notes", "rar_sha256": "6c4cad3bb1e8bbc2d6d5ebb2fc6d7616e25263a5165e92cbed8ceadc911d4469", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_manage_promissory_notes`. The original RAPP
agent is preserved byte-for-byte in `demo_data_manage_promissory_notes_agent.py` and in the RCI capsule.

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

Manage promissory notes Demo Data Generator — Generates 25 realistic promissory note demo records for a sandbox D365 F&SCM legal entity (default USMF), stages them in a dated Excel workbook, creates them, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-manage-promissory-notes
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
      "description": "Excel staging file name, e.g. demo-data-manage-promissory-notes-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_manage_promissory_notes_agent.py` and embedded as the fenced Python below (sha256 6c4cad3bb1e8bbc2…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_manage_promissory_notes_agent.py` first:

```bash
python3 demo_data_manage_promissory_notes_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_manage_promissory_notes_agent.py   # or on stdin
python3 demo_data_manage_promissory_notes_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage promissory notes Demo Data Generator — Generates 25 realistic promissory note demo records for a sandbox D365 F&SCM legal entity (default USMF), stages them in a dated Excel workbook, creates them, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-manage-promissory-notes
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_manage_promissory_notes',
    "version": '3.0.3',
    "display_name": 'Manage promissory notes Demo Data Generator',
    "description": "Generates 25 realistic promissory note demo records for a sandbox D365 F&SCM legal entity (default USMF), stages them in a dated Excel workbook, creates them, and returns each new record's primary key.",
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-manage-promissory-notes',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-manage-promissory-notes',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'b39d924d46d77c07',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/manage-accounts-payable/manage-promissory-notes'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/demo-data-manage-promissory-notes', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Sandbox D365 legal entity to write into; defaults to USMF.', 'record_count': 'How many demo records to generate; defaults to 25.', 'workbook_name': 'Excel staging file name, e.g. demo-data-manage-promissory-notes-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Eliminates the 'no data to demo with' blocker for trainers, implementation partners, and pilot programs by populating realistic but synthetic manage promissory notes data in minutes.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against a SANDBOX legal entity (default USMF), generate 25 realistic demo records for manage promissory notes. Use plausible values for every required field, vary the data so it looks organic, and stage them in an Excel workbook 'demo-data-manage-promissory-notes-2026-05-24.xlsx' BEFORE creating. Then create the records in D365. After creation, output a confirmation list with each new record's primary key. WARNING: this recipe creates data - run in sandbox only, and never against a production legal entity.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates a configurable number of realistic manage promissory notes records and creates them via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Generates 25 realistic promissory note demo records for a sandbox D365 F&SCM legal entity (default USMF), stages them in a dated Excel workbook, creates them, and returns each new record's primary key.", 'example_request': 'Generate 25 demo promissory note records in USMF sandbox, stage them in Excel first, then create them.', 'inputs': [{'description': 'Sandbox D365 legal entity to write into; defaults to USMF.', 'name': 'legal_entity'}, {'description': 'How many demo records to generate; defaults to 25.', 'name': 'record_count'}, {'description': 'Excel staging file name, e.g. demo-data-manage-promissory-notes-2026-05-24.xlsx.', 'name': 'workbook_name'}], 'model': 'claude-opus-5', 'when_to_use': 'Use when you need demo or pilot promissory note data seeded in a sandbox D365 legal entity. Never run against production.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DemoDataManagePromissoryNotes(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataManagePromissoryNotes'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Sandbox D365 legal entity to write into; defaults to USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_count': {'description': 'How many demo records to generate; defaults to 25.', 'type': 'string'}, 'workbook_name': {'description': 'Excel staging file name, e.g. demo-data-manage-promissory-notes-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(DemoDataManagePromissoryNotes().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916abOiWLruX/HuE3Gr6pC5kRmzoyMuyCAqigwCVnZkMYOMMgnUqf9+F2pmVnVXnz4dcT9dKypVWOud3+d518Zf35yujcv67dObFjjFQnSyLImDeuEU/mJd3ss6BW9l6oL/F15ZtHXidm1ZN28f3vyg8eqkapOyANvFoAhqpw2aBUos6sDJkqZNvEVVl3nSNGU9LoqyDRZ+kJfgtlfWfrMIS6Bo0QBdbjksOIwkFsL/1tbyIgsiJ1sERZu04+JHPwidLmsXhiYLP31YNK0TATVtHOSLpAACfKDWX/CDF2SL2eLZ2A8LDxjRvtZ9ePhTB21XF80icLx4UQT3lx0/NMDKJHeAiWkwvgPPgsHJqyxo3j79/LcPbwn4/Pbp1zcvcxpw6Y0DLnBO68hOAQxRvjl4AP7NccmcIgLLqhEEtgDfq6AGjubgEnBk8fr2YxNk4YfFf/5nenfqqPnp0+di8Xp9fpv/U7tiNn3Rlk4zu+c5leMmGQjI+4LJ7s7YfPMHhBDkpYjenzu/SyqrxV/nez8+lbxHQfvj57eymhMFsvb57acFyMDnt7qbP7/PUqoff3rPyntQ//jTdzlN514Dr52FAavfv7y+v8SChd+XJuHii6bw65cuEOGkCoDw3/k3v56mv8S9QvLlufjHsvqw+HPJsz9/BfY+K88Fcv9cLIgB2Pn2fi2T4seXjrrsg8IpvODHn/6ZWC8OvHSu2/+R3J+fguPA8UG0XiEB5Tmn4G8L6OXbN5n/XG0FCubf8QQs/6ruW6D+mexHZv9OdJYUoC2+5vJPxf3ZBuivi5//qW//3YYPi/AzaJos6UHduVnwafHro0R+/sH/fvGHv/0GRP9LMVrZ1d5DwpfcKZIwaNovX37+oXlc/uFvP//QVaCKAyf/0tXZn8n8s7g+9Pwhgq9VP/5xL9BvFGlR3ovFtx5a/FpW/6v+7X1xBojnf7/efFr8vhPnF7SYnfiq9BmC33VjA2z9XRx/evsNQE8BvOm8x22AH//xHws58eqyKcN2oXll1y5AgtskD2bj9ThpFskD8IADIK5NAgL7Wgfqf87wbHEZLn75P94D2z96L2yHZ1z+AoDUmeMKYO3Ld+D+MgN388v7QgeCyzqJkgKAs8ooyud5ZdHOSqs6aIK6B0Dljm3wEfTzx/nDDNC//EvZXx5i3qvxlwdOJ0/kU9fSjHpNlwXvs39mHBQvbzxAVcEQeB3QkJUeMCdMAF5/AH43ZdYD1Jxj0aRJli38BOBKOxPQgwO64tMs7JdffnGdJv5cPGEaWzy5rIHBgm/mLD5+BH6FWRLF7eci8OJy8cOvv/2w+K/Ff7frIXzWoQC+eGUDWLjVjocF6K4uB8tAokBqAXQ8svHrb6/oAjGARRcgd0mYPLlr7oI08L+GWtswH1GCXLgBCDEIb16VdQuwf5G07wspXHyzFyidb83sEJdNC4i3Cgo/KLwRSHWAO98iCVIAOLhNmnD8sOia4KH1F7d2HibmoM2d9peFvFYAF5UZ+Gc287EIbC6LBIT/WyE8rwMhNWBV9quI98VhrsdF5dROFdfOS0foPPMyTwGv7UC4M1Pz52Jm3WAO1aM5nuGJ5hkDDBXPlH6ccw6GkhxUld981R295hB/oT+Ys/5cNK/Cd+rgQfnAlHERdYk/08FfXiXVxGWX+Y/4AUtnSa8s+K+sPGrwyfl/P9U0i3kmWMxDweI1B8282qFLBF/8fzMYzf4zoqjyIqPz3II/6Kr9zMs8GM75e86Ss2mzA48e/D62fIWmrwj9ucgSUGT1+Jfnykc2X2ueqNfVwHqVUR/yQSmBvMxyH5U+V25dzz3ifC6+UgHwZvHAPZBsAAugbeZq/apwvvvV0hj0/vz9+1jw8nmOB6jmRdW5GchSGAS+63gpsKqeu/WVU1D2wdy59zgBEfu9V3NuQLyA/AUwIgH9B+ji/Rs8P+9+Nf0PG5/Tz7zlMRl2oFnrhwBgRzAbOGfqnrQAs5z2OYcDPz89hMzFVLWz7y5oF+Dp82JQB7cuaZJ2hsZnXIMK4PLH+f3p6Xw1GCrQISBYoA+qDkT30TkzqORgtgE2gOIEjZQnxbN0X0F4CHTyGQYAzL5q6CnxcfnlUPBot5mkvm6cHZn3zLy/CIHp4Mr4e7TQ/6xMgLx8XvHQ+/eV9k3bLHtGzAagHtD49e5zQHh/cvxziFh8lfvpHw46P/57Z6EHaxt/LIBPi7htq+YTDD+Z9ivRvgO8gp+2Ng/S/TgT48cnMX78DgofH7jyB8FPnz8t/j3j/iDi1RyfFsj78n0539q/iuv1ArFYf2Ttj/h893OhBt/hFKgvc1Bdc+ZGwPLfuO/rEkCAUQ3wCSx+cmEzU+gdsPYD/EEaPhe/r/a52wC3FNFcnU35OxR4DAGg8p9Z+8ZR4FbRAt3+PDRGwXxSe/RGE7x9Kros+/BWgLr7H5zQZh7K55Ju5nMdCDqYwdokeHx7IMTQzh//eMA9Pj442TsAe4BGWfP7snuxx8yev+uOp5PAOQ9o+PCA42ZmO+DkrHzuLKdJH3A/O9OO1Wz98zA3j38PtP/yRPt/NEj7PT38gRgA6N1BcwQPQv3L4kUTzXx9poo/1fVtDv1HRSYYAOa9fvlp5sIPL7gB7+DsAPjk6zEAePg6mD0O0UUHzrw/z0eQOeSPLfMHsAe8fdv07Q8JbvD2tz+x6xnDL4Cjiz9Jyqa8A5AC6PEH+gS2fi3KP3qPEn/q+1du/PKsn79X8iTQmV1nTHxU6LzwwyJ4j94X/7KJP6JLlPy4JD6i+PuQNcOfmPDwE0A1ILw5ZN9z8T0i5eOENlsLItg+/6Dw6xuoYmfW/arj14gPlgNk+9jMgw0MWh0oBN+fTQnu/fvD/0tAEztg9gQSSA/3HB9zXSSgXddDfdInAtdFQ4/0KRIhA5RAScwhEJIIVqjnBj7tAfr0Vgji4zi5AvKevf1lHt+S2ShiRYXL1QoNcQRd+iBpKO77NEmTHkGhS2flOoRLrBz3+9Y0KfyXp0/P5jB+O4fMEXk5/OubS+JzseCNxDxfaxhCXAil3PFgwdaSHi62qBhJpTqWMyVjFSYp0mzv2MkS2aJDUDxKd6qEZ3XSqaPGdWvbYZSlFjYprGJTM923TYU2dbcqDZ7RAl3OdaWgr50l6t1Rxq7tFiacJBmUlhA0x8V17VxJW5vKDrG1CTtxn007tTtDaRdeKQte5SG64UvaSzIM926atOv6g6AdDpPoqMRNPu08DI3htepVMSzQqh8qqt3DHdyQe1Mi/JsSG+Pudki2thZbYZxaeNtNyLgSbZLfybsL31wEl9eMiBf3F2M70Jx4aup2T9tVnguorEZSsb6yzb6WhCyZtkq2ZaGGFbc9t6U7pvLUrAn3AiUVumcrm56gez0lXAXb0mFCyBi1hOgVbeFX9cLkrB5pYZY1y+puS7Cz1x2Vx8UQksu6Mr3TPrluddZ3Q67blrmtjPyE3AXP0rhGZOSI5WwFW6Jarq9GRUrlTIw1PxC0tUcMGxRnIDSMd221vt15jK+8wcwS+6rjzG5KKNW5toSjXAMIbdneObLatsA1bX8I08ZgJrrNOMZsK2a0woJhi5SJL8Iyd7St0MVbK78nmtORG5+RiMi1GQYR2SvZ8FLRKt1K6fcy1DrniBgT9ZAqwm0vl2nGZQp77zRzraws3hIuHWOpKt6Od8ktOP7Q3NZNyS97WNuvhf7M5R44di1jwVA29igc8hQ6d6cKolWrLBXUHqVjK42jVEu+jt1OEKUfLgmJhzx3H8dUSVGt1ohlR17yPSQM/RJvU3u6bUmnNqJ7yx4iDYQMr2ARWrZlwJgmbZ6KovNPO/XqOLFyM6Nz6Zops1/lyA0tMylGNqNtaPmg1ajr3fbhgTn1l3WhCJbtFMdBEHZhuQb1gLCcDKUFnlj4GnZOCss3esdPki0U0OXGbuuwvRoQT3TJeFCbY4Tgds7lgSGShVmJyEXzgvu2X619Vy1XW9D8ulrSueViYR5GS6QqjSsLy4MIreIVwfVKfpU1d+IwCc+vExz2UmZFxJHwy+jMx/sKaWx+zJotYVOlLdFjVCKtIZtwcfMZXL6LAh0zwTk7UhFn5QeV76HI8ev0LG9EfXVJQc+3EFe1MT14u3tjpilzPHXC2ci5SmZ2xOGil8yG3yS4hdDNea2wlsWsbnx5l5j8CMvxVqFM/RL7N9dudMWkBtne+iSJoVdB3w25CXpp2VzWDnpQHVRh0YI5sNphI/WSsFVyIVQJcVe2K46z65DfSjc+lvbn6oD1eb9WtyZ0uEmanoSX5mIqHavZoUOI4zle24qzP58cGU4IG+I7DTelklWrfcMUin+4awf6BvuS4prrvZQhKVzigcoUcR7dr5QMQ1aqoHGh4RHiXE/rZTThlixjfndkynsYIYflFne88XYMx2G1LrS9VO1oF77CbTrdB4aILJnMzOaaprWN1st7nOLcasuz9/IYHg+orixJsy9ThsrNowhnN/qG7sztRNrR3pYkNFlCDLeJbkq2ZFzPS+DdSTgrqLCJ/dK1hfqEq8AqTyCvzNmx9SN7vZ/OEoSIjaNR+x2DV0N5Jtp1SeN42Vy4dW+dD+5JMoxAwaE9ZOIhqDi+PDvGGsN8JdyYOlyLPKWM3E5xAqZND6N3OZqTsRGJqgBoW+g9tW+s3vI8cmeF0ZoXV0c70uOjkZWUACoVU9cHR7VQ8rS9F8RlP1pc5wQbntVIj1weankdXgZ/rQXhCN0TNrldL6taUnxug6fSRcuT1DFl/zgop8lpEBIOgukWymh6wvHI5ERZCgIIz6nVabrtbD3x45u/C3rzfCi3ggQTnGoIzFUYtoTjS9tTFkxUfLC9YS8aN5o5bV0b1pysEXS8o6sVI94SPkINSneM3nNvxGV3rhl26eCHaUkeTd4YLXDZM9JygoNjXQLwvowef3AL2ehG/d4QhaEZThzSg+7v201pBNKoUfmqHrCI3gWbUG8kGc0rlt27MG6FAHURSLQw/Bz2CEIrbG0jfp5mcizTMG3uGYHx7pEJb0lPUdZXwkh1CTFvY8zwhxvRYEvmehPz8YpbuFjmWMIpQ9W25pk5LbO441if4dDg4AiagKiHaGVrd7P02CRK9opkBJZdRiI4+qn6LV5zbH/d8VEzrVKnmHQO3y3Zra7JdBVUuE/7DUlupYODrrn40Gz42qetDr97t0FsdgmswOKWq1c3GmPk4cSDdj2WSZIrzlQb7mkNV0hn2BJyl+wmpwg26VmTFYIN1UKRuFHynW0kkg+xgacYmgOvl+ueKEJbYk2r4QaP2Vg7oxZK7ACfz5ELTUYBpYm77k6tuTpbCmtAxpVIs+NWyHZtwjfMvQWcae52KRAh707Lkdjamb3W0g1jJ4a1y/HhClkoRjPX7GT7yGpzEc9RtSZP0T6hxT7Nod05UZbjWnfETXMfVfO6LeNkSwqZGmf8rbperNwuJ5GXWemwzooxO9fTpZqkaH2hpXUcSxzXWQIYF8lYWA8CxaejqB5yHdH5OGBCJLnwJ1RdT3beCO6IZ1PpGyq3RIx4d8inXizNnQER4ukuSlx97dzaXF4zUiK801K/7OmlRFfLUCHljLknJIORMKitKcspFWdcWdFhyVNPsb4sb+WWvt+WPNvtVHuPSLE0SQEZ3c62ol5cljXGCuFXWU+pvLQSJakrrjBq+YkkojvYzjg7WEMxckb5hmxLAfFKTEBzPEeGg+kxe0WfLBR2eRnlI4U5ESbZB+YltmzTwTcrMmG3J/MCrY7XBvcVf7wouKjtg6N+4PkKHP043ucyLFof0JsW385VnIJzQ35SWSdZMcVA3RQ6bdxz2kvpnWt4+3xM0WFzitDAhBlLYCtCKQnjau/l0aHvqUFcV6DOSVy18zBB98nydmw2DAufjJNvApyfAvaqaWV8ITgWL1svt+uRd4i1vsT8tXR3UD3F3WWfYMf8du2YEzjDXtrpehpubemfLmTEbu2zcc8kGvdv7BFjbbTyDcq54Xt8C8HQBp9OZYvq5TZlj76N32GD7bHRHY+M114JXtnX+W53AOWlrV282MVmU2dBZ4bTkMf++tKeDGF3qmttn98Yls8zbV0qvnPmzoEKkIrDPGxVM+X6OO41v0VAEdfixqm1siniK2bE8+g3JezqHC0Da50mCVMwS6IrT6uq1oeOlZNrxfV1HZGVQhD5Vo/v3THIw0NQq+fktA1qbGevR6Xl0c3NSC3lpruIvr3yZNQce15vOSg9u2v30mptOO0ZzV0diNU2qVBuZ67vXlKSrbsrsEtIXs2lHmW9axRUOQ7p0lM22BIJwhinu3hPocdGKepOVy3NBNyPtqbjrEyq3iY3s8aWOLGfyErG0dTZ7t21kJPa+nRaubiEaiSVJaOFyFjoNV6Ep5qUsxjorxzd1rzPkuUZOk1BLjEKZV2Yjk/OuZOdoqQ9QmR9Z3gevVm2iJGtjp36fG3aOz9qPbXXy0Mr1tQp7u+9z0YugFTBvMvXDhGvt5xpQ81tsJOwpFdVVgbnXjByX9ufTYeeJmR1F1Xvjgewm0NK4SorOOgocH6Zgu2qqtYsrFeJSZ8vKHNX0VpsrtZNdKvCGUqjYuULc5e6G0gwtZfjcndbU7R/39E7rr2seDBPE1RyPXOOmS7BAKsilr/SVpbCrQg6dJfqJoglHgyUSZDvfJPZGUadXrfRWeuZlMgY1WEqniraHq/HOrRNvipM+oi0e2XjNysZq1ckfRDyLDJ6VxAPhL5L0ko5tyxOJv3FkVww9Y7NGbpP+xPH6cvxTgmCRrrEoZHN6SRWSVtc+sFkSAnIQXubTlvxvM+4zuCMJBM2JwVNscBgXcPL2D3HwbdNe1/CpDxZF5Q37hsn8LWyl+DbwXHN3qyycQxpLonu/lZlTrKQi3KnVdyA0xnE8ccDk0EnJu7kC2SZqCz54i6MokkShByqCgxnNpRhCKs6ks6IZvJ6SnXnygCerS6dYhPb0NhfdkI89lSL9Ihh37k6jQRpezyja38ZjU7pkywHmWp7veg6WQIWp+uziba3O4ieUDG4pd3JzbjF9gaPM/e8HtEdEvC0RnQZ2UEN14WIF+biTtAp4XZyQe05RHCI1/JhtfFN79gnZ5GqLX5z0TV3R5Y6dFnXyQlxdcpHbKfaZVTcSiHMC7KVCzuMZ/E6NCF38mJ/31fGdnXZAJQ+OkO3b9njTcRY4ZxIA7W/3JyxVUN1uGypsZC8LX3RZO1eKp4ikaiWUnbrYWwMHdbijSGrYTj0ohBt9+sRR9r1rTdWggNmlm3p58iWOh9dddBtxwLQ1jH+cCZCaVNtkj0q0E4czH9AUUinXdvHtO92dnkmr1ipRqIftGKcTfg5QIIKuqMXzGU7ibgG0VHGK3IAR6DKOrg4sVNdZGfsChPSh9Fke57cq74YoZvD4IqWvInh8oSQyy7WEbNeJwpK0tQFVw4l3U+rpiV81AVgyUxNKHZHHK6V6605k0suP5arw0kpr5yQ9Xp9hVXRIOgbvTz6yhRUA4epEGnW2iEhlhUur7rsEMHNUGL1ITrbBQb6xG/NW6nzbRHzyhXqmPX2NK0rBzs2Z1/PYXnki2JDrFxE0QZ07LRwF+rL/UFrK4WuDOe6H5aoMvqVE59W8g5HkNCRB5p0UWrYc/F47GMV0IvfQcpws+OOCmH4YsGs54qmn7ZKXYS0DrOp5Fic36JlUysIVLOZpHXJYSgHhvblwd5u+COBbJYqOJVDan8jaXAw2zhEHqnOKc843Z84ei1I1+Yab8wwTXVywp0I2Z/rKnfllRA0tAHABsAmWm5oECdmh4TNWHCBjU+xeD2m2JWjjvAYVN3BadElxeQr6BSZpyEpp/C4QpAzTvrDTujD6AjoPcV025bDmNQOAgDqw6AMYQ48ueWlM1KBR9BIbFic1ZNn4USilefVKp1V4ZCtnCOGa5tLyqd4LKpM0unsHYU84+yjQTFwuqTSroMh63WXT3GxTa7otKwtlS6G8La5eWdbjA9o3Kj4qqGWQU/HTYMTa3YDFRcZ9bowUY5nHD8hq0SlKu2UXLUtFHAMaMllzyZmd9LY4irIe6oeBs7KSunSVTJE5gC6WVtZLrfRuiJvzKHfuEPpDDyFD5V2Hhyup+6HVIeR8Hika5fb5UU4pqFSTMtRAZO8bawHbrsmm9xP5anTwSGI7E+n21DB8TDJJMzcKaLc0avVcsc2bgflvmjBncL05Vrqe6+76dfS7abm7FmML07phhtCVbpMRC/mZ+Ru2n3m3blc8Ki9rmBW51LEtSpHSCMP3qolSpE/ysp+itiJOCm9GiOxr55xeBoHGdtkm4OJeXBxd86XquYInikOx8vqdlfSY7W9asezX4Kz1666YpRr5CfbiYelHI9+ex9XQZtdidhhblISdVQwDSURM4GmYBEgSeZeSzcFDKTEBlXD823UjM0SuZRZgINpxU7uB/OK9Tpa+MJlZS6J1oxNKLx05DqxB5iEQsrYd94Rc5NtvskRfzTdAKLQA78ZfGNY7ZSc9+AAxW59rR333ZGqc6g+RusrZiFuMXa9hlM7h/ClswXxPV54xCk9r3ojN7r15HUr5eIgOpGcj5mD43esTJRN0Sm+FyiofwwgmubpsaWWkHKK3Ek+iaTaqK2tV5sq7tV2oDTGzkLKvO5rbNKuEBxKawllfQmMYe4SL5dXgsTuYQwfJvXMXK8cetptLAuqJC0e46nCJUy+BoQ6UuNOvcgUXUYc7gG03McULeQDqYOjs4lo/Q5j5TYoXRlH9po7qRgoBHqFuXfYZ3ZxzzcUv7HFExQ5J0y38PJCFBztdvEor8Zs6kqFu+ZWDzcTsDq2iItBxXfj6qIC6oTOviU0NsPyUgVcCO09q87JS1upRUE3lx06XXKHQOEtb1d7W0aoXLQluB1ReXAioszloUb29t3DjunkeoQ+wVd0eynqjVnteUz0i5W/aZJEFq8SkSs46rUrFK+aUNtU1GBupZDAmVurjyl78paIlrlXO4RYy0cOu5zejrQMnZZc1bmjeDAPNeAjo+iRVl7tNgc5xBC+Do1LmFn7E0T5J6ywoTVdATT3jwkz6s6oaseVwPUJn6WbK3nkOtiBPAqK7SgkbwlJUZat7IKgB7wOu5NjkDEiYnvKH4tbuk/pOqINE7EUXyJXdrZSN4ai6lTSkCkOir40h8Lcx/FFipylm9WWiIkKUR26fYFIVxuWxcJSzJigwqZcDQp9TbQhNvNI3ubD0jp3rT/pRF83a5NAREnpeJ2T9qGnJoxeb9gtS1MT7kcbpjx3HAG3aY65k17BCMfJEBzwehERYUkUeX1swdDFQrtjVrZxcts0ZhEFpb+Dx2XSVyie9EW3x/WzEPiT3eI+lPQ+2L3PYCil0qUBwAYtOVe4D6QwjVIOe6zOHQh0h7VpCcbK2/HmaGi3hAbraOnYdoKO974k4N3ok5NWm5pyD2pmqpGwO9woRPBPMn2vh83qeD/0ua15p0A5xPs7PbG2L1AykXT5GSOOyNk/w2tBSanIWx72UbQuTThd6vFhyRr6/cyeWasagmVQsL3dkduWRJbp9rjhg9XuAm3LI8q3W3HHdXiYMXSaeliJ8X1nCORSJSFY9lux24OAUStbHy5kIsKdaAXk4C6X3D04m2Pk14pArqYdvjf1gIU2eYvsyqSKUfagZynXhzXadwIGw0rIVqcjxRiXCarYkCxTRBzNbZzJF3jQExrWanbcy7ahYdN509eOwijHSPQcsmIZhvnr24e3+WHY66Hr//xXXvMjnP9nT5KeD32+/orj8cAR3P/00PXp37Dpbx/eai8BFj2flzVZF70eLv3d07KP//KB37x9fP506uvD5Ofj6daJ5t8UvyWF3zUtsKEps8evOMAOt2vmnyE2s4keeP/9M9Nvbnx/+NWWXypnjmRSzD/NCPzEaYPX1+j18BBsHEFyEq/5gpHEl6CuZi9fvwEAzmHvy3fs7bf/CzMYRHkELgAA -->
