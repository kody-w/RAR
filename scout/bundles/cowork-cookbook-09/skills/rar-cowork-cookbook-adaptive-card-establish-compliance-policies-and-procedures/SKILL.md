---
name: "rar-cowork-cookbook-adaptive-card-establish-compliance-policies-and-procedures"
description: "Generates a read-only Adaptive Card JSON file summarizing compliance policy and procedure status from Dynamics 365 F&SCM for a legal entity, with KPI tiles, RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_establish_compliance_policies_and_procedures", "rar_sha256": "970f977f243aaa56754ae9194b737ece9db4dae62fc4e77d935d9077c3cfb2f5", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_establish_compliance_policies_and_procedures`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_establish_compliance_policies_and_procedures_agent.py` and in the RCI capsule.

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

Establish compliance policies and procedures Status Adaptive Card — Generates a read-only Adaptive Card JSON file summarizing compliance policy and procedure status from Dynamics 365 F&SCM for a legal entity, with KPI tiles, RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-establish-compliance-policies-and-procedures
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
      "description": "Date used for the card timestamp and file name.",
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
      "description": "Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-establish-compliance-policies-and-procedures-2026-05-24-card.json.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_establish_compliance_policies_and_procedures_agent.py` and embedded as the fenced Python below (sha256 970f977f243aaa56…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_establish_compliance_policies_and_procedures_agent.py` first:

```bash
python3 adaptive_card_establish_compliance_policies_and_procedures_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_establish_compliance_policies_and_procedures_agent.py   # or on stdin
python3 adaptive_card_establish_compliance_policies_and_procedures_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Establish compliance policies and procedures Status Adaptive Card — Generates a read-only Adaptive Card JSON file summarizing compliance policy and procedure status from Dynamics 365 F&SCM for a legal entity, with KPI tiles, RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-establish-compliance-policies-and-procedures
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_establish_compliance_policies_and_procedures',
    "version": '3.0.2',
    "display_name": 'Establish compliance policies and procedures Status Adaptive Card',
    "description": 'Generates a read-only Adaptive Card JSON file summarizing compliance policy and procedure status from Dynamics 365 F&SCM for a legal entity, with KPI tiles, RAG row, and action buttons.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'verified',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'adaptive-card-establish-compliance-policies-and-procedures',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-establish-compliance-policies-and-procedures',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'af3168c1d861d214',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-06-01', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-system-compliance/establish-compliance-policies-and-procedures'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/adaptive-card-establish-compliance-policies-and-procedures', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'as_of_date': 'Date used for the card timestamp and file name.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'output_filename': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-establish-compliance-policies-and-procedures-2026-05-24-card.json.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives any consuming app (Teams, Outlook, custom dashboard) a single canonical establish compliance policies and procedures status card so different surfaces always show the same numbers.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, produce an Adaptive Card JSON file 'adaptive-card-establish-compliance-policies-and-procedures-2026-05-24-card.json' that visualizes the current state of establish compliance policies and procedures. Include: header with title and timestamp, 3-5 KPI tiles with current value + trend arrow, a RAG indicator row, and 2-3 action buttons. The card should render correctly in Teams, Outlook Adaptive Card preview, and the Adaptive Cards designer. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-06-01', 'what_it_does': 'Generates an Adaptive Card JSON file with current establish compliance policies and procedures KPIs and RAG indicators.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Generates a read-only Adaptive Card JSON file summarizing compliance policy and procedure status from Dynamics 365 F&SCM for a legal entity, with KPI tiles, RAG row, and action buttons.', 'example_request': 'Make me an Adaptive Card showing compliance policy status for USMF as of 2026-05-24.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-establish-compliance-policies-and-procedures-2026-05-24-card.json.', 'name': 'output_filename'}, {'description': 'Date used for the card timestamp and file name.', 'name': 'as_of_date'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a shareable Adaptive Card snapshot of compliance policy/procedure status to embed in Teams, Outlook, or a dashboard.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AdaptiveCardEstablishCompliancePoliciesAndProcedures(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardEstablishCompliancePoliciesAndProcedures'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'as_of_date': {'description': 'Date used for the card timestamp and file name.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-establish-compliance-policies-and-procedures-2026-05-24-card.json.', 'type': 'string'}},
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
    print(AdaptiveCardEstablishCompliancePoliciesAndProcedures().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
