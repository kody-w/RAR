---
name: "rar-cowork-cookbook-teams-update-define-service-terms"
description: "Summarizes the current state of define service terms from the Dynamics 365 ERP plugin for a legal entity, returning a markdown Teams channel post plus a saved Adaptive Card JSON with KPIs and quick-action buttons; does n"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_define_service_terms", "rar_sha256": "e0ddfbe9b6f2aa9bd703369e2b8b939789488c1a08d9b0328b369980968811f5", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_define_service_terms`. The original RAPP
agent is preserved byte-for-byte in `teams_update_define_service_terms_agent.py` and in the RCI capsule.

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

Define service terms Teams Channel Update — Summarizes the current state of define service terms from the Dynamics 365 ERP plugin for a legal entity, returning a markdown Teams channel post plus a saved Adaptive Card JSON with KPIs and quick-action buttons; does n

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-define-service-terms
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
      "description": "Filename for the Adaptive Card JSON, e.g. teams-update-define-service-terms-2026-05-24-card.json.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to summarize, e.g. USMF.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_define_service_terms_agent.py` and embedded as the fenced Python below (sha256 e0ddfbe9b6f2aa9b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_define_service_terms_agent.py` first:

```bash
python3 teams_update_define_service_terms_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_define_service_terms_agent.py   # or on stdin
python3 teams_update_define_service_terms_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define service terms Teams Channel Update — Summarizes the current state of define service terms from the Dynamics 365 ERP plugin for a legal entity, returning a markdown Teams channel post plus a saved Adaptive Card JSON with KPIs and quick-action buttons; does n

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-define-service-terms
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_define_service_terms',
    "version": '3.0.3',
    "display_name": 'Define service terms Teams Channel Update',
    "description": 'Summarizes the current state of define service terms from the Dynamics 365 ERP plugin for a legal entity, returning a markdown Teams channel post plus a saved Adaptive Card JSON with KPIs and quick-action buttons; does n',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'case_to_resolution', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-define-service-terms',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-define-service-terms',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '8a1d8ec58bbf76fb',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/manage-and-work-on-cases/define-service-terms'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/teams-update-define-service-terms', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'card_filename': 'Filename for the Adaptive Card JSON, e.g. teams-update-define-service-terms-2026-05-24-card.json.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to summarize, e.g. USMF.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Replaces 'check the spreadsheet' Teams pings with a glanceable card the team can act on directly - reducing back-and-forth and decision latency.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, summarize the current state of define service terms. Produce: (a) a Communications-ready Teams channel post (markdown) with a 2-sentence summary and 3 bullet highlights; (b) an Adaptive Card JSON 'teams-update-define-service-terms-2026-05-24-card.json' showing KPIs, status indicators, and quick-action buttons (e.g., 'View detail', 'Open in D365'). Do not post the card on my behalf - save the artifacts for me to review.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads define service terms, produces a Communications-ready Teams post + an Adaptive Card with quick-action buttons.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Summarizes the current state of define service terms from the Dynamics 365 ERP plugin for a legal entity, returning a markdown Teams channel post plus a saved Adaptive Card JSON with KPIs and quick-action buttons; does n', 'example_request': "Draft a Teams channel post and Adaptive Card on define service terms status in USMF — save them, don't post.", 'inputs': [{'description': 'D365 legal entity to summarize, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Filename for the Adaptive Card JSON, e.g. teams-update-define-service-terms-2026-05-24-card.json.', 'name': 'card_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a reviewable Teams channel update on define service terms status in D365 F&SCM, with an Adaptive Card artifact saved rather than posted.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class TeamsUpdateDefineServiceTerms(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateDefineServiceTerms'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'card_filename': {'description': 'Filename for the Adaptive Card JSON, e.g. teams-update-define-service-terms-2026-05-24-card.json.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to summarize, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(TeamsUpdateDefineServiceTerms().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
