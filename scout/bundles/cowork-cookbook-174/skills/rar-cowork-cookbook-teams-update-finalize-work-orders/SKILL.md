---
name: "rar-cowork-cookbook-teams-update-finalize-work-orders"
description: "Summarizes finalize work orders status from the Dynamics 365 ERP plugin for a legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON; does not post anything."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_finalize_work_orders", "rar_sha256": "eb14042b2e6f58c7f834a875afff6ba2993ffce44d74e49736c66202bd26d5fa", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_finalize_work_orders`. The original RAPP
agent is preserved byte-for-byte in `teams_update_finalize_work_orders_agent.py` and in the RCI capsule.

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

Finalize work orders Teams Channel Update — Summarizes finalize work orders status from the Dynamics 365 ERP plugin for a legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON; does not post anything.

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-finalize-work-orders
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
      "description": "Output filename for the Adaptive Card JSON, e.g. teams-update-finalize-work-orders-2026-05-24-card.json.",
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
    },
    "scope": {
      "description": "Optional scope adjustments for which finalize work orders to summarize.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_finalize_work_orders_agent.py` and embedded as the fenced Python below (sha256 eb14042b2e6f58c7…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_finalize_work_orders_agent.py` first:

```bash
python3 teams_update_finalize_work_orders_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_finalize_work_orders_agent.py   # or on stdin
python3 teams_update_finalize_work_orders_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Finalize work orders Teams Channel Update — Summarizes finalize work orders status from the Dynamics 365 ERP plugin for a legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON; does not post anything.

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-finalize-work-orders
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_finalize_work_orders',
    "version": '3.0.3',
    "display_name": 'Finalize work orders Teams Channel Update',
    "description": 'Summarizes finalize work orders status from the Dynamics 365 ERP plugin for a legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON; does not post anything.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'service_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-finalize-work-orders',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-finalize-work-orders',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '1f1cad881c87769d',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/deliver-services/finalize-work-orders'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/teams-update-finalize-work-orders', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'card_filename': 'Output filename for the Adaptive Card JSON, e.g. teams-update-finalize-work-orders-2026-05-24-card.json.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'scope': 'Optional scope adjustments for which finalize work orders to summarize.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Replaces 'check the spreadsheet' Teams pings with a glanceable card the team can act on directly - reducing back-and-forth and decision latency.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, summarize the current state of finalize work orders. Produce: (a) a Communications-ready Teams channel post (markdown) with a 2-sentence summary and 3 bullet highlights; (b) an Adaptive Card JSON 'teams-update-finalize-work-orders-2026-05-24-card.json' showing KPIs, status indicators, and quick-action buttons (e.g., 'View detail', 'Open in D365'). Do not post the card on my behalf - save the artifacts for me to review.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads finalize work orders, produces a Communications-ready Teams post + an Adaptive Card with quick-action buttons.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Summarizes finalize work orders status from the Dynamics 365 ERP plugin for a legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON; does not post anything.', 'example_request': "Draft a Teams update on finalize work orders in USMF with an Adaptive Card, but don't post it.", 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Output filename for the Adaptive Card JSON, e.g. teams-update-finalize-work-orders-2026-05-24-card.json.', 'name': 'card_filename'}, {'description': 'Optional scope adjustments for which finalize work orders to summarize.', 'name': 'scope'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a review-ready Teams channel update plus Adaptive Card on finalize work orders status from D365 F&SCM, without auto-posting.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class TeamsUpdateFinalizeWorkOrders(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateFinalizeWorkOrders'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'card_filename': {'description': 'Output filename for the Adaptive Card JSON, e.g. teams-update-finalize-work-orders-2026-05-24-card.json.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'scope': {'description': 'Optional scope adjustments for which finalize work orders to summarize.', 'type': 'string'}},
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
    print(TeamsUpdateFinalizeWorkOrders().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
