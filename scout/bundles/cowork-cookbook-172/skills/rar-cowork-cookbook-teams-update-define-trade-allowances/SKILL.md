---
name: "rar-cowork-cookbook-teams-update-define-trade-allowances"
description: "Summarizes the current state of define trade allowances from Dynamics 365 ERP for a legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON; it does not post anything."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_define_trade_allowances", "rar_sha256": "2cc60cfe48a6d7e5cc75bc6091740e9874f73eb93467b4fb53dc0d693535ad58", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
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
