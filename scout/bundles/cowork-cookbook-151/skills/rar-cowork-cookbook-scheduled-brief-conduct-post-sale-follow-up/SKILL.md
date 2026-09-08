---
name: "rar-cowork-cookbook-scheduled-brief-conduct-post-sale-follow-up"
description: "Builds a morning brief on post-sale follow-up from Dynamics 365 F&SCM (legal entity USMF) with top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then saves a draft email to the owner plus a"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_conduct_post_sale_follow_up", "rar_sha256": "35cd73950cb80521c99ea4837bb01997e23459c2c1ef8a0a966e5a7a66da9339", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_conduct_post_sale_follow_up`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_conduct_post_sale_follow_up_agent.py` and in the RCI capsule.

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

Conduct post-sale follow-up Scheduled Email Brief — Builds a morning brief on post-sale follow-up from Dynamics 365 F&SCM (legal entity USMF) with top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then saves a draft email to the owner plus a

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-conduct-post-sale-follow-up
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
      "description": "D365 F&SCM legal entity to query; defaults to USMF.",
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
      "description": "Responsible owner who receives the drafted brief email.",
      "type": "string"
    },
    "schedule": {
      "description": "Optional run cadence, e.g. weekday mornings at 7am, for a Cowork scheduled task.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_conduct_post_sale_follow_up_agent.py` and embedded as the fenced Python below (sha256 35cd73950cb80521…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_conduct_post_sale_follow_up_agent.py` first:

```bash
python3 scheduled_brief_conduct_post_sale_follow_up_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_conduct_post_sale_follow_up_agent.py   # or on stdin
python3 scheduled_brief_conduct_post_sale_follow_up_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Conduct post-sale follow-up Scheduled Email Brief — Builds a morning brief on post-sale follow-up from Dynamics 365 F&SCM (legal entity USMF) with top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then saves a draft email to the owner plus a

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-conduct-post-sale-follow-up
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_conduct_post_sale_follow_up',
    "version": '3.0.3',
    "display_name": 'Conduct post-sale follow-up Scheduled Email Brief',
    "description": 'Builds a morning brief on post-sale follow-up from Dynamics 365 F&SCM (legal entity USMF) with top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then saves a draft email to the owner plus a',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'prospect_to_quote', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-conduct-post-sale-follow-up',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-conduct-post-sale-follow-up',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '262448f776287fce',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/estimate-and-quote-sales/conduct-post-sale-follow-up'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/scheduled-brief-conduct-post-sale-follow-up', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 F&SCM legal entity to query; defaults to USMF.', 'owner': 'Responsible owner who receives the drafted brief email.', 'schedule': 'Optional run cadence, e.g. weekday mornings at 7am, for a Cowork scheduled task.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Replaces a daily manual spreadsheet stitch with an automatic brief so owners walk into standup already knowing where conduct post-sale follow-up stands.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': 'Using the Dynamics 365 ERP plugin against legal entity USMF, build a short morning brief on conduct post-sale follow-up for the responsible owner. Include: (a) top 5 items by impact today, (b) any anomalies vs the 7-day rolling average, (c) recommended next actions. Draft an email to the owner (save to drafts, do not send). Also produce a Communications-ready summary suitable for a Teams channel post. This recipe is a strong candidate for a Cowork scheduled task - schedule for weekday mornings at 7am.', 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads conduct post-sale follow-up, computes a short brief, drafts an email, and is a strong candidate for a Cowork scheduled task.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a morning brief on post-sale follow-up from Dynamics 365 F&SCM (legal entity USMF) with top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then saves a draft email to the owner plus a', 'example_request': 'Draft my post-sale follow-up morning brief from D365 USMF for the owner, plus a Teams summary.', 'inputs': [{'description': 'D365 F&SCM legal entity to query; defaults to USMF.', 'name': 'legal_entity'}, {'description': 'Responsible owner who receives the drafted brief email.', 'name': 'owner'}, {'description': 'Optional run cadence, e.g. weekday mornings at 7am, for a Cowork scheduled task.', 'name': 'schedule'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a daily or weekly post-sale follow-up brief for the responsible owner from D365 ERP data, as a draft email and Teams-channel summary.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ScheduledBriefConductPostSaleFollowUp(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefConductPostSaleFollowUp'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 F&SCM legal entity to query; defaults to USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'owner': {'description': 'Responsible owner who receives the drafted brief email.', 'type': 'string'}, 'schedule': {'description': 'Optional run cadence, e.g. weekday mornings at 7am, for a Cowork scheduled task.', 'type': 'string'}},
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
    print(ScheduledBriefConductPostSaleFollowUp().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
