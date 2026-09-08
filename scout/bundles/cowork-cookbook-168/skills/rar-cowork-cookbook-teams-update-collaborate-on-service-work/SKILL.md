---
name: "rar-cowork-cookbook-teams-update-collaborate-on-service-work"
description: "Summarizes the current state of collaborate on service work from Dynamics 365 ERP for a legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs, status, and quick-action bu"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_collaborate_on_service_work", "rar_sha256": "e98ffd0d6fc40907ac2e03f2820666a65080e739ed8834a9ec878f1ecad05556", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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
