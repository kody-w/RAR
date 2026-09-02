---
name: "rar-cowork-cookbook-dashboard-develop-procurement-policies"
description: "Produces a self-contained interactive HTML dashboard for develop procurement policies - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_develop_procurement_policies", "rar_sha256": "a26b6c065e9fb1668996193dcfa4fb4acb191e4a10af9db1b258a117ed90a0ef", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "dashboard_develop_procurement_policies_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/dashboard-develop-procurement-policies:2c48cbf5df6d4f7d64544e5938aeb932614bcefbbe6d9ab333c63891761a74be", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/dashboard_develop_procurement_policies`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `dashboard_develop_procurement_policies_agent.py` is
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

Develop procurement policies Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for develop procurement policies - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-develop-procurement-policies
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_develop_procurement_policies_agent.py` and embedded as the fenced Python below (sha256 a26b6c065e9fb166…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_develop_procurement_policies_agent.py` first:

```bash
python3 dashboard_develop_procurement_policies_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_develop_procurement_policies_agent.py   # or on stdin
python3 dashboard_develop_procurement_policies_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop procurement policies Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for develop procurement policies - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-develop-procurement-policies
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_develop_procurement_policies',
    "version": '2.0.0',
    "display_name": 'Develop procurement policies Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for develop procurement policies - opens in any browser, no D365 access needed by the viewer.',
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
        "upstream_slug": 'dashboard-develop-procurement-policies',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-develop-procurement-policies',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'a685a2333c559952',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/develop-procurement-and-sourcing-strategy/develop-procurement-policies'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/dashboard-develop-procurement-policies', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DashboardDevelopProcurementPolicies(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardDevelopProcurementPolicies'
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
    print(DashboardDevelopProcurementPolicies().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
