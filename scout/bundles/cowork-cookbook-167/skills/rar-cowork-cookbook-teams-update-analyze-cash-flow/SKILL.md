---
name: "rar-cowork-cookbook-teams-update-analyze-cash-flow"
description: "Summarizes cash flow status from Dynamics 365 F&SCM for a legal entity and saves two artifacts: a markdown Teams channel post (2-sentence summary + 3 bullets) and an Adaptive Card JSON with KPIs and quick-action buttons;"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_analyze_cash_flow", "rar_sha256": "0ce1e62f3ad9b06568383dfe05ad6795f18cb6b9cbcdbaa957b0a3b01bcc2fdc", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
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
