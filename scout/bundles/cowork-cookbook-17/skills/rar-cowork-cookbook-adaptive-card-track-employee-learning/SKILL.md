---
name: "rar-cowork-cookbook-adaptive-card-track-employee-learning"
description: "Generates a read-only Adaptive Card JSON file visualizing employee learning status from Dynamics 365 ERP for a given legal entity, with KPI tiles, trend arrows, a RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_track_employee_learning", "rar_sha256": "dc05c64c357d3fe3d4343597db5d78e38e9a59e441ffce717aabaa3a2c96e869", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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
