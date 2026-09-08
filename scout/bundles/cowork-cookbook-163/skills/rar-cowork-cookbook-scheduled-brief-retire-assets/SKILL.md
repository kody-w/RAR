---
name: "rar-cowork-cookbook-scheduled-brief-retire-assets"
description: "Builds a morning brief on retire assets from Dynamics 365 ERP (legal entity USMF): top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, then saves an unsent email draft to the owne"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_retire_assets", "rar_sha256": "d6d4f8743b6d6fc7c53e9540d4017d544f9bc3433f6c874a151462b04cd40f07", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_retire_assets`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_retire_assets_agent.py` and in the RCI capsule.

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

Retire assets Scheduled Email Brief — Builds a morning brief on retire assets from Dynamics 365 ERP (legal entity USMF): top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, then saves an unsent email draft to the owne

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-retire-assets
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
      "description": "Dynamics 365 legal entity to query; the recipe uses USMF.",
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
    "responsible_owner": {
      "description": "Person the brief is addressed to and whose email draft is created.",
      "type": "string"
    },
    "schedule": {
      "description": "When the brief should run, e.g. weekday mornings at 7am.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_retire_assets_agent.py` and embedded as the fenced Python below (sha256 d6d4f8743b6d6fc7…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_retire_assets_agent.py` first:

```bash
python3 scheduled_brief_retire_assets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_retire_assets_agent.py   # or on stdin
python3 scheduled_brief_retire_assets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Retire assets Scheduled Email Brief — Builds a morning brief on retire assets from Dynamics 365 ERP (legal entity USMF): top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, then saves an unsent email draft to the owne

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-retire-assets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_retire_assets',
    "version": '3.0.3',
    "display_name": 'Retire assets Scheduled Email Brief',
    "description": 'Builds a morning brief on retire assets from Dynamics 365 ERP (legal entity USMF): top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, then saves an unsent email draft to the owne',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'acquire_to_dispose', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'verified',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'scheduled-brief-retire-assets',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-retire-assets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '66fdd7ec6a6e6a18',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-06-01', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/dispose-of-assets/retire-assets'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/scheduled-brief-retire-assets', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to query; the recipe uses USMF.', 'responsible_owner': 'Person the brief is addressed to and whose email draft is created.', 'schedule': 'When the brief should run, e.g. weekday mornings at 7am.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Replaces a daily manual spreadsheet stitch with an automatic brief so owners walk into standup already knowing where retire assets stands.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': 'Using the Dynamics 365 ERP plugin against legal entity USMF, build a short morning brief on retire assets for the responsible owner. Include: (a) top 5 items by impact today, (b) any anomalies vs the 7-day rolling average, (c) recommended next actions. Draft an email to the owner (save to drafts, do not send). Also produce a Communications-ready summary suitable for a Teams channel post. This recipe is a strong candidate for a Cowork scheduled task - schedule for weekday mornings at 7am.', 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-06-01', 'what_it_does': 'Reads retire assets, computes a short brief, drafts an email, and is a strong candidate for a Cowork scheduled task.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a morning brief on retire assets from Dynamics 365 ERP (legal entity USMF): top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, then saves an unsent email draft to the owne', 'example_request': 'Send me the retire assets morning brief for USMF and draft the email to the owner.', 'inputs': [{'description': 'Dynamics 365 legal entity to query; the recipe uses USMF.', 'name': 'legal_entity'}, {'description': 'Person the brief is addressed to and whose email draft is created.', 'name': 'responsible_owner'}, {'description': 'When the brief should run, e.g. weekday mornings at 7am.', 'name': 'schedule'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a fixed-asset retirement owner wants a daily or weekly retire-assets brief with a drafted email and Teams-ready summary from D365 ERP data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ScheduledBriefRetireAssets(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefRetireAssets'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to query; the recipe uses USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'responsible_owner': {'description': 'Person the brief is addressed to and whose email draft is created.', 'type': 'string'}, 'schedule': {'description': 'When the brief should run, e.g. weekday mornings at 7am.', 'type': 'string'}},
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
    print(ScheduledBriefRetireAssets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
