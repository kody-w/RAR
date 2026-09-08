---
name: "rar-cowork-cookbook-ppt-exec-stage-inventory"
description: "Builds a read-only executive PowerPoint deck on stage inventory from Dynamics 365 F&SCM data, with title, KPI, trend, red-flag, actions, and appendix slides plus speaker notes; call for a monthly review deck."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_stage_inventory", "rar_sha256": "d76a581f7ae593298410969ecc61b39c26e10de57d43236f9d81389592feb8ba", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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
