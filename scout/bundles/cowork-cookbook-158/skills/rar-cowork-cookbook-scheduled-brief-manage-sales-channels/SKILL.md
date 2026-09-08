---
name: "rar-cowork-cookbook-scheduled-brief-manage-sales-channels"
description: "Builds a morning brief on manage sales channels from Dynamics 365 F&SCM (legal entity USMF) with top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, then saves a draft email to th"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_manage_sales_channels", "rar_sha256": "343f92aff185789e0bf2a10621981a6e457a7740118afb9ccc32f045cbf706c1", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_manage_sales_channels`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_manage_sales_channels_agent.py` and in the RCI capsule.

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

Manage sales channels Scheduled Email Brief — Builds a morning brief on manage sales channels from Dynamics 365 F&SCM (legal entity USMF) with top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, then saves a draft email to th

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-manage-sales-channels
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
      "description": "D365 legal entity to run against; the recipe defaults to USMF.",
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
      "description": "When to run the brief, e.g. weekday mornings at 7am, daily or weekly.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_manage_sales_channels_agent.py` and embedded as the fenced Python below (sha256 343f92aff185789e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_manage_sales_channels_agent.py` first:

```bash
python3 scheduled_brief_manage_sales_channels_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_manage_sales_channels_agent.py   # or on stdin
python3 scheduled_brief_manage_sales_channels_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage sales channels Scheduled Email Brief — Builds a morning brief on manage sales channels from Dynamics 365 F&SCM (legal entity USMF) with top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, then saves a draft email to th

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-manage-sales-channels
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_manage_sales_channels',
    "version": '3.0.3',
    "display_name": 'Manage sales channels Scheduled Email Brief',
    "description": 'Builds a morning brief on manage sales channels from Dynamics 365 F&SCM (legal entity USMF) with top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, then saves a draft email to th',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'order_to_cash', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-manage-sales-channels',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-manage-sales-channels',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'c86d947bf70528be',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/develop-sales-policies/manage-sales-channels'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/scheduled-brief-manage-sales-channels', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to run against; the recipe defaults to USMF.', 'owner': 'Responsible owner who receives the drafted email brief.', 'schedule': 'When to run the brief, e.g. weekday mornings at 7am, daily or weekly.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Replaces a daily manual spreadsheet stitch with an automatic brief so owners walk into standup already knowing where manage sales channels stands.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': 'Using the Dynamics 365 ERP plugin against legal entity USMF, build a short morning brief on manage sales channels for the responsible owner. Include: (a) top 5 items by impact today, (b) any anomalies vs the 7-day rolling average, (c) recommended next actions. Draft an email to the owner (save to drafts, do not send). Also produce a Communications-ready summary suitable for a Teams channel post. This recipe is a strong candidate for a Cowork scheduled task - schedule for weekday mornings at 7am.', 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads manage sales channels, computes a short brief, drafts an email, and is a strong candidate for a Cowork scheduled task.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a morning brief on manage sales channels from Dynamics 365 F&SCM (legal entity USMF) with top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, then saves a draft email to th', 'example_request': 'Give me the 7am morning brief on manage sales channels in USMF and draft it to the owner.', 'inputs': [{'description': 'D365 legal entity to run against; the recipe defaults to USMF.', 'name': 'legal_entity'}, {'description': 'Responsible owner who receives the drafted email brief.', 'name': 'owner'}, {'description': 'When to run the brief, e.g. weekday mornings at 7am, daily or weekly.', 'name': 'schedule'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a sales-channel owner wants a daily or weekly morning brief on manage sales channels, as a drafted email and Teams post rather than a sent message.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ScheduledBriefManageSalesChannels(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefManageSalesChannels'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against; the recipe defaults to USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'owner': {'description': 'Responsible owner who receives the drafted email brief.', 'type': 'string'}, 'schedule': {'description': 'When to run the brief, e.g. weekday mornings at 7am, daily or weekly.', 'type': 'string'}},
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
    print(ScheduledBriefManageSalesChannels().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
