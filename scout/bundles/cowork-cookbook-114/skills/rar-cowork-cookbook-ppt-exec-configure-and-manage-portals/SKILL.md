---
name: "rar-cowork-cookbook-ppt-exec-configure-and-manage-portals"
description: "Generates an executive-ready PowerPoint deck on configure and manage portals status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_configure_and_manage_portals", "rar_sha256": "5f04fb211a44e5c5a451aae1d2a0539bb7bc35cbf3955c3033144748fcdc840d", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_configure_and_manage_portals_agent.py` and embedded as the fenced Python below (sha256 5f04fb211a44e5c5…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_configure_and_manage_portals_agent.py` first:

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
    "version": '2.0.0',
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
