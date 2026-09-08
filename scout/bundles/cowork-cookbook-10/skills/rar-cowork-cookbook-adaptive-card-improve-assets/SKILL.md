---
name: "rar-cowork-cookbook-adaptive-card-improve-assets"
description: "Generates a read-only Adaptive Card JSON file visualizing improve assets status from Dynamics 365 F&SCM for a given legal entity, with header, KPI tiles, RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_improve_assets", "rar_sha256": "13a0a4d3162edc05a3cff5afcb346c4b1365f7dc22b75a449fc033d610612087", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
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
