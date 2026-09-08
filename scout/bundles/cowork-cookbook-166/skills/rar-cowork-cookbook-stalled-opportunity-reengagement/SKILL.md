---
name: "rar-cowork-cookbook-stalled-opportunity-reengagement"
description: "Builds a read-only re-engagement list of your open, owner-assigned Dynamics 365 Sales opportunities with no activity beyond a dormancy threshold, returning an Excel workbook and a Teams-ready summary."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/stalled_opportunity_reengagement", "rar_sha256": "17f32191335095eaf9ba2f912ebf6a89d1a43d84ac5cc258b07d7f5b9f6bdf10", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "prospect_to_quote", "intermediate", "integration", "dynamics_365_sales"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/stalled_opportunity_reengagement`. The original RAPP
agent is preserved byte-for-byte in `stalled_opportunity_reengagement_agent.py` and in the RCI capsule.

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

Stalled Opportunity Re-Engagement List — Builds a read-only re-engagement list of your open, owner-assigned Dynamics 365 Sales opportunities with no activity beyond a dormancy threshold, returning an Excel workbook and a Teams-ready summary.

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
  Upstream entry : https://coworkcookbook.com/recipes/stalled-opportunity-reengagement
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
    "dormancy_threshold_days": {
      "description": "Days without activity before an opportunity counts as stalled; defaults to 45.",
      "type": "string"
    },
    "dynamics_environment": {
      "description": "The Dynamics 365 Sales environment the plugin is bound to for analysis.",
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
    "output_workbook_name": {
      "description": "Excel file name for the results; defaults to 'stalled-opportunities.xlsx'.",
      "type": "string"
    },
    "owner": {
      "description": "The opportunity owner to filter on \u2014 the requesting user.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `stalled_opportunity_reengagement_agent.py` and embedded as the fenced Python below (sha256 17f32191335095ea…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `stalled_opportunity_reengagement_agent.py` first:

```bash
python3 stalled_opportunity_reengagement_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 stalled_opportunity_reengagement_agent.py   # or on stdin
python3 stalled_opportunity_reengagement_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Stalled Opportunity Re-Engagement List — Builds a read-only re-engagement list of your open, owner-assigned Dynamics 365 Sales opportunities with no activity beyond a dormancy threshold, returning an Excel workbook and a Teams-ready summary.

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
  Upstream entry : https://coworkcookbook.com/recipes/stalled-opportunity-reengagement
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/stalled_opportunity_reengagement',
    "version": '3.0.3',
    "display_name": 'Stalled Opportunity Re-Engagement List',
    "description": 'Builds a read-only re-engagement list of your open, owner-assigned Dynamics 365 Sales opportunities with no activity beyond a dormancy threshold, returning an Excel workbook and a Teams-ready summary.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'other', 'prospect_to_quote', 'intermediate', 'integration', 'dynamics_365_sales'],
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
        "upstream_slug": 'stalled-opportunity-reengagement',
        "upstream_url": 'https://coworkcookbook.com/recipes/stalled-opportunity-reengagement',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '2609271644f74e10',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-sales', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/pursue-opportunities/nurture-opportunities-and-finalize-the-sale'], 'recipe_category': 'other', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/stalled-opportunity-reengagement', 'uses_skills': {'custom': [], 'ootb': ['Excel', 'Communications'], 'plugin': [{'action': 'search', 'plugin': 'dynamics-365-sales'}, {'action': 'describe', 'plugin': 'dynamics-365-sales'}, {'action': 'read_query', 'plugin': 'dynamics-365-sales'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: A Dynamics 365 Sales licence and access to a Dynamics 365 Sales environment', 'Prerequisite: The Dynamics 365 Sales plugin enabled in your Cowork session (+ > Customize > Dynamics 365 Sales)', 'Prerequisite: The plugin bound to the environment you want to analyze (gear icon on the plugin tile)', "Output matches: A two-sheet workbook plus a short paragraph you can paste into Teams. Each detail row carries a\nconcrete re-engagement angle drawn from that opportunity's own history."], 'confidence': 1.0, 'deliverable': "A two-sheet workbook plus a short paragraph you can paste into Teams. Each detail row carries a\nconcrete re-engagement angle drawn from that opportunity's own history.", 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'dormancy_threshold_days': 'Days without activity before an opportunity counts as stalled; defaults to 45.', 'dynamics_environment': 'The Dynamics 365 Sales environment the plugin is bound to for analysis.', 'output_workbook_name': "Excel file name for the results; defaults to 'stalled-opportunities.xlsx'.", 'owner': 'The opportunity owner to filter on — the requesting user.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Recovers pipeline that would otherwise age out silently. Instead of a generic 'check in' sweep, each dormant deal gets a next step informed by its stage, value, and what happened last.", 'expected_output': "A two-sheet workbook plus a short paragraph you can paste into Teams. Each detail row carries a\nconcrete re-engagement angle drawn from that opportunity's own history.", 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['A Dynamics 365 Sales licence and access to a Dynamics 365 Sales environment', 'The Dynamics 365 Sales plugin enabled in your Cowork session (+ > Customize > Dynamics 365 Sales)', 'The plugin bound to the environment you want to analyze (gear icon on the plugin tile)'], 'prompt': "Using the Dynamics 365 Sales plugin, build a re-engagement list for my stalled opportunities.\n\nUse search and describe first to confirm the opportunity table, the activity or task tables\nrelated to it, and the columns for owner, status, estimated value, sales stage, and the most\nrecent activity or modification date. Do not guess table or column names.\n\nBefore filtering by date, run a read_query to find the actual range of activity dates available,\nand report it. Then treat an opportunity as stalled when it is open, I am the owner, and there\nhas been no activity for longer than 45 days — or the closest equivalent your data supports,\nwhich you should state.\n\nFor each stalled opportunity, summarize: the last thing that happened, how long it has been\ndormant, the estimated value, and the current stage. Then suggest one specific re-engagement\nangle grounded in that record — not a generic follow-up.\n\nProduce an Excel workbook 'stalled-opportunities.xlsx' with a Summary sheet (count and value by\ndormancy band) and a Detail sheet with one row per opportunity including your suggested angle.\nAlso give me a short Teams-ready paragraph summarizing the top three by value.\n\nDo not modify any data, and do not send anything to anyone. If nothing is stalled, say so and\nstop.", 'steps': ['Confirm the **Dynamics 365 Sales** plugin is on and bound to the right environment.', 'Paste the prompt from `prompt.md` and send it.', 'Check the reported activity-date range — if it looks short, your activity tracking may not', 'Tune the 45-day dormancy threshold to your sales cycle.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Correlates opportunities with their activity history to find dormancy, then produces both a\nworking list and a shareable summary. Read-only; drafts nothing into your CRM.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only re-engagement list of your open, owner-assigned Dynamics 365 Sales opportunities with no activity beyond a dormancy threshold, returning an Excel workbook and a Teams-ready summary.', 'example_request': 'Build my stalled opportunity re-engagement list from Dynamics 365 Sales using a 45-day dormancy cutoff.', 'inputs': [{'description': 'The Dynamics 365 Sales environment the plugin is bound to for analysis.', 'name': 'dynamics_environment'}, {'description': 'The opportunity owner to filter on — the requesting user.', 'name': 'owner'}, {'description': 'Days without activity before an opportunity counts as stalled; defaults to 45.', 'name': 'dormancy_threshold_days'}, {'description': "Excel file name for the results; defaults to 'stalled-opportunities.xlsx'.", 'name': 'output_workbook_name'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you want to find stalled open opportunities you own in Dynamics 365 Sales and get a per-deal re-engagement angle, workbook, and short summary.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Confirm the **Dynamics 365 Sales** plugin is on and bound to the right environment.', 'Paste the prompt from `prompt.md` and send it.', 'Check the reported activity-date range — if it looks short, your activity tracking may not', 'Tune the 45-day dormancy threshold to your sales cycle.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class StalledOpportunityReengagement(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'StalledOpportunityReengagement'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'dormancy_threshold_days': {'description': 'Days without activity before an opportunity counts as stalled; defaults to 45.', 'type': 'string'}, 'dynamics_environment': {'description': 'The Dynamics 365 Sales environment the plugin is bound to for analysis.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_workbook_name': {'description': "Excel file name for the results; defaults to 'stalled-opportunities.xlsx'.", 'type': 'string'}, 'owner': {'description': 'The opportunity owner to filter on — the requesting user.', 'type': 'string'}},
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
    print(StalledOpportunityReengagement().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
