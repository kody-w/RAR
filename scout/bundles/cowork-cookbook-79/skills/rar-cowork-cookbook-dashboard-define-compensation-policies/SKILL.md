---
name: "rar-cowork-cookbook-dashboard-define-compensation-policies"
description: "Produces a self-contained interactive HTML dashboard for define compensation policies - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_define_compensation_policies", "rar_sha256": "15bb8f6e15a41f60ec1cbb77dc9eda415e34d6342705380b970ce5409c180dcd", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "dashboard_define_compensation_policies_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/dashboard-define-compensation-policies:08a2431ee0f39c60287a2c8128c51bcda2fb785a5167b849acc62ee8db2a1f64", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/dashboard_define_compensation_policies`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `dashboard_define_compensation_policies_agent.py` is
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

Define compensation policies Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for define compensation policies - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-define-compensation-policies
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_define_compensation_policies_agent.py` and embedded as the fenced Python below (sha256 15bb8f6e15a41f60…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_define_compensation_policies_agent.py` first:

```bash
python3 dashboard_define_compensation_policies_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_define_compensation_policies_agent.py   # or on stdin
python3 dashboard_define_compensation_policies_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define compensation policies Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for define compensation policies - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-define-compensation-policies
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_define_compensation_policies',
    "version": '2.0.0',
    "display_name": 'Define compensation policies Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for define compensation policies - opens in any browser, no D365 access needed by the viewer.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'hire_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-define-compensation-policies',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-define-compensation-policies',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'f97eddf00a8af006',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/manage-compensation-and-benefits/define-compensation-policies'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/dashboard-define-compensation-policies', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DashboardDefineCompensationPolicies(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardDefineCompensationPolicies'
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
    print(DashboardDefineCompensationPolicies().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
