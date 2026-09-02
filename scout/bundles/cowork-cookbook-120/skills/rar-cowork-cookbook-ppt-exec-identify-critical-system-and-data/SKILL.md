---
name: "rar-cowork-cookbook-ppt-exec-identify-critical-system-and-data"
description: "Generates an executive-ready PowerPoint deck on identify critical system and data status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_identify_critical_system_and_data", "rar_sha256": "2ddd2f432920e4af66d41b5b3862ef909d45079f254746570a6a9a01f04bdfa3", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "ppt_exec_identify_critical_system_and_data_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/ppt-exec-identify-critical-system-and-data:3c64928c159927d159b6148f467f3520a5056dc74a9837f82371c6a2d103fba0", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/ppt_exec_identify_critical_system_and_data`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `ppt_exec_identify_critical_system_and_data_agent.py` is
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

Identify critical system and data Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on identify critical system and data status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-identify-critical-system-and-data
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_identify_critical_system_and_data_agent.py` and embedded as the fenced Python below (sha256 2ddd2f432920e4af…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_identify_critical_system_and_data_agent.py` first:

```bash
python3 ppt_exec_identify_critical_system_and_data_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_identify_critical_system_and_data_agent.py   # or on stdin
python3 ppt_exec_identify_critical_system_and_data_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Identify critical system and data Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on identify critical system and data status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-identify-critical-system-and-data
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_identify_critical_system_and_data',
    "version": '2.0.0',
    "display_name": 'Identify critical system and data Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on identify critical system and data status, complete with charts and talking-point notes.',
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
        "upstream_slug": 'ppt-exec-identify-critical-system-and-data',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-identify-critical-system-and-data',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '17b8dbf20164d188',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/define-business-continuity-plan/identify-critical-system-and-data'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/ppt-exec-identify-critical-system-and-data', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.667, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class PptExecIdentifyCriticalSystemAndData(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecIdentifyCriticalSystemAndData'
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
    print(PptExecIdentifyCriticalSystemAndData().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
