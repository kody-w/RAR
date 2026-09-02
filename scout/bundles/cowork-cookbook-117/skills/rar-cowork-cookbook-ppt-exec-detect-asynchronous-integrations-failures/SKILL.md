---
name: "rar-cowork-cookbook-ppt-exec-detect-asynchronous-integrations-failures"
description: "Generates an executive-ready PowerPoint deck on detect asynchronous integrations failures status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_detect_asynchronous_integrations_failures", "rar_sha256": "d99c9467be722f349745b33a0fbeefbe9bc530ad51418136b888dd8b67c19fed", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "ppt_exec_detect_asynchronous_integrations_failures_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/ppt-exec-detect-asynchronous-integrations-failures:48ac0bfd5e0638ef4389c27e1bd40eaae4720ee1317ffaff730a0e992d0974b6", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/ppt_exec_detect_asynchronous_integrations_failures`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `ppt_exec_detect_asynchronous_integrations_failures_agent.py` is
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

Detect asynchronous integrations failures Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on detect asynchronous integrations failures status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-detect-asynchronous-integrations-failures
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_detect_asynchronous_integrations_failures_agent.py` and embedded as the fenced Python below (sha256 d99c9467be722f34…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_detect_asynchronous_integrations_failures_agent.py` first:

```bash
python3 ppt_exec_detect_asynchronous_integrations_failures_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_detect_asynchronous_integrations_failures_agent.py   # or on stdin
python3 ppt_exec_detect_asynchronous_integrations_failures_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Detect asynchronous integrations failures Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on detect asynchronous integrations failures status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-detect-asynchronous-integrations-failures
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_detect_asynchronous_integrations_failures',
    "version": '2.0.0',
    "display_name": 'Detect asynchronous integrations failures Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on detect asynchronous integrations failures status, complete with charts and talking-point notes.',
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
        "upstream_slug": 'ppt-exec-detect-asynchronous-integrations-failures',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-detect-asynchronous-integrations-failures',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '31f20f9e482e60f7',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/monitor-systems-environments-and-capacity/detect-asynchronous-integrations-failures'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/ppt-exec-detect-asynchronous-integrations-failures', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class PptExecDetectAsynchronousIntegrationsFailures(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecDetectAsynchronousIntegrationsFailures'
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
    print(PptExecDetectAsynchronousIntegrationsFailures().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
