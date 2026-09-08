---
name: "rar-cowork-cookbook-teams-update-manage-data-security"
description: "Summarizes data security status from Dynamics 365 F&SCM for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons; nothing is posted."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_manage_data_security", "rar_sha256": "04b74ef826b62b4c77f1d9f9cf7dce52dfdda6da80d30ea00c05ade9e8b66403", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_manage_data_security`. The original RAPP
agent is preserved byte-for-byte in `teams_update_manage_data_security_agent.py` and in the RCI capsule.

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

Manage data security Teams Channel Update — Summarizes data security status from Dynamics 365 F&SCM for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons; nothing is posted.

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-manage-data-security
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
      "description": "Output filename for the Adaptive Card JSON, e.g. teams-update-manage-data-security-2026-05-24-card.json.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_manage_data_security_agent.py` and embedded as the fenced Python below (sha256 04b74ef826b62b4c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_manage_data_security_agent.py` first:

```bash
python3 teams_update_manage_data_security_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_manage_data_security_agent.py   # or on stdin
python3 teams_update_manage_data_security_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage data security Teams Channel Update — Summarizes data security status from Dynamics 365 F&SCM for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons; nothing is posted.

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-manage-data-security
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_manage_data_security',
    "version": '3.0.3',
    "display_name": 'Manage data security Teams Channel Update',
    "description": 'Summarizes data security status from Dynamics 365 F&SCM for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons; nothing is posted.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-manage-data-security',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-manage-data-security',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'cbdd09486be4b4cf',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-system-access-and-security/manage-data-security'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/teams-update-manage-data-security', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'card_filename': 'Output filename for the Adaptive Card JSON, e.g. teams-update-manage-data-security-2026-05-24-card.json.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to summarize, e.g. USMF.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Replaces 'check the spreadsheet' Teams pings with a glanceable card the team can act on directly - reducing back-and-forth and decision latency.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, summarize the current state of manage data security. Produce: (a) a Communications-ready Teams channel post (markdown) with a 2-sentence summary and 3 bullet highlights; (b) an Adaptive Card JSON 'teams-update-manage-data-security-2026-05-24-card.json' showing KPIs, status indicators, and quick-action buttons (e.g., 'View detail', 'Open in D365'). Do not post the card on my behalf - save the artifacts for me to review.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads manage data security, produces a Communications-ready Teams post + an Adaptive Card with quick-action buttons.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Summarizes data security status from Dynamics 365 F&SCM for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons; nothing is posted.', 'example_request': "Draft a Teams update on data security for USMF with an Adaptive Card — save it, don't post.", 'inputs': [{'description': 'D365 legal entity to summarize, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Output filename for the Adaptive Card JSON, e.g. teams-update-manage-data-security-2026-05-24-card.json.', 'name': 'card_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a review-ready Teams update on data security status in D365 F&SCM, drafted as a post plus Adaptive Card, without auto-posting.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class TeamsUpdateManageDataSecurity(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateManageDataSecurity'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'card_filename': {'description': 'Output filename for the Adaptive Card JSON, e.g. teams-update-manage-data-security-2026-05-24-card.json.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to summarize, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(TeamsUpdateManageDataSecurity().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
