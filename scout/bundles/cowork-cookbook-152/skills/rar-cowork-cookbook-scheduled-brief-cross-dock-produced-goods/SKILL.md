---
name: "rar-cowork-cookbook-scheduled-brief-cross-dock-produced-goods"
description: "Builds a cross dock produced goods morning brief from Dynamics 365 F&SCM (legal entity USMF): top 5 items by impact, anomalies vs 7-day rolling average, next actions, plus a saved email draft and Teams-ready summary."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_cross_dock_produced_goods", "rar_sha256": "c70667639c1b93286764db5a1d9f2af4a3fb2b5923ce3c5e65c43a4709669c50", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_cross_dock_produced_goods`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_cross_dock_produced_goods_agent.py` and in the RCI capsule.

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

Cross dock produced goods Scheduled Email Brief — Builds a cross dock produced goods morning brief from Dynamics 365 F&SCM (legal entity USMF): top 5 items by impact, anomalies vs 7-day rolling average, next actions, plus a saved email draft and Teams-ready summary.

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-cross-dock-produced-goods
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
      "description": "D365 legal entity to query; defaults to USMF.",
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
      "description": "When to run, e.g. weekday mornings at 7am.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_cross_dock_produced_goods_agent.py` and embedded as the fenced Python below (sha256 c70667639c1b9328…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_cross_dock_produced_goods_agent.py` first:

```bash
python3 scheduled_brief_cross_dock_produced_goods_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_cross_dock_produced_goods_agent.py   # or on stdin
python3 scheduled_brief_cross_dock_produced_goods_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Cross dock produced goods Scheduled Email Brief — Builds a cross dock produced goods morning brief from Dynamics 365 F&SCM (legal entity USMF): top 5 items by impact, anomalies vs 7-day rolling average, next actions, plus a saved email draft and Teams-ready summary.

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-cross-dock-produced-goods
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_cross_dock_produced_goods',
    "version": '3.0.3',
    "display_name": 'Cross dock produced goods Scheduled Email Brief',
    "description": 'Builds a cross dock produced goods morning brief from Dynamics 365 F&SCM (legal entity USMF): top 5 items by impact, anomalies vs 7-day rolling average, next actions, plus a saved email draft and Teams-ready summary.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'inventory_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-cross-dock-produced-goods',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-cross-dock-produced-goods',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'e527dde5c12269a1',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/process-outbound-goods/cross-dock-produced-goods'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/scheduled-brief-cross-dock-produced-goods', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to query; defaults to USMF.', 'owner': 'Responsible owner who receives the drafted email brief.', 'schedule': 'When to run, e.g. weekday mornings at 7am.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Replaces a daily manual spreadsheet stitch with an automatic brief so owners walk into standup already knowing where cross dock produced goods stands.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': 'Using the Dynamics 365 ERP plugin against legal entity USMF, build a short morning brief on cross dock produced goods for the responsible owner. Include: (a) top 5 items by impact today, (b) any anomalies vs the 7-day rolling average, (c) recommended next actions. Draft an email to the owner (save to drafts, do not send). Also produce a Communications-ready summary suitable for a Teams channel post. This recipe is a strong candidate for a Cowork scheduled task - schedule for weekday mornings at 7am.', 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads cross dock produced goods, computes a short brief, drafts an email, and is a strong candidate for a Cowork scheduled task.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a cross dock produced goods morning brief from Dynamics 365 F&SCM (legal entity USMF): top 5 items by impact, anomalies vs 7-day rolling average, next actions, plus a saved email draft and Teams-ready summary.', 'example_request': 'Give me the cross dock produced goods morning brief for USMF and draft it to the owner.', 'inputs': [{'description': 'D365 legal entity to query; defaults to USMF.', 'name': 'legal_entity'}, {'description': 'Responsible owner who receives the drafted email brief.', 'name': 'owner'}, {'description': 'When to run, e.g. weekday mornings at 7am.', 'name': 'schedule'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a daily or weekly cross dock produced goods brief for the responsible owner, drafted as an email and a Teams channel post.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ScheduledBriefCrossDockProducedGoods(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefCrossDockProducedGoods'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query; defaults to USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'owner': {'description': 'Responsible owner who receives the drafted email brief.', 'type': 'string'}, 'schedule': {'description': 'When to run, e.g. weekday mornings at 7am.', 'type': 'string'}},
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
    print(ScheduledBriefCrossDockProducedGoods().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
