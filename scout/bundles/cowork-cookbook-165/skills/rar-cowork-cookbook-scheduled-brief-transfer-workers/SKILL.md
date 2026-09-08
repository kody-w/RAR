---
name: "rar-cowork-cookbook-scheduled-brief-transfer-workers"
description: "Builds a morning brief on transfer workers from Dynamics 365 ERP (legal entity USMF): top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then saves an email draft to the owner plus a Teams-r"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_transfer_workers", "rar_sha256": "48905ff13cad7312d25cf923a521c3bd9171c0460cd7ab8b7eab66ed5ce706f8", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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
