---
name: "rar-cowork-cookbook-adaptive-card-manage-compensation-changes"
description: "Generates a read-only Adaptive Card JSON file visualizing manage compensation changes status from Dynamics 365 F&SCM (legal entity USMF), with header, KPI tiles, RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_manage_compensation_changes", "rar_sha256": "0b283c4319422b0d351be034b51ea50e86fd42425eb116ece19c82438c72a4ae", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_manage_compensation_changes`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_manage_compensation_changes_agent.py` and in the RCI capsule.

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

Manage compensation changes Status Adaptive Card — Generates a read-only Adaptive Card JSON file visualizing manage compensation changes status from Dynamics 365 F&SCM (legal entity USMF), with header, KPI tiles, RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-manage-compensation-changes
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
      "description": "Date the snapshot represents, used in the timestamp and output filename.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 F&SCM legal entity to report on, e.g. USMF.",
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
      "description": "Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-manage-compensation-changes-2026-05-24-card.json.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_manage_compensation_changes_agent.py` and embedded as the fenced Python below (sha256 0b283c4319422b0d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_manage_compensation_changes_agent.py` first:

```bash
python3 adaptive_card_manage_compensation_changes_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_manage_compensation_changes_agent.py   # or on stdin
python3 adaptive_card_manage_compensation_changes_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage compensation changes Status Adaptive Card — Generates a read-only Adaptive Card JSON file visualizing manage compensation changes status from Dynamics 365 F&SCM (legal entity USMF), with header, KPI tiles, RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-manage-compensation-changes
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_manage_compensation_changes',
    "version": '3.0.2',
    "display_name": 'Manage compensation changes Status Adaptive Card',
    "description": 'Generates a read-only Adaptive Card JSON file visualizing manage compensation changes status from Dynamics 365 F&SCM (legal entity USMF), with header, KPI tiles, RAG row, and action buttons.',
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
        "upstream_slug": 'adaptive-card-manage-compensation-changes',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-manage-compensation-changes',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '432484dfb3781846',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/manage-compensation-and-benefits/manage-compensation-changes'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/adaptive-card-manage-compensation-changes', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'as_of_date': 'Date the snapshot represents, used in the timestamp and output filename.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 F&SCM legal entity to report on, e.g. USMF.', 'output_filename': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-manage-compensation-changes-2026-05-24-card.json.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives any consuming app (Teams, Outlook, custom dashboard) a single canonical manage compensation changes status card so different surfaces always show the same numbers.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, produce an Adaptive Card JSON file 'adaptive-card-manage-compensation-changes-2026-05-24-card.json' that visualizes the current state of manage compensation changes. Include: header with title and timestamp, 3-5 KPI tiles with current value + trend arrow, a RAG indicator row, and 2-3 action buttons. The card should render correctly in Teams, Outlook Adaptive Card preview, and the Adaptive Cards designer. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates an Adaptive Card JSON file with current manage compensation changes KPIs and RAG indicators.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Generates a read-only Adaptive Card JSON file visualizing manage compensation changes status from Dynamics 365 F&SCM (legal entity USMF), with header, KPI tiles, RAG row, and action buttons.', 'example_request': 'Make me an Adaptive Card showing manage compensation changes status for USMF as of 2026-05-24.', 'inputs': [{'description': 'D365 F&SCM legal entity to report on, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Date the snapshot represents, used in the timestamp and output filename.', 'name': 'as_of_date'}, {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-manage-compensation-changes-2026-05-24-card.json.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a shareable Adaptive Card snapshot of compensation change status for Teams, Outlook, or a dashboard, without changing D365 data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AdaptiveCardManageCompensationChanges(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardManageCompensationChanges'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'as_of_date': {'description': 'Date the snapshot represents, used in the timestamp and output filename.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 F&SCM legal entity to report on, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-manage-compensation-changes-2026-05-24-card.json.', 'type': 'string'}},
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
    print(AdaptiveCardManageCompensationChanges().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
