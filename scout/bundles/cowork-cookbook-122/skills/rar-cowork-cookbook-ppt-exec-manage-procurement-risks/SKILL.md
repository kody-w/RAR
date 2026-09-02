---
name: "rar-cowork-cookbook-ppt-exec-manage-procurement-risks"
description: "Generates an executive-ready PowerPoint deck on manage procurement risks status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_manage_procurement_risks", "rar_sha256": "4e7dc5ac0c56c7f9da8dc255564c4c63d533779ae24cb31d7209cf6d324e8971", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "ppt_exec_manage_procurement_risks_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/ppt-exec-manage-procurement-risks:61b2a6a113729af4ebe377d1138159acb68603b160cfe245c557ee726a67c52e", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/ppt_exec_manage_procurement_risks`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `ppt_exec_manage_procurement_risks_agent.py` is
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

Manage procurement risks Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on manage procurement risks status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-manage-procurement-risks
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_manage_procurement_risks_agent.py` and embedded as the fenced Python below (sha256 4e7dc5ac0c56c7f9…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_manage_procurement_risks_agent.py` first:

```bash
python3 ppt_exec_manage_procurement_risks_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_manage_procurement_risks_agent.py   # or on stdin
python3 ppt_exec_manage_procurement_risks_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage procurement risks Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on manage procurement risks status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-manage-procurement-risks
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_manage_procurement_risks',
    "version": '2.0.0',
    "display_name": 'Manage procurement risks Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on manage procurement risks status, complete with charts and talking-point notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-manage-procurement-risks',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-manage-procurement-risks',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '01670af81f1563c0',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/analyze-procurement-and-sourcing/manage-procurement-risks'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/ppt-exec-manage-procurement-risks', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class PptExecManageProcurementRisks(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecManageProcurementRisks'
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
    print(PptExecManageProcurementRisks().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
