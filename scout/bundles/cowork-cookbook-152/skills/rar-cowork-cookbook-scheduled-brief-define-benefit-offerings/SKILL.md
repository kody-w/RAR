---
name: "rar-cowork-cookbook-scheduled-brief-define-benefit-offerings"
description: "Builds a morning brief on define benefit offerings from Dynamics 365 ERP (legal entity USMF): top 5 items by impact today, anomalies vs the 7-day rolling average, and recommended next actions; drafts an email to the owne"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_define_benefit_offerings", "rar_sha256": "8984bd3e61505aadc273add4ef77807d822be6eb6ec52eeacd55a065695e5997", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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
