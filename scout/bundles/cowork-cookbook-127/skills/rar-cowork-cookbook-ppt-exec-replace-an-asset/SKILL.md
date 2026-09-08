---
name: "rar-cowork-cookbook-ppt-exec-replace-an-asset"
description: "Builds a read-only executive PowerPoint deck on asset replacement status from Dynamics 365 F&SCM data (title, KPIs, trend chart, red flags, actions, appendix) with speaker notes; call it to prep a monthly review."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_replace_an_asset", "rar_sha256": "8635c7553c7517298ef4d5599f9c144797df53180270afdbc3ad75f3d4a01c04", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_replace_an_asset`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_replace_an_asset_agent.py` and in the RCI capsule.

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

Replace an asset Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on asset replacement status from Dynamics 365 F&SCM data (title, KPIs, trend chart, red flags, actions, appendix) with speaker notes; call it to prep a monthly review.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-replace-an-asset
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
      "description": "D365 legal entity to report on (e.g. USMF).",
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
      "description": "Target .pptx filename, e.g. ppt-exec-replace-an-asset-2026-05-24.pptx.",
      "type": "string"
    },
    "review_period": {
      "description": "Reporting period and prior period used for the trend comparison (e.g. monthly).",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_replace_an_asset_agent.py` and embedded as the fenced Python below (sha256 8635c7553c751729…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_replace_an_asset_agent.py` first:

```bash
python3 ppt_exec_replace_an_asset_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_replace_an_asset_agent.py   # or on stdin
python3 ppt_exec_replace_an_asset_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Replace an asset Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on asset replacement status from Dynamics 365 F&SCM data (title, KPIs, trend chart, red flags, actions, appendix) with speaker notes; call it to prep a monthly review.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-replace-an-asset
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_replace_an_asset',
    "version": '3.0.3',
    "display_name": 'Replace an asset Executive PowerPoint Deck',
    "description": 'Builds a read-only executive PowerPoint deck on asset replacement status from Dynamics 365 F&SCM data (title, KPIs, trend chart, red flags, actions, appendix) with speaker notes; call it to prep a monthly review.',
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
        "upstream_slug": 'ppt-exec-replace-an-asset',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-replace-an-asset',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'f02f09edd3ee2069',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/dispose-of-assets/replace-an-asset'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/ppt-exec-replace-an-asset', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report on (e.g. USMF).', 'output_filename': 'Target .pptx filename, e.g. ppt-exec-replace-an-asset-2026-05-24.pptx.', 'review_period': 'Reporting period and prior period used for the trend comparison (e.g. monthly).'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Cuts deck prep time from hours to minutes for replace an asset reviews while ensuring the numbers in the slides match D365 to the cent.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build an executive PowerPoint deck on replace an asset for a 15-minute monthly review. Produce 'ppt-exec-replace-an-asset-2026-05-24.pptx' with: (1) title slide, (2) headline KPIs, (3) trend chart vs prior period, (4) top issues / red flags, (5) recommended actions, (6) appendix - data sources and methodology. Include speaker-notes on each slide with talking points. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-25', 'what_it_does': 'Reads replace an asset data and produces a 6-8 slide PowerPoint suitable for an executive review.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only executive PowerPoint deck on asset replacement status from Dynamics 365 F&SCM data (title, KPIs, trend chart, red flags, actions, appendix) with speaker notes; call it to prep a monthly review.', 'example_request': "Build the executive PowerPoint deck on replace an asset for USMF for this month's 15-minute review.", 'inputs': [{'description': 'D365 legal entity to report on (e.g. USMF).', 'name': 'legal_entity'}, {'description': 'Target .pptx filename, e.g. ppt-exec-replace-an-asset-2026-05-24.pptx.', 'name': 'output_filename'}, {'description': 'Reporting period and prior period used for the trend comparison (e.g. monthly).', 'name': 'review_period'}], 'model': 'claude-opus-5', 'when_to_use': 'When you need an executive-ready asset replacement deck for a 15-minute monthly review, sourced from D365 ERP without modifying any data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class PptExecReplaceAnAsset(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecReplaceAnAsset'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report on (e.g. USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Target .pptx filename, e.g. ppt-exec-replace-an-asset-2026-05-24.pptx.', 'type': 'string'}, 'review_period': {'description': 'Reporting period and prior period used for the trend comparison (e.g. monthly).', 'type': 'string'}},
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
    print(PptExecReplaceAnAsset().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
