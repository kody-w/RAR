---
name: "rar-cowork-cookbook-teams-update-manage-sales-channels"
description: "Summarizes the current state of manage sales channels from Dynamics 365 F&SCM for a legal entity and returns a Teams-ready markdown post plus an Adaptive Card JSON file saved for review, never posted."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_manage_sales_channels", "rar_sha256": "f1ca32c973b637c44f3f119b580bcd9d85a2fc5dae8a6d6240829182177dcad5", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_manage_sales_channels`. The original RAPP
agent is preserved byte-for-byte in `teams_update_manage_sales_channels_agent.py` and in the RCI capsule.

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

Manage sales channels Teams Channel Update — Summarizes the current state of manage sales channels from Dynamics 365 F&SCM for a legal entity and returns a Teams-ready markdown post plus an Adaptive Card JSON file saved for review, never posted.

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-manage-sales-channels
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
      "description": "Date used in the summary and card filename, e.g. 2026-05-24.",
      "type": "string"
    },
    "card_filename": {
      "description": "Output name for the Adaptive Card JSON artifact.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to report on, e.g. USMF.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_manage_sales_channels_agent.py` and embedded as the fenced Python below (sha256 f1ca32c973b637c4…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_manage_sales_channels_agent.py` first:

```bash
python3 teams_update_manage_sales_channels_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_manage_sales_channels_agent.py   # or on stdin
python3 teams_update_manage_sales_channels_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage sales channels Teams Channel Update — Summarizes the current state of manage sales channels from Dynamics 365 F&SCM for a legal entity and returns a Teams-ready markdown post plus an Adaptive Card JSON file saved for review, never posted.

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-manage-sales-channels
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_manage_sales_channels',
    "version": '3.0.3',
    "display_name": 'Manage sales channels Teams Channel Update',
    "description": 'Summarizes the current state of manage sales channels from Dynamics 365 F&SCM for a legal entity and returns a Teams-ready markdown post plus an Adaptive Card JSON file saved for review, never posted.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'order_to_cash', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-manage-sales-channels',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-manage-sales-channels',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '3eba98b830ba8559',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/develop-sales-policies/manage-sales-channels'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/teams-update-manage-sales-channels', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'as_of_date': 'Date used in the summary and card filename, e.g. 2026-05-24.', 'card_filename': 'Output name for the Adaptive Card JSON artifact.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report on, e.g. USMF.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Replaces 'check the spreadsheet' Teams pings with a glanceable card the team can act on directly - reducing back-and-forth and decision latency.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, summarize the current state of manage sales channels. Produce: (a) a Communications-ready Teams channel post (markdown) with a 2-sentence summary and 3 bullet highlights; (b) an Adaptive Card JSON 'teams-update-manage-sales-channels-2026-05-24-card.json' showing KPIs, status indicators, and quick-action buttons (e.g., 'View detail', 'Open in D365'). Do not post the card on my behalf - save the artifacts for me to review.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads manage sales channels, produces a Communications-ready Teams post + an Adaptive Card with quick-action buttons.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Summarizes the current state of manage sales channels from Dynamics 365 F&SCM for a legal entity and returns a Teams-ready markdown post plus an Adaptive Card JSON file saved for review, never posted.', 'example_request': "Draft a Teams update on manage sales channels for USMF as of 2026-05-24 with an Adaptive Card — don't post it.", 'inputs': [{'description': 'D365 legal entity to report on, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Date used in the summary and card filename, e.g. 2026-05-24.', 'name': 'as_of_date'}, {'description': 'Output name for the Adaptive Card JSON artifact.', 'name': 'card_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a drafted Teams channel update and triage Adaptive Card on manage sales channels status from D365 ERP data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class TeamsUpdateManageSalesChannels(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateManageSalesChannels'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'as_of_date': {'description': 'Date used in the summary and card filename, e.g. 2026-05-24.', 'type': 'string'}, 'card_filename': {'description': 'Output name for the Adaptive Card JSON artifact.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report on, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(TeamsUpdateManageSalesChannels().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
