---
name: "rar-cowork-cookbook-adaptive-card-source-assets"
description: "Generates a read-only Adaptive Card JSON file summarizing source assets status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, RAG row, and action buttons. Call to embed a status card in Teams, Outlook,"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_source_assets", "rar_sha256": "9f5bbfb53a5d2d0e6e388756595c0f708b380dd0af6763f037722e90d6d3e029", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_source_assets`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_source_assets_agent.py` and in the RCI capsule.

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

Source assets Status Adaptive Card — Generates a read-only Adaptive Card JSON file summarizing source assets status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, RAG row, and action buttons. Call to embed a status card in Teams, Outlook,

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-source-assets
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
    "action_buttons": {
      "description": "The 2-3 action buttons to include on the card.",
      "type": "string"
    },
    "as_of_date": {
      "description": "Date used for the card timestamp and file naming.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "kpi_count": {
      "description": "How many KPI tiles to include (3-5).",
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
      "description": "Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-source-assets-2026-05-24-card.json.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_source_assets_agent.py` and embedded as the fenced Python below (sha256 9f5bbfb53a5d2d0e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_source_assets_agent.py` first:

```bash
python3 adaptive_card_source_assets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_source_assets_agent.py   # or on stdin
python3 adaptive_card_source_assets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Source assets Status Adaptive Card — Generates a read-only Adaptive Card JSON file summarizing source assets status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, RAG row, and action buttons. Call to embed a status card in Teams, Outlook,

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-source-assets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_source_assets',
    "version": '3.0.2',
    "display_name": 'Source assets Status Adaptive Card',
    "description": 'Generates a read-only Adaptive Card JSON file summarizing source assets status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, RAG row, and action buttons. Call to embed a status card in Teams, Outlook,',
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
        "upstream_slug": 'adaptive-card-source-assets',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-source-assets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '805f6a1eed2e1df5',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/acquire-assets/source-assets'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/adaptive-card-source-assets', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'action_buttons': 'The 2-3 action buttons to include on the card.', 'as_of_date': 'Date used for the card timestamp and file naming.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'kpi_count': 'How many KPI tiles to include (3-5).', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'output_filename': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-source-assets-2026-05-24-card.json.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives any consuming app (Teams, Outlook, custom dashboard) a single canonical source assets status card so different surfaces always show the same numbers.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, produce an Adaptive Card JSON file 'adaptive-card-source-assets-2026-05-24-card.json' that visualizes the current state of source assets. Include: header with title and timestamp, 3-5 KPI tiles with current value + trend arrow, a RAG indicator row, and 2-3 action buttons. The card should render correctly in Teams, Outlook Adaptive Card preview, and the Adaptive Cards designer. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-25', 'what_it_does': 'Generates an Adaptive Card JSON file with current source assets KPIs and RAG indicators.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Generates a read-only Adaptive Card JSON file summarizing source assets status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, RAG row, and action buttons. Call to embed a status card in Teams, Outlook,', 'example_request': 'Make an Adaptive Card JSON showing source assets status for USMF as of 2026-05-24.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-source-assets-2026-05-24-card.json.', 'name': 'output_filename'}, {'description': 'Date used for the card timestamp and file naming.', 'name': 'as_of_date'}, {'description': 'How many KPI tiles to include (3-5).', 'name': 'kpi_count'}, {'description': 'The 2-3 action buttons to include on the card.', 'name': 'action_buttons'}], 'model': 'claude-opus-5', 'when_to_use': 'Use when a user wants a shareable Adaptive Card snapshot of source assets status from D365 ERP data, without modifying any data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AdaptiveCardSourceAssets(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardSourceAssets'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'action_buttons': {'description': 'The 2-3 action buttons to include on the card.', 'type': 'string'}, 'as_of_date': {'description': 'Date used for the card timestamp and file naming.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'kpi_count': {'description': 'How many KPI tiles to include (3-5).', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-source-assets-2026-05-24-card.json.', 'type': 'string'}},
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
    print(AdaptiveCardSourceAssets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
