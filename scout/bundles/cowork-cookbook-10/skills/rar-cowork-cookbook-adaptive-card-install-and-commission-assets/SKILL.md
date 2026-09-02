---
name: "rar-cowork-cookbook-adaptive-card-install-and-commission-assets"
description: "Produces a reusable Adaptive Card JSON snapshot of install and commission assets status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_install_and_commission_assets", "rar_sha256": "251bb212f38a1b1b3db896afb94d6f3c27a45b70bf3733c719b7b15bc48f74c8", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "adaptive_card_install_and_commission_assets_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/adaptive-card-install-and-commission-assets:e668bf2844978c8f0ae32e94599e5cf23d250d3e322c3a3a4d844cc8a05d8d27", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/adaptive_card_install_and_commission_assets`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `adaptive_card_install_and_commission_assets_agent.py` is
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

Install and commission assets Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of install and commission assets status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-install-and-commission-assets
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_install_and_commission_assets_agent.py` and embedded as the fenced Python below (sha256 251bb212f38a1b1b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_install_and_commission_assets_agent.py` first:

```bash
python3 adaptive_card_install_and_commission_assets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_install_and_commission_assets_agent.py   # or on stdin
python3 adaptive_card_install_and_commission_assets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Install and commission assets Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of install and commission assets status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-install-and-commission-assets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_install_and_commission_assets',
    "version": '2.0.0',
    "display_name": 'Install and commission assets Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of install and commission assets status for embedding in dashboards, emails, or Teams.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'acquire_to_dispose', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-install-and-commission-assets',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-install-and-commission-assets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'da5a866170a550e6',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/acquire-assets/install-and-commission-assets'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/adaptive-card-install-and-commission-assets', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class AdaptiveCardInstallAndCommissionAssets(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardInstallAndCommissionAssets'
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
    print(AdaptiveCardInstallAndCommissionAssets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
