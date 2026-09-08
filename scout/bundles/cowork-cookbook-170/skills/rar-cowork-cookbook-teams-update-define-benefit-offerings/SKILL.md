---
name: "rar-cowork-cookbook-teams-update-define-benefit-offerings"
description: "Summarizes the current state of define benefit offerings from Dynamics 365 F&SCM (legal entity USMF) and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs, status indicators, and quic"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_define_benefit_offerings", "rar_sha256": "78b7f45bc4853abb47eccc707e15fcd323eaf417116d5519f1033a2b265d260c", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_define_benefit_offerings`. The original RAPP
agent is preserved byte-for-byte in `teams_update_define_benefit_offerings_agent.py` and in the RCI capsule.

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

Define benefit offerings Teams Channel Update — Summarizes the current state of define benefit offerings from Dynamics 365 F&SCM (legal entity USMF) and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs, status indicators, and quic

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-define-benefit-offerings
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
      "description": "Output name for the Adaptive Card JSON, e.g. teams-update-define-benefit-offerings-2026-05-24-card.json.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "Dynamics 365 legal entity to summarize; recipe default is USMF.",
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
    "topic": {
      "description": "Subject area to summarize, here 'define benefit offerings'.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_define_benefit_offerings_agent.py` and embedded as the fenced Python below (sha256 78b7f45bc4853abb…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_define_benefit_offerings_agent.py` first:

```bash
python3 teams_update_define_benefit_offerings_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_define_benefit_offerings_agent.py   # or on stdin
python3 teams_update_define_benefit_offerings_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define benefit offerings Teams Channel Update — Summarizes the current state of define benefit offerings from Dynamics 365 F&SCM (legal entity USMF) and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs, status indicators, and quic

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-define-benefit-offerings
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_define_benefit_offerings',
    "version": '3.0.3',
    "display_name": 'Define benefit offerings Teams Channel Update',
    "description": 'Summarizes the current state of define benefit offerings from Dynamics 365 F&SCM (legal entity USMF) and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs, status indicators, and quic',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'hire_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-define-benefit-offerings',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-define-benefit-offerings',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '888462334fd4da2f',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/manage-compensation-and-benefits/define-benefit-offerings'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/teams-update-define-benefit-offerings', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'card_filename': 'Output name for the Adaptive Card JSON, e.g. teams-update-define-benefit-offerings-2026-05-24-card.json.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to summarize; recipe default is USMF.', 'topic': "Subject area to summarize, here 'define benefit offerings'."}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Replaces 'check the spreadsheet' Teams pings with a glanceable card the team can act on directly - reducing back-and-forth and decision latency.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, summarize the current state of define benefit offerings. Produce: (a) a Communications-ready Teams channel post (markdown) with a 2-sentence summary and 3 bullet highlights; (b) an Adaptive Card JSON 'teams-update-define-benefit-offerings-2026-05-24-card.json' showing KPIs, status indicators, and quick-action buttons (e.g., 'View detail', 'Open in D365'). Do not post the card on my behalf - save the artifacts for me to review.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads define benefit offerings, produces a Communications-ready Teams post + an Adaptive Card with quick-action buttons.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Summarizes the current state of define benefit offerings from Dynamics 365 F&SCM (legal entity USMF) and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs, status indicators, and quic', 'example_request': "Draft a Teams post and Adaptive Card on define benefit offerings status from D365 USMF — save them, don't post.", 'inputs': [{'description': 'Dynamics 365 legal entity to summarize; recipe default is USMF.', 'name': 'legal_entity'}, {'description': "Subject area to summarize, here 'define benefit offerings'.", 'name': 'topic'}, {'description': 'Output name for the Adaptive Card JSON, e.g. teams-update-define-benefit-offerings-2026-05-24-card.json.', 'name': 'card_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need a review-ready Teams update on define benefit offerings status plus an Adaptive Card, without anything being posted for you.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class TeamsUpdateDefineBenefitOfferings(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateDefineBenefitOfferings'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'card_filename': {'description': 'Output name for the Adaptive Card JSON, e.g. teams-update-define-benefit-offerings-2026-05-24-card.json.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to summarize; recipe default is USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'topic': {'description': "Subject area to summarize, here 'define benefit offerings'.", 'type': 'string'}},
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
    print(TeamsUpdateDefineBenefitOfferings().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
