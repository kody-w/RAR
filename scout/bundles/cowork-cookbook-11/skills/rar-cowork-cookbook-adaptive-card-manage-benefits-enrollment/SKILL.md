---
name: "rar-cowork-cookbook-adaptive-card-manage-benefits-enrollment"
description: "Generates a read-only Adaptive Card JSON file visualizing benefits enrollment status from Dynamics 365 F&SCM (legal entity USMF), with header, KPI tiles, RAG row, and action buttons for Teams/Outlook embedding."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_manage_benefits_enrollment", "rar_sha256": "3bad54e70399f5041da271a94d6c14781b13f022cfc61df624c78c95ec7085a9", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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
