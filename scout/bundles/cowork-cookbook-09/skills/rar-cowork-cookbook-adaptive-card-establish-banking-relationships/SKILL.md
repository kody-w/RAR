---
name: "rar-cowork-cookbook-adaptive-card-establish-banking-relationships"
description: "Generates a read-only Adaptive Card JSON file summarizing establish-banking-relationships status from Dynamics 365 F&SCM for a legal entity, with KPI tiles, RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_establish_banking_relationships", "rar_sha256": "7f1c9a81580c7188ac195a7021863c002acd9d3ef8b0df99334720495e997e12", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
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
