---
name: "rar-cowork-cookbook-scheduled-brief-analyze-project-metrics"
description: "Builds a morning brief on project metrics from Dynamics 365 ERP (legal entity USMF): top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, then drafts an email to the owner (saved t"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_analyze_project_metrics", "rar_sha256": "b0100081ecabdda515a46b7cc7a5ee22aab6be7367262b931fd5c71f288c6dd7", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_analyze_project_metrics`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_analyze_project_metrics_agent.py` and in the RCI capsule.

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

Analyze project metrics Scheduled Email Brief — Builds a morning brief on project metrics from Dynamics 365 ERP (legal entity USMF): top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, then drafts an email to the owner (saved t

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-analyze-project-metrics
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
      "description": "Dynamics 365 F&SCM legal entity to query; defaults to USMF.",
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
      "description": "When to run, e.g. weekday mornings at 7am, daily or weekly.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_analyze_project_metrics_agent.py` and embedded as the fenced Python below (sha256 b0100081ecabdda5…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_analyze_project_metrics_agent.py` first:

```bash
python3 scheduled_brief_analyze_project_metrics_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_analyze_project_metrics_agent.py   # or on stdin
python3 scheduled_brief_analyze_project_metrics_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Analyze project metrics Scheduled Email Brief — Builds a morning brief on project metrics from Dynamics 365 ERP (legal entity USMF): top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, then drafts an email to the owner (saved t

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-analyze-project-metrics
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_analyze_project_metrics',
    "version": '3.0.3',
    "display_name": 'Analyze project metrics Scheduled Email Brief',
    "description": 'Builds a morning brief on project metrics from Dynamics 365 ERP (legal entity USMF): top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, then drafts an email to the owner (saved t',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'project_to_profit', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-analyze-project-metrics',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-analyze-project-metrics',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '066528177bc59c4d',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/analyze-project-performance/analyze-project-metrics'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/scheduled-brief-analyze-project-metrics', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 F&SCM legal entity to query; defaults to USMF.', 'owner': 'Responsible owner who receives the drafted email brief.', 'schedule': 'When to run, e.g. weekday mornings at 7am, daily or weekly.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Replaces a daily manual spreadsheet stitch with an automatic brief so owners walk into standup already knowing where analyze project metrics stands.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': 'Using the Dynamics 365 ERP plugin against legal entity USMF, build a short morning brief on analyze project metrics for the responsible owner. Include: (a) top 5 items by impact today, (b) any anomalies vs the 7-day rolling average, (c) recommended next actions. Draft an email to the owner (save to drafts, do not send). Also produce a Communications-ready summary suitable for a Teams channel post. This recipe is a strong candidate for a Cowork scheduled task - schedule for weekday mornings at 7am.', 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads analyze project metrics, computes a short brief, drafts an email, and is a strong candidate for a Cowork scheduled task.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a morning brief on project metrics from Dynamics 365 ERP (legal entity USMF): top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, then drafts an email to the owner (saved t', 'example_request': 'Give me the 7am project metrics morning brief from USMF and draft the email to the owner.', 'inputs': [{'description': 'Dynamics 365 F&SCM legal entity to query; defaults to USMF.', 'name': 'legal_entity'}, {'description': 'Responsible owner who receives the drafted email brief.', 'name': 'owner'}, {'description': 'When to run, e.g. weekday mornings at 7am, daily or weekly.', 'name': 'schedule'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a daily or weekly scheduled project-metrics brief for the responsible owner, drafted as an email and a Teams channel post.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ScheduledBriefAnalyzeProjectMetrics(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefAnalyzeProjectMetrics'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 F&SCM legal entity to query; defaults to USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'owner': {'description': 'Responsible owner who receives the drafted email brief.', 'type': 'string'}, 'schedule': {'description': 'When to run, e.g. weekday mornings at 7am, daily or weekly.', 'type': 'string'}},
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
    print(ScheduledBriefAnalyzeProjectMetrics().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
