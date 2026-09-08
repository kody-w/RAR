---
name: "rar-cowork-cookbook-scheduled-brief-define-benefit-offerings"
description: "Builds a morning brief on define benefit offerings from Dynamics 365 ERP (legal entity USMF): top 5 items by impact today, anomalies vs the 7-day rolling average, and recommended next actions; drafts an email to the owne"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_define_benefit_offerings", "rar_sha256": "8984bd3e61505aadc273add4ef77807d822be6eb6ec52eeacd55a065695e5997", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_define_benefit_offerings`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_define_benefit_offerings_agent.py` and in the RCI capsule.

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

Define benefit offerings Scheduled Email Brief — Builds a morning brief on define benefit offerings from Dynamics 365 ERP (legal entity USMF): top 5 items by impact today, anomalies vs the 7-day rolling average, and recommended next actions; drafts an email to the owne

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-define-benefit-offerings
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
      "description": "When to run the brief, e.g. weekday mornings at 7am.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_define_benefit_offerings_agent.py` and embedded as the fenced Python below (sha256 8984bd3e61505aad…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_define_benefit_offerings_agent.py` first:

```bash
python3 scheduled_brief_define_benefit_offerings_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_define_benefit_offerings_agent.py   # or on stdin
python3 scheduled_brief_define_benefit_offerings_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define benefit offerings Scheduled Email Brief — Builds a morning brief on define benefit offerings from Dynamics 365 ERP (legal entity USMF): top 5 items by impact today, anomalies vs the 7-day rolling average, and recommended next actions; drafts an email to the owne

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-define-benefit-offerings
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_define_benefit_offerings',
    "version": '3.0.3',
    "display_name": 'Define benefit offerings Scheduled Email Brief',
    "description": 'Builds a morning brief on define benefit offerings from Dynamics 365 ERP (legal entity USMF): top 5 items by impact today, anomalies vs the 7-day rolling average, and recommended next actions; drafts an email to the owne',
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
        "upstream_slug": 'scheduled-brief-define-benefit-offerings',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-define-benefit-offerings',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '9d34df12d90be9b1',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/manage-compensation-and-benefits/define-benefit-offerings'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/scheduled-brief-define-benefit-offerings', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to query; defaults to USMF.', 'owner': 'Responsible owner who receives the drafted email brief.', 'schedule': 'When to run the brief, e.g. weekday mornings at 7am.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Replaces a daily manual spreadsheet stitch with an automatic brief so owners walk into standup already knowing where define benefit offerings stands.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': 'Using the Dynamics 365 ERP plugin against legal entity USMF, build a short morning brief on define benefit offerings for the responsible owner. Include: (a) top 5 items by impact today, (b) any anomalies vs the 7-day rolling average, (c) recommended next actions. Draft an email to the owner (save to drafts, do not send). Also produce a Communications-ready summary suitable for a Teams channel post. This recipe is a strong candidate for a Cowork scheduled task - schedule for weekday mornings at 7am.', 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads define benefit offerings, computes a short brief, drafts an email, and is a strong candidate for a Cowork scheduled task.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a morning brief on define benefit offerings from Dynamics 365 ERP (legal entity USMF): top 5 items by impact today, anomalies vs the 7-day rolling average, and recommended next actions; drafts an email to the owne', 'example_request': 'Draft my 7am weekday morning brief on define benefit offerings from D365 USMF and save the email to drafts.', 'inputs': [{'description': 'Dynamics 365 legal entity to query; defaults to USMF.', 'name': 'legal_entity'}, {'description': 'Responsible owner who receives the drafted email brief.', 'name': 'owner'}, {'description': 'When to run the brief, e.g. weekday mornings at 7am.', 'name': 'schedule'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a responsible owner wants a daily or weekly define benefit offerings brief drafted from D365 ERP data, ideally scheduled for weekday mornings at 7am.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ScheduledBriefDefineBenefitOfferings(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefDefineBenefitOfferings'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to query; defaults to USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'owner': {'description': 'Responsible owner who receives the drafted email brief.', 'type': 'string'}, 'schedule': {'description': 'When to run the brief, e.g. weekday mornings at 7am.', 'type': 'string'}},
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
    print(ScheduledBriefDefineBenefitOfferings().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
