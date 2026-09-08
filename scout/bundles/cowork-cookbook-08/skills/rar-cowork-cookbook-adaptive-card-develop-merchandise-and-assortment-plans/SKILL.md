---
name: "rar-cowork-cookbook-adaptive-card-develop-merchandise-and-assortment-plans"
description: "Generates a read-only Adaptive Card JSON file summarizing merchandise and assortment planning status from Dynamics 365 F&SCM, with header, 3-5 KPI tiles, a RAG row, and 2-3 action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_develop_merchandise_and_assortment_plans", "rar_sha256": "e474373f7da6c648c5ca8a79bdef8040aeb6f42fbbbe12eeed03d27f85466486", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_develop_merchandise_and_assortment_plans`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_develop_merchandise_and_assortment_plans_agent.py` and in the RCI capsule.

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

Develop merchandise and assortment plans Status Adaptive Card — Generates a read-only Adaptive Card JSON file summarizing merchandise and assortment planning status from Dynamics 365 F&SCM, with header, 3-5 KPI tiles, a RAG row, and 2-3 action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-develop-merchandise-and-assortment-plans
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
    "as_of_date": {
      "description": "Snapshot date used in the card header timestamp and output filename.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 F&SCM legal entity to report on (e.g. USMF).",
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
      "description": "Name of the Adaptive Card JSON file to produce in Documents/Cowork/output/.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_develop_merchandise_and_assortment_plans_agent.py` and embedded as the fenced Python below (sha256 e474373f7da6c648…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_develop_merchandise_and_assortment_plans_agent.py` first:

```bash
python3 adaptive_card_develop_merchandise_and_assortment_plans_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_develop_merchandise_and_assortment_plans_agent.py   # or on stdin
python3 adaptive_card_develop_merchandise_and_assortment_plans_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop merchandise and assortment plans Status Adaptive Card — Generates a read-only Adaptive Card JSON file summarizing merchandise and assortment planning status from Dynamics 365 F&SCM, with header, 3-5 KPI tiles, a RAG row, and 2-3 action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-develop-merchandise-and-assortment-plans
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_develop_merchandise_and_assortment_plans',
    "version": '3.0.2',
    "display_name": 'Develop merchandise and assortment plans Status Adaptive Card',
    "description": 'Generates a read-only Adaptive Card JSON file summarizing merchandise and assortment planning status from Dynamics 365 F&SCM, with header, 3-5 KPI tiles, a RAG row, and 2-3 action buttons.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'design_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-develop-merchandise-and-assortment-plans',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-develop-merchandise-and-assortment-plans',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '9a3294d6ce4580c7',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['design-to-retire'], 'process_tags': ['design-to-retire/develop-product-strategy/develop-merchandise-and-assortment-plans'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'design-to-retire/adaptive-card-develop-merchandise-and-assortment-plans', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'as_of_date': 'Snapshot date used in the card header timestamp and output filename.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 F&SCM legal entity to report on (e.g. USMF).', 'output_filename': 'Name of the Adaptive Card JSON file to produce in Documents/Cowork/output/.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives any consuming app (Teams, Outlook, custom dashboard) a single canonical develop merchandise and assortment plans status card so different surfaces always show the same numbers.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, produce an Adaptive Card JSON file 'adaptive-card-develop-merchandise-and-assortment-plans-2026-05-24-card.json' that visualizes the current state of develop merchandise and assortment plans. Include: header with title and timestamp, 3-5 KPI tiles with current value + trend arrow, a RAG indicator row, and 2-3 action buttons. The card should render correctly in Teams, Outlook Adaptive Card preview, and the Adaptive Cards designer. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates an Adaptive Card JSON file with current develop merchandise and assortment plans KPIs and RAG indicators.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Generates a read-only Adaptive Card JSON file summarizing merchandise and assortment planning status from Dynamics 365 F&SCM, with header, 3-5 KPI tiles, a RAG row, and 2-3 action buttons.', 'example_request': 'Make an Adaptive Card showing merchandise and assortment plan status for USMF as of 2026-05-24.', 'inputs': [{'description': 'D365 F&SCM legal entity to report on (e.g. USMF).', 'name': 'legal_entity'}, {'description': 'Snapshot date used in the card header timestamp and output filename.', 'name': 'as_of_date'}, {'description': 'Name of the Adaptive Card JSON file to produce in Documents/Cowork/output/.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a shareable Adaptive Card snapshot of merchandise/assortment plan status for Teams, Outlook, or a dashboard. No data is modified.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AdaptiveCardDevelopMerchandiseAndAssortmentPlans(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardDevelopMerchandiseAndAssortmentPlans'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'as_of_date': {'description': 'Snapshot date used in the card header timestamp and output filename.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 F&SCM legal entity to report on (e.g. USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Adaptive Card JSON file to produce in Documents/Cowork/output/.', 'type': 'string'}},
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
    print(AdaptiveCardDevelopMerchandiseAndAssortmentPlans().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/9V6+fObSJbnv6L1RGxVDba5D3miIxaBBAgJkBBCUO5wcYM4xQ019b9vIn1tV3VXz2zPzC8rHwgy893v814q+fWd07VxWb/79E4PnGIlOFmWxEG9cgp/xZVDWafgUqYu+LfyyqKtE7dry7p59/6dHzRenVRtUhZguRAUQe20QbNyVnXg+B/KIptWrO+ACX2w4pzaX+11VVmFSRasmi7PnTqZkyJa5UHtxYBf0gRPtk7TlHWbB0W7qjKnKJY5Teu0XbMK6zJf8VPh5InXrHCKXO3+t84d36+GpI1XMWAb1O9X+AdyJWvSqgWcmvdAnjMrrOpyeP8kj33AV463SL0CqrRl0XwEygSjk1dg+rtPP//1/bsEfH/36dd3XgaEAcp9VWPRgg/6ICur43ep2cJnv8msAZEX64BLBFZWEzBvAe6roA7LOgeP/CBcvd392ARZ+H71r/+aDk4dNT99+lys3j6f3y1/zl2xauNg1ZZO0wb+ynMqx02ypJ0+rthscKYGGLvt6mIxewO8U0QfXyu/Uyqr1V+WsR9fTD5GQfvj53dltbgLWOHzu59WZQ341d3y/eNCpfrxp49ZOQT1jz99p9N07j3w2oUYkPrjl7f7N7Jg4vepSbj6omtb7o1XHXhJFQDiv9Nv+bxEfyP3ZpIvr8k/ltX71Z9TXvT5C5D3FX8uoPvnZIENwMp3H+9lUvz4xqMu+6BwCi/48ad/RNaLAy/Nkqb9f6L784vwK/R+fDPJT++f7vvrCnrT7RvNf8x2CfV/RhMw/Su7b4b6R7Sfnv0b0llSgFz96ss/JfdnC6C/rH7+h7r9Rwver8LP7/ggA1lUO24WfFr9+gyRn3/wvz/84a+/AdL/KRm97GrvSeFL7hRJGDTtly8//9A8H//w159/6CoQxYGTf+nq7M9o/pldn3z+YMG3WT/+cS3gbxRpUQ7F6lsOrX4tq/9V//ZxdXWyxP/+vPm0+n0mLh9otSjxlenLBL/LxgbI+js7/vTuN4BGBdCme0LWAkb/8i+rY+LVZVOG7Ur3yq5dAQe3SR4swl/ipFmBvwtq1ACq6iYBhn2bB+J/8fAicRmufvk/3hPhP3hvCA87bzj3xQNA98V/Id2X3wH0F3D58h2gn3HT/PJxdQHcyjqJksLJANxq2ufCiRYEB5JUddAEdQ/Qy53a4ANI8g/Ll1VSrH75rzH88qT9sZp+eSJ68sLIMyct+Nh0WfBxsYQZB8Wb3h4obcEYeB1gm5UekDF81QYgWpmB8tQuVmvSJMtWfgIQCJS46UkbWPbTQuyXX35xnSb+XLwAHV+9al8DgwnfxFl9+ACUDbMkitvPReDF5eqHX3/7YfXvq/9o1ZP4wkMDer75DUj4LJYgD7tFb+BSEAQAZJ5++/W3N5MDMqDqroCXkzAJXotBHKeB/9X+ush+wEhq5QbA7sDmeQUsuVTUpP24ksLVN3kB02VoqSNx2bQrP6iCwg8KbwJUHaDON0sWZbtqQLA24fR+1TXBk+svbu08RcwBIDjtL6sjp4GqVWbgv0XM5ySwuCwSYP5v0fF6DojUPzSrzVcSH1fKErmryqmdKq6dNx6h8/ILqFZflwPizqoIhs/FUrKDxVTPNHqZJ1p6ksR7c+mHZ+fhlaDzKPzmK+/orW/xV5dnja0/F81bijj14goPlAzANOoSfykc//YWUk1cdpn/tB+QdKH05gX/zSvPGHxrFv6zHqdZ6a8G54/90ucOQ1Bi9f9za7UYgRWE81ZgL1t+tVUuZ+vlnKWbXAR5NaCgo1mBCH0l4vcu5yuSfQX0z0WWgEirp397zXxq/DbnBZJdDTxwZs9P+iCegHMWus9wX8K3rpdEcT4XXyvHosUTJoHUABtA7iwh+5XhMvpV0hgAwHL/vYt4hgewPlAehPSq6twMhFsYBL7reCmQanHXVzeC2A+W9B3ixIv/oNUKUAchBuivgBAJSEJQXT5+Q/PX6FfR/7Dw1SwtS56NZAcytn4SAHIEi4CLWxYPAvHaV/MO9Pz0JALUyKt20d0FOQM0fT0M6uDRJU3SLg5+2TWoAGJ/WK4vTZenwViBNAHGAslQdcC6z/R5Bh0IFSADQBCQTXlSgNYAGOXNCE+CTr5gAcDat971RfH5+E2h4JlzS037unBRZFmztAmvYHWK6feQcfmzMAH08mXGk+/fRto3bgvtBTYbAH2A49fRVz/x8dUSvHqO1Ve6n/5ud/TjP7eBehZ5448B8GkVt23VfILhV2H+Wpc/AtCCX7I232r0h6VkfngrmR9+l+kfwOXD90z/8ASYP3B7GeLT6p+T+A8k3jLm0wr9iHxElqHDW8S9fYCBuA8b6wOxjH4uzsF3oAXsyxyE3OLOCTQF36ri1ymgNEZ1EC2TX1WyWYrrAOr5sywA33wufp8CSwou2kdLyDbl76Dh2R6AdHi58lv1AkNFC3j7S+MZBcsG8JkwTfDuU9Fl2ft3AAeD/9rGbyla+RL6zbKDBEkGWrs2CZ53TvOlDL/4QLHl7o8baL0AvUsMpFuGl5L4rbFZHP2GwM+UAIidPzPxLfeeqi4CL3q0U7UI/toLLt3jE73G9u8Zqs8vTvZxxQcAKbPm9ynxVt6W8v67zH3ZGtjYA1q9f0raLOUYCLAovGS904A0Ahn0p7JkwKnZF2AskIR/LxD/reqsnhNXr4nPDuLZnCzo+GPwMfq4MvTj7qc/ZfGtk/57+iZoTBZifvlpqdHv3xDw/bMWvl9928gAxd62ls9fBooO7Np/XjZRi3efS5YvYA24fFv07QcRN3j31z+T6+mqL19d9ffSKQv8gfKw2Pkf1XYgPBDA77xn98yX3qs5hF9pC794wH9iFyDAE9ZBcVx0+W6k76KWz83fIipQrX39VvHrOxDJAHBa5y2W33YPYDpAwQ/N0gnBAAEAQ3D/ylUw9j+0r3ij2sQO6GAB2YCgCZzGQ9p3KI8iGI/0HMah164fhAxCIE7gUiGBha7rBigWgCqM4D5GhwxJUGA6Bei9cODL0gQmi6SLmMBAHwCUBN+HwSP/TcWXSov9vm1jnon80vTXdy5FgJki0Ujs68PBa9SFbwd3rG9wgUDjjkSqybK2t0urmnBNXfLLft3fA6y1rcu9sbOTyg/7g8exp9OB42zUTHJ+vS3ovYb4DNFpUSY3sYrPHkKcxoOl3Xos1GZ1pAhvHHNv2jb23imsKZktSBTKdnMhtgfa1G27t+3poGj7+8EjJ22CEJWt18ouuBnxDCbcIcYN4IT0pqzKQ31CmdRI4YKzx1btjtAamlsM3urpVacEmV5fNPQ6mj2NlnN1F53DoZfTB0Jg3g26RldH0+q8ud1Hitbu6KiMVSgrmLCxcwPfllB2Z25QUSO6moWnLXwY6CDJJ1KoOXKzVsUhhaedoSeYeSaRvME9MaLU28Fn1qFYo3CYyEGPFzBdtLdeWUtb/Txe8pk4u+T+WN36kav35wN5NqMzRCXr6/kIDzITRlJrkEpN+GfhYUN+0SXnQsLoK3+UWYlJ5It0jakROq837nY0bZMmMkMdsjzXpQdfn6E6808kHWx0uyqJe3WI2Fqbq91DxSubcYtpXfrrKstmGZMYnrsaW07XtfsJHvpdLMgxW8uemonoxO7XkvGY1qqV5Hrm3p2HwF+wkmFJcxRb1rAMPoXqXJZoHm/neqgDk1QGpnxkl/Pm/Oj2snAo40fAb4y8SS97yR2O8DwfdzeT4z3K2sC1X12qNoDqgts1KJ97achR1+slK1EGjPiH3EUSv0/PtHyn0qMXRZUcyki048M9TauYv4nEbsPGvHzDru6OKxkevyMXhg5P3Wa9IzYDlfRmFOQPnI3hjd0IJ3JbbDUCx7M1O5iUFdKMPvNcuTuh7f2UYTUrIy0fsFmH29fa0FNpvIbOYbdvdjV5TfzdLr1LtzKa4aSSH4UyFrshw04GlJZNBsfB/QgVIpHcCGNspCKJsZjk7UblLhdpvWHoDhs7P0mhoCqadc4azJHmB1w/WDOQNIB8d1PR3MbblI6wT7Gb+JDvWNEimSqkgZ2co3hmzIJRkswiyeSA06WGsz7BIH5thRbMqT4BdTNN+T6h3qICHZ3qlJUU5h04XWroxh/2onl6zKHZiOqBpHAjR+eTdWMEyG+PfsjqfaPfK1vhEB+WEKwPHH53KvgTF9E23woDzrmqREzWTXjMdxFJtmkuY7F58i1N4xikN9aXebiig+bEssrzxizmp6Zg1goydfOxEZTCagl+x90CvmZQrHqY1KMyyL0ga3KT1NQ24cd1UOuydr3oiC2jQxJK90TzY+g8XI4mXWReD1VsrG/tq8Di7uaG74+y66fzvsUYLBVuDa3B7k2gNRW0U0euqt3Z3wAvRkRh1VGjsLKExkR0ZNhCu2il7q+d/OGJqbx2RpQKgiML0imjqnzPncb0wR1qprdcgz494swaxOkWTTrhHSY0YZmgSbG1aArF8TEWTBOyD+32IFJ3hMpGRxONS8XjviqMopn6x8k/JOVd50zufB6iStnMJNpMkFLo6FQOt+5ulS6jV6iZeowhCoOzNo7bDTNAA1fESZa7kXtnsOEahA0X8ocJGw9mPNpCvqWdSeCoYSg8aR8N3WmdXVOHIw47yzAETznWt8MNSh60akd4nzfH0pJ0TYTC3W2v97N2186Gc3JvjE9HcN3r5L3HkTs3TQnrBmx3UXTnymgb5OqQNR4E90CH992lIB2Ain7L7gJx0znRHCmI4aj27V4GBoOg2xp1Tii52aebxy2z7pHTTNN2gCpkTwrXfJM2lBa7Wh/71lmakbFhmkO7C3hfQpoHN046pqdbfFg7PV436c21yyx0zuU5q3jXVjP94sFlNUpHElVPmZ5db/0Bq6IsvRKJRR0I/UjkTSPn8rgB8eyv2brTBiRxdife2dZ9uN9cYq9Y31S7rtntTkY8losj5GAKGmo1uYMivNCebgJIwsMxdw/yrlBlwXTgULwy4RG3GWaf8bK9b6MCUcP5sZEVXIOs8Zhhd0TWbMuG6AaWmYDQhCYmEJrjlY46nUJ8E8KXgUchER8uE8UEcDjyzNw+rkVwNowjMWuQ3Zwsdj3t3YH1J4bhji13w6/Ow+SkaP+Y+yBWS9mR+x4ZlKvXb7fBfQ5d6REQ1Fks+JtUwbv63LC1WRE8KnsCxZ0H40QPTaTL4k5Ujv3+nk/+RUiQ613YmjmeCTOSe+MxvWwiePJYUV/na9zNz0FjHySkJoZ5mIiAD5oR0omsxrptH5WccYdDRnLoi0h0s8RhcX5BY6tMsB5GjxI7pRB2OpGRdSriwy5t6su8cx/dGQ7vCAKd5HmTXEluZ8VSLqqSrWIe3VFu4ia7WJYFbRi7shfYTBfGguD4lgomKyN81emZ9nAMGRPlWf1UjhebqmnqqAXngZPgXbI2ql6pWKVBCG0DQu+xdx6nfdIMEwryQtpkOlHdI53pSM4FhZa+jd4o7vut7rX6XmT13Tp2LnvCD6WiMeptmO1AQjbaLRaie2I9orhaX7Mg5spzM8twXuYzq0TigT9cawcX6tnejzIrhIzFZfH+LuY30r+ZUCaSqhwkurHvUbf3j/41ZeHeRHYsduZmC+OoezqGhesgVz5Fb6pquvsHJpzTx8MdTJYtCzVwmGoPWhNkG0NxmxRH4zLdz0iI2BwLb2IJlBuDOdj7Pu3HHZtvoCI3yocNeBqntXWl42sS34ZeOW0e2hHUmKQ4ywfOPhQ4F4CA9+/UhXGIVpJQ7oI0ITQVUrQhr34zxbEmXLXH2GRbdG9YzmPdH8j9oNCY04BYPc7DjOHuLnU35z2rk008wQ3sn85ufQ7L8/Wox6RNhdqdYfzjerQ1SdB1xlZqfxewyI6YVEQT6uv+lHXWMJ3OyPW4j9rzJrqQ/vWg6qb/mG6pbm0ETnlElGPcbRtTLz57UzaxT5828F3aNmMTS8HBa/dVoznINrgVmmkcppgF3aHmgg3IaWjUE4tox8cObBhbL7dqPAVeZULce/DCPqIgHbkf9v0lkFkjzj1KzFHV74qHX14m/ijp+cbenk1EEaF0XLOBJrum4txMoSPcBl7D6jbnon5zxcZofcQKmWbVdXjuD+kwITfJ1jr1LBvmlWXSHTeOV6X19ZNDjbBmBlvISZvHuNa3dzn3k51QOopus2epYQwrabGMdyqIzNeKqgloRg2lVzX+eCPl3DajzSDHMZ7fL1fRa3qjUiiTxa9tF5HmXswxUdxf7VZOhfQ2HzauFXbBYWsfeAWNNVPO+JMlC48jBhLF1EU2tEjLcKPNuTjHRPtwHgUJpfKlFfOKE66qLRzt+ubr5hTA2866+pdtlZ7UgLU2IpJhNFF3MzrBwvmhMxsK9tj1jjytI56f1IC/G5uToqSifdj6oNwfmpuGNDuLzKZMgDCUKs7mJbtmN7g6D87EjIrsQDh2ekwURirFoPA7iofjzTrCtMRm15fysud1du6vaW5tzKo/caPvnZWS03O8Okr0GvQ9OnJA7+Pke6VKeBlRW21DnsKtUVwyej5XjFN3TuPu/CjbNdf54DTsXPYRrqaILZb5ziSO9w6V752wbUPdRfDTDkvWVWt45/WZrBLjgV+FXmOUm09juK2c71M1b3jBP8aWRqtQcScZRuNcytJEBIAKg5wvqR2zvpwi6ysOOYmSGMJF0B6RJykQWVM5CZoQ77w1JUhg47GMr6TruKa+U6vZz8fqVjeNKtXDhTsmmJ5bhK0w0KneHUzOVOnaQvM5Fy08QoatvhtYROcg9NDvdlWpoqiI85yvT7eWK/pTaRkVL5wEZTuUJ8o81VeL9nNS3hwSgTQfDh2QrdwdJ3tfPsTLdp/46/aaSnubloUZV0FvNtbZeLK9xFZw0EDHmSL7aBXomyLawBqPW1Z4keo6Qe9ccxJwTW18l8AK9ERWiA8hO5xg4fgexWU5mpY1KcctUtGkfe8Pj22XtlDADXLkEKC5E24XquiVli/jKKdFWpm7MWYw0h5qZOQrO+XKwEyDSG8yMY0OSLYZ3bSt+ZNjS2bQV4R5QHIrVS5GFrakuu37Cj0iLIonoGjqXKK4GU3vZkQ6QTHM01ad5cIp3mWpZHGSkKEeMkCCYmaXBre2UJZvemvOa33aTOtUXdtMzUygT1HP19Dr14WS7az1tRMLhe+jQEpBhGyuipj39QyAfq1R7qyrpA5Np015YENvwuWDcYKCYCr7+OT47f4EQ4OJ3vzL7j5PFHHZ7UxGHwFuHC1bOJ9ibk4TgjI8jAyunpMttrEvgllDIiUXh8qCJY0EzSiEAFQg/cBLUUx6KJYu0Ch7Nfa7Xu73uguatAB3sa51b8Z5CK7nkt5fBw/VTab2AL4Muz0ymdZVM1HNisz1bcdXKIDxOLu7gxoZIYsnMB5XsESJm/HBoROeR26WmyaKyZd1V2gCxg83zYTgm3gu2ojQ1fHo0nQ9d+x0pwaB8m/xpXdCp5DIaLt2oOM6DU96XszifvZboyJrwhr3RsuulbulBg1FY+uru0ZgP+QvjpfCYproHkNddTFomSSUja0wXjgboUSh4gkq8oXkynUHhkhLHT9e/GwLhSZp40yY3HKRrgzlnBG5K9YqGtPbWKRj0+hm6oxp+SXA7xvL0cacOOjlQLcwCmsHdo0WMAObMLGBVdWopZCBjzfGYTYFb3HYka5G2wzrmwG2Tql620bdBXFU0WrlodshYKNjxfcMPtGpq+7R7kHlXtHKfmNvYzo/EBx3EUmxU0GXuS+grMT3j/yau3m4hXdk5lyCS19qwrjbSEfKzyCTGexZ1ATpGKpC5PEkPUdnlHJcLMqVZGymlD9zaM/ClyL0s6uiEglHdtJ2Zg66u0+P5hSBHdiDmc5qUBDFfN7juEvMhqKAfpAmHof4jq7lpPRpo1PRzB8lF2rCZsBuPJRhA3PXWSfVNwQwgWX72LUY7+H2LNwNNHtoDbd/2HuhwXiwDbk27QF2dk7jXOWaRzYl3uZ7sYXt+No30sTHBdHY6dof3UTGBcgrdWIsSUu3xiBuzokn8JR8Rog4NfKTA0ytKBeFokArN1+Q7JZv9lPF0gzZnVvbgDbITmHzsO2to+hyV1o+7lmytUeGCHCZzW6KLNhEtg5P/Qhm8CNE1XkHbUWp34VestvDQU4j+zmFfDHfX0WIOkV06oux7RuYCOUDeR0fbYfmoVjMrcjayIM5oboH30+IgpGmdK+HY0k6h8QSgrTZpdi95uiSFkzLPPGz8/DzdUsfrXbtbTDMvh3CnLc7UuJElTpI87AjtoPbjmc09jc+AV+h8XjjC3Fto5EWQQ5gXs/4jS0U1VYeD01xyv3dVlWl6VBHrS/YwTIEy3JsgjmeIa89UetgXcUkZ2wMc80pOJ7dR5oFfUiIx8hlVxK1FPATMaAidg6NB99dRZPCrJ1DxvzMt1ApXZSawOsbyvtXUnHWxNQV1yDwM8NXZ15ToBDrbl55a4ikKm7BGG6601UVz7U6aglUzWkRHmX7tut7VDcyLwwVS+wrM9uI95w6yRB19Lt4dAx0pgJ5YPbhoDKSYbJqsG+rwDBJT4Io9FHg24cio2Mt1GWmsUWs3fRAAy1aYK69LQOskjNBtumbkZ2SzdXOT+uTU97Qujm347AtZ2DoTMT7uNiFKBlY7LWZKptnGkQ6+4+CCJuo2CN0HFUxLO2OpaOpBXkarvv0jp+Y4XrbGpMzyWf/SDNlxBMeNGGHSGV2+UhdnPPNRPRexjfHu1q6EmPryJzfYeuxrusBjymK9XnvQE4HdZDiLORO+OVGlDZZ8IzbxdNxnloKLzX+jtUMlivQvn3g0mE+yjzqOmhH6euN0h6GYwWtHakR6FGYsgCfz62MpGRG+yZWO2PTuqSOTVfkvreokTJVV+pBoWwUJ66OnTLizEEabARCIItZW3Nv72USfwjYfuPesFu2PpU19+CESwRlvQSDSkTTduTo+HWazLXq7ctt2fJIsQl0d1NSp+Bwv8ZbsLl9mKY9FNo0V/xF1dpWKtc+FlYmiXG0icB4eRz2sIdcFD8soJ3R8nSGz0wcE+hat/ObSEm8xB92glQjN9BNXs6RoyCESq/p9QSng8jBOm6LJ54eK2PO+oLHe9dN6KtqTVTo5lePOvUu9+DHMbx6LXKvr91N4fzzGuUbma500bgZmQl2wYykSIhmGKrPU1g1w63Y9BMqH7DDzJJa1kVeW+PImhQpDie3aXtnlR1nz0pdq3sb7HiyKdQ8oeVz7aSdJKELDIitdlFhHBNnT2j4RLBL4DOCHLqK0l0alJyTe7YdCWgMQA9rE+5cVx069GVMyqpddjGV7RjhcQ8ab689qLjf0+R06cpaLW5XzB1cnwghs/I2dH/ItHV2AAAGHk9E6AiRzwh8J6bhcNAv5zXuHGpKelySR966iZoWsExoHdydRfkxhQMDO51BgcbF4OrBoxO8ztxOc3C2Uo46c+vJRGg9HCDmAcvXcFOZIqbxYt8746GlacKuijWBRlTUufcNT6qHbXpiRaMuGLuKHjnL7amH1CRKmjSU5sa44YfbDrWdSSruHR9mzSgghc1iRituYEubIl2fBBulpzMuJ7Bbri9+jg3xbQ3B1A7q96cIHucLfr/UAZFBblyKEmhtjuitWwebOtjNWgMa9b3JZQaoDBRbxYNz6N067/sdDjPHcPM4qThrVDRjxzVZplONaXKDwEkvIbofqnFC783RkGcG5e9DAG+Ok4vqvrpdjkb+8pd37999P/x699988Ws5q/kfOxZ6ne58fafjedYXOP6nJ69P/11B//r+Xe0lQMzXMVkDcuLtaOlvDsk+/NcO9hea0+u9q68Hva8T7NaJlreZ3yWF3zVtPX1pyuz59gdY4XbN8rZjs7wQ64Hr7w82/6Dw61QziYovbfmlDtqkXo7JkmJ5syPwk+Ug+3UbvZ0ngvlv7xB9wSnyS1BXiwXe3hYAiuMfkY/Yu9/+L0q4Byp4LgAA -->
