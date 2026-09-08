---
name: "rar-cowork-cookbook-adaptive-card-decommission-assets"
description: "Generates a read-only Adaptive Card JSON file summarizing decommission assets status from Dynamics 365 F&SCM for a legal entity, with KPI tiles, trend arrows, a RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_decommission_assets", "rar_sha256": "94addc11e26c6ff2de4e37677dded4aeb57a8a08d7dd78300c0830dd4f3dfd53", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
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
