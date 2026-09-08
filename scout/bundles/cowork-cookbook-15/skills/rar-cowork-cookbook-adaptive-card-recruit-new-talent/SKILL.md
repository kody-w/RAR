---
name: "rar-cowork-cookbook-adaptive-card-recruit-new-talent"
description: "Generates a read-only Adaptive Card JSON file visualizing recruit-new-talent status from Dynamics 365 F&SCM (legal entity USMF), with header, KPI tiles, RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_recruit_new_talent", "rar_sha256": "aa330b38e4534db096d5578b5cc0e34b04c25de30b195ea87565ccf9711a2b05", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_recruit_new_talent`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_recruit_new_talent_agent.py` and in the RCI capsule.

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

Recruit new talent Status Adaptive Card — Generates a read-only Adaptive Card JSON file visualizing recruit-new-talent status from Dynamics 365 F&SCM (legal entity USMF), with header, KPI tiles, RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-recruit-new-talent
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
      "description": "Name of the Adaptive Card JSON file to produce.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_recruit_new_talent_agent.py` and embedded as the fenced Python below (sha256 aa330b38e4534db0…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_recruit_new_talent_agent.py` first:

```bash
python3 adaptive_card_recruit_new_talent_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_recruit_new_talent_agent.py   # or on stdin
python3 adaptive_card_recruit_new_talent_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Recruit new talent Status Adaptive Card — Generates a read-only Adaptive Card JSON file visualizing recruit-new-talent status from Dynamics 365 F&SCM (legal entity USMF), with header, KPI tiles, RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-recruit-new-talent
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_recruit_new_talent',
    "version": '3.0.2',
    "display_name": 'Recruit new talent Status Adaptive Card',
    "description": 'Generates a read-only Adaptive Card JSON file visualizing recruit-new-talent status from Dynamics 365 F&SCM (legal entity USMF), with header, KPI tiles, RAG row, and action buttons.',
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
        "upstream_slug": 'adaptive-card-recruit-new-talent',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-recruit-new-talent',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '78f01c8a22043700',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/recruit-and-onboard-talent/recruit-new-talent'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/adaptive-card-recruit-new-talent', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'as_of_date': 'Snapshot date used in the card timestamp and output filename.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'output_filename': 'Name of the Adaptive Card JSON file to produce.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives any consuming app (Teams, Outlook, custom dashboard) a single canonical recruit new talent status card so different surfaces always show the same numbers.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, produce an Adaptive Card JSON file 'adaptive-card-recruit-new-talent-2026-05-24-card.json' that visualizes the current state of recruit new talent. Include: header with title and timestamp, 3-5 KPI tiles with current value + trend arrow, a RAG indicator row, and 2-3 action buttons. The card should render correctly in Teams, Outlook Adaptive Card preview, and the Adaptive Cards designer. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates an Adaptive Card JSON file with current recruit new talent KPIs and RAG indicators.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Generates a read-only Adaptive Card JSON file visualizing recruit-new-talent status from Dynamics 365 F&SCM (legal entity USMF), with header, KPI tiles, RAG row, and action buttons.', 'example_request': 'Make an Adaptive Card showing recruit new talent status for USMF as of 2026-05-24.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Snapshot date used in the card timestamp and output filename.', 'name': 'as_of_date'}, {'description': 'Name of the Adaptive Card JSON file to produce.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a Teams/Outlook-ready Adaptive Card snapshot of recruiting status pulled from D365 ERP, without changing any data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AdaptiveCardRecruitNewTalent(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardRecruitNewTalent'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'as_of_date': {'description': 'Snapshot date used in the card timestamp and output filename.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Adaptive Card JSON file to produce.', 'type': 'string'}},
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
    print(AdaptiveCardRecruitNewTalent().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
