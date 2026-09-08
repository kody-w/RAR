---
name: "rar-cowork-cookbook-adaptive-card-track-additional-information-against-a-case"
description: "Generates a read-only Adaptive Card JSON file visualizing case additional-information tracking status from Dynamics 365 F&SCM (legal entity USMF), with header, KPI tiles, RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_track_additional_information_against_a_case", "rar_sha256": "34651d495153515e011e0152d2a0895d518a7550f3d3efe4e3c6371d3ea28411", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
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
