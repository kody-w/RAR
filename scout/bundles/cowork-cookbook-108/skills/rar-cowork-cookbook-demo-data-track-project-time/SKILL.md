---
name: "rar-cowork-cookbook-demo-data-track-project-time"
description: "Generates and creates realistic demo records for track project time in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_track_project_time", "rar_sha256": "472510e58316a77e5726dc8d50cfcb08d9546ad28fb902cf9b84233dfa2a79dc", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "demo_data_track_project_time_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/demo-data-track-project-time:e70d27c94d9238df39d631277eeb9349f6d7a2efbf69202569c89dd961462455", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/demo_data_track_project_time`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `demo_data_track_project_time_agent.py` is
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

Track project time Demo Data Generator — Generates and creates realistic demo records for track project time in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-track-project-time
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_track_project_time_agent.py` and embedded as the fenced Python below (sha256 472510e58316a77e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_track_project_time_agent.py` first:

```bash
python3 demo_data_track_project_time_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_track_project_time_agent.py   # or on stdin
python3 demo_data_track_project_time_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Track project time Demo Data Generator — Generates and creates realistic demo records for track project time in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-track-project-time
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_track_project_time',
    "version": '2.0.0',
    "display_name": 'Track project time Demo Data Generator',
    "description": 'Generates and creates realistic demo records for track project time in a sandbox tenant for training and pilot scenarios.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'project_to_profit', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-track-project-time',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-track-project-time',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'a6976d7294fae1d6',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/manage-project-delivery/track-project-time'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/demo-data-track-project-time', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DemoDataTrackProjectTime(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataTrackProjectTime'
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
    print(DemoDataTrackProjectTime().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
