---
name: "rar-cowork-cookbook-ppt-exec-onboard-new-users"
description: "Generates an executive-ready PowerPoint deck on onboard new users status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_onboard_new_users", "rar_sha256": "72c7a0c15ce7ef6a356299533b0e7407f7cae3083cafb352476f2a7a894be595", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_onboard_new_users`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_onboard_new_users_agent.py` and in the RCI capsule.

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

Onboard new users Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on onboard new users status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-onboard-new-users
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_onboard_new_users_agent.py` and embedded as the fenced Python below (sha256 72c7a0c15ce7ef6a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_onboard_new_users_agent.py` first:

```bash
python3 ppt_exec_onboard_new_users_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_onboard_new_users_agent.py   # or on stdin
python3 ppt_exec_onboard_new_users_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Onboard new users Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on onboard new users status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-onboard-new-users
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_onboard_new_users',
    "version": '2.0.1',
    "display_name": 'Onboard new users Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on onboard new users status, complete with charts and talking-point notes.',
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
        "upstream_slug": 'ppt-exec-onboard-new-users',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-onboard-new-users',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '06ae3a8717ab6ed7',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-system-access-and-security/onboard-new-users'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/ppt-exec-onboard-new-users', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class PptExecOnboardNewUsers(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecOnboardNewUsers'
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
    print(PptExecOnboardNewUsers().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
