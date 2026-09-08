---
name: "rar-cowork-cookbook-teams-update-analyze-knowledge-base-usage"
description: "Summarizes knowledge base usage from Dynamics 365 ERP for a legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons; nothing is posted."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_analyze_knowledge_base_usage", "rar_sha256": "55c99b9a8b49dd66772c1e308c84c31b193794fe0a6bd7236e56dbf5d82c7a24", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_analyze_knowledge_base_usage`. The original RAPP
agent is preserved byte-for-byte in `teams_update_analyze_knowledge_base_usage_agent.py` and in the RCI capsule.

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

Analyze knowledge base usage Teams Channel Update — Summarizes knowledge base usage from Dynamics 365 ERP for a legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons; nothing is posted.

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-analyze-knowledge-base-usage
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
      "description": "Output name for the Adaptive Card JSON, e.g. teams-update-analyze-knowledge-base-usage-2026-05-24-card.json.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to report on (e.g. USMF).",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_analyze_knowledge_base_usage_agent.py` and embedded as the fenced Python below (sha256 55c99b9a8b49dd66…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_analyze_knowledge_base_usage_agent.py` first:

```bash
python3 teams_update_analyze_knowledge_base_usage_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_analyze_knowledge_base_usage_agent.py   # or on stdin
python3 teams_update_analyze_knowledge_base_usage_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Analyze knowledge base usage Teams Channel Update — Summarizes knowledge base usage from Dynamics 365 ERP for a legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons; nothing is posted.

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-analyze-knowledge-base-usage
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_analyze_knowledge_base_usage',
    "version": '3.0.3',
    "display_name": 'Analyze knowledge base usage Teams Channel Update',
    "description": 'Summarizes knowledge base usage from Dynamics 365 ERP for a legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons; nothing is posted.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'case_to_resolution', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-analyze-knowledge-base-usage',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-analyze-knowledge-base-usage',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '4b09998f4c5d1f8e',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/analyze-case-performance/analyze-knowledge-base-usage'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/teams-update-analyze-knowledge-base-usage', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'card_filename': 'Output name for the Adaptive Card JSON, e.g. teams-update-analyze-knowledge-base-usage-2026-05-24-card.json.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report on (e.g. USMF).'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Replaces 'check the spreadsheet' Teams pings with a glanceable card the team can act on directly - reducing back-and-forth and decision latency.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, summarize the current state of analyze knowledge base usage. Produce: (a) a Communications-ready Teams channel post (markdown) with a 2-sentence summary and 3 bullet highlights; (b) an Adaptive Card JSON 'teams-update-analyze-knowledge-base-usage-2026-05-24-card.json' showing KPIs, status indicators, and quick-action buttons (e.g., 'View detail', 'Open in D365'). Do not post the card on my behalf - save the artifacts for me to review.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads analyze knowledge base usage, produces a Communications-ready Teams post + an Adaptive Card with quick-action buttons.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Summarizes knowledge base usage from Dynamics 365 ERP for a legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons; nothing is posted.', 'example_request': "Draft a Teams update on knowledge base usage for USMF with an Adaptive Card, but don't post it.", 'inputs': [{'description': 'D365 legal entity to report on (e.g. USMF).', 'name': 'legal_entity'}, {'description': 'Output name for the Adaptive Card JSON, e.g. teams-update-analyze-knowledge-base-usage-2026-05-24-card.json.', 'name': 'card_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need a review-ready Teams channel update plus Adaptive Card on knowledge base usage status from D365 F&SCM, without auto-posting.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class TeamsUpdateAnalyzeKnowledgeBaseUsage(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateAnalyzeKnowledgeBaseUsage'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'card_filename': {'description': 'Output name for the Adaptive Card JSON, e.g. teams-update-analyze-knowledge-base-usage-2026-05-24-card.json.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report on (e.g. USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(TeamsUpdateAnalyzeKnowledgeBaseUsage().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
