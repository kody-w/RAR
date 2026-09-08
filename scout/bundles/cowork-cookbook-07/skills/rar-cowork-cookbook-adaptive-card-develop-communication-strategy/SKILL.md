---
name: "rar-cowork-cookbook-adaptive-card-develop-communication-strategy"
description: "Generates a read-only Adaptive Card JSON file visualizing develop communication strategy status from Dynamics 365 F&SCM (legal entity USMF), with header, KPI tiles, RAG row, and action buttons; call when you need an embe"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_develop_communication_strategy", "rar_sha256": "2cabff56aa14efb9c846b6a805d8239a725ec573ac08ad3481880ccce2cd03ad", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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
