---
name: "rar-cowork-cookbook-dashboard-define-security-approach"
description: "Produces a self-contained interactive HTML dashboard for define security approach - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_define_security_approach", "rar_sha256": "3dc51647d76726edff4fed42ef675dfa7ae873603df2c7940bb6653f269a519b", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
