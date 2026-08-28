---
name: "rar-cowork-cookbook-ppt-exec-confirm-purchase-details"
description: "Generates an executive-ready PowerPoint deck on confirm purchase details status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_confirm_purchase_details", "rar_sha256": "e65bda9efbf44f82cf3292da5d07510eb5569fd439b22becd4a7ffd55471fc76", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_confirm_purchase_details_agent.py` and embedded as the fenced Python below (sha256 e65bda9efbf44f82…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_confirm_purchase_details_agent.py` first:

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
    "version": '2.0.1',
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
