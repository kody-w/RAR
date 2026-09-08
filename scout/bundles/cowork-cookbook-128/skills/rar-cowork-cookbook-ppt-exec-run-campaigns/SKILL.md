---
name: "rar-cowork-cookbook-ppt-exec-run-campaigns"
description: "Builds a read-only executive PowerPoint deck on run campaigns from Dynamics 365 F&SCM data for a given legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_run_campaigns", "rar_sha256": "f166341952736a30f530b79f11f948583ecfd06be840a9b8560d937733f8e3b1", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_run_campaigns`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_run_campaigns_agent.py` and in the RCI capsule.

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

Run campaigns Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on run campaigns from Dynamics 365 F&SCM data for a given legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-run-campaigns
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
      "description": "Target .pptx filename, e.g. ppt-exec-run-campaigns-2026-05-24.pptx.",
      "type": "string"
    },
    "review_length": {
      "description": "Meeting length the deck must fit, e.g. 15-minute monthly review.",
      "type": "string"
    },
    "review_period": {
      "description": "Reporting period and prior period for trend comparison, e.g. month of May 2026.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_run_campaigns_agent.py` and embedded as the fenced Python below (sha256 f166341952736a30…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_run_campaigns_agent.py` first:

```bash
python3 ppt_exec_run_campaigns_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_run_campaigns_agent.py   # or on stdin
python3 ppt_exec_run_campaigns_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Run campaigns Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on run campaigns from Dynamics 365 F&SCM data for a given legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-run-campaigns
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_run_campaigns',
    "version": '3.0.3',
    "display_name": 'Run campaigns Executive PowerPoint Deck',
    "description": 'Builds a read-only executive PowerPoint deck on run campaigns from Dynamics 365 F&SCM data for a given legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.',
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
        "upstream_slug": 'ppt-exec-run-campaigns',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-run-campaigns',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '5419d0885b000c55',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/manage-marketing-campaigns/run-campaigns'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/ppt-exec-run-campaigns', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report on, e.g. USMF.', 'output_filename': 'Target .pptx filename, e.g. ppt-exec-run-campaigns-2026-05-24.pptx.', 'review_length': 'Meeting length the deck must fit, e.g. 15-minute monthly review.', 'review_period': 'Reporting period and prior period for trend comparison, e.g. month of May 2026.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Cuts deck prep time from hours to minutes for run campaigns reviews while ensuring the numbers in the slides match D365 to the cent.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build an executive PowerPoint deck on run campaigns for a 15-minute monthly review. Produce 'ppt-exec-run-campaigns-2026-05-24.pptx' with: (1) title slide, (2) headline KPIs, (3) trend chart vs prior period, (4) top issues / red flags, (5) recommended actions, (6) appendix - data sources and methodology. Include speaker-notes on each slide with talking points. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads run campaigns data and produces a 6-8 slide PowerPoint suitable for an executive review.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only executive PowerPoint deck on run campaigns from Dynamics 365 F&SCM data for a given legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.', 'example_request': 'Build an executive PowerPoint deck on run campaigns for USMF for our 15-minute monthly review.', 'inputs': [{'description': 'D365 legal entity to report on, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Reporting period and prior period for trend comparison, e.g. month of May 2026.', 'name': 'review_period'}, {'description': 'Target .pptx filename, e.g. ppt-exec-run-campaigns-2026-05-24.pptx.', 'name': 'output_filename'}, {'description': 'Meeting length the deck must fit, e.g. 15-minute monthly review.', 'name': 'review_length'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user needs an executive-ready run campaigns deck for a short monthly review, sourced from D365 ERP without modifying any data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class PptExecRunCampaigns(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecRunCampaigns'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report on, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Target .pptx filename, e.g. ppt-exec-run-campaigns-2026-05-24.pptx.', 'type': 'string'}, 'review_length': {'description': 'Meeting length the deck must fit, e.g. 15-minute monthly review.', 'type': 'string'}, 'review_period': {'description': 'Reporting period and prior period for trend comparison, e.g. month of May 2026.', 'type': 'string'}},
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
    print(PptExecRunCampaigns().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
