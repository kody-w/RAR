---
name: "rar-cowork-cookbook-ppt-exec-manage-trade-allowances"
description: "Generates an executive-ready PowerPoint deck on manage trade allowances status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_manage_trade_allowances", "rar_sha256": "b027249edeee3b1cc616f0a55b7c945d4e662387093ca195abe18a328c5ec4bb", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "ppt_exec_manage_trade_allowances_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/ppt-exec-manage-trade-allowances:3780e869a31be62da779310f4166c4683ca378d3d665208fe31619ed49873edb", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/ppt_exec_manage_trade_allowances`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `ppt_exec_manage_trade_allowances_agent.py` is
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

Manage trade allowances Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on manage trade allowances status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-manage-trade-allowances
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_manage_trade_allowances_agent.py` and embedded as the fenced Python below (sha256 b027249edeee3b1c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_manage_trade_allowances_agent.py` first:

```bash
python3 ppt_exec_manage_trade_allowances_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_manage_trade_allowances_agent.py   # or on stdin
python3 ppt_exec_manage_trade_allowances_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage trade allowances Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on manage trade allowances status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-manage-trade-allowances
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_manage_trade_allowances',
    "version": '2.0.0',
    "display_name": 'Manage trade allowances Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on manage trade allowances status, complete with charts and talking-point notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'order_to_cash', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-manage-trade-allowances',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-manage-trade-allowances',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'b860577c9b0c2cd8',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/manage-accounts-receivable/manage-trade-allowances'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/ppt-exec-manage-trade-allowances', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class PptExecManageTradeAllowances(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecManageTradeAllowances'
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
    print(PptExecManageTradeAllowances().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
