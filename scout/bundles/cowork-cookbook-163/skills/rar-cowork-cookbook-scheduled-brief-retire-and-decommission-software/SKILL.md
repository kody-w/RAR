---
name: "rar-cowork-cookbook-scheduled-brief-retire-and-decommission-software"
description: "Builds a morning brief on retiring and decommissioning software from Dynamics 365 ERP data for a legal entity, drafts an email to the responsible owner (saved to drafts, not sent), plus a Teams-ready summary."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_retire_and_decommission_software", "rar_sha256": "af96bed87c0a2fa8156334543f0f604069f84f34eec8cfbe8ba0361434b0aa07", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
