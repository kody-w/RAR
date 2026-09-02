---
name: "rar-cowork-cookbook-ppt-exec-confirm-purchase-details"
description: "Generates an executive-ready PowerPoint deck on confirm purchase details status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_confirm_purchase_details", "rar_sha256": "b2a22b7f846a817ddee8521cedd3cfa040be5d013221c8336bd3c9186451d637", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "ppt_exec_confirm_purchase_details_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/ppt-exec-confirm-purchase-details:ae8d1a1358a78a39d317c181b7a1c61bcf85804c962dc036882b248adaf74e98", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/ppt_exec_confirm_purchase_details`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `ppt_exec_confirm_purchase_details_agent.py` is
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

Confirm purchase details Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on confirm purchase details status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-confirm-purchase-details
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_confirm_purchase_details_agent.py` and embedded as the fenced Python below (sha256 b2a22b7f846a817d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_confirm_purchase_details_agent.py` first:

```bash
python3 ppt_exec_confirm_purchase_details_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_confirm_purchase_details_agent.py   # or on stdin
python3 ppt_exec_confirm_purchase_details_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Confirm purchase details Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on confirm purchase details status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-confirm-purchase-details
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_confirm_purchase_details',
    "version": '2.0.0',
    "display_name": 'Confirm purchase details Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on confirm purchase details status, complete with charts and talking-point notes.',
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
        "upstream_slug": 'ppt-exec-confirm-purchase-details',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-confirm-purchase-details',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '9be45ba6191e9e0e',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/estimate-and-quote-sales/confirm-purchase-details'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/ppt-exec-confirm-purchase-details', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class PptExecConfirmPurchaseDetails(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecConfirmPurchaseDetails'
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
    print(PptExecConfirmPurchaseDetails().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
