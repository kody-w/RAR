---
name: "rar-cowork-cookbook-adaptive-card-decommission-assets"
description: "Generates a read-only Adaptive Card JSON file summarizing decommission assets status from Dynamics 365 F&SCM for a legal entity, with KPI tiles, trend arrows, a RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_decommission_assets", "rar_sha256": "94addc11e26c6ff2de4e37677dded4aeb57a8a08d7dd78300c0830dd4f3dfd53", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_decommission_assets`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_decommission_assets_agent.py` and in the RCI capsule.

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

Decommission assets Status Adaptive Card — Generates a read-only Adaptive Card JSON file summarizing decommission assets status from Dynamics 365 F&SCM for a legal entity, with KPI tiles, trend arrows, a RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-decommission-assets
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
      "description": "Snapshot date shown in the card header timestamp.",
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
      "description": "Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-decommission-assets-2026-05-24-card.json.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_decommission_assets_agent.py` and embedded as the fenced Python below (sha256 94addc11e26c6ff2…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_decommission_assets_agent.py` first:

```bash
python3 adaptive_card_decommission_assets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_decommission_assets_agent.py   # or on stdin
python3 adaptive_card_decommission_assets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Decommission assets Status Adaptive Card — Generates a read-only Adaptive Card JSON file summarizing decommission assets status from Dynamics 365 F&SCM for a legal entity, with KPI tiles, trend arrows, a RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-decommission-assets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_decommission_assets',
    "version": '3.0.2',
    "display_name": 'Decommission assets Status Adaptive Card',
    "description": 'Generates a read-only Adaptive Card JSON file summarizing decommission assets status from Dynamics 365 F&SCM for a legal entity, with KPI tiles, trend arrows, a RAG row, and action buttons.',
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
        "upstream_slug": 'adaptive-card-decommission-assets',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-decommission-assets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '60aac5f4f7eb53a1',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/dispose-of-assets/decommission-assets'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/adaptive-card-decommission-assets', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'as_of_date': 'Snapshot date shown in the card header timestamp.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'output_filename': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-decommission-assets-2026-05-24-card.json.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives any consuming app (Teams, Outlook, custom dashboard) a single canonical decommission assets status card so different surfaces always show the same numbers.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, produce an Adaptive Card JSON file 'adaptive-card-decommission-assets-2026-05-24-card.json' that visualizes the current state of decommission assets. Include: header with title and timestamp, 3-5 KPI tiles with current value + trend arrow, a RAG indicator row, and 2-3 action buttons. The card should render correctly in Teams, Outlook Adaptive Card preview, and the Adaptive Cards designer. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-25', 'what_it_does': 'Generates an Adaptive Card JSON file with current decommission assets KPIs and RAG indicators.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Generates a read-only Adaptive Card JSON file summarizing decommission assets status from Dynamics 365 F&SCM for a legal entity, with KPI tiles, trend arrows, a RAG row, and action buttons.', 'example_request': 'Make an Adaptive Card JSON of decommission assets status for USMF as of 2026-05-24.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-decommission-assets-2026-05-24-card.json.', 'name': 'output_filename'}, {'description': 'Snapshot date shown in the card header timestamp.', 'name': 'as_of_date'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a Teams/Outlook-ready Adaptive Card snapshot of decommission assets status from D365 ERP without changing any data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AdaptiveCardDecommissionAssets(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardDecommissionAssets'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'as_of_date': {'description': 'Snapshot date shown in the card header timestamp.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-decommission-assets-2026-05-24-card.json.', 'type': 'string'}},
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
    print(AdaptiveCardDecommissionAssets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
