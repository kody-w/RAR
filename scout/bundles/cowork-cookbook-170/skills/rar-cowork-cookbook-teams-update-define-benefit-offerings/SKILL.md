---
name: "rar-cowork-cookbook-teams-update-define-benefit-offerings"
description: "Summarizes the current state of define benefit offerings from Dynamics 365 F&SCM (legal entity USMF) and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs, status indicators, and quic"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_define_benefit_offerings", "rar_sha256": "78b7f45bc4853abb47eccc707e15fcd323eaf417116d5519f1033a2b265d260c", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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
