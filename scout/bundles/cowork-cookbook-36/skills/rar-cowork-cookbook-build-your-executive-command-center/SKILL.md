---
name: "rar-cowork-cookbook-build-your-executive-command-center"
description: "Start every day knowing exactly where to focus - without scrolling through emails, meetings, and chats to triangulate it yourself."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/build_your_executive_command_center", "rar_sha256": "af8aeed741ed798fd57883e1bf37d69798d8fd72c9ccc9770dba85ab95ee81f3", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "build_your_executive_command_center_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/build-your-executive-command-center:bd42d71b8ab134d39e2555d9a631aae78d09c1e49794e6967f32d9b7f3eef063", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "work_management", "advanced", "integration", "fabric_iq"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/build_your_executive_command_center`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `build_your_executive_command_center_agent.py` is
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

Build your executive command center — Start every day knowing exactly where to focus - without scrolling through emails, meetings, and chats to triangulate it yourself.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/build-your-executive-command-center
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `build_your_executive_command_center_agent.py` and embedded as the fenced Python below (sha256 af8aeed741ed798f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `build_your_executive_command_center_agent.py` first:

```bash
python3 build_your_executive_command_center_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 build_your_executive_command_center_agent.py   # or on stdin
python3 build_your_executive_command_center_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Build your executive command center — Start every day knowing exactly where to focus - without scrolling through emails, meetings, and chats to triangulate it yourself.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/build-your-executive-command-center
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/build_your_executive_command_center',
    "version": '2.0.0',
    "display_name": 'Build your executive command center',
    "description": 'Start every day knowing exactly where to focus - without scrolling through emails, meetings, and chats to triangulate it yourself.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'other', 'work_management', 'advanced', 'integration', 'fabric_iq'],
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
        "upstream_slug": 'build-your-executive-command-center',
        "upstream_url": 'https://coworkcookbook.com/recipes/build-your-executive-command-center',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '8a01b3152482f58b',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'advanced', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'fabric-iq', 'process_roots': ['work-management'], 'process_tags': ['work-management/research-and-synthesize/build-personal-insight-dashboards'], 'recipe_category': 'other', 'recipe_type': 'prompt', 'upstream_path': 'work-management/build-your-executive-command-center', 'uses_skills': {'custom': [], 'ootb': ['Meetings'], 'plugin': []}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class BuildYourExecutiveCommandCenter(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BuildYourExecutiveCommandCenter'
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
    print(BuildYourExecutiveCommandCenter().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
