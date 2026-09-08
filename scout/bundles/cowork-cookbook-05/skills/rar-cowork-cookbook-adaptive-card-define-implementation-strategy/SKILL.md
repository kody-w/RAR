---
name: "rar-cowork-cookbook-adaptive-card-define-implementation-strategy"
description: "Generates a read-only Adaptive Card JSON file visualizing define implementation strategy status from Dynamics 365 F&SCM, with header, KPI tiles, RAG row, and action buttons; call when you need an embeddable status card."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_define_implementation_strategy", "rar_sha256": "050a66cc32795e89116dad87e7882c68b982eaa0034185e07a35197e27a775c3", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
