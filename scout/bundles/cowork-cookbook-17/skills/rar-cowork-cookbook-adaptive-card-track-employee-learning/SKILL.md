---
name: "rar-cowork-cookbook-adaptive-card-track-employee-learning"
description: "Generates a read-only Adaptive Card JSON file visualizing employee learning status from Dynamics 365 ERP for a given legal entity, with KPI tiles, trend arrows, a RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_track_employee_learning", "rar_sha256": "dc05c64c357d3fe3d4343597db5d78e38e9a59e441ffce717aabaa3a2c96e869", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_track_employee_learning`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_track_employee_learning_agent.py` and in the RCI capsule.

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

Track employee learning Status Adaptive Card — Generates a read-only Adaptive Card JSON file visualizing employee learning status from Dynamics 365 ERP for a given legal entity, with KPI tiles, trend arrows, a RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-track-employee-learning
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
      "description": "Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-track-employee-learning-2026-05-24-card.json.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_track_employee_learning_agent.py` and embedded as the fenced Python below (sha256 dc05c64c357d3fe3…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_track_employee_learning_agent.py` first:

```bash
python3 adaptive_card_track_employee_learning_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_track_employee_learning_agent.py   # or on stdin
python3 adaptive_card_track_employee_learning_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Track employee learning Status Adaptive Card — Generates a read-only Adaptive Card JSON file visualizing employee learning status from Dynamics 365 ERP for a given legal entity, with KPI tiles, trend arrows, a RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-track-employee-learning
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_track_employee_learning',
    "version": '3.0.2',
    "display_name": 'Track employee learning Status Adaptive Card',
    "description": 'Generates a read-only Adaptive Card JSON file visualizing employee learning status from Dynamics 365 ERP for a given legal entity, with KPI tiles, trend arrows, a RAG row, and action buttons.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'hire_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-track-employee-learning',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-track-employee-learning',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'c3842d180cc2d671',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/analyze-hr-programs/track-employee-learning'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/adaptive-card-track-employee-learning', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'action_buttons': 'The 2-3 action buttons to include on the card.', 'as_of_date': 'Date used for the card timestamp and file naming.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'kpi_count': 'How many KPI tiles to include (3-5).', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'output_filename': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-track-employee-learning-2026-05-24-card.json.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives any consuming app (Teams, Outlook, custom dashboard) a single canonical track employee learning status card so different surfaces always show the same numbers.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, produce an Adaptive Card JSON file 'adaptive-card-track-employee-learning-2026-05-24-card.json' that visualizes the current state of track employee learning. Include: header with title and timestamp, 3-5 KPI tiles with current value + trend arrow, a RAG indicator row, and 2-3 action buttons. The card should render correctly in Teams, Outlook Adaptive Card preview, and the Adaptive Cards designer. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates an Adaptive Card JSON file with current track employee learning KPIs and RAG indicators.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Generates a read-only Adaptive Card JSON file visualizing employee learning status from Dynamics 365 ERP for a given legal entity, with KPI tiles, trend arrows, a RAG row, and action buttons.', 'example_request': 'Make an Adaptive Card showing employee learning status for USMF as of 2026-05-24.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-track-employee-learning-2026-05-24-card.json.', 'name': 'output_filename'}, {'description': 'Date used for the card timestamp and file naming.', 'name': 'as_of_date'}, {'description': 'How many KPI tiles to include (3-5).', 'name': 'kpi_count'}, {'description': 'The 2-3 action buttons to include on the card.', 'name': 'action_buttons'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a Teams/Outlook-renderable Adaptive Card snapshot of employee learning status pulled from Dynamics 365 F&SCM without changing any data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AdaptiveCardTrackEmployeeLearning(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardTrackEmployeeLearning'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'action_buttons': {'description': 'The 2-3 action buttons to include on the card.', 'type': 'string'}, 'as_of_date': {'description': 'Date used for the card timestamp and file naming.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'kpi_count': {'description': 'How many KPI tiles to include (3-5).', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-track-employee-learning-2026-05-24-card.json.', 'type': 'string'}},
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
    print(AdaptiveCardTrackEmployeeLearning().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
