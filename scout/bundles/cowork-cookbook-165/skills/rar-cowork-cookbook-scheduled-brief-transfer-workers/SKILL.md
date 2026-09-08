---
name: "rar-cowork-cookbook-scheduled-brief-transfer-workers"
description: "Builds a morning brief on transfer workers from Dynamics 365 ERP (legal entity USMF): top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then saves an email draft to the owner plus a Teams-r"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_transfer_workers", "rar_sha256": "48905ff13cad7312d25cf923a521c3bd9171c0460cd7ab8b7eab66ed5ce706f8", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_transfer_workers`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_transfer_workers_agent.py` and in the RCI capsule.

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

Transfer workers Scheduled Email Brief — Builds a morning brief on transfer workers from Dynamics 365 ERP (legal entity USMF): top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then saves an email draft to the owner plus a Teams-r

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-transfer-workers
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
      "description": "Person the brief is addressed to and whose draft email is created.",
      "type": "string"
    },
    "schedule": {
      "description": "Optional run cadence, e.g. weekday mornings at 7am.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_transfer_workers_agent.py` and embedded as the fenced Python below (sha256 48905ff13cad7312…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_transfer_workers_agent.py` first:

```bash
python3 scheduled_brief_transfer_workers_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_transfer_workers_agent.py   # or on stdin
python3 scheduled_brief_transfer_workers_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Transfer workers Scheduled Email Brief — Builds a morning brief on transfer workers from Dynamics 365 ERP (legal entity USMF): top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then saves an email draft to the owner plus a Teams-r

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-transfer-workers
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_transfer_workers',
    "version": '3.0.3',
    "display_name": 'Transfer workers Scheduled Email Brief',
    "description": 'Builds a morning brief on transfer workers from Dynamics 365 ERP (legal entity USMF): top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then saves an email draft to the owner plus a Teams-r',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'hire_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-transfer-workers',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-transfer-workers',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '403844c60ae9f2d2',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/manage-performance-and-growth/transfer-workers'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/scheduled-brief-transfer-workers', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to query; defaults to USMF.', 'responsible_owner': 'Person the brief is addressed to and whose draft email is created.', 'schedule': 'Optional run cadence, e.g. weekday mornings at 7am.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Replaces a daily manual spreadsheet stitch with an automatic brief so owners walk into standup already knowing where transfer workers stands.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': 'Using the Dynamics 365 ERP plugin against legal entity USMF, build a short morning brief on transfer workers for the responsible owner. Include: (a) top 5 items by impact today, (b) any anomalies vs the 7-day rolling average, (c) recommended next actions. Draft an email to the owner (save to drafts, do not send). Also produce a Communications-ready summary suitable for a Teams channel post. This recipe is a strong candidate for a Cowork scheduled task - schedule for weekday mornings at 7am.', 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads transfer workers, computes a short brief, drafts an email, and is a strong candidate for a Cowork scheduled task.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a morning brief on transfer workers from Dynamics 365 ERP (legal entity USMF): top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then saves an email draft to the owner plus a Teams-r', 'example_request': 'Give me the 7am transfer workers morning brief for USMF and draft the email to the owner.', 'inputs': [{'description': 'Dynamics 365 legal entity to query; defaults to USMF.', 'name': 'legal_entity'}, {'description': 'Person the brief is addressed to and whose draft email is created.', 'name': 'responsible_owner'}, {'description': 'Optional run cadence, e.g. weekday mornings at 7am.', 'name': 'schedule'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when an owner wants a daily or weekly transfer-worker brief drafted (not sent) as email plus a Teams channel summary from D365 ERP data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ScheduledBriefTransferWorkers(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefTransferWorkers'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to query; defaults to USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'responsible_owner': {'description': 'Person the brief is addressed to and whose draft email is created.', 'type': 'string'}, 'schedule': {'description': 'Optional run cadence, e.g. weekday mornings at 7am.', 'type': 'string'}},
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
    print(ScheduledBriefTransferWorkers().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
