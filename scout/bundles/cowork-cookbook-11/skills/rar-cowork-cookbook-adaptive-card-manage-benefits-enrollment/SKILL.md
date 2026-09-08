---
name: "rar-cowork-cookbook-adaptive-card-manage-benefits-enrollment"
description: "Generates a read-only Adaptive Card JSON file visualizing benefits enrollment status from Dynamics 365 F&SCM (legal entity USMF), with header, KPI tiles, RAG row, and action buttons for Teams/Outlook embedding."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_manage_benefits_enrollment", "rar_sha256": "3bad54e70399f5041da271a94d6c14781b13f022cfc61df624c78c95ec7085a9", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_manage_benefits_enrollment`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_manage_benefits_enrollment_agent.py` and in the RCI capsule.

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

Manage benefits enrollment Status Adaptive Card — Generates a read-only Adaptive Card JSON file visualizing benefits enrollment status from Dynamics 365 F&SCM (legal entity USMF), with header, KPI tiles, RAG row, and action buttons for Teams/Outlook embedding.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-manage-benefits-enrollment
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
      "description": "The 2-3 action buttons to place on the card.",
      "type": "string"
    },
    "as_of_date": {
      "description": "Snapshot date used in the card timestamp and output filename.",
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
      "description": "D365 legal entity to report on, e.g. USMF.",
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
      "description": "Name of the Adaptive Card JSON file to produce.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_manage_benefits_enrollment_agent.py` and embedded as the fenced Python below (sha256 3bad54e70399f504…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_manage_benefits_enrollment_agent.py` first:

```bash
python3 adaptive_card_manage_benefits_enrollment_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_manage_benefits_enrollment_agent.py   # or on stdin
python3 adaptive_card_manage_benefits_enrollment_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage benefits enrollment Status Adaptive Card — Generates a read-only Adaptive Card JSON file visualizing benefits enrollment status from Dynamics 365 F&SCM (legal entity USMF), with header, KPI tiles, RAG row, and action buttons for Teams/Outlook embedding.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-manage-benefits-enrollment
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_manage_benefits_enrollment',
    "version": '3.0.2',
    "display_name": 'Manage benefits enrollment Status Adaptive Card',
    "description": 'Generates a read-only Adaptive Card JSON file visualizing benefits enrollment status from Dynamics 365 F&SCM (legal entity USMF), with header, KPI tiles, RAG row, and action buttons for Teams/Outlook embedding.',
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
        "upstream_slug": 'adaptive-card-manage-benefits-enrollment',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-manage-benefits-enrollment',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'cf55b050cb09554d',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/manage-compensation-and-benefits/manage-benefits-enrollment'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/adaptive-card-manage-benefits-enrollment', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'action_buttons': 'The 2-3 action buttons to place on the card.', 'as_of_date': 'Snapshot date used in the card timestamp and output filename.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'kpi_count': 'How many KPI tiles to include (3-5).', 'legal_entity': 'D365 legal entity to report on, e.g. USMF.', 'output_filename': 'Name of the Adaptive Card JSON file to produce.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives any consuming app (Teams, Outlook, custom dashboard) a single canonical manage benefits enrollment status card so different surfaces always show the same numbers.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, produce an Adaptive Card JSON file 'adaptive-card-manage-benefits-enrollment-2026-05-24-card.json' that visualizes the current state of manage benefits enrollment. Include: header with title and timestamp, 3-5 KPI tiles with current value + trend arrow, a RAG indicator row, and 2-3 action buttons. The card should render correctly in Teams, Outlook Adaptive Card preview, and the Adaptive Cards designer. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates an Adaptive Card JSON file with current manage benefits enrollment KPIs and RAG indicators.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Generates a read-only Adaptive Card JSON file visualizing benefits enrollment status from Dynamics 365 F&SCM (legal entity USMF), with header, KPI tiles, RAG row, and action buttons for Teams/Outlook embedding.', 'example_request': 'Make an Adaptive Card showing benefits enrollment status for USMF as of 2026-05-24.', 'inputs': [{'description': 'D365 legal entity to report on, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Snapshot date used in the card timestamp and output filename.', 'name': 'as_of_date'}, {'description': 'Name of the Adaptive Card JSON file to produce.', 'name': 'output_filename'}, {'description': 'How many KPI tiles to include (3-5).', 'name': 'kpi_count'}, {'description': 'The 2-3 action buttons to place on the card.', 'name': 'action_buttons'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a shareable Adaptive Card snapshot of benefits enrollment status from D365 ERP for a dashboard, email, or Teams message.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AdaptiveCardManageBenefitsEnrollment(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardManageBenefitsEnrollment'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'action_buttons': {'description': 'The 2-3 action buttons to place on the card.', 'type': 'string'}, 'as_of_date': {'description': 'Snapshot date used in the card timestamp and output filename.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'kpi_count': {'description': 'How many KPI tiles to include (3-5).', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report on, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Adaptive Card JSON file to produce.', 'type': 'string'}},
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
    print(AdaptiveCardManageBenefitsEnrollment().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
