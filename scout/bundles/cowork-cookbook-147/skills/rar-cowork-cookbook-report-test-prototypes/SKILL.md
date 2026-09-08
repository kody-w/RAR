---
name: "rar-cowork-cookbook-report-test-prototypes"
description: "Generates a read-only test prototypes summary report from Dynamics 365 F&SCM via the Cowork ERP plugin, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets. Call when you need that report."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_test_prototypes", "rar_sha256": "d2a50067f2fd2f1cf64f9c8618b9d1c64eb9355e2d8d347b773b66d4239b2734", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_test_prototypes`. The original RAPP
agent is preserved byte-for-byte in `report_test_prototypes_agent.py` and in the RCI capsule.

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

Test prototypes Summary Report — Generates a read-only test prototypes summary report from Dynamics 365 F&SCM via the Cowork ERP plugin, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets. Call when you need that report.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-test-prototypes
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
      "description": "Dimensions for breakdowns, such as department, category, or responsible owner, where applicable.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "Dynamics 365 legal entity to report on, e.g. USMF.",
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
      "description": "Name of the Excel workbook to produce, e.g. report-test-prototypes-2026-05-24.xlsx.",
      "type": "string"
    },
    "period": {
      "description": "Posted period to report on; defaults to the most recent posted period available in the tenant.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_test_prototypes_agent.py` and embedded as the fenced Python below (sha256 d2a50067f2fd2f1c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_test_prototypes_agent.py` first:

```bash
python3 report_test_prototypes_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_test_prototypes_agent.py   # or on stdin
python3 report_test_prototypes_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Test prototypes Summary Report — Generates a read-only test prototypes summary report from Dynamics 365 F&SCM via the Cowork ERP plugin, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets. Call when you need that report.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-test-prototypes
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_test_prototypes',
    "version": '3.0.3',
    "display_name": 'Test prototypes Summary Report',
    "description": 'Generates a read-only test prototypes summary report from Dynamics 365 F&SCM via the Cowork ERP plugin, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets. Call when you need that report.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'concept_to_market', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-test-prototypes',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-test-prototypes',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '3954cb6e14522ff5',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/research-and-develop-offerings/test-prototypes'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/report-test-prototypes', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'breakdown_dimensions': 'Dimensions for breakdowns, such as department, category, or responsible owner, where applicable.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to report on, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. report-test-prototypes-2026-05-24.xlsx.', 'period': 'Posted period to report on; defaults to the most recent posted period available in the tenant.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives leadership a fast, repeatable view of where test prototypes stands so decisions are made on facts rather than spreadsheet stitches.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build a summary report of test prototypes for the most recent posted period available in the tenant (USMF demo data is mostly FY2017). Include totals, by-dimension breakdowns (by department / category / responsible owner where applicable), and a 'Top 10 by value' section. Output an Excel workbook 'report-test-prototypes-2026-05-24.xlsx' with Summary, Detail, and Top10 sheets. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads test prototypes records, computes summary statistics and groupings, and emits an Excel report.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Generates a read-only test prototypes summary report from Dynamics 365 F&SCM via the Cowork ERP plugin, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets. Call when you need that report.', 'example_request': 'Build a test prototypes summary report for USMF from the latest posted period as an Excel workbook with a Top 10 sheet.', 'inputs': [{'description': 'Dynamics 365 legal entity to report on, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Posted period to report on; defaults to the most recent posted period available in the tenant.', 'name': 'period'}, {'description': 'Name of the Excel workbook to produce, e.g. report-test-prototypes-2026-05-24.xlsx.', 'name': 'output_filename'}, {'description': 'Dimensions for breakdowns, such as department, category, or responsible owner, where applicable.', 'name': 'breakdown_dimensions'}], 'model': 'claude-opus-5', 'when_to_use': 'Use when a user wants a read-only summary report of test prototypes activity from Dynamics 365 F&SCM, with totals, dimension breakdowns, and a Top 10 by value list.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ReportTestPrototypes(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportTestPrototypes'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'breakdown_dimensions': {'description': 'Dimensions for breakdowns, such as department, category, or responsible owner, where applicable.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to report on, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. report-test-prototypes-2026-05-24.xlsx.', 'type': 'string'}, 'period': {'description': 'Posted period to report on; defaults to the most recent posted period available in the tenant.', 'type': 'string'}},
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
    print(ReportTestPrototypes().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916adOi2JbuX/G+HXGrqsl8QUbNjo64CIioDDKIWHkiixlklBmqz3+/GzUzq+rk6SHifrrmoMDea17PWsvt729220RF9fbpTfPtfMHbaRpHfrWwc2/BFH1RJeCtSBzwb+EWeVPFTtsUVf324c3za7eKyyYucrCd93O/shu/XtiLyre9j0Wejgtw3SzKqmiKZizBs7rNMrsawYqyqJpFUBXZgh1zO4vdeoGRxGL7vzVGXHSxvWgi/6sEnKosyrQN4/wD2Nm0VR7nIRBxwQ2uny7mNQ8B+7iJFtqTxYcF6zd2nH54qKIX5WKJLJxx0dlp6y/qyPeb+n3BAH0XfeTni7FoF7nve4Cv3bzkewda+oOdlalfv3369W8f3mLw+e3T729uatfg1pv6WKcDLZVvSoJNqZ2H4Gk5Atvm4Lr0q6CoMnDL84PF6+rn2k+DD4t//dekt6uw/uXT53zxen1+m/+obf6wQlPYdQMkc+3SduI0bsb3BZ329li/rDHbvAauycP3587vlIDe/z4/+/nJ5D30m58/vxXl7CvguM9vvyyKCvCr2vnz+0yl/PmX97To/ernX77TqVvn5rvNTAxI/f7ldf0iCxZ+XxoHiy+awjEvXpXvxqUPiP9Bv/n1FP1F7mWSL8/FPxflh8WPKc/6/DuQ9xl8DqD7Y7LABmDn2/utiPOfXzyqovNzO3f9n3/5Z2TdyHeTNK6b/xbdX5+EIxDuwFovk/zy4eG+vy2gl27faP5ztiUImP+JJmD5V3bfDPXPaD88+xfSaZyDZPzqyx+S+9EG6N8Xv/5T3f6zDR8Wwec31k/jDsSdk/qfFr8/QuTXn7zvN3/6298B6f+SjFa0lfug8CWz8zgAuffly68/1Y/bP/3t15/aEkSxb2df2ir9Ec0f2fXB508WfK36+c97AX8jT/Kizxffcmjxe1H+r+rv74uzncbe9/v1p8UfM3F+QYtZia9Mnyb4QzbWQNY/2PGXt78DxMmBNq37eAzw41/+ZSHGblXURdAsNLdoAVa1eRNn/iy8HsX1AvydUaPygV3rGBj2tQ7E/+zhWeIiWPz2f9wHuH50X/AOPzHvywzZX75D9m/vCx1QK6oYwK+dLlRaUT7ndujnzcyprPzarzqATs7Y+B9BEn+cPyzifPHbjwl+eex9L8ffHsgcPzFOZYQZ3+o29d9nTcwZk59yuwDo/cF3W0A2LVwgQxADQJ5LQV2kHcDHWes6iQGUezFAEFCfxgdtYJlPM7HffvvNsevoc/4EZGzxLFw1DBZ8E2fx8SNQJkjjMGo+574bFYuffv/7T4v/WPxnux7EZx4KKAgvuwMJ95osLUAetRlYBlwCnAhA4mH33//+MikgA0rmAngpDmL/uRnEYeJ7X+2r7eiPKEEuHB/YFdg0m+05l764eV8IweKbvK96NdeBqAAV1/NLP/f83B0f5exz/s2SedEsahBsdQAqZFv7D66/OZX9EDEDCW03vy1ERgFVp0jBf7OYj0Vgc5HHwPzfvP+8D4hUP9WLzVcS7wtpjrxFaVd2GVX2i0dgP/0Cqs3X7YC4DWpu/zmfy6o/m+qRBk/zhHNDEbsvl36cfQ46EFDbc6/+yjt8NR1zgZ9rZPU5r18hblezK1wA+YBp2MbeDPz/9gqpOira1HvYD0g6U3p5wXt55RGD+l+al1dnsXgW/cXnFkWW+OL/y8ZnVp/meZXjaZ1jF5ykq9bTLXMTOLvv2TeCXmQBYvOZgt/7k68Y9BWKP+dpDGKsGv/tufLhzNeaJ7y1FZBApdUHfRBJwC0z3Uegz4FbVXOK2J/zr5gP1Fs8AA74GqBCMitQfGM4P/0qaQRSf77+Xv8fgVF5s4FAMC/K1klBoAXACI7tJkCq2Y9f/Qui3p8Tt49iN/qTVgtAHbgU0F8AIWKQfqAuvH/D4efTr6L/aeOzzZm3PFrAFuRq9SAA5PBnAWfXzU4F4jXPnhvo+elBBKiRlc2suwOyBWj6vOlX/r2N67iZkfFpV78EWPxxfn9qOt/1hxIkCDAWSIOyBdZ9JM4cVRloYoAMADtAHmVxDoo6MMrLCA+CdjajAIibV9f5pPi4/VLIf2TbXI2+bpwVmffMBf4Z9XY+/hEs9B+FCaCXzSsefP8aad+4zbRnwKwB6AGOX58+O4H3ZzF/dguLr3Q//cNQ8/P/bO55lGfjzwHwaRE1TVl/guFnSf1aUd8BXMFPWetXdf0448LH77jwJ2pPRT8t/mcS/YnEKyM+LZbvyDsyPzq+Iur1AgZgPm6sj/j89HOu+t8hFLAvMhBSs7vGGTG+1ruvS0DRCys/nBc/6189l80ZRB6AD2z/Of9jiM8pBupJHs4hWRd/SP1H4Qfh/nTVt7oEHuUN4O3NLWHoz+PXIyFq/+1T3qbphzcAmP4/H7vmkpPN4VvPMxqwMmismth/XDlAqsQDCfrFA+GZ189+6ve/TLHst2ePcPq2aVagBekPUh3UVrtq5mL1AQje+GExYy5YDNqREmx8dFxgi199mG0DypBdlkCNOQNmjWZhAafnvDZ3eA+cGpp/FEZ+fLDT9xei138M/lcJm0v4H3L0aXUgrAt0/7DwHnUJyAasPptlzm+7Th7K/VCWFLg3/QJ0A+n2A+v8sWA9li6eSx99wrOyFaBU+e/h+8LQxO0PeXxrd/+RgTmXIEDLKz7NhfjDC+zAOxhRgLm/ThtAs9f89xjR8xaM1r/Ok84cBI8t8wewB7x92/TtKwvHf/vbj+R6IOKXOUCfYfZX6aQZ6UAlmA39lwIMZAZ8vdb1X9r/ON0/oghKfkSIjyj+PqT18EP7APPEhfeP7JXi8S3A8/GfLP5vwByB3aYgo5riIV42d4EgGOb6V/5pn92BSHqg8auHauaa2PxAEiDKo6aAyjxb97vbvhuveMyMD6FTu3l+xfH7G0hBG0Se/UrC19ABlgMI/ljPDRgM4AkwBNdPIAHP/pvjyGtXHdmgMZ6/T0FtAkFIKkADDw2WbkDiwdpdkcuVs/aWLon7zhojCB/1Vh6GUw5FYQ5JejiKrR2UwnBA7wlCX+beMp4lmcUABvgIcMz//hjc8l4qPEWe7fNt+plVfWkCoIbEwcodXgv088XA66VDmZQzSheoIlsr7c+H+/VS7I/dtUiqyYpEijkJiKkpcpPGeJgcVAHNza0QHNmpZSybviBaV6fBibiiVpHc9/UeXaJojzAms8+nsid2K5jI9rvctxSsjqNt2jZaum7EbXuo0WxiAqbzR2PKy+CWY/AqutSpQWT8PiV3wlWNFG9f1qqXXU0p3rfXDJ+UM5/zk+4e5PiUT8vJVIZV5eUDCnPlqdy2Vyc2t3AJc4eVv3Pv9V217xdNzEzzXI6lF+v0+TgRvBhxyPW+W0ZOpBFeNUiRldfhcBZrGzeP0yW73PATM6L4bS8e4uzQXNWUs243UdytGmPanlM3TvUj32bbEjrVfIj63aVaUiu/ukKDm+P1xVlDa4gRVWq1uZTNXi0P7uF+kRs3PbfDkk2ze7LnLNVqz9xRWQkIapjnLWOl9aZIbUJm61jN8LOQIqeJCeOK7o4K3KJ6ne3GSkhW2V2MmE4bWNlFLvHOnJgzg0QmP0gX8b4y2OIcW3gb71LviHjd7gpX9fame+gtNu7XiE/yWpT2hC4KV3yXLbXtKUmbGywUfdtv5DJRTJtMT4fO0k7no9pShk+L6WmPhoJ43+zhKj0IFIs1UzVMytHPLGBf7VqECXS2znxSuwQub2NtUMPidj5RTF1P5yK+D72W67QCOdVBlY6rvWZZXVa4U6oTxn17GBpHBl3DKo1lkoc77kwe2HUmxkW036Jn82RGXeNFxlVIHfdgQRt+OPImZNg5g+MRNq10htVVOcr2dTXcDB1amvtNzFRavSqMnFNwRNmu6T7DYsupL9OOKbanobmdUrSiD4jE+nTaYtdzhWgJR5z9LX9o6mtJmVB4v41qclydrsGgyWSjEwjLudF+mfiME8k2TOfLkl1x2iDjuhiFZrdCBS5rIEzS8TNJHcW4zVXDPenCVHexomcju7F3m0TJIprWdxaNMGom3ZJzvroqCS4s4XuK82wv7FpWyklki15gC1Z2CXSC9ArejiuObI+cvm2Out8Le0FbNkykHQ/ns2WqKCUo27FxQcPcB7HgqN6mycxQ2KL6RHuSP16VuLlGbSywx53O9mZCXaWGB3F2lCQzPSj0/ehskYrbtBt3SZykfBPIhOtP+EVfXZYh60Rbj7PLditFV39n6tfIK8jeQtc1ForrvUeR2FA2+r4nK7rKSuFI6KEJ5aa9VScZDrsYcuv17Wyq+3aPUHXl3YJpeeSjrR1X8MGWWdQOx0vTpWXZdlkK8fdeHqYLeR42mmJPYeuJYkVYENfdw+PpMmhJHUYwec03SnA3TDI57ojTLTP4NZ/a+gWJoPt2z4ibpBolYn1BODXNr3WktztXdscJHq9XLWegPchOSiuHcrSJK3RPuKPdbTVN6gkFW57KvAo3N5EhjrI1dra2nsw7NTInWimQ06aNifWIXFceFx+3aqKI7XTCVje97YqtECpSrktWb+aHG0xn0Mbzrzbbwkuc7taUFWm5ljQ1vSxcVr1HUrPe0Fvb0uWNhZzOQj/R4mSYaVLGsXkdq717gFf6Gr3omw6WeOtEI4qv4FAFqfh6RYo52VnMoUoTmIJk2ct3blfy5zxlTiiAotFJiGFFhOdV5DtLATt26bG5tBGW+XiC0kIwtLdMOGHriJDpsIXcNXLeHJdasMwU1HHkyfZIcdN4ws6p8Kn3pBSkN4ejygDT/kZ1td4UfKL3k54tt67I94hYQGrsu+Q1ksgVXK6tnYBk60rg+ExNrGuA0mqKicv9gV6VGYfnjJ3qmbNMHXVUNTk7lWdWFDJX9c2zvhFCpPZrKPTQzNWOElNvothDO8kwPbGZzFu0x080nfPZzXLQCI88s9qYLUof7OZ4OHk7x0UCShXW8kFASu2mUCso6HYgY0x2L/c6qWwJgLk8f6GMu0fVhh8PHRvW/ShiShcP9PHoSfIY3tTaxQIKh+SmWFnLFaRcbioOmeMqMKu2T6r+GuVdNlzpmnE4HiUkOCQy09rujydjRC+He6EVEoHs0EK/HzJ0mjI8K+7YuMeGayqft3SVD7uMzYU0UsVqswq1XmG2llRuFJKFFUnVS4PS+pBdlWv3xMD3frgV+wM8sfjhoAUqVO8nXtQEfLv3WGDJ8Yzr52BreB52JQddvI8E03dQs0kJiqttXVujvZ2ia62vlzBhrJWjdht868JtuME6H7im2jXqenPAqps79qpy13pcXg4J61IeLFAd7LAxJ7qjumfyWLIGIeL2lltbnYS6HiQOGpJsld3SwARgqKyAOAfmToEiO2NX0YWfW8ERKfPSmW6wigMX5Fiw3SHLs5rEB1sTicPlINihAHDMhUj3kJ6c89YUjWtMGUetCDnvKKYykydbUV8rLByXh4u6t2TxbB/YDcrFcZscBhIGAXe/FHVSSfvC8fNNfbvExsHSykOZX1WjOlqEe83FZIr34ZZiubOgoWG1tElc3TABKWy0Ph3i6QCS6kwZB35vmlsG2XvnKvDEtTFyQdjtExxRGcJGx8gd8XoqJ/8QtWU6mlmMr81e43JpMumelrhymow0E/OYx7OdsWlkmYD1Ag2QK0PDSZUdpOnecl1qpuNqGSrnbX6XRMsoec6p98hQYlaVGKspPaik3p6WimVkdBD3WMxFuWGzvgkDWA85K5xIF4ZG2FPpod9RXGlNfbtvR5s15eGOkqclRlCFrzSEfBc2eo/1mDxRBr3iJuswMGyuNSFFwgZphBgmkOrhZKaQ11UxJPVTT2FXbrxdRZPSYNiymYMANf1QLLcgZsoYIKgQXweBu/s1HZzsgmPMqeH5dbyNdpaAakFZxXwk1auap1ubjUctEJKeTBxBy7p9pimhfC5xpFB8tFLEg1BLF+56B0UVCy03ZQTTP/X+4XjZZ4c1IagFRRdnZ4+60t0ZMCKnQVej5xtd93MZbZb8ZS2GOsOVoXlKzrGuwqYwhiB9Rb3xDTS69hihr+GVvL/dC4l37lJtuNmk38gTD8EadN6zabHpR89170khjgEhMPyNPnrO2AZ3og3y24GGEpIiBcaIcDS7nDiGabbXhE5ut7Fwqgk3kETbiT2O7oWwtVacIYL2gwllEMprC7478NC1ZZQehnN98PteudLlqPnDStj21Y62RF1nN+K5ubi96ttcpO/zFb7JE71nTHKrnpLdMXD9s3sNuSbEmyxBPIIvzmOIc/2xyq98Ya82+w2fiao7ZlKpbQ15t99M9r1vedb37YQbjCgWBqKr0PwIbw9Wuj5FjWygxDUcTfoSQ5SIHXEsMbXzhERDxEVbUhvorTpqmdwZywPHla563msg7ppk5QP7IpOvb/BVdqtwWdECXj0DpAJDnzve4PON17OT1VL7XrsL3qEJI9yBR6jghZUAGl+zU2jt1J4hnhz3NWrd91t+xNY6wZQte/BQyXLMg0fZTtvpWRNuhnVf8owmm9ZpLKulwevbll/ukm3aR0knH9Ik9bMTUqC1FNwOMrdZKvDGiffpUSCYHey6nNZeRrY5Zdo+witcM5liJMuo1/vDBKoax6ywM5vLt3IJn9Qz0u+ja8u6l7oVllpMX+DM2FAbSpe9mNkkLUyFrcAm5r1ZluGlqsIAhS3ZLczBOckcFuBGa2x3LUKFOTperSQ6nvSVc9RvBwHrVc7S9+m0Wvkd27NL1iQn9XAHvUBgZRptDs1+MgVJ3RzZza73UGbLimi01anW8gz/LCxFfeyN4O42RCwq+LXHOfaaUUEA+smO6HZrSuzJYxs5bmw7XBof1mZGEg5Cabh3OMdoiBbyasycUrDxcorYYxJTfpnBe6M7F2nS1VR59Jsq39e1thnq1AyM0jHc2DvsWMg6rrgMzugRXzKJq4QaBPoiLEl4en9HV+PUbLirF6lrUOnDpKQ2jGMY12yIaofepsv4Qkf7aV+hteDcxilyqjw9UEpyhvmsQwSmF9N1PGkqTVgMWqa1xBZ1KhB97DplqVoEmDLuNI3YJe3YqXLhc6vRcTk4CA494XuWwfYhL5+569IYfH+6VKscCbYiuSSWIbwOHEazEPbmXYXW5ZxmX5BOvr05DbqBpBsFeQ2SkxrCDaWAeIPNtBFOdFfWGG/bVdHq7M5FXDYnTkJLm1EKAq/wVhGMn1jfEo2MvSzF4MAhg425ujWRphISYlLtdHRt+ogs0C1jaDbkJLeLbp12mr6r4EDjpdDyDZ8R6ojPr+uGp4oBWuoMRaTHY3BZuWghdfhS9VcXhS3l+AjS9rpmqjODZ0NFu1RS1tiNE6xs00iBdemLe20qsbidfME53+OklOuAkbKilpl7eDmAsEDTc8aJpFwLVOUZKKYYnbNVmNU0iOKIaq63dGsmuFh5YCJmqm8uQ4F63drenaisROQOXwUBxhQUtvPI4o6HK9LGj7d1m0s9qg+iYkJwvjvnAKc6eRAdiqqmViQTuZe2JKYVQQI7BSY5E5jKhq6+HcT27JuJPPQE6L5XwrK6ybGZLWuma5mmWN8qAgm9jtXtIINP8La7kluyuHLYWMKlc6I3vLguXfm68nGB2RlnVYbsrRTfnDNvUQzfSCXsYG10c+31CFMpc6VXk3fZwQx0Olwu19YvJzlPL7tgQ3gHKqgwC71KU8vdb5uVTJe2xQf0XVj6Bb5twgCedhi8Cyje1IwraJ4pSAfQfjq20omyh+DCnYl7G9MBz51Ub9SgwgKNUH242UqyPJKWiE/QXpHPsrrMWi4jWCi1sQ17miZ6xWyFWxjqCr8yEpaccDtc6homTXLmxwkyWBIuy+HaEc1OysFAeFw1RDhlcrvSLN8VaSJAyqV/tKVjTdGXEj31FrPdXwYY6zzv6vvZSouALCwMbUoJQfmjePKTm+oTJxYrof1qGXtrFBcw2Fh3UoseYtxaB1p53/nL4625XmzNhKsdJUrhntvtc/6EhHzJhb6iTDyPndPrysIG7hSi3tW+UbRmt7ZaSeFkL5fO0YXRyKx4WT1bfqHwXj0J65wSDxW8EyP8Ch35qxKcM7wL4kBO9q6FePVVsKp+3KM+S69BDk8FWl2EPT0NcVaiOOMa2LW6m9VEG2wJZtU+zjNkXzD7lUlLHd/X5g7kFBTxRuKiNQ65yjURua5Llb2oQVWJkcWOHfA1UxzpgKHrCxkiUu1Omdc6ODNdyXFrSiMOnHU74ebOlNRL1kHp6VgM6GopUHAzUNuGj3ZL6CCZHst6qBcTGX67j26B28fsuvMdyUJANwwhKS7nnNtX2DW27dV5ChzJ8xhzvJyrvIHFK50OUel7dGD7rEdKcn28HzoWykwixxuBwtLlRLQyadvogDmckykiieA2ZZAeeWrF8F5jo37TqB4+oNtNxvNJwLJckB8NubvAttWewJqcKrhORmpTsmglva2A1KRDZ2JUSFTOGMGZX+uZQiDeVb8W5wqlJdHHApgZuiBb25DHtk05GZ3tIeS0RrutilGiCGOgYyXWUGwn6DGLKZSiLkN2UpBOubHhgaQyXnH3V1RtQBRivah7KYE1ymW/yQ2I3HLrrd4w6dAbkLQijDjaw7QDZmyBW+KHpCUO5HTN1vx6WZ2V7GiQ5+p23k6qYGJKGMS4e0LXLrZbWRsqrZrzyi83GG+FRyPGb2Sfap3D+jcnajlhOgR8yWNBk22V9dq3ONCHZRlbJ9h+UMvL0rE20G6FsZLByCLozgrPCwiHMWRPPgvKTRwl6u4cO4HYJlM3xrQSTdTRag/YYDq7Uiq3XqVffKqmR4mM6tuy8PadHKzjCt11F39XFRtkOwW5AFrZmF9uY4ay4Q0Le4l/kxBFRW2jOxEsrvm9QjIWVmRo5Yad2xfKualMKtfR2LEvIaGubUQDY1oyGNUI2d7dnG7xpVk6dnPbXki4bxqjLHl7WLKr2kWvwe7aWPaS1a6IHXWWr4eXEsAlQZBD6vnjeeqMfSMPlzPU3RpNBSNLIuab9dFXIcrSMXigkaautklHrnr1VBL2rpTpdQpt1FWUapdml6554k6e97je4Fc3uu8IA0tqrXEwqHI38s1EJqRwEQHGyT0ED3pAtka0hsiUbm54SmhXGz153D6JlkmcrEdhF4hHodjxvhsEULomAtIe2SAidttR606+ufK0w9hAWGaU6K1r2ouJVUoctqBXZwfVWbrrFduDPkPyPXy9VVrbufc5czkfUZfsXVEROPZitObac9wyyGKUyAIxlm6rnvQsUOPy5jAdMQ4ezf2R39g23WfOUfU0ysYkJYPafu/khhVCuCqKYbMeeGEj1x6X7KadQqC0y0QmLuUQqjleLt310uT562panVMtAqPqcseantP4JxYyPFZ12J2p4I1Ery38DFfoAcqdWIPWiUd65Rkz0Gqk/MKBzRL00YGSdOvbns8DxKFRIsDkyFsxmxYL3Z7y1aihrsfjUrjf2nvWODcTDeAUkZZBn4BOGQr6GrNbhBwy4BUsBPOd055bHIQCWiN9Neiw2C+rDIevqjxg3bo59tC4v65TKgUFbTyjW3R1XGOl14bddqCjNS5HAneSsEOJ8bbFFGF490mGLrTAMPMN7LZkWeJLpDjKF85d29eVVBxQbr3nD7c7HizBPMWd0AITu9aQCEQl13B9rXloi8JOBw2X+4hw0spdQTgyYm15SfC7NDCkyUhLqr30JhKtJlyQqPZ8SjGuYeTwYAUr9EJ4LgXj0BoCI680bnAqXrNSSQo1eveOBMbcpWA8kdQRI0W6cCVJN/KhyHcnDNqcTJm/UeUppOm3D2/fj+fe/ovfl81nN//Pjomepz1ff0DyOG30be/Tg9en/0qQv314q9wYiPE89qrTNnwdJf3l0Ovjj48N5z3j8+dZX8+Kn8fhjR3OP0x+i3OvrZtq/FIX6eOnImCH09bzjxrrWSIXvP/xaPTJ5u1x9uz6JRC9+JLZVeLP9+J8/gGI78V2478uw9fJ34c373UE/AUjiS9+Vc66vX50AFTC3pF37O3v/xfuDvRyVi4AAA== -->
