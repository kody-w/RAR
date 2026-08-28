---
name: "rar-cowork-cookbook-adaptive-card-receive-supplier-credits"
description: "Produces a reusable Adaptive Card JSON snapshot of receive supplier credits status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_receive_supplier_credits", "rar_sha256": "9fc7cf08583e32c53b8c6f553d127c32d7a2846f864bccf6154ae2dd9af5bcbd", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_receive_supplier_credits_agent.py` and embedded as the fenced Python below (sha256 9fc7cf08583e32c5…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_receive_supplier_credits_agent.py` first:

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
    "version": '2.0.0',
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
