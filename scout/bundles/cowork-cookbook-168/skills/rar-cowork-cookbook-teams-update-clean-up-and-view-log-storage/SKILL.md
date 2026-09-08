---
name: "rar-cowork-cookbook-teams-update-clean-up-and-view-log-storage"
description: "Summarizes clean up and view log storage status from the Dynamics 365 ERP plugin for a given legal entity and returns a draft Teams channel post plus an Adaptive Card JSON file, saved for review rather than posted."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_clean_up_and_view_log_storage", "rar_sha256": "d542a98a371e775e2b0c097c4b48dd72a0e6c49fbe5dfe9367b851c7d3f57a40", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_clean_up_and_view_log_storage`. The original RAPP
agent is preserved byte-for-byte in `teams_update_clean_up_and_view_log_storage_agent.py` and in the RCI capsule.

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

Clean up and view log storage Teams Channel Update — Summarizes clean up and view log storage status from the Dynamics 365 ERP plugin for a given legal entity and returns a draft Teams channel post plus an Adaptive Card JSON file, saved for review rather than posted.

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-clean-up-and-view-log-storage
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
      "description": "Optional output filename for the Adaptive Card JSON artifact.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to report on, e.g. USMF.",
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
    "report_date": {
      "description": "Date used in the Adaptive Card filename, e.g. 2026-05-24.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_clean_up_and_view_log_storage_agent.py` and embedded as the fenced Python below (sha256 d542a98a371e775e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_clean_up_and_view_log_storage_agent.py` first:

```bash
python3 teams_update_clean_up_and_view_log_storage_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_clean_up_and_view_log_storage_agent.py   # or on stdin
python3 teams_update_clean_up_and_view_log_storage_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Clean up and view log storage Teams Channel Update — Summarizes clean up and view log storage status from the Dynamics 365 ERP plugin for a given legal entity and returns a draft Teams channel post plus an Adaptive Card JSON file, saved for review rather than posted.

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-clean-up-and-view-log-storage
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_clean_up_and_view_log_storage',
    "version": '3.0.3',
    "display_name": 'Clean up and view log storage Teams Channel Update',
    "description": 'Summarizes clean up and view log storage status from the Dynamics 365 ERP plugin for a given legal entity and returns a draft Teams channel post plus an Adaptive Card JSON file, saved for review rather than posted.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-clean-up-and-view-log-storage',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-clean-up-and-view-log-storage',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '504947e8122ebc70',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/monitor-systems-environments-and-capacity/clean-up-and-view-log-storage'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/teams-update-clean-up-and-view-log-storage', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'card_filename': 'Optional output filename for the Adaptive Card JSON artifact.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report on, e.g. USMF.', 'report_date': 'Date used in the Adaptive Card filename, e.g. 2026-05-24.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Replaces 'check the spreadsheet' Teams pings with a glanceable card the team can act on directly - reducing back-and-forth and decision latency.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, summarize the current state of clean up and view log storage. Produce: (a) a Communications-ready Teams channel post (markdown) with a 2-sentence summary and 3 bullet highlights; (b) an Adaptive Card JSON 'teams-update-clean-up-and-view-log-storage-2026-05-24-card.json' showing KPIs, status indicators, and quick-action buttons (e.g., 'View detail', 'Open in D365'). Do not post the card on my behalf - save the artifacts for me to review.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads clean up and view log storage, produces a Communications-ready Teams post + an Adaptive Card with quick-action buttons.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Summarizes clean up and view log storage status from the Dynamics 365 ERP plugin for a given legal entity and returns a draft Teams channel post plus an Adaptive Card JSON file, saved for review rather than posted.', 'example_request': 'Draft a Teams post and Adaptive Card on clean up and view log storage status for USMF, dated 2026-05-24.', 'inputs': [{'description': 'D365 legal entity to report on, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Date used in the Adaptive Card filename, e.g. 2026-05-24.', 'name': 'report_date'}, {'description': 'Optional output filename for the Adaptive Card JSON artifact.', 'name': 'card_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need a ready-to-review Teams update on clean up and view log storage status in D365 F&SCM, with KPIs and quick-action buttons.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class TeamsUpdateCleanUpAndViewLogStorage(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateCleanUpAndViewLogStorage'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'card_filename': {'description': 'Optional output filename for the Adaptive Card JSON artifact.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report on, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'report_date': {'description': 'Date used in the Adaptive Card filename, e.g. 2026-05-24.', 'type': 'string'}},
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
    print(TeamsUpdateCleanUpAndViewLogStorage().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
