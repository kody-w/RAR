---
name: "rar-cowork-cookbook-teams-update-monitor-compliance"
description: "Summarizes monitor compliance status from Dynamics 365 F&SCM for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick actions."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_monitor_compliance", "rar_sha256": "a940ebefb62ac1e008773c21a87b640c6778b153a409db54e593ea5e7f4ecad6", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_monitor_compliance`. The original RAPP
agent is preserved byte-for-byte in `teams_update_monitor_compliance_agent.py` and in the RCI capsule.

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

Monitor compliance Teams Channel Update — Summarizes monitor compliance status from Dynamics 365 F&SCM for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick actions.

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-monitor-compliance
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
      "description": "Filename for the Adaptive Card JSON, e.g. teams-update-monitor-compliance-2026-05-24-card.json.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to report on, e.g. USMF.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_monitor_compliance_agent.py` and embedded as the fenced Python below (sha256 a940ebefb62ac1e0…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_monitor_compliance_agent.py` first:

```bash
python3 teams_update_monitor_compliance_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_monitor_compliance_agent.py   # or on stdin
python3 teams_update_monitor_compliance_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Monitor compliance Teams Channel Update — Summarizes monitor compliance status from Dynamics 365 F&SCM for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick actions.

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-monitor-compliance
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_monitor_compliance',
    "version": '3.0.3',
    "display_name": 'Monitor compliance Teams Channel Update',
    "description": 'Summarizes monitor compliance status from Dynamics 365 F&SCM for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick actions.',
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
        "upstream_slug": 'teams-update-monitor-compliance',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-monitor-compliance',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'f445614f46efb9f8',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-system-compliance/monitor-compliance'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/teams-update-monitor-compliance', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'card_filename': 'Filename for the Adaptive Card JSON, e.g. teams-update-monitor-compliance-2026-05-24-card.json.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report on, e.g. USMF.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Replaces 'check the spreadsheet' Teams pings with a glanceable card the team can act on directly - reducing back-and-forth and decision latency.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, summarize the current state of monitor compliance. Produce: (a) a Communications-ready Teams channel post (markdown) with a 2-sentence summary and 3 bullet highlights; (b) an Adaptive Card JSON 'teams-update-monitor-compliance-2026-05-24-card.json' showing KPIs, status indicators, and quick-action buttons (e.g., 'View detail', 'Open in D365'). Do not post the card on my behalf - save the artifacts for me to review.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads monitor compliance, produces a Communications-ready Teams post + an Adaptive Card with quick-action buttons.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Summarizes monitor compliance status from Dynamics 365 F&SCM for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick actions.', 'example_request': 'Summarize monitor compliance for USMF and draft a Teams post plus an Adaptive Card I can review before posting.', 'inputs': [{'description': 'D365 legal entity to report on, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Filename for the Adaptive Card JSON, e.g. teams-update-monitor-compliance-2026-05-24-card.json.', 'name': 'card_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a review-ready Teams update on monitor compliance from D365 ERP data, with an Adaptive Card saved rather than posted.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class TeamsUpdateMonitorCompliance(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateMonitorCompliance'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'card_filename': {'description': 'Filename for the Adaptive Card JSON, e.g. teams-update-monitor-compliance-2026-05-24-card.json.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report on, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(TeamsUpdateMonitorCompliance().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
