---
name: "rar-cowork-cookbook-ppt-exec-define-leasing-policies"
description: "Generates an executive-ready PowerPoint deck on define leasing policies status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_define_leasing_policies", "rar_sha256": "da9703edf5623dd4a9054fb4fc79041072329aae6a6285f0aaafa77e7ea1c2ca", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "ppt_exec_define_leasing_policies_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/ppt-exec-define-leasing-policies:f907f0eb8efa6d7cd2c008165c6fdbd518407749e32cdd639336b6e6fd2fca2c", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/ppt_exec_define_leasing_policies`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `ppt_exec_define_leasing_policies_agent.py` is
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

Define leasing policies Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on define leasing policies status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-define-leasing-policies
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_define_leasing_policies_agent.py` and embedded as the fenced Python below (sha256 da9703edf5623dd4…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_define_leasing_policies_agent.py` first:

```bash
python3 ppt_exec_define_leasing_policies_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_define_leasing_policies_agent.py   # or on stdin
python3 ppt_exec_define_leasing_policies_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define leasing policies Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on define leasing policies status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-define-leasing-policies
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_define_leasing_policies',
    "version": '2.0.0',
    "display_name": 'Define leasing policies Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on define leasing policies status, complete with charts and talking-point notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'acquire_to_dispose', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'verified',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'ppt-exec-define-leasing-policies',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-define-leasing-policies',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'cd8b7dd3d584d5d3',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/define-asset-strategy/define-leasing-policies'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/ppt-exec-define-leasing-policies', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class PptExecDefineLeasingPolicies(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecDefineLeasingPolicies'
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
    print(PptExecDefineLeasingPolicies().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
