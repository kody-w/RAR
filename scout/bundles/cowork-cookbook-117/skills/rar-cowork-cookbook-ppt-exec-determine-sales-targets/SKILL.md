---
name: "rar-cowork-cookbook-ppt-exec-determine-sales-targets"
description: "Builds a read-only executive PowerPoint deck on sales target status from Dynamics 365 ERP data for a given legal entity, with title, KPI, trend, red-flag, actions, and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_determine_sales_targets", "rar_sha256": "56818ae9918300246aa9971446b28bab092316d88e097a0a0f94b7e18e5d6ac3", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
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
