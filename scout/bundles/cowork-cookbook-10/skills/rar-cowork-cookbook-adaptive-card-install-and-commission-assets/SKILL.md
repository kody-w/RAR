---
name: "rar-cowork-cookbook-adaptive-card-install-and-commission-assets"
description: "Produces a reusable Adaptive Card JSON snapshot of install and commission assets status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_install_and_commission_assets", "rar_sha256": "251bb212f38a1b1b3db896afb94d6f3c27a45b70bf3733c719b7b15bc48f74c8", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_install_and_commission_assets`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_install_and_commission_assets_agent.py` and in the RCI capsule.

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
