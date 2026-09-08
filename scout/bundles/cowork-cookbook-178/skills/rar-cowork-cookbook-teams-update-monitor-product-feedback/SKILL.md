---
name: "rar-cowork-cookbook-teams-update-monitor-product-feedback"
description: "Summarizes monitor product feedback status from the Dynamics 365 ERP plugin for a given legal entity and saves a markdown Teams channel post plus an Adaptive Card JSON file for review; it does not post anything."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_monitor_product_feedback", "rar_sha256": "e29eb2264e1e1e93cbef99c3f6bdab246647d2d003e552520293bfe39f7a6464", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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
