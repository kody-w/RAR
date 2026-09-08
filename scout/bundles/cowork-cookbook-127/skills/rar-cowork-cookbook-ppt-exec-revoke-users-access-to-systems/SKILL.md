---
name: "rar-cowork-cookbook-ppt-exec-revoke-users-access-to-systems"
description: "Builds a read-only executive PowerPoint deck on user access revocation status from Dynamics 365 ERP data, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_revoke_users_access_to_systems", "rar_sha256": "3b7e41076506934fda265d7c74591004944c7d1ba2f6ab432bd5667a4e3bb622", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
