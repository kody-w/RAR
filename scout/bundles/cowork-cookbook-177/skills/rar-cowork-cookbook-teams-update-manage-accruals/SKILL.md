---
name: "rar-cowork-cookbook-teams-update-manage-accruals"
description: "Summarizes manage accruals status from Dynamics 365 F&SCM for a given legal entity and returns a Teams-ready markdown channel post plus a saved Adaptive Card JSON with KPIs and quick-action buttons; does not post."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_manage_accruals", "rar_sha256": "029e56942d682c2e60d58fa850956e782363c9e7d1923b43164a6364c6209e84", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
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
