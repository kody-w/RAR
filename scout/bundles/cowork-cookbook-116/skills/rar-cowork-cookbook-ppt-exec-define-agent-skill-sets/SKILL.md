---
name: "rar-cowork-cookbook-ppt-exec-define-agent-skill-sets"
description: "Builds a read-only executive PowerPoint deck on agent skill set status from Dynamics 365 ERP data for a given legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_define_agent_skill_sets", "rar_sha256": "1c18c156cdacd0ffb876ff6c0d8c807ba071b781d6961e3dcb970ab442580a57", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_define_agent_skill_sets`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_define_agent_skill_sets_agent.py` and in the RCI capsule.

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

Define agent skill sets Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on agent skill set status from Dynamics 365 ERP data for a given legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-define-agent-skill-sets
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
      "description": "Dynamics 365 legal entity to pull data from, e.g. USMF.",
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
      "description": "Name of the .pptx file to produce, e.g. ppt-exec-define-agent-skill-sets-2026-05-24.pptx.",
      "type": "string"
    },
    "review_length": {
      "description": "Intended briefing duration, e.g. 15-minute monthly review.",
      "type": "string"
    },
    "topic": {
      "description": "Subject of the deck, e.g. define agent skill sets.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_define_agent_skill_sets_agent.py` and embedded as the fenced Python below (sha256 1c18c156cdacd0ff…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_define_agent_skill_sets_agent.py` first:

```bash
python3 ppt_exec_define_agent_skill_sets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_define_agent_skill_sets_agent.py   # or on stdin
python3 ppt_exec_define_agent_skill_sets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define agent skill sets Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on agent skill set status from Dynamics 365 ERP data for a given legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-define-agent-skill-sets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_define_agent_skill_sets',
    "version": '3.0.3',
    "display_name": 'Define agent skill sets Executive PowerPoint Deck',
    "description": 'Builds a read-only executive PowerPoint deck on agent skill set status from Dynamics 365 ERP data for a given legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'case_to_resolution', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-define-agent-skill-sets',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-define-agent-skill-sets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '64ad0bbb221d3b96',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/define-customer-and-employee-service-operations/define-agent-skill-sets'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/ppt-exec-define-agent-skill-sets', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'comparison_period': 'Prior period to trend the KPIs against.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to pull data from, e.g. USMF.', 'output_filename': 'Name of the .pptx file to produce, e.g. ppt-exec-define-agent-skill-sets-2026-05-24.pptx.', 'review_length': 'Intended briefing duration, e.g. 15-minute monthly review.', 'topic': 'Subject of the deck, e.g. define agent skill sets.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Cuts deck prep time from hours to minutes for define agent skill sets reviews while ensuring the numbers in the slides match D365 to the cent.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build an executive PowerPoint deck on define agent skill sets for a 15-minute monthly review. Produce 'ppt-exec-define-agent-skill-sets-2026-05-24.pptx' with: (1) title slide, (2) headline KPIs, (3) trend chart vs prior period, (4) top issues / red flags, (5) recommended actions, (6) appendix - data sources and methodology. Include speaker-notes on each slide with talking points. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads define agent skill sets data and produces a 6-8 slide PowerPoint suitable for an executive review.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only executive PowerPoint deck on agent skill set status from Dynamics 365 ERP data for a given legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.', 'example_request': 'Make an exec PowerPoint on define agent skill sets from D365 USMF for our 15-minute monthly review.', 'inputs': [{'description': 'Dynamics 365 legal entity to pull data from, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Subject of the deck, e.g. define agent skill sets.', 'name': 'topic'}, {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-define-agent-skill-sets-2026-05-24.pptx.', 'name': 'output_filename'}, {'description': 'Intended briefing duration, e.g. 15-minute monthly review.', 'name': 'review_length'}, {'description': 'Prior period to trend the KPIs against.', 'name': 'comparison_period'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants an executive-ready PPTX summarizing define-agent-skill-sets status from D365 F&SCM for a monthly review, without changing any data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class PptExecDefineAgentSkillSets(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecDefineAgentSkillSets'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'comparison_period': {'description': 'Prior period to trend the KPIs against.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to pull data from, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-define-agent-skill-sets-2026-05-24.pptx.', 'type': 'string'}, 'review_length': {'description': 'Intended briefing duration, e.g. 15-minute monthly review.', 'type': 'string'}, 'topic': {'description': 'Subject of the deck, e.g. define agent skill sets.', 'type': 'string'}},
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
    print(PptExecDefineAgentSkillSets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
