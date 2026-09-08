---
name: "rar-cowork-cookbook-ppt-exec-define-value-proposition"
description: "Builds a read-only executive PowerPoint deck on define value proposition from Dynamics 365 F&SCM data for a given legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_define_value_proposition", "rar_sha256": "88c605848ab3ede41b8c6f48ee6912d1342b5f82984f3d23662788188839973c", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
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
