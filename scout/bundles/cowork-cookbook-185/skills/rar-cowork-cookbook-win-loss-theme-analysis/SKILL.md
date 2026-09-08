---
name: "rar-cowork-cookbook-win-loss-theme-analysis"
description: "Analyzes closed won and lost opportunities in a bound Dynamics 365 Sales environment and returns win rates, ranked win/loss reasons, competitor and stage patterns, plus an Excel workbook and a short deck."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/win_loss_theme_analysis", "rar_sha256": "bd9f4823e2de1f8221a8f3a2a4d2d5764fd7cc3993bb10d639e854bbc11a8bb3", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "prospect_to_quote", "advanced", "integration", "dynamics_365_sales"]}
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
