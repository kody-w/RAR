---
name: "rar-cowork-cookbook-teams-update-analyze-knowledge-base-usage"
description: "Summarizes knowledge base usage from Dynamics 365 ERP for a legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons; nothing is posted."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_analyze_knowledge_base_usage", "rar_sha256": "55c99b9a8b49dd66772c1e308c84c31b193794fe0a6bd7236e56dbf5d82c7a24", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
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
