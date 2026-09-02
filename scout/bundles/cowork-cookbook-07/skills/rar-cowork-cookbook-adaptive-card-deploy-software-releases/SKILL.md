---
name: "rar-cowork-cookbook-adaptive-card-deploy-software-releases"
description: "Produces a reusable Adaptive Card JSON snapshot of deploy software releases status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_deploy_software_releases", "rar_sha256": "377a633c0fc53a83a07739e55d423ee321a2fb9378cd30383dc652ef8b216453", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "adaptive_card_deploy_software_releases_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/adaptive-card-deploy-software-releases:3be95e7c74a8139b30bc8b14cba312f06a9a2d98bafa6d77dad7c883ef53915e", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/adaptive_card_deploy_software_releases`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `adaptive_card_deploy_software_releases_agent.py` is
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
