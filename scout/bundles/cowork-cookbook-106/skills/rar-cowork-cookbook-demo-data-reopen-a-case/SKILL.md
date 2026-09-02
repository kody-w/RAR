---
name: "rar-cowork-cookbook-demo-data-reopen-a-case"
description: "Generates and creates realistic demo records for reopen a case in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_reopen_a_case", "rar_sha256": "77bcace760aad2744760317fb9c49684256b0ca8bebd0c9b3ae023f9c6fa97ce", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "demo_data_reopen_a_case_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/demo-data-reopen-a-case:edc43e4da9e73942bcc39f7eeb2a7f2cc7807fb70521f789d2da6cee66cf0b51", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/demo_data_reopen_a_case`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `demo_data_reopen_a_case_agent.py` is
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

Reopen a case Demo Data Generator — Generates and creates realistic demo records for reopen a case in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-reopen-a-case
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_reopen_a_case_agent.py` and embedded as the fenced Python below (sha256 77bcace760aad274…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_reopen_a_case_agent.py` first:

```bash
python3 demo_data_reopen_a_case_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_reopen_a_case_agent.py   # or on stdin
python3 demo_data_reopen_a_case_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Reopen a case Demo Data Generator — Generates and creates realistic demo records for reopen a case in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-reopen-a-case
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_reopen_a_case',
    "version": '2.0.0',
    "display_name": 'Reopen a case Demo Data Generator',
    "description": 'Generates and creates realistic demo records for reopen a case in a sandbox tenant for training and pilot scenarios.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'case_to_resolution', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-reopen-a-case',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-reopen-a-case',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '667aa2c0f6c9ca7c',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/manage-and-work-on-cases/reopen-a-case'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/demo-data-reopen-a-case', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class DemoDataReopenACase(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataReopenACase'
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
    print(DemoDataReopenACase().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
