---
name: "rar-cowork-cookbook-adaptive-card-develop-financial-period-strategy"
description: "Generates a read-only Adaptive Card JSON file visualizing develop financial period strategy status from Dynamics 365 F&SCM (legal entity USMF), with header, 3-5 KPI tiles, RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_develop_financial_period_strategy", "rar_sha256": "9910c086f4ae0d201d5096ce4876386dd2d5c9249913dae3117a78460c25b9ba", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_develop_financial_period_strategy`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_develop_financial_period_strategy_agent.py` and in the RCI capsule.

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

Develop financial period strategy Status Adaptive Card — Generates a read-only Adaptive Card JSON file visualizing develop financial period strategy status from Dynamics 365 F&SCM (legal entity USMF), with header, 3-5 KPI tiles, RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-develop-financial-period-strategy
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
      "description": "Date the status snapshot represents, used in the output filename and card timestamp.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "Dynamics 365 legal entity to read from, e.g. USMF.",
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
      "description": "Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-develop-financial-period-strategy-2026-05-24-card.json.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_develop_financial_period_strategy_agent.py` and embedded as the fenced Python below (sha256 9910c086f4ae0d20…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_develop_financial_period_strategy_agent.py` first:

```bash
python3 adaptive_card_develop_financial_period_strategy_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_develop_financial_period_strategy_agent.py   # or on stdin
python3 adaptive_card_develop_financial_period_strategy_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop financial period strategy Status Adaptive Card — Generates a read-only Adaptive Card JSON file visualizing develop financial period strategy status from Dynamics 365 F&SCM (legal entity USMF), with header, 3-5 KPI tiles, RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-develop-financial-period-strategy
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_develop_financial_period_strategy',
    "version": '3.0.2',
    "display_name": 'Develop financial period strategy Status Adaptive Card',
    "description": 'Generates a read-only Adaptive Card JSON file visualizing develop financial period strategy status from Dynamics 365 F&SCM (legal entity USMF), with header, 3-5 KPI tiles, RAG row, and action buttons.',
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
        "upstream_slug": 'adaptive-card-develop-financial-period-strategy',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-develop-financial-period-strategy',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'f82e41cefe246077',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/define-accounting-policies/develop-financial-period-strategy'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/adaptive-card-develop-financial-period-strategy', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'as_of_date': 'Date the status snapshot represents, used in the output filename and card timestamp.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to read from, e.g. USMF.', 'output_filename': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-develop-financial-period-strategy-2026-05-24-card.json.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives any consuming app (Teams, Outlook, custom dashboard) a single canonical develop financial period strategy status card so different surfaces always show the same numbers.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, produce an Adaptive Card JSON file 'adaptive-card-develop-financial-period-strategy-2026-05-24-card.json' that visualizes the current state of develop financial period strategy. Include: header with title and timestamp, 3-5 KPI tiles with current value + trend arrow, a RAG indicator row, and 2-3 action buttons. The card should render correctly in Teams, Outlook Adaptive Card preview, and the Adaptive Cards designer. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates an Adaptive Card JSON file with current develop financial period strategy KPIs and RAG indicators.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Generates a read-only Adaptive Card JSON file visualizing develop financial period strategy status from Dynamics 365 F&SCM (legal entity USMF), with header, 3-5 KPI tiles, RAG row, and action buttons.', 'example_request': 'Make an Adaptive Card showing develop financial period strategy status for USMF as of 2026-05-24.', 'inputs': [{'description': 'Dynamics 365 legal entity to read from, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Date the status snapshot represents, used in the output filename and card timestamp.', 'name': 'as_of_date'}, {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-develop-financial-period-strategy-2026-05-24-card.json.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants an Adaptive Card snapshot of develop financial period strategy status to embed in Teams, Outlook, or a dashboard. No data is modified.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AdaptiveCardDevelopFinancialPeriodStrategy(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardDevelopFinancialPeriodStrategy'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'as_of_date': {'description': 'Date the status snapshot represents, used in the output filename and card timestamp.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to read from, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-develop-financial-period-strategy-2026-05-24-card.json.', 'type': 'string'}},
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
    print(AdaptiveCardDevelopFinancialPeriodStrategy().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
