---
name: "rar-cowork-cookbook-adaptive-card-manage-shifts"
description: "Generates a read-only Adaptive Card JSON file visualizing manage shifts status from Dynamics 365 F&SCM for a given legal entity, with header, KPI tiles, RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_manage_shifts", "rar_sha256": "27c430835e0a3887298eb923f634b91baf191441a16edc1e3fc10292c67d6db4", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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
