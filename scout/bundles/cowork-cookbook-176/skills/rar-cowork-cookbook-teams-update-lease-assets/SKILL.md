---
name: "rar-cowork-cookbook-teams-update-lease-assets"
description: "Summarizes lease asset status from the Dynamics 365 ERP plugin for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons; does not post a"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_lease_assets", "rar_sha256": "73d1064545cd17b7c25099923e32d92bb553464c940a9a26e7c6988992a7a05b", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_lease_assets`. The original RAPP
agent is preserved byte-for-byte in `teams_update_lease_assets_agent.py` and in the RCI capsule.

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

Lease assets Teams Channel Update — Summarizes lease asset status from the Dynamics 365 ERP plugin for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons; does not post a

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-lease-assets
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
      "description": "Filename for the Adaptive Card JSON, e.g. teams-update-lease-assets-2026-05-24-card.json.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to summarize lease assets for (e.g., USMF).",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_lease_assets_agent.py` and embedded as the fenced Python below (sha256 73d1064545cd17b7…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_lease_assets_agent.py` first:

```bash
python3 teams_update_lease_assets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_lease_assets_agent.py   # or on stdin
python3 teams_update_lease_assets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Lease assets Teams Channel Update — Summarizes lease asset status from the Dynamics 365 ERP plugin for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons; does not post a

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-lease-assets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_lease_assets',
    "version": '3.0.3',
    "display_name": 'Lease assets Teams Channel Update',
    "description": 'Summarizes lease asset status from the Dynamics 365 ERP plugin for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons; does not post a',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'acquire_to_dispose', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-lease-assets',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-lease-assets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '9dcb5003f6db7fe1',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-06-01', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/acquire-assets/lease-assets'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/teams-update-lease-assets', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'card_filename': 'Filename for the Adaptive Card JSON, e.g. teams-update-lease-assets-2026-05-24-card.json.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to summarize lease assets for (e.g., USMF).'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Replaces 'check the spreadsheet' Teams pings with a glanceable card the team can act on directly - reducing back-and-forth and decision latency.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, summarize the current state of lease assets. Produce: (a) a Communications-ready Teams channel post (markdown) with a 2-sentence summary and 3 bullet highlights; (b) an Adaptive Card JSON 'teams-update-lease-assets-2026-05-24-card.json' showing KPIs, status indicators, and quick-action buttons (e.g., 'View detail', 'Open in D365'). Do not post the card on my behalf - save the artifacts for me to review.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-06-01', 'what_it_does': 'Reads lease assets, produces a Communications-ready Teams post + an Adaptive Card with quick-action buttons.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Summarizes lease asset status from the Dynamics 365 ERP plugin for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons; does not post a', 'example_request': "Draft a Teams channel post and Adaptive Card on lease assets status for USMF — don't post it, just save the files.", 'inputs': [{'description': 'D365 legal entity to summarize lease assets for (e.g., USMF).', 'name': 'legal_entity'}, {'description': 'Filename for the Adaptive Card JSON, e.g. teams-update-lease-assets-2026-05-24-card.json.', 'name': 'card_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a review-ready Teams channel update on lease assets from D365 F&SCM, with an Adaptive Card saved for manual posting.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class TeamsUpdateLeaseAssets(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateLeaseAssets'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'card_filename': {'description': 'Filename for the Adaptive Card JSON, e.g. teams-update-lease-assets-2026-05-24-card.json.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to summarize lease assets for (e.g., USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(TeamsUpdateLeaseAssets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
