---
name: "rar-cowork-cookbook-ppt-exec-analyze-case-patterns"
description: "Generates an executive-ready PowerPoint deck on analyze case patterns status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_analyze_case_patterns", "rar_sha256": "ab63fa1ceab1e723a847e8138dfdd5bffcf22c5cdee58387a65fbe543cd41b00", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_analyze_case_patterns`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_analyze_case_patterns_agent.py` and in the RCI capsule.

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

Analyze case patterns Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on analyze case patterns status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-analyze-case-patterns
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
      "description": "The process to automate.",
      "type": "string"
    },
    "trigger": {
      "description": "Optional. What starts it \u2014 schedule, event or manual.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_analyze_case_patterns_agent.py` and embedded as the fenced Python below (sha256 ab63fa1ceab1e723…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_analyze_case_patterns_agent.py` first:

```bash
python3 ppt_exec_analyze_case_patterns_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_analyze_case_patterns_agent.py   # or on stdin
python3 ppt_exec_analyze_case_patterns_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Analyze case patterns Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on analyze case patterns status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-analyze-case-patterns
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_analyze_case_patterns',
    "version": '2.0.0',
    "display_name": 'Analyze case patterns Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on analyze case patterns status, complete with charts and talking-point notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'case_to_resolution', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-analyze-case-patterns',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-analyze-case-patterns',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'd078a0148c0ac232',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/analyze-case-performance/analyze-case-patterns'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/ppt-exec-analyze-case-patterns', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.5, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class PptExecAnalyzeCasePatterns(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecAnalyzeCasePatterns'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'The process to automate.', 'type': 'string'}, 'trigger': {'description': 'Optional. What starts it — schedule, event or manual.', 'type': 'string'}},
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
    print(PptExecAnalyzeCasePatterns().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
