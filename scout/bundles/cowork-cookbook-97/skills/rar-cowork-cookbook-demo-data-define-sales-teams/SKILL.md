---
name: "rar-cowork-cookbook-demo-data-define-sales-teams"
description: "Generates 25 realistic demo sales-team records against a sandbox D365 legal entity (default USMF), stages them in a dated Excel workbook, creates them in D365, and returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_define_sales_teams", "rar_sha256": "b13e53500d02bc88b56956f2813a81b6fb58ccdd5a18bb9d7e04f3eb02e7fff2", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_define_sales_teams`. The original RAPP
agent is preserved byte-for-byte in `demo_data_define_sales_teams_agent.py` and in the RCI capsule.

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

Define sales teams Demo Data Generator — Generates 25 realistic demo sales-team records against a sandbox D365 legal entity (default USMF), stages them in a dated Excel workbook, creates them in D365, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-define-sales-teams
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
      "description": "Sandbox D365 legal entity to write to (default USMF); must not be production.",
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
      "description": "Excel staging file name, e.g. demo-data-define-sales-teams-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_define_sales_teams_agent.py` and embedded as the fenced Python below (sha256 b13e53500d02bc88…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_define_sales_teams_agent.py` first:

```bash
python3 demo_data_define_sales_teams_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_define_sales_teams_agent.py   # or on stdin
python3 demo_data_define_sales_teams_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define sales teams Demo Data Generator — Generates 25 realistic demo sales-team records against a sandbox D365 legal entity (default USMF), stages them in a dated Excel workbook, creates them in D365, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-define-sales-teams
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_define_sales_teams',
    "version": '3.0.3',
    "display_name": 'Define sales teams Demo Data Generator',
    "description": "Generates 25 realistic demo sales-team records against a sandbox D365 legal entity (default USMF), stages them in a dated Excel workbook, creates them in D365, and returns each new record's primary key.",
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'prospect_to_quote', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-define-sales-teams',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-define-sales-teams',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'bf8dfdbc6571008e',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/define-sales-strategy-and-policies/define-sales-teams'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/demo-data-define-sales-teams', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Sandbox D365 legal entity to write to (default USMF); must not be production.', 'record_count': 'Number of demo records to generate (default 25).', 'workbook_name': 'Excel staging file name, e.g. demo-data-define-sales-teams-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Eliminates the 'no data to demo with' blocker for trainers, implementation partners, and pilot programs by populating realistic but synthetic define sales teams data in minutes.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against a SANDBOX legal entity (default USMF), generate 25 realistic demo records for define sales teams. Use plausible values for every required field, vary the data so it looks organic, and stage them in an Excel workbook 'demo-data-define-sales-teams-2026-05-24.xlsx' BEFORE creating. Then create the records in D365. After creation, output a confirmation list with each new record's primary key. WARNING: this recipe creates data - run in sandbox only, and never against a production legal entity.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates a configurable number of realistic define sales teams records and creates them via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Generates 25 realistic demo sales-team records against a sandbox D365 legal entity (default USMF), stages them in a dated Excel workbook, creates them in D365, and returns each new record's primary key.", 'example_request': 'Generate 25 demo sales team records in sandbox USMF, stage them in Excel first, then create them in D365.', 'inputs': [{'description': 'Sandbox D365 legal entity to write to (default USMF); must not be production.', 'name': 'legal_entity'}, {'description': 'Number of demo records to generate (default 25).', 'name': 'record_count'}, {'description': 'Excel staging file name, e.g. demo-data-define-sales-teams-2026-05-24.xlsx.', 'name': 'workbook_name'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need demo/training sales-team data seeded into a sandbox D365 F&SCM legal entity. Never run against production.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DemoDataDefineSalesTeams(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataDefineSalesTeams'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Sandbox D365 legal entity to write to (default USMF); must not be production.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_count': {'description': 'Number of demo records to generate (default 25).', 'type': 'string'}, 'workbook_name': {'description': 'Excel staging file name, e.g. demo-data-define-sales-teams-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(DemoDataDefineSalesTeams().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916adObSLbmX9G890O5ruwXEJvkjo4YFkkIEBKbQJQrXOz7DkJQt/77JNLrpbrdNd0R82nksCUg8+RZn+ekk99f7L6Lyubl44vq28Vib2dZHPnNwi68BVMOZZOCrzJ1wN+FWxZdEzt9Vzbty/sXz2/dJq66uCzA9L1f+I3d+e1ihS8a387itovdhefn5aK1M7/90Pl2Dp64ZeO1Czu046LtFjZ4WHhOeV+wKIEvMj+0s4VfdHE3Lt55fmD3WbfQ1ePu5/eLtrNDIL+L/HwRF2CqB9bzFtu762eLWdVZy/cLF6zefTduFvz+YVDjd31TtAvfdqNF4Q9v2vzULqomzu1mXKT++ApM8+92XgGdXz7+8uv7lxj8fvn4+4ub2S249cICm1i7s1k/iAtfnY3TgG2zTzK7CMGIagROLcB15TdB2eTgFrBl8Xb1rvWz4P3iv/87HewmbH/++KlYvH0+vcx/lL6YtV90pd3OFrp2ZTtxBnzyuqCywR7br6YA/4GYFOHrc+Y3SWW1+Pv87N1zkdfQ7959eimrOUggYp9efl6UDViv6effr7OU6t3Pr1k5+M27n7/JaXsn8d1uFga0fv38dv0mFgz8NjQOFp/V85Z5Wws4N658IPw7++bPU/U3cW8u+fwc/K6s3i9+LHm25+9A32fWOUDuj8UCH4CZL69JGRfv3tZoyptf2IXrv/v5X4l1I99N55z9t+T+8hQc+bYHvPXmEpChcwh+XSzfbPsq818vW4GE+U8sAcO/LPfVUf9K9iOy/yA6Awnbfo3lD8X9aMLy74tf/qVtfzXh/SL4BOoli28g75zM/7j4/ZEiv/zkfbv5069/ANH/VzFq2TfuQ8Ln3C7iwG+7z59/+al93P7p119+6iuQxaAQP/dN9iOZP/LrY50/efBt1Ls/zwXr60ValEOx+FpDi9/L6n81f7wuLgDtvG/324+L7ytx/iwXsxFfFn264LtqbIGu3/nx55c/AOoAeGx69/EY4Md//dfiGLtN2ZZBt1Ddsu8WIMBdnPuz8loUt4v4gXnAAODXNgaOfRsH8n+O8KxxGSx++9/uA9c/uG+4Ds0Y/Rlgqf3ZeyDa5wdef57xuv3tdaEBmWUTh3EBoFmhzudPBcDhopvXqxq/9ZsbwChn7PwPoJQ/zD9m2P3tr8R+fkh4rcbfHsAcP/FOYQ4z1rV95r/OVhmRX7zZ4AJy8u++2wPhWekCTYIYSHsPrG3L7AawcvZAm8ZZtvBigCaApMYn6PfFx1nYb7/95tht9Kl4gjO6eLJXC4EBX9VZfPgATAqyOIy6T4XvRuXip9//+GnxP4u/mvUQPq9xBgTxFgOgIa+epAWoqT4Hw0B4QEABYDxi8Psfb44FYgBvLkDE4iB+ktac+6nvffGyylEfVjixcHzgXeDZvCqbDiD+Iu5eF4dg8VVfsOj8aOaEqATU6vmVX3h+4Y5Aqg3M+erJouwA7XZxG4zvF33rP1b9zWkelOznoLjt7rfFkTkDBioz8M+s5mMQmFwWMXD/1xx43gdCGkCj9BcRrwtpzsJFZTd2FTX22xqB/YwLYJ4v04Fwe+biT8VMs/7sqkdJPN0Tzl3F3EY8QvphjjloQ3JQ/177Ze3wrfPwFtqDL5tPRfuW7nbjPzgeqDIuwj72ZhL421tKtVHZZ97Df0DTWdJbFLy3qDxy8EnyzxZm8cjdxcz/i7kBWLw1PTOR9isYwRb//3RBs+3Ufq9s95S2ZRdbSVOuz5jMbeAcu2fnOKsIEvNZf98alS9g9AWTPxVZDBKsGf/2HPmI5NuYJ871DbBCoZSHfOAWEJNZ7iPL56xtmrk+7E/FF/AH1iweSAcCDSABlMycqV8WnJ9+0TQCdT9ff2sE3mye/QEyeVH1TgbCFPi+59huCrRq5kp9CypIeX+u2iGKgce+t2qOEfAXkL8ASsSg9gBBvH4F5OfTL6r/aeKz35mnPHrBHhRq8xAA9PBnBedIDXEH8Mrunl03sPPjQwgwI6+62XYHlAqw9HnTb/y6j9u4m2Hx6Ve/AnD8Yf5+Wjrf9e8VqA7gLFADVQ+8+6iaGVBy0M0AHUC2giLK4+KZu29OeAi08xkCAMS+5dBT4uP2m0H+o9RmWvoycTZknjMz/SIAqoM74/dIof0oTYC8fB7xWPcfM+3rarPsGS1bgHhgxS9Pny3B65PVn23D4ovcj/+0rXn3n+18Hjyt/zkBPi6irqvajxD05NYv1PoKsAp66to+aPbDzIcfnnz44RsgtH+S+TT34+I/0+tPIt7q4uMCeYVf4fmR+JZXbx/gBuYDff2AzU8/FYr/DUXB8mUOEmsO2gh4/SvlfRkCeC9sAESBwU8KbGfmHABZPzAfROBT8X2iz4UGKKUI58Rsy+8A4MH9IOmfAftKTeBR0YG1vblDDP15R/Yoi9Z/+Vj0Wfb+pQAp99c7sZl58jmR23nrBkoG9Fpd7D+uHrhw7+aff97Enh4/7OwVYDzAoKz9Ptne+GLmy+9q4mkfsMsFK7x/gHE78xuwb158rie7BQkKcnO2oxurWfHnpm1u8x5Y//mJ9f+skPovaQFA3QBKYt4k/gNF/G2R94BTZk86D7Dwnl3kD5f/2oL+89oG6AJm6V75cSbE92+4A77BtgEQzJcdADD6bU/22DoXPdju/jLvPuYoPKbMP8Ac8PV10tf/P3D8l19/oNfTrZ8BURc/iJPU5w7INIDJD2b9QqdA2S85+s0nK/znH1r+hSo/P3PpH5d48ulMtjM0PrJ1Hvh+4b+Gr4u/quUPK3hFfIDxDyvs9Z619x+s/jAQgDWgvNlX34LwzRXlY1c2Kwpc1z3/E+H3F5DR9rzsW06/tfVgOMC2D+3c1kCg4sGC4PpZm+DZf9Twv81tIxs0nWCyg6A+juIw7MErx12vHZzY4ESwWiOovUYcInDwtet6Hm4ja8fZeKQPYwHqO/DKJ4MgWAF5z+r+PPdt8azPrAxwwwcAEP63x+CW92bIU/HZS1/3F7PBb/b8/uIQGBjJYe2Ben4YaIk4kEE6o2hCJry+Z4PeVxcVJFqWOwTnmvt7fIL31D0sWkd0xQtClW6s3DVr5wZdqLCUtIlZPCqW2nKqUstNI6WrpN7vbrEY2cNkpbi7tNbQkeQ0euL2yiReLOWgB/Fd3MoVZMBR0uurnestievNPFZ73CRsfCl1AZQ3y6EZCg3We0gL6zEO5YOOFhtFshN8G06uxCz3LaSWlbqko+OQm4Sq3KHlBtG2bo9wQ29luz2+XUtycxtqsdXP+GoTJK4dC2cYuH2vGPdtZtBVfEMYN6CqVBRIDeIEq6q8ZGuwKFxVXHR0mX7FTm1ba3IaQqtDtDXzrke3fOo7GrLGV1jGdrcjl9yXN9Ma/dbkYOJ0d4sqIk/B+byLDrAh87GObVH84nSCu99N4JGeC6kWWhA2xn3m3OleFOJOWItb7y5tR3p5Kez+UMe1YYVhdqEO1hCJR9OCB/9YbfEUQwSNHCpZS84HfNpxq2nD7xq+bBX+zpvHeIwkhR/2GRJ51e2ykvYNhp6TXXQjT+ubIvAFpqoc4qetTqFEl7HUqquo0QwKii9SKrL2QD9HBWCsIXwppOT5JDsxVcC0FR6Y5o5NNT2ypEx46hVzcoRlOy635d0xIyTFMrbHPsiu261qE2pAEInLnsdxEqTs4gvUkbjSUONZ6tXzl7mxPRD1+Vj50GW3VWTvkoj60tIsm2QCND1seG6p5hp1yXijuli0vVuqHHy1moNhTOs0yJmockdUt8U208nz/Tx00onkWm1vywFy4WCDKS2YkvGDuQ3WMIpsmGHsh4RZk2uNL46451g679UD04k6GopOt7r4m211Opa9Om359tJbjXKop1FORVjGobE57pQCi8MsWDPnjEcY9rjMCiwxMQay5TO9bbV+Nx2uu2Lp7BhWgex9t+YTK8sVYyI0LYyuOx8fzMqry6toOympSFilrfm9luYAnEwpzRAEBOgs4C3TlTurPzgkyaF7RoJgzk4h7HhI4ustwJs1W57YI1kYBK2pSJ8aXqoSq7LItEihufySHbWLtrvhRCGf9kc6h7Abs8uWaMgoyb6KNTw00Au+heh7ChnWwdrZTYpzV7c1Tyl/r7apraYCy+hZF2JJuuvYYCAor6Gve8oLxKMyudoplKdoR1HTVFjZ4CaQyLfTacd4q3terkMNiZEz4hOGEmdHQTB4Kt6lpcIgzjaMzIhoL3YkaktjSO4GdNwkh7LdFK4oQ/dItmlftC7UzjALdHTbPZ82q9GkA55E9uGeXg1CI26GklFvV9jAlYrl2EJrDbI51IfTGBsUi1C3MXWGkiIcz26CapJ9ZiVI552IXGz1Vl75q5Ify2mN92tkJ7B8NHWlJNcCLRNQyhX5lFxMyrdvMHrncFI0kN0E6bdURyMr489Fuz5XXeYzYu7SZXE87y2O393xm7mpaD7kYPXAaLK39Mhjb1ZwvIzlc26WRLBUmvF2wPXi3JdDF4aJLYJs4pdMsjRlhr2PImlRpgtdleXunneh0bHhaOy3qINR1AkecleAwm2tbYTdFc4QXY8AKgMX2plFruTCCo/Ccq1nGc0qIgbF+xsuhpYOHU3dDrdIwB89dOmvndNpHWjH5ixc+Q6j7+drfMA3u+3Fa4zCNU83t79xSygaaEhcpWJAJzSp5+42AvgROlt/bfNKowrLRKXyLVbzloFbhcVwIb89ZRKNGArfHurkAHEjj+2ku8hel2LGOAkEp6YiK7HQJns1xYrBbpN8EwRnWidzRyvSq2wpxz2LHpx14JkHc0wxsfJ4QTu1prVCLG5XZjq7SUVF243A5eap0MOrZJLn8ijx446WfJgS+SsGgf72tNOIflNV1N6PdyEKk7uKMPMzarcFIcr03caQAUC2AdWBeNohJ8FcWVDPSTDA8KWc0hpDTLuTu02LwboAk5cVpPIS2ut+fD9PAl5bxQ26DBRuYN1pFSUMXejuzSRdWu/D5dKHOhdN7hBk5jUJl727ryQct31VlEOZ7nK1wU7OBcVddSuqtmgIVKlGhXZzog18teumc4d9DzBAP2mXfZdd+KseRz1ruVc2cyWBtySdP4cSpcl5vNvQsrgrUuHslPppmFbauoLLhoacdpVspSPkeNWo4aN+5dYoaIyPbaTlW3F7I9FiKNiLiDf6ELoCQrmX7t52npLjOW2jNj6dIPQUR2eb7MNwKQsMc8cSQbhOjZkoHaX6hYFrVGJuo2x0gywV1unVV3DXPxOU7kJY5aqHSudENrYGjvN64gKdSGhHCyYfbs+AWXD9Eprn6QYKU556CZ+iA3qsU5u+xSRR14GqrJl9sBOW8Y0JC8q+b3s/ve2Mkq+jaS+IyJHadcbAq7Ie6WrOj5V+cKBm8paxpZaSSEBJG6WyHWNKRMZrlhm1YLe/c8SFpjuJnWz70FSpfh3gjTi2QxxedPw0ascLTtEyI9SxrW38EsFb2Cpi2lptWe1aAFFiXOWWJ9chFiOhGjRCvuHzygAqBtP2Xsa7cdAdDskqv6CFTWJEoIUFmG6u9pe1HldqjYbrLaXs/fUlulhCekLhMFUc5wiL64u4vKnMLRxSkuJDKLlKNRL7VW80O5rG094tZStW9VSdrrtrwhzvikhfS7baGyxiVmq/I0TRPhz3yqlcXXtI97QzX9Mcjy9JamlHVhQGrRFl5+3V20M2Y5yVC0OUF4eAtOPZw7lGoDKiJJyU6GLPZw5ocXBj63Az/bgZTyf3vDFoNytFGXSvm9E77UvCJdd7SwFYvUwZubY2EXaIRgyljcTgQwTp5VpT9pPEU5FqDhyx2bEb1bCqES2Vq1JTktpI9jWrzg7L+8M5D8MyQdZLpVNyHXa2htjWVbEVNhvEXhfXLCE9vtVraLmGprIJKDZM04vlFOPU09HIDJFVcSx2yPwcS1bbGN9rLekzmH49sSXu6MmEEqmcdAe1oNVpWTCEj2xNUqaWYcRfL+mwOwhwsIulkr2TGsGXKhKKfU6yUDDdT+GqEqOaSPCLnLHS6Sydyz51Xdzm8mPAsfxF13CpTblauZhscDHEyu0gNDkxgj7ZRinoET9mqNVRo3Kw04ua26HA1WWeTfV6qRU7asAoIZk018PvjV9wXN2obUqmnaknayKXYUZaIjzsXVQ4LIeGgq1YVLyo0UKfPd5NfXsTxBET06G4T6RdMLTsb9bYaSf4LHIqfRxmoO5wM6wVw8db58oK22K4uhcaBJLeDkOEEaF67uiqu8CM7m9zkzEcOIq2iXK1iXTpJ1W8F8wTnjNUXN/qDK5CL+7LgL5MqoHe4qYIST8QsdH0tTu8LjSULIJrLWo4Thqwh2YNXIe8bhijPghE2l8FaN2fhO1yVE9dtovtHIr4Ogupo0ovD2wa1fjVTSRN0iCxOBwFN7+Evjrxty4aaWYML5SUBmNJyHzVtOGNuY+TJISyfipEzR4YOzYE87qHLr6XNFZCocedNxjXnaiViGQ3uLy53SGCdXM5Ooje2uI2sd3AObULVI5ArxK6XltT6VMBEx2w1Gg6q0aaVdIUIkycTZIk4Q3sFV5z2qDd/h51h+WtrzdH0BH6XnjcivVAHqS6zWvT7smdABoy+bht6piU8XFibfYQ3gJuzUhMJBqBctiP0h67S8oqryTJ7ZseJpNaFxDCv3EV6tUHQo8ob4NdNdRmxqNQDo7aXOGwuVa0J5/sUFRyctUQ/LrejCzAWdgv3EaFJgzrJ3jys6a48HXDytIxcsAmpRJXHQRjaqILq315zuMEDp2TkVWZtOTtbEDv5vWa2I2kSpo8BXVg6bRgN51/x/nr0Tb35iUpxlo4DNg59/WaMQyEN5Y7boMZKJuMTbe5pKDfYrwLjvI1lizvjbiXMQRsFRIoDxhbHtSYUhxRP9jrjbRPsrvg2qKPH9q+UJo1E2SXOmE4JS+IKzle0zG9b9Z3bHPt11Xtbi5lVRNhx/KdtyKmE7M8DjczEPxjUG51aTtZ9WaV13YpXXfwnTzEKRutVqvlQJsd0vEaenW8fTPuXAE0hkxEgT6VIQyOspUj4kcFRQ/xOtO6O5ZrnHSBLxMaegjUTtigyH5AdScG28r12VmtjkKLZ0bsjcWhwIrCHRRzR1yrWiZJpY33kdVdNPOCAG7nhBVphwGEwve9rDfacNg0DLrGg1S8WpgwBPUBwhs8ORu3frUmrOt6uzEOCdd2xbkREcBeUlokCiqTI4sUJc2z9Pl4x/1x14ugES51U4m2rMqg7AXsrWkLijNub7RHCQsJ2Fq3YWzE5zsSpHAIxe1o+0g/iTbEro8cxkZl1iy1nVu2DqSrmb9TfFe4lMfJswr3eJd75ODJmnwiGPskHrkL76WYDcG0Ia1GgnGqHcYmp73fqsXaQmp7c4vTy1Rs6GpfZOuzlzgxSRMs6gSDhm7TqcWQQ47ZgV5N4iXWTM3letzdSpWZ3YNuMAFS+t3Yimd53/c9tq7PZJ+LYHdxPOtkR4lVp+1yZyoiiK4N7BhDF95SvPMSiybP73kYbeSbTqwOa5L3HfMOyT7Xz034kuaIDJKhi32KJWqfeOZ+jMrtjpfGK5kQmOB1OHdQSAJenTZRezmW0FjS9d53nBjddIakZJjpcLcj4sm3oJTsmrjVfBcIq3WgCzDmJs2ge2ONOieWsomz06MQSeyg4SYl4mk8sJcCWqsQ0lG1tfOkFXxrIGRtXmJKDeKTcyDGut4n+ChM7hRPZbbRGxyHZDz1TjyyFxHfkLdY6djxwcfDJX1MlZMDJQk7qdZ0dTvL2gnkZexqL87MsYZ1rriOLeMIciDXXG3yFZCan6yjet3n29S9YaTqGpLdKyu5I9cZ6D1iZIdAB0hDzSDLt6CZO9moS1m+l7dTJXJwKsj3jJFW57trrieyIiB7JHoYXyOZabJatzQlhVhFgdsoULbTRmJZcZwrsX2811wq4UNa40MiCE71qSclZa3Cw9Y3Vt1GDpuqw6zxWm7ajY0gN35tElFdZHu6SvwhqaW8a5eJd0u7ruAOwwHSiSqdduT6shs7LqZ7V+Uukro1hDt3H67njOwL/VgjIyMf124VBSAzhH2b0ZKEiCa2HTz5KtK+HUmhJV1k/obdk3LQWuFW4TLAC6Tgpoh0S9C64dgowWi9tJbNHVsG5/N2rUEIgxkH6xAUKZJG+RRfMR+9ELFkbm7w8YQXFyznPCkKcpRzy+3dIIxq6QUnZs30HRvzOFqj7VlFr8Y1xkFbMOWDuZ0k72RNqzFpdpNH7g3dH8TJFqxqybDnQNp4tDFe0cY0AEgeVSwcb6foDNt35phoDUPEzYBpWWItOeFklD4R8BdEmAyDO2X0yXanho9cQlJFkuoNr2wlgq/EUnT0XL62NbbZX7HeKC2fhexrL2/DOjZLxiePp2TbhudJWU65lOY7yWJlGz0dyyXBEymmjSmBnxAKQ1vKv3o3KWbkIDA21vKY1E22Sc8xqG1rQ+ziEt/UJ4hUyd49QfKVX4l5TK7MlXcnJMjlaQ2SLjtfn6b47Cz7TVCnKVks6xrZ0AzRKC5+yXYIYXJR4He85a/DCmKcjZarqUrAiE2wAYs0N9+sb7aCDYTpSH3AnIjwNOIkjTgJEZITjp3xjMtXblDQaK6FVhhamjAWMXthljcv3rf5YCe6gzp6YET7tbs0d6uQrjdNmXL3Sa64lRIMS+bkmknNM3tuHerLuFwvN8L+1BxTm/RHaSo1xzwSSAj3qn8+0exSAs2XiskAFxE09u9EuhJgyu3c0hGWK029TsDp/TLhbmhXEJRFbdxo4HuMjySFDU/3fqDWyNlsBy9Zu/WlIGrZ33HwGoJwyItJuxuZzcSEG3vVgeahHyZHXXOCtqoVKXGpOKzQbrK76pIXx64RVqiTCxkCVfeycuTjpek5qyTbcbWdbHg1asYVJrr2enISzdrUboWT0wAPI4Le9Cx2Yr7ZlE5uKftdOp6sZGk02e0EcRI7qpubISqVuDlS3KX29VBIcqLR095xBlZ08qrSi+iEgm1jw3bFHi3gqavRUxTUqFkT9Mo4Eco60s3NJmqgmlQ5lOzgtXO+N2M7wpVMHDR6P237fDNS+0BnhUGM2P4MQcLS4vpdHwbehktu907ujciT/cFbbYjahSVkg14bHL7c68vRCkSi7ZY3392s8Mqpdb+kAbpTmafcNbCx7Vi6c5TSLreXFbbqLjl0CLwAbx1xJU4ULuUodjIQFGiasDQJh6qBh3umOlp7BC1Mt2UdmzwXPW1EE1dS8p5FuUMQ6vEwxVtlRQcHb2gptlvZZ2ldAKqUfNR0jusJg8rg5rPVOjFsoSVIZyOLRGlrrJNw+vnanKnNhfRuCSn0NRnbSxdbWpW+k5BVC41ktwsI0qQCh1wr0Eooj+Qyk/eoeZ9gpwhl6b5mcq65t7ubw1suv9M9BEYat5IyCJdYjwPtIFPdbmtRWjW5ZLZIE06GUqD95DqXsaGJ1EIqMzYJK2qC4724hhu/Uc2oL8iBFNFCYzZSc1t5sAmIc2sSSU03w1piZCF0+kuCqnbJlElYqwRzY+NN1fUsffcQqSMQOOVP3NbfCNbyVJ5WW2Rb7ehhfR5Bx6+yLbHBD2RGBx3sd7dJvCpNXwQbAzJSTPexqiPvFQLAH5IGmMvYtORscvLbYeqZKj3LToIXilYf6qtHgV0+fiRRAq+5u7eB2GKwU7YbdoIHoWG3gdV9YomcrPYShCTheslHIU5nWM15WBPdEekcBYfp3mVCRFMU9feX9y/zsdfbUeu/9TbXfJrz/+zg6Hn+8+WNjceZom97Hx9rffz31Pn1/UvjxkCZ56FYm/Xh2xHTPxyJffirA7155vh8MerLwfHzFLqzw/kV4Ze48Pq2a8bPbZk93tMAM5y+nV8tbOe3T13w/f1h6Fflnzfb+YWMz135ue7Lbj4Ri4v5BQzfi+2vl+HbASGYPIKIxG77GQT6s99Us5Fvx/3ANvQVfkVf/vg/bLQfvtgtAAA= -->
