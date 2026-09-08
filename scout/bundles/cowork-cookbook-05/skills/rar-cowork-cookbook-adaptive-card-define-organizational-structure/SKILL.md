---
name: "rar-cowork-cookbook-adaptive-card-define-organizational-structure"
description: "Generates a read-only Adaptive Card JSON file summarizing organizational-structure status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_define_organizational_structure", "rar_sha256": "c8969fea9d587f161b729a3503a8816f3044d8f7288eb0aa5b9b18a7785cd0db", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_define_organizational_structure`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_define_organizational_structure_agent.py` and in the RCI capsule.

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

Define organizational structure Status Adaptive Card — Generates a read-only Adaptive Card JSON file summarizing organizational-structure status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-define-organizational-structure
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
      "description": "Date/timestamp shown in the card header and used in the filename.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
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
      "description": "Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-define-organizational-structure-2026-05-24-card.json.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_define_organizational_structure_agent.py` and embedded as the fenced Python below (sha256 c8969fea9d587f16…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_define_organizational_structure_agent.py` first:

```bash
python3 adaptive_card_define_organizational_structure_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_define_organizational_structure_agent.py   # or on stdin
python3 adaptive_card_define_organizational_structure_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define organizational structure Status Adaptive Card — Generates a read-only Adaptive Card JSON file summarizing organizational-structure status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-define-organizational-structure
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_define_organizational_structure',
    "version": '3.0.2',
    "display_name": 'Define organizational structure Status Adaptive Card',
    "description": 'Generates a read-only Adaptive Card JSON file summarizing organizational-structure status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, RAG row, and action buttons.',
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
        "upstream_slug": 'adaptive-card-define-organizational-structure',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-define-organizational-structure',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'e86d953023e6ca10',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/develop-people-strategy/define-organizational-structure'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/adaptive-card-define-organizational-structure', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'as_of_date': 'Date/timestamp shown in the card header and used in the filename.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report on, e.g. USMF.', 'output_filename': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-define-organizational-structure-2026-05-24-card.json.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives any consuming app (Teams, Outlook, custom dashboard) a single canonical define organizational structure status card so different surfaces always show the same numbers.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, produce an Adaptive Card JSON file 'adaptive-card-define-organizational-structure-2026-05-24-card.json' that visualizes the current state of define organizational structure. Include: header with title and timestamp, 3-5 KPI tiles with current value + trend arrow, a RAG indicator row, and 2-3 action buttons. The card should render correctly in Teams, Outlook Adaptive Card preview, and the Adaptive Cards designer. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates an Adaptive Card JSON file with current define organizational structure KPIs and RAG indicators.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Generates a read-only Adaptive Card JSON file summarizing organizational-structure status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, RAG row, and action buttons.', 'example_request': 'Make me an Adaptive Card JSON of define organizational structure status for USMF as of 2026-05-24.', 'inputs': [{'description': 'D365 legal entity to report on, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-define-organizational-structure-2026-05-24-card.json.', 'name': 'output_filename'}, {'description': 'Date/timestamp shown in the card header and used in the filename.', 'name': 'as_of_date'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants an Adaptive Card snapshot of D365 organizational-structure status to embed in Teams, Outlook, or a dashboard, without changing data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AdaptiveCardDefineOrganizationalStructure(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardDefineOrganizationalStructure'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'as_of_date': {'description': 'Date/timestamp shown in the card header and used in the filename.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report on, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-define-organizational-structure-2026-05-24-card.json.', 'type': 'string'}},
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
    print(AdaptiveCardDefineOrganizationalStructure().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
