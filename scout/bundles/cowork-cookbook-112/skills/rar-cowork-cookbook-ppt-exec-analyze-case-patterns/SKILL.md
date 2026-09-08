---
name: "rar-cowork-cookbook-ppt-exec-analyze-case-patterns"
description: "Builds a read-only executive PowerPoint deck on case-pattern analysis from Dynamics 365 F&SCM data for a named legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_analyze_case_patterns", "rar_sha256": "1461e173c36d55eeb3c7c4f4b0aebc7e984492b96ec2f29c8cac31e3126eab43", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
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
