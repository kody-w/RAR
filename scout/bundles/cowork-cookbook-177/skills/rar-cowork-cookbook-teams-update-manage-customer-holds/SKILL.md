---
name: "rar-cowork-cookbook-teams-update-manage-customer-holds"
description: "Summarizes customer hold status from Dynamics 365 F&SCM for a legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons; nothing is posted."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_manage_customer_holds", "rar_sha256": "58b9e108e9dda3795a17bb946192046572fc4d3ea396769a47f73e8ca7395b37", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_manage_customer_holds`. The original RAPP
agent is preserved byte-for-byte in `teams_update_manage_customer_holds_agent.py` and in the RCI capsule.

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

Manage customer holds Teams Channel Update — Summarizes customer hold status from Dynamics 365 F&SCM for a legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons; nothing is posted.

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-manage-customer-holds
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
      "description": "Filename for the Adaptive Card JSON, e.g. teams-update-manage-customer-holds-2026-05-24-card.json.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_manage_customer_holds_agent.py` and embedded as the fenced Python below (sha256 58b9e108e9dda379…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_manage_customer_holds_agent.py` first:

```bash
python3 teams_update_manage_customer_holds_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_manage_customer_holds_agent.py   # or on stdin
python3 teams_update_manage_customer_holds_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage customer holds Teams Channel Update — Summarizes customer hold status from Dynamics 365 F&SCM for a legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons; nothing is posted.

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-manage-customer-holds
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_manage_customer_holds',
    "version": '3.0.3',
    "display_name": 'Manage customer holds Teams Channel Update',
    "description": 'Summarizes customer hold status from Dynamics 365 F&SCM for a legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons; nothing is posted.',
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
        "upstream_slug": 'teams-update-manage-customer-holds',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-manage-customer-holds',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '29556ce80f1dcb2e',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/manage-credit-and-collections/manage-customer-holds'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/teams-update-manage-customer-holds', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'card_filename': 'Filename for the Adaptive Card JSON, e.g. teams-update-manage-customer-holds-2026-05-24-card.json.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Replaces 'check the spreadsheet' Teams pings with a glanceable card the team can act on directly - reducing back-and-forth and decision latency.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, summarize the current state of manage customer holds. Produce: (a) a Communications-ready Teams channel post (markdown) with a 2-sentence summary and 3 bullet highlights; (b) an Adaptive Card JSON 'teams-update-manage-customer-holds-2026-05-24-card.json' showing KPIs, status indicators, and quick-action buttons (e.g., 'View detail', 'Open in D365'). Do not post the card on my behalf - save the artifacts for me to review.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads manage customer holds, produces a Communications-ready Teams post + an Adaptive Card with quick-action buttons.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Summarizes customer hold status from Dynamics 365 F&SCM for a legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons; nothing is posted.', 'example_request': "Summarize customer holds in USMF and draft a Teams post plus an Adaptive Card — just save them, don't post.", 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Filename for the Adaptive Card JSON, e.g. teams-update-manage-customer-holds-2026-05-24-card.json.', 'name': 'card_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a review-ready Teams update on customer holds in D365, with an Adaptive Card for triage, saved rather than posted.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class TeamsUpdateManageCustomerHolds(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateManageCustomerHolds'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'card_filename': {'description': 'Filename for the Adaptive Card JSON, e.g. teams-update-manage-customer-holds-2026-05-24-card.json.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(TeamsUpdateManageCustomerHolds().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
