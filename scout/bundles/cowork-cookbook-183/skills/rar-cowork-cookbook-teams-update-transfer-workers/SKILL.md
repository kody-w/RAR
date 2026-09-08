---
name: "rar-cowork-cookbook-teams-update-transfer-workers"
description: "Summarizes transfer workers status from the Dynamics 365 ERP plugin for a given legal entity and saves two artifacts for review: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_transfer_workers", "rar_sha256": "490d11d3d240dd0e56e09ad19df78f3f0a5fcb0a83304406eb6e9ea0523ff40c", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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
