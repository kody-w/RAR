---
name: "rar-cowork-cookbook-ppt-exec-detect-asynchronous-integrations-failures"
description: "Builds a read-only executive PowerPoint deck on asynchronous integration failures from Dynamics 365 F&SCM data, with KPI, trend, red-flag, action and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_detect_asynchronous_integrations_failures", "rar_sha256": "222553cfba4b84fda8105d6191ed73584a187fee853346b2151184e7e6032312", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
