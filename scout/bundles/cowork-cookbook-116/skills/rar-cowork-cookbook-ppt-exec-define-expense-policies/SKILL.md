---
name: "rar-cowork-cookbook-ppt-exec-define-expense-policies"
description: "Builds a read-only executive PowerPoint deck on expense-policy status from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, red-flag, action and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_define_expense_policies", "rar_sha256": "e654eb70debdcc5e981c43eddceaa0050136d0590929a4d60766e2142e97657a", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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
