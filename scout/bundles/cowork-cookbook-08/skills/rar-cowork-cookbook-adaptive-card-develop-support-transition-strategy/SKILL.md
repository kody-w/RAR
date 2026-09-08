---
name: "rar-cowork-cookbook-adaptive-card-develop-support-transition-strategy"
description: "Generates a read-only Adaptive Card JSON file summarizing support transition strategy status from Dynamics 365 ERP for a legal entity, with header, KPI tiles, RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_develop_support_transition_strategy", "rar_sha256": "0b7d5d57dc6b898408857a7aafbf906c46c018c0f3277574a8c88699762864a8", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_develop_support_transition_strategy`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_develop_support_transition_strategy_agent.py` and in the RCI capsule.

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

Develop support transition strategy Status Adaptive Card — Generates a read-only Adaptive Card JSON file summarizing support transition strategy status from Dynamics 365 ERP for a legal entity, with header, KPI tiles, RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-develop-support-transition-strategy
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
      "description": "Date the status snapshot represents, used in the card timestamp and filename.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_develop_support_transition_strategy_agent.py` and embedded as the fenced Python below (sha256 0b7d5d57dc6b8984…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_develop_support_transition_strategy_agent.py` first:

```bash
python3 adaptive_card_develop_support_transition_strategy_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_develop_support_transition_strategy_agent.py   # or on stdin
python3 adaptive_card_develop_support_transition_strategy_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop support transition strategy Status Adaptive Card — Generates a read-only Adaptive Card JSON file summarizing support transition strategy status from Dynamics 365 ERP for a legal entity, with header, KPI tiles, RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-develop-support-transition-strategy
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_develop_support_transition_strategy',
    "version": '3.0.2',
    "display_name": 'Develop support transition strategy Status Adaptive Card',
    "description": 'Generates a read-only Adaptive Card JSON file summarizing support transition strategy status from Dynamics 365 ERP for a legal entity, with header, KPI tiles, RAG row, and action buttons.',
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
        "upstream_slug": 'adaptive-card-develop-support-transition-strategy',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-develop-support-transition-strategy',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '72b8ec39fff52fda',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-06-01', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/support-systems/develop-support-transition-strategy'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/adaptive-card-develop-support-transition-strategy', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'as_of_date': 'Date the status snapshot represents, used in the card timestamp and filename.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'output_filename': 'Name of the Adaptive Card JSON file to produce.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives any consuming app (Teams, Outlook, custom dashboard) a single canonical develop support transition strategy status card so different surfaces always show the same numbers.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, produce an Adaptive Card JSON file 'adaptive-card-develop-support-transition-strategy-2026-05-24-card.json' that visualizes the current state of develop support transition strategy. Include: header with title and timestamp, 3-5 KPI tiles with current value + trend arrow, a RAG indicator row, and 2-3 action buttons. The card should render correctly in Teams, Outlook Adaptive Card preview, and the Adaptive Cards designer. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-06-01', 'what_it_does': 'Generates an Adaptive Card JSON file with current develop support transition strategy KPIs and RAG indicators.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Generates a read-only Adaptive Card JSON file summarizing support transition strategy status from Dynamics 365 ERP for a legal entity, with header, KPI tiles, RAG row, and action buttons.', 'example_request': 'Make an Adaptive Card for our support transition strategy status in USMF as of 2026-05-24.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Name of the Adaptive Card JSON file to produce.', 'name': 'output_filename'}, {'description': 'Date the status snapshot represents, used in the card timestamp and filename.', 'name': 'as_of_date'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants an Adaptive Card snapshot of support transition strategy status from D365 F&SCM to embed in Teams, Outlook, or a dashboard.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AdaptiveCardDevelopSupportTransitionStrategy(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardDevelopSupportTransitionStrategy'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'as_of_date': {'description': 'Date the status snapshot represents, used in the card timestamp and filename.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Adaptive Card JSON file to produce.', 'type': 'string'}},
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
    print(AdaptiveCardDevelopSupportTransitionStrategy().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
