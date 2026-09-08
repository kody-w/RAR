---
name: "rar-cowork-cookbook-ppt-exec-correct-ledger-vouchers"
description: "Builds a read-only executive PowerPoint deck on correct ledger vouchers from Dynamics 365 F&SCM data for a legal entity, with KPI, trend, issues, actions and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_correct_ledger_vouchers", "rar_sha256": "b9ae050cee2d576a7afa1423de2a8c00e1d55430e5f4e9e200c5d7a3e9306a2f", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_correct_ledger_vouchers`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_correct_ledger_vouchers_agent.py` and in the RCI capsule.

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

Correct ledger vouchers Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on correct ledger vouchers from Dynamics 365 F&SCM data for a legal entity, with KPI, trend, issues, actions and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-correct-ledger-vouchers
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
    "briefing_length": {
      "description": "Length of the review the deck must fit, e.g. 15 minutes.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to report on, e.g. USMF.",
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
      "description": "Target .pptx filename, e.g. ppt-exec-correct-ledger-vouchers-2026-05-24.pptx.",
      "type": "string"
    },
    "review_period": {
      "description": "Reporting period and prior period used for the trend comparison (e.g. monthly review as of a given date).",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_correct_ledger_vouchers_agent.py` and embedded as the fenced Python below (sha256 b9ae050cee2d576a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_correct_ledger_vouchers_agent.py` first:

```bash
python3 ppt_exec_correct_ledger_vouchers_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_correct_ledger_vouchers_agent.py   # or on stdin
python3 ppt_exec_correct_ledger_vouchers_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Correct ledger vouchers Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on correct ledger vouchers from Dynamics 365 F&SCM data for a legal entity, with KPI, trend, issues, actions and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-correct-ledger-vouchers
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_correct_ledger_vouchers',
    "version": '3.0.3',
    "display_name": 'Correct ledger vouchers Executive PowerPoint Deck',
    "description": 'Builds a read-only executive PowerPoint deck on correct ledger vouchers from Dynamics 365 F&SCM data for a legal entity, with KPI, trend, issues, actions and appendix slides plus speaker notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-correct-ledger-vouchers',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-correct-ledger-vouchers',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'e8b2c51eb4938f30',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/record-financial-transactions/correct-ledger-vouchers'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/ppt-exec-correct-ledger-vouchers', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'briefing_length': 'Length of the review the deck must fit, e.g. 15 minutes.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report on, e.g. USMF.', 'output_filename': 'Target .pptx filename, e.g. ppt-exec-correct-ledger-vouchers-2026-05-24.pptx.', 'review_period': 'Reporting period and prior period used for the trend comparison (e.g. monthly review as of a given date).'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Cuts deck prep time from hours to minutes for correct ledger vouchers reviews while ensuring the numbers in the slides match D365 to the cent.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build an executive PowerPoint deck on correct ledger vouchers for a 15-minute monthly review. Produce 'ppt-exec-correct-ledger-vouchers-2026-05-24.pptx' with: (1) title slide, (2) headline KPIs, (3) trend chart vs prior period, (4) top issues / red flags, (5) recommended actions, (6) appendix - data sources and methodology. Include speaker-notes on each slide with talking points. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-25', 'what_it_does': 'Reads correct ledger vouchers data and produces a 6-8 slide PowerPoint suitable for an executive review.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only executive PowerPoint deck on correct ledger vouchers from Dynamics 365 F&SCM data for a legal entity, with KPI, trend, issues, actions and appendix slides plus speaker notes.', 'example_request': "Build the executive PowerPoint deck on correct ledger vouchers for USMF for this month's 15-minute review.", 'inputs': [{'description': 'D365 legal entity to report on, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Target .pptx filename, e.g. ppt-exec-correct-ledger-vouchers-2026-05-24.pptx.', 'name': 'output_filename'}, {'description': 'Reporting period and prior period used for the trend comparison (e.g. monthly review as of a given date).', 'name': 'review_period'}, {'description': 'Length of the review the deck must fit, e.g. 15 minutes.', 'name': 'briefing_length'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a monthly executive review deck on correct ledger vouchers status from D365 ERP data, without modifying any records.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class PptExecCorrectLedgerVouchers(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecCorrectLedgerVouchers'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'briefing_length': {'description': 'Length of the review the deck must fit, e.g. 15 minutes.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report on, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Target .pptx filename, e.g. ppt-exec-correct-ledger-vouchers-2026-05-24.pptx.', 'type': 'string'}, 'review_period': {'description': 'Reporting period and prior period used for the trend comparison (e.g. monthly review as of a given date).', 'type': 'string'}},
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
    print(PptExecCorrectLedgerVouchers().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/9V6adObWLLmX9G8N2Kq6sq2EIsA3+iIQYDYJMQqIcodLnaQ2HdUt/77HCS9rqpu9+3uiPkycthCcE7u+WSmD7++OV0bF/Xb5zc9cPIF56RpEgf1wsn9BV0MRX0DX8XNBX8XXpG3deJ2bVE3bx/e/KDx6qRskyIH27ddkvrNwlnUgeN/LPJ0WgRj4HVt0gcLpRiCWimSvF34gXdbFDkgVteB1y7SwI8Av77oPMC3WYR1kS2YKXeyxGsWyAZb7P63Th8WvtM6i7AAkoEtkZMugrxN2unDYkjaeCEpwodFWwe5/2GRNE0XNB8WjjeL1jxUccoSPEvGRZMmQO5FmXbNoikD5wZ450UbNJ+ARsHoZGUaNG+ff/7rh7cEXL99/vXNS50G3HpTypYFGtFPwfcPuU8vscHm1MkjsKqcgD1z8LsMaiBuBm75Qbh4/fqxCdLww+I///M2OHXU/PT5S754fb68zX+0Ll+0cbBoC6dpA3/hOaXjJinQ9NOCSgdnaoCB266e9Vo0wB159Om583dKRbn4y/zsxyeTT1HQ/vjlrQAiOLNFvrz9tAB2/PJWd/P1p5lK+eNPn9LZST/+9DudpnOvs4sAMSD1p6+v3y+yYOHvS5Nw8VVXWPrFCxgoKQNA/A/6zZ+n6C9yL5N8fS7+sSg/LL5PedbnL0DeZ8C5gO73yQIbgJ1vn64g0H588aiLPsid3At+/OkfkQUO9G5p0rT/Et2fn4RjEOXAWi+T/PTh4b6/LpYv3b7R/MdsSxAw/44mYPk7u2+G+ke0H579G9JpkoPAf/fld8l9b8PyL4uf/6Fu/9OGD4vwyxsTpCD/a8dNg8+LXx8h8vMP/u83f/jrb4D0PyWjF13tPSh8zZw8CYOm/fr15x+ax+0f/vrzD10Jojhwsq9dnX6P5vfs+uDzJwu+Vv34572Av5nf8mLIF99yaPFrUf6v+rdPi5MDAOX3+83nxR8zcf4sF7MS70yfJvhDNjZA1j/Y8ae33wDy5ECb7glfAD/+4z8Wh8Sri6YI24XuFV27AA5ukyyYhTfipAGY90CNOgB2bRJg2Nc6EP+zh2eJi3Dxy//xHpD+0XtB+qos268zTH99wfHXJxx/fYfjXz4tDEC3qJMoyQHoapSifMmdCIDvzLOsgyaoe4BT7tQGH0E6f5wvFkm++OWfkf76oPKpnH55IHTyxD2NFmbMa7o0+DRrd46D/KWLB+rTs6QEi7TwgDRhks5AD4QoUlBl2tkSzS1J04WfzCyLenrQBtb6PBP75ZdfXKeJv+RPkEYWzwLWrMCCb+IsPn4EaoVpEsXtlzzw4mLxw6+//bD478X/tOtBfOahgGLx8gWQUNSP8gLkVpeBZcBNwLEAOB6++PW3l3EBmXyugEGdhEnw3Axi8xb475bWeeojjG0WbgAsDKyblUXdAuRfJO2nhRAuvskLmM6P5toQF81cbOeyF+TeBKg6QJ1vlgQ1b9GAAGxCUEK7Jnhw/cWtnYeIGUhyp/1lcaAVUImKFPwzi/lYBDYXeQLM/y0OnvcBkfqHZrF9J/FpIc/RuCid2inj2nnxCJ2nX+ZK/toOiDuLPBi+5HPJDWZTPVLjaR6wCFjGe7n04+xz0DxkAAf85p33Y40z10vjUTfrL3nzCnunnl3hgTIAmEZd4s/F4L9eIdXERZf6D/sBSWdKLy/4L688YpD+B60K+73+hpn7my8dDK3Rxf/3PdGsPcVxGstRBsssWNnQLk+vzL3g7L1n+wiYPuR4ZODvLcs7LL2j85c8TUCI1dN/PVc+fPla80S8rgam1yjtQR8EEpBkpvuI8zlu63rOEOdL/l4GgEqLB+YB8wFQAEkzx+o7w/npu6QxyPz59+8twSMuan82BojlRdm5KYizMAh81wEOaePZbe++BEEfzHk7xIkX/0mr2eogtgD92YcJyD5QKj59g+bn03fR/7Tx2fnMWx5dYQdStX4QAHIEs4Czm2ZfAvHaZ+sN9Pz8IALUyMp21t0FyQI0fd4M6qDqkiZpZ28/7RqUAJQ/zt9PTee7wViCQAPGAllQdsC6j7yZISUDfQ2QAcQkSKMsyUGdB0Z5GeFB0MlmEAAg+2pEnxQft18KBY9kmwvU+8ZZkXnPXPOf4ezk0x+xwvhemAB62bziwfdvI+0bt5n2jJcNwDzA8f3pszn49KzvzwZi8U7389/NNj/+e+PPo2Kbfw6Az4u4bcvm82r1rLLvRfYTQKvVU9ZmLrgfZwz4+Mr1j89c//ie63+i+1T58+Lfk+1PJF658Xmx/gR9guZH+1dsvT7AFPTH7eUjOj/9kmvB71gK2BcZCK7ZcROo8N8K3/sSUP2iGgAPWPwshM1cPwdQsh/ID7zwJf9jsM/JBgpLHs3B2RR/AIFHBwAC/+m0bwUKPMpbwNuf+8UomGe0R2o0wdvnvEvTD28AE4N/PpvNNSibA7qZBzqQOqD7apPg8csFeRmCyAf9SR618Xzrz5Pt/nF/zv1Xi5UEw+PyAdtZB+psmAAgCj5FnxZrbAGSpnsNlO1UztI957S5s3uA0dj+PZPj48JJP4ECAoAvbf4Y4a8yNZfpPyTi06DAkB5Q58NcDAC+gOAHBp01nZPYaUBWgIT4riyPkvH1WTL+XiBmLjN/rCqPHuDRXgCYe2lr6ofdd2l/a2//nvAZdBYzLb/4PBfZDy8kA99gJPmw+DZdAI1e895jNM87MEr/PE82sz8fW+YLsAd8fdv07b8l3ODtr9+T6wF3X+eYe0bO30pngGYtaBefQJ6Oi/dlL23/We5+hCF48xHCPsLoY/93LfOMn3n4TQr/7/lrwXtv91zxyIwSXNXvN0AU+N9A7lHe53YIRHjSgPLz40PSDIRZnE7vwTpXphCUvgikUf4IlJ++I9tDOFA8QAmeLf27C383ZPGYF2c1gOHb539v/PoGMsuZW5FXbr0GDrAcYO3HZm60VgB9AEPw+4kT4Nm/PYq89jexA1phQMAlnQDCIC8IYB/DNw7uhM4ahRE/gB3Cg6Bg7WMYikABFqIBGcAQ5GE+7iABiUAbBw4BvSfafJ27yWSWaRYImOIjsGrw+2Nwy38p8xR+ttS3yWdW+qUTwJINClbyaCNQzw+9ItduAK9crXZXFkYm+4QcxGAtnbaYDDm9ZzH6mOsSapwb1NGC3QmmCi/Rx/KWnFWy0BhKwYXwYuBJgPWInMUJqaWl3Pm475Z7usmM9I5dxyV2311HhOVEOAumDaU26t06xKHlaGljSzgLm56dsido752wIFHuxF2T6JytoqkfW3xFnNyhKu6xCcAbIw9ymTUq4Nuc470aGaY2XET/lGf4bqPjY7vmolE+9DmaW6uV1WESJKw8waruBs/UO2+Jc6qusacOzdDkUsnL/eouj7KGMYIoTqJelVol9FOUyAK7p88xsT8cLuSOLwKhSNny5jkZO1XaKnZhoxUZiVfHIOwVefRvyJ5chvmluuMkFq6OukSOjaiVBzoYstWesctrAtsJLBiSxqOZuzxc+uLYj+eLxV0kS7m6qja03n0VKr5nnNZsg2vaQRKOyZ0zi32KBQf+ttIbirtdIOmED6XKXBUBZ0oGt5dsBd+knPI8FcFQVk2M4lDXNK47VzBJWWMX7s8xgh+I3nbEfFB1qeAgddyzlLy0pnskjWwteceU2RFnTj5cNoYsskmupu7V1hou8+ON7uNoBG90tCKOhyzyrgG0zKHseMZadcA1LLttDTEwTN2OmX2OnbdbNutuvLyPBnopKbvqXO4FDBqYFbyZInVakUIjaKTtTSm+NG+XQjJr7lwSUzaRsBn2grYxe+xwkUfVjMvzWU1jpViSJ1MTz91ImkqyRezLxA+uqHFLpr9CxuEeqp285AX5vqFjLVqWrjeqYpxfaIZNA025GyFPiIyrtMsmPfaHKjavNLTWXbNVaxVuBRapxfpEno4aUx1vSZPKSQo3m0O1D2VK7W26Px6VIZX8BFMgsYF7gj6S505cHawiX5kaQa3Q5Lj1DZxF4wbmtyV+c6LlRXEviDI6l+JwPYd3VQw4MV675bazsVKTvW663Oqjcj0dFR/8dU9HRNfr672xcsK2b6g4RniK4gw28TB/O8PyHrsuBfRsbDZVWO7GyLMOyTrmFcym+suxRej0FodHnPdozbqZJ6fIbCRZBu2ayZmtzU8sJeouHlAyd3AyUVlvIXwvlqgk55u7uNtZjsebGybNsHVsHkSK52jhHJcH5iwY1GhBR57ptjDK5+fJWCv9lkaoe8UWE43VweoQ2weml9zDPRrADGdveIoqD0ZNnLs2deITM/VbgbMxLa6CE3pKU4aCtgLkJISm0yFXrZjpeBpD/NiMLeFdk4Jmb62FKyJ+xyiYl0t6c7mGdiHDq/OuX9uX0MgOt5pm5QAiUu9yCA9HkaOxfXxOopQKCXpFG30rq5O4PHhddm9vdK/v156d5Ud0pCKThTn2fL+s6g3naH1SaJy7xXfYoVlyNCEbkZLXsrzSKq2spRJbSRYkeWtU0w0Uu9K+oxkShA53qTvpgSHhpSv00hYED8Fi7Lavg6VdNYHrQidNK3aIclgrhImtLcprTJ4lYOIgiMhOW0WnnL4rh36L8Bsh0kALiPX0Rp1GkLpjxMUsgt85qhuG3JOCKOlUspIv0HrSE3vfxkbso1rJ21uCI8hibNXUPAp8jyyDNJe1a1CjFuTTA4rdmZWVrTPcbErYzzLPgwgNJdxkMxH9zrQkrEQMTsXTNREelvxYbAMigg6X67Y3OuGgnnP7zNx7Dgy4UoDVVMIFJ7arOLK2sUPJRMdqd61Z2LmI61ychNOdEF1a5JxOybnGICHWOw7RVdd3DHfsplyw+xN8D3vLRqRMHYVlkwTtbuKmTh1vMF6pXSbFJXasUzFV+N7NEup6C29x5nCUFqE3ohVvbLwtXcUmmbQ9Dum14i8Mw1ZhWG51nc5J6wg8S231xpGY+mIqlrMcg32a8/Q1QeQrhRzh3B64wS6JxraN490ll17OIwh+GxkTc5Ocos37RpZkql5dsOoG3yFJMWwBYpZ3goTDncd0dcbyrj7EESaGe5tg7yO+x7RwtQr1en2S6xPsaObA3uvVeGkoczslW5fI04EgKyXVNep6cmqJvl4voEPBN3LPMKcT2WVbiRgxoruKKSnz942t5C13cE9pVPf7YkvBU8LgdSL57iiidOMELMwUnskZAxGrEn8SbhAw0t6XSlo978erLsk4fLe7y/5Ct6q82l8dm8cTQ4w9yxVumrchG0ZStg0cR2uC811m1DeGsjN2NVHfD/jqAslUYBD+uN2ppiY5XXFNsoiEjhQc1YiKYngRxeV+fyNIW9zq0GY5XoUz1XN6H05+FSkTJnH0dRKEXoPQisb6NWH7ozwyaCZ0AFmVm32l9CIrqIvnGwjq7HgdCgo0gIOrKJvGdCAkmynd9Sm47gxM12G9Q/OzWcGCM1DRmu5Hvcil+JidaPoCxe00bM9mfGYJoRQDb3Pp9uEdjHCI1A3QXjpOtEzpLFcM3S7G9lYCHEAeohscxxsW9D6CfeIOseL75sXWpOwC7+1K9IcdxVT0VYJGg/XJBiqvGo1u9ow6pNtrKPVLkBp6TkbXvSB67H0D4inzpSWlTHWlmfJNbWCx0Cyik6ANvGZNUj4NXnbFTue7TuUacqYGSmaxmjTT3EF3XJrtk719qwPhFIZnvY9TAd76yeg30J5TMOtUEUbBUzaSHS+FVzqmZdLLy0kVTpNoDEqpR1Iksl1K3+pMiFoqvtrrfRLoq5W2E/2s2FURv+oYP2EzWCDQlLkE3P1eYc2JXTOmXlVSX5PiAGLHbi4UqRiINSLuTod5WlPjqU3U5bknLeEMQzxUXbeiTvhLPxex4Jh3aJPfFDHNd4ZUG7C6V30v6mg7Q3Roa/AHNmPx20QLvDkWLGH5jn1La6fZjVxGnZKrFlFtc4GOcp4iw25UacOFPJSWY50wpo5Lc2ZXHZh1HysyZt2RZIvqy2MR33N7tR0wBjSbQxITrNEbFw2dzrl2VBo0HQvowGjTOWWyfkne4y1AHsGQHeJoI0V6AhkK8iWm9aEuU8lYFyuTkytmJPVNWY+XwYIMsieUEk5Vt8lVw6CDjTXeyGLH9dDq5qiYs08OhcULJ/NUKsSNz7SSG5CsFkqfXeVXhV7d7s5UmFerTKFNEqr1VrUpUkKlTqR9PV17yvYebnpmiiVYy01e6uJb7SmndjWJNdtd0dy8uavoetqs3ZHmh2umKV3WWgpoLdt0p2/aSotNV9yKPJZXbaIgtnbY+qflmfO2VuokhsCqDlbpy1uRhEM/UGx+Opa0sqVKbKephjachtS3ksY4nBF26x6FC+552dqZpMoC6bnZRL24t1cB78Ok7yT06F8xjSJY0EPlssrqm4SA/HhLTJvLuMPPlUlYq+3mBHuCyBTKpih1vUq4HTHIR8ddXm+ADXXO5R1JCdwu1Xd3SbhrTeGAPqdxhMBP6bFsUft+YnCvODWcKi+h+OJyRyuq7bXjS9O+C9a9q0rB1eGrGDSY3VHXrJ0uRM7Ylaxi14Ux7VjaKQ6VsEuu/hY+Mbk6ysLBtKsbunXoM8OWUCsZ3j7NysS62Ii9jXIyvJjHqBLoLQUC2aGavZH0Td6VhNweDLo/c+ccdKEMzkPKKLNXgsmK6EKteWgl0T0othvZDzdOgPutP/FhJl6XFHu/EWNpIWK7WXFThTvytZpw0BoI0+3g1aSDgRJwW3r33UYRLtiu5sbscrsoWra/hgbD0faBN2gzd475ZdngEi9qrlSdbyAnd1ii2pUtxqUu75PyfDgXwpWB3MOotS1pmPQZYhhVDq9dc4RTHUFzw1KrIDjeqtxz66ALRJlttFTi1ojr1b6sCd6aQA5dyqH8mhgFcYvefDooSx01E105XfuuIWXOOsiT7K05koHRRtyZp+VNOHkRj68PGObwZRCv926/UfPcjvgqM4sOZc+gotom26aTZK0225XnhvEWQ7BlIsURRQ1Yalr+hS56rzOXbkUSzHHHCPaaqlpWb+LTSCZ0kLE7vRpre4/czIMsWiqJjre6XE7rIzrY47lwu7aXML9MRditeJIRD7BvUem4rCLUlTatMkyjLUphYIGKdXDi4lwTVQFtvdCWS7m9U7DrUmdVU5v9/WYKKswRlV+eqrpsYHZtKNG05k7w2jCDVd5CVzWLVmforKOrwaj3Os9sLGgHZlT0lsZsvrZ0/Urb+4RLlwcmHjuKUJJUwtDjsF+2skFh0bHdCscapXC7R3r6woedmPhktlpdveLGXZbwoSyWrYUdCDiFN8fg5quqqZqeQ95vJ9lzi3jgb5i/4VzjvDGXk0rv2O1yiM9r5dxbEUqAgQA7cUowNWx5LA2o2Ovr4Ha/CE1uVtVdhSoukff7a2UkbJqRAdY1rLxt5JWKjBYWinlf4vcUsrHuihcWdXDXu+VkOUevCDasm5w9e7D8wc7x7kzaB4Nw+su9Ugq55K/JMVqeN6nBlVnEZGNam7ux8n3QNJwwnbQuJXfagGIHWtaR9AdPihXP76tLe63vl3ooGcTrHK2xql3QgrEHsc/tmciPQ2Nf/BGx4lDL1P25i6pydGJXdc+IdM7NbHk/FB52worzil5W9b6f2gg+Ojs8d4aWNHcbGTv2yGkLN7JcQi6ZXrjSRkEzS275lbky99R+exARY+tVt76yt7Bx0E4WQdl3xac0RDTtkXSzIL4SZ1LvO4TZqKTL63vCIjv1CE0BSDd96SyPgYpjZq1Zjt/W+6mOnJAFrd3FPXP2WEawJEB8GStki6+W25BUdc+0QfAtSSsca5T3xHa6rPr9ifFGSdZo78R7qb82tOs43HdYdh2w2zX0GYvuB7G07pHP1zqyRbdXVi4FCPHGUNV0ARV345jjImi3SQ5t9dHZ2NZd0ayaXPsbX2awJj7r1YHeqf0ZY46ejF0Tgs3kTczy0tImbjs32GDkJA5ogx9KqtEKZN1DGIJgp+sO2bFWe9+erKtt2YeYwo+8KMAxL7krNR26ZaX1x47bMMGtwdL1CLmqtYf0tEAQEQpRYatIyPpCLOOqqYste6PWwo3BsCWGTnjTKncOFpKBG+va9C/rfRqd3V1+qgv4nOINvbaUZioGknJkdJnYeKgUVrgRXG2YiO2RDEA/Mm5XO8wrNDS+5JfkJJolmzVa5J157EhusDgzG3Uj5gwpCfiJHHUz6wutL7fUTuaT4+7gZdohsuRQFVsUYaLBaETQ2ak3Jl7n/D3GQUqdPAgvS5pfo80qLSAfTJBJV91J9QYaG91JQDM9BYZFTbiiqhVSHeIRtNchPWzEQiJIEpK2rd7BWZ5Zq7Kn7gVeIGHXFXUGsGzfnMDAbXP3G8+MoXaw8V3BZdZ6m9360YOYbOfh1l1TotHFsWtZTEsdbs/4xdhRome6Vq4CsuqdG+N17GsWSlA63CAMmBP1Pl3lwJxYWe9xksrlo01mRd9P5e5qdBFZNOuNVOKbu2tm6sVp7yoQ3G+jieS6YfSGljrJo8oifHBk2CZS7trKyORbutvZzBDwPGeGJ47Uzf3t7JYedO29IcYiuDfdfTwS7jrH9wFMnFubsHKrP/bt5ZQbjYosVz1u7DtTUW6JmFkdRJ6DEFb6cwraeQVfn9Y5qCNgim77k9+3jTHKxD0L3CTaJmfQnfhw5nfpiJhE7Zj5vRHDoSMEc7paW32d4qnqgPjC63MRHpwSqi0W4/2d73hLkpSMsavvd74fIz47hX0+bm57z06otS4nSk2fJLKRN3LHX/QrW66cm+vH8MVcISUWadxQV8NxMrx8x2Urzo94NLzrEOjM0YG80fF6vaoqtvAKb6OZO4RkME+/36XYlq9LVdsSUnhx+dE5SvdLK5NC3dvlNmkHY29VYELWEigj0BW87y4tKaN2F+1UBQ+8ZDpub3Kxv8lQu5RYzolWHF54V8XrCL3iBxSrVgkWhZrfnjHRw2LVu7pnGXFCR2zLgEm3+Umoxl7GVdNdLp22PGX5oXElGHEzCchcDpfSVQ/rOuEvF7yZYPbuQOsqa0YU2Xujl9P5HVcxA0F4Y22IlrAsGM1auhZmI6tNcuBqAeOYDUzEJIymfZgwJa6d90K4xqgq1idI1r0dJhJ0Ul7MkRQaHXazsjSR+IjE6cT1oWME6ngc+3CT3h1/2Zd8qWKluzoWnUvye/IEQ0qHhO0KVuJeMhR3zRTR4QY3N/PaayqOxqK9RRE3WSqpdS9XBVrsl5sCCSR/Q0+ZVYeZ0sMHuD2m/kDCS8RLN5WEKRJ67Gqn7jvN35DnZblvB68gI5g8COR1UyZTfuavccnGzk231KVceatNCttr90yTCTEcDb9dMmnrL6FeGIaAFNi0u2yjyjhqrY/B/IGC4e6O4dGp8MYNxW4jcpx4dCc0BzRmDaMfloRFbaeNbGWjgdulvAw3RJaA5trUrTFdL7e1Ip99wKbZkawsariyMxWzUKK1eV3ehw0YQZdo1ueyslmedr5v2CG7xYF32nZkduGq5YjMSaYQRig89E691gTjAeYpybaVY332m/SkNidt7arnFs5hHnQB5OYQajBPKuHU5EEDVevbleCrqdnECH51OtJv7RAYPrx6soMdlcw0GgZZXXRCOcRnV1tudNuqDX/JtOkKHa0lK4biakuWyWlLyXobbiuEdgtayJMqSSikvHrOFZTgWoprNIXqfWCwnj+5RHkT4BsmcJu8QI+77dIEwHa5H/tAPWLmCSeVwm1gmK1WLbKy+7Utcfzy6ASe47sI29+9HY3F5H7LVStkLyi42tkMy2HjHj2DSSXl1R10ZLQQ9z2EQbvlantF5WkLoUmrhAorh/4hKsBUepUVjLmTHLkf71xdnAWn9Cw4zfloRfDHluELwqcpivrL24e33w/73v7ld9Lm05//ZwdNz/Oi97dOHqeYgeN/fvD6/K+L9NcPb7WXAIGeh2lN2kWvY6m/OUr7+M8OKufd0/M1r/fz6OdpeutE88vPb0nud01bT1+bIn28cwJ2uF0zvzDZzO/UeuD7T8ewLyXmM7rHqfTXtvj6PCx+m19nnF8lCfzEaYPXz+h1tPjhzX+91vQV2WBfg7qc1Xy9tAC0Qz5Bn5C33/4vladLpqcuAAA= -->
