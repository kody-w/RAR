---
name: "rar-cowork-cookbook-scheduled-brief-establish-support-subscription"
description: "Builds a morning brief on establish support subscription from Dynamics 365 ERP (legal entity USMF): top 5 items by impact, anomalies vs 7-day rolling average, and recommended next actions, then saves a draft email to the"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_establish_support_subscription", "rar_sha256": "39e84ce494bc4940829c9560b8c200df4f550240ec507e5facba474269753715", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_establish_support_subscription`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_establish_support_subscription_agent.py` and in the RCI capsule.

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

Establish support subscription Scheduled Email Brief — Builds a morning brief on establish support subscription from Dynamics 365 ERP (legal entity USMF): top 5 items by impact, anomalies vs 7-day rolling average, and recommended next actions, then saves a draft email to the

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-establish-support-subscription
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
      "description": "Optional cadence for the brief, e.g. weekday mornings at 7am.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_establish_support_subscription_agent.py` and embedded as the fenced Python below (sha256 39e84ce494bc4940…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_establish_support_subscription_agent.py` first:

```bash
python3 scheduled_brief_establish_support_subscription_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_establish_support_subscription_agent.py   # or on stdin
python3 scheduled_brief_establish_support_subscription_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Establish support subscription Scheduled Email Brief — Builds a morning brief on establish support subscription from Dynamics 365 ERP (legal entity USMF): top 5 items by impact, anomalies vs 7-day rolling average, and recommended next actions, then saves a draft email to the

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-establish-support-subscription
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_establish_support_subscription',
    "version": '3.0.3',
    "display_name": 'Establish support subscription Scheduled Email Brief',
    "description": 'Builds a morning brief on establish support subscription from Dynamics 365 ERP (legal entity USMF): top 5 items by impact, anomalies vs 7-day rolling average, and recommended next actions, then saves a draft email to the',
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
        "upstream_slug": 'scheduled-brief-establish-support-subscription',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-establish-support-subscription',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '1cd5bd8abc8cadef',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/support-systems/establish-support-subscription'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/scheduled-brief-establish-support-subscription', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to query; defaults to USMF.', 'owner': 'Responsible owner who receives the drafted email brief.', 'schedule': 'Optional cadence for the brief, e.g. weekday mornings at 7am.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Replaces a daily manual spreadsheet stitch with an automatic brief so owners walk into standup already knowing where establish support subscription stands.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': 'Using the Dynamics 365 ERP plugin against legal entity USMF, build a short morning brief on establish support subscription for the responsible owner. Include: (a) top 5 items by impact today, (b) any anomalies vs the 7-day rolling average, (c) recommended next actions. Draft an email to the owner (save to drafts, do not send). Also produce a Communications-ready summary suitable for a Teams channel post. This recipe is a strong candidate for a Cowork scheduled task - schedule for weekday mornings at 7am.', 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads establish support subscription, computes a short brief, drafts an email, and is a strong candidate for a Cowork scheduled task.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a morning brief on establish support subscription from Dynamics 365 ERP (legal entity USMF): top 5 items by impact, anomalies vs 7-day rolling average, and recommended next actions, then saves a draft email to the', 'example_request': 'Draft my 7am brief on establish support subscription for USMF and email the owner.', 'inputs': [{'description': 'Dynamics 365 legal entity to query; defaults to USMF.', 'name': 'legal_entity'}, {'description': 'Responsible owner who receives the drafted email brief.', 'name': 'owner'}, {'description': 'Optional cadence for the brief, e.g. weekday mornings at 7am.', 'name': 'schedule'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when someone wants a daily or weekly establish-support-subscription brief for the responsible owner, drafted as email and a Teams channel post.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ScheduledBriefEstablishSupportSubscription(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefEstablishSupportSubscription'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to query; defaults to USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'owner': {'description': 'Responsible owner who receives the drafted email brief.', 'type': 'string'}, 'schedule': {'description': 'Optional cadence for the brief, e.g. weekday mornings at 7am.', 'type': 'string'}},
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
    print(ScheduledBriefEstablishSupportSubscription().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
