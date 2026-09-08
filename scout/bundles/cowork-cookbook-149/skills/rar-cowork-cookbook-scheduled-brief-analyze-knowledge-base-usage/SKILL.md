---
name: "rar-cowork-cookbook-scheduled-brief-analyze-knowledge-base-usage"
description: "Builds a morning brief on knowledge base usage from Dynamics 365 ERP data for a legal entity, returning top 5 items by impact, anomalies vs the 7-day rolling average, recommended actions, a saved email draft to the owner"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_analyze_knowledge_base_usage", "rar_sha256": "bfff7c2c76409b3adff9f9c9a9cba83e8fe25f208b5f33ea4387087f189b8f50", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_analyze_knowledge_base_usage`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_analyze_knowledge_base_usage_agent.py` and in the RCI capsule.

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

Analyze knowledge base usage Scheduled Email Brief — Builds a morning brief on knowledge base usage from Dynamics 365 ERP data for a legal entity, returning top 5 items by impact, anomalies vs the 7-day rolling average, recommended actions, a saved email draft to the owner

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-analyze-knowledge-base-usage
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
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "Dynamics 365 F&SCM legal entity to query, e.g. USMF.",
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
    "owner": {
      "description": "Responsible owner who receives the drafted email brief.",
      "type": "string"
    },
    "schedule": {
      "description": "When the brief should run, e.g. weekday mornings at 7am.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_analyze_knowledge_base_usage_agent.py` and embedded as the fenced Python below (sha256 bfff7c2c76409b3a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_analyze_knowledge_base_usage_agent.py` first:

```bash
python3 scheduled_brief_analyze_knowledge_base_usage_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_analyze_knowledge_base_usage_agent.py   # or on stdin
python3 scheduled_brief_analyze_knowledge_base_usage_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Analyze knowledge base usage Scheduled Email Brief — Builds a morning brief on knowledge base usage from Dynamics 365 ERP data for a legal entity, returning top 5 items by impact, anomalies vs the 7-day rolling average, recommended actions, a saved email draft to the owner

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-analyze-knowledge-base-usage
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_analyze_knowledge_base_usage',
    "version": '3.0.3',
    "display_name": 'Analyze knowledge base usage Scheduled Email Brief',
    "description": 'Builds a morning brief on knowledge base usage from Dynamics 365 ERP data for a legal entity, returning top 5 items by impact, anomalies vs the 7-day rolling average, recommended actions, a saved email draft to the owner',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'case_to_resolution', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-analyze-knowledge-base-usage',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-analyze-knowledge-base-usage',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '6e69a274e2171abf',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/analyze-case-performance/analyze-knowledge-base-usage'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/scheduled-brief-analyze-knowledge-base-usage', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 F&SCM legal entity to query, e.g. USMF.', 'owner': 'Responsible owner who receives the drafted email brief.', 'schedule': 'When the brief should run, e.g. weekday mornings at 7am.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Replaces a daily manual spreadsheet stitch with an automatic brief so owners walk into standup already knowing where analyze knowledge base usage stands.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': 'Using the Dynamics 365 ERP plugin against legal entity USMF, build a short morning brief on analyze knowledge base usage for the responsible owner. Include: (a) top 5 items by impact today, (b) any anomalies vs the 7-day rolling average, (c) recommended next actions. Draft an email to the owner (save to drafts, do not send). Also produce a Communications-ready summary suitable for a Teams channel post. This recipe is a strong candidate for a Cowork scheduled task - schedule for weekday mornings at 7am.', 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads analyze knowledge base usage, computes a short brief, drafts an email, and is a strong candidate for a Cowork scheduled task.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a morning brief on knowledge base usage from Dynamics 365 ERP data for a legal entity, returning top 5 items by impact, anomalies vs the 7-day rolling average, recommended actions, a saved email draft to the owner', 'example_request': 'Give me the 7am weekday knowledge base usage brief for USMF and draft it to the owner.', 'inputs': [{'description': 'Dynamics 365 F&SCM legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Responsible owner who receives the drafted email brief.', 'name': 'owner'}, {'description': 'When the brief should run, e.g. weekday mornings at 7am.', 'name': 'schedule'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a daily or weekly scheduled brief on knowledge base usage is needed for the responsible owner, drafted (not sent) as email plus a Teams post summary.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ScheduledBriefAnalyzeKnowledgeBaseUsage(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefAnalyzeKnowledgeBaseUsage'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 F&SCM legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'owner': {'description': 'Responsible owner who receives the drafted email brief.', 'type': 'string'}, 'schedule': {'description': 'When the brief should run, e.g. weekday mornings at 7am.', 'type': 'string'}},
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
    print(ScheduledBriefAnalyzeKnowledgeBaseUsage().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
