---
name: "rar-cowork-cookbook-teams-update-monitor-compliance"
description: "Summarizes monitor compliance status from Dynamics 365 F&SCM for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick actions."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_monitor_compliance", "rar_sha256": "a940ebefb62ac1e008773c21a87b640c6778b153a409db54e593ea5e7f4ecad6", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
