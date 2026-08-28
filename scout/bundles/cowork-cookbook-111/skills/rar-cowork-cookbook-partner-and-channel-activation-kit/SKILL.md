---
name: "rar-cowork-cookbook-partner-and-channel-activation-kit"
description: "Adapt the [Product/Campaign name] launch materials for partners and channel teams and route them for review."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/partner_and_channel_activation_kit", "rar_sha256": "671861042a9a2b2268b882baace5e9f62f131178ab5294e1722fe71b76c3bf36", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "concept_to_market", "intermediate", "read_only"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `partner_and_channel_activation_kit_agent.py` and embedded as the fenced Python below (sha256 671861042a9a2b22…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `partner_and_channel_activation_kit_agent.py` first:

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
    "version": '2.0.0',
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
