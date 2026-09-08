---
name: "rar-cowork-cookbook-adaptive-card-source-assets"
description: "Generates a read-only Adaptive Card JSON file summarizing source assets status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, RAG row, and action buttons. Call to embed a status card in Teams, Outlook,"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_source_assets", "rar_sha256": "9f5bbfb53a5d2d0e6e388756595c0f708b380dd0af6763f037722e90d6d3e029", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
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
