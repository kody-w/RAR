---
name: "rar-cowork-cookbook-teams-update-record-employee-absences"
description: "Summarizes employee absence records from Dynamics 365 F&SCM for a given legal entity and returns a Teams channel post in markdown plus an Adaptive Card JSON file with KPIs and quick-action buttons, saved for review rathe"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_record_employee_absences", "rar_sha256": "7cea8c0afd97ef7e5453ad76c54eebe2034f307bafdc518626073ff80627c14a", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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
