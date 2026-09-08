---
name: "rar-cowork-cookbook-ppt-exec-monitor-regulatory-compliance"
description: "Builds a read-only executive PowerPoint deck on regulatory compliance status from Dynamics 365 ERP data for a legal entity, with KPI, trend, red-flag, action, and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_monitor_regulatory_compliance", "rar_sha256": "8b0ec5e9e60edae287f89dc5bacabecb5071f45e11ed9964788470961eb3698f", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_monitor_regulatory_compliance`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_monitor_regulatory_compliance_agent.py` and in the RCI capsule.

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

Monitor regulatory compliance Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on regulatory compliance status from Dynamics 365 ERP data for a legal entity, with KPI, trend, red-flag, action, and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-monitor-regulatory-compliance
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
      "description": "Name of the .pptx file to produce, e.g. ppt-exec-monitor-regulatory-compliance-2026-05-24.pptx.",
      "type": "string"
    },
    "review_period": {
      "description": "Reporting period and comparison prior period for the trend chart, e.g. current month vs prior month.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_monitor_regulatory_compliance_agent.py` and embedded as the fenced Python below (sha256 8b0ec5e9e60edae2…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_monitor_regulatory_compliance_agent.py` first:

```bash
python3 ppt_exec_monitor_regulatory_compliance_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_monitor_regulatory_compliance_agent.py   # or on stdin
python3 ppt_exec_monitor_regulatory_compliance_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Monitor regulatory compliance Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on regulatory compliance status from Dynamics 365 ERP data for a legal entity, with KPI, trend, red-flag, action, and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-monitor-regulatory-compliance
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_monitor_regulatory_compliance',
    "version": '3.0.3',
    "display_name": 'Monitor regulatory compliance Executive PowerPoint Deck',
    "description": 'Builds a read-only executive PowerPoint deck on regulatory compliance status from Dynamics 365 ERP data for a legal entity, with KPI, trend, red-flag, action, and appendix slides plus speaker notes.',
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
        "upstream_slug": 'ppt-exec-monitor-regulatory-compliance',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-monitor-regulatory-compliance',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '86631eb3b6cba168',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/analyze-financial-performance/monitor-regulatory-compliance'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/ppt-exec-monitor-regulatory-compliance', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to report on, e.g. USMF.', 'output_filename': 'Name of the .pptx file to produce, e.g. ppt-exec-monitor-regulatory-compliance-2026-05-24.pptx.', 'review_period': 'Reporting period and comparison prior period for the trend chart, e.g. current month vs prior month.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Cuts deck prep time from hours to minutes for monitor regulatory compliance reviews while ensuring the numbers in the slides match D365 to the cent.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build an executive PowerPoint deck on monitor regulatory compliance for a 15-minute monthly review. Produce 'ppt-exec-monitor-regulatory-compliance-2026-05-24.pptx' with: (1) title slide, (2) headline KPIs, (3) trend chart vs prior period, (4) top issues / red flags, (5) recommended actions, (6) appendix - data sources and methodology. Include speaker-notes on each slide with talking points. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-25', 'what_it_does': 'Reads monitor regulatory compliance data and produces a 6-8 slide PowerPoint suitable for an executive review.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only executive PowerPoint deck on regulatory compliance status from Dynamics 365 ERP data for a legal entity, with KPI, trend, red-flag, action, and appendix slides plus speaker notes.', 'example_request': 'Build the monthly exec compliance deck for USMF as ppt-exec-monitor-regulatory-compliance-2026-05-24.pptx.', 'inputs': [{'description': 'Dynamics 365 legal entity to report on, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-monitor-regulatory-compliance-2026-05-24.pptx.', 'name': 'output_filename'}, {'description': 'Reporting period and comparison prior period for the trend chart, e.g. current month vs prior month.', 'name': 'review_period'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user needs an executive-ready compliance review deck for a monthly 15-minute review, sourced from Dynamics 365 F&SCM without modifying data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class PptExecMonitorRegulatoryCompliance(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecMonitorRegulatoryCompliance'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to report on, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-monitor-regulatory-compliance-2026-05-24.pptx.', 'type': 'string'}, 'review_period': {'description': 'Reporting period and comparison prior period for the trend chart, e.g. current month vs prior month.', 'type': 'string'}},
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
    print(PptExecMonitorRegulatoryCompliance().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
