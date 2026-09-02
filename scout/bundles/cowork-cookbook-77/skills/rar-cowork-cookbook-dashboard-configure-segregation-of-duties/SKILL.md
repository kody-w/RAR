---
name: "rar-cowork-cookbook-dashboard-configure-segregation-of-duties"
description: "Produces a self-contained interactive HTML dashboard for configure segregation of duties - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_configure_segregation_of_duties", "rar_sha256": "6156f6787c113ff88beb4d08218b4435a920a4cc28dc5edb317ab350b3204f91", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "dashboard_configure_segregation_of_duties_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/dashboard-configure-segregation-of-duties:f229a8bc1ac9e3b30acbc6a520653315b88d383be0ad0dfec1cc5eb7efc83a4f", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/dashboard_configure_segregation_of_duties`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `dashboard_configure_segregation_of_duties_agent.py` is
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

Configure segregation of duties Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for configure segregation of duties - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-configure-segregation-of-duties
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_configure_segregation_of_duties_agent.py` and embedded as the fenced Python below (sha256 6156f6787c113ff8…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_configure_segregation_of_duties_agent.py` first:

```bash
python3 dashboard_configure_segregation_of_duties_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_configure_segregation_of_duties_agent.py   # or on stdin
python3 dashboard_configure_segregation_of_duties_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Configure segregation of duties Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for configure segregation of duties - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-configure-segregation-of-duties
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_configure_segregation_of_duties',
    "version": '2.0.0',
    "display_name": 'Configure segregation of duties Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for configure segregation of duties - opens in any browser, no D365 access needed by the viewer.',
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
        "upstream_slug": 'dashboard-configure-segregation-of-duties',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-configure-segregation-of-duties',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '1bec2c32159369d1',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-system-access-and-security/configure-segregation-of-duties'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/dashboard-configure-segregation-of-duties', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DashboardConfigureSegregationOfDuties(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardConfigureSegregationOfDuties'
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
    print(DashboardConfigureSegregationOfDuties().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
