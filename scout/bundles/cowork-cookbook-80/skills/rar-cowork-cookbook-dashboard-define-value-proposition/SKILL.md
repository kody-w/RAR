---
name: "rar-cowork-cookbook-dashboard-define-value-proposition"
description: "Produces a self-contained interactive HTML dashboard for define value proposition - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_define_value_proposition", "rar_sha256": "07343858009ee9fe20afc23218e03a00f9fd7b25066cd8430f54e1e74136d031", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "dashboard_define_value_proposition_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/dashboard-define-value-proposition:ed50cdeaa2fdeaa9e272efc8fb234346cc0156c7d7a08982e3d011b95f554d4e", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/dashboard_define_value_proposition`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `dashboard_define_value_proposition_agent.py` is
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

Define value proposition Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for define value proposition - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-define-value-proposition
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_define_value_proposition_agent.py` and embedded as the fenced Python below (sha256 07343858009ee9fe…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_define_value_proposition_agent.py` first:

```bash
python3 dashboard_define_value_proposition_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_define_value_proposition_agent.py   # or on stdin
python3 dashboard_define_value_proposition_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define value proposition Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for define value proposition - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-define-value-proposition
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_define_value_proposition',
    "version": '2.0.0',
    "display_name": 'Define value proposition Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for define value proposition - opens in any browser, no D365 access needed by the viewer.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'concept_to_market', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-define-value-proposition',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-define-value-proposition',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '005dc69ef673e75a',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/develop-marketing-strategy/define-value-proposition'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/dashboard-define-value-proposition', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DashboardDefineValueProposition(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardDefineValueProposition'
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
    print(DashboardDefineValueProposition().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
