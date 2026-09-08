---
name: "rar-cowork-cookbook-ppt-exec-develop-service-policies"
description: "Builds a read-only executive PowerPoint deck on develop service policies from Dynamics 365 F&SCM data for a given legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_develop_service_policies", "rar_sha256": "4f6387c06b4a3e1401c28f102831f2ae3476a961fea84d368410666dcabb712f", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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
