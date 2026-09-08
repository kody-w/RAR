---
name: "rar-cowork-cookbook-adaptive-card-mitigate-and-update-the-disaster-recovery-plan"
description: "Generates a read-only Adaptive Card JSON file summarizing disaster recovery plan mitigation status from Dynamics 365 F&SCM, with header, 3-5 KPI tiles, a RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_mitigate_and_update_the_disaster_recovery_plan", "rar_sha256": "eabecd921f5c0d473240e775ba8586d021bbca96c899e0a5f79bfac4e28faff1", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_mitigate_and_update_the_disaster_recovery_plan`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_mitigate_and_update_the_disaster_recovery_plan_agent.py` and in the RCI capsule.

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

Mitigate and update the disaster recovery plan Status Adaptive Card — Generates a read-only Adaptive Card JSON file summarizing disaster recovery plan mitigation status from Dynamics 365 F&SCM, with header, 3-5 KPI tiles, a RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-mitigate-and-update-the-disaster-recovery-plan
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
      "description": "D365 legal entity to query, e.g. USMF.",
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
    "output_filename": {
      "description": "Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-mitigate-and-update-the-disaster-recovery-plan-2026-05-24-card.json.",
      "type": "string"
    },
    "snapshot_date": {
      "description": "Date the status snapshot represents, used in the card header timestamp and filename.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_mitigate_and_update_the_disaster_recovery_plan_agent.py` and embedded as the fenced Python below (sha256 eabecd921f5c0d47…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_mitigate_and_update_the_disaster_recovery_plan_agent.py` first:

```bash
python3 adaptive_card_mitigate_and_update_the_disaster_recovery_plan_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_mitigate_and_update_the_disaster_recovery_plan_agent.py   # or on stdin
python3 adaptive_card_mitigate_and_update_the_disaster_recovery_plan_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Mitigate and update the disaster recovery plan Status Adaptive Card — Generates a read-only Adaptive Card JSON file summarizing disaster recovery plan mitigation status from Dynamics 365 F&SCM, with header, 3-5 KPI tiles, a RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-mitigate-and-update-the-disaster-recovery-plan
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_mitigate_and_update_the_disaster_recovery_plan',
    "version": '3.0.2',
    "display_name": 'Mitigate and update the disaster recovery plan Status Adaptive Card',
    "description": 'Generates a read-only Adaptive Card JSON file summarizing disaster recovery plan mitigation status from Dynamics 365 F&SCM, with header, 3-5 KPI tiles, a RAG row, and action buttons.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-mitigate-and-update-the-disaster-recovery-plan',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-mitigate-and-update-the-disaster-recovery-plan',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'dbb2d94f7f88dea6',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-06-01', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/define-business-continuity-plan/mitigate-and-update-the-disaster-recovery-plan'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/adaptive-card-mitigate-and-update-the-disaster-recovery-plan', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'output_filename': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-mitigate-and-update-the-disaster-recovery-plan-2026-05-24-card.json.', 'snapshot_date': 'Date the status snapshot represents, used in the card header timestamp and filename.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives any consuming app (Teams, Outlook, custom dashboard) a single canonical mitigate and update the disaster recovery plan status card so different surfaces always show the same numbers.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, produce an Adaptive Card JSON file 'adaptive-card-mitigate-and-update-the-disaster-recovery-plan-2026-05-24-card.json' that visualizes the current state of mitigate and update the disaster recovery plan. Include: header with title and timestamp, 3-5 KPI tiles with current value + trend arrow, a RAG indicator row, and 2-3 action buttons. The card should render correctly in Teams, Outlook Adaptive Card preview, and the Adaptive Cards designer. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-06-01', 'what_it_does': 'Generates an Adaptive Card JSON file with current mitigate and update the disaster recovery plan KPIs and RAG indicators.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Generates a read-only Adaptive Card JSON file summarizing disaster recovery plan mitigation status from Dynamics 365 F&SCM, with header, 3-5 KPI tiles, a RAG row, and action buttons.', 'example_request': 'Make me an Adaptive Card JSON of disaster recovery plan status from D365 USMF for 2026-05-24.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-mitigate-and-update-the-disaster-recovery-plan-2026-05-24-card.json.', 'name': 'output_filename'}, {'description': 'Date the status snapshot represents, used in the card header timestamp and filename.', 'name': 'snapshot_date'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a Teams/Outlook-renderable Adaptive Card snapshot of disaster recovery plan status pulled from D365 ERP without changing any data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AdaptiveCardMitigateAndUpdateTheDisasterRecoveryPlan(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardMitigateAndUpdateTheDisasterRecoveryPlan'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-mitigate-and-update-the-disaster-recovery-plan-2026-05-24-card.json.', 'type': 'string'}, 'snapshot_date': {'description': 'Date the status snapshot represents, used in the card header timestamp and filename.', 'type': 'string'}},
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
    print(AdaptiveCardMitigateAndUpdateTheDisasterRecoveryPlan().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
