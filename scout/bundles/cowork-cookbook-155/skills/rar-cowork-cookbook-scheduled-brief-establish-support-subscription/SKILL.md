---
name: "rar-cowork-cookbook-scheduled-brief-establish-support-subscription"
description: "Builds a morning brief on establish support subscription from Dynamics 365 ERP (legal entity USMF): top 5 items by impact, anomalies vs 7-day rolling average, and recommended next actions, then saves a draft email to the"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_establish_support_subscription", "rar_sha256": "39e84ce494bc4940829c9560b8c200df4f550240ec507e5facba474269753715", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
