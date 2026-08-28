---
name: "rar-cowork-cookbook-ppt-exec-troubleshoot-reported-incidents"
description: "Generates an executive-ready PowerPoint deck on troubleshoot reported incidents status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_troubleshoot_reported_incidents", "rar_sha256": "e8261c3cb44ac38df448216cd80136180982b872d5918a6e08c3f5c10e44e8f8", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_troubleshoot_reported_incidents`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_troubleshoot_reported_incidents_agent.py` and in the RCI capsule.

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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_troubleshoot_reported_incidents_agent.py` and embedded as the fenced Python below (sha256 e8261c3cb44ac38d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_troubleshoot_reported_incidents_agent.py` first:

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
    "version": '2.0.1',
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
