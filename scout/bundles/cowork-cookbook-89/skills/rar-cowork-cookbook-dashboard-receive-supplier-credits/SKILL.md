---
name: "rar-cowork-cookbook-dashboard-receive-supplier-credits"
description: "Produces a self-contained interactive HTML dashboard for receive supplier credits - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_receive_supplier_credits", "rar_sha256": "b725478c15b46737055244373ffdfcb0f6958ef51ec6b1aae29a13d611b197d2", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_receive_supplier_credits`. The original RAPP
agent is preserved byte-for-byte in `dashboard_receive_supplier_credits_agent.py` and in the RCI capsule.

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

Receive supplier credits Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for receive supplier credits - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-receive-supplier-credits
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_receive_supplier_credits_agent.py` and embedded as the fenced Python below (sha256 b725478c15b46737…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_receive_supplier_credits_agent.py` first:

```bash
python3 dashboard_receive_supplier_credits_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_receive_supplier_credits_agent.py   # or on stdin
python3 dashboard_receive_supplier_credits_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Receive supplier credits Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for receive supplier credits - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-receive-supplier-credits
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_receive_supplier_credits',
    "version": '2.0.1',
    "display_name": 'Receive supplier credits Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for receive supplier credits - opens in any browser, no D365 access needed by the viewer.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-receive-supplier-credits',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-receive-supplier-credits',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '36e8ae485b6f0878',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/manage-accounts-payable/receive-supplier-credits'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/dashboard-receive-supplier-credits', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DashboardReceiveSupplierCredits(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardReceiveSupplierCredits'
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
    print(DashboardReceiveSupplierCredits().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
