---
name: "rar-cowork-cookbook-scheduled-brief-review-access-policies"
description: "Builds a morning brief on review access policies from Dynamics 365 ERP (legal entity USMF): top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, then saves a draft email to the res"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_review_access_policies", "rar_sha256": "3399b983fb8a1cfb24e5a04623262e81d530652b74a3917b989f138197278508", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_review_access_policies`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_review_access_policies_agent.py` and in the RCI capsule.

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

Review access policies Scheduled Email Brief — Builds a morning brief on review access policies from Dynamics 365 ERP (legal entity USMF): top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, then saves a draft email to the res

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-review-access-policies
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
      "description": "Dynamics 365 legal entity to query; the recipe uses USMF.",
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
      "description": "Optional cadence for the scheduled task; recipe suggests weekday mornings at 7am.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_review_access_policies_agent.py` and embedded as the fenced Python below (sha256 3399b983fb8a1cfb…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_review_access_policies_agent.py` first:

```bash
python3 scheduled_brief_review_access_policies_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_review_access_policies_agent.py   # or on stdin
python3 scheduled_brief_review_access_policies_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Review access policies Scheduled Email Brief — Builds a morning brief on review access policies from Dynamics 365 ERP (legal entity USMF): top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, then saves a draft email to the res

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-review-access-policies
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_review_access_policies',
    "version": '3.0.3',
    "display_name": 'Review access policies Scheduled Email Brief',
    "description": 'Builds a morning brief on review access policies from Dynamics 365 ERP (legal entity USMF): top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, then saves a draft email to the res',
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
        "upstream_slug": 'scheduled-brief-review-access-policies',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-review-access-policies',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '55c6d1f2c1415f56',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-system-access-and-security/review-access-policies'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/scheduled-brief-review-access-policies', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to query; the recipe uses USMF.', 'owner': 'Responsible owner who receives the drafted email brief.', 'schedule': 'Optional cadence for the scheduled task; recipe suggests weekday mornings at 7am.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Replaces a daily manual spreadsheet stitch with an automatic brief so owners walk into standup already knowing where review access policies stands.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': 'Using the Dynamics 365 ERP plugin against legal entity USMF, build a short morning brief on review access policies for the responsible owner. Include: (a) top 5 items by impact today, (b) any anomalies vs the 7-day rolling average, (c) recommended next actions. Draft an email to the owner (save to drafts, do not send). Also produce a Communications-ready summary suitable for a Teams channel post. This recipe is a strong candidate for a Cowork scheduled task - schedule for weekday mornings at 7am.', 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads review access policies, computes a short brief, drafts an email, and is a strong candidate for a Cowork scheduled task.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a morning brief on review access policies from Dynamics 365 ERP (legal entity USMF): top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, then saves a draft email to the res', 'example_request': 'Give me the review access policies morning brief for USMF and draft the email to the owner.', 'inputs': [{'description': 'Dynamics 365 legal entity to query; the recipe uses USMF.', 'name': 'legal_entity'}, {'description': 'Responsible owner who receives the drafted email brief.', 'name': 'owner'}, {'description': 'Optional cadence for the scheduled task; recipe suggests weekday mornings at 7am.', 'name': 'schedule'}], 'model': 'claude-opus-5', 'when_to_use': 'Use for a recurring or one-off review-access-policy brief for the responsible owner, with a drafted (unsent) email and a Teams channel summary.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ScheduledBriefReviewAccessPolicies(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefReviewAccessPolicies'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to query; the recipe uses USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'owner': {'description': 'Responsible owner who receives the drafted email brief.', 'type': 'string'}, 'schedule': {'description': 'Optional cadence for the scheduled task; recipe suggests weekday mornings at 7am.', 'type': 'string'}},
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
    print(ScheduledBriefReviewAccessPolicies().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
