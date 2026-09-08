---
name: "rar-cowork-cookbook-ppt-exec-analyze-case-patterns"
description: "Builds a read-only executive PowerPoint deck on case-pattern analysis from Dynamics 365 F&SCM data for a named legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_analyze_case_patterns", "rar_sha256": "1461e173c36d55eeb3c7c4f4b0aebc7e984492b96ec2f29c8cac31e3126eab43", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_analyze_case_patterns`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_analyze_case_patterns_agent.py` and in the RCI capsule.

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

Analyze case patterns Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on case-pattern analysis from Dynamics 365 F&SCM data for a named legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-analyze-case-patterns
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
    "comparison_period": {
      "description": "Prior period to chart the trend against.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to pull from, e.g. USMF.",
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
      "description": "Name of the .pptx file to produce, e.g. ppt-exec-analyze-case-patterns-2026-05-24.pptx.",
      "type": "string"
    },
    "review_period": {
      "description": "Review cadence and length the deck is sized for, e.g. 15-minute monthly review.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_analyze_case_patterns_agent.py` and embedded as the fenced Python below (sha256 1461e173c36d55ee…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_analyze_case_patterns_agent.py` first:

```bash
python3 ppt_exec_analyze_case_patterns_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_analyze_case_patterns_agent.py   # or on stdin
python3 ppt_exec_analyze_case_patterns_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Analyze case patterns Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on case-pattern analysis from Dynamics 365 F&SCM data for a named legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-analyze-case-patterns
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_analyze_case_patterns',
    "version": '3.0.3',
    "display_name": 'Analyze case patterns Executive PowerPoint Deck',
    "description": 'Builds a read-only executive PowerPoint deck on case-pattern analysis from Dynamics 365 F&SCM data for a named legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'case_to_resolution', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-analyze-case-patterns',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-analyze-case-patterns',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '27834d06201b5525',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/analyze-case-performance/analyze-case-patterns'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/ppt-exec-analyze-case-patterns', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'comparison_period': 'Prior period to chart the trend against.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to pull from, e.g. USMF.', 'output_filename': 'Name of the .pptx file to produce, e.g. ppt-exec-analyze-case-patterns-2026-05-24.pptx.', 'review_period': 'Review cadence and length the deck is sized for, e.g. 15-minute monthly review.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Cuts deck prep time from hours to minutes for analyze case patterns reviews while ensuring the numbers in the slides match D365 to the cent.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build an executive PowerPoint deck on analyze case patterns for a 15-minute monthly review. Produce 'ppt-exec-analyze-case-patterns-2026-05-24.pptx' with: (1) title slide, (2) headline KPIs, (3) trend chart vs prior period, (4) top issues / red flags, (5) recommended actions, (6) appendix - data sources and methodology. Include speaker-notes on each slide with talking points. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads analyze case patterns data and produces a 6-8 slide PowerPoint suitable for an executive review.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only executive PowerPoint deck on case-pattern analysis from Dynamics 365 F&SCM data for a named legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.', 'example_request': 'Build an exec PowerPoint on analyze case patterns from D365 USMF for our 15-minute monthly review.', 'inputs': [{'description': 'D365 legal entity to pull from, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-analyze-case-patterns-2026-05-24.pptx.', 'name': 'output_filename'}, {'description': 'Review cadence and length the deck is sized for, e.g. 15-minute monthly review.', 'name': 'review_period'}, {'description': 'Prior period to chart the trend against.', 'name': 'comparison_period'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants an executive PPTX summarizing analyze-case-patterns status from D365 ERP data for a periodic review, without modifying any data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class PptExecAnalyzeCasePatterns(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecAnalyzeCasePatterns'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'comparison_period': {'description': 'Prior period to chart the trend against.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to pull from, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-analyze-case-patterns-2026-05-24.pptx.', 'type': 'string'}, 'review_period': {'description': 'Review cadence and length the deck is sized for, e.g. 15-minute monthly review.', 'type': 'string'}},
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
    print(PptExecAnalyzeCasePatterns().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
