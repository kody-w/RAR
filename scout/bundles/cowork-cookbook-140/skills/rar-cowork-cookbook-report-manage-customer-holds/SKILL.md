---
name: "rar-cowork-cookbook-report-manage-customer-holds"
description: "Generates a read-only customer holds summary report from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_manage_customer_holds", "rar_sha256": "a4ab6f34a4a37eac03e59166bd0aba808bc4c27ee9063044ca3a1f1c99b55bc8", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_manage_customer_holds`. The original RAPP
agent is preserved byte-for-byte in `report_manage_customer_holds_agent.py` and in the RCI capsule.

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

Manage customer holds Summary Report — Generates a read-only customer holds summary report from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-manage-customer-holds
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
      "description": "D365 legal entity to report against, e.g. USMF.",
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
    "output_filename": {
      "description": "Name of the Excel workbook to produce, e.g. report-manage-customer-holds-2026-05-24.xlsx.",
      "type": "string"
    },
    "period": {
      "description": "Posted period to report on; defaults to the most recent posted period available.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_manage_customer_holds_agent.py` and embedded as the fenced Python below (sha256 a4ab6f34a4a37eac…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_manage_customer_holds_agent.py` first:

```bash
python3 report_manage_customer_holds_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_manage_customer_holds_agent.py   # or on stdin
python3 report_manage_customer_holds_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage customer holds Summary Report — Generates a read-only customer holds summary report from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-manage-customer-holds
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_manage_customer_holds',
    "version": '3.0.3',
    "display_name": 'Manage customer holds Summary Report',
    "description": 'Generates a read-only customer holds summary report from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'order_to_cash', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-manage-customer-holds',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-manage-customer-holds',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '295373ee63d64286',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/manage-credit-and-collections/manage-customer-holds'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/report-manage-customer-holds', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report against, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. report-manage-customer-holds-2026-05-24.xlsx.', 'period': 'Posted period to report on; defaults to the most recent posted period available.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives leadership a fast, repeatable view of where manage customer holds stands so decisions are made on facts rather than spreadsheet stitches.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build a summary report of manage customer holds for the most recent posted period available in the tenant (USMF demo data is mostly FY2017). Include totals, by-dimension breakdowns (by department / category / responsible owner where applicable), and a 'Top 10 by value' section. Output an Excel workbook 'report-manage-customer-holds-2026-05-24.xlsx' with Summary, Detail, and Top10 sheets. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads manage customer holds records, computes summary statistics and groupings, and emits an Excel report.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Generates a read-only customer holds summary report from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.', 'example_request': 'Build a customer holds summary report for USMF for the latest posted period as an Excel workbook.', 'inputs': [{'description': 'D365 legal entity to report against, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Posted period to report on; defaults to the most recent posted period available.', 'name': 'period'}, {'description': 'Name of the Excel workbook to produce, e.g. report-manage-customer-holds-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a totals/trends/breakdown report of customer holds activity from D365 ERP, with no data modification.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ReportManageCustomerHolds(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportManageCustomerHolds'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report against, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. report-manage-customer-holds-2026-05-24.xlsx.', 'type': 'string'}, 'period': {'description': 'Posted period to report on; defaults to the most recent posted period available.', 'type': 'string'}},
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
    print(ReportManageCustomerHolds().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/9V6adOjVrLmX9G8N2JsX6pedgHVcSNGQggBEmIVApejzL7vICH5+r/PQVKVl3b37Y6YL6Mqm+2c3PPJzIJf3txxSOru7dObHrrVgneLIk3CbuFWwYKtr3WXg0Ode+C/hV9XQ5d641B3/duHtyDs/S5thrSuwHY+rMLOHcJ+4S660A0+1lVxW/hjP9QloJfURdAv+rEs3e4GFjR1Nyyiri4Xm1vllqnfL/Aludj+b509LKIaCLCI00tYLYowdotFWA3pcHtI1dT9EIJD2KV18AGQGsauSqsYPFxwkx8Wi1nqh8DXdEgW+pPnh8UmHNy0+PAgYtQNiiz6JAyH/h3oEk5u2RRh//bpx58+vKXg/O3TL29+4fbg1pv2EPfgVm4csi+NdrNCYGfhVjFY0tyAGStwDeQC4pfgVhBGi9fV931YRB8W//mf+dXt4v6HT5+rxev3+W3+o43VYkjCxVC7D+18t3G9tAA6vy9WxdW99S9FZ/P2wAtV/P7c+Rululn81/zs+yeT9zgcvv/8VjezW4CPPr/9sAB2/fzWjfP5+0yl+f6H96K+ht33P/xGpx+9LPSHmRiQ+v3L6/pFFiz8bWkaLb7oCse+eHWhnzYhIP47/ebfU/QXuZdJvjwXf183HxZ/TXnW57+AvM848wDdvyYLbAB2vr1ndVp9/+LR1SB23MoPv//hH5H1k9DPi7Qf/iW6Pz4JJyCygbVeJvnhw8N9Py2gl27faP5jtg0ImH9HE7D8K7tvhvpHtB+e/RPpIq1ATn715V+S+6sN0H8tfvyHuv2zDR8W0ee3TViA5O1crwg/LX55hMiP3wW/3fzup18B6f+RjF6Pnf+g8KV0qzQK++HLlx+/6x+3v/vpx+/GBkRx6JZfxq74K5p/ZdcHnz9Y8LXq+z/uBfzNKq/qa7X4lkOLX+rmf3W/vi9ObpEGv93vPy1+n4nzD1rMSnxl+jTB77KxB7L+zo4/vP0KYKcC2oz+4zHAj//4j8Uh9bu6r6Nhofv1OCyAg4e0DGfhjSTtF+DvjBpdCOzap8Cwr3Ug/mcPzxLX0eLn/+M/kPyj/0Jy+Im/s1EBon35CtJfHiD98/vCADTrLo3TCkCvtlKUz/O6apj5NV3Yh90FYJR3G8KPIJU/zieLtFr8/M/IfnlQeG9uPz8AOH3incYKM9b1YxG+z1pZCYD8pw4+wPNwCv0REC9qH0gSpQChZ8Tv6+ICsHK2QJ+nRbEIUoAmoCw9KwSw0qeZ2M8//+y5ffK5eoIzvnjWqx4GC76Js/j4EagUFWmcDJ+r0E/qxXe//Prd4r8X/2zXg/jMQwEV4uUDIKGoH+UFyKmxBMuAe4BDAWA8fPDLry/DAjKgUi6Ax9IoDZ+bQUzmYfDVyvpu9REjlwsvBNYFli1nq84VLh3eF0K0+Cbvq47ONSEBVXERhE1YBWHl3wBVF6jzzZJVPSx6EHh9BArh2IcPrj97nfsQsQTJ7Q4/Lw6sAipQXYD/zWI+FoHNdZUC83+Lged9QKT7rl+sv5J4X8hzFC4at3ObpHNfPCL36Ze5or+2A+Luogqvn6u5zoazqR4p8TRPPPcRqf9y6cfZ56DxACW8CvqvvONXrzHX8bledp+r/hXubje7wgfwD5jGYxrMReBvr5Dqk3osgof9gKQzpZcXgpdXHjH4rPN/bl1ebcTi2QssPo8YghKL/4+7nlnVFc9rHL8yuM2Ckw3Nfrpg7vNmVz1bw1mCWbRHuv3Wl3zFnq8Q/LkqUhBP3e1vz5UPx73WPGFt7IAC2kp70AdRA+wz030E9RykXTeng/u5+or1QOjFA9iAXwECgAyZA/Mrw/npV0kTkObz9W91/xEEXTCrDQJ30YxeAYIqCsPAc/0cSDV766sXQYSHc5Jek9RP/qDV7ALgOUB/AYRIQaqBevD+DX+fT7+K/oeNz/Zm3vJo/UaQl92DAJAjnAWcHTK7Cog3PNtqoOenBxGgRtkMs+4eyAyg6fNm2IXtmPbpMKPg065hA9D343x8ajrfDacGJAMwFgj5ZgTWfSTJHCslaF6ADAAnQM6UaQWKOTDKywgPgm45ZzxA1Fe3+aT4uP1SKHxk1lyFvm6cFZn3zIX9Gdxudfs9MBh/FSaAXjmvePD9c6R94zbTnsGxB6kEOH59+uwA3p9F/NklLL7S/fR3c8v3/95o8yjL5h8D4NMiGYam/wTDz1L6tZK+A2iCn7L2r6r68Vn+Pn4FgY8PEPgDzae6nxb/nlx/IPHKi08L9B15R+ZH+1dcvX7ADOzHtf2RmJ9+rrTwN9AE7OsSBNbstBso498q3NcloMzFHUAgsPhZ8fq5UF5BbX5APPDA5+r3gT4nGqggVTwHZl//DgAepR4E/dNh3yoReFQNgHcwN4RxOE9gj7Tow7dP1VgUH94AOob/w+Q1V5pyjuR+ntVAzgBwHNLwcfUAhmmYT/84ph4fJ27x/gLG/vfR9qoPc338XVI8FQSK+YDDh0XwgHsQiEDBmfmcUG4PIhQE56zIcGtmyZ9D2tzWPbD8yxPL/16gzVwA/gD3c/F9Vgo3fuTQh0X4Hr8vTP2w/UsG35rKv6dugbo+EwzqT3OJ+/CCFnAEg8CHxbeeHqj1mrIe03A1ggH2x3memO382DKfgD3g8G3Tt38D8MK3n/5Krgf+fJkD4enOP0snz7gCcHe28p+KGJAZ8A1GP3xp/8+S6yOGYMuPCPkRI96nop/+0krP0vn3Qii/r6y/M35d/Q0YJXLHAsTvUD+ELOcuC8TDXHP+UJEX7gUE04yAf8EbMH8gN6h/s1V/c9dvRqsfE9lDzMIdnv+A8MsbiG4XhJv7iu9XSw+WA6D72M8tDQzSHzAE189EBc/+rWb/tbdPXNBwgs0u4XrLCCfAEadC10fwkGTQ5dILENdzaYT2fMLHqDBkkCWOEITv4i4aoT7DeCTp+TSg90z1L3PPls7ykAwVIQyDRQSKIQGwKEYEAb2klz5JYYjLeC7pkYzr/bY1T6vgpeRTqdmC3+aO2RgvXX9585YEWLkjemH1/LEwg3qwTXnj/gzjCLxurxKKB91NlAvZWoYkxhs3Xz0gmM4ansfbfF33iOHgDpd3epPb8XW35HY4q/QVU5myXpQa6TQiNjAIv7KmPXncJVCUBhtcoO/TSG8G+bo3T+bS2Hu3XOz71LCI9u56vZyKDCUq7CDRNgTDJ4wupLy/FmLL2Q2bXDhEJ+UgIJcYfa3vHnrKLXjbF4Tjba1qIo67M9FblztCRil6suJD40aO3uhHdWkI2kFHz6MmZrzQM4gUcQlLnrccuWrbm3haavVlimQlN++cc3L8/V7p1eLW+qNMVHZS9fF0OpRcSlEKjdeVyt+KPaXSvIEuoUiJaNJR8DsJiSQGhxf4Em4hGsd2ulUUiZ1sLfKmNm41xZ2MtHvpcN80Zlfz5+WJ396LsdehgZC5vTr2DB0fzlLBjSlnm9w53g43OISl4832JbM83tqLsW0niUsRSeNWkXfYml1r9tf9hpLUtj9c+zRl6evY4zUZjhcCF7SlSsF3oVbya6brObc0t8Z2CO1NhRqilp8SkdfhzXIl0Lkr2iFWWnrDD9PxxGvOxYryDEHWSc3e2VivJr9JNk7ItAHoCgkvxze3tD3LHFe2RFkjRWwpa6TXeUlGuZXE11phuUlxsqSNv7TXcBeQujOESXtmtz26sfw4kpbmyeOnlNSr+/Is4I0Jh0KGmRUuOLm9zU9OceaOHbWX1QLzfSwT8ojzB31bjCcpux1DJTjs5YklMF63hIsew22D2zWn3vt1kmqKcCGbaJ9yyVDqV1ytqsRRJS1z+URprfhUe1a+2jMl2uJ1ITRYzXD7jeexbrgc720d5w4Lc/yZPmVj41e8kzNRJmTHUrmnBk3oZ8KceqFKEywhN05/ZO9qzaxpasSmMUhN0iWrnik5EzpQmyt86+z7dZmGvBmGXpIXTU95DXQfDEcsW1yZwtMVlU7xuRQGCq4LOM4CuK+cHEY4rmGOFY5A8LW/rI9Uiflrw0CG3ApyfYmBCcoY09rclY2DkQInUef1acXHMHcqmQC61IeK2JiW6OdKWTgynGjDtdJkp03vSXMxgj5jM4eMd3zpFuY+O52adKklxKm9JcoVIo5xzJLQei2sl/v2uh2ug6KtYy+926dzsssh5+yU2J7DDyG9LjTxkjC0XZm3wGyv6ao9Clc2T23OPFCW2qlNB684kSZEaqePgTiuep/2hjjK0DNfbd2xg2PpuMYc7naSLzI5jV1ZQFvXhj3SlMyJKfB+1SBFxlObVItH6YoL6L1e3bgz0fA+T0GJZ1tml3SrWyvBhzhOYyNmTL2NC/t6BsWV6VK50zMXp1d9fMmBc87bBBPqKXJo6ygPum1SCmVPJ51fDZJ4rgz6SA5FKIk8zdYWEgc3Rc0oa9BcELErxURWF8PwIdo7DJVzGNT2UFE55vIwB/rc9KjvN3fHX3s8y5JmRGwu10YXLlcZTTYC5+867nLtDn2vo7WvanUiBykFr23baLc8Yp6FFXriyW6vp+akeSxhShd9YCg+i7syi3yHCYI4PkaXFGmOzAgfIG6z1YrVsJmuYVYpELrn3arZnvJgs+KvLH70K1Fk1uLgOqS83F4p2vBQqt9flVD36tVBwE93TgggzzLS676rlGCrSoxVxU7KFCBW3THhV5hRcEJG3mNNKa74WspJZQqUy1qzNYFCRJZQVFu7pqO1Vl1eDe1JUXoyk5eR1TEUJSLW1ArIMddMu1QxBBDLcXHJ0drmGBiJqDd3YXdjakFodnqiTjXwdNryN2klcmUwoLv+yCFGqzkrN+76aJC1C19udiGKgG4cObDiuqpD+aLTIHZO+cXqYgvtWAwDZcGDHLrPLZqoDadilsG5oe9BdZ8QxHaYVZ5CmZ4ZEr09Ws7Qb9gMx7ZEUBx3SgZrNGIel0tbDYYNy2/GC7TrJpimat7cTDC3oaAlDI87tKV6UaJ5m6TI1lL3q1pbD6PREUdnW/JAOamxpOl0YrX1NYpTig00E8P8VTd66eYsVhe5sETVguJNcskPl6QmWh7VVsza1BTWFWRmezBZoT6kyaSj/CauSM8phC2MaMkmBgByO9xIsa+lk0kmPMHmorAjOb9ToATFr2pdtNfGj9YAwaDd7pJO+NErLAHZn6JmuSNtJxyckuR14no2ZRbKhYK18MItE36zKft461j7qtztDjuZbHDi3kK8EEKipubOmog931rrq16p74EEVXXs6WyWLukol5N6b65zlzF9X7seiDNaNLsC41pGdJYuTcBm4J50ScbCFsrb+pCrSEprq8tJ2u1d1TAOHcXYxImN6VZiw/q2hS1ra68EyDpJS0kp8IMKw3vYT9jzrWaE9VS0WmUf1UsO+orLtmukfVqYGSvVCFYkxOGIyMKtsNidYvUdL51Sp9j7vJfuVyKyMpuDasV7jLvUucGJVB1v96zF77nWYa7nwaztorHX+1WBWqC/uZNnVYPkwBCnOt1iaK9KVDGplekip02PnkXd3WWotxYgH0ftzWqFGJUia5atB7R3tBPVQohbxUiZCGu5wG/9dMVeeiqRSHHsI5Fbn0j6vA5roylVs3foa4dxFRgktLUU+7l3VIwtuj+ciXSIk72z3WTwKVtqiEzzNcdVd+J4plqRP7KQXSh8uJ0ETPFdsRQjtGVVKLTTFI+M25Tvj5vNhqXk4Xy/anKcccLRb7HtZc8YjZqpxKbhmrVkJBQE3xF8o2wuvplJcj551Z5hklaoTWXkZbY2NM+zErtMbdbXJzZvYgVZugekONz14mKmRHplXdLQkMk4FxhrMNfosD6d5Cu1XrVjEN9ipx7ZrIqu9oDfXZbZ3y73OM7iwjfKLu/v0DbROT9xit2KEIqwJDI0LwOOgEtqoIV43TlHI7kYEM/IOBcFrEkhF3npexYO+h5cXwuCbm0dFtV38g7Kp2EVKlg4un1xlRkEd+A7Td+WYqsTzqhC94OzLu8b2MAwVIUkZLN34JTTl4Qphnm+g7RsK8OYfsXIm1KRR/1Y35dmp3Egz3eZW2isKkjIqVQ3+njIErs6NIalCim+7moiFZeeHnhUbm40JdpW7RI7Beux0BM2X6nt0ENNr634xF3XRCmMZ3e72a+mo3gso4Kv93dDTKKqVAeN351axXPXp0oVLc/ivK7Lz/J6p5/hSzpSynlP3y1Lt9epTa7AeEwL9m0lTutdFdYnkmVPo9DmzVk2UhEPFaqCQVG6MZEBneBlpe3glDFvsnEYaU/z5I3p3pn1NrGINNcYOSMIdykeczXpXMnTtlCyvYu76ia1PtXoK6gMNrbraWel27NLRkFsMTldoJvVrwI7U5eqGrbyLT7krSjw6z2iqlQ7MSdlrwesl8TW3sPIZrXhqEagD6OQn4s1ISgZYi8zlEXVIdlldnpIop60uXuFinh8S6D79tw3LD0UVL3TkA7WVPTai2tnzASjlwmUTQ5nODESnKWEgcmWUjz2lBGtD8227eTQcTZYTLGbip3WXm57vrPmcHzJpCKskpju7vOybtxNa9qIvVeRzDZ2oNFViViwB2tPQVCEK31wUuw2c4S2adaeUCI7nxqaTlqVXldfbL0+HyzJ3qYyd9ZU2T7xOkiwcgyvzvkKGs0pDYXYvlprz3LYbanx+9TFbksDTEGXnrn5IcTZXTatdXVTidnyGrvH642y6J1CR1V2bpqAKAr+qJvbc3f2/KtuO762E0n96iFUSBpbXD1g5q2OG30gB9O4FdlQEFXe9WOzR4NTcrZb1k362oIbWy/IU2teceSqwNMAH7i8dbfCSuUK4Mzq4hwOrKENFGY53HQ5MXdmJceeGgeYvecPTomv6/0KtGhItGLvldVzVDVG1R4d29CEbF+Qrf0Btpv96s4deSkQ6/vKL1gqTnjSw0U98lfVRnfx8xQ4hS8Pw5bn8e1+M8ouhni7zemkVgTfib7qiJI6IeVonaqKYLotZPAqKUunC27bIcxsiL4+s8RdOziclIg1CbrNlBkxVSacc4D7Iq9yKxCQCXQjybGUGr0yvLOTh/F5vavP+KknV2SY7IIOprvMt+SJhymyiBipvy7x6H52x5tKr+X7vpGtoWVOe4+/5y5AomIFRjyYcM0h3hpXUu10QjEPk3pJldudbwXPdrVM2hpkBOl3OXPuKWobNmk1GxU5xJR7k9FljWqd03CofgyOjsxcUEoSDvsINMZS2ZEqJOhX/nAruz0plwEBZszavPD60ZhOouvxQ+1vnSprtscuu9CZZ98x1DOH0sCVKzoZVw5ukcEPW6JhTIoyNGVH7iUMl0vYJHpkGe1Ssw13scUXEKp3Pq5vfeN81qMBIY2yDxkRw8+35fKAjjvXwcTsHAWgFZEQt8S8Bi3QI9QorX2f7Du6NJGjhq5KCcxqu6OJsMt6gyhpw96m8428pBWOXU1cYaQlSzqktRRG1CNS2OzjzekoDoaPL2/KVVw5NVRTy8YEiGSBWD02wRnToYunJLYi9WG0ZWTKktr9jaSLdmc645GYnPMQ8tHRcSTc7HoacQrqAnsUS8s72wOtjB9xmFhfd8MlIjMKhjcRvNUAaPKeQkI2mKWRtZzCR6zGiwkMxx1urhX10u9H99i6o+H0bqwo3BIIPTSOcsBPkquhUMn6db7ZCmddq10ig7gsX18NbpeFGBswZCtPLtm4pVPdV5PlifKR3p3VcOj36yTr90EBWfTVue/kUDhER970K0rApbXEKAW1MlaTYTqgHyT5CLqgKIqTXiHuVvUZhVdCVXmBcwA9WLYVCdRa88pkVyy8bHiG6pbeROp4eT7vtP4QKpqLZSpdaVDaDiQHdTvqIO8I85J3B01cybq4osNoxOSREu7ENKRCte7dJbqzVjmaI4lFiSXatZgF+mVWDo8+m94Y1TpQTqlRCuaecExwsuudRg+3MLxeJgvnIboGjWZNgl5owg4s6LpuioEzonYuricu1pZTtmKCENtLdF3uT2ixaVzn2Atig68y99r6wWrvTnucTzrOuFRBLu62/ZGIVphzOHf7G14cAsesYdhqMB/fwxeIokh1TBlAPB11KBrBrHLPJWZXiugNutkxnAe7xAlMbAeVV6q4lj6wp5LdKaTiHByj+ZPg3zIVkTHSEtLudqhJt0ttPsyHbY5l3RG67iQdQLpxd9ugY8pOJIa1v8Yw57w/lxvnQgog6pe8XMV7NIrPUZZ17JLtJgoeUmdUxCPDBGBImcpzOfQRQ7Bkdz8OoFMZJT5ENuna3R/pLY1DxR5UfttNpiaPr8yWvDGbrrijJRWzAhuPy8umuVDr2FIVqoZJtgFjnMHb9G64Z1LtJmHj7WiH6089LZyoFV9ePHqTCEhk8EM0NPczQjbngF/6JEaaaU0y5THcmdToh7jOaMbuDo3r4wEPu1ZVNp3VQiifHakJjOuDZ4U4jmvMBN2Cc7ibXDNn5MLluxOEosszt77TiFtIEn+mNxd2u403Vem5eOcMuJANg9tsJikzBt+ZWmlvjM7SQLgqg6pddb2ATunQBa2S0cKRvnHrMD9zoONZakvbQzw/QGJePJNofVsGNFLDF+W2Ap2xiZhBjjFrSRagxiA4Itz7B1QVCILJ2QRF4eIgqiRCmj0U3QV0FOgxzfKzYcGSIEA7pR9iorlAKbbTjRtL4HxAjVdPuIKZFMxV15JGAmp7HhWmXCm4uq67EZcnHVvnSi3mMnKCpG3oxDC/q+3sQHdhvNxcCWbc07AMpLZPYI5ZE/5WwpgmKCqopDQzdgLa5UKCgjhXOjGBjNHN7T5aQ+E5w102lxGCDWZR8y6Dbw55hJEe7wyqjRqWTVNFbx+97Owwrd+Q1HQy/RuKXsyiPadtlkU7zE0PfCeQfLbE6ITBiOLi60ZDadYeTAbFqk2MGybrtEhKNJs2JtIzgq9jXtk1ZpUc8aS48X2IGKE+SeglWjbTOoAuza7RSK2CIBXDb2DwON0QZcRDuceURJEM5Xzd1OkhP/a5GUfaiiIScbsmpnvMXLDLZQ+rnLpjLM0Isn3PFpFi6f5+PTTDPlCXnleQI2ng2vbunq7hcR921ZgHlqyTzb3J+ppJzsGJI3S34W+VtUuShkvcNrvXZws9Rkwtj5x1B60XfGBzCw5r0rMurjzJ9GbUp7Vbxr6Y33PvPIbJpJGXrr+FBHrmDmOurIS9T2vsSu92wWF9QA2c7LcrIRg3J8LPS9y9n4a7mykSpN12d6xeRgJeJd1xxGCThTo+r5kibXe9WV3Ddljer3cUTNeTHIU+jA1YhZ2s6H4f6gEq+4AO4PKGQ5gGMyhTgqZ3h8r1LlrXVEJuaRbJkSjA0iWjSznRNhfQhnd7eBmuqAvhi2kXKkQYDedj4GSnbu0REcXimIT7Hgq5mFOTZBOBkUWaBqW0jT6AaTJdyT0Rik5IF1bXxoFWjYMC+mGq3UwHX4xEr9bXq1Wgj9FUlmwL5u5qrNMbB930e82MO1lDaZ06FZ2QhkdChqw7B+aafOPoiL8LYljSxL3gVOeLuPNH0LhlqIx5HruPLjhsXtDmuN2NRy+k3cCruMs9lNek6kgaNtJ4hxy8uHUChCcmGzGXqVTu1K18NDR/J9toQIwwPFWEzK5xgk2O0RTvo4ArT1rNncqKTggpI1B/P3XUJsFbcaIdYyIUeE33Z1qCdXW1Wr19ePvtZdvbv/Q11vzW5f/Zy5/ne5qvn2A83iCGbvDpwevTvybOTx/eOj8FwjxfbPXFGL9eBf3ptdbHf/ZCcN55e37Y9PVF8PO18uDG8ze+b2kVgA3d7UtfF48PL8AOb+znTwP7+etRHxx//+rzyQyc1F0AhB7qL77bJ2/zN3vzpxRhkLpD+LqMX2/3PrwFr498vuBL8kvYNbN2rxf3QCn8HXnH3379v7Q8KfCDLQAA -->
