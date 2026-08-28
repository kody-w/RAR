---
name: "rar-cowork-cookbook-ppt-exec-onboard-new-users"
description: "Generates an executive-ready PowerPoint deck on onboard new users status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_onboard_new_users", "rar_sha256": "7703b0c030245dfc719cf7acf0a65f2a22be6e968b0f7f21fd4be2657a0995c7", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_onboard_new_users_agent.py` and embedded as the fenced Python below (sha256 7703b0c030245dfc…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_onboard_new_users_agent.py` first:

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
    "version": '2.0.0',
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
