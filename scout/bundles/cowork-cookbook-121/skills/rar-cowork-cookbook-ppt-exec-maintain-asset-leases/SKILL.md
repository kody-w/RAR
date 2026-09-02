---
name: "rar-cowork-cookbook-ppt-exec-maintain-asset-leases"
description: "Generates an executive-ready PowerPoint deck on maintain asset leases status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_maintain_asset_leases", "rar_sha256": "3bc39ed437ea9fef2a29850e945c9b5b988b6c599dea3cf86d38c677da20e768", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "ppt_exec_maintain_asset_leases_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/ppt-exec-maintain-asset-leases:acfa523cf07bd478ad566d9ced55eef017308de12c7f25772f9de862cb4505d2", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/ppt_exec_maintain_asset_leases`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `ppt_exec_maintain_asset_leases_agent.py` is
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

Maintain asset leases Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on maintain asset leases status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-maintain-asset-leases
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_maintain_asset_leases_agent.py` and embedded as the fenced Python below (sha256 3bc39ed437ea9fef…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_maintain_asset_leases_agent.py` first:

```bash
python3 ppt_exec_maintain_asset_leases_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_maintain_asset_leases_agent.py   # or on stdin
python3 ppt_exec_maintain_asset_leases_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Maintain asset leases Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on maintain asset leases status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-maintain-asset-leases
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_maintain_asset_leases',
    "version": '2.0.0',
    "display_name": 'Maintain asset leases Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on maintain asset leases status, complete with charts and talking-point notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'acquire_to_dispose', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'verified',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'ppt-exec-maintain-asset-leases',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-maintain-asset-leases',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '0e8ca7ee79924785',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/manage-active-assets/maintain-asset-leases'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/ppt-exec-maintain-asset-leases', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class PptExecMaintainAssetLeases(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecMaintainAssetLeases'
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
    print(PptExecMaintainAssetLeases().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
