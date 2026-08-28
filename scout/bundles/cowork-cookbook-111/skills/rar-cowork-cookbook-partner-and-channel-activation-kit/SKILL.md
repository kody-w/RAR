---
name: "rar-cowork-cookbook-partner-and-channel-activation-kit"
description: "Adapt the [Product/Campaign name] launch materials for partners and channel teams and route them for review."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/partner_and_channel_activation_kit", "rar_sha256": "fd41112672b2f16c02e2edc8c291971953c63c22a87262228559900ba11041fe", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "concept_to_market", "intermediate", "read_only"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/partner_and_channel_activation_kit`. The original RAPP
agent is preserved byte-for-byte in `partner_and_channel_activation_kit_agent.py` and in the RCI capsule.

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

Partner and channel activation kit — Adapt the [Product/Campaign name] launch materials for partners and channel teams and route them for review.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/partner-and-channel-activation-kit
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
    "criteria": {
      "description": "Optional. The standard to review against, if narrower than the default.",
      "type": "string"
    },
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
      "description": "What is being reviewed \u2014 a file path, URL, document or system.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `partner_and_channel_activation_kit_agent.py` and embedded as the fenced Python below (sha256 fd41112672b2f16c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `partner_and_channel_activation_kit_agent.py` first:

```bash
python3 partner_and_channel_activation_kit_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 partner_and_channel_activation_kit_agent.py   # or on stdin
python3 partner_and_channel_activation_kit_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Partner and channel activation kit — Adapt the [Product/Campaign name] launch materials for partners and channel teams and route them for review.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/partner-and-channel-activation-kit
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/partner_and_channel_activation_kit',
    "version": '2.0.1',
    "display_name": 'Partner and channel activation kit',
    "description": 'Adapt the [Product/Campaign name] launch materials for partners and channel teams and route them for review.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'other', 'concept_to_market', 'intermediate', 'read_only'],
    "category": 'general',
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
        "upstream_slug": 'partner-and-channel-activation-kit',
        "upstream_url": 'https://coworkcookbook.com/recipes/partner-and-channel-activation-kit',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '057c7b6e05b24458',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'none', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/prepare-marketing-campaigns/create-marketing-material'], 'recipe_category': 'other', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/partner-and-channel-activation-kit', 'uses_skills': {'custom': [], 'ootb': ['Word', 'Excel', 'Email', 'Communications'], 'plugin': []}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'review', 'checks': ['Every finding cites a rule ID and an exact location.', "Coverage is stated as a fraction of the inventory, not as 'reviewed'.", 'Severity reflects consequence, and blocking items are listed first.', 'A clean result explicitly says what was checked and found compliant.'], 'confidence': 1.0, 'deliverable': 'A findings report: inventory, per-finding rule/location/severity/fix, coverage fraction, and a re-check delta.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'criteria': 'Optional. The standard to review against, if narrower than the default.', 'subject': 'What is being reviewed — a file path, URL, document or system.'}, 'refined_by': 'rules', 'signals': ['word:review'], 'steps': ['Establish the standard first. Name the specific rule set being applied and its version; a review with an unstated bar is an opinion.', 'Inventory the artifact. Enumerate every reviewable unit (page, slide, endpoint, control) so coverage is measurable rather than asserted.', 'Assess each unit against the standard, recording rule ID, location and observed value — never a bare verdict.', 'Classify severity by consequence, not by how easy the fix is. Blocking, major, minor.', 'Propose a concrete remediation per finding, with the corrected value where one exists.', 'Re-check remediated units and report the delta, so the fix is evidenced rather than claimed.'], 'subject_label': 'artifact under review', 'verb': 'Review'}


class PartnerAndChannelActivationKit(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PartnerAndChannelActivationKit'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'criteria': {'description': 'Optional. The standard to review against, if narrower than the default.', 'type': 'string'}, 'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'What is being reviewed — a file path, URL, document or system.', 'type': 'string'}},
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
    print(PartnerAndChannelActivationKit().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
