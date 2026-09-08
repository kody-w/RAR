---
name: "rar-cowork-cookbook-teams-update-configure-and-monitor-system-generated-numbers"
description: "Summarizes number sequence configuration and monitoring status from Dynamics 365 F&SCM for a given legal entity, returning a Teams-ready markdown post plus an Adaptive Card JSON file saved for review, not posted."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_configure_and_monitor_system_generated_numbers", "rar_sha256": "7576e44e389e36103171228789515b53afbd71e7f8d2cd5eff58507f4d37ff4b", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_configure_and_monitor_system_generated_numbers`. The original RAPP
agent is preserved byte-for-byte in `teams_update_configure_and_monitor_system_generated_numbers_agent.py` and in the RCI capsule.

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

Configure and monitor system generated numbers Teams Channel Update — Summarizes number sequence configuration and monitoring status from Dynamics 365 F&SCM for a given legal entity, returning a Teams-ready markdown post plus an Adaptive Card JSON file saved for review, not posted.

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-configure-and-monitor-system-generated-numbers
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
    "card_filename": {
      "description": "Output filename for the Adaptive Card JSON, e.g. teams-update-configure-and-monitor-system-generated-numbers-2026-05-24-card.json.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to scope the summary to, e.g. USMF.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_configure_and_monitor_system_generated_numbers_agent.py` and embedded as the fenced Python below (sha256 7576e44e389e3610…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_configure_and_monitor_system_generated_numbers_agent.py` first:

```bash
python3 teams_update_configure_and_monitor_system_generated_numbers_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_configure_and_monitor_system_generated_numbers_agent.py   # or on stdin
python3 teams_update_configure_and_monitor_system_generated_numbers_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Configure and monitor system generated numbers Teams Channel Update — Summarizes number sequence configuration and monitoring status from Dynamics 365 F&SCM for a given legal entity, returning a Teams-ready markdown post plus an Adaptive Card JSON file saved for review, not posted.

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-configure-and-monitor-system-generated-numbers
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_configure_and_monitor_system_generated_numbers',
    "version": '3.0.3',
    "display_name": 'Configure and monitor system generated numbers Teams Channel Update',
    "description": 'Summarizes number sequence configuration and monitoring status from Dynamics 365 F&SCM for a given legal entity, returning a Teams-ready markdown post plus an Adaptive Card JSON file saved for review, not posted.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-configure-and-monitor-system-generated-numbers',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-configure-and-monitor-system-generated-numbers',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '56d0a6856668512d',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/administer-system-features/configure-and-monitor-system-generated-numbers'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/teams-update-configure-and-monitor-system-generated-numbers', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'card_filename': 'Output filename for the Adaptive Card JSON, e.g. teams-update-configure-and-monitor-system-generated-numbers-2026-05-24-card.json.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to scope the summary to, e.g. USMF.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Replaces 'check the spreadsheet' Teams pings with a glanceable card the team can act on directly - reducing back-and-forth and decision latency.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, summarize the current state of configure and monitor system generated numbers. Produce: (a) a Communications-ready Teams channel post (markdown) with a 2-sentence summary and 3 bullet highlights; (b) an Adaptive Card JSON 'teams-update-configure-and-monitor-system-generated-numbers-2026-05-24-card.json' showing KPIs, status indicators, and quick-action buttons (e.g., 'View detail', 'Open in D365'). Do not post the card on my behalf - save the artifacts for me to review.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads configure and monitor system generated numbers, produces a Communications-ready Teams post + an Adaptive Card with quick-action buttons.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Summarizes number sequence configuration and monitoring status from Dynamics 365 F&SCM for a given legal entity, returning a Teams-ready markdown post plus an Adaptive Card JSON file saved for review, not posted.', 'example_request': "Draft a Teams update on system generated numbers status in USMF with an Adaptive Card, but don't post it.", 'inputs': [{'description': 'D365 legal entity to scope the summary to, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Output filename for the Adaptive Card JSON, e.g. teams-update-configure-and-monitor-system-generated-numbers-2026-05-24-card.json.', 'name': 'card_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a drafted Teams channel update with an Adaptive Card on system generated number sequence status in D365 F&SCM.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class TeamsUpdateConfigureAndMonitorSystemGeneratedNumbers(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateConfigureAndMonitorSystemGeneratedNumbers'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'card_filename': {'description': 'Output filename for the Adaptive Card JSON, e.g. teams-update-configure-and-monitor-system-generated-numbers-2026-05-24-card.json.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to scope the summary to, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(TeamsUpdateConfigureAndMonitorSystemGeneratedNumbers().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
