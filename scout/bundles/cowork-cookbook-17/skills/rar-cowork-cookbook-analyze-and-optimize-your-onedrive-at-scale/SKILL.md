---
name: "rar-cowork-cookbook-analyze-and-optimize-your-onedrive-at-scale"
description: "Catalogs and categorizes all files in the user's OneDrive, produces a six-screen interactive HTML overview of file disposition, age, relevancy, customer and product, and proposes a reorganization and deletion plan for ap"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/analyze_and_optimize_your_onedrive_at_scale", "rar_sha256": "dc447a65ffb37189aba9879913de5c649e3a9c93468f03500d2f2729fa92bbcb", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "work_management", "advanced", "read_only"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/analyze_and_optimize_your_onedrive_at_scale`. The original RAPP
agent is preserved byte-for-byte in `analyze_and_optimize_your_onedrive_at_scale_agent.py` and in the RCI capsule.

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

Analyze and optimize your OneDrive at scale — Catalogs and categorizes all files in the user's OneDrive, produces a six-screen interactive HTML overview of file disposition, age, relevancy, customer and product, and proposes a reorganization and deletion plan for ap

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
  Upstream entry : https://coworkcookbook.com/recipes/analyze-and-optimize-your-onedrive-at-scale
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `analyze_and_optimize_your_onedrive_at_scale_agent.py` and embedded as the fenced Python below (sha256 dc447a65ffb37189…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `analyze_and_optimize_your_onedrive_at_scale_agent.py` first:

```bash
python3 analyze_and_optimize_your_onedrive_at_scale_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 analyze_and_optimize_your_onedrive_at_scale_agent.py   # or on stdin
python3 analyze_and_optimize_your_onedrive_at_scale_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Analyze and optimize your OneDrive at scale — Catalogs and categorizes all files in the user's OneDrive, produces a six-screen interactive HTML overview of file disposition, age, relevancy, customer and product, and proposes a reorganization and deletion plan for ap

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
  Upstream entry : https://coworkcookbook.com/recipes/analyze-and-optimize-your-onedrive-at-scale
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/analyze_and_optimize_your_onedrive_at_scale',
    "version": '3.0.2',
    "display_name": 'Analyze and optimize your OneDrive at scale',
    "description": "Catalogs and categorizes all files in the user's OneDrive, produces a six-screen interactive HTML overview of file disposition, age, relevancy, customer and product, and proposes a reorganization and deletion plan for ap",
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'other', 'work_management', 'advanced', 'read_only'],
    "category": 'general',
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
        "upstream_slug": 'analyze-and-optimize-your-onedrive-at-scale',
        "upstream_url": 'https://coworkcookbook.com/recipes/analyze-and-optimize-your-onedrive-at-scale',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'a282f3bd0b80e854',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'advanced', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'none', 'process_roots': ['work-management'], 'process_tags': ['work-management/organize-information/catalog-and-clean-up-file-stores'], 'recipe_category': 'other', 'recipe_type': 'prompt', 'upstream_path': 'work-management/analyze-and-optimize-your-onedrive-at-scale', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint'], 'plugin': []}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Microsoft 365 Copilot licence with access to Cowork', 'Output matches: An organization plan and visual overview of your files - with cleanup decisions queued up for your approval.'], 'confidence': 1.0, 'deliverable': 'An organization plan and visual overview of your files - with cleanup decisions queued up for your approval.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Turn a sprawling OneDrive into a structured catalog you can actually act on. An organization plan and visual overview of your files - with cleanup decisions queued up for your approval.', 'expected_output': 'An organization plan and visual overview of your files - with cleanup decisions queued up for your approval.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Microsoft 365 Copilot licence with access to Cowork'], 'prompt': 'Analyze my OneDrive. Catalog and categorize all of the files.\n\nCreate a dynamic HTML presentation showing the disposition of the files, age, relevancy, customer, product etc. The presentation should be no more than five scrolling screens with an executive overview with animated interactivity. The sixth screen should be recommendations.\n\nCreate a plan to optimize my files and reorganize them. The plan should include folders and files to delete which you will rename by prepending the original name with "Delete_" and place them all into a Delete folder.\n\nPresent me with your plan before you act on it.', 'steps': ['Open Cowork and start a new task.', 'Paste the prompt from `prompt.md`, replacing anything in square brackets with your own values.', 'Review the plan Cowork proposes before letting it run.', 'Check any drafted email or calendar change before approving it — the prompt holds them for review rather than sending.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'An organization plan and visual overview of your files - with cleanup decisions queued up for your approval.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Catalogs and categorizes all files in the user's OneDrive, produces a six-screen interactive HTML overview of file disposition, age, relevancy, customer and product, and proposes a reorganization and deletion plan for ap", 'example_request': 'Analyze my OneDrive, categorize everything, and show me a cleanup and reorg plan before you touch anything.', 'inputs': [], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants their OneDrive analyzed, cataloged, visualized, and a cleanup/reorg plan proposed for review before any files are renamed or moved.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and start a new task.', 'Paste the prompt from `prompt.md`, replacing anything in square brackets with your own values.', 'Review the plan Cowork proposes before letting it run.', 'Check any drafted email or calendar change before approving it — the prompt holds them for review rather than sending.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AnalyzeAndOptimizeYourOnedriveAtScale(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AnalyzeAndOptimizeYourOnedriveAtScale'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(AnalyzeAndOptimizeYourOnedriveAtScale().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
