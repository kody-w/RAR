---
name: "rar-cowork-cookbook-ppt-exec-revoke-users-access-to-systems"
description: "Builds a read-only executive PowerPoint deck on user access revocation status from Dynamics 365 ERP data, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_revoke_users_access_to_systems", "rar_sha256": "3b7e41076506934fda265d7c74591004944c7d1ba2f6ab432bd5667a4e3bb622", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_revoke_users_access_to_systems`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_revoke_users_access_to_systems_agent.py` and in the RCI capsule.

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

Revoke users access to systems Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on user access revocation status from Dynamics 365 ERP data, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-revoke-users-access-to-systems
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
      "description": "Dynamics 365 legal entity to report on (e.g. USMF).",
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
      "description": "Target .pptx filename, e.g. ppt-exec-revoke-users-access-to-systems-2026-05-24.pptx.",
      "type": "string"
    },
    "review_period": {
      "description": "Reporting period and prior period used for the trend chart comparison (e.g. monthly).",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_revoke_users_access_to_systems_agent.py` and embedded as the fenced Python below (sha256 3b7e41076506934f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_revoke_users_access_to_systems_agent.py` first:

```bash
python3 ppt_exec_revoke_users_access_to_systems_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_revoke_users_access_to_systems_agent.py   # or on stdin
python3 ppt_exec_revoke_users_access_to_systems_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Revoke users access to systems Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on user access revocation status from Dynamics 365 ERP data, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-revoke-users-access-to-systems
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_revoke_users_access_to_systems',
    "version": '3.0.3',
    "display_name": 'Revoke users access to systems Executive PowerPoint Deck',
    "description": 'Builds a read-only executive PowerPoint deck on user access revocation status from Dynamics 365 ERP data, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.',
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
        "upstream_slug": 'ppt-exec-revoke-users-access-to-systems',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-revoke-users-access-to-systems',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '0922139159b46756',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-system-access-and-security/revoke-users-access-to-systems'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/ppt-exec-revoke-users-access-to-systems', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to report on (e.g. USMF).', 'output_filename': 'Target .pptx filename, e.g. ppt-exec-revoke-users-access-to-systems-2026-05-24.pptx.', 'review_period': 'Reporting period and prior period used for the trend chart comparison (e.g. monthly).'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Cuts deck prep time from hours to minutes for revoke users access to systems reviews while ensuring the numbers in the slides match D365 to the cent.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build an executive PowerPoint deck on revoke users access to systems for a 15-minute monthly review. Produce 'ppt-exec-revoke-users-access-to-systems-2026-05-24.pptx' with: (1) title slide, (2) headline KPIs, (3) trend chart vs prior period, (4) top issues / red flags, (5) recommended actions, (6) appendix - data sources and methodology. Include speaker-notes on each slide with talking points. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads revoke users access to systems data and produces a 6-8 slide PowerPoint suitable for an executive review.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only executive PowerPoint deck on user access revocation status from Dynamics 365 ERP data, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.', 'example_request': "Build an exec PowerPoint on revoke users access to systems for USMF for this month's 15-minute review.", 'inputs': [{'description': 'Dynamics 365 legal entity to report on (e.g. USMF).', 'name': 'legal_entity'}, {'description': 'Target .pptx filename, e.g. ppt-exec-revoke-users-access-to-systems-2026-05-24.pptx.', 'name': 'output_filename'}, {'description': 'Reporting period and prior period used for the trend chart comparison (e.g. monthly).', 'name': 'review_period'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user needs an executive-ready PPTX summarizing revoke-users-access-to-systems status from D365 F&SCM for a short monthly review.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class PptExecRevokeUsersAccessToSystems(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecRevokeUsersAccessToSystems'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to report on (e.g. USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Target .pptx filename, e.g. ppt-exec-revoke-users-access-to-systems-2026-05-24.pptx.', 'type': 'string'}, 'review_period': {'description': 'Reporting period and prior period used for the trend chart comparison (e.g. monthly).', 'type': 'string'}},
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
    print(PptExecRevokeUsersAccessToSystems().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
