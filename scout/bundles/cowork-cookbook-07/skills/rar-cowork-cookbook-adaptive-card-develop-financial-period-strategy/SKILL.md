---
name: "rar-cowork-cookbook-adaptive-card-develop-financial-period-strategy"
description: "Generates a read-only Adaptive Card JSON file visualizing develop financial period strategy status from Dynamics 365 F&SCM (legal entity USMF), with header, 3-5 KPI tiles, RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_develop_financial_period_strategy", "rar_sha256": "9910c086f4ae0d201d5096ce4876386dd2d5c9249913dae3117a78460c25b9ba", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
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
