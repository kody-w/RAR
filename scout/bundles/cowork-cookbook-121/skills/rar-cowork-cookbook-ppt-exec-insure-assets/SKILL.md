---
name: "rar-cowork-cookbook-ppt-exec-insure-assets"
description: "Builds a read-only executive PowerPoint deck on insure assets status from Dynamics 365 ERP data for a legal entity, with title, KPI, trend, red-flag, actions, and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_insure_assets", "rar_sha256": "26181d2d5366c6ab147e1d59b1b9e424c55ea57dd15d97aa38104dba70bba5f9", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_insure_assets`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_insure_assets_agent.py` and in the RCI capsule.

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

Insure assets Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on insure assets status from Dynamics 365 ERP data for a legal entity, with title, KPI, trend, red-flag, actions, and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-insure-assets
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
      "description": "Dynamics 365 legal entity to pull insure assets data from (e.g. USMF).",
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
      "description": "Name of the .pptx file to produce, e.g. ppt-exec-insure-assets-2026-05-24.pptx.",
      "type": "string"
    },
    "review_length": {
      "description": "Length/format of the meeting the deck is sized for, e.g. a 15-minute monthly review.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_insure_assets_agent.py` and embedded as the fenced Python below (sha256 26181d2d5366c6ab…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_insure_assets_agent.py` first:

```bash
python3 ppt_exec_insure_assets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_insure_assets_agent.py   # or on stdin
python3 ppt_exec_insure_assets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Insure assets Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on insure assets status from Dynamics 365 ERP data for a legal entity, with title, KPI, trend, red-flag, actions, and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-insure-assets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_insure_assets',
    "version": '3.0.3',
    "display_name": 'Insure assets Executive PowerPoint Deck',
    "description": 'Builds a read-only executive PowerPoint deck on insure assets status from Dynamics 365 ERP data for a legal entity, with title, KPI, trend, red-flag, actions, and appendix slides plus speaker notes.',
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
        "upstream_slug": 'ppt-exec-insure-assets',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-insure-assets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '64dcb354cfe0eff9',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/manage-active-assets/insure-assets'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/ppt-exec-insure-assets', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'comparison_period': 'Prior period to compare against for the trend chart.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to pull insure assets data from (e.g. USMF).', 'output_filename': 'Name of the .pptx file to produce, e.g. ppt-exec-insure-assets-2026-05-24.pptx.', 'review_length': 'Length/format of the meeting the deck is sized for, e.g. a 15-minute monthly review.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Cuts deck prep time from hours to minutes for insure assets reviews while ensuring the numbers in the slides match D365 to the cent.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build an executive PowerPoint deck on insure assets for a 15-minute monthly review. Produce 'ppt-exec-insure-assets-2026-05-24.pptx' with: (1) title slide, (2) headline KPIs, (3) trend chart vs prior period, (4) top issues / red flags, (5) recommended actions, (6) appendix - data sources and methodology. Include speaker-notes on each slide with talking points. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-25', 'what_it_does': 'Reads insure assets data and produces a 6-8 slide PowerPoint suitable for an executive review.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only executive PowerPoint deck on insure assets status from Dynamics 365 ERP data for a legal entity, with title, KPI, trend, red-flag, actions, and appendix slides plus speaker notes.', 'example_request': 'Build an executive insure assets PowerPoint from D365 USMF for our 15-minute monthly review.', 'inputs': [{'description': 'Dynamics 365 legal entity to pull insure assets data from (e.g. USMF).', 'name': 'legal_entity'}, {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-insure-assets-2026-05-24.pptx.', 'name': 'output_filename'}, {'description': 'Length/format of the meeting the deck is sized for, e.g. a 15-minute monthly review.', 'name': 'review_length'}, {'description': 'Prior period to compare against for the trend chart.', 'name': 'comparison_period'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user needs an executive-ready insure assets deck from D365 F&SCM for a short monthly review, without modifying any data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class PptExecInsureAssets(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecInsureAssets'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'comparison_period': {'description': 'Prior period to compare against for the trend chart.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to pull insure assets data from (e.g. USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-insure-assets-2026-05-24.pptx.', 'type': 'string'}, 'review_length': {'description': 'Length/format of the meeting the deck is sized for, e.g. a 15-minute monthly review.', 'type': 'string'}},
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
    print(PptExecInsureAssets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
