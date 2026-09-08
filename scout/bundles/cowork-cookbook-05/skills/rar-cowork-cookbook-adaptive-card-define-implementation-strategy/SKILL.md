---
name: "rar-cowork-cookbook-adaptive-card-define-implementation-strategy"
description: "Generates a read-only Adaptive Card JSON file visualizing define implementation strategy status from Dynamics 365 F&SCM, with header, KPI tiles, RAG row, and action buttons; call when you need an embeddable status card."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_define_implementation_strategy", "rar_sha256": "050a66cc32795e89116dad87e7882c68b982eaa0034185e07a35197e27a775c3", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_define_implementation_strategy`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_define_implementation_strategy_agent.py` and in the RCI capsule.

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

Define implementation strategy Status Adaptive Card — Generates a read-only Adaptive Card JSON file visualizing define implementation strategy status from Dynamics 365 F&SCM, with header, KPI tiles, RAG row, and action buttons; call when you need an embeddable status card.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-define-implementation-strategy
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
      "description": "Date used in the card timestamp and filename.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to read from, e.g. USMF.",
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
      "description": "Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-define-implementation-strategy-2026-05-24-card.json.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_define_implementation_strategy_agent.py` and embedded as the fenced Python below (sha256 050a66cc32795e89…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_define_implementation_strategy_agent.py` first:

```bash
python3 adaptive_card_define_implementation_strategy_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_define_implementation_strategy_agent.py   # or on stdin
python3 adaptive_card_define_implementation_strategy_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define implementation strategy Status Adaptive Card — Generates a read-only Adaptive Card JSON file visualizing define implementation strategy status from Dynamics 365 F&SCM, with header, KPI tiles, RAG row, and action buttons; call when you need an embeddable status card.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-define-implementation-strategy
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_define_implementation_strategy',
    "version": '3.0.2',
    "display_name": 'Define implementation strategy Status Adaptive Card',
    "description": 'Generates a read-only Adaptive Card JSON file visualizing define implementation strategy status from Dynamics 365 F&SCM, with header, KPI tiles, RAG row, and action buttons; call when you need an embeddable status card.',
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
        "upstream_slug": 'adaptive-card-define-implementation-strategy',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-define-implementation-strategy',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '3281b94ee3fdeb5c',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-06-01', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/implement-solutions/define-implementation-strategy'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/adaptive-card-define-implementation-strategy', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'as_of_date': 'Date used in the card timestamp and filename.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to read from, e.g. USMF.', 'output_filename': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-define-implementation-strategy-2026-05-24-card.json.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives any consuming app (Teams, Outlook, custom dashboard) a single canonical define implementation strategy status card so different surfaces always show the same numbers.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, produce an Adaptive Card JSON file 'adaptive-card-define-implementation-strategy-2026-05-24-card.json' that visualizes the current state of define implementation strategy. Include: header with title and timestamp, 3-5 KPI tiles with current value + trend arrow, a RAG indicator row, and 2-3 action buttons. The card should render correctly in Teams, Outlook Adaptive Card preview, and the Adaptive Cards designer. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-06-01', 'what_it_does': 'Generates an Adaptive Card JSON file with current define implementation strategy KPIs and RAG indicators.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Generates a read-only Adaptive Card JSON file visualizing define implementation strategy status from Dynamics 365 F&SCM, with header, KPI tiles, RAG row, and action buttons; call when you need an embeddable status card.', 'example_request': 'Make an Adaptive Card JSON for define implementation strategy status in USMF as of 2026-05-24.', 'inputs': [{'description': 'D365 legal entity to read from, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-define-implementation-strategy-2026-05-24-card.json.', 'name': 'output_filename'}, {'description': 'Date used in the card timestamp and filename.', 'name': 'as_of_date'}], 'model': 'claude-opus-5', 'when_to_use': 'Use when you want a Teams/Outlook-ready Adaptive Card snapshot of define implementation strategy status from D365 ERP data, without modifying any data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AdaptiveCardDefineImplementationStrategy(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardDefineImplementationStrategy'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'as_of_date': {'description': 'Date used in the card timestamp and filename.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to read from, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-define-implementation-strategy-2026-05-24-card.json.', 'type': 'string'}},
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
    print(AdaptiveCardDefineImplementationStrategy().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
