---
name: "rar-cowork-cookbook-ppt-exec-define-extensions-approach"
description: "Generates an executive-ready PowerPoint deck on define extensions approach status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_define_extensions_approach", "rar_sha256": "cadb23f55eea88f691521ab560889a88da5fe2476e79b52ef82a0b2ca3ad4a10", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "ppt_exec_define_extensions_approach_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/ppt-exec-define-extensions-approach:f2d9dc0ff09d096093d916aac1d67bc7fdd7b61f5a2202a6665fb7c1fc3cfc45", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/ppt_exec_define_extensions_approach`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `ppt_exec_define_extensions_approach_agent.py` is
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
