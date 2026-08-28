---
name: "rar-cowork-cookbook-dashboard-deploy-software-releases"
description: "Produces a self-contained interactive HTML dashboard for deploy software releases - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_deploy_software_releases", "rar_sha256": "dfa47ff2fcf043922ffa3ea96fe93bd37d2fa37bef6ed0f2634a15b713264cde", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_deploy_software_releases`. The original RAPP
agent is preserved byte-for-byte in `dashboard_deploy_software_releases_agent.py` and in the RCI capsule.

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
