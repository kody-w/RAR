---
name: "rar-cowork-cookbook-ppt-exec-allocate-budgets"
description: "Builds a read-only executive PowerPoint deck on allocate budgets from Dynamics 365 ERP data for a legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_allocate_budgets", "rar_sha256": "6dd14d7d6c89a7eba6954e2f3f2598421d0be1259804ff24f65c6cfaca9dd000", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_allocate_budgets`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_allocate_budgets_agent.py` and in the RCI capsule.

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

Allocate budgets Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on allocate budgets from Dynamics 365 ERP data for a legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-allocate-budgets
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
      "description": "Dynamics 365 legal entity to report on (e.g. USMF).",
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
      "description": "Target .pptx filename, e.g. ppt-exec-allocate-budgets-2026-05-24.pptx.",
      "type": "string"
    },
    "review_period": {
      "description": "Monthly period covered and the prior period to compare against.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_allocate_budgets_agent.py` and embedded as the fenced Python below (sha256 6dd14d7d6c89a7eb…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_allocate_budgets_agent.py` first:

```bash
python3 ppt_exec_allocate_budgets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_allocate_budgets_agent.py   # or on stdin
python3 ppt_exec_allocate_budgets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Allocate budgets Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on allocate budgets from Dynamics 365 ERP data for a legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-allocate-budgets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_allocate_budgets',
    "version": '3.0.3',
    "display_name": 'Allocate budgets Executive PowerPoint Deck',
    "description": 'Builds a read-only executive PowerPoint deck on allocate budgets from Dynamics 365 ERP data for a legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.',
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
        "upstream_slug": 'ppt-exec-allocate-budgets',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-allocate-budgets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '1c3b60e13060862c',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/manage-budgets/allocate-budgets'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/ppt-exec-allocate-budgets', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to report on (e.g. USMF).', 'output_filename': 'Target .pptx filename, e.g. ppt-exec-allocate-budgets-2026-05-24.pptx.', 'review_period': 'Monthly period covered and the prior period to compare against.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Cuts deck prep time from hours to minutes for allocate budgets reviews while ensuring the numbers in the slides match D365 to the cent.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build an executive PowerPoint deck on allocate budgets for a 15-minute monthly review. Produce 'ppt-exec-allocate-budgets-2026-05-24.pptx' with: (1) title slide, (2) headline KPIs, (3) trend chart vs prior period, (4) top issues / red flags, (5) recommended actions, (6) appendix - data sources and methodology. Include speaker-notes on each slide with talking points. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-25', 'what_it_does': 'Reads allocate budgets data and produces a 6-8 slide PowerPoint suitable for an executive review.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only executive PowerPoint deck on allocate budgets from Dynamics 365 ERP data for a legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.', 'example_request': "Build the executive allocate budgets PowerPoint deck for USMF for this month's 15-minute review.", 'inputs': [{'description': 'Dynamics 365 legal entity to report on (e.g. USMF).', 'name': 'legal_entity'}, {'description': 'Monthly period covered and the prior period to compare against.', 'name': 'review_period'}, {'description': 'Target .pptx filename, e.g. ppt-exec-allocate-budgets-2026-05-24.pptx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user needs an executive allocate-budgets deck for a 15-minute monthly review, sourced from Dynamics 365 F&SCM without changing any data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class PptExecAllocateBudgets(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecAllocateBudgets'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to report on (e.g. USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Target .pptx filename, e.g. ppt-exec-allocate-budgets-2026-05-24.pptx.', 'type': 'string'}, 'review_period': {'description': 'Monthly period covered and the prior period to compare against.', 'type': 'string'}},
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
    print(PptExecAllocateBudgets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
