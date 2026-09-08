---
name: "rar-cowork-cookbook-adaptive-card-develop-support-transition-strategy"
description: "Generates a read-only Adaptive Card JSON file summarizing support transition strategy status from Dynamics 365 ERP for a legal entity, with header, KPI tiles, RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_develop_support_transition_strategy", "rar_sha256": "0b7d5d57dc6b898408857a7aafbf906c46c018c0f3277574a8c88699762864a8", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
