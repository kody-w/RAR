---
name: "rar-cowork-cookbook-ppt-exec-analyze-case-patterns"
description: "Generates an executive-ready PowerPoint deck on analyze case patterns status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_analyze_case_patterns", "rar_sha256": "ab63fa1ceab1e723a847e8138dfdd5bffcf22c5cdee58387a65fbe543cd41b00", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "ppt_exec_analyze_case_patterns_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/ppt-exec-analyze-case-patterns:7cbc8e48657fdd7b795dfe83ed36b54d8633999b76e1dff2ef1d0d8aa1681b90", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/ppt_exec_analyze_case_patterns`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `ppt_exec_analyze_case_patterns_agent.py` is
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
