---
name: "rar-cowork-cookbook-ppt-exec-maintain-open-service-requests"
description: "Builds a read-only executive PowerPoint deck on open service request status from Dynamics 365 F&SCM data, with title, KPI, trend, red-flag, action, and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_maintain_open_service_requests", "rar_sha256": "2f0c82ffa5c6a3bffa6ef46cb4b06f75d22d0d3ff7e3f1460176cd1dc82f3949", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_maintain_open_service_requests`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_maintain_open_service_requests_agent.py` and in the RCI capsule.

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

Maintain open service requests Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on open service request status from Dynamics 365 F&SCM data, with title, KPI, trend, red-flag, action, and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-maintain-open-service-requests
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
      "description": "Name of the .pptx file to produce, e.g. ppt-exec-maintain-open-service-requests-2026-05-24.pptx.",
      "type": "string"
    },
    "review_period": {
      "description": "Reporting period and prior period used for the trend comparison (e.g. monthly review as of a given date).",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_maintain_open_service_requests_agent.py` and embedded as the fenced Python below (sha256 2f0c82ffa5c6a3bf…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_maintain_open_service_requests_agent.py` first:

```bash
python3 ppt_exec_maintain_open_service_requests_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_maintain_open_service_requests_agent.py   # or on stdin
python3 ppt_exec_maintain_open_service_requests_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Maintain open service requests Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on open service request status from Dynamics 365 F&SCM data, with title, KPI, trend, red-flag, action, and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-maintain-open-service-requests
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_maintain_open_service_requests',
    "version": '3.0.3',
    "display_name": 'Maintain open service requests Executive PowerPoint Deck',
    "description": 'Builds a read-only executive PowerPoint deck on open service request status from Dynamics 365 F&SCM data, with title, KPI, trend, red-flag, action, and appendix slides plus speaker notes.',
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
        "upstream_slug": 'ppt-exec-maintain-open-service-requests',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-maintain-open-service-requests',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'a237f23e8be614ee',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/manage-service-work/maintain-open-service-requests'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/ppt-exec-maintain-open-service-requests', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to pull data from, e.g. USMF.', 'output_filename': 'Name of the .pptx file to produce, e.g. ppt-exec-maintain-open-service-requests-2026-05-24.pptx.', 'review_period': 'Reporting period and prior period used for the trend comparison (e.g. monthly review as of a given date).'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Cuts deck prep time from hours to minutes for maintain open service requests reviews while ensuring the numbers in the slides match D365 to the cent.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build an executive PowerPoint deck on maintain open service requests for a 15-minute monthly review. Produce 'ppt-exec-maintain-open-service-requests-2026-05-24.pptx' with: (1) title slide, (2) headline KPIs, (3) trend chart vs prior period, (4) top issues / red flags, (5) recommended actions, (6) appendix - data sources and methodology. Include speaker-notes on each slide with talking points. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads maintain open service requests data and produces a 6-8 slide PowerPoint suitable for an executive review.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only executive PowerPoint deck on open service request status from Dynamics 365 F&SCM data, with title, KPI, trend, red-flag, action, and appendix slides plus speaker notes.', 'example_request': "Build the exec PowerPoint on open service requests for USMF for this month's 15-minute review.", 'inputs': [{'description': 'D365 legal entity to pull data from, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-maintain-open-service-requests-2026-05-24.pptx.', 'name': 'output_filename'}, {'description': 'Reporting period and prior period used for the trend comparison (e.g. monthly review as of a given date).', 'name': 'review_period'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user needs a 15-minute monthly review deck on maintain open service requests from D365 ERP data, without modifying any records.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class PptExecMaintainOpenServiceRequests(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecMaintainOpenServiceRequests'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to pull data from, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-maintain-open-service-requests-2026-05-24.pptx.', 'type': 'string'}, 'review_period': {'description': 'Reporting period and prior period used for the trend comparison (e.g. monthly review as of a given date).', 'type': 'string'}},
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
    print(PptExecMaintainOpenServiceRequests().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
