---
name: "rar-cowork-cookbook-dashboard-revoke-users-access-to-systems"
description: "Produces a self-contained interactive HTML dashboard for revoke users access to systems - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_revoke_users_access_to_systems", "rar_sha256": "cca96430f4f767d407d7f7be7ab5d959cea65cf27794e11810f2509091406a1a", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "dashboard_revoke_users_access_to_systems_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/dashboard-revoke-users-access-to-systems:23ae02670875e264f1558cf9b4415632e77f569b591b30d68c1700a845dd2d2f", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/dashboard_revoke_users_access_to_systems`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `dashboard_revoke_users_access_to_systems_agent.py` is
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

Revoke users access to systems Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for revoke users access to systems - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-revoke-users-access-to-systems
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_revoke_users_access_to_systems_agent.py` and embedded as the fenced Python below (sha256 cca96430f4f767d4…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_revoke_users_access_to_systems_agent.py` first:

```bash
python3 dashboard_revoke_users_access_to_systems_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_revoke_users_access_to_systems_agent.py   # or on stdin
python3 dashboard_revoke_users_access_to_systems_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Revoke users access to systems Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for revoke users access to systems - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-revoke-users-access-to-systems
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_revoke_users_access_to_systems',
    "version": '2.0.0',
    "display_name": 'Revoke users access to systems Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for revoke users access to systems - opens in any browser, no D365 access needed by the viewer.',
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
        "upstream_slug": 'dashboard-revoke-users-access-to-systems',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-revoke-users-access-to-systems',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '601d027a2f7368ee',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-system-access-and-security/revoke-users-access-to-systems'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/dashboard-revoke-users-access-to-systems', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DashboardRevokeUsersAccessToSystems(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardRevokeUsersAccessToSystems'
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
    print(DashboardRevokeUsersAccessToSystems().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
