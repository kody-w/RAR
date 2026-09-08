---
name: "rar-cowork-cookbook-scheduled-brief-configure-and-manage-agents"
description: "Builds a morning brief on configure-and-manage-agents activity from Dynamics 365 ERP (legal entity USMF): top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then saves a draft email to the o"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_configure_and_manage_agents", "rar_sha256": "0dd888c7d0073615bf768fe53a0157ab03893f4c9a609d6e647302b8d3d9b6c8", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_configure_and_manage_agents`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_configure_and_manage_agents_agent.py` and in the RCI capsule.

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

Configure and manage agents Scheduled Email Brief — Builds a morning brief on configure-and-manage-agents activity from Dynamics 365 ERP (legal entity USMF): top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then saves a draft email to the o

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-configure-and-manage-agents
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
      "description": "D365 F&SCM legal entity to run against (recipe default: USMF).",
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
      "description": "When to run it, e.g. weekday mornings at 7am, or daily/weekly.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_configure_and_manage_agents_agent.py` and embedded as the fenced Python below (sha256 0dd888c7d0073615…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_configure_and_manage_agents_agent.py` first:

```bash
python3 scheduled_brief_configure_and_manage_agents_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_configure_and_manage_agents_agent.py   # or on stdin
python3 scheduled_brief_configure_and_manage_agents_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Configure and manage agents Scheduled Email Brief — Builds a morning brief on configure-and-manage-agents activity from Dynamics 365 ERP (legal entity USMF): top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then saves a draft email to the o

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-configure-and-manage-agents
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_configure_and_manage_agents',
    "version": '3.0.3',
    "display_name": 'Configure and manage agents Scheduled Email Brief',
    "description": 'Builds a morning brief on configure-and-manage-agents activity from Dynamics 365 ERP (legal entity USMF): top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then saves a draft email to the o',
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
        "upstream_slug": 'scheduled-brief-configure-and-manage-agents',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-configure-and-manage-agents',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '1dd5d4fc7a9a7333',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/administer-system-features/configure-and-manage-agents'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/scheduled-brief-configure-and-manage-agents', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 F&SCM legal entity to run against (recipe default: USMF).', 'owner': 'Responsible owner who receives the drafted email brief.', 'schedule': 'When to run it, e.g. weekday mornings at 7am, or daily/weekly.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Replaces a daily manual spreadsheet stitch with an automatic brief so owners walk into standup already knowing where configure and manage agents stands.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': 'Using the Dynamics 365 ERP plugin against legal entity USMF, build a short morning brief on configure and manage agents for the responsible owner. Include: (a) top 5 items by impact today, (b) any anomalies vs the 7-day rolling average, (c) recommended next actions. Draft an email to the owner (save to drafts, do not send). Also produce a Communications-ready summary suitable for a Teams channel post. This recipe is a strong candidate for a Cowork scheduled task - schedule for weekday mornings at 7am.', 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads configure and manage agents, computes a short brief, drafts an email, and is a strong candidate for a Cowork scheduled task.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a morning brief on configure-and-manage-agents activity from Dynamics 365 ERP (legal entity USMF): top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then saves a draft email to the o', 'example_request': 'Draft my 7am weekday morning brief on configure and manage agents from D365 USMF for the owner.', 'inputs': [{'description': 'D365 F&SCM legal entity to run against (recipe default: USMF).', 'name': 'legal_entity'}, {'description': 'Responsible owner who receives the drafted email brief.', 'name': 'owner'}, {'description': 'When to run it, e.g. weekday mornings at 7am, or daily/weekly.', 'name': 'schedule'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a responsible owner wants a daily or weekly D365 ERP morning brief on configure and manage agents, drafted as email plus a Teams channel post.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ScheduledBriefConfigureAndManageAgents(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefConfigureAndManageAgents'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 F&SCM legal entity to run against (recipe default: USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'owner': {'description': 'Responsible owner who receives the drafted email brief.', 'type': 'string'}, 'schedule': {'description': 'When to run it, e.g. weekday mornings at 7am, or daily/weekly.', 'type': 'string'}},
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
    print(ScheduledBriefConfigureAndManageAgents().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
