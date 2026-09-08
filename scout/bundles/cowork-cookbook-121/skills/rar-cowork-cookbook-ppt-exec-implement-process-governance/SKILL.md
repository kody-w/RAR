---
name: "rar-cowork-cookbook-ppt-exec-implement-process-governance"
description: "Builds a read-only executive PowerPoint deck on implement process governance from Dynamics 365 F&SCM data for a legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_implement_process_governance", "rar_sha256": "f9404ca5221d69b8f93a46dac739fc38193459f988517778ae9554233ec2e595", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_implement_process_governance`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_implement_process_governance_agent.py` and in the RCI capsule.

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

Implement process governance Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on implement process governance from Dynamics 365 F&SCM data for a legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-implement-process-governance
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
      "description": "Target .pptx filename, e.g. ppt-exec-implement-process-governance-2026-05-24.pptx.",
      "type": "string"
    },
    "reporting_period": {
      "description": "Current period and prior period used for the trend comparison chart.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_implement_process_governance_agent.py` and embedded as the fenced Python below (sha256 f9404ca5221d69b8…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_implement_process_governance_agent.py` first:

```bash
python3 ppt_exec_implement_process_governance_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_implement_process_governance_agent.py   # or on stdin
python3 ppt_exec_implement_process_governance_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Implement process governance Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on implement process governance from Dynamics 365 F&SCM data for a legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-implement-process-governance
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_implement_process_governance',
    "version": '3.0.3',
    "display_name": 'Implement process governance Executive PowerPoint Deck',
    "description": 'Builds a read-only executive PowerPoint deck on implement process governance from Dynamics 365 F&SCM data for a legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-implement-process-governance',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-implement-process-governance',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '801043706ac101de',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/implement-solutions/implement-process-governance'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/ppt-exec-implement-process-governance', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to pull data from, e.g. USMF.', 'output_filename': 'Target .pptx filename, e.g. ppt-exec-implement-process-governance-2026-05-24.pptx.', 'reporting_period': 'Current period and prior period used for the trend comparison chart.', 'review_length': 'Length/format of the review the deck must fit, e.g. 15-minute monthly review.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Cuts deck prep time from hours to minutes for implement process governance reviews while ensuring the numbers in the slides match D365 to the cent.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build an executive PowerPoint deck on implement process governance for a 15-minute monthly review. Produce 'ppt-exec-implement-process-governance-2026-05-24.pptx' with: (1) title slide, (2) headline KPIs, (3) trend chart vs prior period, (4) top issues / red flags, (5) recommended actions, (6) appendix - data sources and methodology. Include speaker-notes on each slide with talking points. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads implement process governance data and produces a 6-8 slide PowerPoint suitable for an executive review.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only executive PowerPoint deck on implement process governance from Dynamics 365 F&SCM data for a legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.', 'example_request': 'Build the exec PowerPoint on implement process governance from D365 USMF for our 15-minute monthly review.', 'inputs': [{'description': 'Dynamics 365 legal entity to pull data from, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Target .pptx filename, e.g. ppt-exec-implement-process-governance-2026-05-24.pptx.', 'name': 'output_filename'}, {'description': 'Length/format of the review the deck must fit, e.g. 15-minute monthly review.', 'name': 'review_length'}, {'description': 'Current period and prior period used for the trend comparison chart.', 'name': 'reporting_period'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user needs an executive-ready PPTX status deck on implement process governance for a short monthly review, sourced from D365 ERP without changing data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class PptExecImplementProcessGovernance(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecImplementProcessGovernance'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to pull data from, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Target .pptx filename, e.g. ppt-exec-implement-process-governance-2026-05-24.pptx.', 'type': 'string'}, 'reporting_period': {'description': 'Current period and prior period used for the trend comparison chart.', 'type': 'string'}, 'review_length': {'description': 'Length/format of the review the deck must fit, e.g. 15-minute monthly review.', 'type': 'string'}},
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
    print(PptExecImplementProcessGovernance().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
