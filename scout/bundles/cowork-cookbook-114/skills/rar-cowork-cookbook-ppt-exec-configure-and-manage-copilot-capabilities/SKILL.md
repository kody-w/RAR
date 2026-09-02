---
name: "rar-cowork-cookbook-ppt-exec-configure-and-manage-copilot-capabilities"
description: "Generates an executive-ready PowerPoint deck on configure and manage copilot capabilities status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_configure_and_manage_copilot_capabilities", "rar_sha256": "7f9e28ca3e69a3b2e8b094bcd794994fe87a27eac81a642d830e554d5f36c1b1", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "ppt_exec_configure_and_manage_copilot_capabilities_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/ppt-exec-configure-and-manage-copilot-capabilities:4cc8f7e40dd0b3dc195e1d4e02f6c2169219ec7b3b7e47c6c8f84c9c233afe93", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/ppt_exec_configure_and_manage_copilot_capabilities`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `ppt_exec_configure_and_manage_copilot_capabilities_agent.py` is
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

Configure and manage copilot capabilities Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on configure and manage copilot capabilities status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-configure-and-manage-copilot-capabilities
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_configure_and_manage_copilot_capabilities_agent.py` and embedded as the fenced Python below (sha256 7f9e28ca3e69a3b2…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_configure_and_manage_copilot_capabilities_agent.py` first:

```bash
python3 ppt_exec_configure_and_manage_copilot_capabilities_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_configure_and_manage_copilot_capabilities_agent.py   # or on stdin
python3 ppt_exec_configure_and_manage_copilot_capabilities_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Configure and manage copilot capabilities Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on configure and manage copilot capabilities status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-configure-and-manage-copilot-capabilities
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_configure_and_manage_copilot_capabilities',
    "version": '2.0.0',
    "display_name": 'Configure and manage copilot capabilities Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on configure and manage copilot capabilities status, complete with charts and talking-point notes.',
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
        "upstream_slug": 'ppt-exec-configure-and-manage-copilot-capabilities',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-configure-and-manage-copilot-capabilities',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '2ec090c026cffb43',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/administer-system-features/configure-and-manage-copilot-capabilities'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/ppt-exec-configure-and-manage-copilot-capabilities', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class PptExecConfigureAndManageCopilotCapabilities(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecConfigureAndManageCopilotCapabilities'
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
    print(PptExecConfigureAndManageCopilotCapabilities().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
