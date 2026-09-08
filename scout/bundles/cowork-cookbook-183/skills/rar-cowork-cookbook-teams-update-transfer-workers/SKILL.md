---
name: "rar-cowork-cookbook-teams-update-transfer-workers"
description: "Summarizes transfer workers status from the Dynamics 365 ERP plugin for a given legal entity and saves two artifacts for review: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_transfer_workers", "rar_sha256": "490d11d3d240dd0e56e09ad19df78f3f0a5fcb0a83304406eb6e9ea0523ff40c", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_transfer_workers`. The original RAPP
agent is preserved byte-for-byte in `teams_update_transfer_workers_agent.py` and in the RCI capsule.

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

Transfer workers Teams Channel Update — Summarizes transfer workers status from the Dynamics 365 ERP plugin for a given legal entity and saves two artifacts for review: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-transfer-workers
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
      "description": "Output filename for the Adaptive Card JSON, e.g. teams-update-transfer-workers-2026-05-24-card.json.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_transfer_workers_agent.py` and embedded as the fenced Python below (sha256 490d11d3d240dd0e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_transfer_workers_agent.py` first:

```bash
python3 teams_update_transfer_workers_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_transfer_workers_agent.py   # or on stdin
python3 teams_update_transfer_workers_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Transfer workers Teams Channel Update — Summarizes transfer workers status from the Dynamics 365 ERP plugin for a given legal entity and saves two artifacts for review: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-transfer-workers
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_transfer_workers',
    "version": '3.0.3',
    "display_name": 'Transfer workers Teams Channel Update',
    "description": 'Summarizes transfer workers status from the Dynamics 365 ERP plugin for a given legal entity and saves two artifacts for review: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons.',
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
        "upstream_slug": 'teams-update-transfer-workers',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-transfer-workers',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '6c78ca0c060b8dbe',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/manage-performance-and-growth/transfer-workers'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/teams-update-transfer-workers', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'card_filename': 'Output filename for the Adaptive Card JSON, e.g. teams-update-transfer-workers-2026-05-24-card.json.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Replaces 'check the spreadsheet' Teams pings with a glanceable card the team can act on directly - reducing back-and-forth and decision latency.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, summarize the current state of transfer workers. Produce: (a) a Communications-ready Teams channel post (markdown) with a 2-sentence summary and 3 bullet highlights; (b) an Adaptive Card JSON 'teams-update-transfer-workers-2026-05-24-card.json' showing KPIs, status indicators, and quick-action buttons (e.g., 'View detail', 'Open in D365'). Do not post the card on my behalf - save the artifacts for me to review.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads transfer workers, produces a Communications-ready Teams post + an Adaptive Card with quick-action buttons.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Summarizes transfer workers status from the Dynamics 365 ERP plugin for a given legal entity and saves two artifacts for review: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons.', 'example_request': "Draft a Teams post and Adaptive Card on transfer workers status in USMF — don't post it, just save the files.", 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Output filename for the Adaptive Card JSON, e.g. teams-update-transfer-workers-2026-05-24-card.json.', 'name': 'card_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a draft Teams channel update on transfer workers status from D365 F&SCM, saved for review rather than posted.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class TeamsUpdateTransferWorkers(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateTransferWorkers'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'card_filename': {'description': 'Output filename for the Adaptive Card JSON, e.g. teams-update-transfer-workers-2026-05-24-card.json.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(TeamsUpdateTransferWorkers().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
