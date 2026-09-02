---
name: "rar-cowork-cookbook-ppt-exec-determine-sales-targets"
description: "Generates an executive-ready PowerPoint deck on determine sales targets status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_determine_sales_targets", "rar_sha256": "565721477aa04b6393d1d0c9081a2e13547774a1941a0476f022e0ce2540a983", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "ppt_exec_determine_sales_targets_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/ppt-exec-determine-sales-targets:40b061e28f602a1cfa10d509ff090a854aae4df3e633fdbb2e3625602cff7654", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/ppt_exec_determine_sales_targets`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `ppt_exec_determine_sales_targets_agent.py` is
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

Determine sales targets Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on determine sales targets status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-determine-sales-targets
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_determine_sales_targets_agent.py` and embedded as the fenced Python below (sha256 565721477aa04b63…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_determine_sales_targets_agent.py` first:

```bash
python3 ppt_exec_determine_sales_targets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_determine_sales_targets_agent.py   # or on stdin
python3 ppt_exec_determine_sales_targets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Determine sales targets Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on determine sales targets status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-determine-sales-targets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_determine_sales_targets',
    "version": '2.0.0',
    "display_name": 'Determine sales targets Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on determine sales targets status, complete with charts and talking-point notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'prospect_to_quote', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-determine-sales-targets',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-determine-sales-targets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '5626997349275e3a',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/define-sales-strategy-and-policies/determine-sales-targets'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/ppt-exec-determine-sales-targets', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class PptExecDetermineSalesTargets(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecDetermineSalesTargets'
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
    print(PptExecDetermineSalesTargets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
