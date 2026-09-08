---
name: "rar-cowork-cookbook-win-loss-theme-analysis"
description: "Analyzes closed won and lost opportunities in a bound Dynamics 365 Sales environment and returns win rates, ranked win/loss reasons, competitor and stage patterns, plus an Excel workbook and a short deck."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/win_loss_theme_analysis", "rar_sha256": "bd9f4823e2de1f8221a8f3a2a4d2d5764fd7cc3993bb10d639e854bbc11a8bb3", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "prospect_to_quote", "advanced", "integration", "dynamics_365_sales"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/win_loss_theme_analysis`. The original RAPP
agent is preserved byte-for-byte in `win_loss_theme_analysis_agent.py` and in the RCI capsule.

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

Win/Loss Theme Analysis — Analyzes closed won and lost opportunities in a bound Dynamics 365 Sales environment and returns win rates, ranked win/loss reasons, competitor and stage patterns, plus an Excel workbook and a short deck.

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
  Upstream entry : https://coworkcookbook.com/recipes/win-loss-theme-analysis
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
    "analysis_window": {
      "description": "Close-date window to analyze; defaults to the most recent twelve months of available data.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "environment_binding": {
      "description": "The Dynamics 365 Sales environment the plugin is bound to for the analysis.",
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
    "ownership_scope": {
      "description": "Whose opportunities to include \u2014 the caller and their team.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `win_loss_theme_analysis_agent.py` and embedded as the fenced Python below (sha256 bd9f4823e2de1f82…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `win_loss_theme_analysis_agent.py` first:

```bash
python3 win_loss_theme_analysis_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 win_loss_theme_analysis_agent.py   # or on stdin
python3 win_loss_theme_analysis_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Win/Loss Theme Analysis — Analyzes closed won and lost opportunities in a bound Dynamics 365 Sales environment and returns win rates, ranked win/loss reasons, competitor and stage patterns, plus an Excel workbook and a short deck.

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
  Upstream entry : https://coworkcookbook.com/recipes/win-loss-theme-analysis
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/win_loss_theme_analysis',
    "version": '3.0.3',
    "display_name": 'Win/Loss Theme Analysis',
    "description": 'Analyzes closed won and lost opportunities in a bound Dynamics 365 Sales environment and returns win rates, ranked win/loss reasons, competitor and stage patterns, plus an Excel workbook and a short deck.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'other', 'prospect_to_quote', 'advanced', 'integration', 'dynamics_365_sales'],
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
        "upstream_slug": 'win-loss-theme-analysis',
        "upstream_url": 'https://coworkcookbook.com/recipes/win-loss-theme-analysis',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '5554f90f362782df',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'advanced', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-sales', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/analyze-sales/provide-insights-into-sales-strategies-and-performance'], 'recipe_category': 'other', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/win-loss-theme-analysis', 'uses_skills': {'custom': [], 'ootb': ['Excel', 'PowerPoint'], 'plugin': [{'action': 'search', 'plugin': 'dynamics-365-sales'}, {'action': 'describe', 'plugin': 'dynamics-365-sales'}, {'action': 'read_query', 'plugin': 'dynamics-365-sales'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: A Dynamics 365 Sales licence and access to a Dynamics 365 Sales environment', 'Prerequisite: The Dynamics 365 Sales plugin enabled in your Cowork session (+ > Customize > Dynamics 365 Sales)', 'Prerequisite: The plugin bound to the environment you want to analyze (gear icon on the plugin tile)', 'Output matches: A multi-sheet workbook plus a short deck. Where loss reasons are poorly populated, expect Cowork\nto say so directly rather than over-reading a thin field.'], 'confidence': 1.0, 'deliverable': 'A multi-sheet workbook plus a short deck. Where loss reasons are poorly populated, expect Cowork\nto say so directly rather than over-reading a thin field.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'analysis_window': 'Close-date window to analyze; defaults to the most recent twelve months of available data.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'environment_binding': 'The Dynamics 365 Sales environment the plugin is bound to for the analysis.', 'ownership_scope': 'Whose opportunities to include — the caller and their team.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Converts loss reasons from a field nobody reads into a ranked list of what is actually costing deals, which is what makes enablement and product feedback specific enough to act on.', 'expected_output': 'A multi-sheet workbook plus a short deck. Where loss reasons are poorly populated, expect Cowork\nto say so directly rather than over-reading a thin field.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['A Dynamics 365 Sales licence and access to a Dynamics 365 Sales environment', 'The Dynamics 365 Sales plugin enabled in your Cowork session (+ > Customize > Dynamics 365 Sales)', 'The plugin bound to the environment you want to analyze (gear icon on the plugin tile)'], 'prompt': "Using the Dynamics 365 Sales plugin, analyze themes across my team's won and lost opportunities.\n\nUse search and describe to confirm the opportunity table and the columns for status, status\nreason, win or loss reason, competitor if tracked, estimated and actual value, sales stage at\nclose, close date, and owner. Report which of these your environment does not carry.\n\nRun a read_query to find the range of close dates available and report it. Choose an analysis\nwindow inside that range — prefer the most recent twelve months of real data — and state your\nchoice.\n\nScope to opportunities owned by me or my team. Then report:\n- win rate by count and by value\n- the ranked distribution of loss reasons, with total value attached to each\n- the ranked distribution of win reasons where recorded\n- competitor involvement where tracked, and the win rate against each\n- the stage at which lost deals typically died\n- whether outcomes differ by deal value band\n\nRead any free-text loss notes available and group them into recurring themes, quoting a short\nrepresentative example for each. Say how many records supported each theme so I can judge\nwhether it is signal.\n\nProduce an Excel workbook 'win-loss-analysis.xlsx' with a sheet per section above, and a short\nPowerPoint deck 'win-loss-summary.pptx' of no more than six slides covering the headline\nfindings.\n\nDo not modify any data. If there are too few closed opportunities in the window to support\nconclusions, say so and report only what the data can carry.", 'steps': ['Confirm the **Dynamics 365 Sales** plugin is on and bound to the right environment.', 'Paste the prompt from `prompt.md` and send it.', 'Check the record count behind each theme before quoting it anywhere — a theme supported by'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Combines structured reason-code analysis with theme extraction from free-text notes, and\nattaches record counts to every theme so weak signals are visible as weak.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Analyzes closed won and lost opportunities in a bound Dynamics 365 Sales environment and returns win rates, ranked win/loss reasons, competitor and stage patterns, plus an Excel workbook and a short deck.', 'example_request': "Analyze win/loss themes across my team's closed opportunities from the last year and give me the workbook and deck.", 'inputs': [{'description': 'The Dynamics 365 Sales environment the plugin is bound to for the analysis.', 'name': 'environment_binding'}, {'description': 'Whose opportunities to include — the caller and their team.', 'name': 'ownership_scope'}, {'description': 'Close-date window to analyze; defaults to the most recent twelve months of available data.', 'name': 'analysis_window'}], 'model': 'claude-opus-5', 'when_to_use': "Call when a sales user wants recurring win/loss themes across their team's closed Dynamics 365 opportunities, read-only, with workbook and deck output."}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Confirm the **Dynamics 365 Sales** plugin is on and bound to the right environment.', 'Paste the prompt from `prompt.md` and send it.', 'Check the record count behind each theme before quoting it anywhere — a theme supported by'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class WinLossThemeAnalysis(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'WinLossThemeAnalysis'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'analysis_window': {'description': 'Close-date window to analyze; defaults to the most recent twelve months of available data.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'environment_binding': {'description': 'The Dynamics 365 Sales environment the plugin is bound to for the analysis.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'ownership_scope': {'description': 'Whose opportunities to include — the caller and their team.', 'type': 'string'}},
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
    print(WinLossThemeAnalysis().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
