---
name: "rar-cowork-cookbook-ppt-exec-perform-market-research"
description: "Builds a read-only executive PowerPoint deck on market research status from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, issues, actions, and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_perform_market_research", "rar_sha256": "f4196a5daf5e170779127cacf46cdc85ab742867951b6334f846ad683b25725f", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_perform_market_research`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_perform_market_research_agent.py` and in the RCI capsule.

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

Perform market research Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on market research status from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, issues, actions, and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-perform-market-research
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
      "description": "D365 legal entity to pull data from, e.g. USMF.",
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
      "description": "Name of the .pptx file to produce, e.g. ppt-exec-perform-market-research-2026-05-24.pptx.",
      "type": "string"
    },
    "review_length": {
      "description": "Length/format of the review the deck must fit, e.g. 15-minute monthly review.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_perform_market_research_agent.py` and embedded as the fenced Python below (sha256 f4196a5daf5e1707…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_perform_market_research_agent.py` first:

```bash
python3 ppt_exec_perform_market_research_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_perform_market_research_agent.py   # or on stdin
python3 ppt_exec_perform_market_research_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Perform market research Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on market research status from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, issues, actions, and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-perform-market-research
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_perform_market_research',
    "version": '3.0.3',
    "display_name": 'Perform market research Executive PowerPoint Deck',
    "description": 'Builds a read-only executive PowerPoint deck on market research status from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, issues, actions, and appendix slides plus speaker notes.',
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
        "upstream_slug": 'ppt-exec-perform-market-research',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-perform-market-research',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '6ddf9320cd2b4584',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/develop-marketing-strategy/perform-market-research'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/ppt-exec-perform-market-research', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'comparison_period': 'Prior period to chart the trend against.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to pull data from, e.g. USMF.', 'output_filename': 'Name of the .pptx file to produce, e.g. ppt-exec-perform-market-research-2026-05-24.pptx.', 'review_length': 'Length/format of the review the deck must fit, e.g. 15-minute monthly review.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Cuts deck prep time from hours to minutes for perform market research reviews while ensuring the numbers in the slides match D365 to the cent.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build an executive PowerPoint deck on perform market research for a 15-minute monthly review. Produce 'ppt-exec-perform-market-research-2026-05-24.pptx' with: (1) title slide, (2) headline KPIs, (3) trend chart vs prior period, (4) top issues / red flags, (5) recommended actions, (6) appendix - data sources and methodology. Include speaker-notes on each slide with talking points. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads perform market research data and produces a 6-8 slide PowerPoint suitable for an executive review.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only executive PowerPoint deck on market research status from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, issues, actions, and appendix slides plus speaker notes.', 'example_request': 'Build an exec PowerPoint on market research for USMF, 15-minute monthly review, with trend vs prior period.', 'inputs': [{'description': 'D365 legal entity to pull data from, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-perform-market-research-2026-05-24.pptx.', 'name': 'output_filename'}, {'description': 'Length/format of the review the deck must fit, e.g. 15-minute monthly review.', 'name': 'review_length'}, {'description': 'Prior period to chart the trend against.', 'name': 'comparison_period'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user needs an executive-ready market research review deck for a monthly meeting, sourced from D365 ERP data without modifying it.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class PptExecPerformMarketResearch(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecPerformMarketResearch'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'comparison_period': {'description': 'Prior period to chart the trend against.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to pull data from, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-perform-market-research-2026-05-24.pptx.', 'type': 'string'}, 'review_length': {'description': 'Length/format of the review the deck must fit, e.g. 15-minute monthly review.', 'type': 'string'}},
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
    print(PptExecPerformMarketResearch().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
