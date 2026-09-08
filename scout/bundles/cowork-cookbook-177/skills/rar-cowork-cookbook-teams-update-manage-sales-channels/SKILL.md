---
name: "rar-cowork-cookbook-teams-update-manage-sales-channels"
description: "Summarizes the current state of manage sales channels from Dynamics 365 F&SCM for a legal entity and returns a Teams-ready markdown post plus an Adaptive Card JSON file saved for review, never posted."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_manage_sales_channels", "rar_sha256": "f1ca32c973b637c44f3f119b580bcd9d85a2fc5dae8a6d6240829182177dcad5", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
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
