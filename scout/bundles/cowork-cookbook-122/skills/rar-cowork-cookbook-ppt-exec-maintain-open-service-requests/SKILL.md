---
name: "rar-cowork-cookbook-ppt-exec-maintain-open-service-requests"
description: "Generates an executive-ready PowerPoint deck on maintain open service requests status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_maintain_open_service_requests", "rar_sha256": "50d7aeba160d71b0dbd1227c8467777c07a031fb0edc57eeb0688ff29b12a1b6", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "ppt_exec_maintain_open_service_requests_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/ppt-exec-maintain-open-service-requests:3a1c1c7eaf72df5818271ac4641ff82dfb4b56abf24104caec668733d3b81e5a", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/ppt_exec_maintain_open_service_requests`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `ppt_exec_maintain_open_service_requests_agent.py` is
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

Maintain open service requests Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on maintain open service requests status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-maintain-open-service-requests
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_maintain_open_service_requests_agent.py` and embedded as the fenced Python below (sha256 50d7aeba160d71b0…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_maintain_open_service_requests_agent.py` first:

```bash
python3 ppt_exec_maintain_open_service_requests_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_maintain_open_service_requests_agent.py   # or on stdin
python3 ppt_exec_maintain_open_service_requests_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Maintain open service requests Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on maintain open service requests status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-maintain-open-service-requests
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_maintain_open_service_requests',
    "version": '2.0.0',
    "display_name": 'Maintain open service requests Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on maintain open service requests status, complete with charts and talking-point notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'service_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-maintain-open-service-requests',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-maintain-open-service-requests',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '4e999649c50d10a0',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/manage-service-work/maintain-open-service-requests'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/ppt-exec-maintain-open-service-requests', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class PptExecMaintainOpenServiceRequests(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecMaintainOpenServiceRequests'
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
    print(PptExecMaintainOpenServiceRequests().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
