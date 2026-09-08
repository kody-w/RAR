---
name: "rar-cowork-cookbook-ppt-exec-retire-services"
description: "Builds a read-only executive PowerPoint deck on retire services from Dynamics 365 ERP data for a given legal entity, with KPI, trend, issues, actions and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_retire_services", "rar_sha256": "0921065e9544205c0120a10902ecbc6626e09e6c4350dedf59a0414b16a0863a", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_retire_services`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_retire_services_agent.py` and in the RCI capsule.

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

Retire services Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on retire services from Dynamics 365 ERP data for a given legal entity, with KPI, trend, issues, actions and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-retire-services
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
      "description": "Name of the .pptx file to produce, e.g. ppt-exec-retire-services-2026-05-24.pptx.",
      "type": "string"
    },
    "review_period": {
      "description": "Reporting period and prior period used for the trend comparison, e.g. monthly.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_retire_services_agent.py` and embedded as the fenced Python below (sha256 0921065e9544205c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_retire_services_agent.py` first:

```bash
python3 ppt_exec_retire_services_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_retire_services_agent.py   # or on stdin
python3 ppt_exec_retire_services_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Retire services Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on retire services from Dynamics 365 ERP data for a given legal entity, with KPI, trend, issues, actions and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-retire-services
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_retire_services',
    "version": '3.0.3',
    "display_name": 'Retire services Executive PowerPoint Deck',
    "description": 'Builds a read-only executive PowerPoint deck on retire services from Dynamics 365 ERP data for a given legal entity, with KPI, trend, issues, actions and appendix slides plus speaker notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'concept_to_market', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-retire-services',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-retire-services',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '8273db5ab056630b',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/manage-service-offerings/retire-services'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/ppt-exec-retire-services', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report on, e.g. USMF.', 'output_filename': 'Name of the .pptx file to produce, e.g. ppt-exec-retire-services-2026-05-24.pptx.', 'review_period': 'Reporting period and prior period used for the trend comparison, e.g. monthly.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Cuts deck prep time from hours to minutes for retire services reviews while ensuring the numbers in the slides match D365 to the cent.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build an executive PowerPoint deck on retire services for a 15-minute monthly review. Produce 'ppt-exec-retire-services-2026-05-24.pptx' with: (1) title slide, (2) headline KPIs, (3) trend chart vs prior period, (4) top issues / red flags, (5) recommended actions, (6) appendix - data sources and methodology. Include speaker-notes on each slide with talking points. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads retire services data and produces a 6-8 slide PowerPoint suitable for an executive review.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only executive PowerPoint deck on retire services from Dynamics 365 ERP data for a given legal entity, with KPI, trend, issues, actions and appendix slides plus speaker notes.', 'example_request': "Build the executive retire services deck for USMF for this month's 15-minute review.", 'inputs': [{'description': 'D365 legal entity to report on, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-retire-services-2026-05-24.pptx.', 'name': 'output_filename'}, {'description': 'Reporting period and prior period used for the trend comparison, e.g. monthly.', 'name': 'review_period'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user needs a 15-minute monthly executive review deck on retire services status pulled from D365 F&SCM without changing any data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class PptExecRetireServices(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecRetireServices'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report on, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-retire-services-2026-05-24.pptx.', 'type': 'string'}, 'review_period': {'description': 'Reporting period and prior period used for the trend comparison, e.g. monthly.', 'type': 'string'}},
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
    print(PptExecRetireServices().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
