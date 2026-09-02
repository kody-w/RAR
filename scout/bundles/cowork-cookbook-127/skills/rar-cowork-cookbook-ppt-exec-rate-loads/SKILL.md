---
name: "rar-cowork-cookbook-ppt-exec-rate-loads"
description: "Generates an executive-ready PowerPoint deck on rate loads status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_rate_loads", "rar_sha256": "5c899635d3b6006dc74bfe8e105a6ee4608954dc5a940c3109c4a52d77f2669f", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "ppt_exec_rate_loads_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/ppt-exec-rate-loads:7c5cbdb81d2eb6125176a4ca49570f0f788140b43c97bee32e4a20a1a4e8eedd", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/ppt_exec_rate_loads`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `ppt_exec_rate_loads_agent.py` is
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

Rate loads Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on rate loads status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-rate-loads
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_rate_loads_agent.py` and embedded as the fenced Python below (sha256 5c899635d3b6006d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_rate_loads_agent.py` first:

```bash
python3 ppt_exec_rate_loads_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_rate_loads_agent.py   # or on stdin
python3 ppt_exec_rate_loads_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Rate loads Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on rate loads status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-rate-loads
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_rate_loads',
    "version": '2.0.0',
    "display_name": 'Rate loads Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on rate loads status, complete with charts and talking-point notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'inventory_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-rate-loads',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-rate-loads',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'd1d43a7ed71faee6',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/manage-freight-and-transportation/rate-loads'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/ppt-exec-rate-loads', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class PptExecRateLoads(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecRateLoads'
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
    print(PptExecRateLoads().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
