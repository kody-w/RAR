---
name: "rar-cowork-cookbook-report-onboard-new-contractors"
description: "Builds a read-only summary report of onboard new contractors activity from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_onboard_new_contractors", "rar_sha256": "6f836d4bf291d42110050f010c83f6a4c1611399a71da1350be464aba651609a", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_onboard_new_contractors`. The original RAPP
agent is preserved byte-for-byte in `report_onboard_new_contractors_agent.py` and in the RCI capsule.

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

Onboard new contractors Summary Report — Builds a read-only summary report of onboard new contractors activity from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-onboard-new-contractors
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
      "description": "Name of the Excel workbook to produce, e.g. report-onboard-new-contractors-2026-05-24.xlsx.",
      "type": "string"
    },
    "period": {
      "description": "Posted period to cover; defaults to the most recent posted period available in the tenant.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_onboard_new_contractors_agent.py` and embedded as the fenced Python below (sha256 6f836d4bf291d421…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_onboard_new_contractors_agent.py` first:

```bash
python3 report_onboard_new_contractors_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_onboard_new_contractors_agent.py   # or on stdin
python3 report_onboard_new_contractors_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Onboard new contractors Summary Report — Builds a read-only summary report of onboard new contractors activity from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-onboard-new-contractors
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_onboard_new_contractors',
    "version": '3.0.3',
    "display_name": 'Onboard new contractors Summary Report',
    "description": 'Builds a read-only summary report of onboard new contractors activity from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'hire_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-onboard-new-contractors',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-onboard-new-contractors',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '0bf3267f44adfdd2',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/recruit-and-onboard-talent/onboard-new-contractors'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/report-onboard-new-contractors', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report against, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. report-onboard-new-contractors-2026-05-24.xlsx.', 'period': 'Posted period to cover; defaults to the most recent posted period available in the tenant.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives leadership a fast, repeatable view of where onboard new contractors stands so decisions are made on facts rather than spreadsheet stitches.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build a summary report of onboard new contractors for the most recent posted period available in the tenant (USMF demo data is mostly FY2017). Include totals, by-dimension breakdowns (by department / category / responsible owner where applicable), and a 'Top 10 by value' section. Output an Excel workbook 'report-onboard-new-contractors-2026-05-24.xlsx' with Summary, Detail, and Top10 sheets. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads onboard new contractors records, computes summary statistics and groupings, and emits an Excel report.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only summary report of onboard new contractors activity from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.', 'example_request': 'Build an onboard new contractors summary report for USMF from the latest posted period as an Excel workbook.', 'inputs': [{'description': 'D365 legal entity to report against, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Posted period to cover; defaults to the most recent posted period available in the tenant.', 'name': 'period'}, {'description': 'Name of the Excel workbook to produce, e.g. report-onboard-new-contractors-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a no-write summary report of onboard new contractors activity from D365 ERP data, with totals, by-dimension breakdowns, and a Top 10 by value section.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ReportOnboardNewContractors(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportOnboardNewContractors'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report against, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. report-onboard-new-contractors-2026-05-24.xlsx.', 'type': 'string'}, 'period': {'description': 'Posted period to cover; defaults to the most recent posted period available in the tenant.', 'type': 'string'}},
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
    print(ReportOnboardNewContractors().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916adOjRrbmX9G8N2JsX6pe9q1udMQIEBJCgAQICbk6yuwgVrEjT//3SSTV4m53z+2I+TSqstkyT571eU4W/P7mdG1c1m+f3ozAKRZrJ8uSOKgXTuEv+HIo6xQcytQF/y28smjrxO3asm7ePrz5QePVSdUmZQGmc12S+c3CWdSB438si2xaNF2eO/UE7lRl3S7KcFEWbunU/qIIhqc0x5uFLcAh6ZN2WoR1mS+EqXDyxGsWOEUuxP9p8MoiLIFKiyjpg2KRBZGTLYKinSfMelZl0wbgENRJ6X8Ay7VdXSRFBB4uVqMXZIvZjocJQ9LGC+Op14eFELROkn14CDHLCkUWTRwEbfMOrAtGJ6+yoHn79OtfP7wl4Pzt0+9vXuY04Nab/jBJe5qjBgP/3RgwN3OKCAyqJuDaAlwDzYABObjlB+HidfVzE2Thh8V//mc6OHXU/PLpc7F4/T6/zX/0rli0cbBoS+dhn+dUjptkwOr3xTIbnKl5mTp7vQGRKaL358zvkspq8Zf52c/PRd6joP3581sJVHDmuH1++2UBPPv5re7m8/dZSvXzL+9ZOQT1z798l9N07jXw2lkY0Pr9y+v6JRYM/D40CRdfjP2Kf61VB15SBUD4D/bNv6fqL3Evl3x5Dv65rD4s/lzybM9fgL7P3HOB3D8XC3wAZr69X8uk+Pm1Rl2C7HEKL/j5l38m1osDL82Spv1vyf31KTgGCQ+89XLJLx8e4fvrAnrZ9k3mP1+2Agnz71gChn9d7puj/pnsR2T/TnSWFEHzLZZ/Ku7PJkB/Wfz6T237VxM+LMLPb0KQgfKtHTcLPi1+f6TIrz/532/+9Ne/AdH/VzFG2dXeQ8KX3CmSMGjaL19+/al53P7pr7/+1FUgiwMn/9LV2Z/J/DO/Ptb5gwdfo37+41yw/rFIi3IoFt9qaPF7Wf2P+m/vC8vJEv/7/ebT4sdKnH/QYjbi66JPF/xQjQ3Q9Qc//vL2NwA8BbCm8x6PAX78x38slMSry6YM24XhlV27AAFukzyYlTfjpFmAvzNq1AHwa5MAx77GgfyfIzxrDJD4t//lPdD9o/dCd/iJ0l9eEP0FQPSXHyD6t/eFCaSWdRIlBYBffbnffy6cCMDwvGJVB01Q9wCl3KkNPoJi/jifLJJi8du/FvzlIeO9mn57wHDyxDydl2a8a7oseJ8tO8UA+J92eADVgzHwOiA+Kz2gS5gAnJ5xvymzHuDl7IUmTbJs4ScAUcAqT54Anvo0C/vtt99cp4k/F0+AxhdPHmtgMOCbOouPH4FRYZZEcfu5CLy4XPz0+99+Wvzvxb+a9RA+r7EHPPGKA9Bwa2jqAtRVl4NhIEQgqAA0HnH4/W8v1wIxBSBeELUkTILnZJCXaeB/9bOxWX7ESGrhBsC/wLf57NeZ55L2fSGFi2/6vhh35oUYcOPCD6qg8IPCm4BUB5jzzZNF2S4akHxNCOiwa4LHqr+5tfNQMQcF7rS/LRR+D1iozMD/ZjUfg8DkskiA+79lwfM+EFL/1Cy4ryLeF+qciYvKqZ0qrp3XGqHzjMvM66/pQLgzdwafi5ltg9lVj7J4ugcMAp7xXiH9OMcctBCAyAu/+br2Y4wzc6X54Mz6c9G8Ut6p51B4gALAolGX+DMR/NcrpZq47DL/4T+g6SzpFQX/FZVHDmr/pHl5tROLZ0+w+NxhCEos/r/qh2bzl+u1vlovzZWwWKmmbj/DMms9h+/ZRj5ULutnCX7vV75i0ldo/lxkCcixevqv58hHMF9jnnDX1cAAfak/5INMAmGZ5T4SfU7cup5LxPlcfOUAoPTiAXgg1gAVQNXMyfp1wfnpV01jUPrz9fd+4JEYIArAbJDMi6pzM5BoYRD4ruOlQKs5hF/jCrI+mEM3xIkX/8GqOQQgukA+iCtQFRyG4v0bLj+fflX9DxOfbc885dESdqBW64cAoEcwKzgHZA4VUK99tuDAzk8PIcCMvGpn211QLcDS582gDm5d0iTtjIxPvwYVwOSP8/Fp6Xw3GCtQIMBZoAyqDnj3UThzruSgqQE6AOwAdZQnBSB54JSXEx4CnXxGAYCyry70KfFx+2VQ8Ki2mZ2+TpwNmefMhP9MbqeYfgQL88/SBMjL5xGPdf8+076tNsueAbMBoAdW/Pr02Rm8P8n92T0svsr99A97nJ//vW3Qg66Pf0yAT4u4bavmEww/KfYrw74DuIKfujYvtv34AoCPAAA+/gAAf5D6NPjT4t/T7A8iXpXxaYG+I+/I/Gj3yqzXDziC/8jZH4n56edCD75DKVi+zEFqzWGbAL1/472vQwD5RTXAIDD4yYPNTJ8DYOwH8IMYfC5+TPW51ACvFNGcmk35AwQ8GgCQ9s+QfeMn8Khowdr+3CpGwbw7exRGE7x9Kros+/AG8DH4v+7KZgbK52xu5p0cqBsAkG0SPK4e4DC28+kft7Xa48TJ3l/g2PyYcS/emHnzh8J4mghM88AKHxY+cEwz8xwwcV58LiqnAVkKEnQ2pZ2qWffnBm5u+R54/uWJ5/+okDCTwB8gfyblJ6M40aOOPiyC9+h9cTQU8U8X+NZw/qP0E+D7WaBffpqp78MLXsARbBI+LL71+8Cs1w7ssVcuOrC5/XXea8x+fkyZT8AccPg26du/GbjB21//TK8HBn2ZU+EZ0L/XTp2xBWDv7OW/IzKgM1jX77zgZf2/LrCPGIJRHxHyI0a8j1kz/qmfngT6j2rsf+TXeeVHW/FfwCWh02Ugf9vyoWI+914gG2bW+QMnL5wepNIDA1+dSzszUfsnWgA1HkgO+HD28PfQfXdg+di5PRTOnPb5Dw2/v4FMd0DqOa9cf7X+YDgAvo/N3PbAAAzAguD6Wbbg2b+5KXjNbmIHtKVgOhUyOOUTboixqE9gKIogJBIiKOIxeEg5hIdSKIqzrEOjvoPiJOIGBEU4rkORKIWwDpD3LP0vc2eXzBqRLB0iLIuFBIohPvAwRvg+QzGUR9IY4rCuQ7ok67jfp6ZJ4b/MfJo1+/Db/mR2x8va399cigAjN0QjLZ8/HmZRcJN2p+0ZqqmgvNi8la2uTdt5xkEk+rGjMOGwH7kTuY9ScVPy+bRVj4h+3tqV2vIlsWL0LTGY5K4v5FtiSJXRkjjqCvJ6ecxS1MlMEpZ9A7Xo4uoT6URNjRSL8o0VMxksdbxkVh6PxxOC2e7KojEjEJ0zMbIwtKvIk1zmKL86xgOeOJWXnRyhuymyNlVepCGKtoFuV7m2ohN2dDyXVYdyktq+LyAN3jD9BGvnMsusUkCMAjvejtdUTqeVueqcleyMk6D6RnGXDvl55JTOsi7rmy+dzkSbFwbvJlrSdWKWYVuHtLqz65mMQe5WmmVurxI0jbDH18ipqQyI2HPp6PX4FaWZwGQbfD/S+zPt32GS6FFHaVj7JOlW5xHyJU6U7NRlum7mxFHK2OUEG9HUeRnKr7ctV8a2iBZtyiWkJbXIQZCjxFv2HX5HyRHShcy78ZNTG+LE7lY8IW+N9XUwLgpq7W6raNpd6d1BLpWh6SK5YbrmXNKBdqXPpUWbNH2XpF06XA0jXWHnw3JnM8NevaVOLO3kkyJiIsJdSCmg7nt11WS3YKRqZ4s6dyYN8shqZXHvSfmeGg9JgEC0AjHenUKrk1hkaeJKFyHVLb3eRbdA4I55k+qVdLC1Ybfs0NuqajzFRoY9k++wwkxo7ojJW1Je9qRBnRD5dgpOm0IOd7VtdrnZItGedHxPzw/RyTrnom1S+6hFjdAZ+dM+0RljyhRrXR1ue4kl2NXQ4Mgmsbeqk7AyBzm1lww+d4r4zTYlYngdM125XmOkIPjJzROt5W2tNs6qy2zuFDfOsGox2qmC5BgVco0bdoXGauifLuhRNwCgJ8sekuO7lZvX3aTVY6oX5gZFJUhRdowcnlbCqNNLMs4mkxumcFPus+sJUu6NQe/OCquZiRys1YwMK701o+kKNQcCYnUKio1gn6NEUGklFoxKyJGheahP/MlNojN8K6CdWlBDhp2Zw9AWCHWETRcWJ2ZFdVtxqLerfom06TpLTQcrS7Hky5sl0rfV3Ut5MaiX10QYwkSmTw2MM9KZ4W67tBs2ptvkV6I+2W6ZHFj9MrBipWHmVc+U4Xo3VeO2GeUEG/3luJJR91AuA2RzMDgPXkUrCRbv9hIjgqwU9P14aaR6uE6hcm0KbLfClYDhsnjbx3fGro+Tf7oNt+Wtk5dyKa1vpY112SlZmfGauI5r2GOsa7UfcjyaVKYXW+Ne6euqCifgALK7Ms7SOXfhhdl2YZx36voSCtnRse587jr8PRbFXuM2gu4cdb4+aMsNoe+7/DIcN5SVxVUCiY5oSmUzLN3h7lNlJvPKmNa5DNO9vbVOjDyKJ4CEB2eaJP8+IdCKcboGU2VtXai3sICqQ1n1BydN6bHqeioz9puVsJaI3e2gXcKbod5P7XXiz4d9iRxWUEKyg3phmjRB+XKiu/OldBnThdoDaTd7tSTExt4WmQ5Hx4IfpQRe4mdyiHQFsuNAHNAsWbNCgqi81DFHjaMF3l/WfXIjl+u6xFTOT2+j6RCp1BosQ0lh0+eCrzmhHtqDEfQTc9P8nFUgRRD1lmv18d4JsKZZxcbdVGsrtfglwUTeWTNSBIpSrBIZghY8CD52aMBsYBdf5VAkECrhjULB+bU0BiJxx7ukvDg3c2jG7i5ccAU/XA8uNCWbJbvFtjVPWlF+8go7L/ZD2kjphdro9rpXFELXXG5SOclg7Bxbe2POGnUGsWzKCJd+Faynba5YkutcEgik5ZYHxZdrFaJUHnlnKwcdjscEH5oL6sekLm4u8HKVmMFEXTFh41xGqQEIc1rvcIoY+aOedQ4TjnuD51cDguxPYxmUZ+s2WPVpuY+s2A3NhnTEgp+M3U7kg+OwxVkqCN2G9Y73GIHtLSsAmoqMq7ljMvl8uZQsfx3Oa1vPg26/ge5jJflsN0R3R0tXa39XueF+f4euDKCeAb9e9AFuN5dsi6eo1O8Vc7Lc1XqpNIkFc/dwPyD67pBp6Fm+lUbJ8w2Ol6bD59iV0BNzk6v6tu7V7Lj13DIS4j5V+rgibmvUXLLccdzzjq3CmVLyUqkk8WhQvIAUpHtB5R3cg8wc0n6/3u9OZbbLgLv0Disvx3Q7eU18J6lRV279krOLuObyFa20U06qvRpsj3QQA8IlL4mF5tdUWcvrWDIsqNrKGx9fDleZd11ByJmEX62agFO9JMIh3Ev63XA5drfD+izy92iT6ONk44owBNk9aUd1jKVD0hfklr5JI0eeYsUG1YOlS24aauDCnSemlAEjPjqEUnesU2XsfQvXLOmyFS+8kHRGhWg2Gp0bBw6p7JBYgq8cNzF524VlJNlSiCq8vUYKgPTJHj5TNLcqswOFiFHVFMcD0vrS+T5C1+No9Zy+PclnHWtlwTt5kulmcqpsg0w8NUqxSZQKMT19xfXRsqhyGREDGtXSxs4g3jgpnGG3SXLdVGfQCqQnUeY7Xogu57O7t9RJJER4fz4l0nmnY5GbnzLKM1zUUAXdzarB1zJCTUizwJfEejnyPmONZlkVTV+td/zuHF/3h2p/rnhzsI2xPJYMf9vdEAO6N3WxdgX0ZK2jcC3KerymeVdxglwmRZBYSCxVsBcd+9ist5gsIKvDWvUpFWiJjLKnT3u4smEoy4mIo5MGu9j3TWxbvoJJiZ8d91Q1hHW9JTQagezDanMp4rjtsN2WkdZRfE3PUkZf7mjIUb0eVtxRNiJRxKCwsFDqUkd4OIBsZi7q1ueCJS4iE4+I6/qs2VnfDMlBzzbKNmoNKxJI1pIo4+TfhnNqePqJV49F5xBxCRy4g6JdHpV5aYvpldyIu4u0RM6keT8sNdfVb3zA6kfPPh4kh5HuKISQ++VYyd6h4eOIAY2Y2VjkZF4BBp6bWlhvIwoyEMVGYRuT4CnbDmUeomR+7wEqk6lRHjKFn1ZJGTghKV2pFRsoo4aSZuvUcT/1NEyY0+4WIZcuwu7byTW1fbZ0WShl6mG5u8DxaqJIa2s0KT4dUnStYBOCkuu6QKFAKQXqXCfLeGtsKufirw6SjFj5gTc0NYmh/hDbmGLrYudyh9G7YBhDODUqCKPrnYqcQM7VarBu0WpVumV/WZVqtZZ0bXuTckUmouU0KGZiVuXFuMkMMtlnkizrox6jzhXDIssBTXyOWBuZIk7mQUcy0Ic2wc5iYBXN0nxp59pBWpc97ygR7x10EpnE7hBlbiJXsnXfK7G2IQkI3pAU1OII2N9AFaLDRGyp3XHY9Sf8dEcO9CETrT2/TXlygzmbKi1E/rzlWhB9V9158j7lS3x0OOOegQzjWza5wdrymBZVRWBYjlqoPDFdTENr3rYSaCnultppqyg2KLZ6A2IjrDIC46GEd2Di6GU1wjgrdaQbhV8m1X2FOi4PGmGRizJ+xfiAQjXOsePhplOHAd8PnHO/FWZk45zAuY0HTYQ4dJsx8WETphKiU0Zlp3dKHKB8rJ6WYphsKpxQR4akV+Vwpo+celndauBNkkZj2qFTsVXcbRqEqR1OhwJqJtS6ruMttc5N/kCxCZ+tuN2mho7M3hxhZnWs6PwIQMxSJD2hVCqnxsKz5aSTOviwW3vx8Vrl6XiIdRDd1Wl7SnXnou5u+zWaCrcNZWTJUlIz20NOUXpJtzW9rmLESroNveO8vZnk+Rpnl17Db28J24ChvTsgMEDeNQthmyTUlCYl5AG7kaRjg6Y22xkTOWGOEJDCFrX95fFORHdDc7TbBTKm9YQaiYnbSAxj1HBrREu182MdIk1lKh0ryz1tb2gihxPBsFqhLW1jUKY7nqZrrrphDG0CHKZucAUayjiROLK6NuWYuUs5bQ7p8RAzYJule8O95kiMGE/USJt1hkTaob+3Sd8I3IGgeDFvlzwAb5VH3Qi0ONTt5EbEkJs0Bcm1Usdgy1IeMKoc0bHGteuFMJqb2PMoQFdB56y11uCTkULwmnX6SQcF2BiguXcFHKXdrF2SuGZsheW1qdSNcSSUKxVsIkQlRs9Dh0FtEh4pyyWbCKsa399OENX4fKN2VqWzY5hyOeHLvHXZCD5227CipxLRgLlqfxiZ7dEUG59T0RO1vXii0uQpClPVGbn73qQT7J5Srn1HxONo3CNvKWRKZ7BqE8wu2FAkbLalhCUexnPUXrSJWmOXoY0jtMo69YWnscqwPSq7MKSxLC5sTN0DadxVDrwcL9yOk28oZaJnXzNBE7sbY/hoWocVwx1pzVWmimz6i3u+3Hv0enatnsf1vQcLrqoMuWpk7RUvRLcXohVtjl1w7X0yOMh7zGVddpjURjgEmzxa4aAcOG08NdSRdup7VwQMZo5Mj014hl+6Nq3v2sg4BH0lml7Lr+fa0o7QFbXIjSnlrqj1XgHxSoldrLVzoPScd4ONakF0tdn7S1btbAFurE0Bi+w1aJDKX8Jey+j+LS25W6HgpbHmJw2Pl6zNe0N7FjGZb5MUVUwZdEyoewyNe4c6N9hPrqXtlN0Fh7NOjTPSdTe1hlWONxQlfeI7mDbzTU4PxFIeEP/aE8fb2OIuJCwDTKHrPUxDKjycHbJIL+o1J3F4BQ/O+tROOOwbNegxbOrgnFY92KkYWGVD5qVxYnGvUKApb6sSVnBLkXUUKrg8udL5miyuh3HcMOpGEtL8uOeZ5ghT91V4Ra8GqgpqEUwlNjktqUER4y5PGzX0JnpHNOSA5xpoo23IViXSxPdYmrvptG915UDSfirxkX8JJ/hchH4VeLl3Sjyw18MDtWrTab1rbC+9Wp5o99urZxZ9StMtvL1h+T0Ifc8Sh5GAxfqksYm1oagOSTP2vMdsd99UTe7ZV2PppAZHAPawXR+zivEarvSVcEGz277htrczuW4wQa3PVtPe4UB0GpsUrZiKmAt2V65Y2Ay3kFlOm7gg8kvKMpCbCNB2og7ZGI3YmMZJL0gFSSgC0uLGaS0GIietAwX0unhYJ3G93RlocCkBa1xbgZd9XMojqSjBHpRx+NEOptUOOV4M/e7cr+TAdgfJgJiWPJ9OqKbB1i0ohBGm+hyCVlu7F7dbeR+fJdwnVhfKCgR6TennUBrCQQNbpe5mCrBp+1PpGu5SrceMpcxEoRxIpnLtsi0pjTTuiqVetKOnWsDCvZkz1EVHr37FVjtVKrdkayl4wIgZWLOL6IviZvU9blAv1bmC3a3ug0oPw64ddTT2OZ+AM2hUzpuq6NgOD1clcrufMA1COA8lCyyPcUwU9852hFuxCJLTBdfb7iQ16oFADIMIkukSXNFpJO7+wK0uBxdN1o668QCJcjBb3DXrmpcJAW8iIQ0vInveqVsndDUxseqE23s84t8DvdkDxAwwutyp1KnXHEQVSbq+FZSabAKXgFuvI/XRb0RB61mK9Dw88LRr7607z80gF2E4sbisMRalg/2oorin4egl3ZCaj1vVTeF6pNvzWN1xcnrchkc+TAN7mfdLBLnvzk4vndtr2zoVO8pXs/UucS3L9+FC3rFVcfULs9j3e26vVD4VXhlJY6YVF6TnlXtaUTplu4jr+Ui03p5JtJwolkFKuMenZdJGR3TlpznLyaoESSyzIYKdoaAHiRjYlI9RFE6b7YFEyGPbbe8S1hlNl4Cu19RgWVpCm33TJsR2z4lNkNuTTJ/XPt0NO2m4rYe9OCI5g/i0eO58H2P2+IErdxGtjRzGpZtyl6qICski5izhNV16V4Wpg+EmDATb0rCr0IhrW9DJ4ghPlDG28rMCymn9GF180OwEtMaXw9HFKLetzlmhtK6M4W4utyhcVU7lHhS0vm0uNt1MmHJ3BvSWNyOB77zBK/j+Th9Ik8ajibykdRGUu2Mvmuc1qd1H0faNw+RtkJbc0G28D4lUMLCpORlwveNEvsjKICUEzCJE0SBJlzoQcYv7plGFvNcL+1SVKDFn4qtFOxBqFne6dc29Ed/NgvX1DY6tz7Q1IfsOgNAd21/P2TarLzFyyI3NyZBNXIp8ZmiSyLtwAwtTZzyDy6u0gZyy70gfW075uZbX2x5jsEwrfXskfTdIYSQ7ohmzT27nG0mDvS1inNXSP8BifzNoAFw8bckYaEk8RdiuhPORbGUCdBqw6rd3L9DX7oaMEWqkkH7vZOm+2YZpZ2DKEjlurwqmRZSF9J1zVlk2MnCtHDl2iGxy69L8yuDZA7UtNwUfisMSJP6J2KcQ5rh+L5wKTda8O34maBls1PA417SOOhtQtEFKKk+wdZeGY+Bw1DjU8Cm12GJ/NTQW9vE2swoP5C4eljV+8gmeDGFA/JeMK2DGWWKoZwSxxyTbHl8eBzrwjZb25TqTbtcuT1u33jH9UJd0w8Zlt/M9OL5orF9ZtXoidj2HFxPu1f7oBpRMVvE56SE7rs/qiA0J2/chTVkxmycjvcN5Ywz5utFav4DWRhEEkJBw5mj7/EGO3A7UwwoZRF3gjiiygo4ZZjrehp3oW15cz0bUkJ5+x6tiwKLaNpHUvmk16EEE6qALztWbIPKAF/qmxqExH1zi7LKAg8Wg3h0O+Hi/01dzF1BZYCblRhaRRnFr3Oujk5IwArNTr6hcJmSMcYKZIRseOrOhtwMcDZQ0I3XiyvuVRUEK6Jf26OicXYXrUCYo7WwebWggYio9BmuU8QWY2MZnDctsn1sul395+/D2/fXb23/zy6353cv/s1dAz7c1Xz/NeLxVDBz/02OtT/9dhf764a32EqDO8xVXk3XR65XQ373g+vivXxPOc6fnh1BfXxA/Xzi3TjR/GfyWFH7XtPX0pSmzx0cZYIbbNfPnhM38xakHjj++En0uB07ipA6+tOWXOmjB2dv8od/8nUXgJ0779TJ6ver78Oa/vgD6glPkl6CuZgNf7/SBXfg78o6//e3/ALI+s9nMLQAA -->
