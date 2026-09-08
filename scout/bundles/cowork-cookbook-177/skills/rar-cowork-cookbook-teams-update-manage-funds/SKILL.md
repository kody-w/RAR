---
name: "rar-cowork-cookbook-teams-update-manage-funds"
description: "Summarizes manage funds status from Dynamics 365 F&SCM for a given legal entity and returns a markdown Teams channel post plus an Adaptive Card JSON file with KPIs and quick-action buttons; saves artifacts without postin"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_manage_funds", "rar_sha256": "020d82089249b6b5e10a4cab5384c070ce4f567aaaa225d4cdf41227bab0db9d", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_manage_funds`. The original RAPP
agent is preserved byte-for-byte in `teams_update_manage_funds_agent.py` and in the RCI capsule.

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

Manage funds Teams Channel Update — Summarizes manage funds status from Dynamics 365 F&SCM for a given legal entity and returns a markdown Teams channel post plus an Adaptive Card JSON file with KPIs and quick-action buttons; saves artifacts without postin

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-manage-funds
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
      "description": "Filename for the Adaptive Card JSON, e.g. teams-update-manage-funds-2026-05-24-card.json.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to summarize, e.g. USMF.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_manage_funds_agent.py` and embedded as the fenced Python below (sha256 020d82089249b6b5…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_manage_funds_agent.py` first:

```bash
python3 teams_update_manage_funds_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_manage_funds_agent.py   # or on stdin
python3 teams_update_manage_funds_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage funds Teams Channel Update — Summarizes manage funds status from Dynamics 365 F&SCM for a given legal entity and returns a markdown Teams channel post plus an Adaptive Card JSON file with KPIs and quick-action buttons; saves artifacts without postin

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-manage-funds
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_manage_funds',
    "version": '3.0.3',
    "display_name": 'Manage funds Teams Channel Update',
    "description": 'Summarizes manage funds status from Dynamics 365 F&SCM for a given legal entity and returns a markdown Teams channel post plus an Adaptive Card JSON file with KPIs and quick-action buttons; saves artifacts without postin',
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
        "upstream_slug": 'teams-update-manage-funds',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-manage-funds',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'a259a34791c140ba',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/manage-cash/manage-funds'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/teams-update-manage-funds', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'card_filename': 'Filename for the Adaptive Card JSON, e.g. teams-update-manage-funds-2026-05-24-card.json.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to summarize, e.g. USMF.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Replaces 'check the spreadsheet' Teams pings with a glanceable card the team can act on directly - reducing back-and-forth and decision latency.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, summarize the current state of manage funds. Produce: (a) a Communications-ready Teams channel post (markdown) with a 2-sentence summary and 3 bullet highlights; (b) an Adaptive Card JSON 'teams-update-manage-funds-2026-05-24-card.json' showing KPIs, status indicators, and quick-action buttons (e.g., 'View detail', 'Open in D365'). Do not post the card on my behalf - save the artifacts for me to review.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-25', 'what_it_does': 'Reads manage funds, produces a Communications-ready Teams post + an Adaptive Card with quick-action buttons.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Summarizes manage funds status from Dynamics 365 F&SCM for a given legal entity and returns a markdown Teams channel post plus an Adaptive Card JSON file with KPIs and quick-action buttons; saves artifacts without postin', 'example_request': "Draft a Teams post and Adaptive Card on manage funds status in D365 for USMF — save them, don't post.", 'inputs': [{'description': 'D365 legal entity to summarize, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Filename for the Adaptive Card JSON, e.g. teams-update-manage-funds-2026-05-24-card.json.', 'name': 'card_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a review-ready Teams update on manage funds status from D365 ERP, with an Adaptive Card for triage, saved rather than posted.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class TeamsUpdateManageFunds(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateManageFunds'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'card_filename': {'description': 'Filename for the Adaptive Card JSON, e.g. teams-update-manage-funds-2026-05-24-card.json.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to summarize, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(TeamsUpdateManageFunds().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
