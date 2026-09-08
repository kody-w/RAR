---
name: "rar-cowork-cookbook-scheduled-brief-analyze-project-metrics"
description: "Builds a morning brief on project metrics from Dynamics 365 ERP (legal entity USMF): top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, then drafts an email to the owner (saved t"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_analyze_project_metrics", "rar_sha256": "b0100081ecabdda515a46b7cc7a5ee22aab6be7367262b931fd5c71f288c6dd7", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
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
