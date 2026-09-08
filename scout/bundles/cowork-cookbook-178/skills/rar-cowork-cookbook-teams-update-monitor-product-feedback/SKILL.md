---
name: "rar-cowork-cookbook-teams-update-monitor-product-feedback"
description: "Summarizes monitor product feedback status from the Dynamics 365 ERP plugin for a given legal entity and saves a markdown Teams channel post plus an Adaptive Card JSON file for review; it does not post anything."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_monitor_product_feedback", "rar_sha256": "e29eb2264e1e1e93cbef99c3f6bdab246647d2d003e552520293bfe39f7a6464", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_monitor_product_feedback`. The original RAPP
agent is preserved byte-for-byte in `teams_update_monitor_product_feedback_agent.py` and in the RCI capsule.

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

Monitor product feedback Teams Channel Update — Summarizes monitor product feedback status from the Dynamics 365 ERP plugin for a given legal entity and saves a markdown Teams channel post plus an Adaptive Card JSON file for review; it does not post anything.

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-monitor-product-feedback
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
      "description": "Output name for the Adaptive Card JSON, e.g. teams-update-monitor-product-feedback-2026-05-24-card.json.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_monitor_product_feedback_agent.py` and embedded as the fenced Python below (sha256 e29eb2264e1e1e93…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_monitor_product_feedback_agent.py` first:

```bash
python3 teams_update_monitor_product_feedback_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_monitor_product_feedback_agent.py   # or on stdin
python3 teams_update_monitor_product_feedback_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Monitor product feedback Teams Channel Update — Summarizes monitor product feedback status from the Dynamics 365 ERP plugin for a given legal entity and saves a markdown Teams channel post plus an Adaptive Card JSON file for review; it does not post anything.

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-monitor-product-feedback
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_monitor_product_feedback',
    "version": '3.0.3',
    "display_name": 'Monitor product feedback Teams Channel Update',
    "description": 'Summarizes monitor product feedback status from the Dynamics 365 ERP plugin for a given legal entity and saves a markdown Teams channel post plus an Adaptive Card JSON file for review; it does not post anything.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'design_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-monitor-product-feedback',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-monitor-product-feedback',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '46dea531959aaecc',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['design-to-retire'], 'process_tags': ['design-to-retire/analyze-product-performance/monitor-product-feedback'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'design-to-retire/teams-update-monitor-product-feedback', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'card_filename': 'Output name for the Adaptive Card JSON, e.g. teams-update-monitor-product-feedback-2026-05-24-card.json.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to summarize, e.g. USMF.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Replaces 'check the spreadsheet' Teams pings with a glanceable card the team can act on directly - reducing back-and-forth and decision latency.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, summarize the current state of monitor product feedback. Produce: (a) a Communications-ready Teams channel post (markdown) with a 2-sentence summary and 3 bullet highlights; (b) an Adaptive Card JSON 'teams-update-monitor-product-feedback-2026-05-24-card.json' showing KPIs, status indicators, and quick-action buttons (e.g., 'View detail', 'Open in D365'). Do not post the card on my behalf - save the artifacts for me to review.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads monitor product feedback, produces a Communications-ready Teams post + an Adaptive Card with quick-action buttons.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Summarizes monitor product feedback status from the Dynamics 365 ERP plugin for a given legal entity and saves a markdown Teams channel post plus an Adaptive Card JSON file for review; it does not post anything.', 'example_request': "Draft a Teams update on monitor product feedback for USMF with an Adaptive Card — don't post it, just save the files.", 'inputs': [{'description': 'D365 legal entity to summarize, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Output name for the Adaptive Card JSON, e.g. teams-update-monitor-product-feedback-2026-05-24-card.json.', 'name': 'card_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need a ready-to-review Teams channel update and Adaptive Card on monitor product feedback status pulled from Dynamics 365 F&SCM.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class TeamsUpdateMonitorProductFeedback(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateMonitorProductFeedback'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'card_filename': {'description': 'Output name for the Adaptive Card JSON, e.g. teams-update-monitor-product-feedback-2026-05-24-card.json.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to summarize, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(TeamsUpdateMonitorProductFeedback().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
