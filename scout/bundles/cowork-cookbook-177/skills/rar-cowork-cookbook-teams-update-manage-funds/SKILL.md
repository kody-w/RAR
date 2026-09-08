---
name: "rar-cowork-cookbook-teams-update-manage-funds"
description: "Summarizes manage funds status from Dynamics 365 F&SCM for a given legal entity and returns a markdown Teams channel post plus an Adaptive Card JSON file with KPIs and quick-action buttons; saves artifacts without postin"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_manage_funds", "rar_sha256": "020d82089249b6b5e10a4cab5384c070ce4f567aaaa225d4cdf41227bab0db9d", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
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
