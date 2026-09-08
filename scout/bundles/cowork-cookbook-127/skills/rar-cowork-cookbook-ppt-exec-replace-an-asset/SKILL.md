---
name: "rar-cowork-cookbook-ppt-exec-replace-an-asset"
description: "Builds a read-only executive PowerPoint deck on asset replacement status from Dynamics 365 F&SCM data (title, KPIs, trend chart, red flags, actions, appendix) with speaker notes; call it to prep a monthly review."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_replace_an_asset", "rar_sha256": "8635c7553c7517298ef4d5599f9c144797df53180270afdbc3ad75f3d4a01c04", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
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
