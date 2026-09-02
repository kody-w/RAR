---
name: "rar-cowork-cookbook-dashboard-define-security-approach"
description: "Produces a self-contained interactive HTML dashboard for define security approach - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_define_security_approach", "rar_sha256": "3dc51647d76726edff4fed42ef675dfa7ae873603df2c7940bb6653f269a519b", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "dashboard_define_security_approach_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/dashboard-define-security-approach:dc641e2e0cdd4daac2c987aec54f21d5119b8a7f7feaae899e56bb6a3c347edd", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/dashboard_define_security_approach`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `dashboard_define_security_approach_agent.py` is
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

Define security approach Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for define security approach - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-define-security-approach
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_define_security_approach_agent.py` and embedded as the fenced Python below (sha256 3dc51647d76726ed…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_define_security_approach_agent.py` first:

```bash
python3 dashboard_define_security_approach_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_define_security_approach_agent.py   # or on stdin
python3 dashboard_define_security_approach_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define security approach Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for define security approach - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-define-security-approach
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_define_security_approach',
    "version": '2.0.0',
    "display_name": 'Define security approach Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for define security approach - opens in any browser, no D365 access needed by the viewer.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-define-security-approach',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-define-security-approach',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '09da00c3cb024cd0',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/implement-solutions/define-security-approach'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/dashboard-define-security-approach', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DashboardDefineSecurityApproach(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardDefineSecurityApproach'
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
    print(DashboardDefineSecurityApproach().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
