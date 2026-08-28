---
name: "rar-cowork-cookbook-adaptive-card-receive-supplier-credits"
description: "Produces a reusable Adaptive Card JSON snapshot of receive supplier credits status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_receive_supplier_credits", "rar_sha256": "f5b650ee666abf6e19e04d852e9d6942e926a0862704fcd28deb5ad6ad575de3", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_receive_supplier_credits`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_receive_supplier_credits_agent.py` and in the RCI capsule.

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

Receive supplier credits Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of receive supplier credits status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-receive-supplier-credits
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_receive_supplier_credits_agent.py` and embedded as the fenced Python below (sha256 f5b650ee666abf6e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_receive_supplier_credits_agent.py` first:

```bash
python3 adaptive_card_receive_supplier_credits_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_receive_supplier_credits_agent.py   # or on stdin
python3 adaptive_card_receive_supplier_credits_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Receive supplier credits Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of receive supplier credits status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-receive-supplier-credits
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_receive_supplier_credits',
    "version": '2.0.1',
    "display_name": 'Receive supplier credits Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of receive supplier credits status for embedding in dashboards, emails, or Teams.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-receive-supplier-credits',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-receive-supplier-credits',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '06314b17cbb9a724',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/manage-accounts-payable/receive-supplier-credits'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/adaptive-card-receive-supplier-credits', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class AdaptiveCardReceiveSupplierCredits(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardReceiveSupplierCredits'
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
    print(AdaptiveCardReceiveSupplierCredits().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
