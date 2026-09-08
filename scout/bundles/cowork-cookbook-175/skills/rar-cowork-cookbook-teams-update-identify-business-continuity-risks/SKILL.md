---
name: "rar-cowork-cookbook-teams-update-identify-business-continuity-risks"
description: "Summarizes business continuity risk status from Dynamics 365 F&SCM for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_identify_business_continuity_risks", "rar_sha256": "364e0d03ba6c3a77e1be8bdaca6637473168ec9a23193abd51eb277f119c9ca6", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_identify_business_continuity_risks`. The original RAPP
agent is preserved byte-for-byte in `teams_update_identify_business_continuity_risks_agent.py` and in the RCI capsule.

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

Identify business continuity risks Teams Channel Update — Summarizes business continuity risk status from Dynamics 365 F&SCM for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-identify-business-continuity-risks
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
      "description": "Filename for the Adaptive Card JSON, e.g. teams-update-identify-business-continuity-risks-2026-05-24-card.json.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to summarize, e.g. USMF.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_identify_business_continuity_risks_agent.py` and embedded as the fenced Python below (sha256 364e0d03ba6c3a77…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_identify_business_continuity_risks_agent.py` first:

```bash
python3 teams_update_identify_business_continuity_risks_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_identify_business_continuity_risks_agent.py   # or on stdin
python3 teams_update_identify_business_continuity_risks_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Identify business continuity risks Teams Channel Update — Summarizes business continuity risk status from Dynamics 365 F&SCM for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-identify-business-continuity-risks
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_identify_business_continuity_risks',
    "version": '3.0.3',
    "display_name": 'Identify business continuity risks Teams Channel Update',
    "description": 'Summarizes business continuity risk status from Dynamics 365 F&SCM for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons.',
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
        "upstream_slug": 'teams-update-identify-business-continuity-risks',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-identify-business-continuity-risks',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '4ee5b84fcfc86df0',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/define-business-continuity-plan/identify-business-continuity-risks'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/teams-update-identify-business-continuity-risks', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'card_filename': 'Filename for the Adaptive Card JSON, e.g. teams-update-identify-business-continuity-risks-2026-05-24-card.json.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to summarize, e.g. USMF.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Replaces 'check the spreadsheet' Teams pings with a glanceable card the team can act on directly - reducing back-and-forth and decision latency.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, summarize the current state of identify business continuity risks. Produce: (a) a Communications-ready Teams channel post (markdown) with a 2-sentence summary and 3 bullet highlights; (b) an Adaptive Card JSON 'teams-update-identify-business-continuity-risks-2026-05-24-card.json' showing KPIs, status indicators, and quick-action buttons (e.g., 'View detail', 'Open in D365'). Do not post the card on my behalf - save the artifacts for me to review.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads identify business continuity risks, produces a Communications-ready Teams post + an Adaptive Card with quick-action buttons.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Summarizes business continuity risk status from Dynamics 365 F&SCM for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons.', 'example_request': 'Draft a Teams update on business continuity risks for USMF and save the post plus an Adaptive Card for me to review.', 'inputs': [{'description': 'D365 legal entity to summarize, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Filename for the Adaptive Card JSON, e.g. teams-update-identify-business-continuity-risks-2026-05-24-card.json.', 'name': 'card_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a review-ready Teams update on business continuity risks from D365 ERP data, saved as files rather than posted.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class TeamsUpdateIdentifyBusinessContinuityRisks(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateIdentifyBusinessContinuityRisks'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'card_filename': {'description': 'Filename for the Adaptive Card JSON, e.g. teams-update-identify-business-continuity-risks-2026-05-24-card.json.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to summarize, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(TeamsUpdateIdentifyBusinessContinuityRisks().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
