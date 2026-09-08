---
name: "rar-cowork-cookbook-analyze-and-optimize-your-onedrive-at-scale"
description: "Catalogs and categorizes all files in the user's OneDrive, produces a six-screen interactive HTML overview of file disposition, age, relevancy, customer and product, and proposes a reorganization and deletion plan for ap"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/analyze_and_optimize_your_onedrive_at_scale", "rar_sha256": "dc447a65ffb37189aba9879913de5c649e3a9c93468f03500d2f2729fa92bbcb", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "work_management", "advanced", "read_only"]}
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
