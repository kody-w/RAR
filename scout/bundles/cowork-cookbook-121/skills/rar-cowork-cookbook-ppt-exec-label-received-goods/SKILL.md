---
name: "rar-cowork-cookbook-ppt-exec-label-received-goods"
description: "Builds a read-only executive PowerPoint deck on label received goods status from Dynamics 365 F&SCM data, with title, KPI, trend, red-flag, actions, and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_label_received_goods", "rar_sha256": "2fbfa6142084460ad1d99d56a5c281fb47b697edaf33e918fe0a0bc19f5d5d77", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_label_received_goods`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_label_received_goods_agent.py` and in the RCI capsule.

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

Label received goods Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on label received goods status from Dynamics 365 F&SCM data, with title, KPI, trend, red-flag, actions, and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-label-received-goods
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
      "description": "Prior period to chart the trend against.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to pull data from, e.g. USMF.",
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
      "description": "Name of the .pptx file to produce, e.g. ppt-exec-label-received-goods-2026-05-24.pptx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_label_received_goods_agent.py` and embedded as the fenced Python below (sha256 2fbfa6142084460a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_label_received_goods_agent.py` first:

```bash
python3 ppt_exec_label_received_goods_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_label_received_goods_agent.py   # or on stdin
python3 ppt_exec_label_received_goods_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Label received goods Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on label received goods status from Dynamics 365 F&SCM data, with title, KPI, trend, red-flag, actions, and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-label-received-goods
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_label_received_goods',
    "version": '3.0.3',
    "display_name": 'Label received goods Executive PowerPoint Deck',
    "description": 'Builds a read-only executive PowerPoint deck on label received goods status from Dynamics 365 F&SCM data, with title, KPI, trend, red-flag, actions, and appendix slides plus speaker notes.',
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
        "upstream_slug": 'ppt-exec-label-received-goods',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-label-received-goods',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '1bf26ae8ae06b352',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/process-inbound-goods/label-received-goods'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/ppt-exec-label-received-goods', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'comparison_period': 'Prior period to chart the trend against.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to pull data from, e.g. USMF.', 'output_filename': 'Name of the .pptx file to produce, e.g. ppt-exec-label-received-goods-2026-05-24.pptx.', 'review_length': 'Length/format of the review the deck must fit, e.g. 15-minute monthly review.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Cuts deck prep time from hours to minutes for label received goods reviews while ensuring the numbers in the slides match D365 to the cent.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build an executive PowerPoint deck on label received goods for a 15-minute monthly review. Produce 'ppt-exec-label-received-goods-2026-05-24.pptx' with: (1) title slide, (2) headline KPIs, (3) trend chart vs prior period, (4) top issues / red flags, (5) recommended actions, (6) appendix - data sources and methodology. Include speaker-notes on each slide with talking points. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads label received goods data and produces a 6-8 slide PowerPoint suitable for an executive review.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only executive PowerPoint deck on label received goods status from Dynamics 365 F&SCM data, with title, KPI, trend, red-flag, actions, and appendix slides plus speaker notes.', 'example_request': 'Build an executive PowerPoint on label received goods for USMF for our 15-minute monthly review.', 'inputs': [{'description': 'D365 legal entity to pull data from, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-label-received-goods-2026-05-24.pptx.', 'name': 'output_filename'}, {'description': 'Length/format of the review the deck must fit, e.g. 15-minute monthly review.', 'name': 'review_length'}, {'description': 'Prior period to chart the trend against.', 'name': 'comparison_period'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user needs an executive-ready label received goods deck for a short monthly review, sourced from D365 ERP without modifying data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class PptExecLabelReceivedGoods(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecLabelReceivedGoods'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'comparison_period': {'description': 'Prior period to chart the trend against.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to pull data from, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-label-received-goods-2026-05-24.pptx.', 'type': 'string'}, 'review_length': {'description': 'Length/format of the review the deck must fit, e.g. 15-minute monthly review.', 'type': 'string'}},
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
    print(PptExecLabelReceivedGoods().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
