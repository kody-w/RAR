---
name: "rar-cowork-cookbook-adaptive-card-create-a-case-from-a-channel"
description: "Generates a read-only Adaptive Card JSON file visualizing the current state of 'create a case from a channel' from Dynamics 365 F&SCM, with header, KPI tiles, RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_create_a_case_from_a_channel", "rar_sha256": "e361c6d536f6d2c214e7a7052691f97b0ddc7b5e8e73f8e09254688879510fec", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_create_a_case_from_a_channel`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_create_a_case_from_a_channel_agent.py` and in the RCI capsule.

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

Create a case from a channel Status Adaptive Card — Generates a read-only Adaptive Card JSON file visualizing the current state of 'create a case from a channel' from Dynamics 365 F&SCM, with header, KPI tiles, RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-create-a-case-from-a-channel
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
      "description": "Date used for the card timestamp and filename.",
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
      "description": "Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-create-a-case-from-a-channel-2026-05-24-card.json.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_create_a_case_from_a_channel_agent.py` and embedded as the fenced Python below (sha256 e361c6d536f6d2c2…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_create_a_case_from_a_channel_agent.py` first:

```bash
python3 adaptive_card_create_a_case_from_a_channel_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_create_a_case_from_a_channel_agent.py   # or on stdin
python3 adaptive_card_create_a_case_from_a_channel_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Create a case from a channel Status Adaptive Card — Generates a read-only Adaptive Card JSON file visualizing the current state of 'create a case from a channel' from Dynamics 365 F&SCM, with header, KPI tiles, RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-create-a-case-from-a-channel
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_create_a_case_from_a_channel',
    "version": '3.0.2',
    "display_name": 'Create a case from a channel Status Adaptive Card',
    "description": "Generates a read-only Adaptive Card JSON file visualizing the current state of 'create a case from a channel' from Dynamics 365 F&SCM, with header, KPI tiles, RAG row, and action buttons.",
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
        "upstream_slug": 'adaptive-card-create-a-case-from-a-channel',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-create-a-case-from-a-channel',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '20c5fe821e5fbb9f',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/intake-cases/create-a-case-from-a-channel'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/adaptive-card-create-a-case-from-a-channel', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'action_buttons': 'The 2-3 action buttons to include on the card.', 'as_of_date': 'Date used for the card timestamp and filename.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'kpi_count': 'How many KPI tiles to include (3-5).', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'output_filename': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-create-a-case-from-a-channel-2026-05-24-card.json.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives any consuming app (Teams, Outlook, custom dashboard) a single canonical create a case from a channel status card so different surfaces always show the same numbers.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, produce an Adaptive Card JSON file 'adaptive-card-create-a-case-from-a-channel-2026-05-24-card.json' that visualizes the current state of create a case from a channel. Include: header with title and timestamp, 3-5 KPI tiles with current value + trend arrow, a RAG indicator row, and 2-3 action buttons. The card should render correctly in Teams, Outlook Adaptive Card preview, and the Adaptive Cards designer. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates an Adaptive Card JSON file with current create a case from a channel KPIs and RAG indicators.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Generates a read-only Adaptive Card JSON file visualizing the current state of 'create a case from a channel' from Dynamics 365 F&SCM, with header, KPI tiles, RAG row, and action buttons.", 'example_request': 'Make an Adaptive Card for create-a-case-from-a-channel status in USMF as of 2026-05-24.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-create-a-case-from-a-channel-2026-05-24-card.json.', 'name': 'output_filename'}, {'description': 'Date used for the card timestamp and filename.', 'name': 'as_of_date'}, {'description': 'How many KPI tiles to include (3-5).', 'name': 'kpi_count'}, {'description': 'The 2-3 action buttons to include on the card.', 'name': 'action_buttons'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a Teams/Outlook-ready Adaptive Card snapshot of create-a-case-from-a-channel status from D365 ERP, without changing any data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AdaptiveCardCreateACaseFromAChannel(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardCreateACaseFromAChannel'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'action_buttons': {'description': 'The 2-3 action buttons to include on the card.', 'type': 'string'}, 'as_of_date': {'description': 'Date used for the card timestamp and filename.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'kpi_count': {'description': 'How many KPI tiles to include (3-5).', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-create-a-case-from-a-channel-2026-05-24-card.json.', 'type': 'string'}},
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
    print(AdaptiveCardCreateACaseFromAChannel().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
