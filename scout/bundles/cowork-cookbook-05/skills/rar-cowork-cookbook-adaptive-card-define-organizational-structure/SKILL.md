---
name: "rar-cowork-cookbook-adaptive-card-define-organizational-structure"
description: "Generates a read-only Adaptive Card JSON file summarizing organizational-structure status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_define_organizational_structure", "rar_sha256": "c8969fea9d587f161b729a3503a8816f3044d8f7288eb0aa5b9b18a7785cd0db", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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
