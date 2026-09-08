---
name: "rar-cowork-cookbook-teams-update-record-employee-absences"
description: "Summarizes employee absence records from Dynamics 365 F&SCM for a given legal entity and returns a Teams channel post in markdown plus an Adaptive Card JSON file with KPIs and quick-action buttons, saved for review rathe"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_record_employee_absences", "rar_sha256": "7cea8c0afd97ef7e5453ad76c54eebe2034f307bafdc518626073ff80627c14a", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_record_employee_absences`. The original RAPP
agent is preserved byte-for-byte in `teams_update_record_employee_absences_agent.py` and in the RCI capsule.

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

Record employee absences Teams Channel Update — Summarizes employee absence records from Dynamics 365 F&SCM for a given legal entity and returns a Teams channel post in markdown plus an Adaptive Card JSON file with KPIs and quick-action buttons, saved for review rathe

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-record-employee-absences
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
      "description": "Output filename for the Adaptive Card JSON, e.g. teams-update-record-employee-absences-2026-05-24-card.json.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to query, e.g. USMF.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_record_employee_absences_agent.py` and embedded as the fenced Python below (sha256 7cea8c0afd97ef7e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_record_employee_absences_agent.py` first:

```bash
python3 teams_update_record_employee_absences_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_record_employee_absences_agent.py   # or on stdin
python3 teams_update_record_employee_absences_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Record employee absences Teams Channel Update — Summarizes employee absence records from Dynamics 365 F&SCM for a given legal entity and returns a Teams channel post in markdown plus an Adaptive Card JSON file with KPIs and quick-action buttons, saved for review rathe

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-record-employee-absences
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_record_employee_absences',
    "version": '3.0.3',
    "display_name": 'Record employee absences Teams Channel Update',
    "description": 'Summarizes employee absence records from Dynamics 365 F&SCM for a given legal entity and returns a Teams channel post in markdown plus an Adaptive Card JSON file with KPIs and quick-action buttons, saved for review rathe',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'hire_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-record-employee-absences',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-record-employee-absences',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '8f875e2b7c86acd7',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/manage-time-and-attendance/record-employee-absences'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/teams-update-record-employee-absences', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'card_filename': 'Output filename for the Adaptive Card JSON, e.g. teams-update-record-employee-absences-2026-05-24-card.json.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Replaces 'check the spreadsheet' Teams pings with a glanceable card the team can act on directly - reducing back-and-forth and decision latency.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, summarize the current state of record employee absences. Produce: (a) a Communications-ready Teams channel post (markdown) with a 2-sentence summary and 3 bullet highlights; (b) an Adaptive Card JSON 'teams-update-record-employee-absences-2026-05-24-card.json' showing KPIs, status indicators, and quick-action buttons (e.g., 'View detail', 'Open in D365'). Do not post the card on my behalf - save the artifacts for me to review.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads record employee absences, produces a Communications-ready Teams post + an Adaptive Card with quick-action buttons.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Summarizes employee absence records from Dynamics 365 F&SCM for a given legal entity and returns a Teams channel post in markdown plus an Adaptive Card JSON file with KPIs and quick-action buttons, saved for review rathe', 'example_request': 'Draft a Teams update on employee absences in USMF with an Adaptive Card I can review before posting.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Output filename for the Adaptive Card JSON, e.g. teams-update-record-employee-absences-2026-05-24-card.json.', 'name': 'card_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a draft Teams channel update on employee absence status from D365 ERP data, with an Adaptive Card artifact they will review before posting.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class TeamsUpdateRecordEmployeeAbsences(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateRecordEmployeeAbsences'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'card_filename': {'description': 'Output filename for the Adaptive Card JSON, e.g. teams-update-record-employee-absences-2026-05-24-card.json.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(TeamsUpdateRecordEmployeeAbsences().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
