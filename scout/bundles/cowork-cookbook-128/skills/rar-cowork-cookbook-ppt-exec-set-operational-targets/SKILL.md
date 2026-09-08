---
name: "rar-cowork-cookbook-ppt-exec-set-operational-targets"
description: "Builds a read-only executive PowerPoint deck on set operational targets from Dynamics 365 F&SCM data (title, KPIs, trend vs prior period, red flags, actions, appendix) with speaker notes; call for a 15-minute monthly rev"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_set_operational_targets", "rar_sha256": "15a24493ca7a8febcbb36169a018aa15cf40d46365e05f150c684eff90fa2225", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_set_operational_targets`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_set_operational_targets_agent.py` and in the RCI capsule.

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

Set operational targets Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on set operational targets from Dynamics 365 F&SCM data (title, KPIs, trend vs prior period, red flags, actions, appendix) with speaker notes; call for a 15-minute monthly rev

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-set-operational-targets
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
      "description": "Dynamics 365 legal entity to report on (e.g. USMF).",
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
      "description": "Name of the .pptx file to produce, e.g. ppt-exec-set-operational-targets-2026-05-24.pptx.",
      "type": "string"
    },
    "review_length": {
      "description": "Target briefing length the deck is scoped to, e.g. 15-minute monthly review.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_set_operational_targets_agent.py` and embedded as the fenced Python below (sha256 15a24493ca7a8feb…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_set_operational_targets_agent.py` first:

```bash
python3 ppt_exec_set_operational_targets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_set_operational_targets_agent.py   # or on stdin
python3 ppt_exec_set_operational_targets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Set operational targets Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on set operational targets from Dynamics 365 F&SCM data (title, KPIs, trend vs prior period, red flags, actions, appendix) with speaker notes; call for a 15-minute monthly rev

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-set-operational-targets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_set_operational_targets',
    "version": '3.0.3',
    "display_name": 'Set operational targets Executive PowerPoint Deck',
    "description": 'Builds a read-only executive PowerPoint deck on set operational targets from Dynamics 365 F&SCM data (title, KPIs, trend vs prior period, red flags, actions, appendix) with speaker notes; call for a 15-minute monthly rev',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'forecast_to_plan', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-set-operational-targets',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-set-operational-targets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '182730e7c2dfbb07',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/conduct-financial-planning/set-operational-targets'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/ppt-exec-set-operational-targets', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to report on (e.g. USMF).', 'output_filename': 'Name of the .pptx file to produce, e.g. ppt-exec-set-operational-targets-2026-05-24.pptx.', 'review_length': 'Target briefing length the deck is scoped to, e.g. 15-minute monthly review.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Cuts deck prep time from hours to minutes for set operational targets reviews while ensuring the numbers in the slides match D365 to the cent.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build an executive PowerPoint deck on set operational targets for a 15-minute monthly review. Produce 'ppt-exec-set-operational-targets-2026-05-24.pptx' with: (1) title slide, (2) headline KPIs, (3) trend chart vs prior period, (4) top issues / red flags, (5) recommended actions, (6) appendix - data sources and methodology. Include speaker-notes on each slide with talking points. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads set operational targets data and produces a 6-8 slide PowerPoint suitable for an executive review.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only executive PowerPoint deck on set operational targets from Dynamics 365 F&SCM data (title, KPIs, trend vs prior period, red flags, actions, appendix) with speaker notes; call for a 15-minute monthly rev', 'example_request': 'Build the executive PowerPoint on set operational targets for USMF for our 15-minute monthly review.', 'inputs': [{'description': 'Dynamics 365 legal entity to report on (e.g. USMF).', 'name': 'legal_entity'}, {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-set-operational-targets-2026-05-24.pptx.', 'name': 'output_filename'}, {'description': 'Target briefing length the deck is scoped to, e.g. 15-minute monthly review.', 'name': 'review_length'}], 'model': 'claude-opus-5', 'when_to_use': 'Use when you need an executive-ready PPTX summarizing operational target status from D365 ERP for a monthly review, without modifying any data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class PptExecSetOperationalTargets(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecSetOperationalTargets'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to report on (e.g. USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-set-operational-targets-2026-05-24.pptx.', 'type': 'string'}, 'review_length': {'description': 'Target briefing length the deck is scoped to, e.g. 15-minute monthly review.', 'type': 'string'}},
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
    print(PptExecSetOperationalTargets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
