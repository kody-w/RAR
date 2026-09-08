---
name: "rar-cowork-cookbook-scheduled-brief-conduct-post-sale-follow-up"
description: "Builds a morning brief on post-sale follow-up from Dynamics 365 F&SCM (legal entity USMF) with top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then saves a draft email to the owner plus a"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_conduct_post_sale_follow_up", "rar_sha256": "35cd73950cb80521c99ea4837bb01997e23459c2c1ef8a0a966e5a7a66da9339", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
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
