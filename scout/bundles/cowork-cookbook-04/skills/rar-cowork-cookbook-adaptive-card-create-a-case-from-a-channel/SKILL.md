---
name: "rar-cowork-cookbook-adaptive-card-create-a-case-from-a-channel"
description: "Generates a read-only Adaptive Card JSON file visualizing the current state of 'create a case from a channel' from Dynamics 365 F&SCM, with header, KPI tiles, RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_create_a_case_from_a_channel", "rar_sha256": "e361c6d536f6d2c214e7a7052691f97b0ddc7b5e8e73f8e09254688879510fec", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
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
