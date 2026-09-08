---
name: "rar-cowork-cookbook-adaptive-card-manage-shifts"
description: "Generates a read-only Adaptive Card JSON file visualizing manage shifts status from Dynamics 365 F&SCM for a given legal entity, with header, KPI tiles, RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_manage_shifts", "rar_sha256": "27c430835e0a3887298eb923f634b91baf191441a16edc1e3fc10292c67d6db4", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_manage_shifts`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_manage_shifts_agent.py` and in the RCI capsule.

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

Manage shifts Status Adaptive Card — Generates a read-only Adaptive Card JSON file visualizing manage shifts status from Dynamics 365 F&SCM for a given legal entity, with header, KPI tiles, RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-manage-shifts
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
      "description": "Date/timestamp the card snapshot represents.",
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
      "description": "Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-manage-shifts-2026-05-24-card.json.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_manage_shifts_agent.py` and embedded as the fenced Python below (sha256 27c430835e0a3887…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_manage_shifts_agent.py` first:

```bash
python3 adaptive_card_manage_shifts_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_manage_shifts_agent.py   # or on stdin
python3 adaptive_card_manage_shifts_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage shifts Status Adaptive Card — Generates a read-only Adaptive Card JSON file visualizing manage shifts status from Dynamics 365 F&SCM for a given legal entity, with header, KPI tiles, RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-manage-shifts
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_manage_shifts',
    "version": '3.0.2',
    "display_name": 'Manage shifts Status Adaptive Card',
    "description": 'Generates a read-only Adaptive Card JSON file visualizing manage shifts status from Dynamics 365 F&SCM for a given legal entity, with header, KPI tiles, RAG row, and action buttons.',
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
        "upstream_slug": 'adaptive-card-manage-shifts',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-manage-shifts',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '465fe13eb27fb9f7',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/manage-time-and-attendance/manage-shifts'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/adaptive-card-manage-shifts', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'as_of_date': 'Date/timestamp the card snapshot represents.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'output_filename': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-manage-shifts-2026-05-24-card.json.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives any consuming app (Teams, Outlook, custom dashboard) a single canonical manage shifts status card so different surfaces always show the same numbers.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, produce an Adaptive Card JSON file 'adaptive-card-manage-shifts-2026-05-24-card.json' that visualizes the current state of manage shifts. Include: header with title and timestamp, 3-5 KPI tiles with current value + trend arrow, a RAG indicator row, and 2-3 action buttons. The card should render correctly in Teams, Outlook Adaptive Card preview, and the Adaptive Cards designer. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates an Adaptive Card JSON file with current manage shifts KPIs and RAG indicators.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Generates a read-only Adaptive Card JSON file visualizing manage shifts status from Dynamics 365 F&SCM for a given legal entity, with header, KPI tiles, RAG row, and action buttons.', 'example_request': 'Make an Adaptive Card JSON of manage shifts status for USMF as of 2026-05-24.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-manage-shifts-2026-05-24-card.json.', 'name': 'output_filename'}, {'description': 'Date/timestamp the card snapshot represents.', 'name': 'as_of_date'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a Teams/Outlook-ready Adaptive Card snapshot of manage shifts status from D365 ERP data, without modifying any data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AdaptiveCardManageShifts(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardManageShifts'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'as_of_date': {'description': 'Date/timestamp the card snapshot represents.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-manage-shifts-2026-05-24-card.json.', 'type': 'string'}},
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
    print(AdaptiveCardManageShifts().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
