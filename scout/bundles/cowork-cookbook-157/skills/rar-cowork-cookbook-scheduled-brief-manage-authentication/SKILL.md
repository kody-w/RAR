---
name: "rar-cowork-cookbook-scheduled-brief-manage-authentication"
description: "Schedulable morning-brief email summarizing manage authentication for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_manage_authentication", "rar_sha256": "c2589380dbf337fe5efd14af2c67f305bd8f3eecebb190680655d30f2186afa7", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_manage_authentication`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_manage_authentication_agent.py` and in the RCI capsule.

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

Manage authentication Scheduled Email Brief — Schedulable morning-brief email summarizing manage authentication for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-manage-authentication
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_manage_authentication_agent.py` and embedded as the fenced Python below (sha256 c2589380dbf337fe…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_manage_authentication_agent.py` first:

```bash
python3 scheduled_brief_manage_authentication_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_manage_authentication_agent.py   # or on stdin
python3 scheduled_brief_manage_authentication_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage authentication Scheduled Email Brief — Schedulable morning-brief email summarizing manage authentication for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-manage-authentication
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_manage_authentication',
    "version": '2.0.1',
    "display_name": 'Manage authentication Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing manage authentication for the responsible owner; designed to run daily or weekly.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-manage-authentication',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-manage-authentication',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '629151c481143ee4',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-system-access-and-security/manage-authentication'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/scheduled-brief-manage-authentication', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class ScheduledBriefManageAuthentication(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefManageAuthentication'
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
    print(ScheduledBriefManageAuthentication().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
