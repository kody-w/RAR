---
name: "rar-cowork-cookbook-teams-update-close-periods"
description: "Summarizes close periods status for a Dynamics 365 F&SCM legal entity and saves two artifacts: a markdown Teams channel post (2-sentence summary plus 3 bullets) and an Adaptive Card JSON; does not post anything."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_close_periods", "rar_sha256": "60bb0c237c18e04806b3f6528f6dd59f0fff6ad1d20e0dd1fba51db360c0a857", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
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
