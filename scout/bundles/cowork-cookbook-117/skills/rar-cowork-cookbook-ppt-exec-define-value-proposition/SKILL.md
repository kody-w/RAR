---
name: "rar-cowork-cookbook-ppt-exec-define-value-proposition"
description: "Builds a read-only executive PowerPoint deck on define value proposition from Dynamics 365 F&SCM data for a given legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_define_value_proposition", "rar_sha256": "88c605848ab3ede41b8c6f48ee6912d1342b5f82984f3d23662788188839973c", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_define_value_proposition`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_define_value_proposition_agent.py` and in the RCI capsule.

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

Define value proposition Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on define value proposition from Dynamics 365 F&SCM data for a given legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-define-value-proposition
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
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "Dynamics 365 legal entity to pull data from, e.g. USMF.",
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
      "description": "Target .pptx filename, e.g. ppt-exec-define-value-proposition-2026-05-24.pptx.",
      "type": "string"
    },
    "reporting_period": {
      "description": "Current period and prior period used for the trend comparison chart.",
      "type": "string"
    },
    "review_length": {
      "description": "Length/format of the review the deck must fit, e.g. 15-minute monthly review.",
      "type": "string"
    },
    "topic": {
      "description": "Subject of the deck, e.g. define value proposition.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_define_value_proposition_agent.py` and embedded as the fenced Python below (sha256 88c605848ab3ede4…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_define_value_proposition_agent.py` first:

```bash
python3 ppt_exec_define_value_proposition_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_define_value_proposition_agent.py   # or on stdin
python3 ppt_exec_define_value_proposition_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define value proposition Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on define value proposition from Dynamics 365 F&SCM data for a given legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-define-value-proposition
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_define_value_proposition',
    "version": '3.0.3',
    "display_name": 'Define value proposition Executive PowerPoint Deck',
    "description": 'Builds a read-only executive PowerPoint deck on define value proposition from Dynamics 365 F&SCM data for a given legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'concept_to_market', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-define-value-proposition',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-define-value-proposition',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'd162af2b76414f2d',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/develop-marketing-strategy/define-value-proposition'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/ppt-exec-define-value-proposition', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to pull data from, e.g. USMF.', 'output_filename': 'Target .pptx filename, e.g. ppt-exec-define-value-proposition-2026-05-24.pptx.', 'reporting_period': 'Current period and prior period used for the trend comparison chart.', 'review_length': 'Length/format of the review the deck must fit, e.g. 15-minute monthly review.', 'topic': 'Subject of the deck, e.g. define value proposition.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Cuts deck prep time from hours to minutes for define value proposition reviews while ensuring the numbers in the slides match D365 to the cent.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build an executive PowerPoint deck on define value proposition for a 15-minute monthly review. Produce 'ppt-exec-define-value-proposition-2026-05-24.pptx' with: (1) title slide, (2) headline KPIs, (3) trend chart vs prior period, (4) top issues / red flags, (5) recommended actions, (6) appendix - data sources and methodology. Include speaker-notes on each slide with talking points. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads define value proposition data and produces a 6-8 slide PowerPoint suitable for an executive review.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only executive PowerPoint deck on define value proposition from Dynamics 365 F&SCM data for a given legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.', 'example_request': 'Build an exec PowerPoint on define value proposition for USMF, 15-minute monthly review, with speaker notes.', 'inputs': [{'description': 'Dynamics 365 legal entity to pull data from, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Subject of the deck, e.g. define value proposition.', 'name': 'topic'}, {'description': 'Length/format of the review the deck must fit, e.g. 15-minute monthly review.', 'name': 'review_length'}, {'description': 'Target .pptx filename, e.g. ppt-exec-define-value-proposition-2026-05-24.pptx.', 'name': 'output_filename'}, {'description': 'Current period and prior period used for the trend comparison chart.', 'name': 'reporting_period'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user needs an executive-ready value proposition status deck for a short monthly review, sourced from D365 ERP without modifying data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class PptExecDefineValueProposition(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecDefineValueProposition'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to pull data from, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Target .pptx filename, e.g. ppt-exec-define-value-proposition-2026-05-24.pptx.', 'type': 'string'}, 'reporting_period': {'description': 'Current period and prior period used for the trend comparison chart.', 'type': 'string'}, 'review_length': {'description': 'Length/format of the review the deck must fit, e.g. 15-minute monthly review.', 'type': 'string'}, 'topic': {'description': 'Subject of the deck, e.g. define value proposition.', 'type': 'string'}},
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
    print(PptExecDefineValueProposition().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
