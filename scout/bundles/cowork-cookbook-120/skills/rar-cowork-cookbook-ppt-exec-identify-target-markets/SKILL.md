---
name: "rar-cowork-cookbook-ppt-exec-identify-target-markets"
description: "Builds a read-only executive PowerPoint deck on target-market identification from Dynamics 365 F&SCM data for a legal entity, with title, KPI, trend, red-flag, actions, and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_identify_target_markets", "rar_sha256": "1d3db7ad7ca83952e6f0e4b38de42f226e662c0c2256623090e33443fe21f190", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_identify_target_markets`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_identify_target_markets_agent.py` and in the RCI capsule.

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

Identify target markets Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on target-market identification from Dynamics 365 F&SCM data for a legal entity, with title, KPI, trend, red-flag, actions, and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-identify-target-markets
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
      "description": "Name of the .pptx file to produce, e.g. ppt-exec-identify-target-markets-2026-05-24.pptx.",
      "type": "string"
    },
    "review_length": {
      "description": "Length/format of the meeting the deck must fit, e.g. 15-minute monthly review.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_identify_target_markets_agent.py` and embedded as the fenced Python below (sha256 1d3db7ad7ca83952…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_identify_target_markets_agent.py` first:

```bash
python3 ppt_exec_identify_target_markets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_identify_target_markets_agent.py   # or on stdin
python3 ppt_exec_identify_target_markets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Identify target markets Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on target-market identification from Dynamics 365 F&SCM data for a legal entity, with title, KPI, trend, red-flag, actions, and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-identify-target-markets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_identify_target_markets',
    "version": '3.0.3',
    "display_name": 'Identify target markets Executive PowerPoint Deck',
    "description": 'Builds a read-only executive PowerPoint deck on target-market identification from Dynamics 365 F&SCM data for a legal entity, with title, KPI, trend, red-flag, actions, and appendix slides plus speaker notes.',
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
        "upstream_slug": 'ppt-exec-identify-target-markets',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-identify-target-markets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '3eb1be1d98915577',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/research-and-develop-offerings/identify-target-markets'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/ppt-exec-identify-target-markets', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'comparison_period': 'Prior period to chart the trend against.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to pull data from, e.g. USMF.', 'output_filename': 'Name of the .pptx file to produce, e.g. ppt-exec-identify-target-markets-2026-05-24.pptx.', 'review_length': 'Length/format of the meeting the deck must fit, e.g. 15-minute monthly review.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Cuts deck prep time from hours to minutes for identify target markets reviews while ensuring the numbers in the slides match D365 to the cent.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build an executive PowerPoint deck on identify target markets for a 15-minute monthly review. Produce 'ppt-exec-identify-target-markets-2026-05-24.pptx' with: (1) title slide, (2) headline KPIs, (3) trend chart vs prior period, (4) top issues / red flags, (5) recommended actions, (6) appendix - data sources and methodology. Include speaker-notes on each slide with talking points. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads identify target markets data and produces a 6-8 slide PowerPoint suitable for an executive review.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only executive PowerPoint deck on target-market identification from Dynamics 365 F&SCM data for a legal entity, with title, KPI, trend, red-flag, actions, and appendix slides plus speaker notes.', 'example_request': 'Build an executive PowerPoint on identify target markets from D365 USMF for our 15-minute monthly review.', 'inputs': [{'description': 'Dynamics 365 legal entity to pull data from, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-identify-target-markets-2026-05-24.pptx.', 'name': 'output_filename'}, {'description': 'Length/format of the meeting the deck must fit, e.g. 15-minute monthly review.', 'name': 'review_length'}, {'description': 'Prior period to chart the trend against.', 'name': 'comparison_period'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user needs an executive-ready .pptx on identify-target-markets status for a short monthly review, sourced from D365 ERP without changing data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class PptExecIdentifyTargetMarkets(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecIdentifyTargetMarkets'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'comparison_period': {'description': 'Prior period to chart the trend against.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to pull data from, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-identify-target-markets-2026-05-24.pptx.', 'type': 'string'}, 'review_length': {'description': 'Length/format of the meeting the deck must fit, e.g. 15-minute monthly review.', 'type': 'string'}},
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
    print(PptExecIdentifyTargetMarkets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
