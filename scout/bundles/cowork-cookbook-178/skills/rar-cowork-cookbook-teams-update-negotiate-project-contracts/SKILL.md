---
name: "rar-cowork-cookbook-teams-update-negotiate-project-contracts"
description: "Summarizes negotiate project contracts status from Dynamics 365 ERP for a legal entity and saves two artifacts for review: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons; nothi"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_negotiate_project_contracts", "rar_sha256": "85e132a20633d924b92624244fb902b3e786efd9e017a52434633c2b7d8c891d", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_negotiate_project_contracts`. The original RAPP
agent is preserved byte-for-byte in `teams_update_negotiate_project_contracts_agent.py` and in the RCI capsule.

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

Negotiate project contracts Teams Channel Update — Summarizes negotiate project contracts status from Dynamics 365 ERP for a legal entity and saves two artifacts for review: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons; nothi

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-negotiate-project-contracts
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
    "as_of_date": {
      "description": "Date used for the status snapshot and in the card filename, e.g. 2026-05-24.",
      "type": "string"
    },
    "card_filename": {
      "description": "Output name for the Adaptive Card JSON, e.g. teams-update-negotiate-project-contracts-2026-05-24-card.json.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_negotiate_project_contracts_agent.py` and embedded as the fenced Python below (sha256 85e132a20633d924…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_negotiate_project_contracts_agent.py` first:

```bash
python3 teams_update_negotiate_project_contracts_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_negotiate_project_contracts_agent.py   # or on stdin
python3 teams_update_negotiate_project_contracts_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Negotiate project contracts Teams Channel Update — Summarizes negotiate project contracts status from Dynamics 365 ERP for a legal entity and saves two artifacts for review: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons; nothi

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-negotiate-project-contracts
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_negotiate_project_contracts',
    "version": '3.0.3',
    "display_name": 'Negotiate project contracts Teams Channel Update',
    "description": 'Summarizes negotiate project contracts status from Dynamics 365 ERP for a legal entity and saves two artifacts for review: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons; nothi',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'project_to_profit', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-negotiate-project-contracts',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-negotiate-project-contracts',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '56f4b903d3c6e5ee',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/manage-project-contracts/negotiate-project-contracts'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/teams-update-negotiate-project-contracts', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'as_of_date': 'Date used for the status snapshot and in the card filename, e.g. 2026-05-24.', 'card_filename': 'Output name for the Adaptive Card JSON, e.g. teams-update-negotiate-project-contracts-2026-05-24-card.json.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to summarize, e.g. USMF.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Replaces 'check the spreadsheet' Teams pings with a glanceable card the team can act on directly - reducing back-and-forth and decision latency.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, summarize the current state of negotiate project contracts. Produce: (a) a Communications-ready Teams channel post (markdown) with a 2-sentence summary and 3 bullet highlights; (b) an Adaptive Card JSON 'teams-update-negotiate-project-contracts-2026-05-24-card.json' showing KPIs, status indicators, and quick-action buttons (e.g., 'View detail', 'Open in D365'). Do not post the card on my behalf - save the artifacts for me to review.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads negotiate project contracts, produces a Communications-ready Teams post + an Adaptive Card with quick-action buttons.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Summarizes negotiate project contracts status from Dynamics 365 ERP for a legal entity and saves two artifacts for review: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons; nothi', 'example_request': "Draft a Teams channel post and Adaptive Card on negotiate project contracts status for USMF as of 2026-05-24 — don't post it.", 'inputs': [{'description': 'D365 legal entity to summarize, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Date used for the status snapshot and in the card filename, e.g. 2026-05-24.', 'name': 'as_of_date'}, {'description': 'Output name for the Adaptive Card JSON, e.g. teams-update-negotiate-project-contracts-2026-05-24-card.json.', 'name': 'card_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need a review-ready Teams channel update on negotiate project contracts status from D365 F&SCM, without auto-posting it.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class TeamsUpdateNegotiateProjectContracts(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateNegotiateProjectContracts'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'as_of_date': {'description': 'Date used for the status snapshot and in the card filename, e.g. 2026-05-24.', 'type': 'string'}, 'card_filename': {'description': 'Output name for the Adaptive Card JSON, e.g. teams-update-negotiate-project-contracts-2026-05-24-card.json.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to summarize, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(TeamsUpdateNegotiateProjectContracts().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
