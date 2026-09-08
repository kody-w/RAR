---
name: "rar-cowork-cookbook-d365-recipe-planner"
description: "Interviews you across seven discovery points and returns a copy-paste-ready Copilot Cowork prompt for a Dynamics 365 automation plus a predicted cost tier with the factors behind it; planning only, it never runs the reci"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/d365_recipe_planner", "rar_sha256": "e880c6864518da1f2e2a40695f9eed368594591bcc4678b39a92d1b30f78ca77", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt_skill", "other", "administer_to_operate", "beginner", "read_only"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/d365_recipe_planner`. The original RAPP
agent is preserved byte-for-byte in `d365_recipe_planner_agent.py` and in the RCI capsule.

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

D365 Recipe Planner — Interviews you across seven discovery points and returns a copy-paste-ready Copilot Cowork prompt for a Dynamics 365 automation plus a predicted cost tier with the factors behind it; planning only, it never runs the reci

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
  Upstream entry : https://coworkcookbook.com/recipes/d365-recipe-planner
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
    "business_outcome": {
      "description": "The business outcome you want and the process to automate.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "d365_app": {
      "description": "Which D365 surface: Sales, Finance, or ERP/Supply Chain.",
      "type": "string"
    },
    "data_scope_and_frequency": {
      "description": "Data scope (e.g. legal entity, records, date range) and how often it should run.",
      "type": "string"
    },
    "deliverable_format": {
      "description": "Desired output format, e.g. summary, HTML dashboard, or Cookbook .md recipe file.",
      "type": "string"
    },
    "mode": {
      "description": "Read-only versus write-back.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `d365_recipe_planner_agent.py` and embedded as the fenced Python below (sha256 e880c6864518da1f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `d365_recipe_planner_agent.py` first:

```bash
python3 d365_recipe_planner_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 d365_recipe_planner_agent.py   # or on stdin
python3 d365_recipe_planner_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
D365 Recipe Planner — Interviews you across seven discovery points and returns a copy-paste-ready Copilot Cowork prompt for a Dynamics 365 automation plus a predicted cost tier with the factors behind it; planning only, it never runs the reci

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
  Upstream entry : https://coworkcookbook.com/recipes/d365-recipe-planner
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/d365_recipe_planner',
    "version": '3.0.3',
    "display_name": 'D365 Recipe Planner',
    "description": 'Interviews you across seven discovery points and returns a copy-paste-ready Copilot Cowork prompt for a Dynamics 365 automation plus a predicted cost tier with the factors behind it; planning only, it never runs the reci',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt_skill', 'other', 'administer_to_operate', 'beginner', 'read_only'],
    "category": 'general',
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
        "upstream_slug": 'd365-recipe-planner',
        "upstream_url": 'https://coworkcookbook.com/recipes/d365-recipe-planner',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '32c43131c60f330e',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'beginner', 'last_verified_on': '2026-07-28', 'mutates_data': False, 'plugin': 'none', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/administer-system-features/configure-and-manage-copilot-capabilities'], 'recipe_category': 'other', 'recipe_type': 'prompt+skill', 'upstream_path': 'administer-to-operate/d365-recipe-planner', 'uses_skills': {'custom': ['d365-recipe-planner'], 'ootb': [], 'plugin': []}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Copilot Cowork access', 'Prerequisite: Install the d365-recipe-planner skill - either publish it as a Cowork plugin and turn it on under + > Customize, or drop the skill folder at Documents/Cowork/skills/d365-recipe-planner/ in your OneDrive', 'Prerequisite: No Dynamics 365 plugin is required: the planner writes prompts, it does not query D365', 'Prerequisite: Optional: enable a Dynamics 365 Sales or ERP plugin if you want the planner to confirm entity names against your tenant before finalizing a prompt', 'Output matches: A conversational recipe summary, a fenced copy-paste prompt, and a cost tier naming the two to four factors that drove the score. On request, a Cookbook-format `.md` recipe file saved to your Cowork output folder.\n\nThe capture below is a real run. From the brief "keep an eye on overdue customer invoices", the skill produced an **AR Overdue Invoice Monitor** recipe: it identified the surface as D365 Finance via the `dynamics-365-erp` plugin scoped to legal entity USMF, set the mode to read-only, drafted a four-part prompt with lettered deliverable requirements for an interactive HTML aging dashboard, and scored the plan **Medium** — naming the HTML-with-charts deliverable as the largest cost driver.\n\nNote how the drafted prompt tells Cowork to *confirm the exact open-balance entity in the tenant before querying* and to *say what it found instead of guessing* if that entity cannot be confirmed. That is the skill\'s no-fabrication guardrail reaching into the prompts it writes.'], 'confidence': 1.0, 'deliverable': 'A conversational recipe summary, a fenced copy-paste prompt, and a cost tier naming the two to four factors that drove the score. On request, a Cookbook-format `.md` recipe file saved to your Cowork output folder.\n\nThe capture below is a real run. From the brief "keep an eye on overdue customer invoices", the skill produced an **AR Overdue Invoice Monitor** recipe: it identified the surface as D365 Finance via the `dynamics-365-erp` plugin scoped to legal entity USMF, set the mode to read-only, drafted a four-part prompt with lettered deliverable requirements for an interactive HTML aging dashboard, and scored the plan **Medium** — naming the HTML-with-charts deliverable as the largest cost driver.\n\nNote how the drafted prompt tells Cowork to *confirm the exact open-balance entity in the tenant before querying* and to *say what it found instead of guessing* if that entity cannot be confirmed. That is the skill\'s no-fabrication guardrail reaching into the prompts it writes.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'business_outcome': 'The business outcome you want and the process to automate.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'd365_app': 'Which D365 surface: Sales, Finance, or ERP/Supply Chain.', 'data_scope_and_frequency': 'Data scope (e.g. legal entity, records, date range) and how often it should run.', 'deliverable_format': 'Desired output format, e.g. summary, HTML dashboard, or Cookbook .md recipe file.', 'mode': 'Read-only versus write-back.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Lowers the barrier to authoring Cowork automations. A short interview replaces trial-and-error prompt writing, the generated prompt names the correct plugin and scope anchor for the chosen app, and the cost tier tells you what a run commits you to before you make it.', 'expected_output': 'A conversational recipe summary, a fenced copy-paste prompt, and a cost tier naming the two to four factors that drove the score. On request, a Cookbook-format `.md` recipe file saved to your Cowork output folder.\n\nThe capture below is a real run. From the brief "keep an eye on overdue customer invoices", the skill produced an **AR Overdue Invoice Monitor** recipe: it identified the surface as D365 Finance via the `dynamics-365-erp` plugin scoped to legal entity USMF, set the mode to read-only, drafted a four-part prompt with lettered deliverable requirements for an interactive HTML aging dashboard, and scored the plan **Medium** — naming the HTML-with-charts deliverable as the largest cost driver.\n\nNote how the drafted prompt tells Cowork to *confirm the exact open-balance entity in the tenant before querying* and to *say what it found instead of guessing* if that entity cannot be confirmed. That is the skill\'s no-fabrication guardrail reaching into the prompts it writes.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Copilot Cowork access', 'Install the d365-recipe-planner skill - either publish it as a Cowork plugin and turn it on under + > Customize, or drop the skill folder at Documents/Cowork/skills/d365-recipe-planner/ in your OneDrive', 'No Dynamics 365 plugin is required: the planner writes prompts, it does not query D365', 'Optional: enable a Dynamics 365 Sales or ERP plugin if you want the planner to confirm entity names against your tenant before finalizing a prompt'], 'prompt': 'Activate the **D365 Recipe Planner** skill for this conversation. I want to plan a new Dynamics 365 Cowork recipe.\n\nInterview me on the seven discovery points — business outcome, the process to automate, which D365 app (Sales, Finance, or ERP/Supply Chain), deliverable format, read-only versus write-back, data scope, and frequency — then draft a copy-paste-ready Cowork prompt and predict its cost tier with the factors that drove the score.\n\nPlan only. Do not run the recipe or pull any records while we design it.', 'steps': ['Install the skill by whichever route you prefer — publish it as a Cowork plugin, or unzip the package below into `Documents/Cowork/skills/` so the folder lands at `Documents/Cowork/skills/d365-recipe-planner/`.', 'Start a new Cowork task. If you installed it as a plugin, turn it on under **+ > Customize**. If you installed it as a skill folder, Cowork discovers it automatically at the start of each conversation — there is no registration step.', 'Paste the prompt from `prompt.md`, or simply describe what you want to automate; the skill\'s description makes it self-invoking on phrases like "plan a recipe" or "help me automate a D365 task".', 'Answer the discovery questions. If you already have a rich brief, give it up front and the skill will skip ahead.', 'Copy the generated prompt into a **fresh** task to actually run it. The planner deliberately will not execute it for you.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-07-28', 'what_it_does': 'Runs a short discovery interview across seven points — business outcome, process, D365 app, deliverable format, read-only versus write-back, data scope, and frequency — then:\n\n1. Maps the chosen app to the correct Cowork plugin and scope anchor. Finance and ERP/Supply Chain are the same product (F&SCM) and share the `dynamics-365-erp` surface with a **legal entity** scope; Sales is a separate product on Dataverse scoped by **environment**.\n2. Drafts a single copy-paste prompt with an explicit scope line, the data to pull, lettered deliverable requirements, an output location, and guardrails appropriate to read-only versus write-back.\n3. Scores the plan against a seven-factor rubric and reports a low / medium / high cost tier **with the factors that drove it**, plus one suggestion for moving it down a tier.\n4. Optionally saves the result as a Cookbook-format recipe markdown file.\n\nIt plans and drafts only. Its own guardrails forbid pulling, modifying, or creating records — the single live call it permits is a read-only schema lookup to confirm an entity exists.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Interviews you across seven discovery points and returns a copy-paste-ready Copilot Cowork prompt for a Dynamics 365 automation plus a predicted cost tier with the factors behind it; planning only, it never runs the reci', 'example_request': 'Help me plan a D365 recipe to monitor overdue customer invoices in Finance and tell me the cost tier.', 'inputs': [{'description': 'The business outcome you want and the process to automate.', 'name': 'business_outcome'}, {'description': 'Which D365 surface: Sales, Finance, or ERP/Supply Chain.', 'name': 'd365_app'}, {'description': 'Desired output format, e.g. summary, HTML dashboard, or Cookbook .md recipe file.', 'name': 'deliverable_format'}, {'description': 'Read-only versus write-back.', 'name': 'mode'}, {'description': 'Data scope (e.g. legal entity, records, date range) and how often it should run.', 'name': 'data_scope_and_frequency'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you want to plan or draft a Dynamics 365 Cowork recipe prompt and estimate its cost tier before running it in a fresh task.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Install the skill by whichever route you prefer — publish it as a Cowork plugin, or unzip the package below into `Documents/Cowork/skills/` so the folder lands at `Documents/Cowork/skills/d365-recipe-planner/`.', 'Start a new Cowork task. If you installed it as a plugin, turn it on under **+ > Customize**. If you installed it as a skill folder, Cowork discovers it automatically at the start of each conversation — there is no registration step.', 'Paste the prompt from `prompt.md`, or simply describe what you want to automate; the skill\'s description makes it self-invoking on phrases like "plan a recipe" or "help me automate a D365 task".', 'Answer the discovery questions. If you already have a rich brief, give it up front and the skill will skip ahead.', 'Copy the generated prompt into a **fresh** task to actually run it. The planner deliberately will not execute it for you.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class D365RecipePlanner(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'D365RecipePlanner'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'business_outcome': {'description': 'The business outcome you want and the process to automate.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'd365_app': {'description': 'Which D365 surface: Sales, Finance, or ERP/Supply Chain.', 'type': 'string'}, 'data_scope_and_frequency': {'description': 'Data scope (e.g. legal entity, records, date range) and how often it should run.', 'type': 'string'}, 'deliverable_format': {'description': 'Desired output format, e.g. summary, HTML dashboard, or Cookbook .md recipe file.', 'type': 'string'}, 'mode': {'description': 'Read-only versus write-back.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(D365RecipePlanner().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
