---
name: "rar-cowork-cookbook-ppt-exec-define-expense-policies"
description: "Builds a read-only executive PowerPoint deck on expense-policy status from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, red-flag, action and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_define_expense_policies", "rar_sha256": "e654eb70debdcc5e981c43eddceaa0050136d0590929a4d60766e2142e97657a", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_define_expense_policies`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_define_expense_policies_agent.py` and in the RCI capsule.

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

Define expense policies Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on expense-policy status from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, red-flag, action and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-define-expense-policies
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
      "description": "Name of the .pptx file to produce, e.g. ppt-exec-define-expense-policies-2026-05-24.pptx.",
      "type": "string"
    },
    "review_period": {
      "description": "Reporting period and prior period used for the trend comparison (e.g. monthly review as of 2026-05-24).",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_define_expense_policies_agent.py` and embedded as the fenced Python below (sha256 e654eb70debdcc5e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_define_expense_policies_agent.py` first:

```bash
python3 ppt_exec_define_expense_policies_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_define_expense_policies_agent.py   # or on stdin
python3 ppt_exec_define_expense_policies_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define expense policies Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on expense-policy status from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, red-flag, action and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-define-expense-policies
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_define_expense_policies',
    "version": '3.0.3',
    "display_name": 'Define expense policies Executive PowerPoint Deck',
    "description": 'Builds a read-only executive PowerPoint deck on expense-policy status from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, red-flag, action and appendix slides plus speaker notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'hire_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-define-expense-policies',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-define-expense-policies',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'de776e78e138b621',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/develop-people-strategy/define-expense-policies'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/ppt-exec-define-expense-policies', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report on (e.g. USMF).', 'output_filename': 'Name of the .pptx file to produce, e.g. ppt-exec-define-expense-policies-2026-05-24.pptx.', 'review_period': 'Reporting period and prior period used for the trend comparison (e.g. monthly review as of 2026-05-24).'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Cuts deck prep time from hours to minutes for define expense policies reviews while ensuring the numbers in the slides match D365 to the cent.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build an executive PowerPoint deck on define expense policies for a 15-minute monthly review. Produce 'ppt-exec-define-expense-policies-2026-05-24.pptx' with: (1) title slide, (2) headline KPIs, (3) trend chart vs prior period, (4) top issues / red flags, (5) recommended actions, (6) appendix - data sources and methodology. Include speaker-notes on each slide with talking points. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads define expense policies data and produces a 6-8 slide PowerPoint suitable for an executive review.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only executive PowerPoint deck on expense-policy status from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, red-flag, action and appendix slides plus speaker notes.', 'example_request': "Build the executive deck on define expense policies for USMF for this month's 15-minute review.", 'inputs': [{'description': 'D365 legal entity to report on (e.g. USMF).', 'name': 'legal_entity'}, {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-define-expense-policies-2026-05-24.pptx.', 'name': 'output_filename'}, {'description': 'Reporting period and prior period used for the trend comparison (e.g. monthly review as of 2026-05-24).', 'name': 'review_period'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user needs a 15-minute monthly executive review deck on define expense policies from D365 ERP data, without modifying any data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class PptExecDefineExpensePolicies(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecDefineExpensePolicies'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report on (e.g. USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-define-expense-policies-2026-05-24.pptx.', 'type': 'string'}, 'review_period': {'description': 'Reporting period and prior period used for the trend comparison (e.g. monthly review as of 2026-05-24).', 'type': 'string'}},
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
    print(PptExecDefineExpensePolicies().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
