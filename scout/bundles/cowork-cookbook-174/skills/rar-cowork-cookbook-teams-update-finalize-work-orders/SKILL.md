---
name: "rar-cowork-cookbook-teams-update-finalize-work-orders"
description: "Summarizes finalize work orders status from the Dynamics 365 ERP plugin for a legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON; does not post anything."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_finalize_work_orders", "rar_sha256": "eb14042b2e6f58c7f834a875afff6ba2993ffce44d74e49736c66202bd26d5fa", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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
