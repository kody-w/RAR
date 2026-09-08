---
name: "rar-cowork-cookbook-scheduled-brief-prepare-to-go-live"
description: "Builds a morning brief on go-live readiness from Dynamics 365 F&SCM (legal entity USMF): top 5 items by impact today, anomalies vs the 7-day rolling average, and recommended next actions, then saves a draft email to the"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_prepare_to_go_live", "rar_sha256": "5c3cefff493b1c4cf6890121fe7908424a07b80cddbf3a1a42b6bd979ca4c50f", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_prepare_to_go_live`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_prepare_to_go_live_agent.py` and in the RCI capsule.

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

Prepare to go live Scheduled Email Brief — Builds a morning brief on go-live readiness from Dynamics 365 F&SCM (legal entity USMF): top 5 items by impact today, anomalies vs the 7-day rolling average, and recommended next actions, then saves a draft email to the

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-prepare-to-go-live
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
      "description": "Dynamics 365 legal entity to query, e.g. USMF.",
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
      "description": "When to run, e.g. weekday mornings at 7am.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_prepare_to_go_live_agent.py` and embedded as the fenced Python below (sha256 5c3cefff493b1c4c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_prepare_to_go_live_agent.py` first:

```bash
python3 scheduled_brief_prepare_to_go_live_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_prepare_to_go_live_agent.py   # or on stdin
python3 scheduled_brief_prepare_to_go_live_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Prepare to go live Scheduled Email Brief — Builds a morning brief on go-live readiness from Dynamics 365 F&SCM (legal entity USMF): top 5 items by impact today, anomalies vs the 7-day rolling average, and recommended next actions, then saves a draft email to the

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-prepare-to-go-live
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_prepare_to_go_live',
    "version": '3.0.3',
    "display_name": 'Prepare to go live Scheduled Email Brief',
    "description": 'Builds a morning brief on go-live readiness from Dynamics 365 F&SCM (legal entity USMF): top 5 items by impact today, anomalies vs the 7-day rolling average, and recommended next actions, then saves a draft email to the',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-prepare-to-go-live',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-prepare-to-go-live',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'c3a2f4d5a9eb2a77',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/implement-solutions/prepare-to-go-live'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/scheduled-brief-prepare-to-go-live', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to query, e.g. USMF.', 'owner': 'Responsible owner who receives the drafted email brief.', 'schedule': 'When to run, e.g. weekday mornings at 7am.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Replaces a daily manual spreadsheet stitch with an automatic brief so owners walk into standup already knowing where prepare to go live stands.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': 'Using the Dynamics 365 ERP plugin against legal entity USMF, build a short morning brief on prepare to go live for the responsible owner. Include: (a) top 5 items by impact today, (b) any anomalies vs the 7-day rolling average, (c) recommended next actions. Draft an email to the owner (save to drafts, do not send). Also produce a Communications-ready summary suitable for a Teams channel post. This recipe is a strong candidate for a Cowork scheduled task - schedule for weekday mornings at 7am.', 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads prepare to go live, computes a short brief, drafts an email, and is a strong candidate for a Cowork scheduled task.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a morning brief on go-live readiness from Dynamics 365 F&SCM (legal entity USMF): top 5 items by impact today, anomalies vs the 7-day rolling average, and recommended next actions, then saves a draft email to the', 'example_request': 'Draft my go-live morning brief for USMF and email it to the owner as a draft, plus a Teams summary.', 'inputs': [{'description': 'Dynamics 365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Responsible owner who receives the drafted email brief.', 'name': 'owner'}, {'description': 'When to run, e.g. weekday mornings at 7am.', 'name': 'schedule'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a responsible owner wants a daily or weekly go-live readiness brief drafted as an email (not sent) plus a Teams channel summary.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ScheduledBriefPrepareToGoLive(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefPrepareToGoLive'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'owner': {'description': 'Responsible owner who receives the drafted email brief.', 'type': 'string'}, 'schedule': {'description': 'When to run, e.g. weekday mornings at 7am.', 'type': 'string'}},
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
    print(ScheduledBriefPrepareToGoLive().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
