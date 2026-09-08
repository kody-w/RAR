---
name: "rar-cowork-cookbook-scheduled-brief-verify-employment"
description: "Builds a morning brief on verify employment from Dynamics 365 ERP data for legal entity USMF, returning top 5 items by impact, anomalies vs the 7-day rolling average, recommended next actions, a saved email draft to the"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_verify_employment", "rar_sha256": "3474d9d5a7ab851df5fd1dfcf910f5c8367319d5cff800ea786aa58ee539bb87", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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
