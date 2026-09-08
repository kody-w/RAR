---
name: "rar-cowork-cookbook-ppt-exec-onboard-new-users"
description: "Builds a read-only executive PowerPoint deck on new-user onboarding status from Dynamics 365 ERP data, with title, KPI, trend, red-flag, action and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_onboard_new_users", "rar_sha256": "a2bae41c7e2054e5e258403ee21133c1cb459345ce68dfd3a8c962f8bb374df5", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_onboard_new_users`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_onboard_new_users_agent.py` and in the RCI capsule.

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

Onboard new users Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on new-user onboarding status from Dynamics 365 ERP data, with title, KPI, trend, red-flag, action and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-onboard-new-users
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
    "comparison_period": {
      "description": "Prior period to chart the trend against.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to pull data from, e.g. USMF.",
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
      "description": "Target .pptx filename, e.g. ppt-exec-onboard-new-users-2026-05-24.pptx.",
      "type": "string"
    },
    "review_context": {
      "description": "Meeting length and cadence the deck is sized for, e.g. 15-minute monthly review.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_onboard_new_users_agent.py` and embedded as the fenced Python below (sha256 a2bae41c7e2054e5…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_onboard_new_users_agent.py` first:

```bash
python3 ppt_exec_onboard_new_users_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_onboard_new_users_agent.py   # or on stdin
python3 ppt_exec_onboard_new_users_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Onboard new users Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on new-user onboarding status from Dynamics 365 ERP data, with title, KPI, trend, red-flag, action and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-onboard-new-users
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_onboard_new_users',
    "version": '3.0.3',
    "display_name": 'Onboard new users Executive PowerPoint Deck',
    "description": 'Builds a read-only executive PowerPoint deck on new-user onboarding status from Dynamics 365 ERP data, with title, KPI, trend, red-flag, action and appendix slides plus speaker notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-onboard-new-users',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-onboard-new-users',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '417709d617642e56',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-system-access-and-security/onboard-new-users'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/ppt-exec-onboard-new-users', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'comparison_period': 'Prior period to chart the trend against.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to pull data from, e.g. USMF.', 'output_filename': 'Target .pptx filename, e.g. ppt-exec-onboard-new-users-2026-05-24.pptx.', 'review_context': 'Meeting length and cadence the deck is sized for, e.g. 15-minute monthly review.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Cuts deck prep time from hours to minutes for onboard new users reviews while ensuring the numbers in the slides match D365 to the cent.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build an executive PowerPoint deck on onboard new users for a 15-minute monthly review. Produce 'ppt-exec-onboard-new-users-2026-05-24.pptx' with: (1) title slide, (2) headline KPIs, (3) trend chart vs prior period, (4) top issues / red flags, (5) recommended actions, (6) appendix - data sources and methodology. Include speaker-notes on each slide with talking points. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads onboard new users data and produces a 6-8 slide PowerPoint suitable for an executive review.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only executive PowerPoint deck on new-user onboarding status from Dynamics 365 ERP data, with title, KPI, trend, red-flag, action and appendix slides plus speaker notes.', 'example_request': 'Build an executive PowerPoint on new user onboarding from D365 USMF for our 15-minute monthly review.', 'inputs': [{'description': 'D365 legal entity to pull data from, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Target .pptx filename, e.g. ppt-exec-onboard-new-users-2026-05-24.pptx.', 'name': 'output_filename'}, {'description': 'Meeting length and cadence the deck is sized for, e.g. 15-minute monthly review.', 'name': 'review_context'}, {'description': 'Prior period to chart the trend against.', 'name': 'comparison_period'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants an executive-ready onboarding-status deck from D365 F&SCM data for a short monthly review; no data is modified.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class PptExecOnboardNewUsers(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecOnboardNewUsers'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'comparison_period': {'description': 'Prior period to chart the trend against.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to pull data from, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Target .pptx filename, e.g. ppt-exec-onboard-new-users-2026-05-24.pptx.', 'type': 'string'}, 'review_context': {'description': 'Meeting length and cadence the deck is sized for, e.g. 15-minute monthly review.', 'type': 'string'}},
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
    print(PptExecOnboardNewUsers().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
