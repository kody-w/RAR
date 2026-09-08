---
name: "rar-cowork-cookbook-teams-update-manage-accruals"
description: "Summarizes manage accruals status from Dynamics 365 F&SCM for a given legal entity and returns a Teams-ready markdown channel post plus a saved Adaptive Card JSON with KPIs and quick-action buttons; does not post."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_manage_accruals", "rar_sha256": "029e56942d682c2e60d58fa850956e782363c9e7d1923b43164a6364c6209e84", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_manage_accruals`. The original RAPP
agent is preserved byte-for-byte in `teams_update_manage_accruals_agent.py` and in the RCI capsule.

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

Manage accruals Teams Channel Update — Summarizes manage accruals status from Dynamics 365 F&SCM for a given legal entity and returns a Teams-ready markdown channel post plus a saved Adaptive Card JSON with KPIs and quick-action buttons; does not post.

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-manage-accruals
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
      "description": "Filename for the generated Adaptive Card JSON, e.g. teams-update-manage-accruals-2026-05-24-card.json.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_manage_accruals_agent.py` and embedded as the fenced Python below (sha256 029e56942d682c2e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_manage_accruals_agent.py` first:

```bash
python3 teams_update_manage_accruals_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_manage_accruals_agent.py   # or on stdin
python3 teams_update_manage_accruals_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage accruals Teams Channel Update — Summarizes manage accruals status from Dynamics 365 F&SCM for a given legal entity and returns a Teams-ready markdown channel post plus a saved Adaptive Card JSON with KPIs and quick-action buttons; does not post.

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-manage-accruals
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_manage_accruals',
    "version": '3.0.3',
    "display_name": 'Manage accruals Teams Channel Update',
    "description": 'Summarizes manage accruals status from Dynamics 365 F&SCM for a given legal entity and returns a Teams-ready markdown channel post plus a saved Adaptive Card JSON with KPIs and quick-action buttons; does not post.',
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
        "upstream_slug": 'teams-update-manage-accruals',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-manage-accruals',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '4c366755010bda9a',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/record-financial-transactions/manage-accruals'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/teams-update-manage-accruals', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'card_filename': 'Filename for the generated Adaptive Card JSON, e.g. teams-update-manage-accruals-2026-05-24-card.json.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to summarize, e.g. USMF.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Replaces 'check the spreadsheet' Teams pings with a glanceable card the team can act on directly - reducing back-and-forth and decision latency.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, summarize the current state of manage accruals. Produce: (a) a Communications-ready Teams channel post (markdown) with a 2-sentence summary and 3 bullet highlights; (b) an Adaptive Card JSON 'teams-update-manage-accruals-2026-05-24-card.json' showing KPIs, status indicators, and quick-action buttons (e.g., 'View detail', 'Open in D365'). Do not post the card on my behalf - save the artifacts for me to review.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-25', 'what_it_does': 'Reads manage accruals, produces a Communications-ready Teams post + an Adaptive Card with quick-action buttons.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Summarizes manage accruals status from Dynamics 365 F&SCM for a given legal entity and returns a Teams-ready markdown channel post plus a saved Adaptive Card JSON with KPIs and quick-action buttons; does not post.', 'example_request': 'Draft a Teams update on manage accruals for USMF with an Adaptive Card I can review before posting.', 'inputs': [{'description': 'D365 legal entity to summarize, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Filename for the generated Adaptive Card JSON, e.g. teams-update-manage-accruals-2026-05-24-card.json.', 'name': 'card_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a reviewable Teams channel update on manage accruals status from D365 ERP, with an Adaptive Card artifact saved rather than posted.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class TeamsUpdateManageAccruals(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateManageAccruals'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'card_filename': {'description': 'Filename for the generated Adaptive Card JSON, e.g. teams-update-manage-accruals-2026-05-24-card.json.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to summarize, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(TeamsUpdateManageAccruals().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
