---
name: "rar-cowork-cookbook-teams-update-define-service-terms"
description: "Summarizes the current state of define service terms from the Dynamics 365 ERP plugin for a legal entity, returning a markdown Teams channel post plus a saved Adaptive Card JSON with KPIs and quick-action buttons; does n"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_define_service_terms", "rar_sha256": "e0ddfbe9b6f2aa9bd703369e2b8b939789488c1a08d9b0328b369980968811f5", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
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
