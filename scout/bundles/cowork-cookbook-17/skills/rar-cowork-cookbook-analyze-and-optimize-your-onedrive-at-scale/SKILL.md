---
name: "rar-cowork-cookbook-analyze-and-optimize-your-onedrive-at-scale"
description: "Turn a sprawling OneDrive into a structured catalog you can actually act on."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/analyze_and_optimize_your_onedrive_at_scale", "rar_sha256": "8b1b2e9e5d4de92ac49c51ab33788fabfa6496c362a5b374bdf0ff3b9c84c480", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "work_management", "advanced", "read_only"]}
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

Analyze and optimize your OneDrive at scale — Turn a sprawling OneDrive into a structured catalog you can actually act on.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a analyze capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

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
    "data_source": {
      "description": "Optional. Where the evidence comes from.",
      "type": "string"
    },
    "operation": {
      "description": "What to do: run, plan, checklist, describe.",
      "enum": [
        "run",
        "plan",
        "checklist",
        "describe"
      ],
      "type": "string"
    },
    "subject": {
      "description": "The question to answer, stated as a question.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `analyze_and_optimize_your_onedrive_at_scale_agent.py` and embedded as the fenced Python below (sha256 8b1b2e9e5d4de92a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `analyze_and_optimize_your_onedrive_at_scale_agent.py` first:

```bash
python3 analyze_and_optimize_your_onedrive_at_scale_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 analyze_and_optimize_your_onedrive_at_scale_agent.py   # or on stdin
python3 analyze_and_optimize_your_onedrive_at_scale_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Analyze and optimize your OneDrive at scale — Turn a sprawling OneDrive into a structured catalog you can actually act on.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a analyze capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

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
    "version": '2.0.1',
    "display_name": 'Analyze and optimize your OneDrive at scale',
    "description": 'Turn a sprawling OneDrive into a structured catalog you can actually act on.',
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
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'c0e09e99d98ca30f',
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


# The toasted capability. The upstream entry supplies the WHAT; this procedure
# is RAR's own method for that shape of work, generated by
# @kody-w/skill_toaster_agent from the metadata we hold. No upstream text is
# reproduced here — see the module docstring.
_SPEC = {'archetype': 'analyze', 'checks': ['The question is falsifiable and answered directly.', 'The decision threshold was stated before the result.', 'Missing evidence is named rather than silently excluded.', 'Uncertainty is quantified.'], 'confidence': 0.5, 'deliverable': 'A decision-grade answer: one-sentence verdict, method, evidence, uncertainty, and what would change the conclusion.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'data_source': 'Optional. Where the evidence comes from.', 'subject': 'The question to answer, stated as a question.'}, 'refined_by': 'rules', 'signals': ['word:analyze'], 'steps': ["Restate the question so it is falsifiable. 'Is X better?' becomes 'Does X reduce Y by more than Z?'", 'Declare in advance what result would change the decision — this is what separates analysis from justification.', 'Identify the evidence available and, explicitly, the evidence that is missing.', 'Compute the comparison, holding the method constant across every option.', 'Quantify uncertainty. A point estimate with no interval invites false confidence.', 'Answer the original question in one sentence, then show the working beneath it.'], 'subject_label': 'question under analysis', 'verb': 'Analyze'}


class AnalyzeAndOptimizeYourOnedriveAtScale(BasicAgent):
    """Analyze agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AnalyzeAndOptimizeYourOnedriveAtScale'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'data_source': {'description': 'Optional. Where the evidence comes from.', 'type': 'string'}, 'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'The question to answer, stated as a question.', 'type': 'string'}},
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

    # ── entry point ─────────────────────────────────────────────────────

    def perform(self, **kwargs):
        """Run the toasted capability. Always returns a string."""
        op = str(kwargs.get("operation") or "run").strip().lower()
        subject = self._subject(kwargs)

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
