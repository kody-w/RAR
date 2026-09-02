---
name: "rar-cowork-cookbook-analyze-and-optimize-your-onedrive-at-scale"
description: "Turn a sprawling OneDrive into a structured catalog you can actually act on."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/analyze_and_optimize_your_onedrive_at_scale", "rar_sha256": "cde6df9da0973b3b0e0482eddcd4521ca5b1e33a1d3701ec7ff0cd552170fd14", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "analyze_and_optimize_your_onedrive_at_scale_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/analyze-and-optimize-your-onedrive-at-scale:f5ab595c48cfe56cd428c3bc62fd10d4a409e5d1d8432d1106afdf001457817d", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "work_management", "advanced", "read_only"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/analyze_and_optimize_your_onedrive_at_scale`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `analyze_and_optimize_your_onedrive_at_scale_agent.py` is
retained temporarily as a byte-exact rollback backup.

When Scout can execute local files, resolve this skill directory and run:

```bash
python3 scripts/run_agent.py --preflight
echo '{}' | python3 scripts/run_agent.py
```

Pass the real JSON arguments instead of `{}`. The runner verifies the
`SKILL.md` and agent checksums, prefers the rollback backup while it exists,
and otherwise executes the exact vaulted agent bytes directly from the Grail
record. If preflight reports a host dependency that Scout cannot satisfy, use
the `brainstem_chat` MCP tool to run the canonical agent in the user's
Brainstem. Never paraphrase the factory or agent into a new implementation.

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
