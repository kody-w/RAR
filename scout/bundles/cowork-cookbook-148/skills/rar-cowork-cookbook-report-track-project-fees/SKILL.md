---
name: "rar-cowork-cookbook-report-track-project-fees"
description: "Builds a read-only summary report of track project fees from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_track_project_fees", "rar_sha256": "965935fb3f96d3b4488fa85ddef96a67ac81ce4870e398fbfd8f7da60b0f2261", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_track_project_fees`. The original RAPP
agent is preserved byte-for-byte in `report_track_project_fees_agent.py` and in the RCI capsule.

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

Track project fees Summary Report — Builds a read-only summary report of track project fees from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-track-project-fees
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
      "description": "Dimensions to break down by where applicable, e.g. department, category, responsible owner.",
      "type": "string"
    },
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
      "description": "Name of the Excel workbook to produce, e.g. report-track-project-fees-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_track_project_fees_agent.py` and embedded as the fenced Python below (sha256 965935fb3f96d3b4…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_track_project_fees_agent.py` first:

```bash
python3 report_track_project_fees_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_track_project_fees_agent.py   # or on stdin
python3 report_track_project_fees_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Track project fees Summary Report — Builds a read-only summary report of track project fees from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-track-project-fees
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_track_project_fees',
    "version": '3.0.3',
    "display_name": 'Track project fees Summary Report',
    "description": 'Builds a read-only summary report of track project fees from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'project_to_profit', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-track-project-fees',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-track-project-fees',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '43c0f49d0f581df5',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/manage-project-delivery/track-project-fees'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/report-track-project-fees', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'breakdown_dimensions': 'Dimensions to break down by where applicable, e.g. department, category, responsible owner.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report against, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. report-track-project-fees-2026-05-24.xlsx.', 'period': 'Posted period to report on; defaults to the most recent posted period available.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives leadership a fast, repeatable view of where track project fees stands so decisions are made on facts rather than spreadsheet stitches.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build a summary report of track project fees for the most recent posted period available in the tenant (USMF demo data is mostly FY2017). Include totals, by-dimension breakdowns (by department / category / responsible owner where applicable), and a 'Top 10 by value' section. Output an Excel workbook 'report-track-project-fees-2026-05-24.xlsx' with Summary, Detail, and Top10 sheets. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads track project fees records, computes summary statistics and groupings, and emits an Excel report.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only summary report of track project fees from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.', 'example_request': 'Build a track project fees summary report for USMF for the latest posted period as an Excel workbook.', 'inputs': [{'description': 'D365 legal entity to report against, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Posted period to report on; defaults to the most recent posted period available.', 'name': 'period'}, {'description': 'Dimensions to break down by where applicable, e.g. department, category, responsible owner.', 'name': 'breakdown_dimensions'}, {'description': 'Name of the Excel workbook to produce, e.g. report-track-project-fees-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a totals/breakdown/top-10 report of track project fees from D365 ERP data, without modifying any records.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ReportTrackProjectFees(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportTrackProjectFees'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'breakdown_dimensions': {'description': 'Dimensions to break down by where applicable, e.g. department, category, responsible owner.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report against, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. report-track-project-fees-2026-05-24.xlsx.', 'type': 'string'}, 'period': {'description': 'Posted period to report on; defaults to the most recent posted period available.', 'type': 'string'}},
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
    print(ReportTrackProjectFees().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/9V6adOjRrbmX9G8N2JsX6pe9q06bsQAEohFCO0CV0eZHcS+g3z7v08iqcp2d7lvd8R8GVXZEpB58qzPc7KSX9/sro2K+u3T28G384Vkp2kc+fXCzr2FUAxFnYCvInHAfwu3yNs6drq2qJu3D2+e37h1XLZxkYPpfBenXrOwF7Vvex+LPJ0WTZdldj2BO2VRt4siWLS17SaLsi5uvtsuAt9vFkFdZIvllNtZ7DYLnCIX4v8+CJtFUAAlFmHc+/ki9UM7Xfh5G7fTQ7OyaFoffPl1XHgfwAJtV+dxHoKHi9Xo+uli1vyh9BC30eLw1OTDYum3dpx+eAg5FiWKLJrI99vmHdjjj3ZWpn7z9unnv354i8Hvt0+/vrmp3YBbb/uHEcfZAOOpvwjUB9NSOw/B83ICfszBNVAK6J6BW54fLF5XPzZ+GnxY/Od/JoNdh81Pnz7ni9fn89v8Z9/lizbyF21hP0xz7dJ24hQY/L7g0sGempeVs4sbEIY8fH/O/E1SUS7+a37243OR99Bvf/z8VgAV7DlIn99+WgCnfn6ru/n3+yyl/PGn97QY/PrHn36T03TOIz5AGND6/cvr+iUWDPxtaBwsvhyMlfBaq/bduPSB8N/ZN3+eqr/EvVzy5Tn4x6L8sPi+5Nme/wL6PhPNAXK/Lxb4AMx8e78Vcf7ja426AIlj567/409/JtaNfDdJ46b9l+T+/BQcgewG3nq55KcPj/D9dQG9bPsm88+XLUHC/DuWgOFfl/vmqD+T/Yjs34lO4xyU2ddYflfc9yZA/7X4+U9t+2cTPiyCz29LPwWVW9tO6n9a/PpIkZ9/8H67+cNf/wZE/49iDkVXuw8JXzI7jwO/ab98+fmH5nH7h7/+/ENXgiz27exLV6ffk/k9vz7W+YMHX6N+/ONcsP4pT/JiyBffamjxa1H+r/pv74uzncbeb/ebT4vfV+L8gRazEV8Xfbrgd9XYAF1/58ef3v4GMCcH1nTu4zHAj//4j8UmduuiKYJ2cXCLrl2AALdx5s/KH6O4WYC/M2rUPvBrEwPHvsa9IHbWGMDuL//HfUD5R/cF5fATkr888PjLa/CXGY9/eV8cgcCijsM4B6C75wzjc26HAHznxcrab/y6BwDlTK3/EdTxx/nHIs4Xv/ypzC+P6e/l9MsDd+Mn0u0FeUa5pkv999meSwSQ/qm9C2DcH323A5LTwgVqBDEA5hnomyLtAUrOtjdJnKYLLwY4AhjpSQzAP59mYb/88otjN9Hn/AnL+OJJVQ0MBnxTZ/HxI7AnSOMwaj/nvhsVix9+/dsPi/9e/LNZD+HzGgYghpf3gYbKYasvQDV1GRgGAgNCCaDi4f1f//byKhCTA24FsYqD2H9OBtmY+N5XFx/W3EeMpBaOD1wL3JrNLp2JLW7fF3Kw+Kbvi1RnNogAGS48v/Rzz8/dCUi1gTnfPJkX7aIBKdcEgP+6xn+s+otT2w8VM1DWdvvLYiMYgHuKFPxvVvMxCEwu8hi4/1sCPO8DIfUPzYL/KuJ9oc/5tyjt2i6j2n6tEdjPuMxE/poOhNuL3B8+5zO9+rOrHsXwdA8YBDzjvkL6cY456DkAc+de83Xtxxh7Zsjjgynrz3nzSnS7nkPhAuAHi4Zd7M3w/5dXSjVR0aXew39A01nSKwreKyqPHDz+Y3/yah0WT/5ffO4wBCUW/593O7OtnCTtVxJ3XC0XK/24N58xmHu8OVbPtnDWYFbtUW+/tSRfYecr+n7O0xgkVD395TnyEbnXmCeidTUwYM/tH/JB2oAYzHIfWT1naV3P9WB/zr/CPFB68cA0EFgAAaBE5sz8uuD89KumEajz+fo3yn9kQe3NZoPMXZSdk4KsAv73nDkgbTQH7WskQYr7c7CGKHajP1g1hwDEE8hfACViUGuACt6/Qe/z6VfV/zDx2dnMUx5dXwcKs34IAHr4s4JzQOZQAfXaZ0sN7Pz0EALMyMp2tt0BpQEsfd70a7/q4iZuZxh8+tUvAfZ+nL+fls53/bEEuQacBXK+7IB3H1Uy50oG+hagAwAKUDRZnAMeB055OeEh0M7mkgeQ+mo0nxIft18G+Y/Smgno68TZkHnOzOnP5Lbz6ffIcPxemgB52Tzise7fZ9q31WbZMzo2AOHAil+fPsn//cnfzwZh8VXup3/Ys/z4721rHox8+mMCfFpEbVs2n2D4yaJfSfQdYBP81LV5EerHR8l/fJX8x7nk/yDwaeunxb+n1B9EvIri0wJ9R96R+ZH2SqrXB/hA+MibH4n56ed87/8GmWD5IgNZNUdsAgz+jd++DgEkF9YAfsDgJ981M00OgJkfAA/c/zn/fZbPVQb4Iw/nrGyK31X/g+hBxj+j9Y2HwKO8BWt7cyMY+vO261ETjf/2Ke/S9MMbgEb/n223ZpLJ5hxu5t0Z8DSAxTb2H1cO0CvxQJV+8UCO5s2zj/r173aqy2/PZkh5zFnMk2aHAFMBi9hlCbSac/rDwn8P32d2tet2pqsPwJTWD4sZXkE3UgIpj7YLzAccAvRrp3LW/7lFm5u6B06N7T/qsX38sNP3F043v0/+F1/NfP27Gn26HLjaBWZ/WHhAlWbmV+Dy2SNzfdsNKBhQK9/V5UEtX57U8h3HzHz0B/aZm4Enndnho6Rf/jgdNuJ3F/jW3v6j9AvoM2aBXvFpptwPL6QD32BLAtz6dXcBzHrt9x6b8rwDW+mf553NHPzHlPkHmAO+vk369s8Rjv/21+/p9YDDL3NqPhPs77XTZ5ibORt4+e84FegM1vU692s2/Gmtf8QQjPqIkB8x4n1Mm/G7LnrS+D9qYPye5X/n+SL/C/BIYHdp+0jYWcNsbvlAMsz894fuYGH3IJPmzP3O2mDxB4sALp5d+lusfvNY8dgYPtRM7fb57xi/voF6s0Gu2a+Ke+0swHAAuh+bub+CARqBBcH1EzfAs399z/Ga2EQ2aH3BTJYiWZwMHDxgKQ93CIJhApshPeAFlrIp2nYZ1PUJhkZ8nGUCJ/CYgPZsCnGQAMMoFMh7ws6XuXuMZ2VIlg4QlsUCAsWQWRBGeB5DMZRL0hhis45NOiRrO79NTeLce1n4tGh237ftz+yJl6EAdigCjFwTjcw9PwLMog6M0c6kXaErwozpcOlKEVTQdspYlE7JTD5iQyLoYr5ka8vsZEVIDlvFJuolafEjv9G5NaUYmBCUHkNvTsJexE60TW8RTBAEJV+md7K/E/eCsXySvnbMtGTEMumCUomKs3mocnHv5BZvpJd8025I80pgKAypKXV290q5MiOXb0WzdNOLvWwqnTJOp+hIl4pNYkV8dPZlQ6SC5uA0fNTu0J3obx6mlm7EO+OeTdVIJYVIjpBJBq2LIsvkqryeIqDFeEF2oSZKF3/sElVjrmWJchmROCk6dGndnPWrOnj9pI9y0YTHxNqQopIeCWp1TVrL1uCrD+fZPcjLjPSv5RTErIGnkAlBnThqK7tCho0cq3KHTlnKmtVojmi12u3NhigOPnH2+eFyyQRshBGkj/cmjeZlx0/3eO+EoZQKEsEHQa4xkBXwQr7J/Mn1Ja0dTjKJJxtkd2CP1lI6UIm2EQZoSu9roVF2xPGciVRp31qCMlqfv7Z6P/HxQWCV3e5WRVNs2G4IGxNyOkTTkbJXEqXqdqKxVlilinKoS2uEJKrZMwcj2MlYKG9G7gQ5qSrTioJZLEHmUX9s1qp7sIowgc5yKiWJSxJbMT6M+6wI+eAiFM3ttj+nYYhuMy4g8MtJcq7hXrwJmB3d1atB+uMt7Mo9avubqOnbzKBIAT/s4KQMcZQ/qEXTRIrQnw+81oSQnogrWI5k8aYFo5Rtxmnd50UiSljIHHilPjnl1XDOTnLhC5URduQqXxkEYogtN1xwdec0l3otFOJubG+7DKs5FdGXPpdiuHWuT4ckuccsmqlto5R0hV6saFQnEVKFfijX3qHaiueENcrdCLuSGC0hhrvCo1TIedwhkbU0G1+51vLlBiH6kTirkya3xnE6HJPYljyS8KrNXdpQRTrS9zXNtjeKLSOmQ2iDXm8qo4DSbXiuYdQYxyU83eBltmRtmV7CDYzfGKoJxha/WVvSrQWbUScuHlq95uJVtL/QK04rzmTOnymicDYhe6p4Zh9uNDIm2dpoc27Zb+xYMSwft49K5ipootIyX18q6Bi1EXN3VC67JLZdrfiqR0JF2w/CPeCuqX9anvH83vXrBhIneOWYDEb46bD0gVcaTQunwdncmyOth04WBNzBzHDYhza7xtrKqKm5rCPgUhkd07rAyPQS3I6khNwGCXaZOL9ceL0jC3gIcdE9lnspUQCKLwe+OzPWzj5tA4squyCSGl2yAtbfIGq2QjA6vQg73QlA7saovKSdU7YEmFFKrkR1keN0V+2Oxnxkq/uJDIMxzvi0GOOLWtO9KfMXttqn/srdlHfN2PaGtmqisWJPfXXWUd86aQbr8tFRJJNT4/v6QCeYRQBaGFTBOdyxK3UKbIyapnA1CAi72U0r2Oh9WLYFX9tt/Ig5HI1lj+lbtRGSmIEwKURvmEycghWPh6AW642Lb7H1yrg5LmxJkGKmbbhql6GAUkrdX3mivm28oTQ4u1TFbofrPJ8UvLapb5YvOgGmX/nAkGBiUM5rgSNJj1RPPu1hDmPI1KbgCwjTmYAkp8o6Jp7MNExhrnFCQtmkNIyrEKRxZ3r8dr297JiejQXCY9XW3E03b43sRnxsy63Edd2GRcz46lpBI8OW19RHp48aPVTObLG9kLFVdEtTZtc8pJ3vjKoJsuRHeMKX2FJd8ZfB4neHeyYppVDHHF7iXqvh0z7XK3/PBaCQSQFqy1ypFGxz4tQ4OxE1REVTpqGpExx20/YkRDcdkyzpqt987sBvaTrXTWcsUqQaOFy5mvC53NdCJjj+qetD13VVlU/6BlVsaPDrNCQvRYgxhYBBB6II7goAKk3wT3lyhxjjSLIBvq5CLqd52WKk8yU+7Q7BWS0wf9xRN4EBSi3jsW9g2186VxfZZl3E8z1AVGi9Z9oejk3qcodp+uDsGavD1WMvV+rWtvKhwmSZu1qr1l8CcuCJ7BKp69GNsrW105oMIpZOKKPnwCR51Dsye1LZsGQzhcqNVQaiJtcaoSDj0u45fzcO62hDSKSQS8ulIe6PVkneorU67syhpxu2IIQY9wZKGMSNddxewmTFFGhbbrY9iY1GkxVkTAysGqCYpAdi220MtbnkcYHfCSV2zhAKaeFau/HBDtGobUIcsMZqDWJ/QFXH4E5XRDZ3Ik3Qt5bNiBULn50jI29daq8K69v2oEj60lVCf40EWR7c3B2rSFpMQUEi74v7aZs4rOm6O98b+ko7GcvCSIvLHWnZAS+gpkq4Q8OKXnve7WVeX2Gx6I900o2xuJngG3afrsi+v64E7mLFuK+tEmGFL+WU1cXJjuUAbqEmHDTr5K84c7wcc3O765P1lujFulTXcX2KhU2IX9OI2FymlWldJQE2DrGq6mZsppozObEc7hHuVG6US1ijZIceovhIyKQ5iEo8qQrinwNFy/a7E08Rss6nntewJ8S8hjnDepUcud3ajjpFvZYD1JttWYnFJedl6hpiWqrnLnst2JWCT1dRpzLvwKY5JvubrUJOLcUqqs8Kh40wrsPcrNW9Rl7HSyNel7jusrvsuEkK8+ZF4NZWUbzYSAIlXo+syZV23BG35iSacrGx6cY5GGMdI0OYsPBhhFlFH7klLlrNNHa6MFS0suFVOgkt8b4OrmpbbZ0J9CJaYuVl20Kg42pWq5C7pdfuRpol6vN2DSp1uzmlW/NqUcH6TBIW3WD+jsm2rmUMOutxyy16rwheqs/nJEZjU+GUSUmkXRfiu5KAptNS0STW1mJxJ6NxHJRT1snuKqNh3xSoyoQSaats4Cjl8J0rrrcwNx7y9iKw2qGewkgIU/OY1Yl/h/josNpFVrleEnLqJ8QNTaJt7F5LSAnH2Nz2SctLOszSq8A7uMRqb1QMbuWJdZ5iXZcF0HxUaAknnFEcUeK+oq+pzladBKtwD0d7GaRIePci0CRORzlbQyDdqYSZTmvNguPVYSJvIFEVo7mtVY1u0668x4GhuYi1y5H0GpbCITE4hJq4cHcuyk0oJe41X5K+JWRNuCM3a2mvrMSjEVJheYrWzHLCSq3N0QNciYFUDDtdhjxet6R73a0yPuvSHlbHq8e1NsfciIt8Ey2X4siL6d8mU8MNP0SQ1Favfbczt6uWvaR07Y+IdDlXWrPbTjWWTFmZrDERkXfyKO7JmAt90Moa1VQa47WwEbwi1AsB1Vf+lntS2bpF7Ij8BdusVYhgsR3Ousa6a60VUWHKVoo3jRzXvWBVhcJ569qSLVIVNhU3eSZHSWywPhaUD69HhpXuYGfRQydqBTGZmqu2id39MvUJVE3vQ2pw096uefwG1UWI7PlOZ0p6dZ1Wp1WqG815JKE48dFtI01tlW5BWyZeRvgoyoeWvktoCBp3U1r5B+Z223DYUg5tc9XvBbQjcAzsIdAyJFXdW+6alXE8xkrBYCvZlIbudtr47N49Skogb1LVkBMnInmVRPY3ZO/c9qHXTMOgKFPpai61DWDkcPYY4XShQ4yl1RidCi+FiSsHhcLpntthyNU9j+BjuArRc9XrDQ02eRw6hZbUwqa+9qpDc+fZKDns13UnFO1ZkjkbkcQLdiI2wjZenVcrPg1g+IZQmxTendkeuXOlPNQDbxYrVzO9Mx2manw/mqFgYt1qn9zk9cGIqQiJ6HBpImub5FiBPSsl4a780NKQZTVcskHDJjAeMtk93NI9vvbaYBXbCpJ2Ct3r45SSw2o0TtWZIZt9y+ab/Dqi52MiSEt51bHHbXbJ7fqsKpqHHdZn5+w7ZnmwlSbDAuCRkyuADuUOmWuYyKBsOREnIWEM0Bdtuvs9Pt24E+5AljdtKv0yJFBxHSaZo5jxcjKnTbm+ZpxRVQTLiVe1DNIT6cqQRXs7tpz27K0aplM36hc+MpHL5apkNGel3C0cOkHO+u1ZDoaTaZfy2SbVm07Ed9tO+LY6pB6ltyV6kYtKEIZ2q3EhZJ7LW3q+UL10D3qwjdT4/tDZYOke9qAbAVBvnU3T3mXku30+TlOiiCIs4x4SME2zoYdVWCQdG0UemSPHoL1M0T6DQEV4SR8bXFcv/QN/IOkLfYSpo0S2dazDIq4F3Rm5r9e7bIdiTGCgSASvD7c+72I94bilWurGtdroOnwlk7g/QplMRJ3feCdDlmOOPWhVqxNKdJJI5KRG/bKK4MgNCUq4lmtasCtPiZqrlNe7jcOFBHmdpLZNG7JE6T10adbmYC5xh7hFHai41W5qcKneWMbUhmil0VwrOdFuQhV3OO7290vjrO2LJ4kUFMWN1LUY5/AlnZu2Ul6JqRpayFeK3jNPhzryj3f1ouQWpV1iO8LloPbWxpmO6OLQEpgfHVu6XsXbrGIdnshRhsFqsmktH3NuirZCm8DuDBOqd8taQQlkmW8Ltt05hQpqXKnxPRze1MPl7GfGtg7pa6INaFZX58iPl03stJNLQFaNopCXL49VcoOlQKpN8lIdPQEdFai4DYcqsepD7KaFN1FLKnRjr0KWjg6gIrlzR6bX07vpdenNragWHk7L43Biz37PxKYD64OIrSM2uxPEzYimTm9TjNR7veMRF3AEJAWh4SwNGSkutdmweNHDOKrBYY/eNEB+mn5HYREeqwPG8DefuV91RIKQ23lVwvxdc7yTvyOY7Wil6SYolTUy7oeeWdpnmtKuFJIOEtdOUSuvIjozCE44rCNO9XV4r+RsGmJKeNEYfENZlHo8lB3eW/ZybCK7QVmRbvoJz/TtjkJGJSIHcpnAF6gaVbzc0m7MdNN2ye0KlTJghq1r7Ybg8cW40xzhD57RUeFonZZIYjt3NdkfmJXo37Uud5w6KvfXCtRG6+rbuyig69IW2aldU27aazXVeM2AeKskS5BQ2nNxd+QHCGLMc4tZ+agf5cPmaKOoIHTROeqVGLR1SH09M9kYVJLtnggpRam2HYmxoRu/YW5NQ5ASvyZ764QxWRD7XVoSu5YN9yqROhvCWdVrL4SixKtXVqolUmgO92MMsYx76svaPjkZpUNlAXq4W54OSiGADp/Teylps3UTSRAvnRIXawjIXduJivT9jVe0A1SLOdPdCsozAo/Br/fwHFvrM5OkCtmb2VbAsW0RnQ33vFx2Nu4rMXo0r2R9704xibe6ftj2sOJH+REae+9wP4r68epdzdjqdlOfN1srtqodnrEXvalLo1WCiYzXm4pMRSxroAZH7/TxnLptZ6IUlNfmjggJqOUCRxJYQr8wSqXCy9G+oDXRyjTeIghZbgHyXUZ8l5iZodvIYNMcxVe7Dt1Um3w63g60C3WZyGeSXfnIcuVdl6dtf81ts9ttQjV3inUvIW2mm5yR3WByqyKIKFrLW2P4XAFRCpUhzpRMWHDnKrzhfJPtCEi82ZBOoSSNn+2j3QeZVuJ53QdqWmOmRfdHDNjSSiLYfFgo3l8nOvOOOFLR3fUunvV70VcuQl8yvOqdy1aLIMbB1NoPI+XelWddJOigdE9Xg7YRYn/C4FBn9mXD2Yy4L31YIr1bRiJUja1sXUWxYo0uJS/FbfdospXOiI5HuwaZrruk6XMez66hE4bkUZ1u8fIs+H0bg9ZisG+bFq9PwWWUGBu6imjIZ6NWJevxvivXWW+K7GpD9cZqK24MkitbgPJ36LQRD5Y8XhsLALOO3rPzYbANkl+vuQhOm6s9moAXEhyP/TGrAx7jSZvcXc70alsM2RGyKzai79eWtjmPc0lxUiNCjvT9JtyO3bBj0fO9Gbwb42bnNWaFlbhmYWjpGsjO2bf7NWWd8HhAagsrac1oNcQtt6MjM5oHOsM90aEe7linsc6Y1lOzm5PaJAOV51O9NFWUvmwdub8NWMPYYdckmwhFNHkI8C6ZHIbdaX0+qmRfcVi6q5x+W+OXpBeqrX3kqKynr25L5gQZ+gc8ocaLrgRKwVXtcUh4HzrzMnS4NMFptVIam/IvWnHNSQWJStzeXk+u39EaWntmFDidTyeCtYJLTe1q7whL9SUiJ4eE8YGx4bIZXRYCXSU3jZdYZcV7Hq4QU2rdrRLBPswa5IocHUTESuQMry5nlbDHsaUxiujRY3XocIgswSbgyrYnvoD6CrraPN7jWpZuiYiKMM1DvPuoVEtY9QpbtBFbqngxYG2sPgbput8luIvSKzJ0MxyUh2azwOTzGLbQQVmaw3K/y053m0JvF3PPlm56x/l6R94QYSPwdZ4aobo3NXQpV2Fwa5meW0aICfNNjt09p6E3G08OCWKTGrexYo4XV2po22ldhZL9wy2vtMIv9wFPFUa9FAzU2uMIy1AW3tRR31YNoAlXXrO6TwiBtNNgeI+XQtHk7G3Y4I6oINq6OerjIGT5cSxQ3Cm9Uy2evAsi1m4FEYzb9e0t2Rz39C1naiWvUbW1AK54pgRhFzr3uqWDW3djozKHvszElrlLTmzgWIu3ZbbEQ20JGl1vA9qsNqxYLMB1OdWO5JYwdH1PyFwl4iS6Io5H7rxixN15d6Vip7shhC6K1z3eS1kSKQS9vJdHY9/y2S4ttf21M5ZMsU6aiPK2ROJNYY9VxhW3ABW2UxewPntZuRe/iHo6yvCuuXg6x6zTa1Os7fu47YNDN7GJETqRBbC3kivTCncIeebhNoWvhkBDcNaHJwJ2Q3tDwFYysauLc9MNEhcqHcaiu7sVuoHlcUJc7gNs7Xr6jd5O/DEmI2cXctzbh7ffjuXe/ueXyOYjmv9nJ0XPQ52vL448Dhp92/v0WOvTv6DLXz+81W4MNHmefzVpF74Ojf7u9Ovjnx4aztOm55tYX0+KnyfhrR3O7yK/xSB3mraevjRF+nhRBMxwumZ+i7GZ1XLB9+/PRp8rPe88VG6LeVgQz/fifH79w/diu/Vfl+HrFPDDm/d6MekLTpFf/LqczXu9bwCswt+Rd/ztb/8XjD8IkzMuAAA= -->
