---
name: "rar-cowork-cookbook-adaptive-card-develop-currency-policies"
description: "Generates a read-only Adaptive Card JSON file visualizing develop currency policies status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, a RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_develop_currency_policies", "rar_sha256": "0666b74f2166c1bb876ceaae50f3e8f5800774ea2126acfeacf17671d4bebf07", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
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
