---
name: "rar-cowork-cookbook-ppt-exec-retire-services"
description: "Builds a read-only executive PowerPoint deck on retire services from Dynamics 365 ERP data for a given legal entity, with KPI, trend, issues, actions and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_retire_services", "rar_sha256": "0921065e9544205c0120a10902ecbc6626e09e6c4350dedf59a0414b16a0863a", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
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
