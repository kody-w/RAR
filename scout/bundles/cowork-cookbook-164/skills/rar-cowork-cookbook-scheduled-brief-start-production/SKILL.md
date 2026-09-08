---
name: "rar-cowork-cookbook-scheduled-brief-start-production"
description: "Builds a morning brief on start production from Dynamics 365 F&SCM (legal entity USMF): top 5 items by impact today, anomalies vs the 7-day rolling average, and recommended next actions; drafts an email to the responsibl"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_start_production", "rar_sha256": "beb5a91202b36c15ae769aa94edde83d57d62ef62c3c5045240e6d2652bb73b5", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_start_production`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_start_production_agent.py` and in the RCI capsule.

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

Start production Scheduled Email Brief — Builds a morning brief on start production from Dynamics 365 F&SCM (legal entity USMF): top 5 items by impact today, anomalies vs the 7-day rolling average, and recommended next actions; drafts an email to the responsibl

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-start-production
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
      "description": "Dynamics 365 legal entity to query; defaults to USMF.",
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
    "responsible_owner": {
      "description": "Person the brief is addressed to and the email draft is created for.",
      "type": "string"
    },
    "schedule": {
      "description": "Optional cadence for the scheduled task, e.g. weekday mornings at 7am.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_start_production_agent.py` and embedded as the fenced Python below (sha256 beb5a91202b36c15…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_start_production_agent.py` first:

```bash
python3 scheduled_brief_start_production_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_start_production_agent.py   # or on stdin
python3 scheduled_brief_start_production_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Start production Scheduled Email Brief — Builds a morning brief on start production from Dynamics 365 F&SCM (legal entity USMF): top 5 items by impact today, anomalies vs the 7-day rolling average, and recommended next actions; drafts an email to the responsibl

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-start-production
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_start_production',
    "version": '3.0.3',
    "display_name": 'Start production Scheduled Email Brief',
    "description": 'Builds a morning brief on start production from Dynamics 365 F&SCM (legal entity USMF): top 5 items by impact today, anomalies vs the 7-day rolling average, and recommended next actions; drafts an email to the responsibl',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'plan_to_produce', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-start-production',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-start-production',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '71185b7ace410841',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['plan-to-produce'], 'process_tags': ['plan-to-produce/run-production-operations/start-production'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'plan-to-produce/scheduled-brief-start-production', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to query; defaults to USMF.', 'responsible_owner': 'Person the brief is addressed to and the email draft is created for.', 'schedule': 'Optional cadence for the scheduled task, e.g. weekday mornings at 7am.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Replaces a daily manual spreadsheet stitch with an automatic brief so owners walk into standup already knowing where start production stands.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': 'Using the Dynamics 365 ERP plugin against legal entity USMF, build a short morning brief on start production for the responsible owner. Include: (a) top 5 items by impact today, (b) any anomalies vs the 7-day rolling average, (c) recommended next actions. Draft an email to the owner (save to drafts, do not send). Also produce a Communications-ready summary suitable for a Teams channel post. This recipe is a strong candidate for a Cowork scheduled task - schedule for weekday mornings at 7am.', 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads start production, computes a short brief, drafts an email, and is a strong candidate for a Cowork scheduled task.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a morning brief on start production from Dynamics 365 F&SCM (legal entity USMF): top 5 items by impact today, anomalies vs the 7-day rolling average, and recommended next actions; drafts an email to the responsibl', 'example_request': 'Send me the start production morning brief for USMF and draft it to the owner.', 'inputs': [{'description': 'Dynamics 365 legal entity to query; defaults to USMF.', 'name': 'legal_entity'}, {'description': 'Person the brief is addressed to and the email draft is created for.', 'name': 'responsible_owner'}, {'description': 'Optional cadence for the scheduled task, e.g. weekday mornings at 7am.', 'name': 'schedule'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when someone wants a daily or weekly start-production morning brief for the responsible owner, as an unsent email draft plus a Teams channel summary.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ScheduledBriefStartProduction(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefStartProduction'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to query; defaults to USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'responsible_owner': {'description': 'Person the brief is addressed to and the email draft is created for.', 'type': 'string'}, 'schedule': {'description': 'Optional cadence for the scheduled task, e.g. weekday mornings at 7am.', 'type': 'string'}},
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
    print(ScheduledBriefStartProduction().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
