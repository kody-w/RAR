---
name: "rar-cowork-cookbook-ppt-exec-troubleshoot-reported-incidents"
description: "Generates an executive-ready PowerPoint deck on troubleshoot reported incidents status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_troubleshoot_reported_incidents", "rar_sha256": "f789aad0f908fef72c46edf02816c20e0e9e1786eaf2f32a5ffad4e47b8f4d80", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "ppt_exec_troubleshoot_reported_incidents_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/ppt-exec-troubleshoot-reported-incidents:ae2e556dde2dfc8eaaf1875950c854d73167aff381500984ac33c6bf7a754907", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/ppt_exec_troubleshoot_reported_incidents`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `ppt_exec_troubleshoot_reported_incidents_agent.py` is
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

Troubleshoot reported incidents Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on troubleshoot reported incidents status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-troubleshoot-reported-incidents
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_troubleshoot_reported_incidents_agent.py` and embedded as the fenced Python below (sha256 f789aad0f908fef7…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_troubleshoot_reported_incidents_agent.py` first:

```bash
python3 ppt_exec_troubleshoot_reported_incidents_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_troubleshoot_reported_incidents_agent.py   # or on stdin
python3 ppt_exec_troubleshoot_reported_incidents_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Troubleshoot reported incidents Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on troubleshoot reported incidents status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-troubleshoot-reported-incidents
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_troubleshoot_reported_incidents',
    "version": '2.0.0',
    "display_name": 'Troubleshoot reported incidents Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on troubleshoot reported incidents status, complete with charts and talking-point notes.',
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
        "upstream_slug": 'ppt-exec-troubleshoot-reported-incidents',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-troubleshoot-reported-incidents',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '7f399b942d2d323a',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/support-systems/troubleshoot-reported-incidents'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/ppt-exec-troubleshoot-reported-incidents', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class PptExecTroubleshootReportedIncidents(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecTroubleshootReportedIncidents'
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
    print(PptExecTroubleshootReportedIncidents().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
