---
name: "rar-cowork-cookbook-ppt-exec-identify-critical-system-and-data"
description: "Builds a read-only executive PowerPoint deck on critical system and data status from Dynamics 365 F&SCM ERP data for a given legal entity, with KPI, trend, red-flag, action and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_identify_critical_system_and_data", "rar_sha256": "2ac0100c7a5cb55a9b1802f97f2142eecc43b0c771c1e7f47fc91a284b3cacbb", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
