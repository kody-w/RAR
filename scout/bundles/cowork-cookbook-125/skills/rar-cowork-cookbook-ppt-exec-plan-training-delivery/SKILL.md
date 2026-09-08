---
name: "rar-cowork-cookbook-ppt-exec-plan-training-delivery"
description: "Builds a read-only executive PowerPoint deck on plan training delivery from Dynamics 365 ERP data for a legal entity, with title, KPI, trend, issues, actions and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_plan_training_delivery", "rar_sha256": "e1862e92d1a936a0404753290c6c27b78a0c4c127342ddaf9f646e7b86e348dd", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_plan_training_delivery`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_plan_training_delivery_agent.py` and in the RCI capsule.

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

Plan training delivery Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on plan training delivery from Dynamics 365 ERP data for a legal entity, with title, KPI, trend, issues, actions and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-plan-training-delivery
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
      "description": "Target .pptx filename, e.g. ppt-exec-plan-training-delivery-2026-05-24.pptx.",
      "type": "string"
    },
    "review_period": {
      "description": "Reporting period and prior period used for the trend comparison (e.g. monthly).",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_plan_training_delivery_agent.py` and embedded as the fenced Python below (sha256 e1862e92d1a936a0…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_plan_training_delivery_agent.py` first:

```bash
python3 ppt_exec_plan_training_delivery_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_plan_training_delivery_agent.py   # or on stdin
python3 ppt_exec_plan_training_delivery_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Plan training delivery Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on plan training delivery from Dynamics 365 ERP data for a legal entity, with title, KPI, trend, issues, actions and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-plan-training-delivery
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_plan_training_delivery',
    "version": '3.0.3',
    "display_name": 'Plan training delivery Executive PowerPoint Deck',
    "description": 'Builds a read-only executive PowerPoint deck on plan training delivery from Dynamics 365 ERP data for a legal entity, with title, KPI, trend, issues, actions and appendix slides plus speaker notes.',
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
        "upstream_slug": 'ppt-exec-plan-training-delivery',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-plan-training-delivery',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '172dc0d9bce8f7e2',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/train-users-and-increase-adoption/plan-training-delivery'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/ppt-exec-plan-training-delivery', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report on, e.g. USMF.', 'output_filename': 'Target .pptx filename, e.g. ppt-exec-plan-training-delivery-2026-05-24.pptx.', 'review_period': 'Reporting period and prior period used for the trend comparison (e.g. monthly).'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Cuts deck prep time from hours to minutes for plan training delivery reviews while ensuring the numbers in the slides match D365 to the cent.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build an executive PowerPoint deck on plan training delivery for a 15-minute monthly review. Produce 'ppt-exec-plan-training-delivery-2026-05-24.pptx' with: (1) title slide, (2) headline KPIs, (3) trend chart vs prior period, (4) top issues / red flags, (5) recommended actions, (6) appendix - data sources and methodology. Include speaker-notes on each slide with talking points. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads plan training delivery data and produces a 6-8 slide PowerPoint suitable for an executive review.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only executive PowerPoint deck on plan training delivery from Dynamics 365 ERP data for a legal entity, with title, KPI, trend, issues, actions and appendix slides plus speaker notes.', 'example_request': "Build the executive plan training delivery deck for USMF for this month's 15-minute review.", 'inputs': [{'description': 'D365 legal entity to report on, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Target .pptx filename, e.g. ppt-exec-plan-training-delivery-2026-05-24.pptx.', 'name': 'output_filename'}, {'description': 'Reporting period and prior period used for the trend comparison (e.g. monthly).', 'name': 'review_period'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user needs a monthly 15-minute executive review deck on plan training delivery status sourced from Dynamics 365 F&SCM.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class PptExecPlanTrainingDelivery(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecPlanTrainingDelivery'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report on, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Target .pptx filename, e.g. ppt-exec-plan-training-delivery-2026-05-24.pptx.', 'type': 'string'}, 'review_period': {'description': 'Reporting period and prior period used for the trend comparison (e.g. monthly).', 'type': 'string'}},
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
    print(PptExecPlanTrainingDelivery().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
