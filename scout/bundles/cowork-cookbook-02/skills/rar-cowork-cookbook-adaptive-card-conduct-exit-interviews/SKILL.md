---
name: "rar-cowork-cookbook-adaptive-card-conduct-exit-interviews"
description: "Generates a read-only Adaptive Card JSON file summarizing exit interview status from Dynamics 365 ERP for a given legal entity, with KPI tiles, a RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_conduct_exit_interviews", "rar_sha256": "6d0676d183ffce276b364957889f752222eb03d1e27dd879e9daf5af0e828e24", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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
