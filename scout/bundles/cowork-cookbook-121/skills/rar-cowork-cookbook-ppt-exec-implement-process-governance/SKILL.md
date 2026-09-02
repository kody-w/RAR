---
name: "rar-cowork-cookbook-ppt-exec-implement-process-governance"
description: "Generates an executive-ready PowerPoint deck on implement process governance status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_implement_process_governance", "rar_sha256": "309d410d60fa788e05eaf9f5c76376e92dcc4977b0b2ecfe01baf3ffcf231ec3", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "ppt_exec_implement_process_governance_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/ppt-exec-implement-process-governance:049e8735788093938cb39922c75d07721b20daa07d6aa276b0dfc9b165ff6b17", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/ppt_exec_implement_process_governance`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `ppt_exec_implement_process_governance_agent.py` is
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

Implement process governance Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on implement process governance status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-implement-process-governance
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_implement_process_governance_agent.py` and embedded as the fenced Python below (sha256 309d410d60fa788e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_implement_process_governance_agent.py` first:

```bash
python3 ppt_exec_implement_process_governance_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_implement_process_governance_agent.py   # or on stdin
python3 ppt_exec_implement_process_governance_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Implement process governance Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on implement process governance status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-implement-process-governance
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_implement_process_governance',
    "version": '2.0.0',
    "display_name": 'Implement process governance Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on implement process governance status, complete with charts and talking-point notes.',
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
        "upstream_slug": 'ppt-exec-implement-process-governance',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-implement-process-governance',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'ac7a4fd00bf5dceb',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/implement-solutions/implement-process-governance'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/ppt-exec-implement-process-governance', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class PptExecImplementProcessGovernance(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecImplementProcessGovernance'
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
    print(PptExecImplementProcessGovernance().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
