---
name: "rar-cowork-cookbook-dashboard-receive-supplier-credits"
description: "Produces a self-contained interactive HTML dashboard for receive supplier credits - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_receive_supplier_credits", "rar_sha256": "28ed5afeb2f27c55c91b4893cd1c6ffd234e15f762345a9a2b97f79ed46cf541", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "dashboard_receive_supplier_credits_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/dashboard-receive-supplier-credits:c8ac34295b8c5c8e3aea3863609089d266923666defa96af83a475f80c1c083b", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/dashboard_receive_supplier_credits`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `dashboard_receive_supplier_credits_agent.py` is
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
