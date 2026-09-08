---
name: "rar-cowork-cookbook-ppt-exec-perform-predictive-maintenance"
description: "Builds a read-only executive PowerPoint deck on predictive maintenance status from Dynamics 365 F&SCM ERP data for a given legal entity, with KPI, trend, red-flag, action, and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_perform_predictive_maintenance", "rar_sha256": "47b06e8a98e6ea1d148deaff4cd2406c5c76d66f48ebcf5dc410b8a6177e6317", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_perform_predictive_maintenance`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_perform_predictive_maintenance_agent.py` and in the RCI capsule.

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

Perform predictive maintenance Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on predictive maintenance status from Dynamics 365 F&SCM ERP data for a given legal entity, with KPI, trend, red-flag, action, and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-perform-predictive-maintenance
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
    "comparison_period": {
      "description": "Prior period to compare against for the trend chart.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "Dynamics 365 legal entity to pull ERP data from, e.g. USMF.",
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
      "description": "Name of the .pptx file to produce, e.g. ppt-exec-perform-predictive-maintenance-2026-05-24.pptx.",
      "type": "string"
    },
    "review_length": {
      "description": "Length/format of the review the deck must fit, e.g. a 15-minute monthly review.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_perform_predictive_maintenance_agent.py` and embedded as the fenced Python below (sha256 47b06e8a98e6ea1d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_perform_predictive_maintenance_agent.py` first:

```bash
python3 ppt_exec_perform_predictive_maintenance_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_perform_predictive_maintenance_agent.py   # or on stdin
python3 ppt_exec_perform_predictive_maintenance_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Perform predictive maintenance Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on predictive maintenance status from Dynamics 365 F&SCM ERP data for a given legal entity, with KPI, trend, red-flag, action, and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-perform-predictive-maintenance
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_perform_predictive_maintenance',
    "version": '3.0.3',
    "display_name": 'Perform predictive maintenance Executive PowerPoint Deck',
    "description": 'Builds a read-only executive PowerPoint deck on predictive maintenance status from Dynamics 365 F&SCM ERP data for a given legal entity, with KPI, trend, red-flag, action, and appendix slides plus speaker notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'acquire_to_dispose', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-perform-predictive-maintenance',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-perform-predictive-maintenance',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'fd681fa875f95cce',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/perform-asset-maintenance/perform-predictive-maintenance'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/ppt-exec-perform-predictive-maintenance', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'comparison_period': 'Prior period to compare against for the trend chart.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to pull ERP data from, e.g. USMF.', 'output_filename': 'Name of the .pptx file to produce, e.g. ppt-exec-perform-predictive-maintenance-2026-05-24.pptx.', 'review_length': 'Length/format of the review the deck must fit, e.g. a 15-minute monthly review.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Cuts deck prep time from hours to minutes for perform predictive maintenance reviews while ensuring the numbers in the slides match D365 to the cent.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build an executive PowerPoint deck on perform predictive maintenance for a 15-minute monthly review. Produce 'ppt-exec-perform-predictive-maintenance-2026-05-24.pptx' with: (1) title slide, (2) headline KPIs, (3) trend chart vs prior period, (4) top issues / red flags, (5) recommended actions, (6) appendix - data sources and methodology. Include speaker-notes on each slide with talking points. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-25', 'what_it_does': 'Reads perform predictive maintenance data and produces a 6-8 slide PowerPoint suitable for an executive review.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only executive PowerPoint deck on predictive maintenance status from Dynamics 365 F&SCM ERP data for a given legal entity, with KPI, trend, red-flag, action, and appendix slides plus speaker notes.', 'example_request': 'Build a 15-minute exec PowerPoint on predictive maintenance for legal entity USMF from D365 ERP data.', 'inputs': [{'description': 'Dynamics 365 legal entity to pull ERP data from, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-perform-predictive-maintenance-2026-05-24.pptx.', 'name': 'output_filename'}, {'description': 'Length/format of the review the deck must fit, e.g. a 15-minute monthly review.', 'name': 'review_length'}, {'description': 'Prior period to compare against for the trend chart.', 'name': 'comparison_period'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user needs an executive-ready predictive maintenance deck for a monthly review, sourced from Dynamics 365 ERP data without modifying it.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class PptExecPerformPredictiveMaintenance(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecPerformPredictiveMaintenance'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'comparison_period': {'description': 'Prior period to compare against for the trend chart.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to pull ERP data from, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-perform-predictive-maintenance-2026-05-24.pptx.', 'type': 'string'}, 'review_length': {'description': 'Length/format of the review the deck must fit, e.g. a 15-minute monthly review.', 'type': 'string'}},
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
    print(PptExecPerformPredictiveMaintenance().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916efPaVtbmV2F+b9UkeWUbLUhCnuqqAQFaAEloQyhOOdr3fUPK5LvPFeAl3e53uqfmryGxAenec8/6POdY/PFmdW1Y1G8f3xTPyheMlaZR6NULK3cXdDEUdQLeisQGfxZOkbd1ZHdtUTdv795cr3HqqGyjIgfbt12Uus3CWtSe5b4v8nRceHfP6dqo9xZSMXi1VER5u3A9J1kU+aKsPTdyHnczC9zwcit3vEXTWm3XLPy6yBa7MbeyyGkWGIEvDv9doc+LvSwtXKu1Fn4BdFwEYHu+SL3AShde3kbt+G4xRG24OErcu0Vbe7n7DijkvvdTK3i3sJxZ2XcP46yyBHej+6JJI2DJokzBsU3pWQmwPi9ar/kAbPTuVlamXvP28dff3r1F4PPbxz/enNRqwKU3qWz3wEbJq4E6mfTVovM3g4CM1MoDsLgcgaNz8L18LgeXXM9fvL793Hip/27xn/+ZDFYdNL98/JQvXq9Pb/N/cpcv2tBbtIXVtJ67cKzSsqMUmPxhsUkHa2yAoW1X53MMGhCnPPjw3PlNUlEu/jbf+/l5yIfAa3/+9FYAFazZMZ/eflkAt356q7v584dZSvnzLx/SOXo///JNTtPZsee0szCg9YfPr+8vsWDht6WRv/isSHv6dVbtOVHpAeHf2Te/nqq/xL1c8vm5+OeifLf4seTZnr8BfZ+ZaAO5PxYLfAB2vn2IQQb+/DqjLvpnhH7+5Z+JdUKQq2nUtP+S3F+fgkOQ/sBbL5f88u4Rvt8W0Mu2rzL/+bElSJh/xxKw/MtxXx31z2Q/Ivt3otMoB/n/JZY/FPejDdDfFr/+U9v+qw3vFv6nt52XgkKpLTv1Pi7+eKTIrz+53y7+9NufQPT/UYxSdLXzkPA5s/LI95r28+dff2oel3/67defuhJksWdln7s6/ZHMH/n1cc5fPPha9fNf94LztTzJiyFffK2hxR9F+d/qPz8sdAvgyrfrzcfF95U4v6DFbMSXQ58u+K4aG6Drd3785e1PAEA5sKZ7oNiMP//xH4tz5NRFU/jtQnGKrl2AALdR5s3Kq2HULMD/M2rUHvBrEwHHvtaB/J8jPGtc+Ivf/6fzwPr3zgvrl2XZfp7x+2sxfsPrz9/h9e8fFioQX9RREOUAhOWNJH3KrQCA8Xw02NR4dQ/gyh5b7z0Q9H7+sIjyxe//4gmfH8I+lOPvD9iOnigo09yMgE2Xeh9mW68h4IGnZQ6gsSfzeIu0cIBSfgQQfOaBpkgB3bSzX5okStOFGwGMAXQ2PmQD332chf3++++21YSf8idkY4snzzVLsOCrOov374HCfhoFYfsp95ywWPz0x58/Lf7X4r/a9RA+nyEBBnlFBmjIK6KwAJXWZWAZCBoIM4CRR2T++PPlYyAmB9QE4hj5kffcDDI18dwvDlfYzXsUJxa2B/wJnJyVRd0CHlhE7YcF5y++6gsOnW/NTBEWzczJMxd6uTMCqRYw56snAREuGpCOjQ+YtWu8x6m/27X1UDEDJW+1vy/OtAR4qUjBX7Oaj0Vgc5FHwP1f0+F5HQipf2oW2y8iPiyEOTcXpVVbZVhbrzN86xmXmeZf24Fwa5F7w6d85mFvdtWjUJ7uAYuAZ5xXSN/PMQcNSwZQwW2+nP1YY83sqT5YtP6UN68isOo5FA4gBXBo0EXunHv/45VSTVh0qfvwH9B0lvSKgvuKyiMHX23AP+ts9j/qhnZzN/SpQ2Fktfj/sIOa3bJhGHnPbNT9brEXVPn2DNfcS85hfbaf4NiHPo/S/NbZfEGvLyD+KU8jkHv1+D+eKx9Bfq15AmMHVAUgJD/kA6cATWa5jwKYE7qu59KxPuVf2AKYsnhAI3AoQAtQTXMSfzlwvvtF0xBAwvz9W+fwSJjanZ0BknxRdnYKEtD3PNe2QIjacA7kl+iCavDmgh7CyAn/YtXsd5B0QP4c1QiUJWCUD18R/Hn3i+p/2fhskOYtj+axAzVcPwQAPbxZwTlMczSBeu2zdQd2fnwIAWZkZTvbboMqApY+L3q1V3VRE7UzYj796pUAtN/P709L56vevQSFA5wFyqPsgHcfBTVjTQbaH6ADyFJQX1mUg3YAOOXlhIdAK5vRAaDvq199SnxcfhnkPapw5rEvG2dD5j1za/BMbSsfvwcR9UdpAuTNlfH02t9n2tfTZtkzkDYADMGJX+4+e4gPzzbg2Wcsvsj9+A+z0c//3vj0IHbtrwnwcRG2bdl8XC6fZPyFiz8AGFs+dW1mXn4/o8L7F2u+/4YC779Dgb+If1r+cfHvqfgXEa8S+bhAPsAf4PnW6ZVirxfwCP1+e3u/mu9+ymXvG9aC44sM5NgcvxE0Al+J8csSwI5BDRAILH4SZTPz6wAo/cEMIBif8u9zfq45QDx5MOdoU3yHBY8OAeT/M3ZfCQzcyltwtjt3l4E3D3aPCmm8t495l6bv3gBMev/yQDdTVTandzMPg6CQQCzayHt8A7ECt6OmyOe+Jirc+eJfJ2UJXK4Xz7sz2Dy3AOWDRzZ/TcAH+M6G1u2scTuWs4rP0W5uBh/AdG//8QDx8cFKPwB6ASCYNt9n+4vLZi7/riifXgXedIAx72aCAFgD9ABene2cC9pqQIUA3X6oy4NAPj8J5B8V+gsNfc81s/klCMB3rARq+93C+xB8WGjK+fDDw762yP940hX0I7NQt/g4U/O7F8yBdzDWvFt8nVCAia+Z8THl5x0Yx3+dp6M5vI8t8wewB7x93fT13zxs7+23H+n1wMLPcyY+8+nvtRNmjAMcMHv8A6jk+zNrZyfUhds53svyf7HI36MwSryH8ffo6iHth84CnX/kDZ+BSkEb/qNKp8f15XwK8NxLt+eex8dHs5F1c1pG7Us9a4Hg7wG0zx12BpIwTMfXlh9o8FABUAqwYHbxt9h982DxGDZnZYHH2+e/jfzxBirMmlPiVWOvaQUsBwj8vpn7siUAI3Ag+P6EDXDv/3aOeYlpQgs00EDOirRhwltb1NojPAtxkdXa9SzfXzkuuoIJB3dIwiUIf7X2bMfHXWeFwPbaIhCS9AgMIYG8JwZ9nnvQaFYNp0gfpijUXyEo7Lqej65cd02sgTAShS3KtnAbpyz729Ykyt2XvU/7Zmd+Halmv7zM/uPNJlZgJbtquM3zRS8pBFwk7XtoQDXh3Zpkkwoyn4okY4+5JnuY4zIcqoauy++vw8FLFJFnbmXSHVJkzUeBiu9zcivBHeQwJr+L2tIVcQ+l5TvHZb6Y7zKDRO4ZkjPOYOVHPcnQwzXLgnbTD0mTtvHxTN+NE3rwI/yEjQqGE1k6luRO3R4xpllu+juJLSGFHIphjLlQVsyk2cORJboaC6ubsrrcOec6XlozPaU300mvrEhF3QWjDHYi8NNhBd28qaCA/DNa0swl3MoxUKE9x/A1QWJOOUYkfYsdWUeZ+95Yk76qyTLoLW+bIxN0SZV0HZ8cgj7y9+YWPmZHl2BIWPPCG3uU5TJE1bu+TviUS1bH1O52g3/ue+w+rTtjakefXXVq3aIQ5K4NO5Z56NIN10tpH/gmG46soNpn3oF2R32c6MhchvqNpU282+7swJW78z1p867aEiStHPTd+biDozu/jmJfwqYtrmzkZi9kg3O+1ptCmU4bxXZqWnfsUPFuhzbadzruRnK0PS03tXgqD4SIpebazhSocKkyTQfrfPWPKnncbHfsZo1xZmjjt6OsNbwtq/Y+YmtBW0WmzukdX+2XlY3kOIe1mWjxZ3QYOF+fDnuqNNGSonTp5GU3Txt0Vd7KVscfRWFjqoN7osMoNuWdGE5c0cS0qSVVNp2F9YkSaKqGtfAWtlXgV8lEXTkTp3ldiHd3XUyxruxV/kooLJGj1XLD00pTRCeF1dpVfo6mrTcsB3oVeNerFTbM+hayfbf2xlvWUvQqpvlhF2IHyNpCgI+jQdiKAc0eklW4ZCLIgHc7u7ndsVWiMentGNaqFdbpdXPIs22aGkbdVXrEXrR76OEgqW+1Udk8amTHdehFOwk6RlXlYIxm0Ia5VQklGg3oQJwn/irdeT84CffNWvMGkbOFcFBcUwpswaYaK1+1gmapuL+zJ8/ie7xOoaZESrkXzCw0Vaenyio+pGgdkwjLYxlZe5R+XzPcGd16Z8FZshff20AD3/XxPjOXIy0UUHYiCc9feUYQ60UN8UGSrHfKKN8y+VrbkaeLOLu6lokGVStz5dSYGOy4W3yELheIyMQpOBiZACJ/2gj5djwZ63g16abJ4zc2WdrcVTKOhejeuQ0Y3gTdYHblRjrxSEqnmynwvAOZEvgKNFN5vbli9OjDgn2+mvTo7MIENXM5Rcn9BAN0yIa2Dw9IQcFwsSy3ouSKnJkbkaDG9xMPC7s7HKkKCx89A7eky5KWOCyZqv4KuVGhuYJ6bcusdqmAPaZoFaGO0KehkJLCCboQd2iabnLA8ta9xSGdv0vBKufisGkGWZA4x0qQtS9wU2zG60mJ/D5pfI9PyhoO1lpmKUesPDZNh+5pq+mligr7vb0u9nIRAI6PylM49Lv0trwTo2rDNtGIqmFIuKWsqoMRcjW2q5ujTuyPFegIsTI/SrLuw93q2uro5SYyS5pmYUzKaJJF0ZTNC2t04UnY+RF1Jpo6j/JLSqLbfl1jAXtfnWMzSxi8N+O9PiFHtRkxgbugK+4KILZWGUe4ZvSBkEEED9Cm3Qyxagi8mfQow2yx8No6qQ07E9MbiGZeuCHz+jVyFK65R/gHTzlCDOs7LllAtXTaxuIEx+M4RoHtbNoJLZMCMmToauEtrE5GW2InDN6urTOWak3DnIZ2cO+38lArurHClpJXDffJGJfcbh/L5TkMBbN0vCG4+JWwc3C9HnRLjBvlRA7adW8Jaw5gABQfL8oBvmnEuDarcQoVOeCwniIqtD7DtCrSGV/uu5OJRzbF+MpkBMW4zkw18g+VLKb9VRe0A88x/H6nXTaJe+dNS+Yu0e4yEhNxMB13W0qX44WpDth1rdAZc8CEa4fvqk20L2BNyi9an1gV7p70XBOxQ2OjfOO2oOrbYlTw2wRLUl8hLssjqJOHu8rcxONhc2bdO7JPmUJf52uVdwuKjsdUUfhQX1Gw7yQ7P75qrH29hAFSHNQJXwJE9JdQficaSFq6xWpSlHybVR5k4wE9HIeLbe034i4rb/dR9jdWnVqhAdsHO479O8RxVlW38CAYjCQVALlzePCkErQX8CpsAWGx+6PmXpmLHLu3cEcsB2+o13nIQ8Ryu0mc02kfhbDCs4eQMwEMjDV8oodtyu3FeNvpedZOrKCjmxXZrUX/QNzzc2z1UaTvaExhJq+NADVD+s1DmGCrXK9ToctUTK01PTk3oCyGKKZPFt4bl3BpKaRJx0kY0krSe74pMvBRUSmSOLZ8UFkm5e+wqzjwR1aJh33h7NTqZnj3Djt2ZsZd4Wh/F68SrMPwodpGQ4VJZzdXry57iRsO0y9j2gQKb2j7aOzbY69xkaABXEYI5qrjZ1+OUrnQfOUubwDqnY/i/o7zt5TbTPwp0wsYcO4dkdYdVXObKr1qGiuI0UXaWHvnEmpiD5ve6UDwCgCRfmJhThz2nLISuFE9m7Bmhlx206+5qvITvtmhm4TGNfV6oFotieT4vDqHtyHdxs2RpXq6Q9MkMNJ839EWZS1RVUzDiVxNhKdbXOT0037blzejRK/95V5Z9aYUBbr1hFunnVr4vA3Ol9wXHEPOq2tzOlqaslJNsdnTywI2BOKc0sNprYgInF7krq5LNjI3/EFqAkDMqaREWZCB+t/QrXz0tqvqGl4uHIL02no17HXQPpyOpaOK12V1Dk8Fsmm1vQ+NUB3J4cV3QKckHbTBUstAu+81VAyrvo64IEVhojFpKlaHSaRs3VkfRnO9pbeG7ppYG7LVfudbOwIJd/vaQ72ch+0sDqfuVCLb8W4H5Skta04qxM4UtsVk8jembDJapj2r3CR8EQL0P4mpdleQ/hoNAWgA7rK0YjJdghUhT7HhcL/Qqqcx+omlG/dscZ7hxERZ+IZGd8upb8sDVKgHsQKnjvQhHBkqNMPDtjjnXgbaqKQDITd1KSzghtVHtNgxPuDubahuV7TiI3gznUyPgFebfUBt9mmoy5VWT/IyuaGFxAqnKqt3GQut7WYJQeKeXDpJxdir3aRCTt6wNkbxqc0y1wiPj9th1HVOUZf8Fk8c2TGzSmEMtV5D5kqlQNQrJuUUrdJF/3K1WoWLL9vaUA+TdUrgc2rmTlbT9FXlToFWatHK4fkLf7neIooQltroirtCWCHuiqxyg0OUDj3UzE5UmXLLn8jwmJbMKahB54QL8bEJrLGVi2i3R2y4Nfx1wCyVe39J9Pt2I6YFo634BBccPfFLVoXrQTusAzCfHIiTJ8IV6kfSCIeQZYNkuGSXOq117E5SfZWmUXJCR9HdC8Xlbq15X9yCdhU9DRLi6eh2fypEH3LqS8e455wyeThzz5Nr8HfmWtTx0HTtDR8Qf21rJrwSw8xV0WOPHeub3im75kSf6d1hWPuqLUfGVjlsDGaMcjOPNFBlBt/BtdNCtuq1Q7kUioi0T6iuNcEoKs0lMkLRVnI9Tqzz4bCJ0svWJAzXOikM1fdo5B3FSmE5puevZ81WgCpwf3WqgVIkp2c2HKxvFUKRNnwOp4NuYKHlGNSBRO9R3e+HCpFTDNOOpXujZYivDC8gjqftBlcOGGTp2aGrr/656lES3/k5c99d1BudYS6Jdwg5dfYWhbWuMpO95HZk3UPt8VKqmlGs3BhlApm5dFYkMHHjBiA6ymChVVBoN9dXK9TRWkeLDXvYwozP3bbKrQwy0xkiOUHQ4YKgaDyupn2MGOZpae02rrAs7qZwhzHCtspJ3l0gN4WKS56ovNd5R53c++mNqa45mE0aVGZOOWe2lgBlOnyxy5PixpxbrNUxK8qJ82rW90dL2XfeKYfNUiK26V276ZZBcWEMn5F2m2x5q+Y9eVWTcqV0rBmyeamrx5XULnlZKXlrt78Qa3haOra/Fcu1rtw3sj4wlUdZ1rZubEPdUxtq5CFut42Rjb+5kUfaYLWNmWnG8XzpEvmoegOcqzYbMGaX4kjf3PtrXG4mx/bQLWlWmpYnUnf1Lo0obk/3PHHxpLVwBoD6VrL8TCU8l7ngNxtn9BuxO1/PQJpOFav4xPE5vcZv9EEHRH5OSPVcriCWujZ0bu07wIseJdEYWjQZy/u2cOC8AaQVmo/h3vFomqqK3vF3oC5QCt6dydNt9IybielX5uBZhCziHDS62R7RjrBWKh1HdrUk1Pg20M8UuLKC/HzqqYY3+3IqqQijGiTN2oZfHrGQPm9oREfE9o4wXZ4MflKYUwOfk4qi1mlp3cwAYb1155Seu+y4A3FxT2rebrT72d4HBMus0XLHNeZxvOQevbR3l4FnWAtVFb7tc5MhPVNqGF0O7v5K2HI0ZEjjTl2PR1w41Jqg2bkkVPsw0mNxKCIiWxZmI5fXlsbzKbGkI4xQZCljx7C88kEXiudVceRJrhSJDN2KMGhq7fZUKmS61tvaJuudxWBmfcMCiSqs3QVDJQIxjXJXdrWXSmi1JkvCQBMPxyHoGomkgJzayrROWD11ZyIhViN+RHflsqAEGfy1C0NW7dSlzIChp2pg0e2WrlFNq1usK+2egsnbGq9oN4N0g6w3pMdk2lKCsANTm+srgbg0hglQeRiM40U95mu85J2x2p8zYGt/2wlZZ+2mOimomETP5oFdtWTqg7R2ajCU3FoyhwRLaNMVYbPleijd9SZH7SvTrfF6su/l5hjv1wJ7szUGfCtQkYPZspEoEltS+yV1CfdaebVzCDKW92ngx/1KPmPLOlIyu8Y2PLwpL6fWkq7DObjfEEYVzXsAhy5lnFk/iVU414g+o5o2YM+FbSl8dw+gTZPcuZsaxwdMMafCagnrcJyQqa/cyFeRc39HYLa+RQfQZmrH2Esh1rkVxO4UMxk2bR3RgPg9xoCkz1ziNK64i8BzuJz72JUAL8cKTyzhaALLHXPMDc6Ms6F4JluP5SaQtlIeTWSZDQRpZ2siwsCQvVMbVBVkAg19QA1Qvge53tcyim2RWFVoc08f8TO7s/H7XcdMoqe17NJUKJJXe1mDJcDLoLyRGowqhz7dId2+OIQtuUGLlYe6hGR0mnoSxUsgL0vUEHJOXcn42LIR0zcRf02U/dW6M/xwk4oy91aMaZmbgnHOMBhSDfYgVBYRMlB12sKD29yMacT3961DcGDGjQpbD0lO6bss5VmhFqV8h/J0UOO4oqh7qULVJWD+tScZvKtjULg/nc/JVR0IrbVIDRmiboL3x85Ob44zidjQiJFF90IvIhddIVuz2qZLMp4wQhsl+h5SFCOVZDo095Pe4+LdPlUmKxbdwTZVZLI8Kt75000n2144OMqhbjKoC06mVCP1GOZWoKyKoRMH6byUuzWDeXtEN4KlLAHEUHSHkp26s9WOBdjimdrOGfD8msV4Spd5RrtnUjftRFVz7oqVTjCYPLY+h6PbDiPlt2mMh9pGs5Dd0vHw9ircNlIWQ/BZuVeiNbLBujsLMpUYyDEgLrqYV4pFDTuj21iqA7qHHYDrvK1IcvLKksqg/uq5Wmq0gCqXYF5HK8NZeZ20Ms7+CccKnJRoK5zuN2fvc9S1xSLf6ewrkreUAE+O7xgWdlgZ+jG/6Ma9OpGt66WTCyMjEShYss9xNtvw9SCcEwF1YCTHGqPqLXk1EIZ9FnvtTAQQjJM4fkupNYlQmoSnrI6YhbRb8jqYmQ6VUsTEkCq9vfNiO9a5baQvM5PF/DY7gBL2bnu5oYly1yQYd5dLDDZuW4htMOGg0eJZAlnmuj6RhEdWZMUU3YZLZFRC5SqjpzL3k/3Fp3OUlbtiumsAPoTy4NrycQ1G8xEmwiZOi1oVLYmK6mzX2x5bF1vtsKxzriHBYIswEU1ay+0OczUvFmBJxiqt8xB65TiIT97u/V1orzjrY+LJaOIDmhIX32IbU+Ez7FqoQnSLrqv+Kth6y491tm7cIxrrV2SKqajAlesg19j5DMZUNW1A/W3bJjvfMfjEDS4GJaO9pi5TD9p8PK9YtORvBgNoTN2PdCSc+MBXjbHHbMWD0BuTtIjThL3K0tZWPF0ofjCycDiKkRBzSLTd2R1oLVOHn9YNcbnd0Qu6DmM9tiBEzSmSslVJCSeVXa+BSpRokPoISx12a/aNdPC1zNQFqNuMu8v9iLNeBJCUVmAwHu8iskf7/LRUu4tNaTLp+uTApL50XTu+14K5TSxcuB0hzCnJ/DBa+uCJJ6/OO82FWgWqps5oCio0XJNbR0SJjvkVjBnr4CI4p6kwGAR0u4OH0aex6G/L8zZpPXw7oq2f2Jm/Yp0kUpDzZmXwOYd2DsVmeWwbJkwN1fp8czloc7kSeAxvkqvoXWhxjCmhOWw4t9vpZJOQRounF/94QxQpUyNQVgCaRRyvptqt0Y0fxWVzaM7ubRkN8A6JQx26JjolLhlQ65NzQ6tK7dtsFWKEhaB1d+6MfpIMYGBj3NsBQkuGXHGs45+hgEmymKwQwxhkDTtoAoEdXPMEnQqp60tBZnaqtLr6rXH2OrPANtkawFKa4SgZX13shG8KctWj6Q0QyJln+OVSFADT2qKw6r2K4mHBw49kf6rq1Xg4SMUquK2x453bXwTwNpUCvNUugy6421MiGx4zXNrSlU1UcAkUTrYS61yXR3PkC3FkEK1lt8ubNAaKqsQNQeEbMpWNHobCbrJvcg3lPhUt9aS4+Su8xO8l0jvKUhi0U3aAm71VY04fUHMDA9rdfF+HdsVZmrsxLivhsGyRyccicrlmpADjWDU6whQVXZC1t1yjMH7P0rUJGXGHTyTKNnoSyqeleYag+2q9XTYW1Wdhct5sNn/729u7t28PAd/+3R+6zQ+A/p89h3o+Mvryi5XHQ07Pcj8+zvr4b2v227u32omAXs8nb03aBa8HVH/33O39v/gIcxYyPn9J9uVp9vOBfGsF84+u36Lc7Zq2Hj83Rfr49QrYYXfN/AvNZv4RrwPe//LM9mUS+Gg5j8eOn9visxs1ZdHMp80n1xlQxWq/fA1eDyTfvbmv59SfMQL/7NXlbO/rlw/ATOwD/AF7+/N/A9sUSz8zLwAA -->
