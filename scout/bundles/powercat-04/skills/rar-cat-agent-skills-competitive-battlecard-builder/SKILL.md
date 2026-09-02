---
name: "rar-cat-agent-skills-competitive-battlecard-builder"
description: "Build an interactive comparison app, either a sales battlecard advocating for your product against named competitors, or a neutral, unbiased comparison across two or more peer items with no side taken. Filterable by item and category, with live search, a compact scorecard, and copy-to-clipboard talking points. Every claim is tagged verified or unverified so nothing invented ends up in front of a\u2026"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/competitive_battlecard_builder", "rar_sha256": "0b7356f6516b4afaabbed99ae04111381a60d133eeba92effdad8545f2f05ddd", "source_kind": "rar-agent", "source_commit": "cdba6310faf6c2aa731f37d58cfe8e921a360080", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "competitive_battlecard_builder_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cat-agent-skills/competitive-battlecard-builder:4692329ff55f18521e06bee588972515a36180cf2262063f55feed9e73e99147", "kind": "skill"}, "version": "2.0.0", "author": "Michael Heath", "tags": ["sales_enablement", "productivity", "comparison"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cat-agent-skills/competitive_battlecard_builder`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `competitive_battlecard_builder_agent.py` is
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

Competitive Battlecard Builder — Build an interactive comparison app, either a sales battlecard advocating for your product against named competitors, or a neutral, unbiased comparison across two or more peer items with no side taken. Filterable by item and category, with live search, a compact scorecard, and copy-to-clipboard talking points. Every claim is tagged verified or unverified so nothing invented ends up in front of a…

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a analyze capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#competitive-battlecard-builder
  Upstream author: Michael Heath
  Upstream version: 1.0.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "data_source": {
      "description": "Optional. Where the evidence comes from.",
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
      "description": "The question to answer, stated as a question.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `competitive_battlecard_builder_agent.py` and embedded as the fenced Python below (sha256 0b7356f6516b4afa…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `competitive_battlecard_builder_agent.py` first:

```bash
python3 competitive_battlecard_builder_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 competitive_battlecard_builder_agent.py   # or on stdin
python3 competitive_battlecard_builder_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Competitive Battlecard Builder — Build an interactive comparison app, either a sales battlecard advocating for your product against named competitors, or a neutral, unbiased comparison across two or more peer items with no side taken. Filterable by item and category, with live search, a compact scorecard, and copy-to-clipboard talking points. Every claim is tagged verified or unverified so nothing invented ends up in front of a…

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a analyze capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#competitive-battlecard-builder
  Upstream author: Michael Heath
  Upstream version: 1.0.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/competitive_battlecard_builder',
    "version": '2.0.0',
    "display_name": 'Competitive Battlecard Builder',
    "description": 'Build an interactive comparison app, either a sales battlecard advocating for your product against named competitors, or a neutral, unbiased comparison across two or more peer items with no side taken. Filterable by item and category, with live search, a compact scorecard, and copy-to-clipboard talking points. Every claim is tagged verified or unverified so nothing invented ends up in front of a…',
    "author": 'Michael Heath',
    "tags": ['sales_enablement', 'productivity', 'comparison'],
    "category": 'general',
    "quality_tier": "frontier",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cat-agent-skills',
        "source_name": 'CAT Agent Skills',
        "source_url": 'https://microsoft.github.io/cat-agent-skills/',
        "upstream_slug": 'competitive-battlecard-builder',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#competitive-battlecard-builder',
        "upstream_version": '1.0.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": 'd2d932cf8ec2e523',
    },
    # The platforms the upstream entry targets. First-class and queryable, not
    # buried in prose: this is what lets the registry answer "what can I launch
    # into Copilot Studio / Cowork / Scout", which is the whole reason an
    # agent.py container beats a bare skill entry for cross-platform reach.
    "platforms": ['Copilot Studio'],
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
_SPEC = {'archetype': 'analyze', 'checks': ['The question is falsifiable and answered directly.', 'The decision threshold was stated before the result.', 'Missing evidence is named rather than silently excluded.', 'Uncertainty is quantified.'], 'confidence': 0.667, 'deliverable': 'A decision-grade answer: one-sentence verdict, method, evidence, uncertainty, and what would change the conclusion.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'data_source': 'Optional. Where the evidence comes from.', 'subject': 'The question to answer, stated as a question.'}, 'refined_by': 'rules', 'signals': ['tag:comparison'], 'steps': ["Restate the question so it is falsifiable. 'Is X better?' becomes 'Does X reduce Y by more than Z?'", 'Declare in advance what result would change the decision — this is what separates analysis from justification.', 'Identify the evidence available and, explicitly, the evidence that is missing.', 'Compute the comparison, holding the method constant across every option.', 'Quantify uncertainty. A point estimate with no interval invites false confidence.', 'Answer the original question in one sentence, then show the working beneath it.'], 'subject_label': 'question under analysis', 'verb': 'Analyze'}


class CompetitiveBattlecardBuilder(BasicAgent):
    """Analyze agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'CompetitiveBattlecardBuilder'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'data_source': {'description': 'Optional. Where the evidence comes from.', 'type': 'string'}, 'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'The question to answer, stated as a question.', 'type': 'string'}},
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
    print(CompetitiveBattlecardBuilder().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/+15WZOjSLbmX2GiHzLrKjLEJpZoa7NBaEMLSAIEqLIsk8VZxL4L6tZ/H0dSRGTerq7b12we5mGUZpEs7sfP+p3Pnd+fzLry0+Lp9WkX2L4JImQFzMp/en5yQGkXQVYFaQLfTusgchAzQYKkAoVpV0EDEDuNM7MIyjRBzCx7RkBQ+aBATKQ0I1AilllVEbDNAk50mtQ2qyDxEDctkC6tCyQrUqe2K8T0zCApKyQxY+DcZIIqqNKifEbSQVgC6qowo2ekTqzALB9j3ta1i7QskapNh8FxWgAkA1CHoAJxibRQISRJkTJwAFKZIUhekEUQDRZYEUCs7jYOmgVlmhXw0qJ7vk+KBvtKYBa2/wx1uK0IdS1tuMJg0fN9Upp1X6r0ix0FmZUOhlZmFA5WZil0VPmCzBtQdIgdmUGMBFBP0/OgAfBh4AbwAupcJ+93ZQqVrfxhfgCfQk87CEicEqkz+ABxizSpkNRFzK81juIUDBK4mnEGff30+utvz08BvH56/f0JLlfCR0/8w5fQlul7LG6RBAWcHJmJB0dlHcyABN5noIDBieEjB7jI4+5zCSL3GfmP/whbs/DKX16/Jsjj9/Vp+HesEwSGHalSsxwUts3MtIIoqLoXhItasyuRAlR1kZRDYlQFtO7lPvNDUpoh/xjefb4v8uKB6vPXpxSqYA759/Xpl8FTX5+Kerh+GaRkn395idIWFJ9/+ZBT1tYFwDBBYVDrl2+P+4dYOPBjaODeVv0HlHrPdAt8ffrBuOF313uwE858ernAmH6+C4a5C+NjJjb4/Mu/Emv7wA6joKz+Lbm/3gX7wITB+fxQ/Jfnm5N/Q0YPg95l/utlMxjW/4klcPjbcs/Iw1H/SvbN//9FdBQksNbfPP6n4v5swugfyK//0ra/mvCMuF+fZmAo0FsVvyK/f5P3c/7XT87Hw0+//QFF/7diZIhD9k3Ct9hMAheU1bdvv34qb48//fbrpzqDuQbM+FtdRH8m88/8elvnJw8+Rn3+eS5cX03CJG0T5D3Tkd/T7H8Vf7wgJzMKnI/n5SvyY70MvxEyGPG26N0FP9RMCXX9wY+/PP0B8QHCbAEhd3gNq/xvf0Mg6EP8TN0Kke20rhAY4CqIwaC84kO8Uh5F/V3eCNvtS+x8v6EYLHcIEWYdVciyMINowPIh4oMFEJ++/2+Ipl9MDyLYlzIMoqgc2x9Q9O2jL3yz7mD0/QVRfLhqWgRekJgRcuT2e+QmYFjvlhllHX9phiWhOsEdco68MMBNWUfg78j3v17i203aS9YNFnxNYEhg14GiIP5naQG7SdQh5gBRVleBLxBXIYwUaRRZph0iw586exncovkgeTjLhu0QXIFdVwCJYHuLEDeAWPwM412mEewf1eDCmwMQJ4B9Aza17tY3oJtfB2Hfv3+3zNL/mtwxmEDuLbccwwHvCiNfvmQFcKPA86uvCbD9FPn0+x+fkP9E/mrWTfiwxt4s7xGDeRwha1kSEViUdQyHlciQERBxbkH7/Y97GAbtEthCH23pNhlK+8iAwYJ7bN4CA20eVATFY6Wf/Ya0PvQLbLXQW7C8y+evySAiHchCG5TgzYn3yXfXv0X6vs4Qk/LhQxgn2Ajj29hb8g3BhG3ZeUEEF3n3FDQXxrUaIuqnkF04IIOtFCR2B2ea1UcIYceFfKUKShf2/rqEpg6Sv1vFjZWAGOKSWX1Hdvwetrg0gn8GB92Wh7PTJBgC/0jV+2MopPgEc2z6JuIFEQH0JgJJi5n5BeQwt3Guec+IgeU85kPhA+FpkaGVgyFGt2K+Zd4P3Rz5aOfIo58jAyfASOT/E7X/94jaED1uuTzOl5wynyFzUTka91Kz4cAh8ncWDjnTzes33PjgUW+Q+9aMviZRANOz6P5+H+nequs+5g7wdQEVOnLHm/wB54qb3KCCNTIkfVEMdW1+Td663uA6aF05ADiEsnAAxvR9wbtj75r6EK+G+w8GhNzLb/AzLGwkq60osBEXAOeGAZVfDAjzSE9YMGDwDIQE2//JKujACkYAykegEgGsXNgZb4kvPlx9K/v34cHAK++pCbWF6QxeEG2obFidMKUBJIfDGOiFTzdRSAygj6GK7x4ufTO7K5MW4ZuCJrTDjLoe/BiAxztYpEN3hcu9IxAUajpmBV3ZwhhAgLneA/uu5iNUUNd4qJ7bpJ+j/TAV+bE7/31AIajiRws0o+hWCh++ga2rgKUzpDekHGEJcS4Gj/yBiXDjMC93GnLnOe+6vCI8pyDcTbZ868/I5/iNCdxIg/pzUF4Rv6qy8nU8fh/24sHqq62XIB3/U7P/2w+t+MsHuHx5tOKfFrj74hX5afv504hHXr4i2Av6gg6vtoENhsR7/F5/LM3PP1w/wnYLC4BIkNxQGGbNkKKlD5wbSzuCj7hCbdIYwt/g7m6AnbfW+jYE9levAN4w+N5qy6FDt5AU3GTfWuV77B+FAQ1LvIEXQNj4KNghbkMk74F670TwVTL0OGegsh54GfZpg7kleHpN6ih6fhrg97/f3A29BiYn9N2wI4R1AolhFYDb3ZCw3+7r3m5/2ulLtwszGqoJFtW9JzeBc/M4DCwEjiH7B8WqLhs0uW/qBoL5zj7/WeytNCGmOOnrUKGQMMCdwjPyTvqfkbdt2CAZJDXch/46bDgGW+BQ+N/72PfTCQs8/fYnajz2H/+sxFCZeQ3xbsC5odcmJdxBwsBU9+gPbOHt/Z8YCEUXIK8hDXEG5T6s/VAiva/8x03p6r6d/v3pDSWG6zsnuicPnPBvstbB/De28W0Qaw6Tb/V288aNjH8zYYgHVvHDK2+gSN/umfj0CgEGPD/BybBE4A6jv50cPN11gUZ80HgoAULFl3JgSWNYeFAS5C7ZYABsm84PCwyPA+c2frh4/Uvu/ydo8EpSLE7grOtOJi7GTHAMoJQFwIRhWBqfYBOToDAGtV0cp3CUIoZhsLewgCYAy2IkDXUoYWrE5kOHMTa4H2r/7uP/6Xbk6T4d9gd8QsH5qEUTE8qlJhhlkaZrmpYFFWBNgJIYhhEMZlKogxEEAJbJ4sB1HdNhJuTExV104jjOIO9Bie86fXvbfrxF5F6M36BacXDLCtg7KQJDXdOlbNw0aQJzCdqZMLYLGMDiGHQKijJDWB5TH1EZgnY3e8hWyIYhF22GdX5/RHnIQIqEI1dkKXD3Hz8eQRMm28t1qo8Kyk2D6QhvTfHsp0JIhFcP56ryZMxEerrmp5mTyThOL0+hTFVnEsJRRgYL0r+0hjLZNsly4tBHzFDzcHMyl3i7KUeuW6C13ifSde0vOXPPxLhfbC3qmMb7zNKyINbOgcAUiWzmi9mYZTZ7eqsdYmd5Pm00SbtYi31UFWF8ni52x9MGb4kwU7jupBqlhqldbUcXU9fwRV4zi33NbMLTcRKGJ61b6WrsLoPwWp9sgerOJiMupGNIr3cny1Sp01HFT+stieu5Pdp1ImoZukrzOH1V04hvD6caEzVh5aGyxlM7ZW12zCkKw6TOVauY7qLTpdYOtO6FkwxT0obFJGJj6vRS1rdgJi1mehtYM/Wq5JylOHjciIGL79tQSbRrL8XBKbd0Z1cGPiXu1mvazldCQ0ZKXjh8q1K0XnMcoDJ9OWN9+2wTrsJNLrRh4WbfLbKr5JelLOQlNyvlou+FjFmD434/bgueJ0cjoHSdbOtbWEiLkBm5RDJx5COwAi/GOeOqOZGoxzl9Jp1Zbs9PPJ2oGwW9qN3UXtimJsfU7MSzWw2QrlQuT34iMTx3OGSbfL4523pEtYA0NivZxPFQ9+PU8krxINQeRezYeXqWe3pWGddlIApMU57ruHdXksFQUu/KpQCOMyu49kshIqWlbQfnLXfpmiiPpauaZ2c+uZisN58dkuS8PieQKl3xkU+idLlvlpbv1J62m0+t8RLoR3XV1q5d77dR5esrRS2i0l8TgjHV1kVvyUGx3YQ7Ne91O/RG9V5br4xN4+H8sVjFKVom/GkCbDyWT16DjtHxyXGzajvVmDUetltBPM9ktFOP5hL0HstfjwXWesuxyFjL2SXy8gU7li9Ux6S50KZaw1PgGLSmvhaV2vKyLkwgvT54SsaFJy7I+pwW441iTU77RXsA4jEtpDkuLMZdv4P5vopwZjEF5cjWMCXaXa5RJfrnoKE5pdPH1mw33VlmW/ZSj1XZRsCC/GoeL+n4CJZOuVYTP9GcxtcIe6XIRnlZo+XieKLZvkWvjO/Jh42vuZs4JPTD0vX6/dVqDh5I+VMz8g3VoCFgWQ7jV4QbSaU09TbZmcz2G9tOTy26nJx2Xj2VK3M5X7qhRs2NEeFLeby9qL6iJZXt8efTKBcPYTPakPGmsQRtpKIti03nOOWOLf9QRRZ3EKa8NjmoGzIHfEvxsTdvuSWTOdI2nfIkdK9v8ovDfpHW1Gpqb215UnN0djUlQZwHsR1Y3NycNXrCCCzpyNW8vV4cVzkeNI6yTzFqnxKyFnrGrdlOTRZLJR+5azZVc6dtzIYgxAkWR8RmxE6LMUFaoyubHVayowdHOdADQuv6y8HYL/Irvzhzkn9lZEy9UOdgwkueRU4Tdu9qBSVNCGxE+4dJezzrWl6MmvVmVbRxtpiQTrlqCJyidKqphGhFZLN12Vk9n7Ubg5tKvs3O+lEALr4j5+LlRMn+gsC2++XIVDt5xJ6xItQuajZGNd+I+K1Ry3uRaA45pa6IjS8wR4AfTSpcyKwS1bgpCIoSTg7peI6d5rUjZZh9FhSHN9ahgI03F05oiUzDeVSeiavLqMx7tVpgPeNVokyJPjAYaXqu5JU9Y+fOMlfmSXcx+FFOWThub0LsXIg1ba9XIkGZ+JWkMGCj6JJ0+lK4okLGHt2ZHpcFlV64NKJmk4V0jmPKGHnRMs82/UQYN4mtFXvqQipbbMxmEx0s3GQ9ni+8TbnIl4S4k8/h2kl5zl4o+jHdpuvZUnTpZtNyswWQVLOiCg0zIvIwzVfmKcN2fbRp6DKYahEE/wkTthYakH3Z7g3f6nZJIIPgdNQ0q7+OIu5c64G66LNFSWR+jioJ6R/2MU85ge9c9SpqqSS2JxOcVs60PD9vfdGVTGllqRJWgtpTJJKnOGBw9ZHV3fjIA8ONQ8fDM0igRmCajXcyjRXy3q4PNc8ts3i7w8Jed+tZKAiNTHRovh6Tx4Uub6bgauYteRE5mDScOBnHp7PBbNTmsBCtUBfZOp6drgp73GynBoXiF92g9jJ2PtKodfCDtahFDemHhheiYpPtSbBlVUMQ+UPPLzoKX7Qm15ha0k7SjJCC3EiDtTbZ79wkR8lad8MjZ6RcaXQdVwd7G9+KQjaX9kuUoccrMLmy5r5oxNClBXpieVUyxyN2hE4PR8Prdt5GkJSEltvpvKk3PE+pM9Vj7D64ROJ+yhyn61W8s2A32iyCEdgT0bxa+nPipJ9dc7HczPQ9Tof7+SGw5qa6Agczguqt0BWmbxaxuqWdZhOIOqd45MGs1wdbDdSQp+f+qVilYmrPFmFT+f52ttIkdVkFfE2al/UJ7pvcM5saVEHnx8DdnZJlkHanljCMtUDmpaFjQm0dN+gsSukJOGypECXW8opO/Vqec4pghutTIZ1UMqP3hjcaSTMCrL2U9KPdsfQWC5I4rkeVvC4L10otPEXJHXNYdvyxlFdOnV3GAVqeDUONpZnQebvZtmbkuAJdD5Zbhbf7eLVlSPgGN3TnEi+3nbHK7c40hCm7w8W2WPHZaF54fLLeAnyyinh1i01WqRAxrTU5ZBd9v6np5AqxwzVVbH3NIctsQkcIXQuU86VdJIUyqg1Z3VjggpqEtuhzleNbCdcBm7lCtdtR7LFIJKrmWgOlrnNru6hOzHJN5iePWLKBPZvmMS3PzsJlQZ1LxQ0VW/Pdrc/PxvZeNfc2qm67+Vz19oEpS7qWHc/y5Mi4l5RvUsbeUIu9HM2jXbx0qkt63Tb2jhOtaBs5SsGp5hHrCHG8ODTHS7UPaiY/sKEmY9WKPcbMRYWF3uyj2dkXdQUTkpPNxSfvEpsOKxnGYSOOqCDmRXHmq1VI+XguKr5n5kuPOfvzrbCbBRqRGqSbU8a0dhYGi7m6npR1F1rBoVnFrbowwuqaH0JGuaLELjiBQkrwxTSTzgtWLfYKX6lSx/V7SivF2cqdCblwnevqmdGZIxWOWBtvxQ0aaFo7T1SpwHzbSgI02U0zKlbD/HoM9me+Jck9N8H3ckdNLhdcVWWnh4y/t2n1Ek1G5DXG9kyKLg/UUSdPhVstQ7Pw0SC45p0EPGt+GHlHujIzssIk9pLuq2rZgobCY7yhWH1mUiKJRwzoNzOHc+O86T2XrnsxNSQxsXR/7xmJb7bX/bkAxWJvpWYYTcb8EkV3a3Z24FLipHT+LLBC4LQsozJ1rk36NOCweNbaDsr05ZVcLuV+dDnh60O6HtOOsBdVbHvZUdFJg8xg1xmMge22nadEzbQSV5jIOIxlugtfAvy0ama7vYnriZ7FxoJx5yEVa3THrEd4SPI9fh6PmvlqzC3OsrVSRtvxaN1MULj7WnWzvUZd0XgGu5ctb3gMz/b1zJYa+UqpZtB7YTSGfEMZe6q0gkgQeTVaHDx3vpWv6nUydeFWYE5k1dwwlUBany88YC29iJySlA5RCw3VzhqkMDOi9qrTUjbEldNhDdgZ1DHmrv0GV3abplXi8lDtmLrgNGVP42mduO1ktaZovq7Ei0j0EnWgLbopluWxJ81GB362XZ+3I33RixcicVeA4zpD6XFn6qxX59E2S42Vnkt95Zwzl6IZfaUHy+O0wN0lw13VUGGNMU/ZsxUk57OqFrI+O45wocS2regapxNuKOZ1HI3MhZKcWofLmYZa9CvZtRoSnUymDJhHEr8npMlZmrpNsKlOm92hssrj1Ii28WnXzTD8OtZL1lZX07nf6FmNXux5sULBRfdTsCWcVFntV7Xoymk7bmU00G16wZzF0VrrGEYpimQnJHPHxLqMUXJllvfFOEuKlpTaMgi2hNdNaUgabFZy1sdEOK6iRcxX06O9a/RF5KHlcj5SphreYNXBkW1z7u8a93oC15ki7jARR3EucSIn2MZwbzMCpIqvpV3W72s0OTfzOSPMF9Flr+S7thgbMTuKN5Mp0QGi0fHLNlX96zRxZ5zC5F1dKgdLWnpWG2GS3dqQjW4u7GSnK2OqW2uzKmtpvy2XhI3WfnzAHZs+N3adn1ma1QkB7l4mHbpv2cVpyy6tqyxmuicewDx0ORAqalJdztzsZIwPTpYeryl+6HgdAgA3cVj7yhrxWpqEFHlUSK9ySr3cXsjWskZT+nwuKYLeNApwXW2161fCbOwyMLsPTMaPplbTGCPLI/v1OBNTjfa0MQnYk+VP6G4lo6ux2+7HvbQ8EJhrLFvmRFNZkITz5LSKhXXZijsbxYpeL6MxqXTmyQAC6nAYi293ihGMl+d0CetnTTVNgOOMK84PO2vno2xZX0/kTqdUur7o9nanNeNlSsTNIlvoft95HLVykpZr0emWNwWUuC4SOpmmR8rK3ahWOrpwnbzWL5e6WdNStPR5La4WbDgOKeeQ0tKsneQ5nfHKKKF7v+f4a+uPp2iqhe21ZS55I2xp7SzvKK4/EprskSOMdvLo2GtsVKh2Y5fsammf9vHEXRcWRxDEjF/xZ4JqpmPALMtujsO6IFzP75lxyXb7FPYRgSe7OXmu7HOq1koJBHxLTHQvmrGKaVDmeWThh2lf1wRnk1NNWnfEOBWOnmkRwkEp2cUcMOZ6S8XdlZmvLjR5uQBsrCqbDRVnldJHmKMY6zFHjOaCnOzXB457en66fZ58emUpmn1+Gg53H0e0//7ZntcH2beHGILAmOen/3uHT/eDoLevNbdTVWA6r7fVX/9dFX97firsAKpzPwsso9p7nDb917O1L3993DdM7u7fVYcvStfq7Vi7Mr3bYeTtk+Q3qKx1/wD6dNN++AAZNEF1Owh9/6o4qPX4PAC1wYfvA09//B9b+VVd1CYAAA== -->
