---
name: "rar-cowork-cookbook-teams-update-manage-data-security"
description: "Summarizes data security status from Dynamics 365 F&SCM for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons; nothing is posted."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_manage_data_security", "rar_sha256": "04b74ef826b62b4c77f1d9f9cf7dce52dfdda6da80d30ea00c05ade9e8b66403", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
