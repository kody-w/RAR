---
name: "rar-cowork-cookbook-scheduled-brief-start-production"
description: "Builds a morning brief on start production from Dynamics 365 F&SCM (legal entity USMF): top 5 items by impact today, anomalies vs the 7-day rolling average, and recommended next actions; drafts an email to the responsibl"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_start_production", "rar_sha256": "beb5a91202b36c15ae769aa94edde83d57d62ef62c3c5045240e6d2652bb73b5", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
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
