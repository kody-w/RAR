---
name: "rar-cowork-cookbook-scheduled-brief-prepare-to-go-live"
description: "Builds a morning brief on go-live readiness from Dynamics 365 F&SCM (legal entity USMF): top 5 items by impact today, anomalies vs the 7-day rolling average, and recommended next actions, then saves a draft email to the"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_prepare_to_go_live", "rar_sha256": "5c3cefff493b1c4cf6890121fe7908424a07b80cddbf3a1a42b6bd979ca4c50f", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
