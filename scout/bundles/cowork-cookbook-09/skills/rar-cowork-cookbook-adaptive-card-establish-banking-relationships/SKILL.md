---
name: "rar-cowork-cookbook-adaptive-card-establish-banking-relationships"
description: "Generates a read-only Adaptive Card JSON file summarizing establish-banking-relationships status from Dynamics 365 F&SCM for a legal entity, with KPI tiles, RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_establish_banking_relationships", "rar_sha256": "7f1c9a81580c7188ac195a7021863c002acd9d3ef8b0df99334720495e997e12", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_establish_banking_relationships`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_establish_banking_relationships_agent.py` and in the RCI capsule.

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

Establish banking relationships Status Adaptive Card — Generates a read-only Adaptive Card JSON file summarizing establish-banking-relationships status from Dynamics 365 F&SCM for a legal entity, with KPI tiles, RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-establish-banking-relationships
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
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to report on (e.g. USMF).",
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
    },
    "snapshot_date": {
      "description": "Date used for the card timestamp and output filename.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_establish_banking_relationships_agent.py` and embedded as the fenced Python below (sha256 7f1c9a81580c7188…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_establish_banking_relationships_agent.py` first:

```bash
python3 adaptive_card_establish_banking_relationships_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_establish_banking_relationships_agent.py   # or on stdin
python3 adaptive_card_establish_banking_relationships_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Establish banking relationships Status Adaptive Card — Generates a read-only Adaptive Card JSON file summarizing establish-banking-relationships status from Dynamics 365 F&SCM for a legal entity, with KPI tiles, RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-establish-banking-relationships
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_establish_banking_relationships',
    "version": '3.0.2',
    "display_name": 'Establish banking relationships Status Adaptive Card',
    "description": 'Generates a read-only Adaptive Card JSON file summarizing establish-banking-relationships status from Dynamics 365 F&SCM for a legal entity, with KPI tiles, RAG row, and action buttons.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-establish-banking-relationships',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-establish-banking-relationships',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '8a2e28176b24d2e1',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/manage-cash/establish-banking-relationships'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/adaptive-card-establish-banking-relationships', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report on (e.g. USMF).', 'output_filename': 'Name of the Adaptive Card JSON file to produce.', 'snapshot_date': 'Date used for the card timestamp and output filename.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives any consuming app (Teams, Outlook, custom dashboard) a single canonical establish banking relationships status card so different surfaces always show the same numbers.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, produce an Adaptive Card JSON file 'adaptive-card-establish-banking-relationships-2026-05-24-card.json' that visualizes the current state of establish banking relationships. Include: header with title and timestamp, 3-5 KPI tiles with current value + trend arrow, a RAG indicator row, and 2-3 action buttons. The card should render correctly in Teams, Outlook Adaptive Card preview, and the Adaptive Cards designer. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates an Adaptive Card JSON file with current establish banking relationships KPIs and RAG indicators.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Generates a read-only Adaptive Card JSON file summarizing establish-banking-relationships status from Dynamics 365 F&SCM for a legal entity, with KPI tiles, RAG row, and action buttons.', 'example_request': 'Make an Adaptive Card showing establish banking relationships status for USMF as of 2026-05-24.', 'inputs': [{'description': 'D365 legal entity to report on (e.g. USMF).', 'name': 'legal_entity'}, {'description': 'Date used for the card timestamp and output filename.', 'name': 'snapshot_date'}, {'description': 'Name of the Adaptive Card JSON file to produce.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a Teams/Outlook-ready Adaptive Card snapshot of establish banking relationships status from D365 ERP data, without changing any data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AdaptiveCardEstablishBankingRelationships(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardEstablishBankingRelationships'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report on (e.g. USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Adaptive Card JSON file to produce.', 'type': 'string'}, 'snapshot_date': {'description': 'Date used for the card timestamp and output filename.', 'type': 'string'}},
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
    print(AdaptiveCardEstablishBankingRelationships().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
