---
name: "rar-cowork-cookbook-scheduled-brief-retire-and-decommission-software"
description: "Builds a morning brief on retiring and decommissioning software from Dynamics 365 ERP data for a legal entity, drafts an email to the responsible owner (saved to drafts, not sent), plus a Teams-ready summary."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_retire_and_decommission_software", "rar_sha256": "af96bed87c0a2fa8156334543f0f604069f84f34eec8cfbe8ba0361434b0aa07", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_retire_and_decommission_software`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_retire_and_decommission_software_agent.py` and in the RCI capsule.

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

Retire and decommission software Scheduled Email Brief — Builds a morning brief on retiring and decommissioning software from Dynamics 365 ERP data for a legal entity, drafts an email to the responsible owner (saved to drafts, not sent), plus a Teams-ready summary.

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-retire-and-decommission-software
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
      "description": "Dynamics 365 F&SCM legal entity to query, e.g. USMF.",
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
      "description": "When the brief should run, e.g. weekday mornings at 7am, daily, or weekly.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_retire_and_decommission_software_agent.py` and embedded as the fenced Python below (sha256 af96bed87c0a2fa8…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_retire_and_decommission_software_agent.py` first:

```bash
python3 scheduled_brief_retire_and_decommission_software_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_retire_and_decommission_software_agent.py   # or on stdin
python3 scheduled_brief_retire_and_decommission_software_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Retire and decommission software Scheduled Email Brief — Builds a morning brief on retiring and decommissioning software from Dynamics 365 ERP data for a legal entity, drafts an email to the responsible owner (saved to drafts, not sent), plus a Teams-ready summary.

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-retire-and-decommission-software
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_retire_and_decommission_software',
    "version": '3.0.3',
    "display_name": 'Retire and decommission software Scheduled Email Brief',
    "description": 'Builds a morning brief on retiring and decommissioning software from Dynamics 365 ERP data for a legal entity, drafts an email to the responsible owner (saved to drafts, not sent), plus a Teams-ready summary.',
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
        "upstream_slug": 'scheduled-brief-retire-and-decommission-software',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-retire-and-decommission-software',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'cdbf05ae93bd1575',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/uptake-software-releases/retire-and-decommission-software'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/scheduled-brief-retire-and-decommission-software', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 F&SCM legal entity to query, e.g. USMF.', 'owner': 'Responsible owner who receives the drafted email brief.', 'schedule': 'When the brief should run, e.g. weekday mornings at 7am, daily, or weekly.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Replaces a daily manual spreadsheet stitch with an automatic brief so owners walk into standup already knowing where retire and decommission software stands.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': 'Using the Dynamics 365 ERP plugin against legal entity USMF, build a short morning brief on retire and decommission software for the responsible owner. Include: (a) top 5 items by impact today, (b) any anomalies vs the 7-day rolling average, (c) recommended next actions. Draft an email to the owner (save to drafts, do not send). Also produce a Communications-ready summary suitable for a Teams channel post. This recipe is a strong candidate for a Cowork scheduled task - schedule for weekday mornings at 7am.', 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads retire and decommission software, computes a short brief, drafts an email, and is a strong candidate for a Cowork scheduled task.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a morning brief on retiring and decommissioning software from Dynamics 365 ERP data for a legal entity, drafts an email to the responsible owner (saved to drafts, not sent), plus a Teams-ready summary.', 'example_request': 'Draft my weekly retire-and-decommission software brief for USMF and email it to the owner as a draft.', 'inputs': [{'description': 'Dynamics 365 F&SCM legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Responsible owner who receives the drafted email brief.', 'name': 'owner'}, {'description': 'When the brief should run, e.g. weekday mornings at 7am, daily, or weekly.', 'name': 'schedule'}], 'model': 'claude-opus-5', 'when_to_use': 'Use for a recurring daily or weekly software retirement/decommission brief for an owner, e.g. scheduled weekday mornings at 7am.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ScheduledBriefRetireAndDecommissionSoftware(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefRetireAndDecommissionSoftware'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 F&SCM legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'owner': {'description': 'Responsible owner who receives the drafted email brief.', 'type': 'string'}, 'schedule': {'description': 'When the brief should run, e.g. weekday mornings at 7am, daily, or weekly.', 'type': 'string'}},
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
    print(ScheduledBriefRetireAndDecommissionSoftware().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
