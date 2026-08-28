---
name: "rar-cowork-cookbook-adaptive-card-deploy-software-releases"
description: "Produces a reusable Adaptive Card JSON snapshot of deploy software releases status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_deploy_software_releases", "rar_sha256": "377a633c0fc53a83a07739e55d423ee321a2fb9378cd30383dc652ef8b216453", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_deploy_software_releases_agent.py` and embedded as the fenced Python below (sha256 377a633c0fc53a83…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_deploy_software_releases_agent.py` first:

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
    "version": '2.0.0',
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
