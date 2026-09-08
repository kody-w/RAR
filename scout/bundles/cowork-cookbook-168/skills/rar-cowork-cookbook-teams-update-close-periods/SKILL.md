---
name: "rar-cowork-cookbook-teams-update-close-periods"
description: "Summarizes close periods status for a Dynamics 365 F&SCM legal entity and saves two artifacts: a markdown Teams channel post (2-sentence summary plus 3 bullets) and an Adaptive Card JSON; does not post anything."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_close_periods", "rar_sha256": "60bb0c237c18e04806b3f6528f6dd59f0fff6ad1d20e0dd1fba51db360c0a857", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_close_periods`. The original RAPP
agent is preserved byte-for-byte in `teams_update_close_periods_agent.py` and in the RCI capsule.

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

Close periods Teams Channel Update — Summarizes close periods status for a Dynamics 365 F&SCM legal entity and saves two artifacts: a markdown Teams channel post (2-sentence summary plus 3 bullets) and an Adaptive Card JSON; does not post anything.

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-close-periods
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
    "card_filename": {
      "description": "Filename for the saved Adaptive Card JSON, e.g. teams-update-close-periods-2026-05-24-card.json.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to summarize close periods for (e.g., USMF).",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_close_periods_agent.py` and embedded as the fenced Python below (sha256 60bb0c237c18e048…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_close_periods_agent.py` first:

```bash
python3 teams_update_close_periods_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_close_periods_agent.py   # or on stdin
python3 teams_update_close_periods_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Close periods Teams Channel Update — Summarizes close periods status for a Dynamics 365 F&SCM legal entity and saves two artifacts: a markdown Teams channel post (2-sentence summary plus 3 bullets) and an Adaptive Card JSON; does not post anything.

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-close-periods
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_close_periods',
    "version": '3.0.3',
    "display_name": 'Close periods Teams Channel Update',
    "description": 'Summarizes close periods status for a Dynamics 365 F&SCM legal entity and saves two artifacts: a markdown Teams channel post (2-sentence summary plus 3 bullets) and an Adaptive Card JSON; does not post anything.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'verified',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'teams-update-close-periods',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-close-periods',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'bdf354bd5ebd2272',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/close-financial-periods/close-periods'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/teams-update-close-periods', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'card_filename': 'Filename for the saved Adaptive Card JSON, e.g. teams-update-close-periods-2026-05-24-card.json.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to summarize close periods for (e.g., USMF).'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Replaces 'check the spreadsheet' Teams pings with a glanceable card the team can act on directly - reducing back-and-forth and decision latency.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, summarize the current state of close periods. Produce: (a) a Communications-ready Teams channel post (markdown) with a 2-sentence summary and 3 bullet highlights; (b) an Adaptive Card JSON 'teams-update-close-periods-2026-05-24-card.json' showing KPIs, status indicators, and quick-action buttons (e.g., 'View detail', 'Open in D365'). Do not post the card on my behalf - save the artifacts for me to review.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-25', 'what_it_does': 'Reads close periods, produces a Communications-ready Teams post + an Adaptive Card with quick-action buttons.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Summarizes close periods status for a Dynamics 365 F&SCM legal entity and saves two artifacts: a markdown Teams channel post (2-sentence summary plus 3 bullets) and an Adaptive Card JSON; does not post anything.', 'example_request': "Draft a Teams post and Adaptive Card on close periods status for USMF — save them, don't post.", 'inputs': [{'description': 'D365 legal entity to summarize close periods for (e.g., USMF).', 'name': 'legal_entity'}, {'description': 'Filename for the saved Adaptive Card JSON, e.g. teams-update-close-periods-2026-05-24-card.json.', 'name': 'card_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a review-ready Teams channel update on D365 close periods status with a KPI Adaptive Card, saved for manual posting.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class TeamsUpdateClosePeriods(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateClosePeriods'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'card_filename': {'description': 'Filename for the saved Adaptive Card JSON, e.g. teams-update-close-periods-2026-05-24-card.json.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to summarize close periods for (e.g., USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(TeamsUpdateClosePeriods().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
