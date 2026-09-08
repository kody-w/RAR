---
name: "rar-cowork-cookbook-ppt-exec-develop-service-policies"
description: "Builds a read-only executive PowerPoint deck on develop service policies from Dynamics 365 F&SCM data for a given legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_develop_service_policies", "rar_sha256": "4f6387c06b4a3e1401c28f102831f2ae3476a961fea84d368410666dcabb712f", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_develop_service_policies`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_develop_service_policies_agent.py` and in the RCI capsule.

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

Develop service policies Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on develop service policies from Dynamics 365 F&SCM data for a given legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-develop-service-policies
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
      "description": "Prior period to trend the KPIs against.",
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
      "description": "Name of the .pptx file to produce, e.g. ppt-exec-develop-service-policies-2026-05-24.pptx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_develop_service_policies_agent.py` and embedded as the fenced Python below (sha256 4f6387c06b4a3e14…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_develop_service_policies_agent.py` first:

```bash
python3 ppt_exec_develop_service_policies_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_develop_service_policies_agent.py   # or on stdin
python3 ppt_exec_develop_service_policies_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop service policies Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on develop service policies from Dynamics 365 F&SCM data for a given legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-develop-service-policies
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_develop_service_policies',
    "version": '3.0.3',
    "display_name": 'Develop service policies Executive PowerPoint Deck',
    "description": 'Builds a read-only executive PowerPoint deck on develop service policies from Dynamics 365 F&SCM data for a given legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'service_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-develop-service-policies',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-develop-service-policies',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '59b7d11a01fe881b',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/develop-service-strategy/develop-service-policies'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/ppt-exec-develop-service-policies', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'comparison_period': 'Prior period to trend the KPIs against.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report on, e.g. USMF.', 'output_filename': 'Name of the .pptx file to produce, e.g. ppt-exec-develop-service-policies-2026-05-24.pptx.', 'review_length': 'Length/format of the review the deck must fit, e.g. 15-minute monthly review.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Cuts deck prep time from hours to minutes for develop service policies reviews while ensuring the numbers in the slides match D365 to the cent.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build an executive PowerPoint deck on develop service policies for a 15-minute monthly review. Produce 'ppt-exec-develop-service-policies-2026-05-24.pptx' with: (1) title slide, (2) headline KPIs, (3) trend chart vs prior period, (4) top issues / red flags, (5) recommended actions, (6) appendix - data sources and methodology. Include speaker-notes on each slide with talking points. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads develop service policies data and produces a 6-8 slide PowerPoint suitable for an executive review.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only executive PowerPoint deck on develop service policies from Dynamics 365 F&SCM data for a given legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.', 'example_request': 'Build the executive PowerPoint deck on develop service policies for USMF for our 15-minute monthly review.', 'inputs': [{'description': 'D365 legal entity to report on, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-develop-service-policies-2026-05-24.pptx.', 'name': 'output_filename'}, {'description': 'Length/format of the review the deck must fit, e.g. 15-minute monthly review.', 'name': 'review_length'}, {'description': 'Prior period to trend the KPIs against.', 'name': 'comparison_period'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user needs an executive-ready PPTX on develop service policies status for a short monthly review, sourced from D365 ERP without modifying data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class PptExecDevelopServicePolicies(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecDevelopServicePolicies'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'comparison_period': {'description': 'Prior period to trend the KPIs against.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report on, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-develop-service-policies-2026-05-24.pptx.', 'type': 'string'}, 'review_length': {'description': 'Length/format of the review the deck must fit, e.g. 15-minute monthly review.', 'type': 'string'}},
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
    print(PptExecDevelopServicePolicies().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
