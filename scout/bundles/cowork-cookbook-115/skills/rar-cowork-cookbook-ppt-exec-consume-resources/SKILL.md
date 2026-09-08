---
name: "rar-cowork-cookbook-ppt-exec-consume-resources"
description: "Builds a read-only executive PowerPoint deck on consume resources status from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, issues, actions and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_consume_resources", "rar_sha256": "b6d34f4f97939ed9f154d02175b3b599d69a9c49427a0db3e2881d562937d81a", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_consume_resources`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_consume_resources_agent.py` and in the RCI capsule.

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

Consume resources Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on consume resources status from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, issues, actions and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-consume-resources
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
      "description": "Prior period to trend the current numbers against.",
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
      "description": "Target .pptx filename, e.g. ppt-exec-consume-resources-2026-05-24.pptx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_consume_resources_agent.py` and embedded as the fenced Python below (sha256 b6d34f4f97939ed9…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_consume_resources_agent.py` first:

```bash
python3 ppt_exec_consume_resources_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_consume_resources_agent.py   # or on stdin
python3 ppt_exec_consume_resources_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Consume resources Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on consume resources status from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, issues, actions and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-consume-resources
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_consume_resources',
    "version": '3.0.3',
    "display_name": 'Consume resources Executive PowerPoint Deck',
    "description": 'Builds a read-only executive PowerPoint deck on consume resources status from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, issues, actions and appendix slides plus speaker notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'plan_to_produce', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-consume-resources',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-consume-resources',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '91b01535f6fb09f7',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['plan-to-produce'], 'process_tags': ['plan-to-produce/run-production-operations/consume-resources'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'plan-to-produce/ppt-exec-consume-resources', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'comparison_period': 'Prior period to trend the current numbers against.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to pull data from, e.g. USMF.', 'output_filename': 'Target .pptx filename, e.g. ppt-exec-consume-resources-2026-05-24.pptx.', 'review_length': 'Length/format of the meeting the deck must fit, e.g. 15-minute monthly review.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Cuts deck prep time from hours to minutes for consume resources reviews while ensuring the numbers in the slides match D365 to the cent.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build an executive PowerPoint deck on consume resources for a 15-minute monthly review. Produce 'ppt-exec-consume-resources-2026-05-24.pptx' with: (1) title slide, (2) headline KPIs, (3) trend chart vs prior period, (4) top issues / red flags, (5) recommended actions, (6) appendix - data sources and methodology. Include speaker-notes on each slide with talking points. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads consume resources data and produces a 6-8 slide PowerPoint suitable for an executive review.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only executive PowerPoint deck on consume resources status from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, issues, actions and appendix slides plus speaker notes.', 'example_request': 'Build an exec PowerPoint on consume resources for USMF for our 15-minute monthly review.', 'inputs': [{'description': 'D365 legal entity to pull data from, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Target .pptx filename, e.g. ppt-exec-consume-resources-2026-05-24.pptx.', 'name': 'output_filename'}, {'description': 'Length/format of the meeting the deck must fit, e.g. 15-minute monthly review.', 'name': 'review_length'}, {'description': 'Prior period to trend the current numbers against.', 'name': 'comparison_period'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user needs an executive-ready PPTX summarizing consume resources status from D365 ERP for a short monthly review, without modifying data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class PptExecConsumeResources(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecConsumeResources'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'comparison_period': {'description': 'Prior period to trend the current numbers against.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to pull data from, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Target .pptx filename, e.g. ppt-exec-consume-resources-2026-05-24.pptx.', 'type': 'string'}, 'review_length': {'description': 'Length/format of the meeting the deck must fit, e.g. 15-minute monthly review.', 'type': 'string'}},
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
    print(PptExecConsumeResources().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
