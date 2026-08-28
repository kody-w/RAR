---
name: "rar-cowork-cookbook-analyze-and-optimize-your-onedrive-at-scale"
description: "Turn a sprawling OneDrive into a structured catalog you can actually act on."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/analyze_and_optimize_your_onedrive_at_scale", "rar_sha256": "cde6df9da0973b3b0e0482eddcd4521ca5b1e33a1d3701ec7ff0cd552170fd14", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "work_management", "advanced", "read_only"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `analyze_and_optimize_your_onedrive_at_scale_agent.py` and embedded as the fenced Python below (sha256 cde6df9da0973b3b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `analyze_and_optimize_your_onedrive_at_scale_agent.py` first:

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
    "version": '2.0.0',
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
