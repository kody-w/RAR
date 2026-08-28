---
name: "rar-cowork-cookbook-dashboard-revoke-users-access-to-systems"
description: "Produces a self-contained interactive HTML dashboard for revoke users access to systems - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_revoke_users_access_to_systems", "rar_sha256": "cca96430f4f767d407d7f7be7ab5d959cea65cf27794e11810f2509091406a1a", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_revoke_users_access_to_systems`. The original RAPP
agent is preserved byte-for-byte in `dashboard_revoke_users_access_to_systems_agent.py` and in the RCI capsule.

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
