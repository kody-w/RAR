---
name: "rar-cowork-cookbook-ppt-exec-plan-software-releases"
description: "Builds a read-only executive PowerPoint deck on software release planning from Dynamics 365 F&SCM ERP data for a given legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_plan_software_releases", "rar_sha256": "310d3bd7be3a864af306239adef536a7d8c0c9e1055c29e779ff318229a64c55", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_plan_software_releases`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_plan_software_releases_agent.py` and in the RCI capsule.

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

Plan software releases Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on software release planning from Dynamics 365 F&SCM ERP data for a given legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-plan-software-releases
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
      "description": "Prior period used for the trend chart comparison.",
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
      "description": "Name of the .pptx file to produce, e.g. ppt-exec-plan-software-releases-2026-05-24.pptx.",
      "type": "string"
    },
    "review_length": {
      "description": "Intended briefing length the deck is scoped to, e.g. a 15-minute monthly review.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_plan_software_releases_agent.py` and embedded as the fenced Python below (sha256 310d3bd7be3a864a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_plan_software_releases_agent.py` first:

```bash
python3 ppt_exec_plan_software_releases_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_plan_software_releases_agent.py   # or on stdin
python3 ppt_exec_plan_software_releases_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Plan software releases Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on software release planning from Dynamics 365 F&SCM ERP data for a given legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-plan-software-releases
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_plan_software_releases',
    "version": '3.0.3',
    "display_name": 'Plan software releases Executive PowerPoint Deck',
    "description": 'Builds a read-only executive PowerPoint deck on software release planning from Dynamics 365 F&SCM ERP data for a given legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.',
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
        "upstream_slug": 'ppt-exec-plan-software-releases',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-plan-software-releases',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'a3386bb4bb31719c',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/uptake-software-releases/plan-software-releases'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/ppt-exec-plan-software-releases', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'comparison_period': 'Prior period used for the trend chart comparison.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to pull data from, e.g. USMF.', 'output_filename': 'Name of the .pptx file to produce, e.g. ppt-exec-plan-software-releases-2026-05-24.pptx.', 'review_length': 'Intended briefing length the deck is scoped to, e.g. a 15-minute monthly review.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Cuts deck prep time from hours to minutes for plan software releases reviews while ensuring the numbers in the slides match D365 to the cent.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build an executive PowerPoint deck on plan software releases for a 15-minute monthly review. Produce 'ppt-exec-plan-software-releases-2026-05-24.pptx' with: (1) title slide, (2) headline KPIs, (3) trend chart vs prior period, (4) top issues / red flags, (5) recommended actions, (6) appendix - data sources and methodology. Include speaker-notes on each slide with talking points. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads plan software releases data and produces a 6-8 slide PowerPoint suitable for an executive review.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only executive PowerPoint deck on software release planning from Dynamics 365 F&SCM ERP data for a given legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.', 'example_request': 'Build an exec PowerPoint on plan software releases from D365 USMF for our 15-minute monthly review.', 'inputs': [{'description': 'Dynamics 365 legal entity to pull data from, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-plan-software-releases-2026-05-24.pptx.', 'name': 'output_filename'}, {'description': 'Intended briefing length the deck is scoped to, e.g. a 15-minute monthly review.', 'name': 'review_length'}, {'description': 'Prior period used for the trend chart comparison.', 'name': 'comparison_period'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants an executive-ready PPTX summarizing software release planning status from D365 ERP data for a short monthly review.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class PptExecPlanSoftwareReleases(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecPlanSoftwareReleases'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'comparison_period': {'description': 'Prior period used for the trend chart comparison.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to pull data from, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-plan-software-releases-2026-05-24.pptx.', 'type': 'string'}, 'review_length': {'description': 'Intended briefing length the deck is scoped to, e.g. a 15-minute monthly review.', 'type': 'string'}},
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
    print(PptExecPlanSoftwareReleases().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
