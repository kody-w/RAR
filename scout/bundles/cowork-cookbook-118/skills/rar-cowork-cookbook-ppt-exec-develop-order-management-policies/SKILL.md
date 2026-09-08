---
name: "rar-cowork-cookbook-ppt-exec-develop-order-management-policies"
description: "Builds a read-only executive PowerPoint deck on order management policy status from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, issues, actions and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_develop_order_management_policies", "rar_sha256": "e76c03bcc52fd1cdeb8ba00764963227129785d78edc407ab041c2ede46d7f88", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_develop_order_management_policies`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_develop_order_management_policies_agent.py` and in the RCI capsule.

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

Develop order management policies Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on order management policy status from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, issues, actions and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-develop-order-management-policies
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
      "description": "Dynamics 365 legal entity to pull data from (e.g. USMF).",
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
      "description": "Name of the .pptx file to produce, e.g. ppt-exec-develop-order-management-policies-2026-05-24.pptx.",
      "type": "string"
    },
    "review_length": {
      "description": "Length of the meeting the deck must fit, e.g. 15-minute monthly review.",
      "type": "string"
    },
    "review_period": {
      "description": "Reporting period and comparison period for the trend chart (e.g. current month vs prior).",
      "type": "string"
    },
    "topic": {
      "description": "Subject of the deck, e.g. 'develop order management policies'.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_develop_order_management_policies_agent.py` and embedded as the fenced Python below (sha256 e76c03bcc52fd1cd…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_develop_order_management_policies_agent.py` first:

```bash
python3 ppt_exec_develop_order_management_policies_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_develop_order_management_policies_agent.py   # or on stdin
python3 ppt_exec_develop_order_management_policies_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop order management policies Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on order management policy status from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, issues, actions and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-develop-order-management-policies
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_develop_order_management_policies',
    "version": '3.0.3',
    "display_name": 'Develop order management policies Executive PowerPoint Deck',
    "description": 'Builds a read-only executive PowerPoint deck on order management policy status from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, issues, actions and appendix slides plus speaker notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'order_to_cash', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-develop-order-management-policies',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-develop-order-management-policies',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'fce419cd9cf6cbb1',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/develop-sales-policies/develop-order-management-policies'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/ppt-exec-develop-order-management-policies', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to pull data from (e.g. USMF).', 'output_filename': 'Name of the .pptx file to produce, e.g. ppt-exec-develop-order-management-policies-2026-05-24.pptx.', 'review_length': 'Length of the meeting the deck must fit, e.g. 15-minute monthly review.', 'review_period': 'Reporting period and comparison period for the trend chart (e.g. current month vs prior).', 'topic': "Subject of the deck, e.g. 'develop order management policies'."}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Cuts deck prep time from hours to minutes for develop order management policies reviews while ensuring the numbers in the slides match D365 to the cent.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build an executive PowerPoint deck on develop order management policies for a 15-minute monthly review. Produce 'ppt-exec-develop-order-management-policies-2026-05-24.pptx' with: (1) title slide, (2) headline KPIs, (3) trend chart vs prior period, (4) top issues / red flags, (5) recommended actions, (6) appendix - data sources and methodology. Include speaker-notes on each slide with talking points. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads develop order management policies data and produces a 6-8 slide PowerPoint suitable for an executive review.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only executive PowerPoint deck on order management policy status from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, issues, actions and appendix slides plus speaker notes.', 'example_request': 'Build an exec PowerPoint on order management policies from D365 USMF for our 15-minute monthly review.', 'inputs': [{'description': 'Dynamics 365 legal entity to pull data from (e.g. USMF).', 'name': 'legal_entity'}, {'description': "Subject of the deck, e.g. 'develop order management policies'.", 'name': 'topic'}, {'description': 'Reporting period and comparison period for the trend chart (e.g. current month vs prior).', 'name': 'review_period'}, {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-develop-order-management-policies-2026-05-24.pptx.', 'name': 'output_filename'}, {'description': 'Length of the meeting the deck must fit, e.g. 15-minute monthly review.', 'name': 'review_length'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user needs an executive-ready PPTX summarizing develop order management policies for a short monthly review, sourced from D365 ERP data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class PptExecDevelopOrderManagementPolicies(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecDevelopOrderManagementPolicies'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to pull data from (e.g. USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-develop-order-management-policies-2026-05-24.pptx.', 'type': 'string'}, 'review_length': {'description': 'Length of the meeting the deck must fit, e.g. 15-minute monthly review.', 'type': 'string'}, 'review_period': {'description': 'Reporting period and comparison period for the trend chart (e.g. current month vs prior).', 'type': 'string'}, 'topic': {'description': "Subject of the deck, e.g. 'develop order management policies'.", 'type': 'string'}},
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
    print(PptExecDevelopOrderManagementPolicies().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
