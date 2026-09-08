---
name: "rar-cowork-cookbook-ppt-exec-monitor-asset-performance"
description: "Builds a read-only executive PowerPoint deck on monitor asset performance from Dynamics 365 F&SCM data for a given legal entity, with title, KPI, trend, red-flag, actions, and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_monitor_asset_performance", "rar_sha256": "dfb9b5dbbfe663682b61aee11bf37632eaa2e318b24325f4a4caf06b29109ea0", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_monitor_asset_performance`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_monitor_asset_performance_agent.py` and in the RCI capsule.

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

Monitor asset performance Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on monitor asset performance from Dynamics 365 F&SCM data for a given legal entity, with title, KPI, trend, red-flag, actions, and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-monitor-asset-performance
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
      "description": "D365 legal entity to pull data from (e.g. USMF).",
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
      "description": "Name of the .pptx file to produce, e.g. ppt-exec-monitor-asset-performance-2026-05-24.pptx.",
      "type": "string"
    },
    "review_period": {
      "description": "Reporting period and prior period to compare the trend chart against.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_monitor_asset_performance_agent.py` and embedded as the fenced Python below (sha256 dfb9b5dbbfe66368…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_monitor_asset_performance_agent.py` first:

```bash
python3 ppt_exec_monitor_asset_performance_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_monitor_asset_performance_agent.py   # or on stdin
python3 ppt_exec_monitor_asset_performance_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Monitor asset performance Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on monitor asset performance from Dynamics 365 F&SCM data for a given legal entity, with title, KPI, trend, red-flag, actions, and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-monitor-asset-performance
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_monitor_asset_performance',
    "version": '3.0.3',
    "display_name": 'Monitor asset performance Executive PowerPoint Deck',
    "description": 'Builds a read-only executive PowerPoint deck on monitor asset performance from Dynamics 365 F&SCM data for a given legal entity, with title, KPI, trend, red-flag, actions, and appendix slides plus speaker notes.',
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
        "upstream_slug": 'ppt-exec-monitor-asset-performance',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-monitor-asset-performance',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'f639c30c1c80af15',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/analyze-assets/monitor-asset-performance'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/ppt-exec-monitor-asset-performance', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to pull data from (e.g. USMF).', 'output_filename': 'Name of the .pptx file to produce, e.g. ppt-exec-monitor-asset-performance-2026-05-24.pptx.', 'review_period': 'Reporting period and prior period to compare the trend chart against.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Cuts deck prep time from hours to minutes for monitor asset performance reviews while ensuring the numbers in the slides match D365 to the cent.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build an executive PowerPoint deck on monitor asset performance for a 15-minute monthly review. Produce 'ppt-exec-monitor-asset-performance-2026-05-24.pptx' with: (1) title slide, (2) headline KPIs, (3) trend chart vs prior period, (4) top issues / red flags, (5) recommended actions, (6) appendix - data sources and methodology. Include speaker-notes on each slide with talking points. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-25', 'what_it_does': 'Reads monitor asset performance data and produces a 6-8 slide PowerPoint suitable for an executive review.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only executive PowerPoint deck on monitor asset performance from Dynamics 365 F&SCM data for a given legal entity, with title, KPI, trend, red-flag, actions, and appendix slides plus speaker notes.', 'example_request': "Build the executive monitor asset performance deck for USMF for this month's 15-minute review.", 'inputs': [{'description': 'D365 legal entity to pull data from (e.g. USMF).', 'name': 'legal_entity'}, {'description': 'Reporting period and prior period to compare the trend chart against.', 'name': 'review_period'}, {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-monitor-asset-performance-2026-05-24.pptx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user needs a monthly 15-minute executive review deck on monitor asset performance sourced from Dynamics 365 ERP, without changing any data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class PptExecMonitorAssetPerformance(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecMonitorAssetPerformance'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to pull data from (e.g. USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-monitor-asset-performance-2026-05-24.pptx.', 'type': 'string'}, 'review_period': {'description': 'Reporting period and prior period to compare the trend chart against.', 'type': 'string'}},
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
    print(PptExecMonitorAssetPerformance().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
