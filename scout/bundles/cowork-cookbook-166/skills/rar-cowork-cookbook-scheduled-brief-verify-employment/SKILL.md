---
name: "rar-cowork-cookbook-scheduled-brief-verify-employment"
description: "Builds a morning brief on verify employment from Dynamics 365 ERP data for legal entity USMF, returning top 5 items by impact, anomalies vs the 7-day rolling average, recommended next actions, a saved email draft to the"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_verify_employment", "rar_sha256": "3474d9d5a7ab851df5fd1dfcf910f5c8367319d5cff800ea786aa58ee539bb87", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_verify_employment`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_verify_employment_agent.py` and in the RCI capsule.

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

Verify employment Scheduled Email Brief — Builds a morning brief on verify employment from Dynamics 365 ERP data for legal entity USMF, returning top 5 items by impact, anomalies vs the 7-day rolling average, recommended next actions, a saved email draft to the

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-verify-employment
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_verify_employment_agent.py` and embedded as the fenced Python below (sha256 3474d9d5a7ab851d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_verify_employment_agent.py` first:

```bash
python3 scheduled_brief_verify_employment_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_verify_employment_agent.py   # or on stdin
python3 scheduled_brief_verify_employment_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Verify employment Scheduled Email Brief — Builds a morning brief on verify employment from Dynamics 365 ERP data for legal entity USMF, returning top 5 items by impact, anomalies vs the 7-day rolling average, recommended next actions, a saved email draft to the

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-verify-employment
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_verify_employment',
    "version": '3.0.3',
    "display_name": 'Verify employment Scheduled Email Brief',
    "description": 'Builds a morning brief on verify employment from Dynamics 365 ERP data for legal entity USMF, returning top 5 items by impact, anomalies vs the 7-day rolling average, recommended next actions, a saved email draft to the',
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
        "upstream_slug": 'scheduled-brief-verify-employment',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-verify-employment',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'ee25802ce90e8fc6',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/manage-workplace-compliance/verify-employment'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/scheduled-brief-verify-employment', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to query; defaults to USMF.', 'owner': 'Responsible owner who receives the drafted email brief.', 'schedule': 'When to run, e.g. weekday mornings at 7am, daily or weekly.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Replaces a daily manual spreadsheet stitch with an automatic brief so owners walk into standup already knowing where verify employment stands.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': 'Using the Dynamics 365 ERP plugin against legal entity USMF, build a short morning brief on verify employment for the responsible owner. Include: (a) top 5 items by impact today, (b) any anomalies vs the 7-day rolling average, (c) recommended next actions. Draft an email to the owner (save to drafts, do not send). Also produce a Communications-ready summary suitable for a Teams channel post. This recipe is a strong candidate for a Cowork scheduled task - schedule for weekday mornings at 7am.', 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads verify employment, computes a short brief, drafts an email, and is a strong candidate for a Cowork scheduled task.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a morning brief on verify employment from Dynamics 365 ERP data for legal entity USMF, returning top 5 items by impact, anomalies vs the 7-day rolling average, recommended next actions, a saved email draft to the', 'example_request': 'Give me the verify employment morning brief for USMF and draft it to the owner.', 'inputs': [{'description': 'Dynamics 365 legal entity to query; defaults to USMF.', 'name': 'legal_entity'}, {'description': 'Responsible owner who receives the drafted email brief.', 'name': 'owner'}, {'description': 'When to run, e.g. weekday mornings at 7am, daily or weekly.', 'name': 'schedule'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when someone wants a daily or weekly verify-employment morning brief for the responsible owner, drafted as an email and a Teams channel post.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ScheduledBriefVerifyEmployment(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefVerifyEmployment'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to query; defaults to USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'owner': {'description': 'Responsible owner who receives the drafted email brief.', 'type': 'string'}, 'schedule': {'description': 'When to run, e.g. weekday mornings at 7am, daily or weekly.', 'type': 'string'}},
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
    print(ScheduledBriefVerifyEmployment().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
