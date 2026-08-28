---
name: "rar-cowork-cookbook-blueprint-position-and-onboarding-readiness"
description: "Paste this recruit-and-onboard workflow blueprint into Cowork and it reports which positions are vacant, how long they have been open, and which new hires lack onboarding records."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/blueprint_position_and_onboarding_readiness", "rar_sha256": "6592f4d1839069da9c0e4325583dd5fb5d7232fa2db1c95063d9fb3c6a81e170", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt_blueprint", "blueprint", "hire_to_retire", "advanced", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/blueprint_position_and_onboarding_readiness`. The original RAPP
agent is preserved byte-for-byte in `blueprint_position_and_onboarding_readiness_agent.py` and in the RCI capsule.

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

Open Position & Onboarding Readiness Blueprint — Paste this recruit-and-onboard workflow blueprint into Cowork and it reports which positions are vacant, how long they have been open, and which new hires lack onboarding records.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a design capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/blueprint-position-and-onboarding-readiness
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
    "constraints": {
      "description": "Optional. Hard constraints \u2014 budget, platform, deadline, compliance.",
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
      "description": "What is being designed.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `blueprint_position_and_onboarding_readiness_agent.py` and embedded as the fenced Python below (sha256 6592f4d1839069da…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `blueprint_position_and_onboarding_readiness_agent.py` first:

```bash
python3 blueprint_position_and_onboarding_readiness_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 blueprint_position_and_onboarding_readiness_agent.py   # or on stdin
python3 blueprint_position_and_onboarding_readiness_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Open Position & Onboarding Readiness Blueprint — Paste this recruit-and-onboard workflow blueprint into Cowork and it reports which positions are vacant, how long they have been open, and which new hires lack onboarding records.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a design capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/blueprint-position-and-onboarding-readiness
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/blueprint_position_and_onboarding_readiness',
    "version": '2.0.1',
    "display_name": 'Open Position & Onboarding Readiness Blueprint',
    "description": 'Paste this recruit-and-onboard workflow blueprint into Cowork and it reports which positions are vacant, how long they have been open, and which new hires lack onboarding records.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt_blueprint', 'blueprint', 'hire_to_retire', 'advanced', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'blueprint-position-and-onboarding-readiness',
        "upstream_url": 'https://coworkcookbook.com/recipes/blueprint-position-and-onboarding-readiness',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '12750246048c8972',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'advanced', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/recruit-and-onboard-talent'], 'recipe_category': 'blueprint', 'recipe_type': 'prompt+blueprint', 'upstream_path': 'hire-to-retire/blueprint-position-and-onboarding-readiness', 'uses_skills': {'custom': [], 'ootb': ['Excel', 'Email'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'design', 'checks': ['Constraints are written down and the design respects them.', 'At least two options were genuinely considered.', 'The trade-off accepted is stated explicitly.', 'The riskiest assumption has a cheap test attached.'], 'confidence': 0.529, 'deliverable': 'A design record: constraints, options considered, the choice, the trade-off accepted, and the first thing to de-risk.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'constraints': 'Optional. Hard constraints — budget, platform, deadline, compliance.', 'subject': 'What is being designed.'}, 'refined_by': 'rules', 'signals': ['tag:blueprint', 'word:blueprint', 'kind:blueprint'], 'steps': ['Write the constraints down first. A design produced before the constraints are known is a preference.', 'State the success condition in terms someone else could measure without you present.', 'Produce at least two genuinely different approaches; a single option is a decision already made, not a design.', 'Compare them against the constraints, and name what each one gives up. Every design gives something up.', 'Choose, and record why the rejected options were rejected — that record is what survives the next reorganisation.', 'Identify the riskiest assumption and the cheapest way to test it before committing.'], 'subject_label': 'thing being designed', 'verb': 'Design'}


class BlueprintPositionAndOnboardingReadiness(BasicAgent):
    """Design agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BlueprintPositionAndOnboardingReadiness'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'constraints': {'description': 'Optional. Hard constraints — budget, platform, deadline, compliance.', 'type': 'string'}, 'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'What is being designed.', 'type': 'string'}},
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
    print(BlueprintPositionAndOnboardingReadiness().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/9V6aZPaWJfmX9FkR4xdLTvRLuE33ogRAoQWEBJakMoVLqEdtK+ImvrvcwVk2tVd1d3VM1+GdCaL7j3Lc5bnXOHfXtyujYv65cvLIXBziHfTNImDGnJzH+KKoagv4Km4nMAv5BV5Wyenri3q5uXTix80Xp2UbVLkYPvebdoAauOkgerAq7uk/QxkfC7yU+HWPjRJCtNigE5pF5R1krcQ+C3edEzqkhbsLIu6baAhTrwYKosmmaQ3kFsHUO96bt5+gmIgJC3yCOgKRih2+wA6BUEOFWWQf7oLeuzOgwGKkzpooNT1LtDTkARsBPYVtd+8Ah+Cq5uVadC8fPn5l08vCXj98uW3Fy91G/DRy+LN1v3TEjb3lXc5WuCCp6CZsEjdPAIbyhGAmYP3ZVCHRZ2Bj/wghJ7vPjZBGn6C/vVfL4NbR81PX77m0PPx9WX60bp88gpqiwlMH/Lc0j0ladKOrxCbDu44Ydt29YQI1IBY5NHrY+d3SUUJ/XO69vGh5DUK2o9fXwA4tTt58PXlJ6iogb66m16/TlLKjz+9gtAE9cefvstputM58NpJGLD69dvz/VMsWPh9aRLetf4TSH3kxCn4+vKDc9PjYffkJ9j58noukvzjQ3BZF32Qu7kXfPzpr8R6ceBd0qRp/0tyf34IjkF8gE9Pw3/6dAf5Fwh+OvQu86/VliCsf8cTsPxN3SfoCdRfyb7j/29Ep1M6vSP+p+L+bAP8T+jnv/TtP9rwCQq/viyDNOlBdpzS4Av027fDfsX9/MH//uGHX34Hov9TMYeiq727hG+Zmydh0LTfvv38obl//OGXnz90Jci1wM2+dXX6ZzL/DNe7nj8g+Fz18Y97gX4jv+TFcG8Dj0yHfivK/1H//gqZbpr43z9vvkA/1sv0gKHJiTelDwh+qJkG2PoDjj+9/A5aRQ686bz7ZVDl//Iv0Dbx6qIpwhY6eEUHelmXt0kWTMbrU1cE/6bargOAa5MAYJ/rQP5PEZ4sLkLo1//l3TviZ+/ZdWfvDfPbWz/8Bprct+/97Fv91oh+fYV0oKKokyjJ3RTS2P3+a+5GwdRtG6ApaIK6B43lNLbBZ9CSPk8vQCOGfv0bWr7dBb6W46+Ptv3oWRonTP2q6dLgdfLZikFPfngI+jYUXAOvA7rSwgOGhQnouZ8AFk2R9k/WaC5JmkI+6NgeIJjxLhtg+GUS9uuvv57cJv6aPxosDj2Yp5mBBe/mQJ8/Aw/DNIni9mseeHEBffjt9w/Q/4b+o1134ZMOQGBvEQIWigdlB2gn6jKwDAQPhBv4f4/Qb78/cQZickCVIJ5JmASPzSBjL4H/Bvphw37GSAoQFAAbAJ1N9DZRUNK+QkIIvdv7znwu4LemhfwAsJkf5N4IpLrAnXck86KFGpCWTTh+gromuGv99VS7dxMzUPpu+yu05faARYoU/JnMvC8Cm4s8AfC/p8TjcyCk/tBAizcRr9BuylGodGu3jGv3qSN0H3EB7PG2HQh3J579mk/MGUxQ3QvmAQ9YBJDxniH9PMUcjBAZ6A5+86b7vsaduE6/c179NW+exTBx/sTUwJQRirrEnyjiH8+UauKiS/07fsDSSdIzCv4zKvccVACI0Bt3Q/8T+s7d0Dt5Q+8kD33tMAQloP8PJ5nJWZbntRXP6qsltNrpmv0IwjSzTcF6jHlgkoBAJj6c+z5dvPWmtxb9NU8TkFH1+I/Hynvonmseba+rAdIaq93lg7wBQZjk3tN6StO6ngrC/Zq/cQHwB7o3PhAI0ANAjUyp+aZwuvpmaQwKfXr/fS54ujkhAlIXKrtTCtIqDAL/NOHRxlNreoseyPFgKtMHdD96BQHp9YRzAyAEpoKnIb9DtyuAmwDOsC6y78vv8QdW+J0HrAVDcfAKWaC6pgxrQKSmHABrAAof7qKgLAAYAxPfEW5it3wYM2XG00AXFHeTRPmP+D8vfa+GuyWT8UCm67stQHKYGrUfXB9xfbfyGSlgajbV733TH4P99BT6kbL+8TW/W/jODaAtpBPb/wANBMoxa+55OHW1BuRrFjzTB+TBndhfH9z8IP93W778u6PDx793urizrfHHuH2B4rYtmy+z2YMh3wjyFfSUGciQpAya72T5+a3kfqxdEOPP7zT2BxUPxL5Af8/MP4h4ZvcXCH1FXpHpkpx4wZS+zwdAhfu8sD8T09WvuRZ8DzdQX2SgdU5RGAE7vzPV2xJAV1EdRNPiB3M1E+ENgGPvrRoE5Gv+nhLPcgFMkEcTzTbFD2X86E/NM37vjAIu5S3Q7U9jXxRMZ6N0Mr8JXr7kXZp+esndLPhbZ6KJP0D6AlimMxUoJDBPtUlwfwdQBMaChG3vb/94lFTuL9z0FdpMDfeHtW+Fcup8cK75BIERuZ1OVp9ATbn+NC1+miimTJOpb0xOtGM5Wf04LE2D2/tU9+/13osbdCW/+DLV+F08+Ps+TE9aHseb+9Ex78D57udpkJ+cBUvB0/va9/PxKXj55U/MeM71f2FEMvWXqSM9WkXg/4krQEgdVB3gBX8y47tf39UVDx2/381rHwfS317eWsozKs/hEywHtfu5meh1BlIYKATvH8kGrv3fjKVPUaAbglkIyKLIORYSPsrgc4Sa++7cQwICx0iSwX2fDE+kT2M4FrqYf0K9OYlQuD8PT7hHuQwaoPRk2iN7v03jRDKZFyBhgM9RzPNxCggi5iiNuUA0QbuujzAMjdChDwjj+9YLaKZPnx8+ToC+T8gTNk/Xf3s5UQRYuSEagX08uNncdCmCPu3iE0xTYVQ1C6qsDdQ9OUeH3hfOstyxtFZe+AMurcVleTi6zsWz1ubKvd4au2BnmgiPOr3xlMrtzFLJu1mWqM5ySIJj0uF0LqjaYts3rSmWhF0hbbvt10fGxLBtLQq+bGs6eVzpmNUG4sKSkjliFnUY9qm5F3nMlGTPTRpprQWm3HnjAT7xuabRBjq2Br09VrBtzOL0alvx2pZ6VTTorEySFuPnaL+wSIdhJesQX2VLcVJduS6cjRGJu7EayESiYNPissFllrczm5EImbsJhXTpwirPErxyDYMNKUc4LRMnX84ZeK+PRJjfxnG2JoN9ruOMcA2VdlVvxENk8I5pdrq7kSM0OQ3FxRrRsfNX9Z5ZNMRqbXYjIov4QTcrRLBivO0ItMqrluKWpumZhSldd/tbiVwDtTDWl7mZSgvKFNaDwdc3aTTILKiQRhSPiRVblixyLsxWeeHOKCWtWti/Sh11DBlG9CrkmjWhkFzOdhasqdaIMbk1ZTFJNe10WcW226ZiuudqGZe6XhAMjhT6q1uxZEg0Hhw1jcczF16kGLnBGrTx/TE0lxsCl0ouDmS6trW1RMZ96Z1HjN1fgc0CvdCQDBncq1+1twWSkyy9yuKD2OSV7h9N5XbzpKrcpnW2shLeUy/EpSEtdZ9bgRh0xwbbLHNd3Vo+yjFbpA67NQHnmxMvVDC9wzYKKTjITXb2ILycZbbzZC2YCtMqKVw3YyOQPlPSHHztqkS0EPGi3mbxeWCSZN43sk2RFsyB3p5kTmIHhHrZ0fqGJ2Lv6lNr08waKYg6ewaTjpvwqEPmztWPT7fBT0IOU24KsZ1R65vTjCeKzM3Bd7eGXyJH/3jFT/hSsooYt2lRHo79qOaDjUd5byvGaXPoR3PPbPg6s/ezOJ7FK0tEQMFhmnc6uiMq6fMIjfxYQOTcCbF6RxxGD8uMRQ+yiG9PYhQSu4V9rcxLssrP3JJoiArf7ppasaW10i6LbdOSzXYTWJkp2jJvpPWFQEYejW4Ryyp2ligX6nzYDcfddXsQ6uV1nRCWvNLUcTmG21ubX5aJ3YXmlo41q0QZYsWgNU+bWGJVtMazudshhx0o+SAtgwLROznXKTtEGER39uSBr2i8wGUeLiTJz0NGCVc7tD44t/4SL3uyxlHYFDt5Rc0yVnSk/qwJJyGr7fONMq5bkzTTpWGzPZm0AnUium0vu7tjtd53VH9dng0rjZCrFFJCuq2jDF/Nqq1uFcvbzMZF1reNxsPgtsk3SFCNki/f0GibzmGbuHCJ7xHIWYYbUVhnJl+viWi78VOLF2cWr9ZYcxAsbaxIccjMczBGtHpUE8Hf3Ai2H8laMdtliQnaiagDWBQRXOE8c79P1uvEcJBUZ+J6scgWdu/r5Ck47D1CV1bgJBQp7YIze1Vz23XC8rBz09Yxs/DFQ0nQWdWKpVom3npT+vGZUBX7tOjZdksO0U7vliRDiYcGP+1oe44QsW5yDF0yJ4JqoxO8paWblMqg5p2Cjqlqru2ddler3TFkKXRFnegZvMQOPOI0lLdVVXyOGavWOZX0yiWN0EpsJ6BuG1rcnoftMnL8dd0vzlUtGRHsqJkLpjLYw1fxph8ij72AjBoO80rrNzdk36lcPQ5stz4s4iCN1P06Xe1D9rJlDCUKdz0pUlSdsWMDKpjlNqIW8Hhr7cGR+1ocIu2It6rJdVUUt1pgUyY3WOEYEV5NtGS8qCLDU6LmoBmLjI8vsYblG73tVElzmxBpVB4/bwO8KTI/xHaH5nY5Ww3GBEdzgMPcEUU2W9sWy16v8Plw1iTYKy9O7q9s7zA7KMktyGdEM1gFfrS3GOFt5yVF5zjJkDC5yec3kpL3RMMwsz5o/KvGSHysZxdqLvnRJVr3mlCoaNeXUmmqBy+occtzDI5ZOPN4hWk3rcxVUl7D2dYY0rNjHgxnx0mdQmljLCnZSUXcG7HhPUQ8xzNvNTPXsc5necoVAqEEaXbs2CNuY4ZeONhxi13SU166uhsRDL0j0uomMt0iydc1GWxyfs91/nbTH9BdpbgjLssmHI/MapDYXLACWjQVgwRtJK6XMm/jpD4kZbpcJ43FhAurTvdOOMRrvSRKNxvnXVmK9cm3G3NBxPaoCdp4zGVHTm9eNcvtC37ZLVfEtkdO+gFUnIji8eK2KJAml7ixlzuVokUM2wdEhSyupitz+DwDrT8zpMVai+yq9/mNHKjXvQfjixEpgBqJ51Uuu4FTAHdGwkOlbIcWrmKvZbKkuKgrtwp3zgpt5QuTLC5zKvbYlOT7gxoUYVU2+bmmwsyV5l7JtX7uOGYhMHQlAFD2QrPYbzdbE+VgxUd73SiPh5WayT1nKNtW3/gIVo1NOtiMIY31EVPIwMlK3O4XPUmbVbIembmbEYjmHQ1/XmFZbZX2EuZRwk9Q3cFXRLa6LnxmnfE6OtN9qtgXR984CMVmriRefhmMnhv668kv1LWyXvdGzV65ucwWiGzcRN4V5g0fqdJ6Xa8Mw/XNlZGbiQm4MHL2vhPNk5w2aUpFWw4r+CrHCU++OWpIz1ud83TyNqaFIVBUeEAi9GRWvmYFDn1QBLaZ7/EjyYApTlgvROkiLY7CmT7p/V5Zef3RodAuc8zB82aBLIlCSM6KseWXWcBVs1NBOW4hZfyZWlJBOyqbQVvIaMQ2xia83TDK9GrN3nTCdasSi0gVxTl/E0nviC4XO8deH+rGrlG41MuNOCevy3FIWVyuU0qUwlOBopsm4sjQcxaaGRKCuhp9ikzWN5bWSzxfr3hVFzU6mp0WrVbSRLwYzXxZpjJ+oiJ9vzrT3DopL0XnZL1mj2IJJ/BK21uyjKFcZ4u+UyzIfh7btgXG+NVGurmMbjA7cVNsy+O2OMSuhDSrxQ4khQDGb7Ku3Ks81/vzFfeY0qIyg7+MHLeWheDQ2KZXyE5r1PbcFZCZvBfVrNtxkY0r/lm13B3Suiu9EXZexDrYyk+a1bVolQKOsqtqivlSn6euOBiuZ4XcHmBN3nxnFPH9gsNqAyPZxAEozlbo3K58M3RN0zHYbebt6oZmz5frQQ8v9kJVjVuLrI9WUqMeM2zjTUo4UoZoskhstDVc4+lRiLxoe4CJs+YM7Ja0/ZWV6dX1IhjHPjgQ4njE83SIz/ghuAiDcJmP/uxKdRTIcWkgaLFrsLWALDI4tiU7xkMhYuCxPhPOPhUc0h0oDh23M4HxB6SyqzKSuFsS9KkPEr/J3NwVudyQ0Kg3qtIXLawoz1cyOC3Mle6uqkEHahVp5GnDF/hFaypX1vR2hMeS8g3b1PGyobuYc843D7MJNTguVKRyjBwdVsue2FgB6RT6ZofSbNrKok4tlPUxIk3hdDNWzvGW84YWaWJ7WTeWtNhLHKGBE4TbwsQ1CeYMr/VEBYZfU/a0rT4bMYvZ78vgsGBW7t7QirwUl9tiSdm40cUJ1cMHKrloG2ztFQZPpuXIbDj0RkqVcrVhouU9aaXsEZu32l5mGSO0B5VaKUyMStGSUqM+9xuyJWaqlURdS2IDOJeFXSLxSUWX6UDuJCekruuA9nRkozTwwY9o4yysFSzSywYl1IVA2QdGuYkFT6KrcU9RDnXZ7rhNqeycNla0Ds0QOO/JjUAFJkb1wSUl8NpF2+FKjcx+kR39xKfkWSeOgSzgm0Xj0dKwu93WvNQcGtpAsiw/SvFZZXb8rbc3LgPGciHkaN8GTaldhvqtO84s+NAytCYTxDjqrmB3ZB5nuiRbPluzMrGc3cIyoshxtPcii/sYTTqdFsdVw2wJZdw7dqGrtH22Zi7bENbaFmah2ouY3lKYbLYx7MU1xjYL0p7P5/oYwPM93aLobFjTppGUe2s2q3J414g+xshHdBHSIKcxg7YNEqVKlTIGg+D6a7DjnJrOl50x7E1txl5aNR62Sb+oOTdmh+2uEAmSSBQkFzaptCLVSGFxMe9z0Q1g+1h3ejJu9WKwuqQZWz2y98Et4smVOyeD45hvAtsmQDW3g7Q9bZVZSTiep6xpolmk4BRBocIMNryh33g+Kng2Sga4xw+w37bpKMwXx8ov5YVVaB18lq4zva97lnW2u7To4i47n2YgMxqfv5JdDOfmsZphTSgiAOyLlo7qBWFR6bKckzBPDgpII8yfa6tkJ+FYkYzcvrTN6+icXWyeOuHmkB9pN94RQakoCk/mxyuJj0NAiAm76XEuXzPrQ8gtgprdxqeE1XgiD5y8OIxMWp/PcGkhgsrvwIl2r7USTxXB3kR2zoHFyYi6iP5puO57LgVH4rZexVdsIajZjMMVNxAR4sqw5KWRrUFTqsNyLOHb3PJh2uu1ji/CllUsJe2MW9XWPWIJZRQvYjTUD0RgYWysboP0sjvaIUWz5jHPeb4l+mDGbcGxCpZxWiJPtH/uYjORsvm5VgJqle0aRxZ9v8SuQR7fTM0wtnO4PK57yr/2sn08+PPcvyG3C0aX6hDfmhy1hW2IW/vWl7gGEPIspC43RY4Uua1weDl61hJ09MFb2Bxhb5ZtmcHHTJX8GV3vvaqyfaS30HG5NHjjct3IeKEcq5uiyNlOZdc6nNbLUKU60rA3l+WV35ONvzkdVsvLPD8NqSGQ5tw+B4dZBKKFDiwOsy6AJx+XBHLawPNhZd1Om26kWDyv+pApOpDw5/yKgBmPDRGvMMMq587oHqaWMrPULljpn3WFuHnZKYvRM9olfYstZzOp5mFe3dTMqqT3yE5FYpOI6CHWCJakEhO7bY49KfPULvDtwdZPeUbmLkm48+XMzKXd4mCTkgrLND2bpWtOY5mNjofnUtyI5DGTFq1DtT7bDKsZWe0tcKY7Mx1LF+iO64DfDk7aK9uqMXO5w90sPuq7I9kmREfht9PZpMCQTfuFixsFz5USXYTbK5yfM3YTI/PNqBskYeHINWk2Ayvm3JrpdmyazZZCZR6JHEdvxnILeMGpLoTMI0e3RdKdWFeko1k+qRLUuJTnfelEPYM7q3zgj6QW1R2PHmRBd0lPRLoztu5gy95te0yp+xFQ/YpwMgJD8aTplhvyOBSGuYcPlUG7JG5fB/HaKT2LqnJDWvKJYuOtrh+2BzY/Ubt402iGXMlCxSDHqPJ6kS5vSW5ruH2zj+Bokfh6TywdCUvYlihZlv3ny6eX6Sb181bzf+c76ekG3/+z+4yPW4JvX0Pdb/YChV/uur78t6z75dNL7SXAtscd1ibtoudNyH9zf/Xz3/gmYxI0Pr78nb5Du7Zvt+xbN5r+Z9NLkvtd09bjt6ZIu/vN3k8vp6552AYc9J437OsiK9tv75qnVT+8nr6C/NYWwK0WvAIfuH4/4TLdVAUrguh5//nTiz+CCCZe8w2nyG9BXU5uP78eAd5ir8gr+vL7/wFucMvkeyYAAA== -->
