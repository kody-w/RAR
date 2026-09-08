---
name: "rar-cowork-cookbook-ppt-exec-monitor-regulatory-compliance"
description: "Builds a read-only executive PowerPoint deck on regulatory compliance status from Dynamics 365 ERP data for a legal entity, with KPI, trend, red-flag, action, and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_monitor_regulatory_compliance", "rar_sha256": "8b0ec5e9e60edae287f89dc5bacabecb5071f45e11ed9964788470961eb3698f", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
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
