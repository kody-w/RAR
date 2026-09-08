---
name: "rar-cowork-cookbook-ppt-exec-pick-goods"
description: "Builds a read-only executive PowerPoint deck on pick goods status from Dynamics 365 F&SCM data, with title, KPI, trend, issues, actions and appendix slides plus speaker notes; call it to prep a monthly review."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_pick_goods", "rar_sha256": "b3949c07ac736b717eb76b8c923daa19d67d33b7e70b7733ef9d36f484f64e06", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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
