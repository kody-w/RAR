---
name: "rar-cowork-cookbook-ppt-exec-plan-training-delivery"
description: "Builds a read-only executive PowerPoint deck on plan training delivery from Dynamics 365 ERP data for a legal entity, with title, KPI, trend, issues, actions and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_plan_training_delivery", "rar_sha256": "e1862e92d1a936a0404753290c6c27b78a0c4c127342ddaf9f646e7b86e348dd", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
