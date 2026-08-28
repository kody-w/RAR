---
name: "rar-cowork-cookbook-build-your-executive-command-center"
description: "Start every day knowing exactly where to focus - without scrolling through emails, meetings, and chats to triangulate it yourself."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/build_your_executive_command_center", "rar_sha256": "0024acacd7530f855f8bf3bc163a6658077a36267eb0394a36ff9093e0f9d93f", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "work_management", "advanced", "integration", "fabric_iq"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/build_your_executive_command_center`. The original RAPP
agent is preserved byte-for-byte in `build_your_executive_command_center_agent.py` and in the RCI capsule.

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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `build_your_executive_command_center_agent.py` and embedded as the fenced Python below (sha256 0024acacd7530f85…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `build_your_executive_command_center_agent.py` first:

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
    "version": '2.0.1',
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
