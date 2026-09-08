---
name: "rar-cowork-cookbook-adaptive-card-improve-assets"
description: "Generates a read-only Adaptive Card JSON file visualizing improve assets status from Dynamics 365 F&SCM for a given legal entity, with header, KPI tiles, RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_improve_assets", "rar_sha256": "13a0a4d3162edc05a3cff5afcb346c4b1365f7dc22b75a449fc033d610612087", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_improve_assets`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_improve_assets_agent.py` and in the RCI capsule.

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

Improve assets Status Adaptive Card — Generates a read-only Adaptive Card JSON file visualizing improve assets status from Dynamics 365 F&SCM for a given legal entity, with header, KPI tiles, RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-improve-assets
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
      "description": "Date used for the card timestamp and output filename (e.g. 2026-05-24).",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to pull improve assets data from (e.g. USMF).",
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
      "description": "Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-improve-assets-2026-05-24-card.json.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_improve_assets_agent.py` and embedded as the fenced Python below (sha256 13a0a4d3162edc05…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_improve_assets_agent.py` first:

```bash
python3 adaptive_card_improve_assets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_improve_assets_agent.py   # or on stdin
python3 adaptive_card_improve_assets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Improve assets Status Adaptive Card — Generates a read-only Adaptive Card JSON file visualizing improve assets status from Dynamics 365 F&SCM for a given legal entity, with header, KPI tiles, RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-improve-assets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_improve_assets',
    "version": '3.0.2',
    "display_name": 'Improve assets Status Adaptive Card',
    "description": 'Generates a read-only Adaptive Card JSON file visualizing improve assets status from Dynamics 365 F&SCM for a given legal entity, with header, KPI tiles, RAG row, and action buttons.',
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
        "upstream_slug": 'adaptive-card-improve-assets',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-improve-assets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '7b91d0e753c5a34a',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/manage-active-assets/improve-assets'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/adaptive-card-improve-assets', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'as_of_date': 'Date used for the card timestamp and output filename (e.g. 2026-05-24).', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to pull improve assets data from (e.g. USMF).', 'output_filename': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-improve-assets-2026-05-24-card.json.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives any consuming app (Teams, Outlook, custom dashboard) a single canonical improve assets status card so different surfaces always show the same numbers.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, produce an Adaptive Card JSON file 'adaptive-card-improve-assets-2026-05-24-card.json' that visualizes the current state of improve assets. Include: header with title and timestamp, 3-5 KPI tiles with current value + trend arrow, a RAG indicator row, and 2-3 action buttons. The card should render correctly in Teams, Outlook Adaptive Card preview, and the Adaptive Cards designer. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-25', 'what_it_does': 'Generates an Adaptive Card JSON file with current improve assets KPIs and RAG indicators.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Generates a read-only Adaptive Card JSON file visualizing improve assets status from Dynamics 365 F&SCM for a given legal entity, with header, KPI tiles, RAG row, and action buttons.', 'example_request': 'Make an Adaptive Card JSON of improve assets status for USMF as of 2026-05-24.', 'inputs': [{'description': 'D365 legal entity to pull improve assets data from (e.g. USMF).', 'name': 'legal_entity'}, {'description': 'Date used for the card timestamp and output filename (e.g. 2026-05-24).', 'name': 'as_of_date'}, {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-improve-assets-2026-05-24-card.json.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants an embeddable Adaptive Card snapshot of improve assets status from D365 ERP for Teams, Outlook, or a dashboard.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AdaptiveCardImproveAssets(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardImproveAssets'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'as_of_date': {'description': 'Date used for the card timestamp and output filename (e.g. 2026-05-24).', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to pull improve assets data from (e.g. USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-improve-assets-2026-05-24-card.json.', 'type': 'string'}},
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
    print(AdaptiveCardImproveAssets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
