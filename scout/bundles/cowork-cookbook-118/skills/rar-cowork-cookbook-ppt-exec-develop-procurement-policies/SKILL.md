---
name: "rar-cowork-cookbook-ppt-exec-develop-procurement-policies"
description: "Builds a read-only executive PowerPoint deck on procurement policy development from Dynamics 365 ERP data for a legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_develop_procurement_policies", "rar_sha256": "f5c203b32eb8bb981ef8c6bc72e5fdbdb89cda9ba0a1a2d6a1eccb7b70e88515", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
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
