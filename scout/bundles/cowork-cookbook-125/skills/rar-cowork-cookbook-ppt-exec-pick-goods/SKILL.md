---
name: "rar-cowork-cookbook-ppt-exec-pick-goods"
description: "Builds a read-only executive PowerPoint deck on pick goods status from Dynamics 365 F&SCM data, with title, KPI, trend, issues, actions and appendix slides plus speaker notes; call it to prep a monthly review."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_pick_goods", "rar_sha256": "b3949c07ac736b717eb76b8c923daa19d67d33b7e70b7733ef9d36f484f64e06", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_pick_goods`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_pick_goods_agent.py` and in the RCI capsule.

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

Pick goods Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on pick goods status from Dynamics 365 F&SCM data, with title, KPI, trend, issues, actions and appendix slides plus speaker notes; call it to prep a monthly review.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-pick-goods
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
    "comparison_period": {
      "description": "Prior period to trend current pick goods performance against.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to query, e.g. USMF.",
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
      "description": "Name of the .pptx file to produce, e.g. ppt-exec-pick-goods-2026-05-24.pptx.",
      "type": "string"
    },
    "review_length": {
      "description": "Length/format of the review the deck must fit, e.g. 15-minute monthly review.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_pick_goods_agent.py` and embedded as the fenced Python below (sha256 b3949c07ac736b71…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_pick_goods_agent.py` first:

```bash
python3 ppt_exec_pick_goods_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_pick_goods_agent.py   # or on stdin
python3 ppt_exec_pick_goods_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Pick goods Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on pick goods status from Dynamics 365 F&SCM data, with title, KPI, trend, issues, actions and appendix slides plus speaker notes; call it to prep a monthly review.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-pick-goods
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_pick_goods',
    "version": '3.0.3',
    "display_name": 'Pick goods Executive PowerPoint Deck',
    "description": 'Builds a read-only executive PowerPoint deck on pick goods status from Dynamics 365 F&SCM data, with title, KPI, trend, issues, actions and appendix slides plus speaker notes; call it to prep a monthly review.',
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
        "upstream_slug": 'ppt-exec-pick-goods',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-pick-goods',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '39df96bf3b7a8585',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/process-outbound-goods/pick-goods'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/ppt-exec-pick-goods', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'comparison_period': 'Prior period to trend current pick goods performance against.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'output_filename': 'Name of the .pptx file to produce, e.g. ppt-exec-pick-goods-2026-05-24.pptx.', 'review_length': 'Length/format of the review the deck must fit, e.g. 15-minute monthly review.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Cuts deck prep time from hours to minutes for pick goods reviews while ensuring the numbers in the slides match D365 to the cent.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build an executive PowerPoint deck on pick goods for a 15-minute monthly review. Produce 'ppt-exec-pick-goods-2026-05-24.pptx' with: (1) title slide, (2) headline KPIs, (3) trend chart vs prior period, (4) top issues / red flags, (5) recommended actions, (6) appendix - data sources and methodology. Include speaker-notes on each slide with talking points. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads pick goods data and produces a 6-8 slide PowerPoint suitable for an executive review.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only executive PowerPoint deck on pick goods status from Dynamics 365 F&SCM data, with title, KPI, trend, issues, actions and appendix slides plus speaker notes; call it to prep a monthly review.', 'example_request': 'Build an executive pick goods deck for USMF for our 15-minute monthly review, with speaker notes.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-pick-goods-2026-05-24.pptx.', 'name': 'output_filename'}, {'description': 'Length/format of the review the deck must fit, e.g. 15-minute monthly review.', 'name': 'review_length'}, {'description': 'Prior period to trend current pick goods performance against.', 'name': 'comparison_period'}], 'model': 'claude-opus-5', 'when_to_use': 'Use when preparing a 15-minute monthly executive review of pick goods status from D365 ERP data and you need a slide deck with talking points.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class PptExecPickGoods(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecPickGoods'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'comparison_period': {'description': 'Prior period to trend current pick goods performance against.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-pick-goods-2026-05-24.pptx.', 'type': 'string'}, 'review_length': {'description': 'Length/format of the review the deck must fit, e.g. 15-minute monthly review.', 'type': 'string'}},
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
    print(PptExecPickGoods().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
