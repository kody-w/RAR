---
name: "rar-cowork-cookbook-adaptive-card-track-additional-information-against-a-case"
description: "Generates a read-only Adaptive Card JSON file visualizing case additional-information tracking status from Dynamics 365 F&SCM (legal entity USMF), with header, KPI tiles, RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_track_additional_information_against_a_case", "rar_sha256": "34651d495153515e011e0152d2a0895d518a7550f3d3efe4e3c6371d3ea28411", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_track_additional_information_against_a_case`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_track_additional_information_against_a_case_agent.py` and in the RCI capsule.

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

Track additional information against a case Status Adaptive Card — Generates a read-only Adaptive Card JSON file visualizing case additional-information tracking status from Dynamics 365 F&SCM (legal entity USMF), with header, KPI tiles, RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-track-additional-information-against-a-case
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
      "description": "Date used for the card timestamp and file name.",
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
      "description": "Dynamics 365 legal entity to read from, e.g. USMF.",
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
    "output_file_name": {
      "description": "Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-track-additional-information-against-a-case-2026-05-24-card.json.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_track_additional_information_against_a_case_agent.py` and embedded as the fenced Python below (sha256 34651d495153515e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_track_additional_information_against_a_case_agent.py` first:

```bash
python3 adaptive_card_track_additional_information_against_a_case_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_track_additional_information_against_a_case_agent.py   # or on stdin
python3 adaptive_card_track_additional_information_against_a_case_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Track additional information against a case Status Adaptive Card — Generates a read-only Adaptive Card JSON file visualizing case additional-information tracking status from Dynamics 365 F&SCM (legal entity USMF), with header, KPI tiles, RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-track-additional-information-against-a-case
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_track_additional_information_against_a_case',
    "version": '3.0.2',
    "display_name": 'Track additional information against a case Status Adaptive Card',
    "description": 'Generates a read-only Adaptive Card JSON file visualizing case additional-information tracking status from Dynamics 365 F&SCM (legal entity USMF), with header, KPI tiles, RAG row, and action buttons.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'case_to_resolution', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-track-additional-information-against-a-case',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-track-additional-information-against-a-case',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'd11b662019bbe3fd',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/manage-and-work-on-cases/track-additional-information-against-a-case'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/adaptive-card-track-additional-information-against-a-case', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'action_buttons': 'The 2-3 action buttons to include on the card.', 'as_of_date': 'Date used for the card timestamp and file name.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'kpi_count': 'How many KPI tiles to include (3-5).', 'legal_entity': 'Dynamics 365 legal entity to read from, e.g. USMF.', 'output_file_name': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-track-additional-information-against-a-case-2026-05-24-card.json.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives any consuming app (Teams, Outlook, custom dashboard) a single canonical track additional information against a case status card so different surfaces always show the same numbers.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, produce an Adaptive Card JSON file 'adaptive-card-track-additional-information-against-a-case-2026-05-24-card.json' that visualizes the current state of track additional information against a case. Include: header with title and timestamp, 3-5 KPI tiles with current value + trend arrow, a RAG indicator row, and 2-3 action buttons. The card should render correctly in Teams, Outlook Adaptive Card preview, and the Adaptive Cards designer. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates an Adaptive Card JSON file with current track additional information against a case KPIs and RAG indicators.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Generates a read-only Adaptive Card JSON file visualizing case additional-information tracking status from Dynamics 365 F&SCM (legal entity USMF), with header, KPI tiles, RAG row, and action buttons.', 'example_request': 'Make an Adaptive Card JSON for case additional-info tracking status in USMF as of 2026-05-24.', 'inputs': [{'description': 'Dynamics 365 legal entity to read from, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-track-additional-information-against-a-case-2026-05-24-card.json.', 'name': 'output_file_name'}, {'description': 'Date used for the card timestamp and file name.', 'name': 'as_of_date'}, {'description': 'How many KPI tiles to include (3-5).', 'name': 'kpi_count'}, {'description': 'The 2-3 action buttons to include on the card.', 'name': 'action_buttons'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a shareable Adaptive Card snapshot of case additional-information tracking status for Teams, Outlook, or a dashboard, without changing data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AdaptiveCardTrackAdditionalInformationAgainstACase(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardTrackAdditionalInformationAgainstACase'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'action_buttons': {'description': 'The 2-3 action buttons to include on the card.', 'type': 'string'}, 'as_of_date': {'description': 'Date used for the card timestamp and file name.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'kpi_count': {'description': 'How many KPI tiles to include (3-5).', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to read from, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_file_name': {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-track-additional-information-against-a-case-2026-05-24-card.json.', 'type': 'string'}},
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
    print(AdaptiveCardTrackAdditionalInformationAgainstACase().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
