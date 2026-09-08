---
name: "rar-cowork-cookbook-scheduled-brief-cross-dock-produced-goods"
description: "Builds a cross dock produced goods morning brief from Dynamics 365 F&SCM (legal entity USMF): top 5 items by impact, anomalies vs 7-day rolling average, next actions, plus a saved email draft and Teams-ready summary."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_cross_dock_produced_goods", "rar_sha256": "c70667639c1b93286764db5a1d9f2af4a3fb2b5923ce3c5e65c43a4709669c50", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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
