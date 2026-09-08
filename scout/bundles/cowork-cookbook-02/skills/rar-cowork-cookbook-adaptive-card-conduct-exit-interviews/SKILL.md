---
name: "rar-cowork-cookbook-adaptive-card-conduct-exit-interviews"
description: "Generates a read-only Adaptive Card JSON file summarizing exit interview status from Dynamics 365 ERP for a given legal entity, with KPI tiles, a RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_conduct_exit_interviews", "rar_sha256": "6d0676d183ffce276b364957889f752222eb03d1e27dd879e9daf5af0e828e24", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_conduct_exit_interviews`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_conduct_exit_interviews_agent.py` and in the RCI capsule.

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

Conduct exit interviews Status Adaptive Card — Generates a read-only Adaptive Card JSON file summarizing exit interview status from Dynamics 365 ERP for a given legal entity, with KPI tiles, a RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-conduct-exit-interviews
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
    "as_of_date": {
      "description": "Snapshot date used in the card timestamp and output filename.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "Dynamics 365 legal entity to query, e.g. USMF.",
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
      "description": "Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-conduct-exit-interviews-2026-05-24-card.json.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_conduct_exit_interviews_agent.py` and embedded as the fenced Python below (sha256 6d0676d183ffce27…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_conduct_exit_interviews_agent.py` first:

```bash
python3 adaptive_card_conduct_exit_interviews_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_conduct_exit_interviews_agent.py   # or on stdin
python3 adaptive_card_conduct_exit_interviews_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Conduct exit interviews Status Adaptive Card — Generates a read-only Adaptive Card JSON file summarizing exit interview status from Dynamics 365 ERP for a given legal entity, with KPI tiles, a RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-conduct-exit-interviews
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_conduct_exit_interviews',
    "version": '3.0.2',
    "display_name": 'Conduct exit interviews Status Adaptive Card',
    "description": 'Generates a read-only Adaptive Card JSON file summarizing exit interview status from Dynamics 365 ERP for a given legal entity, with KPI tiles, a RAG row, and action buttons.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'hire_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-conduct-exit-interviews',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-conduct-exit-interviews',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '19186a45075ced88',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/offboard-talent/conduct-exit-interviews'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/adaptive-card-conduct-exit-interviews', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'as_of_date': 'Snapshot date used in the card timestamp and output filename.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to query, e.g. USMF.', 'output_filename': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-conduct-exit-interviews-2026-05-24-card.json.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives any consuming app (Teams, Outlook, custom dashboard) a single canonical conduct exit interviews status card so different surfaces always show the same numbers.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, produce an Adaptive Card JSON file 'adaptive-card-conduct-exit-interviews-2026-05-24-card.json' that visualizes the current state of conduct exit interviews. Include: header with title and timestamp, 3-5 KPI tiles with current value + trend arrow, a RAG indicator row, and 2-3 action buttons. The card should render correctly in Teams, Outlook Adaptive Card preview, and the Adaptive Cards designer. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates an Adaptive Card JSON file with current conduct exit interviews KPIs and RAG indicators.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Generates a read-only Adaptive Card JSON file summarizing exit interview status from Dynamics 365 ERP for a given legal entity, with KPI tiles, a RAG row, and action buttons.', 'example_request': 'Make an Adaptive Card showing exit interview status for USMF as of 2026-05-24.', 'inputs': [{'description': 'Dynamics 365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Snapshot date used in the card timestamp and output filename.', 'name': 'as_of_date'}, {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-conduct-exit-interviews-2026-05-24-card.json.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants an embeddable Adaptive Card snapshot of exit interview status for Teams, Outlook, or a dashboard, without changing any D365 data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AdaptiveCardConductExitInterviews(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardConductExitInterviews'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'as_of_date': {'description': 'Snapshot date used in the card timestamp and output filename.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-conduct-exit-interviews-2026-05-24-card.json.', 'type': 'string'}},
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
    print(AdaptiveCardConductExitInterviews().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
