---
name: "rar-cowork-cookbook-teams-update-clean-up-and-view-log-storage"
description: "Summarizes clean up and view log storage status from the Dynamics 365 ERP plugin for a given legal entity and returns a draft Teams channel post plus an Adaptive Card JSON file, saved for review rather than posted."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_clean_up_and_view_log_storage", "rar_sha256": "d542a98a371e775e2b0c097c4b48dd72a0e6c49fbe5dfe9367b851c7d3f57a40", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
