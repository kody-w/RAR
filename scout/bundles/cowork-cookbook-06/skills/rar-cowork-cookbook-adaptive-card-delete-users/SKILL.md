---
name: "rar-cowork-cookbook-adaptive-card-delete-users"
description: "Generates a read-only Adaptive Card JSON file visualizing delete users status from Dynamics 365 F&SCM (legal entity USMF), with header, KPI tiles, RAG row, and action buttons. Call for a dashboard/Teams-ready card."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_delete_users", "rar_sha256": "f165c84a477beb36ef8f3fa16d7d59fdab88b6e93af48ca77c79a54294fd1920", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_delete_users`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_delete_users_agent.py` and in the RCI capsule.

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

Delete users Status Adaptive Card — Generates a read-only Adaptive Card JSON file visualizing delete users status from Dynamics 365 F&SCM (legal entity USMF), with header, KPI tiles, RAG row, and action buttons. Call for a dashboard/Teams-ready card.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-delete-users
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
    "as_of_date": {
      "description": "Date stamp used in the card header/timestamp and file name.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to report against (recipe default: USMF).",
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
    "output_file_name": {
      "description": "File name for the generated card JSON, e.g. adaptive-card-delete-users-2026-05-24-card.json.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_delete_users_agent.py` and embedded as the fenced Python below (sha256 f165c84a477beb36…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_delete_users_agent.py` first:

```bash
python3 adaptive_card_delete_users_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_delete_users_agent.py   # or on stdin
python3 adaptive_card_delete_users_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Delete users Status Adaptive Card — Generates a read-only Adaptive Card JSON file visualizing delete users status from Dynamics 365 F&SCM (legal entity USMF), with header, KPI tiles, RAG row, and action buttons. Call for a dashboard/Teams-ready card.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-delete-users
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_delete_users',
    "version": '3.0.2',
    "display_name": 'Delete users Status Adaptive Card',
    "description": 'Generates a read-only Adaptive Card JSON file visualizing delete users status from Dynamics 365 F&SCM (legal entity USMF), with header, KPI tiles, RAG row, and action buttons. Call for a dashboard/Teams-ready card.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'verified',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'adaptive-card-delete-users',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-delete-users',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '40dad3c2053ec79a',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-06-01', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-system-access-and-security/delete-users'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/adaptive-card-delete-users', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'as_of_date': 'Date stamp used in the card header/timestamp and file name.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report against (recipe default: USMF).', 'output_file_name': 'File name for the generated card JSON, e.g. adaptive-card-delete-users-2026-05-24-card.json.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives any consuming app (Teams, Outlook, custom dashboard) a single canonical delete users status card so different surfaces always show the same numbers.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, produce an Adaptive Card JSON file 'adaptive-card-delete-users-2026-05-24-card.json' that visualizes the current state of delete users. Include: header with title and timestamp, 3-5 KPI tiles with current value + trend arrow, a RAG indicator row, and 2-3 action buttons. The card should render correctly in Teams, Outlook Adaptive Card preview, and the Adaptive Cards designer. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-06-01', 'what_it_does': 'Generates an Adaptive Card JSON file with current delete users KPIs and RAG indicators.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Generates a read-only Adaptive Card JSON file visualizing delete users status from Dynamics 365 F&SCM (legal entity USMF), with header, KPI tiles, RAG row, and action buttons. Call for a dashboard/Teams-ready card.', 'example_request': 'Make an Adaptive Card JSON of delete users status for USMF as of 2026-05-24, read-only.', 'inputs': [{'description': 'D365 legal entity to report against (recipe default: USMF).', 'name': 'legal_entity'}, {'description': 'File name for the generated card JSON, e.g. adaptive-card-delete-users-2026-05-24-card.json.', 'name': 'output_file_name'}, {'description': 'Date stamp used in the card header/timestamp and file name.', 'name': 'as_of_date'}], 'model': 'claude-opus-5', 'when_to_use': 'Use when you need a shareable Adaptive Card snapshot of delete users status from D365 ERP for Teams, Outlook, or dashboards, without changing any data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AdaptiveCardDeleteUsers(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardDeleteUsers'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'as_of_date': {'description': 'Date stamp used in the card header/timestamp and file name.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report against (recipe default: USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_file_name': {'description': 'File name for the generated card JSON, e.g. adaptive-card-delete-users-2026-05-24-card.json.', 'type': 'string'}},
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
    print(AdaptiveCardDeleteUsers().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
