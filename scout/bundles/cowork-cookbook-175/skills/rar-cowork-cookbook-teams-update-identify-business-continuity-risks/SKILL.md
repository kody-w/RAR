---
name: "rar-cowork-cookbook-teams-update-identify-business-continuity-risks"
description: "Summarizes business continuity risk status from Dynamics 365 F&SCM for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_identify_business_continuity_risks", "rar_sha256": "364e0d03ba6c3a77e1be8bdaca6637473168ec9a23193abd51eb277f119c9ca6", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
