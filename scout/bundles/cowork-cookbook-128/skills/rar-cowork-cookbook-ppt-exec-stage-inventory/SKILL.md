---
name: "rar-cowork-cookbook-ppt-exec-stage-inventory"
description: "Builds a read-only executive PowerPoint deck on stage inventory from Dynamics 365 F&SCM data, with title, KPI, trend, red-flag, actions, and appendix slides plus speaker notes; call for a monthly review deck."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_stage_inventory", "rar_sha256": "d76a581f7ae593298410969ecc61b39c26e10de57d43236f9d81389592feb8ba", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_stage_inventory`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_stage_inventory_agent.py` and in the RCI capsule.

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

Stage inventory Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on stage inventory from Dynamics 365 F&SCM data, with title, KPI, trend, red-flag, actions, and appendix slides plus speaker notes; call for a monthly review deck.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-stage-inventory
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
      "description": "D365 legal entity to pull stage inventory from, e.g. USMF.",
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
      "description": "Name of the .pptx file to produce, e.g. ppt-exec-stage-inventory-2026-05-24.pptx.",
      "type": "string"
    },
    "review_length": {
      "description": "Target meeting length the deck is scoped to, e.g. 15-minute monthly review.",
      "type": "string"
    },
    "review_period": {
      "description": "Reporting period and prior period used for the trend chart comparison.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_stage_inventory_agent.py` and embedded as the fenced Python below (sha256 d76a581f7ae59329…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_stage_inventory_agent.py` first:

```bash
python3 ppt_exec_stage_inventory_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_stage_inventory_agent.py   # or on stdin
python3 ppt_exec_stage_inventory_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Stage inventory Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on stage inventory from Dynamics 365 F&SCM data, with title, KPI, trend, red-flag, actions, and appendix slides plus speaker notes; call for a monthly review deck.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-stage-inventory
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_stage_inventory',
    "version": '3.0.3',
    "display_name": 'Stage inventory Executive PowerPoint Deck',
    "description": 'Builds a read-only executive PowerPoint deck on stage inventory from Dynamics 365 F&SCM data, with title, KPI, trend, red-flag, actions, and appendix slides plus speaker notes; call for a monthly review deck.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'inventory_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-stage-inventory',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-stage-inventory',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '5f7e7fe70088f410',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/maintain-inventory-levels/stage-inventory'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/ppt-exec-stage-inventory', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to pull stage inventory from, e.g. USMF.', 'output_filename': 'Name of the .pptx file to produce, e.g. ppt-exec-stage-inventory-2026-05-24.pptx.', 'review_length': 'Target meeting length the deck is scoped to, e.g. 15-minute monthly review.', 'review_period': 'Reporting period and prior period used for the trend chart comparison.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Cuts deck prep time from hours to minutes for stage inventory reviews while ensuring the numbers in the slides match D365 to the cent.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build an executive PowerPoint deck on stage inventory for a 15-minute monthly review. Produce 'ppt-exec-stage-inventory-2026-05-24.pptx' with: (1) title slide, (2) headline KPIs, (3) trend chart vs prior period, (4) top issues / red flags, (5) recommended actions, (6) appendix - data sources and methodology. Include speaker-notes on each slide with talking points. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads stage inventory data and produces a 6-8 slide PowerPoint suitable for an executive review.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only executive PowerPoint deck on stage inventory from Dynamics 365 F&SCM data, with title, KPI, trend, red-flag, actions, and appendix slides plus speaker notes; call for a monthly review deck.', 'example_request': "Build my executive stage inventory deck for USMF for this month's 15-minute review.", 'inputs': [{'description': 'D365 legal entity to pull stage inventory from, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-stage-inventory-2026-05-24.pptx.', 'name': 'output_filename'}, {'description': 'Reporting period and prior period used for the trend chart comparison.', 'name': 'review_period'}, {'description': 'Target meeting length the deck is scoped to, e.g. 15-minute monthly review.', 'name': 'review_length'}], 'model': 'claude-opus-5', 'when_to_use': 'Use when a user wants an executive stage-inventory PPTX for a 15-minute monthly review, sourced from D365 ERP without modifying any data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class PptExecStageInventory(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecStageInventory'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to pull stage inventory from, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-stage-inventory-2026-05-24.pptx.', 'type': 'string'}, 'review_length': {'description': 'Target meeting length the deck is scoped to, e.g. 15-minute monthly review.', 'type': 'string'}, 'review_period': {'description': 'Reporting period and prior period used for the trend chart comparison.', 'type': 'string'}},
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
    print(PptExecStageInventory().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
