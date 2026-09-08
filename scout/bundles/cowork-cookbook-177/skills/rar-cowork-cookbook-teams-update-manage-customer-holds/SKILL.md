---
name: "rar-cowork-cookbook-teams-update-manage-customer-holds"
description: "Summarizes customer hold status from Dynamics 365 F&SCM for a legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons; nothing is posted."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_manage_customer_holds", "rar_sha256": "58b9e108e9dda3795a17bb946192046572fc4d3ea396769a47f73e8ca7395b37", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
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
