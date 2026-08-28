---
name: "rar-cowork-cookbook-dashboard-define-security-approach"
description: "Produces a self-contained interactive HTML dashboard for define security approach - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_define_security_approach", "rar_sha256": "e115f365a1abd6248eb92a9c00dcfd205cdf516d389d1a96dba8f56d5dd59634", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_define_security_approach`. The original RAPP
agent is preserved byte-for-byte in `dashboard_define_security_approach_agent.py` and in the RCI capsule.

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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_define_security_approach_agent.py` and embedded as the fenced Python below (sha256 e115f365a1abd624…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_define_security_approach_agent.py` first:

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
    "version": '2.0.1',
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
