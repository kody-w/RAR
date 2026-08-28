---
name: "rar-cowork-cookbook-ppt-exec-confirm-purchase-details"
description: "Generates an executive-ready PowerPoint deck on confirm purchase details status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_confirm_purchase_details", "rar_sha256": "b2a22b7f846a817ddee8521cedd3cfa040be5d013221c8336bd3c9186451d637", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_confirm_purchase_details`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_confirm_purchase_details_agent.py` and in the RCI capsule.

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
