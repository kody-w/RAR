---
name: "rar-cowork-cookbook-ppt-exec-label-received-goods"
description: "Builds a read-only executive PowerPoint deck on label received goods status from Dynamics 365 F&SCM data, with title, KPI, trend, red-flag, actions, and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_label_received_goods", "rar_sha256": "2fbfa6142084460ad1d99d56a5c281fb47b697edaf33e918fe0a0bc19f5d5d77", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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

<!-- rci-capsule:v1:H4sIAAAAAAAC/9V6adOjVrLmX9G8N2JsX6oKhFhroiOGXRJIYhfC1VFmE/sOAsnT/30O0ltlu9vd93bEfBlV2RJwTu75ZGYdfn3zxiGpu7fPb0bkVSvJK4o0ibqVV4Urrp7qLgdfde6D/1ZBXQ1d6o9D3fVvH97CqA+6tBnSugLb2TEtwn7lrbrICz/WVXFfRXMUjEN6i1ZqPUWdWqfVsAqjIF/V1arw/KgAi4MILAhXcV2D3f3gDWO/unZ1ueLvlVemQb/aEPhK/J8Gd1iF3uB9WE3pkKyGdCiiDytZ3X1YDV1UhR8ArfDjtfDiDysvWITqPzy18JoGPE7nVV+kQORVUwAOfRN5OVCzqoeo/wSUiWavbIqof/v8818/vKXg99vnX9+CwuvBrTe1GQSgjLLIrL+LLC0Sg52FV8VgSXMHdqzAdRN117orwa0wuq7er37so+L6YfWf/5lPXhf3P33+Uq3eP1/elj/6WK2GJFoNtdcPwB6B13h+WqTD/dOKKSbv3gP9hrGrFhP3wA1V/Om18zdKdbP6y/LsxxeTT3E0/PjlrQYieIs9vrz9tKo7wK8bl9+fFirNjz99Khbn/PjTb3T60c+iYFiIAak/fX2/ficLFv62NL2uvhqqwL3zAu5MmwgQ/51+y+cl+ju5d5N8fS3+sW4+rP6c8qLPX4C8r0DzAd0/JwtsAHa+fcpAgP34zqOrb1HlVUH040//jGyQgFAs0n74b9H9+UU4AdENrPVukp8+PN331xX0rtt3mv+cbQMC5t/RBCz/xu67of4Z7adn/450kVYg6r/58k/J/dkG6C+rn/+pbv9qw4fV9csbHxUgRzrPL6LPq1+fIfLzD+FvN3/4698A6f+SjFGPXfCk8LX0qvQa9cPXrz//0D9v//DXn38YGxDFkVd+Hbviz2j+mV2ffP5gwfdVP/5xL+BvVXlVT9Xqew6tfq2b/9H97dPK9gCa/Ha//7z6fSYuH2i1KPGN6csEv8vGHsj6Ozv+9PY3ADsV0GZ8gRfAj//4j9UhDbq6r6/DygjqcVgBBw9pGS3Cm0nar8DfBTW6CNi1T4Fh39eB+F88vEhcX1e//O/gCeUfg3coh5tm+LrA89cnDH/9BsNfnzD8y6eVCYjWXRqnlVesdEZVv1ReHAH4BgybLuqjbgFt/z5EH0Euf1x+rNJq9cu/pPv1SeJTc//lCczpC/F0bregXT8W0adFr3MSVe9aBKAivYpItCrqAIhyTQFGL1Df1wWoK8Nigz5Pi2IVpoAZqEz3J21gp88LsV9++cX3+uRL9YLnzepVsnoYLPguzurjR6DTtUjjZPhSRUFSr3749W8/rP7P6l/tehJfeKigRrx7AUi4N07HFciqsQTLgIOASwFkPL3w69/eLQvIVKD4AJ+l1zR6bQZRmUfhNzMbW+YjihMrPwLmBaYtm7obAOav0uHTanddfZcXMF0eLVUhqfulvC7VLqqCO6DqAXW+WxKUulUPQq+/3j+sxj56cv3F77yniCVIb2/4ZXXgVFCD6gL8bxHzuQhsrqsUmP97ELzuAyLdD/2K/Ubi0+q4xOGq8TqvSTrvncfVe/kF1J5v2wFxb1VF05dqqbTRYqpnUrzMAxYBywTvLv24+Bz0HiVAgLD/xvu5xlsqpfmsmN2Xqn8PeK9bXBGAAgCYxmMaLmXgf72HVJ/UYxE+7QckXSi9eyF898ozBpU/a06EP2tn+KWd+TKiyBpb/f/cAi1aM5KkCxJjCvxKOJr65eWNpetbvPZqFEFDsgIh+cq835qUb0D0DY+/VEUKQqu7/6/XyqcP39e8MG4EsgJk0Z/0QQABSRa6z/he4rXrlszwvlTfgB+osnqi3GK5OgDJssToN4bL02+SJiDjl+vfmoBnPHThYgwQw6tm9AsQX9coCn0P+GJIFo99cyMI9mjJ1ylJg+QPWq0AdRBTgP7ivhRkHSgOn76D8evpN9H/sPHV6yxbnn3gCFK0exIAckSLgIubFq8C8YZXkw30/PwkAtQom2HR3QdJAjR93Yy6qB3TPh0WQHzZNWoAEn9cvl+aLnejuQF5AYwFor8ZgXWf+bJASQk6GSADCEeQPmVagcoOjPJuhCdBr1ySvyi+tZ4vis/b7wpFzyRbStK3jYsiy56lyr+i2Kvuv8cI88/CBNArlxVPvn8fad+5LbQXnOwB1gGO356+2oFPr4r+ahlW3+h+/ocp5sd/b9B51mjrjwHweZUMQ9N/huFXXf1WVj8BlIJfsvZLif24pP/HZ5p//JbmH59p/geiL30/r/49wf5A4j0xPq/Wn5BPyPJIeQ+s9w+wA/eRvXzElqdfKj36DUAB+7oEkbV47Q5q+vdq920JKHlxF8XL4lf165eiOYE6/YR74IIv1e8jfck0UE2qeInMvv4dAjzLPoj6l8e+VyXwqBoA73BpD+NomceeedFHb5+rsSg+vAEcjP6LOWypOuUSyv0yuYGkAZ3WkEbPK+AX8Djt62qZPtI6XG7+cX5Vwe1u9Xq6AAtQoBteI9mCraB0PSN4kW24N4swryls6duewDMP/0j09PzhFZ9AnQAgV/S/j+b3UrSU4t8l3ct+wG4BUODDgvcAS4BkwH6LbkvCej3IABD8fypLARxVfAX2BPnzjwLxSyV5Llm9liyqNuPSP4HC8szXD6voU/xpZRkH8U8ZfO9g/5H6GbQQC8Gw/rxU0w/v0AW+wdTxYfV9gABqvY90z9G7GsG0/PMyvCxufG5ZfoA94Ov7pu//4uBHb3/9M7me+PZ1ibNXtPy9dMcFtwCuL1b+BLJzfsXkYoCuDscgetf8XybuRxRBiY8I/hHFnjT+1ESgHU+j6SsQJB6SfxREed6HlyEY2Otdotee589nf1COoJu7psO7UGv8I4DopREuQbAlxf19w5/wfwoASgMosItZf/PXb1arn/PfIiqw8vD654pf30D2eEsYvOfP+wABlgMk/dgv7RMM4AUwBNcvIADP/r3R4n1zn3iguwW70at/9Yg1hiIUhhGIF65Dmg5xwsMDlFpffYz0CZqMQu+62UT0mrpGiIf4wZq+4iEekiSg98KSr0uDmC4C4TR5RWgavWJrFAnD6IpiYUgRFBHgJIp4tO/hPk57/m9b87QK37V8abWY8PuUs1jjXdlf33wCAyu3WL9jXh8Optd+hML+XXFgB6dTJR4Cw1sLrns8Wlx2nA3vJEz6Jn84vb8bRfnBWCd3X5quGKjjbpfUIpRuSe7aKOQJDUuI3RUnuizJkGRiw77j/d2l4DScsSmc54Ii73Sx53euodp6UsrhXhJGM4P3NfeYtP1UrB870ljrQboP7iOrwNDxdp0vg6HrWX7BL1ezOWBoXLnHu5RzVt7XHVZQ/e52L+59X2qdM+LplRg5h58JqkgpaISUnAxSmhngXYvbvS6JcrrDhStN0uUlTfOHhGkGMo15Sw2BiWmRaIy7YAvtNUgq5TXUmnfuYAP6uWD7OwsqrnfrIRiG+AgfLAbfujUUVR0O0aqDdWYIwep1o4gQhliavnOE7EG6vrg/FE4/c91eV0R91DJqLUJtuieTM7ZlXbflBYci06N2p0g1tB7rqTH2TYKyjKRrhcQ61YOC3JtMp70g5nYkycfJ2rl4zpUwHhNU2O6vBw6dmavrXrq8qA1HEtHcNhXEvik45atHWKMfrqwebn6m7WUmv0+5pj2mmzhLcsJ0cnAq+IdlSevdub3Tp0taGgVIs1biTbSmGPw8bwehGNqeuxFznEYIRCIQ1T+IdXMWyyJP/Z3HW7qrP+RMjnjWKvvc2e+K6QTLvLxWhKIKiAsLd2GjuUME1Q4n3my+DIqr0VhdK80pzlUm4ew2TQhRulPXKmHdZY7LG+5hCPmeruAEryN5jap1QmkHU5EM1Pa3HIaxmwdlUoppjjpqWIgoBTzRVm7aG/xpHUdOwuVYAksjdavPAno24SjVA9dmWmkYWmEsLuy56L1JGFASzASplWzljpRnw2e9mztUje7uOJHcGSRWk6yFQ7t8tIi7DM9y1/iYglwcpIZFD+aqY8JQVjSddv4xmYzQVWP/uKV7r8KGo+WZ+JW/KJG0j/GuYPtm3ei3o1smrkndDg0IHQu6nSzYL/YWRK+VjFA74yJi0/FBXTbktEWZI0352kOBd7uTSVzGazPAKR6xAJ4t6n4P+emo7MXaFe5Du8ctMtc839g1sLtzCdgpw7t5UWfBv6kbR9vaFNspQptuH+axTKYWVbO5HKfJnBvIHPpEoCM5rhyBYVMdW9vB5ZRrdV+dLZnhM3aNVTd7esyqOh+AXOM2n7TLGevvYj5JeNM/Tjw/oPtbTWviNiWvDNm5RrPWmmZKj8dInvYPtOMuCHJ4nKdMuysTJ+4pdw9t5ZzKrlDoEg3lMFzdWvnt3Kmsz8cFatBN75nR1SUT9DpKt4C6gw01pkgid7rT6q72CMzSDgVqneAD/eCx2MH4gEYgflths0T4JzmO4vimnuSZGQp97+XVfDrfbZ6NTpvN8fzwFJbxUqfUSi56hEo8XRnrcpsuOFoUmdk7G4Ww1SlAuuJkhhMUbdzLVIUxmwWG+zCpy9W7nJR77O6GGwtI6QRZzdswm32oy+Vhe8DdMbvNII2b9WOeNG1W1ubUQjt+y9SnorXc8TiqypZnG+geB3zI+8zgbdnA08yoszSmM+Xr1EWM3GwR23Mb5VBI95vJmi21Wyt9FnGQtzbQmmxZhnvQdNW4D4uEdczEbM/i0M32RKj9gzwfXCjKz9YZCZjscLwH7snJcBv4riq2vV9s8AFRNvFtE6H5pt4F7I0vdxa2DwzKTqMDTdateG5zapueytwWFQ/ZYaU5Y5xxoNeWYrvC+EhxwaAgoYgFcysfN0QZh716NbSQ587HTDJ6bDMZfS7R16sarf3SN5wyzzb6nkPPl5LSC6Rf2zIP70sLq05eYVTKujDPnG6oZ+1mM9qODvTzuTBYLEYOYw8lurO9GOaay9k4Dde3vJbnYB3hWdQzPDHX9SlJNFrsOhEbz4GAXyR8sCQcRTKZQc29XGRH2UH96+2R41cnnI2EM++myapx6d3quEWMjDKRMvDVoKbZOGau5CGrQvhRi49hQkhPPuwkerjTV26vwHB9n0K1qKlIfeioa1xw0SAfD4ESzzPL8Mqu8Kdg08FTXWBG4XW2oek5y0BXcmIH1nRtOhrZVhmwpKE837/kGtsy+SO55cLWPKe1a+94RDQEat9sLave8bGr5dYp1NhZMBjPFQ++pl+OoNy2fI4FpSuZ9pkyJWZEC7G6hQR5kVHDc3LUZCY/4OXemSPSVuVOLl2bbEhitnylvUAuBsXsIcuFooAaWd4NG23iCS5z+aw6pZyY96MRrvNcMM2OFg/JLqVMmb7ty5Y7wPc5lymWPWu90cf1we8dOhD9wAwuhrBLcTiNiLTXOLv2vWN8OPUNefC2zQZvKdmjThDm5kxpp3yxgVw6tLNkhx2FGIwgrTHdmnjbm9kNUu7nViAacd+YnLRVFCFNxYrXSu/QFc4u3MLifIOFvdB3bN0Xfs5ynKURCgeaq51DWb4r2cVWmg6qFRNaoMv2xaDodldr+HlXWqjgjruUkTHW3Wi253URgSDG4cyzNikxdaBjelmgjmbdGpvWxi7OdckvysfahPUTA2/mVrfUPK7R/Ro/U6ejSLRoUoORFzNIg/KSSwP7ecgzl/g0RvhYPkzZoTJdF9vy7ro7m9Rq6Iq4HJs4TKz6+GnKTgbZbBPRqQzP9ZKm3O/POr9OnFI0ZPHKUWt23PXUlTjLF6vm9ii3L3NLOhLkFskwDzsye5G5brwrmleXmqdTYd1g5HauS1wzBT3k2i0GRVjLOVeTmHMFPar8gVwP9mNy9rks7KSrssmGDuZaObt6WYM17N3vsdMDxUNVn1xYsIzOO5RkGw/ahSP3vM/zeptjRsnsXNAYtJUQg8o/ifSYxtXePyGuj+4OTMVIiUMeDxZ6oLN8o4kPzXXOyAECEdJNh0Hwlb5r6sDXeuQiVHBgbyucCaS65YmusDbxpS/Ou/NZmyJZcfalTOGco594BBbmeu639h1teAkmOJMZjBag1dXG+wfsci1/YYK4ZQWJTwvIO1L8acNe0Ca0ZjmYNuuMvlGqgp/izV5OSjgmkXu1I5kTDRvSWXmoWpDkIFh3nW7m1F277qX4DEdtnoiICkc9toPEY0PMuiF0cmL2llA2VrpDGG+NsEFhEEUWzxBe0kfzIPTqGnhIo3Pbkudt2pjo7gaZJYKu1YphLFJoZU2wK5ZMyHyWtOMRwiTFyei7pVGO7djJhlH3513eMg9p8DK/EWJ379TMYHqpnFjcdOA03qfujQE5lf3I90UTyRbo8PblQ4/KWYBFHjRZenfOFTljesGbD8nGt7prN2MQ0ilZ7bR5NO3tSyafpp07svsZ53bllZZFAd/KmACxR944JeOtmaZArZDpqu4xCN67zcjXMCRn+XCJinVWH6E9Bj+0tMQCtzRNVFY3O/Wy62t+vsg9NG0yIvRFNxAjJwx8WQ7LiDVsxR0NvLN0v0VTUAUfaXtLx7t6Lcz7LaflmS0i4VxEbTYQW6aMZSa+QvS1628PEp1lT8DabM8Dq/Rlra3H/R1CjVBPuopmaLZyW/J6Fx/jxGvFZBQpIqsyCuaKI4xaiayw92MNzetMb7f6FRLlbb5VUrzlkWCg0eM4h7PXmVs1kjL/RMXKvvW9ZAOmv2SUjyfmOuRJ67o8vxFFJNysi/tedlNa2FxoFEKGy13wTtsLKenXJGODtswSY3+npaQ/CEmG5EF7REGTVrO3g8Huhai7C2N7ta6hYqmRss+o6AC5/UAbARcNKHrK9qNEbE3TJogTwT/SZs0IROoqoPlweyw9NBpa+G4hDmAuk8e4KdY1WsNjuqMbQ7/gcn0TqGYvW2m3vpA+rmiaTeiBRKo4zDCjv+etoxmlgijTF6otRf7odnd1b+qzgcTkYYfc5Da8MsdqLXEWqZRBZqpQfCMzn6r3R8+hNEG32LCq7Ehbq4NNuPWaQrlqKntJodi1G/c7OwjV+NZ6+rmuTCytDduRCr9RH9EFNckhoFpE9QzpEuyjZOfQhxMEUBo0YWdSKx2l2NMHWOqFjcLnN9sT1X2QtCXkR2zBWIeSre+6IELGYJ2QjXFoKGhbeDfOjKQxNUYwQ/ObzXwrHryzITydZjKuOfpSSqh1wEwXTtxgDF1FmJeJpJ1fLBmMAxgu3O5cjj6y6B4T2GXcaHDVsptO0R4GSYxqVuExd5zDm6sPsFHh6vnsdSQUCUNkhowpePQ2V2lP6tQdvc2UnXoSumILCvNYPEQJ5xC+xJUNyeDYCSn4ZEbyXKx0IeCFaavXm0PA7chCsYq23+ts2Upn9UFb3snr9pVZ0OUQ4T0m8HrHwwnBBQU1XvOz0yAAK5yejE5IdGPb1uEPVq0QiV8LN7InjZh5MJBk9pu2asC80Nm6DzU4u9lO9iO08cQS/RzfJf7asuRqgNR7f2Zvd4LXd2WKsthlW+r1ia+sg190NLsdo7MohYNIb/jY813cc0g3Usj+cb6c2eoyHsNwxh1vq3MVGZ4ucrexFd+kzhkHVVoJ3Q/17OpurUExNI6UM1naUEnxadr0Z8dqRuGKe3gkqeGMtL0N623WnD2rnW/jGWKGtYcwa/PkIh4vNRniakU+C7bHZjFxodag3M/hySluLq2cSPumwhxyzHiTDHr4Vid9fxP8CwSXshrkO7qTiTW69Q8zRV6kYlZ4HQWFw76AYOmYw0xcbiMFwzdsA8scltry3b1t1kd4a8bSxTSFaUNDnfegXZwhdk0jPvZb13F2II11b5MFqrvdbjSzekBJFxOBGUcXaT6DASUZml1JSjzG3U0hiaPTwQn31SlpN01b2lVWXS1SghDPvPJZrZ4f0tbLsdo+wUpwxGMzDdoHNPlJ6lTmRkj9ytgO87EQyTDfSaXQjyFcnQhCpsITVqXkuLNIMGD7+/wgnRl6L7XUnVWbCqsUfb/ZmCHtHlU0mEmsVZJsTe7TOiSt8bSuw8fdg7otiRxtOhh3SCyBYhSp6uMsOWHRUMFmFswaPbpeRnJ1GXD3Sw/1oYQit2PstAle2We+BsHqI4bqQ7TUwcxWOUlmvN906EYsdyqWKYWhCrzjC0Yj57t8nR7MeIIv95MSHO75ndcOmN+09uBsRF72xri9RsppzYogsahAstX4wfravsMbn41JzBm8cyJvh+6gVvxmP1M1XqOmnm87dA0rbIwFqhNe7e097RXWMTiTMI3TJmLliDBjaG5HcXM/bAM+hpSuzScYQbf9TXqU68ij3OuJwtjTeMvQlsc0L8pGK30I5pnPt7wemDsaEeuxtGzfiWD3jnJ3JvLth1apnduJt64+oaaEexTmH/d7TXNhYz5QbKAeJDKwwoujOZGKVIMpTvgetukLT2RlEXgtBXlg4jZL02uzddtyl41ZPHxlOGetAMmoyJaSNEYJL0SOYp1uzs27jJoVtwVRd4/wRrLxWVPJGm7udSRqunShtuEjk29tFs2cYMg2ohK6PV4YaiKvDSHyHnQk1vRpY0fmeYicrCYeNM6I+oZEDvCm2VzwEMqiDFVKilwr2HHuGgwzjnSHC20yViZZ3GR0oKHGKJSMtDsODzi0hlrex2izCbobMgptNTp6c1YTBWLXCddOrImrQSVhSJfwm/NgQZfCbM7joT4ft3v3QDWUrM8OOTwmGEwOpX0rnRnKlcBNmbVxTNWOs2W6PxLHcXvRMqGBvdwPIfRiwZsCj3VpUtrD6W4GmSiVV+QE8cHWbzyuFSgtuCcXjLiuHc6SzqdQitiMulHyfu+Kl7EMIU1nKfl68cVZjyTlMhzm3F7fhO4+TKZittJ0kg2kpAgYlUdvpEIsGmNR26BRkD56bmda1k7pfUo4DIhOHDYavY0aA2cQJZkfNuyZHCygaz+36VJkicOw24T7qKjQApOs0RvEUqT3slREW9UfZCTH7Ud0lip/Lu8DRV8vsmwX/eFC89tj7kyEfz4PGgIiDSMJMb8cyKvnH6OoFjeTUATkmvetvPc7RYHS+JzYIr+Pr+YG8UcUwal+Ou59AoTeKb8JCGefE8KIb0cuzsM9eWZbLpXQ0D4Cx+8fVE9oyCPJ/VRWz2GF2WMg3OxBpQn+YMANuUe70wOWhnOC38mZlCbKg5t+7lloZO68MeupTIuPKhbWtZSFp+0IR3Bwwzl2VpEQ1REZZiSbw318DkkUxcY16M1PJBncqzJy8MJia+jWjmdC37Dbgta2LhxqJDsSU7IW19yxOFEqxxtHfi1yjgYd2wAmDfLADB0bzdBF3I8Qzt7R4ap05RXbBnlqrA8M5uyrHToGiFNUme+4CD211OES7iBGOxN4hjD5+RRp3L6u0EMgMrtw5G2yz9GN93BzSEra4ipmAovswlvvPh525ZBOzcI2byDnabZ5VH5Mqn1a+1ioO+sg2nU4atMikY6n5rahI1JzIKBDgUKwBLLU28pwZ7EDQVE0h4PKf70xeFJSbeKjlO0cdHtrh0dvw5nNFUyxGxemjR2gCyfuiQ4buztKmGrH7lq6baR1QOCg4VREEZYu3jq9XA9YdSE3EFxgnitQY0pPu9kxIBK0RTgcHC+nZltikwb1ipZzO44oLDg7CqKjMbpq69tcrwy6TrYGmXZtWWWOEfd4oD82DWgC4+5iIvmlPXUJbPGEpvNeFtwhXNtU+rbbQHM5+VjUQc6VTlW7qnc+gbv0oxFvV0NlZysrGOJ8UtdkaU+KZEYsJJz1e2Hp1kQyY3P3lOzSoTeA2DB8gNlGO5GM5T6gnM2IOkdbVD0dkFtyk4VoS96hg3MBo5muqIMcnViY2mZk7fQxzjEM85e3D2+/Hd+9/ffeJVuOcf6fnSa9Dn6+vTXyPJSMvPDzk9fn/6Y8f/3w1gUpkOZ1VtYXY/x+uPR3J2Uf/+VB47L1/nox69vp8usofPDi5S3lt7QKx37o7l/7uni+LQJ2+GO/vNzYL++/BuD7D+ep7+K/Le8ZAg2Xd7K+DvXX97cyn7eXF0GiMPWG6P0yfj86/PAWvr+L9HVD4F+jrln0fH/rAKi3+YR82rz97f8Ck94EZ08uAAA= -->
