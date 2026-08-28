---
name: "rar-cowork-cookbook-ppt-exec-analyze-case-patterns"
description: "Generates an executive-ready PowerPoint deck on analyze case patterns status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_analyze_case_patterns", "rar_sha256": "fca2cdf882539664cbd21a266cba51f842531f07480d3497509cb93ee68375d8", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_analyze_case_patterns_agent.py` and embedded as the fenced Python below (sha256 fca2cdf882539664…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_analyze_case_patterns_agent.py` first:

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
    "version": '2.0.1',
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
