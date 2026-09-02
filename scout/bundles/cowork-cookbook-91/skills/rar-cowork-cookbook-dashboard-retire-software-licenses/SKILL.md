---
name: "rar-cowork-cookbook-dashboard-retire-software-licenses"
description: "Produces a self-contained interactive HTML dashboard for retire software licenses - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_retire_software_licenses", "rar_sha256": "40747695a6645e36dd7b210407872d73f7679186109f5b5f9e0a852f86ac505c", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "dashboard_retire_software_licenses_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/dashboard-retire-software-licenses:d35f022b3206a2d61052168c5b48048f599d6df7078fa71d01735194e0d17c89", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/dashboard_retire_software_licenses`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `dashboard_retire_software_licenses_agent.py` is
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

Retire software licenses Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for retire software licenses - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-retire-software-licenses
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_retire_software_licenses_agent.py` and embedded as the fenced Python below (sha256 40747695a6645e36…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_retire_software_licenses_agent.py` first:

```bash
python3 dashboard_retire_software_licenses_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_retire_software_licenses_agent.py   # or on stdin
python3 dashboard_retire_software_licenses_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Retire software licenses Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for retire software licenses - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-retire-software-licenses
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_retire_software_licenses',
    "version": '2.0.0',
    "display_name": 'Retire software licenses Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for retire software licenses - opens in any browser, no D365 access needed by the viewer.',
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
        "upstream_slug": 'dashboard-retire-software-licenses',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-retire-software-licenses',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '93cd5747bf498122',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-licensing-and-entitlements/retire-software-licenses'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/dashboard-retire-software-licenses', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DashboardRetireSoftwareLicenses(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardRetireSoftwareLicenses'
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
    print(DashboardRetireSoftwareLicenses().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
