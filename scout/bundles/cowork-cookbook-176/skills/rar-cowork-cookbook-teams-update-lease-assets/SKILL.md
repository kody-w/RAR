---
name: "rar-cowork-cookbook-teams-update-lease-assets"
description: "Summarizes lease asset status from the Dynamics 365 ERP plugin for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons; does not post a"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_lease_assets", "rar_sha256": "73d1064545cd17b7c25099923e32d92bb553464c940a9a26e7c6988992a7a05b", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
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
