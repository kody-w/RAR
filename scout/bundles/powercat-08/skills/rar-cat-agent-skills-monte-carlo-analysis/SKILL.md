---
name: "rar-cat-agent-skills-monte-carlo-analysis"
description: "Run Monte Carlo simulations from natural-language risk inputs \u2014 triangular, normal, uniform, or log-normal \u2014 and return percentiles, a histogram PNG, optional interactive HTML, and a downloadable results spreadsheet."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/monte_carlo_analysis", "rar_sha256": "33b7c20af7270399ddff663b9d1f2e284248d5d4d316cf53a57fb526dbaaadc0", "source_kind": "rar-agent", "source_commit": "d16979f79339ed06511e0bc50c363f1286d140c7", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "monte_carlo_analysis_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cat-agent-skills/monte-carlo-analysis:3e5c458a38ad2d6f313e1ad0403124d3fadf07754895d18f50a680c7f06fe3bc", "kind": "skill"}, "version": "2.0.0", "author": "Nazish Qasim", "tags": ["monte_carlo", "risk_assessment", "python", "simulation", "matplotlib", "charts", "csv", "analysis"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cat-agent-skills/monte_carlo_analysis`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `monte_carlo_analysis_agent.py` is
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

Monte Carlo Analysis — Run Monte Carlo simulations from natural-language risk inputs — triangular, normal, uniform, or log-normal — and return percentiles, a histogram PNG, optional interactive HTML, and a downloadable results spreadsheet.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a analyze capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#monte-carlo-analysis
  Upstream author: Nazish Qasim
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `monte_carlo_analysis_agent.py` and embedded as the fenced Python below (sha256 33b7c20af7270399…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `monte_carlo_analysis_agent.py` first:

```bash
python3 monte_carlo_analysis_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 monte_carlo_analysis_agent.py   # or on stdin
python3 monte_carlo_analysis_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Monte Carlo Analysis — Run Monte Carlo simulations from natural-language risk inputs — triangular, normal, uniform, or log-normal — and return percentiles, a histogram PNG, optional interactive HTML, and a downloadable results spreadsheet.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a analyze capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#monte-carlo-analysis
  Upstream author: Nazish Qasim
  Upstream version: 1.0.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/monte_carlo_analysis',
    "version": '2.0.0',
    "display_name": 'Monte Carlo Analysis',
    "description": 'Run Monte Carlo simulations from natural-language risk inputs — triangular, normal, uniform, or log-normal — and return percentiles, a histogram PNG, optional interactive HTML, and a downloadable results spreadsheet.',
    "author": 'Nazish Qasim',
    "tags": ['monte_carlo', 'risk_assessment', 'python', 'simulation', 'matplotlib', 'charts', 'csv', 'analysis'],
    "category": 'devtools',
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
        "upstream_slug": 'monte-carlo-analysis',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#monte-carlo-analysis',
        "upstream_version": '1.0.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": '8a9d6a293cabe5cc',
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
_SPEC = {'archetype': 'analyze', 'checks': ['The question is falsifiable and answered directly.', 'The decision threshold was stated before the result.', 'Missing evidence is named rather than silently excluded.', 'Uncertainty is quantified.'], 'confidence': 1.0, 'deliverable': 'A decision-grade answer: one-sentence verdict, method, evidence, uncertainty, and what would change the conclusion.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'data_source': 'Optional. Where the evidence comes from.', 'subject': 'The question to answer, stated as a question.'}, 'refined_by': 'rules', 'signals': ['tag:analysis'], 'steps': ["Restate the question so it is falsifiable. 'Is X better?' becomes 'Does X reduce Y by more than Z?'", 'Declare in advance what result would change the decision — this is what separates analysis from justification.', 'Identify the evidence available and, explicitly, the evidence that is missing.', 'Compute the comparison, holding the method constant across every option.', 'Quantify uncertainty. A point estimate with no interval invites false confidence.', 'Answer the original question in one sentence, then show the working beneath it.'], 'subject_label': 'question under analysis', 'verb': 'Analyze'}


class MonteCarloAnalysis(BasicAgent):
    """Analyze agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'MonteCarloAnalysis'
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
    print(MonteCarloAnalysis().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/91aWZObWJb+K0z2g11NOgGBAGVHRQxCaENCLBIgyhU2+76IHdXUf5+LpEzb3VXVMxHzNHKEUuLes5/znXOv/NuT2dRBXj69PgnmNawCSDKrMH16fnLcyi7Dog7zDCzKTQbt86x2IdYskxwCe5rEHBcryCvzFMrMuinN5FNiZn5j+i5UhlUMhVnR1BX0uZmgGAHVZTiuJmb5DGV5mZrJM9RkoQc+PkN5CSW5/+n+/I3CzByodAHnDCrc0nazOkzc6hkyoSCs6twvzRQShRWgvikKCEOgY2naddi60Pq43z3feJiQk3dZkpuOaSVAN7dqEqBXVZSu6VSB69YvwGS3N9MC8H96/eXX56cQfH56/e3JTswKPHq6mX+zngGChiqsAMloLlgrBuDEDHwHWo7mgEeO60GPbx8rN/Geob//Pe7M0q9+ev2cQY/X56fx3+jdOnChOjer2nUg2yxMK0zCeniBmKQzh+rhhQpYUgE3Zv7LnfIbp7yAfh7XPt6FvPhu/fHzUw5UuIXp89NPo4s/P5XN+Pll5FJ8/OklyTu3/PjTNz5VY0WuXY/MgNYvXx7fH2zBxm9bQ+8m9WfA9Z4tlvv56TvjxtcjekBTQPn0EuVh9vHOuCjz1s3MzHY//vRnbO3AteMEhPp/xPeXO+MAxBTY9FD8p+ebk3+F4IdB7zz/XGwBwvq/sQRsfxP3DD0c9We8b/7/J9ZJmLnVu8f/kN0fEcA/Q7/8qW1/RfAMeZ+fFm4CiqQcC+IV+u2LInLsLx+cbw8//Po7YP1v2Sh5Awpz5PAlNUExu1X95csvH6rb4w+//vKhKUCuuWb6pSmTP+L5R369yfnBg49dH3+kBfJPWZyB2obeMx36LS/+o/z9BVLNJHS+Pa9eoe/rZXzB0GjEm9C7C76rmQro+p0ff3r6HaBCBqxp7NsyqPK//Q3ah3aZV7lXQ4qdNzUEAlyHqTsqfwQoBR0fRf1V4Te73UvqfIXA07HcAUSYAIegVWmGCQTqYYz4aEHuQV//0zbrTwBIs/pTFYdJUiHpCEBf7BGBvpgPCPr6Ah0DICsvQz8c8U9mRBG6kY1SbvlQNemndhQElAjvQCOzmxFkAAq6/4C+/hHjLzceL8Uwavs5A+43QUwcqHbTIi/NMkwGyBzhyBpq9xNATgAZZZ4klmnH0PjWFC+jC7TAzR6Osc0McnvXbkAXSXIbKOvd0RzAcZ4AvK5Hd92MhZywBL7Iy+HeAprsdWT29etXy6yCz9kdb3Ho3qIqBGx4Vxj69AnAupeEflB/zlw7yKEPv/3+Afov6K+obsxHGSJA+5uPQM4m0FY5CBAowCYF2ypojD5Al1uAfvv97vxRu8wtIVA2oRe6N2LA7Vu0bw3oFpG3cACbRxXd8iHpR79BXQD8AoU18BYo5er5czayyMHWsgsr982Jd+K769/ie5czxqR6+BDE6dagx723RBuDaeel8wJtPOjdU8BcENd6jGiQVzXIzcLNHDezB0Bp1t9CmOU1VIHyqLwBdO8KmDpy/moB1qNzUoBBZv0V2rMiaGd5At5GB93EA+o8C8fAPxL0/hgwKT+AHJu/sXiBBBd4EyrM0iyC0qzc2z7PvGcEaGNv9IC5CWVuB43N2h1jdCvcW+Z9P668dey3ueL//zgzeoBZrWRuxRy5BcQJR/l8T1d7tBt47z74gRkDAhrfa+/b3PEGUW/g/TlLQhDicvjHfad3y9D7njsgNiVIP5mRb/xHrChvfMMa5NmYOGU51ob5OXvrEqPZIMrVCHgADuIRXPJ3gePqm6YBqPnx+7eJAbqn8OgMUBxQ0VhJaEOe6zq3OqqD0RFvXgdJ544VC8rKDn6wCgLcQUIB/hBQIgQuBG69uU4A1QamrHsyvG8PxzkMaOE0NtAWlKP7AmljdYAMryDLBcPUuAd44cONFZS6wMdAxXcPV4FZ3JXJy/g9LaAb6l7d7wPwWAOJPnYjIO69igFTEPgauLIDMQBF2t8D+67mI1RA13SsqBvRj9F+mAp9383+MVYyUPFb8zCT5JZf33wD4L9Mq1sOghYdVwArUveRPyARbj3/5d6273PBuy6vEMscIebGW7n1M+hj+tY5b0329GNQXqGgrovqFUHet734YR001kuYI//SHP92a2Kfbk3s01sT+4Ht3QOv0PfnnB82PJLxFcJe0Bd0XNqFoEaBEY/XKyjvB8o70MfvPj9idYuF6wA0uMEXSJUxL0E9OrdRRna/BRMok6cAcEYfDwCv33vS2xbQmPzS9cfN9x5Vja2tA930xvvWY94D/qgGgLyZP+JJlX9XpWOwxvDdo/MO4WApG5uDM857vjuef5LR3Mp9es2aJHl+yszU/bNzzwjNIA+Bx8YjEigJgGd16N6+jbn55S7t9vWHg+ThgWxj4YD6ubewNnRufrZBNt0BeFSnHopR/v28M85e74PZv7K9VSGADyd/HYsR9FeA3M/Q+zz8DL2dUG4HvawBR7Rfxll8tAVsBX/e974ffi336dc/UOMxmv+rEmMRXhoAbSOkja0pq8DhCoSjvsd8bK5v639gIGBdupcGdG1nVO6btd+UyO+Sf78pXd9Pmr89vQHC+Pk+QtxTBhD85Wg3Gv3Wkr+MzMyR5FZQNx/cptMvJgjs2Hq/W/LHOeLLPeueXgGCuM9PgBiUAxi5r7cD9NNdA6D6t7kWcABY8KkaRwkEFBngBBp8Maodg9r5TsD4OHRu+8cPr38yDP9Tub/i7tQmprSJ06YzcUgPx3AXMx2UQHFsQji4ZzoeSlFTgp5NHYz2pqhJ0qhNeSjpubhlA8kVSIPUfEhGsNHVQOd3f/7PpvKnOxEA+8mUBFQ4blH2BDU9akKh+GzmOJ5Hkrg1czBv4k5oYkLQztQBGmKk7U1xc0p51nRCgm5mmo59c9RjRrxr8uVtHn/z/r3cvoACSsNRTwcjZ9TMo2Y4PnMdlJximIta9hS1cRL3sAlNOhgBLH96J31EYAzQ3dgxH8FAAYazdpTz2yOiY46RBNi5JqoNc3+xyAwzKH1n9YE+i0jvvIlmm20gx81MOEiYI6hC0ovbPRFdOvQonw5Vp2hT7uz7h47Ng1Qw2o3k2htaseFZg/gxZR/rGeddUNWXnNZrkOMVp9jNvoMXV5Ft1GbLpFdbnW7rwwxTLZquRZEod7y89iQynahDsstS+VTGk9lyW7X8IEpx4qRknFZJtDvjUuos1WO+LRwOTbj8ulSTpo54JwzLI3/tDzLQLr3MRHzduLtSAEOUZqRKeApVVSOTo3Ex5mE+mRglgdthYbdZuiwktfCTszGRKzNpEz1EyVYUp82wYFPF27pJc7rG+1zVhuRcCDt+eTry/YrUeZ6JDtl1QnliWSGHsuCQNdo7eiJMV8Qk9OWYwgxek1Ur46OBmjDVZcchIa8F6vWSCFRQ9vzxQvMat4uFU4miaNN5DRGX5hITu7N0CeLThTO8LBl6l4w7Y3lpd8qiazeOfy7NQepUiz3YF80Q+XofGKsu9vqFauqutXcixyCty9FBBXg5aDN1Wx7O1w12jadMxJRDm1zSQ3+6FAabRSs44MR03hp4mso7QmmIyUG4YtScVSzRjrUTt1g4OpPp4jkMcNyY+BqSSv0usnewIquLK4EOfLD1rIlUHDcqp5k5qBXOThezUNL4khCq2Jz3pUBtu7Q5pn14YmvODpFLSB4v7rw+71pjk8w0xlFW9UaaYpvV4erPlJlcLulgJcq0Re7CJSiFE1yvsXnKY2F/TuDDgVFPgtLRsY0sjomxyp1NMSc1utomcFn1eSG0yQnW5QXRcptVN0nY9rBby8XKaBYhwjV2BTuacEz2ZZ9UTjq7phecZ2EVwborc0ypTUUdrmi9jdVS16YXw5Sv8SzSDLJLQlczjAlck/rpsEkLg4PjEnYbdeXRx90giZMLxakzHlurOM567nEx7NexJO5F3pDDjGXEWRsEu9V6hyvs/kDQaDcn/DCfH7SG3hKK328kwXD2fjNXam+1WLaxdub4A34GGVpHZ5Ln0QLRToE6tJFaHqfMyTJ5IYwmsnqMtvR6IfWzMPYsgpnM5/6EwqRwfg7YacizysowdH+3P1URh/lp15GdfJHn5xXbaY6ENstmu8cZNba1KFpYmyzbZNLAbzskIpcuzRcrGonVdInOxOVcWPhntqNWuU+tBh4Zoou5jOhInXk1Nxl4FUZP9UwOGAE/qPS00WmE3k8sfbvLkO0kJVYYeUj0ZbPXzzSZBTOhP0eVzgVlYqmWyaVtGKGgBI6nJs9gKck1UyVDvYnb7fZU7I6IoSGlGqzXTY0eJeyYg66xKU6Wk2QXR/DWZL7drPW8VniVIeRgM3iIFcgiJplYOD05cX25Thti6V+SZK/mC1GCka0/ULi0PU0EfXFZeXAxJSbaHNnuqGukrWRzKbOwjPEMqwasf8Bn00bbTcu1vtzkHDurWCzd6CQsp5bRVLa4Zc08aPNlflH3mY1lhcAu8yPDLE2ebMxd5Oa7rtwELlVcrB6pipNZXw6NF++Op0N0VlbCIvS06XHJoYNw5Keicl17LOh950lq71LMKONM2p8JuoG52cRraFyBaX/Y7w9+y8bJcmFVuWNGC2I4qyvx7J6zfak7sagcw9NxJuvkGVnGMNyyYqUOF5HW+iUeeNOBx/R8rit6EETTFX/yt5Xv6iE3wSpX5rMLl6z8OX0xPOOEbCTKOZ4bHj04suZwNj+YjXXlrgSxkS8FfQwPmb8wpV10oCR8v3FBFHZTcqcuDaMV18OJ0abN3t9FXq6VdH5BrZjopTpdX7xQNXrdOEZYsg+OjYCmBqooSz9u9gO83aBn52KqqDJoQdTLO9NZILxhuUaz4ZZrhzqVzarfnyx9CIW2D3G4zuVB6NaSxPT7KSXwB4o6S7YQCITWKNkSh2NVRQ++XrkXXuAOcVio+Yr0pktNExenVWvQycFxcXZiCPj8gHF5s7xGikkI4cXZaFIuhOnCcc16LRZrdLI1mTO5bVFyzXf6Od4tMGLHFKfGUNBmn/MqyXRWlq3CMo/D7TYR9m1Locj+crUUaeWy9lmoJCc3UjdmOceN5OvkslKG60TzsuG4RZojrmRry12i+5rE51h/9FdVyBPsaocV5iKiiLT0w4DBif3a4S9T5dh5S6Yhmn5xYOz5udZ305nLCfFZkYR857nLVYXRGZLIjUxw3e4UKT4yLLhyeSr3oYvZuWZIrYNiTbHs5pNFMNeIZG6zG0XiK2WpVfDJYYxuuyPPvruy0DabM+qaV2cCtu6nOJhHtXRHk8k5uzKrfoOezkd1FvJZNTGp+HQKyZrLpK3WVuo0qC4L3fGl0OGmw8EPjcWpYjNRjakcEKTJtsiUVNlbLLfOFvYlI+br7b60hPgQnRRH447yfDP0G2fZHzxryCKT4rQ+F9b72teEKFHV4ipbZz2N5/Uk97Cr3/Isud1Ta+D0wq/8BYflEhsZkhVMBEepTisAcmkg6HY0FKslecXiYe668IydKus4E3pSsLWim256vJ7pg0srQtKq7MLph2mMlCGXsWmW0ysAUIO6zGfwYgfiWAu0fyXhSFiVFWXTrGgE6Mqnl8ry2J308KJdDzkGE1uexHnJ3HJn0fLCjA4NLtYHVPLFa17KMXaVGXEjDgoMb1QScbR0KYiZDhLdJ+Fwy7Sb8+HSbVPnOsSGHhH1rtkvegGPNjPK5RHVPV7jnDrMLHQJ+iWemOo+nICqQ+SpVPVo7cKUXpNs5yiqT8vTxZndCvJ2OimQNc2sAw2zhZ3IhTixuWJdigbKxkS0NV9xjErAK5Zjounc9pRC2uDMaZ0lFJr17LVUMNuEJxQrN1t7uUhdkCuhgq8N/8j7wjVfeXZ9ghMTAJRkHlPBO7FXFN+pLOoLa9w6pVSNsjJqLLeHPDxnlUx2kwNZXwd/O4/7+eYcHi9Z2F10fiCmS5w1lTBbrgAG75yw2ip1OGcPur4/uf0l3DWGtZj3EpzNlCzV11ag92Wnrfc7/ChY9QVlHZuJj5WQyD0a5j4YhzxK453W0VuNXLLRyWNTJNN1EnRY1KRlAUbFBT0dcFdMHH3WicnVOMxiYZlZq6CpzkEgDb1o5s5VOFBn9bCJ0vW+6NxrvGgZX9GoRurnuwN10ryr02l4U2rTa+VKmLmo905CR9IxVpCNgSuGEKpliHTmoiC3q/PcbKu0pKwimMk8p/kMcnKPDiOGOxjJQxyR4o5QBZcgsEBbVCU1a0/lYj4TNwl5cMmh2sKTmGavWDKDwRiPbNhToSYlMoWRsMBEWYx5N3Woyub5LgOHlS5zo1ku98RsIcoOvYUNfrGuOznYIkztCl23MuflXAuYfDNxqk10nM8W043USPttxyUcHSKruEaHFt+XhnSOZogUivP8oItmZPI7xiZgfEgz93SeSUnvdBve2vMIcVnZe3tPZzlzRUQqjfaZ1zVrmKRYN1hHM7FzSZvaUWXF017WzuRqFimrRbGgjxgiRHhmWweOHQi9mzhzRzhcq+Px3B3Ek0eRZK8gs5Y4LPah5rDq0Ieur0TDHIWRxeAscCqbro+2fG2VyKlkgzd8AybysiJSLEJ2NMonjR6g7G5A8vQgpLMG6xt8YKzTlqeZBncD69BLXugGJ96W3N2BC/bddti4HruaKggYVk/cepst6FaebQ/kRl5fpmk7l5ZK57j7Pit3S3Humqa/sPpqte8Ag53multhmlzZbb/WavvicTHXERUJUwZJHxZyPoQ8zgjzWbKLVgKDCFdeCRFwGFs2jJtv1225ZvKcO9CT1aUSKce/5BRqsAcYYAihJ/sCN9LepU4YkTm1AWplFlEgV07ptjKujecUq76ZS3AeEamsZ9iKAHZMc69YARvs2rEEuFBWHG/TLub7JRx2dRATfB8wa5rq5bjSNyedUu1QbHQxzUNsO8nzZUdqkdryOHvN11xL8aXbmC6Mw8k0Xh1Kexoxtu7ZSivHdNycMWaj6TNhshcrFl2G+8VlTkYUzoWrhcNuC9FXuzJBl7qIS7Y5TeUmuLYxg/FUqypLQvJ2cA3HRjUZqFjPtJmn6lOc2ywQG6YPiURjCzi7XtqQMnwY7pFNkmmkwpftufZgrDdIZH3kPMqWEGRA4QWqLtxl51slqYs+t2lOugus91ftHuv3adtESL/uTDDVn/3zQsWuy8miEcSQyrXYT7dK3IYwjCDTuURLfXSc6okGE0zUiw6+bVu12WheW+6j0sGU3UAUzNpZhCjR7YnFTjltuPK61tfpIncmBl829VWblmJd13hRNJRIGjvjxNBbZU8VQB04O6YAwAdn3R9PM8Lx4rVmH3xGb7gt0QgMnsIrg1N1MsLj/jIHuy9cP9C71US3WvTCS3hVmFFdDkuCBOkHT7Cz1NK4VXP+vqVLeWcvkdLgti2d6w7MrsVrjTfSVHfoqeLuA5g945oCjr04mIAaGt7s57l3WR/XutKW7pVxDXRCrDPmgMe2QJEsmnNpOp2zQlTEVyuUT9bF2q07yRVaH95HyRWco3kqkFvTuJDGll7BpkrRx4MiMQzz889Pz0+339WeXmcTCn9+Gi9XH1ek/+6Wzb+GxZcHMT6Zos9P/3dXQ/drmrcfRm63mq7pvN6kv/61Yr8+P5V2CJS438VVSeM/boD++Zbr0x9dt40kw/0nv3G1r98ujmvTv10Bfid9vMEKq/iLWVVuVY0/1I0Xr2//a+bbz29Pt4vEIsnrJLRul7JmWY+S7KoF7++igeqP63qg8WS8r3/6/b8BA/1jf8wkAAA= -->
