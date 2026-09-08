---
name: "rar-cowork-cookbook-ppt-exec-detect-asynchronous-integrations-failures"
description: "Builds a read-only executive PowerPoint deck on asynchronous integration failures from Dynamics 365 F&SCM data, with KPI, trend, red-flag, action and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_detect_asynchronous_integrations_failures", "rar_sha256": "222553cfba4b84fda8105d6191ed73584a187fee853346b2151184e7e6032312", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_detect_asynchronous_integrations_failures`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_detect_asynchronous_integrations_failures_agent.py` and in the RCI capsule.

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

Detect asynchronous integrations failures Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on asynchronous integration failures from Dynamics 365 F&SCM data, with KPI, trend, red-flag, action and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-detect-asynchronous-integrations-failures
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
      "description": "D365 legal entity to report on, e.g. USMF.",
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
      "description": "Name of the .pptx file to produce, e.g. ppt-exec-detect-asynchronous-integrations-failures-2026-05-24.pptx.",
      "type": "string"
    },
    "review_period": {
      "description": "Reporting period and prior period for the trend comparison (e.g. monthly review as of 2026-05-24).",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_detect_asynchronous_integrations_failures_agent.py` and embedded as the fenced Python below (sha256 222553cfba4b84fd…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_detect_asynchronous_integrations_failures_agent.py` first:

```bash
python3 ppt_exec_detect_asynchronous_integrations_failures_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_detect_asynchronous_integrations_failures_agent.py   # or on stdin
python3 ppt_exec_detect_asynchronous_integrations_failures_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Detect asynchronous integrations failures Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on asynchronous integration failures from Dynamics 365 F&SCM data, with KPI, trend, red-flag, action and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-detect-asynchronous-integrations-failures
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_detect_asynchronous_integrations_failures',
    "version": '3.0.3',
    "display_name": 'Detect asynchronous integrations failures Executive PowerPoint Deck',
    "description": 'Builds a read-only executive PowerPoint deck on asynchronous integration failures from Dynamics 365 F&SCM data, with KPI, trend, red-flag, action and appendix slides plus speaker notes.',
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
        "upstream_slug": 'ppt-exec-detect-asynchronous-integrations-failures',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-detect-asynchronous-integrations-failures',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '6d313435d22f4df0',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/monitor-systems-environments-and-capacity/detect-asynchronous-integrations-failures'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/ppt-exec-detect-asynchronous-integrations-failures', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report on, e.g. USMF.', 'output_filename': 'Name of the .pptx file to produce, e.g. ppt-exec-detect-asynchronous-integrations-failures-2026-05-24.pptx.', 'review_period': 'Reporting period and prior period for the trend comparison (e.g. monthly review as of 2026-05-24).'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Cuts deck prep time from hours to minutes for detect asynchronous integrations failures reviews while ensuring the numbers in the slides match D365 to the cent.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build an executive PowerPoint deck on detect asynchronous integrations failures for a 15-minute monthly review. Produce 'ppt-exec-detect-asynchronous-integrations-failures-2026-05-24.pptx' with: (1) title slide, (2) headline KPIs, (3) trend chart vs prior period, (4) top issues / red flags, (5) recommended actions, (6) appendix - data sources and methodology. Include speaker-notes on each slide with talking points. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads detect asynchronous integrations failures data and produces a 6-8 slide PowerPoint suitable for an executive review.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only executive PowerPoint deck on asynchronous integration failures from Dynamics 365 F&SCM data, with KPI, trend, red-flag, action and appendix slides plus speaker notes.', 'example_request': "Build the exec PowerPoint on async integration failures for USMF for this month's 15-minute review.", 'inputs': [{'description': 'D365 legal entity to report on, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-detect-asynchronous-integrations-failures-2026-05-24.pptx.', 'name': 'output_filename'}, {'description': 'Reporting period and prior period for the trend comparison (e.g. monthly review as of 2026-05-24).', 'name': 'review_period'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user needs a 15-minute monthly review deck summarizing async integration failure status from D365 ERP data, without modifying any data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class PptExecDetectAsynchronousIntegrationsFailures(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecDetectAsynchronousIntegrationsFailures'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report on, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-detect-asynchronous-integrations-failures-2026-05-24.pptx.', 'type': 'string'}, 'review_period': {'description': 'Reporting period and prior period for the trend comparison (e.g. monthly review as of 2026-05-24).', 'type': 'string'}},
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
    print(PptExecDetectAsynchronousIntegrationsFailures().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
