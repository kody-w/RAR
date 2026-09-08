---
name: "rar-cowork-cookbook-ppt-exec-monitor-data-synchronization-failures"
description: "Builds a read-only executive PowerPoint deck on data synchronization failures from Dynamics 365 F&SCM ERP data, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_monitor_data_synchronization_failures", "rar_sha256": "808a98d7f02e5fd6b17c4a13194612398ae603c4ec0db9affa324c07055dc183", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
