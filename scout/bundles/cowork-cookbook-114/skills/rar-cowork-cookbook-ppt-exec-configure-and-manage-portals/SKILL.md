---
name: "rar-cowork-cookbook-ppt-exec-configure-and-manage-portals"
description: "Generates an executive-ready PowerPoint deck on configure and manage portals status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_configure_and_manage_portals", "rar_sha256": "dd4d0b3b37b054fdfaacecf70bce51d1ec030cb5ea8f1d54831a37057fc7a3f0", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_configure_and_manage_portals`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_configure_and_manage_portals_agent.py` and in the RCI capsule.

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

Configure and manage portals Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on configure and manage portals status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-configure-and-manage-portals
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_configure_and_manage_portals_agent.py` and embedded as the fenced Python below (sha256 dd4d0b3b37b054fd…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_configure_and_manage_portals_agent.py` first:

```bash
python3 ppt_exec_configure_and_manage_portals_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_configure_and_manage_portals_agent.py   # or on stdin
python3 ppt_exec_configure_and_manage_portals_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Configure and manage portals Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on configure and manage portals status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-configure-and-manage-portals
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_configure_and_manage_portals',
    "version": '2.0.1',
    "display_name": 'Configure and manage portals Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on configure and manage portals status, complete with charts and talking-point notes.',
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
        "upstream_slug": 'ppt-exec-configure-and-manage-portals',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-configure-and-manage-portals',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '04629b8acbcbb056',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/administer-system-features/configure-and-manage-portals'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/ppt-exec-configure-and-manage-portals', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class PptExecConfigureAndManagePortals(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecConfigureAndManagePortals'
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
    print(PptExecConfigureAndManagePortals().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
