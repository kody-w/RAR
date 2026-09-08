---
name: "rar-cowork-cookbook-ppt-exec-determine-sales-targets"
description: "Builds a read-only executive PowerPoint deck on sales target status from Dynamics 365 ERP data for a given legal entity, with title, KPI, trend, red-flag, actions, and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_determine_sales_targets", "rar_sha256": "56818ae9918300246aa9971446b28bab092316d88e097a0a0f94b7e18e5d6ac3", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_determine_sales_targets`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_determine_sales_targets_agent.py` and in the RCI capsule.

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

Determine sales targets Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on sales target status from Dynamics 365 ERP data for a given legal entity, with title, KPI, trend, red-flag, actions, and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-determine-sales-targets
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
      "description": "Prior period used for the trend chart comparison.",
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
      "description": "Target .pptx filename, e.g. ppt-exec-determine-sales-targets-2026-05-24.pptx.",
      "type": "string"
    },
    "review_length": {
      "description": "Meeting length the deck is scoped for, e.g. 15-minute monthly review.",
      "type": "string"
    },
    "topic": {
      "description": "Subject of the deck, e.g. determine sales targets.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_determine_sales_targets_agent.py` and embedded as the fenced Python below (sha256 56818ae991830024…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_determine_sales_targets_agent.py` first:

```bash
python3 ppt_exec_determine_sales_targets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_determine_sales_targets_agent.py   # or on stdin
python3 ppt_exec_determine_sales_targets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Determine sales targets Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on sales target status from Dynamics 365 ERP data for a given legal entity, with title, KPI, trend, red-flag, actions, and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-determine-sales-targets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_determine_sales_targets',
    "version": '3.0.3',
    "display_name": 'Determine sales targets Executive PowerPoint Deck',
    "description": 'Builds a read-only executive PowerPoint deck on sales target status from Dynamics 365 ERP data for a given legal entity, with title, KPI, trend, red-flag, actions, and appendix slides plus speaker notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'prospect_to_quote', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-determine-sales-targets',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-determine-sales-targets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '890ac07447980630',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/define-sales-strategy-and-policies/determine-sales-targets'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/ppt-exec-determine-sales-targets', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'comparison_period': 'Prior period used for the trend chart comparison.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to pull data from, e.g. USMF.', 'output_filename': 'Target .pptx filename, e.g. ppt-exec-determine-sales-targets-2026-05-24.pptx.', 'review_length': 'Meeting length the deck is scoped for, e.g. 15-minute monthly review.', 'topic': 'Subject of the deck, e.g. determine sales targets.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Cuts deck prep time from hours to minutes for determine sales targets reviews while ensuring the numbers in the slides match D365 to the cent.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build an executive PowerPoint deck on determine sales targets for a 15-minute monthly review. Produce 'ppt-exec-determine-sales-targets-2026-05-24.pptx' with: (1) title slide, (2) headline KPIs, (3) trend chart vs prior period, (4) top issues / red flags, (5) recommended actions, (6) appendix - data sources and methodology. Include speaker-notes on each slide with talking points. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads determine sales targets data and produces a 6-8 slide PowerPoint suitable for an executive review.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only executive PowerPoint deck on sales target status from Dynamics 365 ERP data for a given legal entity, with title, KPI, trend, red-flag, actions, and appendix slides plus speaker notes.', 'example_request': 'Build an executive PowerPoint on sales targets for USMF for our 15-minute monthly review.', 'inputs': [{'description': 'D365 legal entity to pull data from, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Subject of the deck, e.g. determine sales targets.', 'name': 'topic'}, {'description': 'Target .pptx filename, e.g. ppt-exec-determine-sales-targets-2026-05-24.pptx.', 'name': 'output_filename'}, {'description': 'Meeting length the deck is scoped for, e.g. 15-minute monthly review.', 'name': 'review_length'}, {'description': 'Prior period used for the trend chart comparison.', 'name': 'comparison_period'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants an executive-ready sales-targets deck from D365 F&SCM for a short monthly review, without modifying any ERP data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class PptExecDetermineSalesTargets(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecDetermineSalesTargets'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'comparison_period': {'description': 'Prior period used for the trend chart comparison.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to pull data from, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Target .pptx filename, e.g. ppt-exec-determine-sales-targets-2026-05-24.pptx.', 'type': 'string'}, 'review_length': {'description': 'Meeting length the deck is scoped for, e.g. 15-minute monthly review.', 'type': 'string'}, 'topic': {'description': 'Subject of the deck, e.g. determine sales targets.', 'type': 'string'}},
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
    print(PptExecDetermineSalesTargets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
