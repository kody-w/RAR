---
name: "rar-cowork-cookbook-scheduled-brief-configure-and-manage-agents"
description: "Builds a morning brief on configure-and-manage-agents activity from Dynamics 365 ERP (legal entity USMF): top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then saves a draft email to the o"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_configure_and_manage_agents", "rar_sha256": "0dd888c7d0073615bf768fe53a0157ab03893f4c9a609d6e647302b8d3d9b6c8", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
