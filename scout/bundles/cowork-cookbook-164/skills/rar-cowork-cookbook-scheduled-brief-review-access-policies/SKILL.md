---
name: "rar-cowork-cookbook-scheduled-brief-review-access-policies"
description: "Builds a morning brief on review access policies from Dynamics 365 ERP (legal entity USMF): top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, then saves a draft email to the res"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_review_access_policies", "rar_sha256": "3399b983fb8a1cfb24e5a04623262e81d530652b74a3917b989f138197278508", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
