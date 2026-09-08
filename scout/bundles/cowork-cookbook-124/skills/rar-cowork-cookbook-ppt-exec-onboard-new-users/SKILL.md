---
name: "rar-cowork-cookbook-ppt-exec-onboard-new-users"
description: "Builds a read-only executive PowerPoint deck on new-user onboarding status from Dynamics 365 ERP data, with title, KPI, trend, red-flag, action and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_onboard_new_users", "rar_sha256": "a2bae41c7e2054e5e258403ee21133c1cb459345ce68dfd3a8c962f8bb374df5", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
