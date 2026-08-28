---
name: "rar-cowork-cookbook-scheduled-brief-manage-authentication"
description: "Schedulable morning-brief email summarizing manage authentication for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_manage_authentication", "rar_sha256": "e0272533965f4f4ab1e42fffaa68f7a394a7990c99d80d0d89f9f1ceefeab3dd", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_manage_authentication_agent.py` and embedded as the fenced Python below (sha256 e0272533965f4f4a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_manage_authentication_agent.py` first:

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
    "version": '2.0.0',
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
