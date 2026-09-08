---
name: "rar-cowork-cookbook-report-budget-asset-maintenance"
description: "Builds a read-only budget asset maintenance summary from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_budget_asset_maintenance", "rar_sha256": "ad115f36cca85a505821d5880868c8fd857abcabf24599110422e0edaee1b032", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_budget_asset_maintenance`. The original RAPP
agent is preserved byte-for-byte in `report_budget_asset_maintenance_agent.py` and in the RCI capsule.

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

Budget asset maintenance Summary Report — Builds a read-only budget asset maintenance summary from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-budget-asset-maintenance
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
    "breakdown_dimensions": {
      "description": "Dimensions to break totals down by, e.g. department, category, responsible owner.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to query, e.g. USMF.",
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
      "description": "Name of the Excel workbook to produce, e.g. report-budget-asset-maintenance-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_budget_asset_maintenance_agent.py` and embedded as the fenced Python below (sha256 ad115f36cca85a50…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_budget_asset_maintenance_agent.py` first:

```bash
python3 report_budget_asset_maintenance_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_budget_asset_maintenance_agent.py   # or on stdin
python3 report_budget_asset_maintenance_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Budget asset maintenance Summary Report — Builds a read-only budget asset maintenance summary from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-budget-asset-maintenance
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_budget_asset_maintenance',
    "version": '3.0.3',
    "display_name": 'Budget asset maintenance Summary Report',
    "description": 'Builds a read-only budget asset maintenance summary from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'acquire_to_dispose', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'verified',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'report-budget-asset-maintenance',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-budget-asset-maintenance',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '1d593e2c3b5bbaec',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/perform-asset-maintenance/budget-asset-maintenance'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/report-budget-asset-maintenance', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'breakdown_dimensions': 'Dimensions to break totals down by, e.g. department, category, responsible owner.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. report-budget-asset-maintenance-2026-05-24.xlsx.', 'period': 'Posted period to report on; defaults to the most recent posted period available.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives leadership a fast, repeatable view of where budget asset maintenance stands so decisions are made on facts rather than spreadsheet stitches.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build a summary report of budget asset maintenance for the most recent posted period available in the tenant (USMF demo data is mostly FY2017). Include totals, by-dimension breakdowns (by department / category / responsible owner where applicable), and a 'Top 10 by value' section. Output an Excel workbook 'report-budget-asset-maintenance-2026-05-24.xlsx' with Summary, Detail, and Top10 sheets. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-25', 'what_it_does': 'Reads budget asset maintenance records, computes summary statistics and groupings, and emits an Excel report.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only budget asset maintenance summary from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets.', 'example_request': 'Build a budget asset maintenance summary report for USMF for the latest posted period as an Excel workbook.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Posted period to report on; defaults to the most recent posted period available.', 'name': 'period'}, {'description': 'Dimensions to break totals down by, e.g. department, category, responsible owner.', 'name': 'breakdown_dimensions'}, {'description': 'Name of the Excel workbook to produce, e.g. report-budget-asset-maintenance-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a no-write summary report of budget asset maintenance from D365 ERP, with totals, by-dimension breakdowns, and a top-10-by-value list.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ReportBudgetAssetMaintenance(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportBudgetAssetMaintenance'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'breakdown_dimensions': {'description': 'Dimensions to break totals down by, e.g. department, category, responsible owner.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. report-budget-asset-maintenance-2026-05-24.xlsx.', 'type': 'string'}, 'period': {'description': 'Posted period to report on; defaults to the most recent posted period available.', 'type': 'string'}},
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
    print(ReportBudgetAssetMaintenance().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916eZObWLbnV9Hki5iqerJTrEJyR0cMQiAEAoRYhCh3uNj3RexQr777XKRM29Xtfv06Yv4a2Zliuffs53fOSfj9xWqbsKhePr0onpUvDlaaRqFXLazcXVBFX1QJ+CoSG/wsnCJvqshum6KqXz68uF7tVFHZREUOtu/aKHXrhbWoPMv9WOTpuLBbN/CahVXX4HdmRXnj5VbueIu6zTKrGhd+VWSL/ZhbWeTUC3SNL5j/rVDCwi+AAIsg6rx8kXqBlS68vIma8SFVWdSNB768KircD4Bd01Z5lAfg5oIeHC9dzFI/BO6jJlwoT2YfFnuvsaL0w4OIWpQLGFrY46Kz0hZIFHpeU78CrbzBysrUq18+/fq3Dy8ROH759PuLkwItgJYXryyqZvdQjJz1Er6pBTanVh6AVeUIbJqDcyAk0CUDl1zPX7yd/Vx7qf9h8Z//mfRWFdS/fPqcL94+n1/mf5c2XzSht2gK66GqY5WWHaXAAK8LMu2tsX7TejZ3DVySB6/Pnd8oAf3+Ot/7+cnkFcj78+eXAohgzQ77/PLLAhj580vVzsevM5Xy519e06L3qp9/+Uanbu3Yc5qZGJD69cvb+RtZsPDb0shffFHONPXGq/KcqPQA8e/0mz9P0d/IvZnky3Pxz0X5YfFjyrM+fwXyPoPOBnR/TBbYAOx8eY2LKP/5jUdVdE8P/fzLPyPrhJ6TpFHd/I/o/vokHIJIB9Z6M8kvHx7u+9ti+abbV5r/nG0JAubf0QQsf2f31VD/jPbDs39HOo1yr/7qyx+S+9GG5V8Xv/5T3f67DR8W/ueXvZeCTK4sO/U+LX5/hMivP7nfLv70tz8A6X9JRinaynlQ+JJZeeR7dfPly68/1Y/LP/3t15/aEkSxZ2Vf2ir9Ec0f2fXB508WfFv185/3Av5anuRFny++5tDi96L8X9UfrwvdSiP32/X60+L7TJw/y8WsxDvTpwm+y8YayPqdHX95+QMgTw60aZ3HbYAf//EfCyFyqqIu/GahOEXbLICDmyjzZuHVMKoX4P+MGpUH7FpHwLBv60D8zx6eJS78xW//x3nA+kfnDdZX1QPTvjzR+ssDrb98h9a/vS5UQLaooiDKARRfyPP5c24FAJJnlmXl1V7VAZiyx8b7CLL543ywiPLFb/+C8pcHkddy/O2BydET9S7UcUa8uk2911m3awiqwFMTB0C8N3hOC+inhQOE8SMA1XMRqIu0A4g526FOojRduBHAFFCpnkUD2OrTTOy3336zrTr8nD8hGl08S1i9Agu+irP4+BFo5adREDafc88Ji8VPv//x0+K/Fv/drgfxmccZKPrmCSAhp0jiAmRWm4FlwEnArQA2Hp74/Y832wIyOai5wG+RH3nPzSAyE899N7TCkh8RfL2wPWBgYNxsNuxc9KLmdXH0F1/lXTxtPleGEBTKheuVXu56uTMCqhZQ56sl86JZ1CD8ah/Uxrb2Hlx/syvrIWIGUtxqflsI1BnUoSIFv2YxH4vA5iKPgPm/hsHzOiBS/VQvdu8kXhfiHIuL0qqsMqysNx6+9fTLXOTftgPi1iL3+s/5XHC92VSPxHiaBywClnHeXPpx9jnoRUBVz936nfdjjTVXS/VRNavPef0W9FY1u8IBRQAwDdrInWPvL28hVYdFm7oP+wFJZ0pvXnDfvPKIwd0/62TemovFsy9YfG4RCMYW/1/0QrPe5OFwoQ+kSu8XtKhebk9/zH3g7Ldn6zjLMgv5yL1vrco7HL2j8uc8jUBwVeNfnisfXnxb80S6tgKqXMjLgz6wEPDHTPcR4XPEVtWcG9bn/B3+gfiLB9YBJwM4AOkyR+k7w/nuu6QhyPn5/Fsr8IiIyp0NAKJ4UbZ2CiLM9zzXtpwESDW77t2fINy9OWP7MHLCP2k1OwM4D9BfACEikHegRLx+heTn3XfR/7Tx2fHMWx7dYAuStHoQAHJ4s4Cza2anAfGaZ9sN9Pz0IALUyMpm1t0GaQI0fV70Ku/eRnXUzJD4tKtXAjT+OH8/NZ2vekMJMgMYC8R/2QLrPjJmjpoM9DNABgAaIIGyKAf1HRjlzQgPglY2pz+A17cG9EnxcflNIe+RZnNhet84KzLvmWv9M8ytfPweJdQfhQmgN6fJ02p/H2lfuc20Z6SsAdoBju93n03B67OuPxuHxTvdT/8w1/z8740+j0qt/TkAPi3CpinrT6vVs7q+F9dXgFOrp6z1W6H9+ISCjw8o+PgdFPyJ7FPjT4t/T7Q/kXhLjU8L+BV6heZbp7fQevsAS1Afd7eP2Hz3c37xvoEoYF9kILZmv40zNLxXvPcloOwFFYAjsPhZAeu5cPagVj8gHzjhc/59rM+5BipKHsyxWRffYcCj9IO4f/rsa2UCt/IG8HbnNjHw5tHskRm19/Ipb9P0wwuASu9fj2Rz8cnmeK7nOQ5kDgDLJvIeZzaQLnFBxn5xQbzm9bPX+v3vJtv913szvDz2gIPGSuvFvBdY58PCew1e51prVc1cvD4ANRovKGaoBb1JCfY+GjKwHFQUIFUzlrPsz+FtbvceSDU0/8hdehxY6esbZtffh/9b9Zqr93dZ+jQ3MLMDlP2wcIEo9VxtgblnO8wZbtUgZUC2/FCWR5n58iwzPzDHXJv+VImAVe6tV72bQVME5od0v/a7/0j0CpqNmY5bfJrr7oc3iAPfYEYB1nwfN4A2bwPgY1bPWzBb/zqPOrOnH1vmA7AHfH3d9PVvFbb38rcfyfXAwS9zND5j6u+lE2d8A/g/G/fvyiqQGfB1W8d70/5fJPlHBELWHyH8I4K9Dmk9/NBQz3r+j3Kcvy/3j47s2XYU+V+AXXyrTZtHjM5yZnP3ByJhLn9/ahMWVgfCaAbjH/AGzB9FBJTi2bDfPPbNbsVjXnyImVrN888bv7+AFLNAoFlvSfY2cIDlAHM/1nOrtQIwBBiC8ydggHv/7ijytr0OLdALg/2WC8O4j64dx9rgFg7hGwR28c0G2qw3zsZ3Nzhh2Y5l+wiGb7cwDGEI4kGea3kebEMoAug9UefL3E5Gs0j4lvCh7RbxMRiBXGBUBHNdQG7t4AQCWVvbwm18a9nftiZR7r7p+dRrNuLXqWi2x5u6AG/WGFjJYvWRfH6o1Ra2Vxhhjxy7NKDVZehFSYu4Ycgtp9/keb8tpiZjgu7aYB2ZXGnskI2cTbO3SjRNwaMwYbcJd3gfT5yvG65q0lp5SQkMQkYKEdLERXXYN+L7sHIxNPcwNtErRC7lOzqsIORm8obQR6OC3U+WLXARvyU4Y3dNl+fGX42Wp0OJZQ0HXi7sQT8YpR71kuq6yLLi5AN6WE4OJ9JZPqyPy/PgdKs2Dokjbt1JntE3KZMdy2sl7LSRx8WR3xxrpsqV0lHY0+6oq8TOuV50M7mjvVZNGCOkmsF3kXVntdQOpbEyYlc5SeYlydY3hesYD/dY8s6k3SBofeWclGvdqMvbeV/DVoOeYGzrrVaRcZowokMIFkUHP4KZ8hiiNq/d4XURqEXMOCVc0Dcdb+lQ8QrT52TTaBUsDAUoAD0uo+d4tIvWqn4qwgOzY7BdR3hnv2ZNifUO6s7kzgqz3p5oas1faD4KgB05rS0VgmzPdUlxfRlpLq2bpXc3CsKTYsIodEIliEFm16hADVl5vNvifkVtrvcLx3GmMhR13wbcudwb19v6NvLuRTH4pWqJqLUfk50SiA0pWwodroyDpiJ5buZonHnXrdQ7JXfKor2KaxftqvSnPMCu3Ik5UBGj7x1+PHEco1/5vbC+7Vaxiytm44WHK3Uy72xdkisdSyXlnuR6iY35uEa0VZWcXG6/VDKDNjP+Xt83Qbr37zBlmFRmC5S5vFDD6XodlZPAxhHrnwfhKIq7dXa3teZsRT5yh4/CSdZvdDxyEu8PhXOyuLCR6hHB8mSX3vgwVg9hlV5JpsroRDeMqr3rEatYJuNa1U6/OsgSvhflUe5MyjjvDMyKpYFLouXGY4UE69ty38eMH5zgdL+hlUHCVCEMrh0VQ4fpsrIO5ZJz9RzUY3OkO5YeBWI6Ehou3Ia7vztq6hE9q9s8L3vEt+Ej3OIINyFSrTjMutf6zYZebTViwuHyrqzkrSJx9XKFsusd0TsdJ1SUu+HHi9I3YkWmdOheUW7FXnTOaAtVHOWjvq6p5HjeLY/V1ppWfh/m/aFolQ3piv1oGVFjhk3EnWC+Cte27Ao5H/NNyKb3VLFOE69EvUtuR5BJakFeHVb2dpszGdMaSk8FDWNSWu0v1WhujkU/rX1hClKEoFHBW1LZIHahCN0abe0Yd4Aca4oLDFkWDXlqfKphjh19dPIpAe0UNzVif5ji9bbv91vjUoaHkluNNyrYtragoxbcOmaFN34YtSJi+nvuWFeZSCMQVab9rpEGdnexNHlXyefAKC5nL7sFyQnT9bqMDrRFdtDxUMrlUYfKk5eU0Wl/G9WM2hCdw4sZwg2w5ZCObI7U0Z8i+Ew7VqefDqmhGhm8n1bGUdPQ4jgm9jBlNDKqB7VGY+HGwEdW6Jqjh3eGW+5ONxa6HpWT7Cw3ttBK6sWK1PEcXU3MX5ZoaO/G0vdPu8uebfdXXPMxetVX47HrxWFpHWn2nLGr8OSat7CTsXovR6eK2QdK3+cyD2P3Vt7deXGSDZO/acjhVFed0uyI0xTkeZw4N9oq9uRm5TKc4hEuYm4SkapujlOFqy7OjyJ84t3cZK6JeCaP+9jJJT+hpTt8FaWN5Ehr11t5yhZTlyB+ROJAC3ZPRB1N2qMa3Ag08SX67MDQWWAT+OpOIlT0h5UTBLV/daI71Oq3XZObyxMe9/wp4hgvxIwdEZNSYiS9tleVpKK5bVRmBVpNywru6Diyt5tAlkzhMsJ7mzgYiqoHheIyQolLIczmElodkSaJE2887NlTe+apu32GqOSuoyil9HgEi6UekIqyHJaVEiipd0DcEPXJUcYgba/3mHXX4Wh7rShe1HetqbEtzg8pGXknnYIlRdjkKIEtvRXrDnLNak2QY5J6uu94UejGRKgMs9ju4iBnbmHktt15qe4a1RXbMYiVS22f2XiFJgkLWWem2BgRvDvAd6Lm+OXBNAn8fpVPZLnbNa06YJKZZiC2Ha6oUyjVSk9HJLFj0fByv7fQRDLObbPaQ9hlmZfYMt8PKzWiYf127yWLdMQ6TjZiy4b7+zLvpbrEbI3bhbIRJNyu0CT+ON00la5h12ICNAyPG88m251AK7WqTjaxz8MJwvdplQl97TBMLB2aA9e1IyrZiYWhga42S7Y0wWRt7CEOwsj4aB0b0VDMSmmy9YG2lVRMJEnKjse7MmDNMLWxQjlnatvVlMqCFGvCHRZUgrIbLxuh3/iMP9WXCxQkg+if1zoE4fddRCIAQ1SL1PGbbl9vho5sXZ1X1qSZ3pRrpfi2fjsoPHthi8iILOZ0dy6TQGArZ6PzoXK/jLdizQyOwcgkf1XSg3JQ01hQjz7beSFyBcWL341WFbI9GZ5l2AnbszFKO8baMofUNJuTDRW7jCk4LefVkx0RPE+PumTsSugYYVG/K4MhVZSm47fGvdU2MmhIA63mbrdJqS5o6u+oMNLTWK4pUwSWU89psGMxGBbyQ3Q0qit6rFqDAf2oHR6tu+mkXCmd9ZoOOEiCA4HcXw7OBi7NhluGjRklAYJKOqYWSw8ypV3IQqFUDRfHNHgCBmU1YCZjkJl7eM/MnTJkE1UdleyqDDTN77PL+rYVZG0we/pS06fTsawtovZlf+8z5U4oqGUTrtaKGQXnllcveex4TASvlVvEQENIqWg21rq99g1unIKe7LvpZG432nQjd4d9TjVbYj1N65FEkGDpKbLJ945hM4hn5GHeTuaWHG/4oA1rCIZ2G9bgq0CzGv06nm5ckAS51somtWZcKo8xThGS2oaL9qjL6hU0aQFvrcNesbs9Hpzu1fVwuzEJRB2ue5fotRqT90a0tGW1v+pbl04suonM2pkQv99IMlBWKIr9jiYghPbqFIfUeLBbtC/IQ5Pg0mF7xggIloJDoedSaHZqbtPr1Ca1IKRoOLgquZ7uL6tS8GU2Bk0R0vHBZDgicl6tUKoF09w+zIg9geWcTGNLSOw6AQWTJ2efKfJuGJSlDaW4SfjmQoh1I3oXZS36eSySy3SNK0dFA21OZSgQRVWMmVBJHPNFdIKwq5hk9MVO+uDqUHSFcLeDcWRO/KZBPAZf3Zq1rfa8AZW0BR1iTJtjG9FjCKGuSeaomHKKdYU+VpfwnF8PAtNfp1Mqnop4uYX7PFyn3R0GFjxjgb1u5JTaF7ADldqKDlhs7Fe37MjfHJneRwklrHRY1PitqWWcv1MMyrB5wSeON7FKHQJ4wzm12MY/NeuNKHFpK3sJGxy9rOtd7EJt4ktc6qISkHXO6orc5GpLLW1VCjsi8KEK5mBCSaU1BDVNdgIC7NVcM6HNUU7OiWH1MrZE1twpkfWTuyap04Y6ZgriJ1pnwl1ClCJ73QglbHA1jGquGqPkMfL1iVwf+ES49SGeeypZHfQjq+d9qO2Z3F6eI7tHcl3AliXtXfpULQlMFsNjOlRyMeSMSifMEF1Ar6FUCicB4FM9V1u2tDQcbrlKevVpcFYX8mb4kOq7DGNcT6ElDOkeQTR5Pe5OkKpJ0w7qEmGfstDKIgv6woNCmoleK/EH262JcQdlTZzIcAeVJoaeeqREkmrJuuYRau0ovlvaDTJLGaZvXNzWxyst04HPpnG/PbOrHm3Ot3W0Pd7T0OJ6cYtca+l65xkhGhhqRa5vCSfgpnAyztdoDIOGOy571UDOKh10TC0K+mEEQwit3pjJ5Anbv4XlhiOFc6yqWW2nzYClw0VNmt05TdvW1aVby1Np0lTiPe8cPMOPh4Z3E3kojxW7P+4U/aRbpXkiZB7Y2yp4grmqhgjqM8xTMHvsxzBZZbvVkuvwIGnBRCNQFJ3EQr3FuSGwrKYTYFy5sN3N8jXBualHp7yBSDOvAMwmmk+Z2g9UEBP1matS+VgJqLLpYQSDvPKecSsNbYJ2aSWXPU7iYVK58dTv9AC3hWMG19RGO2R7XaH2Nbq5X7tYHhjZvkOcLrnD6YAa3F69Li1c6MOWDA6Upi4ZvBdo3tpTrXevJgXa+PtlbJjrhtTQXMs9P7bXiqzahWefOW3XWySE5E1Le7a01/Pi6GMmN0xSyckcQR8ENPNNkYBDnlHsugpi3G9yisIaS9JuBmWiypnYF2gaO2Y9bSmU0I0j2iB41zcxO7iulIXDHjWmJm3I/ZHKVSP14jRO3CNF4eXZzV2R4GxfkTcJRAfTPl7GjQotQX/v36dbuCFyzTAiGY0GSNKp6ZqOd+estglIm0DEPegg5cool3jtoKiEH2yxHtgDo9kCipAyJBoRB6kOKZkdfE3ukYAPNbhKbUwkpc8aqlINxYqU2RNjXh6WaDtpolvB/HWael/YqHuvSejcvZzIHEE4lBS58rJKN2mT2/g1hESzcGOPHrrC2ssoImXwzRg4ZA8Xck64nottpuzqNelyed1IhAgnTWYibGzkjgtzLtRAPBIXq2IrXrriyniDXoFBJwh5N9MvWSlNwdYoK0zEqliPvCivI6Km3GLJVDAqb/O9ejeYlayp1VHH0YNfFCs8tzSKvN6HxB2SAblM66JQdiaM5mSXTX7vqKtKLDeWs4zizXWrdDBoiI5bQwSE+KWyz2WzleCBzxuZ9cXQ5VGj6hzEbIiW5mNqI7I3GztYpFkjUgGxzd3YbonVlvFX9PV+wzObxZfX1VD1bCi2xO3SGbqrR7VLnnneL51RQfVqPJ/jRDPxnEEUfSUs5QvIgUTxTDQDLeqgLhMwyQfydmI2O46Lg2B/PqzaZEJ7yE7gU5rZmU2vGC4VULv33HCN3hrJlOIGMXB72rECmDPqcXNTpxHM5CpW36BqqneegZ92BT9eHXuFowb4lC1d+NkSZEhw910xzMaILY9QHupHysX4iMh9YICTYajTCoDLeo1ZYqyW69MVsonEOkPJfaka8G1lhuEqc/dishMykhGyfbjdrrE1UU/n6JCRgY/AVUXrJj+prcIYTVZd2woHrDUBwsqeO9nb/S0OcxMttibuu7chEvbnSQItCO6sGNw5xVBoV2Ssh0fUI0du6e3J7cmFwFxihLKyy2NGOBE5PMhw2uBme2sxRWB1mqGx8rK9aRKZHJpjwsYyHHNoz01aHEGsjQS2kIMta3vMuoZXvNVdW58NFIPO7naDXae4v3CnyxLFD3gXVGJUYe4NNTcb/LBbhpiLw7ByW63NfSvH1qSumiXddVdNYT1m7LOT5IUt1g765FwYW9KcMzPRYXfONpZpwLilrIyTwt/0qRka1uPxrsukLD7h/A22t7GgkwDIQf6Ty1E/VL3tYqque/utsM2lgdfRpuraSXC7Gi7jFhEgQXLhsoCREorhULB3Wtml+TVEgC8aXj0K4g1fH25Ye8VMr1v2g9O7JOiMZdMzzdvG68kzx65GD3hJskY22LSCeNkmBiwVXcrBNZpd9PZGbnrCRdMTMmxsuCI2LVLnjbXJWB3Kq8bjpwq5mUSnLuGRaA5iWSgg9xoUPadFwJWGTxGkCE9i7fWq2viWd192HpaBSRe1l0uFQsoUksw1fzhtT3HfrIn8lh60ar3zR0k4Xtc0KGW254WOJq3hdYXQlgiy9Z6jZAIGODAR0xsL3tIEswnOeMq2Uz3lOzQzAjsIcJUf82ivU8vOjaT60Fux0CC21l23h421NBg42GXQ6Z6w/UkuWQS/iVuawtqzJjHCGSfLZnfBxy1/kCohUUHXd8AhUYeurjJaaMmwLBmu0to4ELe6ixIUzDjWVs8jgtx0VHE6bq/59TbtVo3u9em6grYuKQWtleA06tByWyQye0Oxo7+uJujWDktpokKiAxUmRlar5MAh3PaOHKslLmcesAEs4ea29Hr9iNjuITw1MU2dmWzbZraVOQ6aViXIUocwJGPiq5Szd9fO6yeO2XrXIas0RkyG7LwczMO+JeBMtfP7xd20uCFs5TV81yaH4TwiQQTtEiAmSw+rA5F20opu9pGy7a78UJ62Asnqd08LeDQXODbS4fieNKEYX1UFdql6xUmQKGHQuInUATG9xs7l88qOUTeYTvlWch1Y9HxM97ZnSfU6tSYPq6Ul5MK2IoVI2MhW5F88/Lg7H3YJtI+IFu1WynKSXMul/NE9MMPQyO21d31vaFoi1XB8apcsdyLwbFnfE4FNV/qI6uclhrWWTGTEnb2B0oGfNaSUnBIJC82+FFaR6L1UWZ24pL2JUl3UqNVsN9puGzhNhUIpnq8pFD8mYkyKDHWbxKqSBrMkkHT0z86h2Wdn+SwfD62nLcmSCTpNiCxu7bGDQ7KnAvZO+LnJEtTeQCUUxbkzaktpWfWiiZlTVbZw3xUhzktm0YZEymzYe+zVzrG7r6MzDW/XONFWCtHeazTRNzKxba64gkrGCXTz6EmqanQI++VkHgjsyDq+sAwOSR4Td9gwLF0zGE1co0zsVKsC27erUMkUeyD28bbCp0q0mhsPBspbttxeidhqJ8Vw2LPIb64rtT7ZeEajtN95IKlVIc/Ga2d48Vq1HdeOdaLdLtfO0WBHv++tWyzLe60yeqvss4yMOOxe1MEZSOGyZU+s+TYyvKbhSHVAmW7MnNja16FtKVGwqllcFjlzL6y3+JFId34DeQ2YV28Xu/FWa3hZc329HfY+Gu87F0vXVoideVorWIuYvE4epdCZiKM4bXiAE9EhZWVGkPaeT7gOusXa5WoXYyLo3bGoEX1FE33S3+rOsLuVPuNHx7Vk5Npt2WPROr16h8xx9yvMh2HPtDqOIknyry8fXr49xnv5n75/Nj/M+X/2TOn5+Of9PZPH40nPcj89eH36H0v0tw8vlRMBeZ5Pzeq0Dd4eMv3dM7OP/+KB47x5fL7Q9f6I+fn4vLGC+SXnlyh327qpxi91kT7eMQE77LaeX4ys53dnHfD9/dPVJz9wYDmPB4VfmuKLG9VlUc+8Zr5V5rmR1byfBm+PED+8uG+vN31B1/gXrypnLd/eUgDKoa/QK/ryx/8FgrI/V5MuAAA= -->
