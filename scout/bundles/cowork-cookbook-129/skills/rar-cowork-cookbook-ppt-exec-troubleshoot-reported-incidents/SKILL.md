---
name: "rar-cowork-cookbook-ppt-exec-troubleshoot-reported-incidents"
description: "Builds a read-only executive PowerPoint deck on reported-incident troubleshooting status from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, issues, actions and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_troubleshoot_reported_incidents", "rar_sha256": "b8b8536b818e2487e4ba31459cf0bacacc01e350ba2e688102c404e05608b881", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_troubleshoot_reported_incidents`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_troubleshoot_reported_incidents_agent.py` and in the RCI capsule.

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

Troubleshoot reported incidents Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on reported-incident troubleshooting status from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, issues, actions and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-troubleshoot-reported-incidents
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
      "description": "Dynamics 365 legal entity to pull data from, e.g. USMF.",
      "type": "string"
    },
    "meeting_length": {
      "description": "Length of the review the deck must fit, e.g. 15 minutes.",
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
      "description": "Name of the .pptx file to produce, e.g. ppt-exec-troubleshoot-reported-incidents-2026-05-24.pptx.",
      "type": "string"
    },
    "review_period": {
      "description": "Reporting period and comparison prior period for the trend chart (e.g. monthly review).",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_troubleshoot_reported_incidents_agent.py` and embedded as the fenced Python below (sha256 b8b8536b818e2487…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_troubleshoot_reported_incidents_agent.py` first:

```bash
python3 ppt_exec_troubleshoot_reported_incidents_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_troubleshoot_reported_incidents_agent.py   # or on stdin
python3 ppt_exec_troubleshoot_reported_incidents_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Troubleshoot reported incidents Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on reported-incident troubleshooting status from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, issues, actions and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-troubleshoot-reported-incidents
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_troubleshoot_reported_incidents',
    "version": '3.0.3',
    "display_name": 'Troubleshoot reported incidents Executive PowerPoint Deck',
    "description": 'Builds a read-only executive PowerPoint deck on reported-incident troubleshooting status from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, issues, actions and appendix slides plus speaker notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-troubleshoot-reported-incidents',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-troubleshoot-reported-incidents',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '9de6251d212a8618',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/support-systems/troubleshoot-reported-incidents'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/ppt-exec-troubleshoot-reported-incidents', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to pull data from, e.g. USMF.', 'meeting_length': 'Length of the review the deck must fit, e.g. 15 minutes.', 'output_filename': 'Name of the .pptx file to produce, e.g. ppt-exec-troubleshoot-reported-incidents-2026-05-24.pptx.', 'review_period': 'Reporting period and comparison prior period for the trend chart (e.g. monthly review).'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Cuts deck prep time from hours to minutes for troubleshoot reported incidents reviews while ensuring the numbers in the slides match D365 to the cent.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build an executive PowerPoint deck on troubleshoot reported incidents for a 15-minute monthly review. Produce 'ppt-exec-troubleshoot-reported-incidents-2026-05-24.pptx' with: (1) title slide, (2) headline KPIs, (3) trend chart vs prior period, (4) top issues / red flags, (5) recommended actions, (6) appendix - data sources and methodology. Include speaker-notes on each slide with talking points. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads troubleshoot reported incidents data and produces a 6-8 slide PowerPoint suitable for an executive review.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only executive PowerPoint deck on reported-incident troubleshooting status from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, issues, actions and appendix slides plus speaker notes.', 'example_request': 'Build the exec PowerPoint on troubleshoot reported incidents from D365 USMF for our 15-minute monthly review.', 'inputs': [{'description': 'Dynamics 365 legal entity to pull data from, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-troubleshoot-reported-incidents-2026-05-24.pptx.', 'name': 'output_filename'}, {'description': 'Reporting period and comparison prior period for the trend chart (e.g. monthly review).', 'name': 'review_period'}, {'description': 'Length of the review the deck must fit, e.g. 15 minutes.', 'name': 'meeting_length'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user needs an executive-ready incident troubleshooting deck for a short monthly review, sourced from D365 ERP data without modifying it.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class PptExecTroubleshootReportedIncidents(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecTroubleshootReportedIncidents'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to pull data from, e.g. USMF.', 'type': 'string'}, 'meeting_length': {'description': 'Length of the review the deck must fit, e.g. 15 minutes.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-troubleshoot-reported-incidents-2026-05-24.pptx.', 'type': 'string'}, 'review_period': {'description': 'Reporting period and comparison prior period for the trend chart (e.g. monthly review).', 'type': 'string'}},
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
    print(PptExecTroubleshootReportedIncidents().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
