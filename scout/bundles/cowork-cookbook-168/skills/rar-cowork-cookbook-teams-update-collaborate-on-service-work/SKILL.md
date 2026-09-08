---
name: "rar-cowork-cookbook-teams-update-collaborate-on-service-work"
description: "Summarizes the current state of collaborate on service work from Dynamics 365 ERP for a legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs, status, and quick-action bu"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_collaborate_on_service_work", "rar_sha256": "e98ffd0d6fc40907ac2e03f2820666a65080e739ed8834a9ec878f1ecad05556", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_collaborate_on_service_work`. The original RAPP
agent is preserved byte-for-byte in `teams_update_collaborate_on_service_work_agent.py` and in the RCI capsule.

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

Collaborate on service work Teams Channel Update — Summarizes the current state of collaborate on service work from Dynamics 365 ERP for a legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs, status, and quick-action bu

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-collaborate-on-service-work
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
      "description": "Output filename for the Adaptive Card JSON, e.g. teams-update-collaborate-on-service-work-2026-05-24-card.json.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_collaborate_on_service_work_agent.py` and embedded as the fenced Python below (sha256 e98ffd0d6fc40907…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_collaborate_on_service_work_agent.py` first:

```bash
python3 teams_update_collaborate_on_service_work_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_collaborate_on_service_work_agent.py   # or on stdin
python3 teams_update_collaborate_on_service_work_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Collaborate on service work Teams Channel Update — Summarizes the current state of collaborate on service work from Dynamics 365 ERP for a legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs, status, and quick-action bu

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-collaborate-on-service-work
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_collaborate_on_service_work',
    "version": '3.0.3',
    "display_name": 'Collaborate on service work Teams Channel Update',
    "description": 'Summarizes the current state of collaborate on service work from Dynamics 365 ERP for a legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs, status, and quick-action bu',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'service_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-collaborate-on-service-work',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-collaborate-on-service-work',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'f084f12fd56abe2e',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/deliver-services/collaborate-on-service-work'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/teams-update-collaborate-on-service-work', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'card_filename': 'Output filename for the Adaptive Card JSON, e.g. teams-update-collaborate-on-service-work-2026-05-24-card.json.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to summarize, e.g. USMF.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Replaces 'check the spreadsheet' Teams pings with a glanceable card the team can act on directly - reducing back-and-forth and decision latency.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, summarize the current state of collaborate on service work. Produce: (a) a Communications-ready Teams channel post (markdown) with a 2-sentence summary and 3 bullet highlights; (b) an Adaptive Card JSON 'teams-update-collaborate-on-service-work-2026-05-24-card.json' showing KPIs, status indicators, and quick-action buttons (e.g., 'View detail', 'Open in D365'). Do not post the card on my behalf - save the artifacts for me to review.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads collaborate on service work, produces a Communications-ready Teams post + an Adaptive Card with quick-action buttons.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Summarizes the current state of collaborate on service work from Dynamics 365 ERP for a legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs, status, and quick-action bu', 'example_request': "Draft a Teams update on collaborate on service work for USMF with an Adaptive Card, but don't post it.", 'inputs': [{'description': 'D365 legal entity to summarize, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Output filename for the Adaptive Card JSON, e.g. teams-update-collaborate-on-service-work-2026-05-24-card.json.', 'name': 'card_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Use when you need a review-ready Teams channel update plus Adaptive Card on collaborate on service work status from D365 F&SCM data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class TeamsUpdateCollaborateOnServiceWork(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateCollaborateOnServiceWork'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'card_filename': {'description': 'Output filename for the Adaptive Card JSON, e.g. teams-update-collaborate-on-service-work-2026-05-24-card.json.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to summarize, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(TeamsUpdateCollaborateOnServiceWork().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
