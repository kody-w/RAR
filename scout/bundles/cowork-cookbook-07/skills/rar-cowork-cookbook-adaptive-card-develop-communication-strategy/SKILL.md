---
name: "rar-cowork-cookbook-adaptive-card-develop-communication-strategy"
description: "Generates a read-only Adaptive Card JSON file visualizing develop communication strategy status from Dynamics 365 F&SCM (legal entity USMF), with header, KPI tiles, RAG row, and action buttons; call when you need an embe"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_develop_communication_strategy", "rar_sha256": "2cabff56aa14efb9c846b6a805d8239a725ec573ac08ad3481880ccce2cd03ad", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_develop_communication_strategy`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_develop_communication_strategy_agent.py` and in the RCI capsule.

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

Develop communication strategy Status Adaptive Card — Generates a read-only Adaptive Card JSON file visualizing develop communication strategy status from Dynamics 365 F&SCM (legal entity USMF), with header, KPI tiles, RAG row, and action buttons; call when you need an embe

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-develop-communication-strategy
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
      "description": "Date used for the card timestamp and filename.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 F&SCM legal entity to read from (recipe default: USMF).",
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
      "description": "Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-develop-communication-strategy-2026-05-24-card.json.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_develop_communication_strategy_agent.py` and embedded as the fenced Python below (sha256 2cabff56aa14efb9…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_develop_communication_strategy_agent.py` first:

```bash
python3 adaptive_card_develop_communication_strategy_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_develop_communication_strategy_agent.py   # or on stdin
python3 adaptive_card_develop_communication_strategy_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop communication strategy Status Adaptive Card — Generates a read-only Adaptive Card JSON file visualizing develop communication strategy status from Dynamics 365 F&SCM (legal entity USMF), with header, KPI tiles, RAG row, and action buttons; call when you need an embe

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-develop-communication-strategy
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_develop_communication_strategy',
    "version": '3.0.2',
    "display_name": 'Develop communication strategy Status Adaptive Card',
    "description": 'Generates a read-only Adaptive Card JSON file visualizing develop communication strategy status from Dynamics 365 F&SCM (legal entity USMF), with header, KPI tiles, RAG row, and action buttons; call when you need an embe',
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
        "upstream_slug": 'adaptive-card-develop-communication-strategy',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-develop-communication-strategy',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '76b045d11a4f4b4e',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/develop-people-strategy/develop-communication-strategy'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/adaptive-card-develop-communication-strategy', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'as_of_date': 'Date used for the card timestamp and filename.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 F&SCM legal entity to read from (recipe default: USMF).', 'output_filename': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-develop-communication-strategy-2026-05-24-card.json.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives any consuming app (Teams, Outlook, custom dashboard) a single canonical develop communication strategy status card so different surfaces always show the same numbers.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, produce an Adaptive Card JSON file 'adaptive-card-develop-communication-strategy-2026-05-24-card.json' that visualizes the current state of develop communication strategy. Include: header with title and timestamp, 3-5 KPI tiles with current value + trend arrow, a RAG indicator row, and 2-3 action buttons. The card should render correctly in Teams, Outlook Adaptive Card preview, and the Adaptive Cards designer. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates an Adaptive Card JSON file with current develop communication strategy KPIs and RAG indicators.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Generates a read-only Adaptive Card JSON file visualizing develop communication strategy status from Dynamics 365 F&SCM (legal entity USMF), with header, KPI tiles, RAG row, and action buttons; call when you need an embe', 'example_request': 'Make an Adaptive Card JSON for develop communication strategy status in USMF as of 2026-05-24.', 'inputs': [{'description': 'D365 F&SCM legal entity to read from (recipe default: USMF).', 'name': 'legal_entity'}, {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-develop-communication-strategy-2026-05-24-card.json.', 'name': 'output_filename'}, {'description': 'Date used for the card timestamp and filename.', 'name': 'as_of_date'}], 'model': 'claude-opus-5', 'when_to_use': 'Use when you want a Teams/Outlook/designer-compatible Adaptive Card snapshot of develop communication strategy status from D365 ERP, without changing any data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AdaptiveCardDevelopCommunicationStrategy(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardDevelopCommunicationStrategy'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'as_of_date': {'description': 'Date used for the card timestamp and filename.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 F&SCM legal entity to read from (recipe default: USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-develop-communication-strategy-2026-05-24-card.json.', 'type': 'string'}},
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
    print(AdaptiveCardDevelopCommunicationStrategy().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
