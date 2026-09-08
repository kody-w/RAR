---
name: "rar-cowork-cookbook-teams-update-define-trade-allowances"
description: "Summarizes the current state of define trade allowances from Dynamics 365 ERP for a legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON; it does not post anything."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_define_trade_allowances", "rar_sha256": "2cc60cfe48a6d7e5cc75bc6091740e9874f73eb93467b4fb53dc0d693535ad58", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_define_trade_allowances`. The original RAPP
agent is preserved byte-for-byte in `teams_update_define_trade_allowances_agent.py` and in the RCI capsule.

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

Define trade allowances Teams Channel Update — Summarizes the current state of define trade allowances from Dynamics 365 ERP for a legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON; it does not post anything.

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-define-trade-allowances
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
      "description": "Output name for the Adaptive Card JSON, e.g. teams-update-define-trade-allowances-2026-05-24-card.json.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_define_trade_allowances_agent.py` and embedded as the fenced Python below (sha256 2cc60cfe48a6d7e5…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_define_trade_allowances_agent.py` first:

```bash
python3 teams_update_define_trade_allowances_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_define_trade_allowances_agent.py   # or on stdin
python3 teams_update_define_trade_allowances_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define trade allowances Teams Channel Update — Summarizes the current state of define trade allowances from Dynamics 365 ERP for a legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON; it does not post anything.

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-define-trade-allowances
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_define_trade_allowances',
    "version": '3.0.3',
    "display_name": 'Define trade allowances Teams Channel Update',
    "description": 'Summarizes the current state of define trade allowances from Dynamics 365 ERP for a legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON; it does not post anything.',
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
        "upstream_slug": 'teams-update-define-trade-allowances',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-define-trade-allowances',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'd5837052b6b49015',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/develop-sales-policies/define-trade-allowances'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/teams-update-define-trade-allowances', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'card_filename': 'Output name for the Adaptive Card JSON, e.g. teams-update-define-trade-allowances-2026-05-24-card.json.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to summarize, e.g. USMF.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Replaces 'check the spreadsheet' Teams pings with a glanceable card the team can act on directly - reducing back-and-forth and decision latency.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, summarize the current state of define trade allowances. Produce: (a) a Communications-ready Teams channel post (markdown) with a 2-sentence summary and 3 bullet highlights; (b) an Adaptive Card JSON 'teams-update-define-trade-allowances-2026-05-24-card.json' showing KPIs, status indicators, and quick-action buttons (e.g., 'View detail', 'Open in D365'). Do not post the card on my behalf - save the artifacts for me to review.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads define trade allowances, produces a Communications-ready Teams post + an Adaptive Card with quick-action buttons.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Summarizes the current state of define trade allowances from Dynamics 365 ERP for a legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON; it does not post anything.', 'example_request': "Draft a Teams update on define trade allowances for USMF with an Adaptive Card — save it, don't post.", 'inputs': [{'description': 'D365 legal entity to summarize, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Output name for the Adaptive Card JSON, e.g. teams-update-define-trade-allowances-2026-05-24-card.json.', 'name': 'card_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need a review-ready Teams channel update on define trade allowances status, with KPIs and quick-action buttons, drafted but not posted.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class TeamsUpdateDefineTradeAllowances(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateDefineTradeAllowances'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'card_filename': {'description': 'Output name for the Adaptive Card JSON, e.g. teams-update-define-trade-allowances-2026-05-24-card.json.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to summarize, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(TeamsUpdateDefineTradeAllowances().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
