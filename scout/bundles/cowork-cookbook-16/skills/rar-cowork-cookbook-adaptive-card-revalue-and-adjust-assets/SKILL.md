---
name: "rar-cowork-cookbook-adaptive-card-revalue-and-adjust-assets"
description: "Generates a read-only Adaptive Card JSON file summarizing revalue-and-adjust-assets status from Dynamics 365 F&SCM for a legal entity, with KPI tiles, RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_revalue_and_adjust_assets", "rar_sha256": "024b71b469273cb2ec84808eafe026d9469d3f9f5c67fa9d9225acf7318b2e80", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_revalue_and_adjust_assets`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_revalue_and_adjust_assets_agent.py` and in the RCI capsule.

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

Revalue and adjust assets Status Adaptive Card — Generates a read-only Adaptive Card JSON file summarizing revalue-and-adjust-assets status from Dynamics 365 F&SCM for a legal entity, with KPI tiles, RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-revalue-and-adjust-assets
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
      "description": "Date used for the snapshot and in the output filename.",
      "type": "string"
    },
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
      "description": "Name of the Adaptive Card JSON file to produce.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_revalue_and_adjust_assets_agent.py` and embedded as the fenced Python below (sha256 024b71b469273cb2…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_revalue_and_adjust_assets_agent.py` first:

```bash
python3 adaptive_card_revalue_and_adjust_assets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_revalue_and_adjust_assets_agent.py   # or on stdin
python3 adaptive_card_revalue_and_adjust_assets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Revalue and adjust assets Status Adaptive Card — Generates a read-only Adaptive Card JSON file summarizing revalue-and-adjust-assets status from Dynamics 365 F&SCM for a legal entity, with KPI tiles, RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-revalue-and-adjust-assets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_revalue_and_adjust_assets',
    "version": '3.0.2',
    "display_name": 'Revalue and adjust assets Status Adaptive Card',
    "description": 'Generates a read-only Adaptive Card JSON file summarizing revalue-and-adjust-assets status from Dynamics 365 F&SCM for a legal entity, with KPI tiles, RAG row, and action buttons.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'acquire_to_dispose', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'verified',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'adaptive-card-revalue-and-adjust-assets',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-revalue-and-adjust-assets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '07b946f18740ca43',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/manage-active-assets/revalue-and-adjust-assets'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/adaptive-card-revalue-and-adjust-assets', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'as_of_date': 'Date used for the snapshot and in the output filename.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report on, e.g. USMF.', 'output_filename': 'Name of the Adaptive Card JSON file to produce.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives any consuming app (Teams, Outlook, custom dashboard) a single canonical revalue and adjust assets status card so different surfaces always show the same numbers.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, produce an Adaptive Card JSON file 'adaptive-card-revalue-and-adjust-assets-2026-05-24-card.json' that visualizes the current state of revalue and adjust assets. Include: header with title and timestamp, 3-5 KPI tiles with current value + trend arrow, a RAG indicator row, and 2-3 action buttons. The card should render correctly in Teams, Outlook Adaptive Card preview, and the Adaptive Cards designer. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-25', 'what_it_does': 'Generates an Adaptive Card JSON file with current revalue and adjust assets KPIs and RAG indicators.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Generates a read-only Adaptive Card JSON file summarizing revalue-and-adjust-assets status from Dynamics 365 F&SCM for a legal entity, with KPI tiles, RAG row, and action buttons.', 'example_request': 'Make an Adaptive Card showing revalue and adjust assets status for USMF as of 2026-05-24.', 'inputs': [{'description': 'D365 legal entity to report on, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Date used for the snapshot and in the output filename.', 'name': 'as_of_date'}, {'description': 'Name of the Adaptive Card JSON file to produce.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants an embeddable Adaptive Card snapshot of fixed asset revaluation/adjustment status for Teams, Outlook, or a dashboard.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AdaptiveCardRevalueAndAdjustAssets(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardRevalueAndAdjustAssets'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'as_of_date': {'description': 'Date used for the snapshot and in the output filename.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report on, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Adaptive Card JSON file to produce.', 'type': 'string'}},
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
    print(AdaptiveCardRevalueAndAdjustAssets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/9V6ebOb2JLnV9HcjpiqauwrdoE7OmIQmxCLhBCSoPzCxQ5iFYtYquu7z0G613a95+p5b2L+GdlVEnBO7vnLTB9+f3G6Ni7rl08vRuAUC9HJsiQO6oVT+Au27Ms6BV9l6oL/Fl5ZtHXidm1ZNy8fXvyg8eqkapOyANvFoAhqpw2ahbOoA8f/WBbZuGB8Byy4BwvWqf3F1thpizDJgkXT5blTJ1NSRGD13cm64CNg+dHxr13TfnSaJmibRdM6bdcswrrMF9xYOHniNQuMJBbC/zRYdRGWQM5FFkROtgiKNmnHD4s+aeOFvJcWLWDTfFgcGHFRl/2Hh0KONwu7ABq0ZdG8Ah2CwckrsPDl069/+/CSgN8vn35/8TIgANDpXfpZ+MNTSqbwmYeMzENEQCJzigisrUZgxwJcV0ENBMvBLT8IF29XPzdBFn5Y/Pu/p71TR80vnz4Xi7fP55f5z6ErFm0cLNrSadrAX3hO5bhJBnR6XTBZ74wNsFPb1cVs3wa4oYhenzu/USqrxX/Oz35+MnmNgvbnzy9lNfsF6P355ZcFsNjnl7qbf7/OVKqff3nNyj6of/7lG52mc6+B187EgNSvX96u38iChd+WJuHii7Hn2TdedeAlVQCIf6ff/HmK/kbuzSRfnot/LqsPix9TnvX5TyDvM9BcQPfHZIENwM6X12uZFD+/8ajLe1A4hRf8/MtfkfXiwEuzpGn/Kbq/PgnHILSBtd5M8suHh/v+toDedPtK86/ZViBg/hVNwPJ3dl8N9Ve0H579O9JZUoCkfPflD8n9aAP0n4tf/1K3/27Dh0X4+YULMpA3teNmwafF748Q+fUn/9vNn/72ByD9fyRjlF3tPSh8yZ0iCYOm/fLl15+ax+2f/vbrT10Fojhw8i9dnf2I5o/s+uDzJwu+rfr5z3sBf7NIi7IvFl9zaPF7Wf2P+o/XxcnJEv/b/ebT4vtMnD/QYlbinenTBN9lYwNk/c6Ov7z8AfCnANp0D5Ca4eff/m2hJl5dNmXYLgyv7NoFcHCb5MEs/DFOmgX4O6MGgNCgbhJg2Ld1IP5nD88Sl+Hit//lPaD8o/cG5UvnDdm+eADavrwh8BeAkV+eCPzlicC/vS6OgHxZJ1FSAJQ9MPv958KJANrOrKs6aIL6DuDKHdvgI8jqj/OPRVIsfvsnOXx5EHutxt8eCJ08UfDASjMCNl0WvM66nuOgeNPMA1UqGAKvA3yy0gNChU+kB7KUGag07WyXJk2ybOEnAGNAtRoftIHtPs3EfvvtN9dp4s/FE7KxxbOMNUuw4Ks4i48fgXZhlkRx+7kIvLhc/PT7Hz8t/mvx3+16EJ957IF2b54BEj7qHsi0LgfLgNOAmwGMPDzz+x9vNgZkQAFdAD8mYRI8N4NITQP/3eDGhvmIEuTCDYChgZHzqqzbuYAm7etCChdf5QVM50dzpYjLpl34QRUUflB4I6DqAHW+WrIo20UDwrEJQensmuDB9Te3dh4i5iDlnfa3hcruQV0qM/C/WczHIrC5LBJg/q/h8LwPiNQ/NYv1O4nXhTbH5qJyaqeKa+eNR+g8/TJX8LftgLizKIL+czGX4WA21SNRnuaJ5vYi8d5c+vHRRHglaCIKv3nnHb21IP7i+Kii9eeieUsCp55d4YGiAJhGXeLPpeE/3kKqicsu8x/2A5LOlN684L955RGDbw3As5F4hPDirU0xnm3Kn3udzx0KI/ji/8O2aFaWEcUDLzJHnlvw2vFgPZ0wN4Czs549IyD84PVIuG/9yjsmvUPz5yJLQETV4388Vz4UfVvzhLuuBpY+MIcHfRA3wAkz3UdYz2Fa13NCOJ+L9xoAxF48AA9IDTAA5Mgcmu8M56fvksYg0efrb/3AIwyA0YHiIHQXVedmIKzCIPBdx0uBVLOX3r0HYjyY07SPEy/+k1azZUEoAfoLIEQCvALqxOtXXH4+fRf9Txufbc+85dESdiAz6wcBIEcwCzi7ZPYXEK999ttAz08PIkCNvGpn3V2QG0DT582gDm5d0iTt7NqnXYMKQPHH+fup6Xw3GCqQDsBYIOirDlj3kSZzrOWgqQEyAKQAWZMnBSjywChvRngQdPI55wGmvnWhT4qP228KBY/cmqvT+8ZZkXnPXPCf0eoU4/fQcPxRmAB6+bziwffvI+0rt5n2DI8NgDjA8f3pszN4fRb3Z/eweKf76R8Gmp//tZnnUa7NPwfAp0XctlXzabl8ltj3CvsKwGn5lLX5Wm0/zrXw418m9p/IPzX/tPjXRPwTibcU+bRAXuFXeH6kvIXY2wdYhP24tj7i89MZ4b4hKGBf5iDGZv+NoLx/LXfvS0DNi2qAMWDxs/w1c9XsQaF+4D1wxufi+5ifcw6UkyKaY7Qpv8OCR92fYe3prveyBB4VLeDtzz1jFMzT2iNDmuDlU9Fl2YcXgHzBPzulzfUnn6O7mQc8kEegD2uT4HHlNF/K8IsPVJmv/jzWcuDuXNT8byFWgMYkBhJ+1688E+qhzizULGs7VrNwz1Ftbu4ekDS0/8hi9/jhZK8LLgDwlzXfx/lbbZpr83fp+LQnsKMH9Piw8B8FBsgHBJhVnFPZaUBuAJl/KMujOHx5Focf6DzXku/rx6PwP3oKAHYfFsFr9LowDVX4Ie2vHe4/Ej6DdmKm5Zef5sr64Q3PwDeYSj4svg4YQKO3ke8xoxcdmKZ/nYeb2ZGPLfMPsAd8fd309V8k3ODlbz+S6+GjL+8++kfptBnMANjPBv6rAg2EBwL4nfcjHwMmDyAG5WyW95shvolTPgavWRwgfvv8d4LfX0BgAohonbfQfOvcwXKAWx+buUdZghQGDMH1M9nAs//bnv6NTBM7oJkEdGAUd1eIi5M0usI8Fw08CqdgKnDCAEZJnwYPfCykQ8IjV6FD+zSKEo4XrjCEAoupWaxn5n6Z+7FkFm2WC1jkI0j+4NtjcMt/0+mpw2ywryPEIxGfqv3+4pI4WLnBG4l5ftgljbgkprjj9gJNZFgOJ6sdLZ3fu4TqdwWCNImxukhom53PWzKtYt3EIsPZ8nocwdI6PdzOtz1vBCoPjdhU+N1aMQd7b0/OoCiVwNBQcSSWNx8esY2nWyHinFU2OaUbJrKXwrW88El7clbC2VhNetldddkmArngG69nqTBYLlOUMt2NbMsknLLbo1pFuece6+v+TqNWiFnxSTS6OOmIkw1tvf6Sq7AyuYKV7SZU0wFSIsltnOyk0nxFCeKaOh9dAtoiSxr178Ou3kpqAp9uirGL8euk+oM2CIHlUj5UuPB5Z4cHPuQGUlopqZPLKN75MV+2GeiNtrWGrfHdVctx6I7FAx0UZnKpsSW95zcnbHLkHV94OkHqsUtsm4zJslDWSP58T6dMLadSdFeZKIzprvGhFlfLi2iN6ARjDJZf/CgShQ0R2GzJ7AbIvjN9rBiWS9wIPMe1PivN9K4K56ETZPLQNwncnZxAwo17r0wqeXSuGXleykR6qTiMVpvuZAzXDSzkYbldS4TGLVnqzDuxgtjy2rxXF5wpzHhdKyaRbG351Gk3fnlzkA2xLdtk7zDRyMO8PQqmlhZojBEZtvXQxjlFxPFw0Mx2e5OkiDCHdr+OEuVsrMW0sjYqNY68UnPrna8yS7qBKxi+2wciSSAnHtvD/uBcuWJ/qAi5MMiLhFU+RB0ut/J+O8rTCGio1yOTKnTGJ36KIa1tclTCc5ncdqJnXTf7DgoSL201lryy24E7rPjgxC/bU6xbaCMGlKTnfEjBl4SMraOticGSH/v+tjY114K3/q1nW0XHoq3boicH4StZ7e/tOklRFqFuyC5phkuqwLq9HA6ZcCzwa0IYtaQseVA/7tH9kPvy0EkaxDQYzw2HFYPHDbpZb4k0iCAXcy1sPxju3pzQcLqMAam1RF3RjY3bh729P9dk0EfnNQlLOxdR0Q6EZsxxVnUWIStBl94Bwq/3fc5pRrHiaAkv6hVlhaWpDBsWuVrJ2j3ATXnapn6FWnV6RJslq2nB5JVRgUCN6ukGRx2EERZJMkL2kXawsq0+OuuU7Igznd5ZR0H4gsPRdGXvBtF22eOOJ8Yy5G9TLcDMVsgc8mroNuMHwqoiCby4lNeaOWMsHOJi2ylqbO+32hYed9O+Qbe5RfcJx+bQBhsK5Mjf6RNXDwYbBIiVbq7X8cpTy9IWr0DH1LgZgU5A+zE4cDdtK61qZCosN4/Km6xed7B8p5TG3K144I4Wz8XzmVrtiVN1pe9pf2W0voBgqjB1j7aso3rqz+ItY5x+uZ4o/x7kbiJtkNvN1kOISUDsK+PAqvT2VB/gic1H2WH5tdTdSSp261a0pMtVPybB2CpxXyu5tezJ8eLAned4yf0csmleTU3LDbrMjJZRm8JJJhrWkwO0grYy2smJWYw1v/TjjX/jCgCH6VjvMkQW7ku1G/QlfSoEezsO59A1XQ7r1g509i0G6xtjUvuWoHNcuuxRM4w927WEWseNoz56grVhbn1feDK9ZDo9y4XUYUlFZcpy1C/WJSAcBdU36/telHE4O/E8O010Ftu1uaIGXCEPlx4nCu4ebjJvdVIdNkhN8wx7a9cqtpOZpOERDoW8c30V4TC4jlekHuQRTZzEQpRwrJp4URVd43CK705AI0SV71tS96XiYKtJDJ3KWNSRw2aiHWXbsY4WyVS4wTtzz5SdlPorqWYGEt32242OSerVZiSmsEaNpJeB7niiN6S2wpiwRekoepgcXbGjK+PI7lE3qNO6rVyks9y10UsBvyOu/rC1pYsgxOvK1nyaa7pdBCe2cGB3wsVZGuaUYsK5I7hS4p1TWe63sQ6d6lrAm7NvOv2Zbi162XSiKTfo2VTEgHdRexls7hR5x2wZL8nc3OJszG99hN5k52tKpY2xpRuavaK5qMbe1NTDqqScMoBySw/bkZdEOoixcUnjUIfdcmy5xHxtcy8mctBupyI4mLBdFWFT2FHMWZLQycyOy1trhMs749SZE1/gI+Fer+GVMg+IcLSrPujUnTuUVBgeY4rOJwI6JDv0YJI27Ki+piY5tWP1mAiHAK/xvXPB3YvEV3pzN0hOlxzzkg+3PDhKrUntEtXmDFgSBlOAVZWoDKbU9yIC+ZvQTdbn7nJU+1qlkl5EbyJtx1RGyCvN3zpE2FUT51G+DRUB7pmpttOLGpdKPEYDEC7Usba5axonBs+3O0NraVZETTPDl/u6NIulIlJln+5v7HHkRKrfuVkIgu7o6YmUrgtIXt3kgVmfXXuD7Ybtar1TtXxVw5U6hifRXN92Frc73cOTW6c8Ehmm4Cw5jlEmyypz4T6YpSzHUH5mmZpTC69hI/1eao5dVv7Fs4UNdRGRlIvHU9YL+cbehtGWhZhoGCHuzNRFVEtZwS8b14hGNTXEoRIZHoh1EnjWTk6JnOfH68QHpR6Auu0Y9+wGw4anjxyESmsDz7gNsxm7YhvIVXrMssFIRfcE6viRvO/Xd4I8l4kwLsFIT5tVcFWvQXzU4XNgqiLcBpzV8GmOi1EvSlORd3J4Uj1/zaiJ4lVpfk6IECalJOA0/XIZheud71gpU+7pckCi65WSm1ZfHpkM+ILs6142ccFhPZpLrJtsibrs8JLMrwRBTHau2PpX8kBp3jnlxygk2xAaCylaE6bfjHG8z03lVjU2j/Dmcbwd70q1jbQV6jQWQ6tTP6GYK6Tueiv1LNFkBtSMtL513UOYSpqFcOOUEuHGplZ2nUwBg2cZProlCKV1oXSp0Bw18XZcK3YZp2kSOZ68lvMVc0FJmetPzeqQ3a0oojzeyQ4RXJ1HplHBc8gBo4IcTwxjjcM656cblQliyjpJcXV0aEW2fMVTB1Q+jPWdPgbrmFE8QyUTLQlyOEHSFgS+U1/JkF0zCMi+8WxBzSYaNB2xpOPeoVAbAxU0aJhGkhPW6OuyvR2JcgmL2o0baIPc3sYGd/EBWi6LlNLvbX4steSy59ibHToOtkG3SFqK53HgTaVOZTa4HUOJC+X18mz0oKu/1yGBT2x4q2WndMy1xAFLwzobbOX0ILBi5ssXxezcwDFzf3SurIxkZF/q4W53TOPB4Kr13c6sKjLaeHc+FlmaHoYmQlAjV7ZWJMUQrlXOQYZx9SDCaJSytQ4qpuaUUGZkOLOnqZXYJ0xC5s1xKvsxRTQ3Se8tx/PJUogdWrPUHkZP8iTe7E7KeXhgSTbzKr+DlFWDBfdraFiBQ6dFlFDVxHD2uM25+NJJTLpd92d5592kyoV6VslVralKwZcakixV4nrYjyt4HXhoq+mxJiDteOKSnbhBWI0R0DjS+H6DHy1XoteyhI39sWG2kcIL7QYDzafV1WQmoHyROOLKkPQxWZfHM7MrygQHjmq2FyyR3Juxg2Gyc8pVXIjDxVQaRe6N+6YVnTu0OWRQrqFKjHRHsW7Z8nCK2suQk6soPid03ZobjT6SVWzesJN436f5tavcU5P1xGi2kdlu6iMDDQ4F9zduD50PVS71eaCOiHbEIanVrAt5EC01ynk88DTWuux5lL6pic4cQ5nPNXfc4aoStDpAgojq0cKKChj1kS11U+XBG5ENVQOAqmJvgG9KbK/NwxZec/lJObebFAp9ob0QscEpfgn8JfFuvF7j242ZSIaHYiuTNxIVn7amX5r0lQ76y4B2lkNKlyiLDf52w8/1ZpneqrxsZSVf2s2VTOWEPOZJ7qZHk5nO5MTgMj8eqm5SYJu6rX0zPzCaXTvr89RV/UE6F4Qo7tAJCrZdRFEiGIIO8irq+mS/h5rYxdEcGemsxE5MtUbKUqi0U8nIx1WxvZ0CswxGfK2rhRJXqpMX97O/KwihboelEVVM4bu7s7xaJftoxWyqtV6sLittE7QJdMbtcSfX6yaaTHfINeWmjnK86zvoyDOcLicEnDuOWEy4e3L6EteR/XSqMA93ICSFm0HM8Its0WxxlW5gULgHqbSNw1RscW9aF4JgWZm65sX4mgSd423YQjEqhWuMUIhypdXuMkFPrZ9mEH0uK2FMootCCkVUMmKsrxp5Ky6lLGb6E30qI+1yrgYL8+F9e91V2PVwg1LOkG9GV4K2x5SNYyRBLLiiTiMJrTHhQsb7OK0m9Hbygo3qbE5uXDg1nJCUpXV1L50GSapotVaYNNnsQJtwRuoGv+z75VViyfOelDa7reDlOWJP65YYp+OQXm5gVlwyRXuUz9gNy7aHivVXbaGbazigiLWwQuWou55RmpyiXbK93gJEOdWh25/8Aw2Z+GbYna5tu2K7TJA0/F7iPuZxerBhu6k+3TN/0x5OBBu2CIFMbWfH+KZYEY4EcOKMIlVhBVrgD72pbSylRuoM9BLk7cJV2FG4clN+WK4lfpkFl/ws+0fhDnMMsrXd6k4WAtrVwBrIPc9kMg3cay0gHqVSR1g5aScQxOaSNyOhN1jbhLSlGVP3Ujww+ulwbtfaAanVfO1sc8ivnE5aCvcDmJIIfuiiu08LSby/WCokJkOaHS/Yuplc9HZRjmtK29hu461xm+6A3Hs33E8rbEnKG4gjZPZyVQV6KRwhbRQDrs3h6pJNW1eGXd7mKAreDqfjelwJERNI/prbwH1xPkIxVxv+VLWGtDMv7VqoCD5e5QrOsscNISQ7FbO3BQTyZVue62ZSIZuUp5PpUZirB34kk46rNvduLLjAwseDcN2m2Gp32YWUs+04ux1SHD3Tox45+qHZD8udjyAnGCeScO/gkSVOtNbl0WTvNicJLpKT5IgQvwuUfVe4xC2s9lyuBCff03aTwCKbyhHosd3glgDdLoi1tOOkPe46L9SPUnQIlQg/hruObVbqCo+3ZYm7DoawbJdkMbdNrqDbqS8nKt+GN9H2bvpWcWnOusaFjZW0Tbi+NYChfT85E0HhrBBeiTHeJOK1TbZGZsxNl7gerTCtN64pHuQDV4reHu7j9nJZq3C7OXDeoKjIWryKFqTVbNpH6aHkaQrWytGnFACFoA9D6XRfcHAVBmePT5KpElZUd7nC5F64IthFW+P1biTWLsOKoVV1NGs55jGChlsjIKO68bgIUupb2i9hdCMXmiGsXJsKwl1qLjfKZWrhyzETV+VK6NthdWoIqIcv6rjzB2dbZdrpBCSQ8n3a15NrNFefF+73fJdfFUIpEZdOeD8+DIcq8JnQZtcaqe0o5SbfOQiWqckLTA8ZQIcNJvNLnjf7O8N4MFGgt2tHI95RTD3Gte0a9o+bTIQrL45vG7Uadlx1Fy810jShOvZrftAF3yRgzI96RdrQcAgG3UDQQX2iNv50le+3azCUG9JqGq2hJGTFiPnltMx6z8Wq+nw/eWTteFitueFOHmk1KcFQugtX5qrzdpgebs/HnAZwYptuhKw38XBVwvNR3zgqZdfuBblk2Jm/+KG9MrFYN5G+uzoeFWmjjtN1aVdKi6DCRdreyZ3F5HcGho9usDprHQnRp9oMVeOGI9dkz+0y4C2v9FoZd7SREItePxBnbBOTAcE3vJk4FV9tkK1cBI220rqdGYnbC4GoI0nDprnERrxnaitjHdBFtAfQMoY8RG3wYPLUk14OMc2wMYIsk4kxWWGzu14Lq1ftg3GrvXYDc/EwSHvEFuI7KFTQKUfxIwqqYu835Fm0crltuG6ScopcovLdzlcaHnRRoWPKzk2mxpD8S5FqMALJG9SCIRUz6Y1dGSAKuAoEz4XY+dihbc9E5tmV7tXuucWMsGJQqmXGGkekW78iTUdGJl9D4coY7srZaBv01FpkiJOtmZWiQ2OcmoYo4bJ2q1vI8WxRq6yxRG2qVBQTb2ef0oiNSusksnVFfGpWdQl75iFC7Y1kLLlgctf1ymZ8zpUHW4E6YFd+o+jItr8kdX+Tr61RwmdCsbqW7eO9pGHcNdd0+pQTCl+f6eWtWMcYCeWBvNHYkIy5fcgQ9+yigM7c79HQgliqasD47/PrNM4iztjRGXdP+NQUr+NliS2zcFeQ1+URo5jDKTzW6Sa7b05qo4Qtkcl+TyzdDGmIw7IGg25K3W/JmRzwGHNv6S6EiBhVQri9JLIsnyW6sYUct0R3C5CahOurWygUHKCkAktXa6kKeRfQ3IjGXrtKQnxjZglLa4x13BYl1HrIKimm8GLz9HTzmBGMSlLU0uNeZw8WQTAS2N21fcNwLezctahAV4ZrYiqvwjVhStb+cq2oaxCIDblyad2FdZK9ome5DGJ9z5IVVu+5Se5qN3EgL13WnYEgiJZAGuaISyQuqIu7og5Yg15IYWlRXOstp2CtL8UpbPgj1xKIjLV42VnJbXdzDLRLl4dQ7a7ddZLkaFkSS3nUfLs+1esTvvdjG2FbTKTDvMsNOXALHDkajXIgJ33XY3c656zQZtQdRA9mfbmFVzm7o8qxLvWh8bbhmrDSG8MgMkKJN29bRXJCCfpJP5PmRdtUvYsqXe5QDiWw63J1vTRxoaKRm3JORO44yAhTJhGHnEAA1GPcYVNj0JD3q7690N1yJQQZV0ouSdg0gOl7aOy3g+neBLhR3Rrz7lFbHYiiT7Bue2JPngGrJFPFuKMs3ToP7wVWjCrEeZG/k+5HbIWwl9Vxq+4t6jYdoWC1POwDfHvV4NEUDvX9yHS7YUVxA3JxieNGZxjm5cPLtxOrl3/1par58OX/2TnP87jm/T2Kx4lc4PifHrw+/cuS/e3DS+0lQK7nyVaTddHb4dDfnWt9/CdPz2ci4/OtpfeT1ucxcetE8/u9L0nhg9X1+KUps8c7FWCH2zXz24DN/MKoB76/P2D8k0rztfc42/vSll/8BIyOzXy2lRTzGxOBn8ynx8/L6O3U78OL//ZyzheMJL4EdTUr/XYoD3TFXuFX9OWP/w0P48Ongy0AAA== -->
