---
name: "rar-cowork-cookbook-dashboard-deploy-software-releases"
description: "Produces a self-contained interactive HTML dashboard for deploy software releases - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_deploy_software_releases", "rar_sha256": "dfa47ff2fcf043922ffa3ea96fe93bd37d2fa37bef6ed0f2634a15b713264cde", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "dashboard_deploy_software_releases_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/dashboard-deploy-software-releases:591086e70edffb62f19e07656a4e81b39f9d6be6ede2be3870ed6ec35fb4054c", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/dashboard_deploy_software_releases`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `dashboard_deploy_software_releases_agent.py` is
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

Deploy software releases Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for deploy software releases - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-deploy-software-releases
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_deploy_software_releases_agent.py` and embedded as the fenced Python below (sha256 dfa47ff2fcf04392…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_deploy_software_releases_agent.py` first:

```bash
python3 dashboard_deploy_software_releases_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_deploy_software_releases_agent.py   # or on stdin
python3 dashboard_deploy_software_releases_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Deploy software releases Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for deploy software releases - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-deploy-software-releases
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_deploy_software_releases',
    "version": '2.0.0',
    "display_name": 'Deploy software releases Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for deploy software releases - opens in any browser, no D365 access needed by the viewer.',
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
        "upstream_slug": 'dashboard-deploy-software-releases',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-deploy-software-releases',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'd08b3f9c0689f02b',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/uptake-software-releases/deploy-software-releases'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/dashboard-deploy-software-releases', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DashboardDeploySoftwareReleases(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardDeploySoftwareReleases'
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
    print(DashboardDeploySoftwareReleases().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
