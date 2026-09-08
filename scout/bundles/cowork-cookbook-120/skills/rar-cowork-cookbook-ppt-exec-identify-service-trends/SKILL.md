---
name: "rar-cowork-cookbook-ppt-exec-identify-service-trends"
description: "Builds a read-only executive PowerPoint deck on service trends from Dynamics 365 ERP data for a legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_identify_service_trends", "rar_sha256": "518942a5052a6ce92db4384d12e87740dcdf55ab160ad7ced17a51e089c91163", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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
