---
name: "rar-cowork-cookbook-ppt-exec-perform-market-research"
description: "Builds a read-only executive PowerPoint deck on market research status from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, issues, actions, and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_perform_market_research", "rar_sha256": "f4196a5daf5e170779127cacf46cdc85ab742867951b6334f846ad683b25725f", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
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
