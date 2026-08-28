---
name: "rar-cowork-cookbook-adaptive-card-deploy-software-releases"
description: "Produces a reusable Adaptive Card JSON snapshot of deploy software releases status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_deploy_software_releases", "rar_sha256": "96e056f720ec621afad6f7b46a75e6d37b482fca55b12dfd6aad01b30840ff60", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_deploy_software_releases`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_deploy_software_releases_agent.py` and in the RCI capsule.

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

Deploy software releases Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of deploy software releases status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-deploy-software-releases
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_deploy_software_releases_agent.py` and embedded as the fenced Python below (sha256 96e056f720ec621a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_deploy_software_releases_agent.py` first:

```bash
python3 adaptive_card_deploy_software_releases_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_deploy_software_releases_agent.py   # or on stdin
python3 adaptive_card_deploy_software_releases_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Deploy software releases Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of deploy software releases status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-deploy-software-releases
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_deploy_software_releases',
    "version": '2.0.1',
    "display_name": 'Deploy software releases Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of deploy software releases status for embedding in dashboards, emails, or Teams.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'verified',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'adaptive-card-deploy-software-releases',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-deploy-software-releases',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'b25dcdcec4d8c0c3',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-06-01', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/uptake-software-releases/deploy-software-releases'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/adaptive-card-deploy-software-releases', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class AdaptiveCardDeploySoftwareReleases(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardDeploySoftwareReleases'
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
    print(AdaptiveCardDeploySoftwareReleases().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
