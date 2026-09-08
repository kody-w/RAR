---
name: "rar-cowork-cookbook-ppt-exec-identify-service-trends"
description: "Builds a read-only executive PowerPoint deck on service trends from Dynamics 365 ERP data for a legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_identify_service_trends", "rar_sha256": "518942a5052a6ce92db4384d12e87740dcdf55ab160ad7ced17a51e089c91163", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_identify_service_trends`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_identify_service_trends_agent.py` and in the RCI capsule.

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

Identify service trends Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on service trends from Dynamics 365 ERP data for a legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-identify-service-trends
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
    "meeting_length": {
      "description": "Length of the review the deck must fit, e.g. 15-minute monthly review.",
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
      "description": "Name of the .pptx file to produce, e.g. ppt-exec-identify-service-trends-2026-05-24.pptx.",
      "type": "string"
    },
    "review_period": {
      "description": "Reporting period and prior period to compare against for the trend chart.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_identify_service_trends_agent.py` and embedded as the fenced Python below (sha256 518942a5052a6ce9…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_identify_service_trends_agent.py` first:

```bash
python3 ppt_exec_identify_service_trends_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_identify_service_trends_agent.py   # or on stdin
python3 ppt_exec_identify_service_trends_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Identify service trends Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on service trends from Dynamics 365 ERP data for a legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-identify-service-trends
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_identify_service_trends',
    "version": '3.0.3',
    "display_name": 'Identify service trends Executive PowerPoint Deck',
    "description": 'Builds a read-only executive PowerPoint deck on service trends from Dynamics 365 ERP data for a legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.',
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
        "upstream_slug": 'ppt-exec-identify-service-trends',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-identify-service-trends',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '0bce64ec10688df4',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/analyze-service-performance/identify-service-trends'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/ppt-exec-identify-service-trends', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to pull data from (e.g. USMF).', 'meeting_length': 'Length of the review the deck must fit, e.g. 15-minute monthly review.', 'output_filename': 'Name of the .pptx file to produce, e.g. ppt-exec-identify-service-trends-2026-05-24.pptx.', 'review_period': 'Reporting period and prior period to compare against for the trend chart.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Cuts deck prep time from hours to minutes for identify service trends reviews while ensuring the numbers in the slides match D365 to the cent.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build an executive PowerPoint deck on identify service trends for a 15-minute monthly review. Produce 'ppt-exec-identify-service-trends-2026-05-24.pptx' with: (1) title slide, (2) headline KPIs, (3) trend chart vs prior period, (4) top issues / red flags, (5) recommended actions, (6) appendix - data sources and methodology. Include speaker-notes on each slide with talking points. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads identify service trends data and produces a 6-8 slide PowerPoint suitable for an executive review.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only executive PowerPoint deck on service trends from Dynamics 365 ERP data for a legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.', 'example_request': 'Build an exec PowerPoint on service trends from D365 legal entity USMF for our 15-minute monthly review.', 'inputs': [{'description': 'Dynamics 365 legal entity to pull data from (e.g. USMF).', 'name': 'legal_entity'}, {'description': 'Reporting period and prior period to compare against for the trend chart.', 'name': 'review_period'}, {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-identify-service-trends-2026-05-24.pptx.', 'name': 'output_filename'}, {'description': 'Length of the review the deck must fit, e.g. 15-minute monthly review.', 'name': 'meeting_length'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants an executive-ready service-trends deck for a short monthly review, sourced from Dynamics 365 F&SCM without changing any data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class PptExecIdentifyServiceTrends(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecIdentifyServiceTrends'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to pull data from (e.g. USMF).', 'type': 'string'}, 'meeting_length': {'description': 'Length of the review the deck must fit, e.g. 15-minute monthly review.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-identify-service-trends-2026-05-24.pptx.', 'type': 'string'}, 'review_period': {'description': 'Reporting period and prior period to compare against for the trend chart.', 'type': 'string'}},
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
    print(PptExecIdentifyServiceTrends().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
