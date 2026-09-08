---
name: "rar-cowork-cookbook-ppt-exec-define-agent-skill-sets"
description: "Builds a read-only executive PowerPoint deck on agent skill set status from Dynamics 365 ERP data for a given legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_define_agent_skill_sets", "rar_sha256": "1c18c156cdacd0ffb876ff6c0d8c807ba071b781d6961e3dcb970ab442580a57", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
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
