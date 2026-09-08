---
name: "rar-cowork-cookbook-ppt-exec-identify-critical-system-and-data"
description: "Builds a read-only executive PowerPoint deck on critical system and data status from Dynamics 365 F&SCM ERP data for a given legal entity, with KPI, trend, red-flag, action and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_identify_critical_system_and_data", "rar_sha256": "2ac0100c7a5cb55a9b1802f97f2142eecc43b0c771c1e7f47fc91a284b3cacbb", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_identify_critical_system_and_data`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_identify_critical_system_and_data_agent.py` and in the RCI capsule.

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

Identify critical system and data Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on critical system and data status from Dynamics 365 F&SCM ERP data for a given legal entity, with KPI, trend, red-flag, action and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-identify-critical-system-and-data
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
      "description": "Target .pptx filename, e.g. ppt-exec-identify-critical-system-and-data-2026-05-24.pptx.",
      "type": "string"
    },
    "review_period": {
      "description": "Reporting period and prior period for trend comparison (e.g. month of 2026-05).",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_identify_critical_system_and_data_agent.py` and embedded as the fenced Python below (sha256 2ac0100c7a5cb55a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_identify_critical_system_and_data_agent.py` first:

```bash
python3 ppt_exec_identify_critical_system_and_data_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_identify_critical_system_and_data_agent.py   # or on stdin
python3 ppt_exec_identify_critical_system_and_data_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Identify critical system and data Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on critical system and data status from Dynamics 365 F&SCM ERP data for a given legal entity, with KPI, trend, red-flag, action and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-identify-critical-system-and-data
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_identify_critical_system_and_data',
    "version": '3.0.3',
    "display_name": 'Identify critical system and data Executive PowerPoint Deck',
    "description": 'Builds a read-only executive PowerPoint deck on critical system and data status from Dynamics 365 F&SCM ERP data for a given legal entity, with KPI, trend, red-flag, action and appendix slides plus speaker notes.',
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
        "upstream_slug": 'ppt-exec-identify-critical-system-and-data',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-identify-critical-system-and-data',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'b10d8cb7f3a65519',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/define-business-continuity-plan/identify-critical-system-and-data'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/ppt-exec-identify-critical-system-and-data', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report on, e.g. USMF.', 'output_filename': 'Target .pptx filename, e.g. ppt-exec-identify-critical-system-and-data-2026-05-24.pptx.', 'review_period': 'Reporting period and prior period for trend comparison (e.g. month of 2026-05).'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Cuts deck prep time from hours to minutes for identify critical system and data reviews while ensuring the numbers in the slides match D365 to the cent.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build an executive PowerPoint deck on identify critical system and data for a 15-minute monthly review. Produce 'ppt-exec-identify-critical-system-and-data-2026-05-24.pptx' with: (1) title slide, (2) headline KPIs, (3) trend chart vs prior period, (4) top issues / red flags, (5) recommended actions, (6) appendix - data sources and methodology. Include speaker-notes on each slide with talking points. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads identify critical system and data data and produces a 6-8 slide PowerPoint suitable for an executive review.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only executive PowerPoint deck on critical system and data status from Dynamics 365 F&SCM ERP data for a given legal entity, with KPI, trend, red-flag, action and appendix slides plus speaker notes.', 'example_request': 'Build the executive PowerPoint deck on critical system and data for USMF for the May 2026 monthly review.', 'inputs': [{'description': 'D365 legal entity to report on, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Target .pptx filename, e.g. ppt-exec-identify-critical-system-and-data-2026-05-24.pptx.', 'name': 'output_filename'}, {'description': 'Reporting period and prior period for trend comparison (e.g. month of 2026-05).', 'name': 'review_period'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user needs a 15-minute monthly executive review deck on critical system and data status sourced from D365 ERP, without modifying any data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class PptExecIdentifyCriticalSystemAndData(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecIdentifyCriticalSystemAndData'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report on, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Target .pptx filename, e.g. ppt-exec-identify-critical-system-and-data-2026-05-24.pptx.', 'type': 'string'}, 'review_period': {'description': 'Reporting period and prior period for trend comparison (e.g. month of 2026-05).', 'type': 'string'}},
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
    print(PptExecIdentifyCriticalSystemAndData().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
