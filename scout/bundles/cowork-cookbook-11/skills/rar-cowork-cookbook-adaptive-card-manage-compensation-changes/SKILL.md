---
name: "rar-cowork-cookbook-adaptive-card-manage-compensation-changes"
description: "Generates a read-only Adaptive Card JSON file visualizing manage compensation changes status from Dynamics 365 F&SCM (legal entity USMF), with header, KPI tiles, RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_manage_compensation_changes", "rar_sha256": "0b283c4319422b0d351be034b51ea50e86fd42425eb116ece19c82438c72a4ae", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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
