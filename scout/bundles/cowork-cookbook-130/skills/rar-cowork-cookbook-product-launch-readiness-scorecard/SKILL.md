---
name: "rar-cowork-cookbook-product-launch-readiness-scorecard"
description: "Scores released products on launch readiness based on setup completeness (dimensions, pricing, BOM, tax, default order settings) and produces a scorecard."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/product_launch_readiness_scorecard", "rar_sha256": "26a8baac5f7a3ac17f0ffa8ec43de81ab6789469c41f12e717f2a6e189b31fed", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/product_launch_readiness_scorecard`. The original RAPP
agent is preserved byte-for-byte in `product_launch_readiness_scorecard_agent.py` and in the RCI capsule.

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

Released Product Launch Readiness Scorecard — Scores released products on launch readiness based on setup completeness (dimensions, pricing, BOM, tax, default order settings) and produces a scorecard.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/product-launch-readiness-scorecard
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
    "audience": {
      "description": "Optional. Who reads it \u2014 this drives register, length and what can be assumed.",
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
      "description": "What to produce, and about what.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `product_launch_readiness_scorecard_agent.py` and embedded as the fenced Python below (sha256 26a8baac5f7a3ac1…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `product_launch_readiness_scorecard_agent.py` first:

```bash
python3 product_launch_readiness_scorecard_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 product_launch_readiness_scorecard_agent.py   # or on stdin
python3 product_launch_readiness_scorecard_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Released Product Launch Readiness Scorecard — Scores released products on launch readiness based on setup completeness (dimensions, pricing, BOM, tax, default order settings) and produces a scorecard.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/product-launch-readiness-scorecard
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/product_launch_readiness_scorecard',
    "version": '2.0.0',
    "display_name": 'Released Product Launch Readiness Scorecard',
    "description": 'Scores released products on launch readiness based on setup completeness (dimensions, pricing, BOM, tax, default order settings) and produces a scorecard.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'concept_to_market', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'product-launch-readiness-scorecard',
        "upstream_url": 'https://coworkcookbook.com/recipes/product-launch-readiness-scorecard',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '07c7efc65e507d80',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-23', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/manage-service-offerings'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/product-launch-readiness-scorecard', 'uses_skills': {'custom': [], 'ootb': ['Excel', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'author', 'checks': ['The claim is stated in the first paragraph, not withheld.', 'Every section maps to the claim.', 'Numbers are sourced and current.', 'The ask is explicit and actionable.'], 'confidence': 0.333, 'deliverable': 'A finished draft with a stated claim, an outline that serves it, and an explicit ask.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'audience': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'subject': 'What to produce, and about what.'}, 'refined_by': 'rules', 'signals': ['tag:report'], 'steps': ['Fix the reader and the decision. A document that does not change a decision does not need to exist.', 'State the single claim in one sentence before writing anything else. If it will not compress, the piece is not ready.', 'Outline to the claim: every section either supports it or is cut.', 'Draft at full length without editing, so structure problems surface before sentence problems.', 'Cut to the shortest version that still lands, then check each remaining paragraph earns its place.', 'Close with what the reader should do next, stated as an action rather than a summary.'], 'subject_label': 'document to produce', 'verb': 'Draft'}


class ProductLaunchReadinessScorecard(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ProductLaunchReadinessScorecard'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'audience': {'description': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'type': 'string'}, 'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'What to produce, and about what.', 'type': 'string'}},
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
    print(ProductLaunchReadinessScorecard().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/816aZeb2JblX6GjPthZhC1mkN96azUSoAkQgyQk0rmczCDmGZSV/70vkiLsrMqsV9mrP7Qcdgi4nLPPtM+54N9erLYJ8+rly4vuWRm0spIkCr0KsjIXWuZ9XsXgVx7b4C/k5FlTRXbb5FX98vrierVTRUUT5dl0u5NXXg1VXuJZtedCRZW7rdPUUJ5BidVmTgiuWW6UeXUN2fcl4ErtNW0BBKdF4jXe/dpHN0q9rAZS61cgJXKiLHiFFnvpFWqs4RVyPd9qkwbKKxfgBAIasKD+6Y74oRTAsKB6wuNYlfsZQPUGa9JQv3z5+ZfXlwh8f/ny24uTWDU49aI8oIp3lNobSP1NALg/sbIALCxG4KsMHBde5edVCk4BNNDz6GPtJf4r9O//HvdWBRB9+ZpBz8/Xl+mP1mZQE3pQk1t1A+x3rMKyoyRqxs8Qm/TWOLmvaavsjh+4Ogs+P+78LikvoH9O1z4+lHwOvObj15ccQLCmQHx9+Qk4Buir2un750lK8fGnz0nee9XHn77LqVv76jnNJAyg/vztefwUCxZ+Xxr5d63/BFIfIbe9ry8/GDd9HrgnO8GdL5+veZR9fAgGIem8zMoc7+NPfyXWCT0nTqK6+R/J/fkhOASBAjY9gf/0enfyLxD8NOhd5l+rLUBY/44lYPmbulfo6ai/kn33/38SnUx59e7xPxX3ZzfA/4R+/kvb/rsbXiH/6wvnJVEHssNOvC/Qb990hV/+/MH9fvLDL78D0f9SjJ63lXOX8C21ssj36ubbt58/1PfTH375+UNbgFzzrPRbWyV/JvPP/HrX8wcPPld9/OO9QP8xi7O8z6D3TId+y4v/Vf3+GTpZSeR+P19/gX6sl+kDQ5MRb0ofLvihZmqA9Qc//vTyO6CIDFgDOGG6DKr83/4NkiKnyuvcbyBADG0DgQA3gKgm8IcwqiHwM9V25QG/1hFw7HMdyP8pwhPi3Id+/d/OnVQ/OU9SnT158tuDI7+9c+S3dwL79TN0AJLzKgqizEogjVWUr5kVeFkzaS0A7XpVB/jEHhvvE2CiT9MXKMqgX/+18G93OZ+L8dc7gUYPhtKWm4md6jbxPk8WGqGXPe1xQJfwBs9pgYokdwAePwLM+gosr/OkA+w2eaOOoySB3AgoAd1ivMsGHvsyCfv1118B/4dfswed4tCjjdQzsOAdDvTpEzDMT6IgbL5mnhPm0Ifffv8A/Qf03911Fz7pUACzP+MBEG71vQyB+mpBYwEdaQou8MQ9Hr/9/nQvEJOBfgKiF/mR97gZ5GfsuW++1tfsJ4ykINsDPgb+TYu8mnoPFDWfoY0PveMFSqdLE4uHed2AjlV4metlzgikWsCcd09meQPVIAlrf3yF2tq7a/3Vrqw7xBQUutX8CklLBfSMPAH/TDDvi8DNeRYB979nwuM8EFJ9qKHFm4jPkDxlJFRYlVWElfXU4VuPuIBe8XY7EG5Bmdd/zab+6E2uupfHwz1gEfCM8wzppynmU9sGXODWb7rva6ypsx3uHa76mtXP1LeqKRQOaAVAadBG7tQQ/vFMqTrM28S9+w8gnSQ9o+A+o3LPQe1tsni2a+jRr6H3hg29d2zoa4shKAH9/zuTTAaxq5XGr9gDz0G8fNAuD0dPQ9YUkMdcBmYDCGTbo6i+zwtvbPNGul+zJAJZU43/eKy8h+e55kFkbQWM01jtLh/kBoA5yb2n7pSKVTUlvfU1e2P3V4D3TmWTr3IH1MGUfm8Kp6tvSENQzNPx905/DzUIAzAfpCdUtHYCUsf3PNe2nBigmrz+FiSQx95Uin0YgXj8aBUEpIN0AfKnsERT3Prs7jo5B2aCyvOrPP2+PJpC/XS3C4Ep1vsMGaCCpiwC8fXAEDStAV74cBcFpR7wMYD47uE6tIoHmGnwfQK0nrH40f/PS98z/o5kAg9kWq7VAE/2Ewe73vCI6zvKZ6QA1HSq0ftNfwz201Loxyb0j6/ZHeE77YPST6b+/YNrIFByaX1Puom5asA+qfdMH5AH91b9+dFtH+38HcuX/zLrf/x724F7/zz+MW5foLBpivrLbPboeW8t7zMorRnIkKjw6rf29+lRjp/ey/HTe638QfLDUV+gv4fuDyKeSf0FQj8jn5Hpkhg53pS1zw9wxvLT4vKJmK5OvPM9ykB9ngJWnJw/gn773oTeloBOFFReMC1+NKV66mU9aJ93FgZx+Jq9Z8KzSgDJZ8HUQev8h+q9d2MQ10fY3psFuJQ1QLc7zW+BN21ukgl+7b18ydokeX3JrNT7H21qppYAshW4Y9oMgUCAgaiJvPuR1brR5JPp+x/3efv7FyuZSiu/0yfg/+atIO743QqAm2oxiKYu8AoBzEET3k3qp3qcZggbmFjXoCPfN2jNWEygH5ueaQB7n87+K4J7SQMucvMvU2UDQgaT9Cv0PhRPdPzYpty3flkL9mk/TwP5ZDNYCn69r33fxtreyy9/AuM5n/81iCfdvN6Ns+ypnU0m/olNQFrllS3on+6E57uB3/XmD2W/33E2jx3mby9vjPKM0nOaBMtB6U5l0jYzkMpAITh+JB249n8xZz4lAA4EUw4QgVEWY1uWQ/q0hVsOSvuI71uM5xC46zGoZVM0MyeouUOgPop5NFiAWZSHMnMbR31vkvdI3m/ToBBNqDAgjnFolHDntEU5Ho7YuOOhGOrSuIeQc9xnGI/48dYYUOjT1Idpkx/fR957qj4s/u3Fpgiwck3UG/bxWc7mJ4vCaFsLbbiivAvpUyrKl0iK3azQ3nro2nDtDZcGkU5rHr+jN4Gjn+TDlpM5rLlYiy5XfWcDj2c6uylspNdkIvQGppqVRdSj6czwvUtcdkHK9UZ52hmFsTmNplJWwRFn4jKa+1Fj7ra3QkeJGHNWw0mMiavvd9lpZlhCaTsnu6hPnm7qzfyIGIPHLHi43pXNclDSVBeMApbjHNHak2GimRtsin1jm1a0g8GsyWzigpSG1dao81I8nlo+PW3UTSy40RCfQmYnW3rfnO3wsuao+T6rGMrLbAaeCZ7T4RUNbzStQ/syM6/RKIibEqUzjTxdamdUdo19iZL85FBbFe4xJhESTxCt9cwsuDI0hRSeB815XxzRY9uzrHleFNZcyXCZiM6SrA9GQgnEKd71klkhK2yIi8LfJaGSe+VRwvROV0Sap6/b7lrus8YkK8v1kT0xMsciky6BofR1yR8Ws4DBSo1Kgjo55oZUUfyh1XoupgwTqWIdX83RPOTQgViMhinWUeyk7RbNHCERcfGSUDiPtLrtVquUXdfZFts1V7YS5lhjLhM5iXbFjsEai53t1yIf1sJ6tLlFtcaqY50tLbI1DqdCcWco7COwWpmXlb69oIGAhNnSXG7FvR2tbrTM43ZAyE1FIjwncNqtC6qNfV4xvls1wdHczNfVInXiI0yCsbA89UG1Q2baLpOGbLcqDiXdrHauTR4UoVbnFTLWBCeFeLdUrvrm5pjWLTdc0q8y1sdERKsTSZGO2qohr5GPJMKKugqoYa5u7eq2nrVamqdoejIxOdOOTm9faKbTFry70eZI7o2aSFPFjh6KI349FFFJBQWmmK14cPfNjmFjhkdhfgA/WTZmF+S4pboZyxv+wcapyyw4KoE+NPZaQLpilWxLtxuMnVhfDWq3R7VO1/WSPGk7NHecS1gbq1Eb8EhSmWwWjDbchWDGcQZj2S5CBqG0+BofD6HTaFwmMsn2okjFbr1F80iowyhY9fawENxzsooPgdb00ripuGFVxKcbrwWmIEggCa7GYpBwRZbsUPe4ao7FZmbkVsbxdtJrPELk0cVRx9lyT+5iZbk4owWTYWDMw3kb5U2YveXIhjzfqsGfzYjMaGq+EdHOOPCV4p2Z8jR4lLixl5GaF/WGbDPBjWfZ5gqmkE27aNjFKrlSHDdvo2ILs3WVhBm8JIXgZJ4O6cgmt9IPuUzjo5JXryLc+SckPIu3ztzEBNU0a04c5sIYHrj25BRDV5zsyoxPK1fJZztaDzesVp4Mm7vqqg6jVrrNUbHZbbBRG0t606zjA4ZsFrwoXbrLEeZoKuU4dImtD/UY2b0+m0srT7G1MYSZCkn0q1oWXb8tLqIOiixaphh+oK+g549JiIhjf7XU0Oa6OS8e0Ku7T3lSk30+0fjW3RepqJeec1DTeofI/lkYz0eZOKVMyxadPcCn5lAeM/q2wxSZQ6x5ULStCLdiMXhEOFwMMz0KFbE27da2gAa5RI1mP+OQddPDhKvMzmGt4CG7QFOYWrKiiOTbysJvBwI/LEhy7R6qVhvlhYWYxO5847zruT+piFki1yGsL4HK0PuBc2bLxW3ZaLds6fkyg7mdipl715+l6+tMrnGVVhlrcb4JkWlnZs5XMHdclkt1JcbWiWMX4XZ5ievKVVQ5wwBdYvtkfjiygZ7yZ6NhLHV5ZFpR1PiAxO0wZwWdkze4jm4TlaoQLLF4ex5s8b5YloGxvqk7+hRS1LUmsT4rEV1RBN5NqLmM3eqZdLYZsqJE3mpSeran4phllrY5S9IDs1s0y931Clco4TDGcm2fl17fqsJytV4zJ58yDMb0FHSnXCtyN0PzLJL7o4wp4j4ltwe2C/nykizDq6mYq/yUW5onZoaEVqx76y6hbJ7yLjsvNXe5M1pxCEY4Gwg45QZaj2L0dMzYa12y1yZmQyshvX7GHiWuT1bri3rAAj899B1tLqmg9wnLTBTF4ZQ93OaRNnhhvUgC2SpO3mVnHDg5QZo8mtsrGMUtjTsH8a1oDjNeGTF8sXB3WGaZ1hJN2/AmD4SsK7szswHkK3WuVuhN5XOpwm9lRmoNY7MxBh+QdCbTws7y0WJT81JVqETQLzLVU9bRvA3NXSUpuXEDUdkullhOCqagVTefPjsHRiO09KrNE5zcDOGg+xwM5CYroV11ozhiB5c+HS50yobLlA+H+aVnZGV35LF+bwo8jNTeEdGqnAw6uD2mprji+AXSaI2dCKEVyLMbG6yrbUmGuTdDCdXNebHlOLU62LGi+hfrsDwHA7W0iCLLTgLhxVd0zY0FsgwAKZe9nl3aa9qoDn/2qjHlouF2nJ0TqmNIfR8vQ229ZxPnLGV6M+7Tvk50bHtcYnGfCeze2zbFZZOGHYkbVSQMjFvghGT6h23pWWhpiUi74Dmd2ofG9jbv5UUgbTJf8IZEUG63NlbhQC7sGxFeCao4Misqt0fjMKz50tmpsHVYr0LKDm4pR9ox2whtyp3UxYIo8jjMVsXAmIJBaRtORZeO7G5mduPr6yTXEVA73qzyZ7W0ZmLcQtbs4DCFSjKsE9qUr+MVV5xXZQXkFPnO2fg+rCC0D59zLtxQqRRUAcfSK39t8s6+V4aCU1Cxsi9wd0qydMxQxHEG51qY4tDNGTMKbP6yV0V9bu3m6mLJ9yd2AWrvsEdm5imKswCWwvh6W8n54rLfXL2Oy2f5PMl2LHI5b9DTtVBvkm5aJL3UbFTWSz9dBlKlo2q+PSdbMjpuLDAa2JWY5q3ktSez6Jc3dD13dlrUCQt7pYWUuosr/jymoX8ygzW8uUbX1Lok12txHBIORoZCV5tCPMZrd7MMhh2r3NjQlAQNGatSUJOiJKQmua05koG3Cyo+FgW7007m/ljwhtCgtyCVzmIh7y7h4GarKEaCs7XYHwfdvY5HijX3cnSoCWoMIxHNtp3AoqTur1O9uLVL7zaUx2Kz0dfLLX0W6nIhaSPhnNg20EwPhgVx3bqxXjn93plXLjesk0ZSF0q7C2+35dY4psGuqDXTZDvVsoVWxQ1qjYMRFDO6UbpsF0TXFAtpffM8UTK0zTx3kevmml5WZ0oQRHQ8qEM1iKszCjbrpDQXeJOm6fggqMWZVbI2sDmyHxlTcmdmGSjD1uQc4ABdO6o0dYvIvbMyuCLER74QaFupy2OLyAf5trQO54K7nGVcdq5NwyfGwMJDTeT5IR9JbcfXrK2tECLY2bbdcvG4MDaHCDO3joeg/RiUgUns90y35M6lfLotdWNd8KhxownTRLzsontL2zgwoIVqF2mIWXVPdFftYJ4E59o1HXyUQmUtLlOfXsoXRLjoBblZ22SLCFtAn+nltjfH9pbs0OJqZSh7pYNqWVScju1W5FjaOyI+G7uzyRm6LK48I9unyzT3shI7ZGReDv3+sHctGZWsYLS8mNqObcxd0X22XpfaMe0jbU2vSFWxaWm7PsVnmlmatpIuhxm1XJtNv/GwqtzOh9gK5nlVgH3H7eAR+/W5DrBWcvaluiKrUu4QeTiNV5k7FrcAkEdLCp105FV4x6khuU8NO8CWCma19vksIjv4fKgut0PllvOWDMO5al8joqLOLn3VGTjblfEBN313pC/7wgsEvFaKG+7CtLObHTG3oNH5bRXvrKWOaxmVwv7R8aJW9PxgUShzQQ0aQtQQdyDofh3Q9PbGeL2Q4NrWHTC1tvfcPGYJNI1s8rqnxS2q2rDoLHw7Lx2SU4gEzE4HqtG1QS3Z882bG6Qw7xVd7GmePc225LnvTso1WFPE/tZ1GOg49bpHuMzZ9cY5s6+lsiDpdtaBcp8F4qwAHYj1nQqHNx2JjXNkPWwVe1yV+w1tqjPHkcXGOmMyWzFG0HPprhezIF/KdNcfKC5xXPbaJc5YqQHFi7rGD2QEq0E0zDUzSFnneB1F5BxmKUpRmb2f84tWKIodWRCKF94aokkvxBw3yduh20kH6nBpie3OlqRZYSdEYW/J+KiMexeXbXQ/C2nkhiKruW6u5n7sSsWI4+fjickcdY7H1rUfrRubpkSseG7vELkoLnzZxIURofeaIF+Vy1yD/aoSdjMbH52VxdfUYksspDkrKCmXzBmBoOkOV0rQi0LLLWUMhIY35fB83iYy2EUdyVmzd72u5NchGRAEabdGq3jU8YYLksomMJnZSlBlxFnoa3YU2ovGryOXWHjh+tYfcPs8P11XrOoYkjLOBSS381T3qtSCN05pcDkgQW+Ij4xglhQrd4IwYItLX8J6tvRbCXP8PQsjzercR0G0FfDzeMFPzGy/WKw2drtAxCo0rD2+QAbKkIogUJY2K4ydfBg69WjMM/0yR/fC3GOMk4wycHETKprZHFLJYpSsaba1uqdXNL+WhxVezwYS0Z2x5WB7tBMJpaMrCpurXYyONBjnGIXsOrB3v6Kjh++7dHXGQi667khqeeu1oZKHG5rN2TXBzL2kObNmRttN14XLi6wJVYgxuTDTsatbmE2TqStjjp8M0kVQSqLPpXaxwhvnaL0rrg6UhHMslngsyvVpRUjqCuYMotXYk64QDkzeYkuOFYFgNsISO/snCc8LQkyxPcwb8IU72s3s1ivLuQ30I4YvNy24qvhticJ6hJIwzLZaZ4GyVWWqZoROViLMUlxx2w1j2lAF0hyiReTiR1+/DNTBbVl/RgyO11cUk/SBTVPHTh5YoVttJfVgB8ehstKyTmeosQ7QFL0OgXwGHG6qp+hM5DOOR7jeUuP5GR9qZoatom26N1QKhs+q7QmFF2E4WrUCji/p9Ha0WKPWPHutgI2dg3X8glFgg8+1wo8xp3X24dpMSxhDZbFtYIxCvX1LxVkTGGXsXqzYxi+wXaFsVhMKB2oiSrf4sMHTdcoK14Br14XayAEXzlen/fE6N0wdoaTbAjP0oIdR2i2TxXh2RzTfY93Gu1aS1KVIt0a7gJ6TG7AdTGnyHHSZg1DY/rCb+6G/mKVkO8M3UtfBUt6tlPNCsjtpKWDWdWHgns9nLCKiIpmVhYI7t6y8IBiyzoI9EhEySY1MLrkL5HQU2UMyW6n2baNvUSEGGx0fbcL5ThCztXARcO2GbOKq8teBQnPydlj3O5ZlX15fpufNz6fGf+OF8fSM7v/Zo8LHU72390f357VA9Ze7ri9/B9Qvry+VEwFIj0eiddIGz8eH/+mB6Kd//eZhun98vIedXnUNzdsj9sYKpv9K9BJlbls31fitzpP2/lD29cVu6wc4IN8Bv1/uhqXF9Kj58V54ev6cAyuL5luTf0utKvamc1E2vb7x3MhqvOdh8HxC/PrijiBAkVN/wynym1cVk53PFxmT+6c3GS+//x/h0pzYzSUAAA== -->
