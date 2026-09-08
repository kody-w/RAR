---
name: "rar-cowork-cookbook-ppt-exec-maintain-open-service-requests"
description: "Builds a read-only executive PowerPoint deck on open service request status from Dynamics 365 F&SCM data, with title, KPI, trend, red-flag, action, and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_maintain_open_service_requests", "rar_sha256": "2f0c82ffa5c6a3bffa6ef46cb4b06f75d22d0d3ff7e3f1460176cd1dc82f3949", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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
