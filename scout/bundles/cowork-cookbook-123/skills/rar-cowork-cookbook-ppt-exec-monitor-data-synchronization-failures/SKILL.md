---
name: "rar-cowork-cookbook-ppt-exec-monitor-data-synchronization-failures"
description: "Builds a read-only executive PowerPoint deck on data synchronization failures from Dynamics 365 F&SCM ERP data, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_monitor_data_synchronization_failures", "rar_sha256": "808a98d7f02e5fd6b17c4a13194612398ae603c4ec0db9affa324c07055dc183", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_monitor_data_synchronization_failures`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_monitor_data_synchronization_failures_agent.py` and in the RCI capsule.

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

Monitor data synchronization failures Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on data synchronization failures from Dynamics 365 F&SCM ERP data, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-monitor-data-synchronization-failures
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
      "description": "Prior period to chart the trend against.",
      "type": "string"
    },
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
      "description": "Target .pptx filename, e.g. ppt-exec-monitor-data-synchronization-failures-2026-05-24.pptx.",
      "type": "string"
    },
    "review_context": {
      "description": "Meeting length and cadence the deck is sized for, e.g. 15-minute monthly review.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_monitor_data_synchronization_failures_agent.py` and embedded as the fenced Python below (sha256 808a98d7f02e5fd6…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_monitor_data_synchronization_failures_agent.py` first:

```bash
python3 ppt_exec_monitor_data_synchronization_failures_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_monitor_data_synchronization_failures_agent.py   # or on stdin
python3 ppt_exec_monitor_data_synchronization_failures_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Monitor data synchronization failures Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on data synchronization failures from Dynamics 365 F&SCM ERP data, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-monitor-data-synchronization-failures
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_monitor_data_synchronization_failures',
    "version": '3.0.3',
    "display_name": 'Monitor data synchronization failures Executive PowerPoint Deck',
    "description": 'Builds a read-only executive PowerPoint deck on data synchronization failures from Dynamics 365 F&SCM ERP data, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-monitor-data-synchronization-failures',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-monitor-data-synchronization-failures',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '6bf6c3b7db9b902f',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-data/monitor-data-synchronization-failures'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/ppt-exec-monitor-data-synchronization-failures', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'comparison_period': 'Prior period to chart the trend against.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report on (e.g. USMF).', 'output_filename': 'Target .pptx filename, e.g. ppt-exec-monitor-data-synchronization-failures-2026-05-24.pptx.', 'review_context': 'Meeting length and cadence the deck is sized for, e.g. 15-minute monthly review.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Cuts deck prep time from hours to minutes for monitor data synchronization failures reviews while ensuring the numbers in the slides match D365 to the cent.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build an executive PowerPoint deck on monitor data synchronization failures for a 15-minute monthly review. Produce 'ppt-exec-monitor-data-synchronization-failures-2026-05-24.pptx' with: (1) title slide, (2) headline KPIs, (3) trend chart vs prior period, (4) top issues / red flags, (5) recommended actions, (6) appendix - data sources and methodology. Include speaker-notes on each slide with talking points. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads monitor data synchronization failures data and produces a 6-8 slide PowerPoint suitable for an executive review.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only executive PowerPoint deck on data synchronization failures from Dynamics 365 F&SCM ERP data, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.', 'example_request': 'Build an exec PowerPoint on data sync failures for USMF for our 15-minute monthly review.', 'inputs': [{'description': 'D365 legal entity to report on (e.g. USMF).', 'name': 'legal_entity'}, {'description': 'Target .pptx filename, e.g. ppt-exec-monitor-data-synchronization-failures-2026-05-24.pptx.', 'name': 'output_filename'}, {'description': 'Meeting length and cadence the deck is sized for, e.g. 15-minute monthly review.', 'name': 'review_context'}, {'description': 'Prior period to chart the trend against.', 'name': 'comparison_period'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants an executive-ready deck summarizing D365 data sync failure status for a short monthly review; no data is modified.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class PptExecMonitorDataSynchronizationFailures(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecMonitorDataSynchronizationFailures'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'comparison_period': {'description': 'Prior period to chart the trend against.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report on (e.g. USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Target .pptx filename, e.g. ppt-exec-monitor-data-synchronization-failures-2026-05-24.pptx.', 'type': 'string'}, 'review_context': {'description': 'Meeting length and cadence the deck is sized for, e.g. 15-minute monthly review.', 'type': 'string'}},
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
    print(PptExecMonitorDataSynchronizationFailures().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
