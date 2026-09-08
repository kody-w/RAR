---
name: "rar-cowork-cookbook-ppt-exec-consume-resources"
description: "Builds a read-only executive PowerPoint deck on consume resources status from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, issues, actions and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_consume_resources", "rar_sha256": "b6d34f4f97939ed9f154d02175b3b599d69a9c49427a0db3e2881d562937d81a", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
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
