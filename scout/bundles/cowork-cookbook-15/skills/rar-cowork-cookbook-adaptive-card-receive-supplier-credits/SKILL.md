---
name: "rar-cowork-cookbook-adaptive-card-receive-supplier-credits"
description: "Produces a reusable Adaptive Card JSON snapshot of receive supplier credits status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_receive_supplier_credits", "rar_sha256": "9fc7cf08583e32c53b8c6f553d127c32d7a2846f864bccf6154ae2dd9af5bcbd", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "adaptive_card_receive_supplier_credits_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/adaptive-card-receive-supplier-credits:fcf72a2efa47e4f6fcf4ec1cd9029c60473a87870b9265e87875b641c57fcf79", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/adaptive_card_receive_supplier_credits`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `adaptive_card_receive_supplier_credits_agent.py` is
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
