---
name: "rar-cowork-cookbook-teams-update-configure-and-monitor-system-generated-numbers"
description: "Summarizes number sequence configuration and monitoring status from Dynamics 365 F&SCM for a given legal entity, returning a Teams-ready markdown post plus an Adaptive Card JSON file saved for review, not posted."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_configure_and_monitor_system_generated_numbers", "rar_sha256": "7576e44e389e36103171228789515b53afbd71e7f8d2cd5eff58507f4d37ff4b", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
