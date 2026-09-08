---
name: "rar-cowork-cookbook-adaptive-card-develop-currency-policies"
description: "Generates a read-only Adaptive Card JSON file visualizing develop currency policies status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, a RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_develop_currency_policies", "rar_sha256": "0666b74f2166c1bb876ceaae50f3e8f5800774ea2126acfeacf17671d4bebf07", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_develop_currency_policies`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_develop_currency_policies_agent.py` and in the RCI capsule.

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

Develop currency policies Status Adaptive Card — Generates a read-only Adaptive Card JSON file visualizing develop currency policies status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, a RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-develop-currency-policies
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
      "description": "Date used for the card timestamp and output filename.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_develop_currency_policies_agent.py` and embedded as the fenced Python below (sha256 0666b74f2166c1bb…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_develop_currency_policies_agent.py` first:

```bash
python3 adaptive_card_develop_currency_policies_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_develop_currency_policies_agent.py   # or on stdin
python3 adaptive_card_develop_currency_policies_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop currency policies Status Adaptive Card — Generates a read-only Adaptive Card JSON file visualizing develop currency policies status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, a RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-develop-currency-policies
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_develop_currency_policies',
    "version": '3.0.2',
    "display_name": 'Develop currency policies Status Adaptive Card',
    "description": 'Generates a read-only Adaptive Card JSON file visualizing develop currency policies status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, a RAG row, and action buttons.',
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
        "upstream_slug": 'adaptive-card-develop-currency-policies',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-develop-currency-policies',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '52b2348b4e0d167b',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/define-accounting-policies/develop-currency-policies'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/adaptive-card-develop-currency-policies', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'as_of_date': 'Date used for the card timestamp and output filename.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report on, e.g. USMF.', 'output_filename': 'Name of the Adaptive Card JSON file to produce.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives any consuming app (Teams, Outlook, custom dashboard) a single canonical develop currency policies status card so different surfaces always show the same numbers.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, produce an Adaptive Card JSON file 'adaptive-card-develop-currency-policies-2026-05-24-card.json' that visualizes the current state of develop currency policies. Include: header with title and timestamp, 3-5 KPI tiles with current value + trend arrow, a RAG indicator row, and 2-3 action buttons. The card should render correctly in Teams, Outlook Adaptive Card preview, and the Adaptive Cards designer. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates an Adaptive Card JSON file with current develop currency policies KPIs and RAG indicators.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Generates a read-only Adaptive Card JSON file visualizing develop currency policies status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, a RAG row, and action buttons.', 'example_request': 'Make an Adaptive Card showing develop currency policies status for USMF as of 2026-05-24.', 'inputs': [{'description': 'D365 legal entity to report on, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Date used for the card timestamp and output filename.', 'name': 'as_of_date'}, {'description': 'Name of the Adaptive Card JSON file to produce.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants an embeddable Adaptive Card snapshot of develop currency policies status for Teams, Outlook, or a dashboard.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AdaptiveCardDevelopCurrencyPolicies(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardDevelopCurrencyPolicies'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'as_of_date': {'description': 'Date used for the card timestamp and output filename.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report on, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Adaptive Card JSON file to produce.', 'type': 'string'}},
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
    print(AdaptiveCardDevelopCurrencyPolicies().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
