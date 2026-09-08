---
name: "rar-cowork-cookbook-ppt-exec-implement-process-governance"
description: "Builds a read-only executive PowerPoint deck on implement process governance from Dynamics 365 F&SCM data for a legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_implement_process_governance", "rar_sha256": "f9404ca5221d69b8f93a46dac739fc38193459f988517778ae9554233ec2e595", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
