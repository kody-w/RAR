---
name: "rar-cowork-cookbook-ppt-exec-develop-procurement-policies"
description: "Builds a read-only executive PowerPoint deck on procurement policy development from Dynamics 365 ERP data for a legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_develop_procurement_policies", "rar_sha256": "f5c203b32eb8bb981ef8c6bc72e5fdbdb89cda9ba0a1a2d6a1eccb7b70e88515", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_develop_procurement_policies`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_develop_procurement_policies_agent.py` and in the RCI capsule.

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

Develop procurement policies Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on procurement policy development from Dynamics 365 ERP data for a legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-develop-procurement-policies
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
      "description": "Target .pptx filename, e.g. ppt-exec-develop-procurement-policies-2026-05-24.pptx.",
      "type": "string"
    },
    "review_length": {
      "description": "Meeting length the deck is scoped to, e.g. 15-minute monthly review.",
      "type": "string"
    },
    "topic": {
      "description": "Subject of the deck, e.g. develop procurement policies.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_develop_procurement_policies_agent.py` and embedded as the fenced Python below (sha256 f5c203b32eb8bb98…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_develop_procurement_policies_agent.py` first:

```bash
python3 ppt_exec_develop_procurement_policies_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_develop_procurement_policies_agent.py   # or on stdin
python3 ppt_exec_develop_procurement_policies_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop procurement policies Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on procurement policy development from Dynamics 365 ERP data for a legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-develop-procurement-policies
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_develop_procurement_policies',
    "version": '3.0.3',
    "display_name": 'Develop procurement policies Executive PowerPoint Deck',
    "description": 'Builds a read-only executive PowerPoint deck on procurement policy development from Dynamics 365 ERP data for a legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-develop-procurement-policies',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-develop-procurement-policies',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'e4c801899fba6318',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/develop-procurement-and-sourcing-strategy/develop-procurement-policies'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/ppt-exec-develop-procurement-policies', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'comparison_period': 'Prior period used for the trend chart comparison.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report on, e.g. USMF.', 'output_filename': 'Target .pptx filename, e.g. ppt-exec-develop-procurement-policies-2026-05-24.pptx.', 'review_length': 'Meeting length the deck is scoped to, e.g. 15-minute monthly review.', 'topic': 'Subject of the deck, e.g. develop procurement policies.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Cuts deck prep time from hours to minutes for develop procurement policies reviews while ensuring the numbers in the slides match D365 to the cent.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build an executive PowerPoint deck on develop procurement policies for a 15-minute monthly review. Produce 'ppt-exec-develop-procurement-policies-2026-05-24.pptx' with: (1) title slide, (2) headline KPIs, (3) trend chart vs prior period, (4) top issues / red flags, (5) recommended actions, (6) appendix - data sources and methodology. Include speaker-notes on each slide with talking points. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads develop procurement policies data and produces a 6-8 slide PowerPoint suitable for an executive review.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only executive PowerPoint deck on procurement policy development from Dynamics 365 ERP data for a legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.', 'example_request': 'Build me an exec PowerPoint on develop procurement policies from D365 USMF for our 15-minute monthly review.', 'inputs': [{'description': 'D365 legal entity to report on, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Subject of the deck, e.g. develop procurement policies.', 'name': 'topic'}, {'description': 'Target .pptx filename, e.g. ppt-exec-develop-procurement-policies-2026-05-24.pptx.', 'name': 'output_filename'}, {'description': 'Meeting length the deck is scoped to, e.g. 15-minute monthly review.', 'name': 'review_length'}, {'description': 'Prior period used for the trend chart comparison.', 'name': 'comparison_period'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user needs an executive-ready procurement policy deck for a short monthly review, sourced from D365 F&SCM without changing any data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class PptExecDevelopProcurementPolicies(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecDevelopProcurementPolicies'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'comparison_period': {'description': 'Prior period used for the trend chart comparison.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report on, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Target .pptx filename, e.g. ppt-exec-develop-procurement-policies-2026-05-24.pptx.', 'type': 'string'}, 'review_length': {'description': 'Meeting length the deck is scoped to, e.g. 15-minute monthly review.', 'type': 'string'}, 'topic': {'description': 'Subject of the deck, e.g. develop procurement policies.', 'type': 'string'}},
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
    print(PptExecDevelopProcurementPolicies().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
