---
name: "rar-cowork-cookbook-scheduled-brief-manage-sales-channels"
description: "Builds a morning brief on manage sales channels from Dynamics 365 F&SCM (legal entity USMF) with top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, then saves a draft email to th"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_manage_sales_channels", "rar_sha256": "343f92aff185789e0bf2a10621981a6e457a7740118afb9ccc32f045cbf706c1", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
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
