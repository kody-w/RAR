---
name: "rar-cowork-cookbook-stalled-opportunity-reengagement"
description: "Builds a read-only re-engagement list of your open, owner-assigned Dynamics 365 Sales opportunities with no activity beyond a dormancy threshold, returning an Excel workbook and a Teams-ready summary."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/stalled_opportunity_reengagement", "rar_sha256": "17f32191335095eaf9ba2f912ebf6a89d1a43d84ac5cc258b07d7f5b9f6bdf10", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "prospect_to_quote", "intermediate", "integration", "dynamics_365_sales"]}
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
