---
name: "rar-cowork-cookbook-ppt-exec-configure-and-manage-portals"
description: "Generates an executive-ready PowerPoint deck on configure and manage portals status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_configure_and_manage_portals", "rar_sha256": "5f04fb211a44e5c5a451aae1d2a0539bb7bc35cbf3955c3033144748fcdc840d", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "ppt_exec_configure_and_manage_portals_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/ppt-exec-configure-and-manage-portals:3b486e3d3fad02e21855f731ed98b14de767dbf86022017c048c4efbba8bdf45", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/ppt_exec_configure_and_manage_portals`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `ppt_exec_configure_and_manage_portals_agent.py` is
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
