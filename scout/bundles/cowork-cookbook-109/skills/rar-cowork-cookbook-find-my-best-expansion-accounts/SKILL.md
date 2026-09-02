---
name: "rar-cowork-cookbook-find-my-best-expansion-accounts"
description: "Surface the accounts most likely to grow - and arrive at each one with the expansion case already built."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/find_my_best_expansion_accounts", "rar_sha256": "173643220b7c6bb75a7e6e15a60d7c7d621a4669c4c9c907769e2f2c97cc3e67", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "find_my_best_expansion_accounts_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/find-my-best-expansion-accounts:ede3e817be6186237451d266cc3496eff766ef3877bb57d2a937a650ff7114c5", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "prospect_to_quote", "intermediate", "integration", "dynamics_365_sales"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/find_my_best_expansion_accounts`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `find_my_best_expansion_accounts_agent.py` is
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

Find my best expansion accounts — Surface the accounts most likely to grow - and arrive at each one with the expansion case already built.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/find-my-best-expansion-accounts
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `find_my_best_expansion_accounts_agent.py` and embedded as the fenced Python below (sha256 173643220b7c6bb7…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `find_my_best_expansion_accounts_agent.py` first:

```bash
python3 find_my_best_expansion_accounts_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 find_my_best_expansion_accounts_agent.py   # or on stdin
python3 find_my_best_expansion_accounts_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Find my best expansion accounts — Surface the accounts most likely to grow - and arrive at each one with the expansion case already built.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/find-my-best-expansion-accounts
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/find_my_best_expansion_accounts',
    "version": '2.0.0',
    "display_name": 'Find my best expansion accounts',
    "description": 'Surface the accounts most likely to grow - and arrive at each one with the expansion case already built.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'other', 'prospect_to_quote', 'intermediate', 'integration', 'dynamics_365_sales'],
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
        "upstream_slug": 'find-my-best-expansion-accounts',
        "upstream_url": 'https://coworkcookbook.com/recipes/find-my-best-expansion-accounts',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'c9d998441be5b302',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-sales', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/estimate-and-quote-sales/conduct-upsell-cross-sell-or-repeat-sale-prompt'], 'recipe_category': 'other', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/find-my-best-expansion-accounts', 'uses_skills': {'custom': [], 'ootb': ['Communications'], 'plugin': []}, 'verification_status': 'draft'},
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


class FindMyBestExpansionAccounts(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'FindMyBestExpansionAccounts'
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
    print(FindMyBestExpansionAccounts().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
