---
name: "rar-cowork-cookbook-teams-update-negotiate-project-contracts"
description: "Summarizes negotiate project contracts status from Dynamics 365 ERP for a legal entity and saves two artifacts for review: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons; nothi"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_negotiate_project_contracts", "rar_sha256": "85e132a20633d924b92624244fb902b3e786efd9e017a52434633c2b7d8c891d", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
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
