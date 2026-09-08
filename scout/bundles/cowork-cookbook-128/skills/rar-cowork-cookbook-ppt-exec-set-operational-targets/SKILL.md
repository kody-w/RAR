---
name: "rar-cowork-cookbook-ppt-exec-set-operational-targets"
description: "Builds a read-only executive PowerPoint deck on set operational targets from Dynamics 365 F&SCM data (title, KPIs, trend vs prior period, red flags, actions, appendix) with speaker notes; call for a 15-minute monthly rev"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_set_operational_targets", "rar_sha256": "15a24493ca7a8febcbb36169a018aa15cf40d46365e05f150c684eff90fa2225", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
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
