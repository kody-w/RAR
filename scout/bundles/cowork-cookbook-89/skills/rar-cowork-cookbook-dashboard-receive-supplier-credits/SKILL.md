---
name: "rar-cowork-cookbook-dashboard-receive-supplier-credits"
description: "Produces a self-contained interactive HTML dashboard for receive supplier credits - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_receive_supplier_credits", "rar_sha256": "28ed5afeb2f27c55c91b4893cd1c6ffd234e15f762345a9a2b97f79ed46cf541", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_receive_supplier_credits_agent.py` and embedded as the fenced Python below (sha256 28ed5afeb2f27c55…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_receive_supplier_credits_agent.py` first:

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
    "version": '2.0.0',
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
