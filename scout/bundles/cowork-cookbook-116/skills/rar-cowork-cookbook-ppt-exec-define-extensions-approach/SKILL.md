---
name: "rar-cowork-cookbook-ppt-exec-define-extensions-approach"
description: "Generates an executive-ready PowerPoint deck on define extensions approach status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_define_extensions_approach", "rar_sha256": "cadb23f55eea88f691521ab560889a88da5fe2476e79b52ef82a0b2ca3ad4a10", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_define_extensions_approach`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_define_extensions_approach_agent.py` and in the RCI capsule.

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

Define extensions approach Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on define extensions approach status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-define-extensions-approach
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_define_extensions_approach_agent.py` and embedded as the fenced Python below (sha256 cadb23f55eea88f6…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_define_extensions_approach_agent.py` first:

```bash
python3 ppt_exec_define_extensions_approach_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_define_extensions_approach_agent.py   # or on stdin
python3 ppt_exec_define_extensions_approach_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define extensions approach Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on define extensions approach status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-define-extensions-approach
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_define_extensions_approach',
    "version": '2.0.0',
    "display_name": 'Define extensions approach Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on define extensions approach status, complete with charts and talking-point notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-define-extensions-approach',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-define-extensions-approach',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'fa922bffff553dd1',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/implement-solutions/define-extensions-approach'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/ppt-exec-define-extensions-approach', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class PptExecDefineExtensionsApproach(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecDefineExtensionsApproach'
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
    print(PptExecDefineExtensionsApproach().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
