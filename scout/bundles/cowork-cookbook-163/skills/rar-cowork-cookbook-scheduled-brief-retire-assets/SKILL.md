---
name: "rar-cowork-cookbook-scheduled-brief-retire-assets"
description: "Builds a morning brief on retire assets from Dynamics 365 ERP (legal entity USMF): top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, then saves an unsent email draft to the owne"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_retire_assets", "rar_sha256": "d6d4f8743b6d6fc7c53e9540d4017d544f9bc3433f6c874a151462b04cd40f07", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
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
