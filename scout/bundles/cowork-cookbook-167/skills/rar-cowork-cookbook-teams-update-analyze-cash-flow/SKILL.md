---
name: "rar-cowork-cookbook-teams-update-analyze-cash-flow"
description: "Summarizes cash flow status from Dynamics 365 F&SCM for a legal entity and saves two artifacts: a markdown Teams channel post (2-sentence summary + 3 bullets) and an Adaptive Card JSON with KPIs and quick-action buttons;"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_analyze_cash_flow", "rar_sha256": "0ce1e62f3ad9b06568383dfe05ad6795f18cb6b9cbcdbaa957b0a3b01bcc2fdc", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_analyze_cash_flow`. The original RAPP
agent is preserved byte-for-byte in `teams_update_analyze_cash_flow_agent.py` and in the RCI capsule.

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

Analyze cash flow Teams Channel Update — Summarizes cash flow status from Dynamics 365 F&SCM for a legal entity and saves two artifacts: a markdown Teams channel post (2-sentence summary + 3 bullets) and an Adaptive Card JSON with KPIs and quick-action buttons;

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-analyze-cash-flow
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
      "description": "Filename for the saved Adaptive Card JSON, e.g. teams-update-analyze-cash-flow-2026-05-24-card.json.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to analyze, e.g. USMF.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_analyze_cash_flow_agent.py` and embedded as the fenced Python below (sha256 0ce1e62f3ad9b065…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_analyze_cash_flow_agent.py` first:

```bash
python3 teams_update_analyze_cash_flow_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_analyze_cash_flow_agent.py   # or on stdin
python3 teams_update_analyze_cash_flow_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Analyze cash flow Teams Channel Update — Summarizes cash flow status from Dynamics 365 F&SCM for a legal entity and saves two artifacts: a markdown Teams channel post (2-sentence summary + 3 bullets) and an Adaptive Card JSON with KPIs and quick-action buttons;

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-analyze-cash-flow
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_analyze_cash_flow',
    "version": '3.0.3',
    "display_name": 'Analyze cash flow Teams Channel Update',
    "description": 'Summarizes cash flow status from Dynamics 365 F&SCM for a legal entity and saves two artifacts: a markdown Teams channel post (2-sentence summary + 3 bullets) and an Adaptive Card JSON with KPIs and quick-action buttons;',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'order_to_cash', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'verified',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'teams-update-analyze-cash-flow',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-analyze-cash-flow',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'fc6099fca87509a6',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/analyze-sales-performance/analyze-cash-flow'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/teams-update-analyze-cash-flow', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'card_filename': 'Filename for the saved Adaptive Card JSON, e.g. teams-update-analyze-cash-flow-2026-05-24-card.json.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to analyze, e.g. USMF.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Replaces 'check the spreadsheet' Teams pings with a glanceable card the team can act on directly - reducing back-and-forth and decision latency.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, summarize the current state of analyze cash flow. Produce: (a) a Communications-ready Teams channel post (markdown) with a 2-sentence summary and 3 bullet highlights; (b) an Adaptive Card JSON 'teams-update-analyze-cash-flow-2026-05-24-card.json' showing KPIs, status indicators, and quick-action buttons (e.g., 'View detail', 'Open in D365'). Do not post the card on my behalf - save the artifacts for me to review.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-25', 'what_it_does': 'Reads analyze cash flow, produces a Communications-ready Teams post + an Adaptive Card with quick-action buttons.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Summarizes cash flow status from Dynamics 365 F&SCM for a legal entity and saves two artifacts: a markdown Teams channel post (2-sentence summary + 3 bullets) and an Adaptive Card JSON with KPIs and quick-action buttons;', 'example_request': "Draft a Teams channel post and Adaptive Card on cash flow status for USMF from D365 — don't post it, just save the files.", 'inputs': [{'description': 'D365 legal entity to analyze, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Filename for the saved Adaptive Card JSON, e.g. teams-update-analyze-cash-flow-2026-05-24-card.json.', 'name': 'card_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a review-ready Teams channel update on cash flow drafted from D365 ERP data, with an Adaptive Card saved for them to post themselves.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class TeamsUpdateAnalyzeCashFlow(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateAnalyzeCashFlow'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'card_filename': {'description': 'Filename for the saved Adaptive Card JSON, e.g. teams-update-analyze-cash-flow-2026-05-24-card.json.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to analyze, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(TeamsUpdateAnalyzeCashFlow().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
