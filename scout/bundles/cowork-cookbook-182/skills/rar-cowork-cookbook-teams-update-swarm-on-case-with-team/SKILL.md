---
name: "rar-cowork-cookbook-teams-update-swarm-on-case-with-team"
description: "Drafts a Teams channel post on swarm on case with team status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_swarm_on_case_with_team", "rar_sha256": "9b796e6103b200d7cced9bbbc02cd25b315c0c22dbd5c5ec82d870ff150449a8", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "teams_update_swarm_on_case_with_team_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/teams-update-swarm-on-case-with-team:1bc3d7910f10883f41197c3d527eb529daa762c9ffe61bae88a70f0b6e001bbf", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/teams_update_swarm_on_case_with_team`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `teams_update_swarm_on_case_with_team_agent.py` is
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

Swarm on case with team Teams Channel Update — Drafts a Teams channel post on swarm on case with team status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-swarm-on-case-with-team
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_swarm_on_case_with_team_agent.py` and embedded as the fenced Python below (sha256 9b796e6103b200d7…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_swarm_on_case_with_team_agent.py` first:

```bash
python3 teams_update_swarm_on_case_with_team_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_swarm_on_case_with_team_agent.py   # or on stdin
python3 teams_update_swarm_on_case_with_team_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Swarm on case with team Teams Channel Update — Drafts a Teams channel post on swarm on case with team status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-swarm-on-case-with-team
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_swarm_on_case_with_team',
    "version": '2.0.0',
    "display_name": 'Swarm on case with team Teams Channel Update',
    "description": 'Drafts a Teams channel post on swarm on case with team status with an interactive Adaptive Card for quick triage.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'case_to_resolution', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-swarm-on-case-with-team',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-swarm-on-case-with-team',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '6b9fdb93d32c404c',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/manage-and-work-on-cases/swarm-on-case-with-team'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/teams-update-swarm-on-case-with-team', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class TeamsUpdateSwarmOnCaseWithTeam(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateSwarmOnCaseWithTeam'
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
    print(TeamsUpdateSwarmOnCaseWithTeam().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/716eZOjxpbvV2Fq/rA9qm4hFgF1wxEPBBICJMSqxX2jmiXZxL5IAo+/+yRSVXV7bM9cv3jx6Ogqlsyzn985mVm/PjldGxX108uTAZwcWTlpGkegRpzcRxbFtajP8FdxduF/xCvyto7dri3q5un5yQeNV8dlGxc5nM7XTtA2iIOYwMkaxIucPAcpUhZNixQ50lydOhtvPKcByDVuI6SFA5GmddquebyA/OO8BbXjtfEFIKzvlPebhVP7SFDUSNXF3hmBMjgh+AwlADcnK1PQPL388s/npxjeP738+uSlTgNfPd0FsUrfaYExclfzBeS9h5zGL3B66uQhHFf20AI5fC5BDblk8JUPAuTt6ccGpMEz8h//cYY0wuanly858nZ9eRr/6V2OtBFA2sJpWuBDBUvHjdO47T8jbHp1+gapQdvV+WicBgqfh58fM79RKkrk5/Hbjw8mn0PQ/vjlqYAiOKN5vzz9hED1vzzV3Xj/eaRS/vjT57S4gvrHn77RaTo3AV47EoNSf359e34jCwd+GxoHd64/Q6oPR7rgy9N3yo3XQ+5RTzjz6XNSxPmPD8JlXVxA7uQe+PGnvyLrRcA7p3HT/kt0f3kQjoDjQ53eBP/p+W7kfyKTN4U+aP412xK69e9oAoe/s3tG3gz1V7Tv9v9vpNM4B82Hxf+U3J9NmPyM/PKXuv1PE56R4MsTD1KYGbXjpuAF+fXV2AmLX37wv7384Z+/QdL/Kxmj6GrvTuE1c/I4AE37+vrLD8399Q///OWHroSxBrPltavTP6P5Z3a98/mdBd9G/fj7uZC/lZ/z4pojH5GO/FqU/1b/9hmxnTT2v71vXpDv82W8JsioxDvThwm+y5kGyvqdHX96+g0iRA616bz7Z5jl//7vyCb26qIpghYxvKJrEejgNs7AKLwZxQ1iviX1V0NeK8rnzP+KwLdjukOIcLq0RVa1E0OYq4vR46MGRYB8/T/eHTo/eW/QOR2xrnnt7mD0esfC1yJ/HbHwdYS+1/H718+IGUHWRR2Hce6kiM7udgiEurwdmd7Do+myT5eRL5QpfuCOvliPmNN0KfgH8vVfYfR6p/m57EdlvuTQOw50mQ8BOSuL2qnjtEecEa3cvgWfIMhCRKmLNHUdiL7jj678PFpoH4H8zW4exG5wA17XAiQtPCh8EENgfoaub4oUYng7WrM5x2mK+HENTVXU/b3IQIu/jMS+fv3qOk30JX/AMY48ikszhQM+BEY+fSprEKRxGLVfcuBFBfLDr7/9gPwn8j/NuhMfeexgYbjbDIZ0ikiGukVgfnYZHNYgY3BA8Ln779ffHs4YpcthNYRZFQcxuE+G1L4Fw6jBw0Pv7oE6jyKC+o3T7+2GXCNoFyRuobVgpjfPX/KRRAGH1tcYVsY3Iz4mP0z/7u8Hn9EnzZsNoZ+CusjuY+9xODrTK2r/M7IOkA9LQXWhX+/FORrLsQ9KkPsg93o402m/uTAvWqSB2dME/TPSNVDVkfJXF5IejZNBiHLar8hmsYPVrkjhj9FAd/ZwdpHHo+PfAvbxGhKpf4Axxr2T+IxsAbQmUjq1U0b12AyM4wLnERGwyr3Ph8QdJAdXZKzrYPTRPa/vkWf8RTfx6D0Wb73Ho/YjXzoMnRHI//cGZRSUXa10YcWaAo8IW1M/PqJqbKRGJR+9F+wU7pPvKfKte3gHmncI/pKnMfRE3f/jMTK4B9JjzAPWuhpGic7qd/pjStd3unELw2H0b12PIex8yd+x/hlaAzqjGWELZu15xIDig+H49V3SCKbm+Pyt7iOPSBszAMYwUnZuGntIAIB/D/c2qsdkerM9jA0wJhaMfi/6nVYIpA79DumPto+hg2A9uJtuC5MC9kqPCP8YHo/dFJTC7zwoLcwa8BnZj0EMA7FBXABbonEMtMIPd1JIBqCNoYgfFm4ip3wIMza3bwI6oy+KbAyX7zzw9hEG5FhUIL+PbINUHRhc0JZX6ASYTLeHZz/kfPMVFDYbI/8+6ffuftMV+b4o/WPMOCjjN9CH/fhYz78zDgzLGsbvCBuw0p4bmNMZeAsgGAn30v35UX0f5f1Dlpc/dPQ//r2m/15Prd977gWJ2rZsXqbTR817L3mfvSKbwhiJS9A8yt+nR1X6dM+0T0X+acy0T2NifWrv8f0d7YepXpC/J9/vSLwF9gsy+4x+RsdPSuyBMXLfLmiOxSfu+IkYv37JdfDNz2/BMOIZxFi3/ygr70NgbQlrEI6DH2WmGavTFRbEO7rdy8RHLLxlyog44VgTm+K7DB51Gj37cNwHCsNP+Yjv/tjRPVY76Sh+A55e8i5Nn59yJwP/yipnRFoYrtAa4+IIpg7skNoY3J8+uqXx4ffruXtSQTTwi5cxt2BVg53tM/LRpD4j78uG+0os7+C66ZexQR5ZwqHw18fYj8WiC57gQq3ty1Hyx1po7Mve+uU/CjGmFJTYA2PdLj5ydOT4ByLwJgxB/Uci6v3GSd+AAgL6WAthCX5L7wbK6cPu6RmBvoNpBzMJAmQHJ/yRDeRTA4jyEGlHdb/Z75taxUOX3+5maB8Lyl+f3gFjvH+0Ao+4gRP+Vss2mvW91L6OxJ2RxL2xulv53pS+Qg3jsaR+9ykc+4PXRyg+vUDEAc9Poy1hrUrj4b6GfnpIBFX51s5CChA7PjVjizCFmQQpwcJdjmqcIe59x2B8Hfv38ePNy5/3wP8LCLzMXA/3KWaGBjOUpvGAmM0YCr4iMQq4JMb4jkPNMY8JAjCfuQ6gaYdCA9SdAxSduW4ABRn9mTlvgkxnoyegCh/m/r/qzZ8eNGDtwMg5JMK4FDOHEqC4i6GoT3mwGjGu63oo5vkY6eIz0kM9DPNdn/RI4NGYT0M5gxmJEgTj0CO9t87wIdjrexf+7psHHrxCFM3iUWzMcTzao2aEz1DO3AM46uIemGEzn8IBSjJ4QNOAgPM/pr75Z3TfQ/cxemFTCFuyy8jn1zd/jxE5J+BIkWjW7ONaTBnbcfdTV4+USZ1Objd8ruFWiWaXo2zz52CelKpyXphcfprrQJApSfIMuzUP65OCtcKJuxTJJLxQxmR+wsBekbepBIGMV3LWyMyGUifTYVhKnLC+dm5mkMv4eIhdXcbVqJKMIp1N1ttpLcb+4jAcVoc46mU71aXpdOdQYFnL+n6/ZDhDKvt4Ux/j7eUIgnqv2/upz5JnJU+NMrW6tJYs0tgHC9GaZdkxW8q06+77074wYuwgR/3WLInpbmCo4KJklHwmwPSQTWVfuyzP5VlPrv2iieZYmRrprAWrboZGnLxMlP3KxHn3tl/PaWkvAe14Movu5KYkEYYHNd1sF1pSlXKppMd6OOPbTMH3nZE5dTVb0NVmQSjKfsFU6mzY2QtsXyyMWV+jWVXkUn5e1E2N3kixIjBPxtIDI7Z6lnV2P9z0IjWk0Ct6E/WJQwNOZqMvKtPYlztCFpcyNDXZS95tgcs3FIKWoRPc0BkiOImb7Y2MXXFxok4OF1wiQ0GrK3XMIkcu+2AW5ueDnBoRUMTUuQl74O9vi2LYohrPeMHGkK+2K3Xqvtk5qdF7kuzQx1Y4Y/6kkc1yblfALo/KjeZvM63krePC0w1RQtn5Ja8Odb7b5jJJovza966Xw05p846J2qTF2f2A9V6ShtiNjTvoie3mlnPN6SYKx3UaRs7ypudkevOqJj3SB7ClrJMlc1KjLQPsusyOqXmdV2CVb2xiThPdkl3jE4/Qmu1kEJdrLSQuvtYP6e6o7cTpkWntTS1XVaOoSUFouJSTQSYlM8GQFku6AJZHHR1vVm4ney8rS9pIzrNSNxw0r4LW3Rmm2Hu+iKq7IsqJy+5qBeFaZqalvlxpk4S+3kCOYuQkO2DSzZeJOYXXU2dQKL3R3ONpayxJi3HOYQy9uXfOuSCYFylqrFVzvKWiUICVYukEry6qpjQwLfVQtLWswvPml+tyNwFkdTSXVkpFc06blbKxEJxFlzhyYfhCITRB7J91meNPp7XrLDItkve6bi47b70KPbMlKaX1lGrCXfIMyxNRBVrPn8/HwhekYrpe6wIpycqs2QexaaW0WG5u2QSU7dnKtrPl0G8CCy8d0evc2XQ3zWdurF+vludMl/raD5p6YhrHS5CuxH0YXTb42bRP5r7aStjam92cdMYU65tRc9OpthEZf6mfpvNLxQeY1tmxVdskvZRre1/t9ANzOWv0pLNRdgiKm3AKgt3hYEiHJVCJ1EAX0626X/nqpXUMe7pHu8qzV+kSdLt2iR/UE4Fy8n5xMzil3Em1lYugq0hNFksyDMnFQGwvMuvsjlk6I6J1QstGEG/99nxNlgo153U5XZmpMV1zmSaubF2r65bqXJO8nvPlTFluZh2/xKWymqj2QXOTSD1b4LT0QvdgZWBzmg2lIh9Mw4onFSp7u9NtLviT/LyuxK2b3KYWc6rQCiUnEKGHlHNl8wDKfWMcbxwL+qTexLsF15dlMNsmOR1lDITUwIpI3LuEU+BPTPYQANSAzcoAqhu5SZfLbduQKxPSaVCCZgTlQqOxvAyvh/P1IvLQCRVX8aQJYShc7/VNXlZBgknEkldl2jzjSnMRh5uUGZvZTi+pztYU5rIRxH2hhG7EM7pRl0I1ReWdwxVTyMquriftXKyNs18JRYZTvn/hRU0q16wRGk0n16uoOvKS6bJJpW42it27bGlpaxLLMldISrwLZY4gKT7tF4aODUQ/VNhWPjTOzlRgNb2dYFaiyaGYMCCX5kyXhElacMYtq4vukg4HJbP6g5dtJ43P580iJrWJ0yX8ocdlbInvGr9dhrFyrqZJrevldGod5jewO/eoH0gJqU1lJ1TcnqZn+HJ9FBzObI3NWXVOgzzE5yo9xDfUyrzCc3d+V5ZSuw0zYstaWrCRAWfVc6qIS/R4BkfGDw3T0rfunlikFS3pVbO4DPZulaBlIidVynsb0jrB9Qk13YD1YW+ASRI2Ub/0jxU0ndLSegqLJan0fE6l2rp0LjULluzlFs2k1jgTnlvvZ6vTbe00tgJQfd5sKhaPOHQTgblxTaZ7Slz4t3SW7Tp5td7QtNEwVV7v0NwsPZ2oCNs9zYcVWQL8SGfXDKC7G2oWUpw6tmcxia7PMcHGhanALlA0vtA4uGEbVck2hw1Kdf1CMMr4tEYJE5OGa8jytq0tpLrDplhl6Kw4LFIgn5Q9ipo3ectPMgam8byIhZsWlyVYbb0jwbKJ1xeW3cw8mzZ3vL4/mLtMjYt5Jps5228JdhYaNL/RykMRbWZ51tOXXuM1Z1u17KlQo6XtBE4sb1asjknxVUvlMiF6b7bLEq8+M4IuJNmGHa65Hi6ERLlIm5ljXG20MdBruWRTcCKkdAEMHKWP6G1Bniam62NFo8/O7bZcnfSFH09Tfy8ZcpK7iQa7o2zD4HLEGDETob1wgH1lvTFwRo2FvBisDtVsGCiSY0pmxoNgdTLdhlKE1Ub28oU6510Vsyu7WjvSmh22S/S4tDFtrWodCFrlwDSymu5QzRBC+7rbYXjHhFgEtt0N9iWHHWdxoSUr3XSF0qI1t27VfK6sHeWY81OcSMgNPi0qtkchsF7rhmmGVVBEgrcatrdyByZce2l2e1cmt12Z+CK1Oax7G/p5Qm1uV2XY7NdCr95s2J6GlRDxHM+6/E6g3bRLRXaKRWgEIx4v4olQdHnE+OciQZfxPhTTLbqvM//satGO9JbmjN83a9gTlOvDCa3ULeU3PYyHdumSlN6RlpRuFe6gtHtiNhD8teA5QSHguhjlsDXMnLO/KecSe+B2+MLceupyLaggHKx5sCFYjWwWcy0RjTrM9fX2wBgUuTCV2i+HBTilfstO05s2Cdt8tTjmwn5yPtnsBpVwvVaK82W5JjX67BlLithGUp9pZqRFW0G6Nlxgi4N1y7epo3l7gAmYetyYp5pbooDUnNoWjqeArZY7Y3suM0apY0/YaCud78LG3M9ssOlBnVL5JhfsszxnsAs3MbKgZItTwUX+VZzbwy095DXG3jKCXIkn2j92RyI0KC1y4x5LcsY2rEPlufYMV8+gIs76rklrfW8G9JWtNjjDRKrk26EJDgszttY1F3scndAcFyYQ7bACzKVZUy6SbEirxVnq9g2xNNl4xszS/EA4ZlrzU/asnc57wZ/yZ+aw83LfO0aKdvNgK7J3rRRYy03kzjSX4LYW1duLPtTJUp2xCp1ip/Ci5twpKsSkisyFxB0q0yJvRxfv2Bat3NWlCrc3K5sIfUU6+81y3QvqkYo82tzbQyZeF3pqSmcIBsluYYkDZuBZykk2mZNk617WTHzQT9jKSPneITp/vV5ZxcpJ6dtWJ12WoqVMVJZMzxDJKjhrJKOa1+WF3VkHFc89SZ1ucnMflaE2XJtNndn7qFMXVCY6CYUHlaidAoNghWV+lPLqRFk0F8j7U2YEPhpXpDK1reXg4Kg8ZAmroR12ToaO1w9yNpGFpNkskqOacDapsipM8v6y1wx55Uq300VOpf0Mp9GL5Yn2akGz3EqUbXEGQnXiUrUGwcbhZOGw2w6D0+W7RIgTXq42V/62X1aJjhpxDUvJZlJI7mXSB96cCqt1TXSTAaW5pTgRTrXeo4p9wAeVX69iouOPE0fvQmcysyyp4gKf5TWKIDCmiyBQkziBizzR4GKLH8r9BAd5NFC+0+fZ9cL3cKmV+lTKdAo9EdUadP3VcwGWs4GNgqWv6G56w1s1sfXubKGUyoXNueHsfuvKeXDwmM6eu4ILC0rSA8bTOcGsTqnOC/SaVpWgzaOdvlTn6kG3DxU9rdsQ3/kMx8YUf/DFQAABJ9W8UgHYcZPDxJWmR4/hfTG6UBnlWC6zdRbXiY/5LTm72mc+kPkrztZ9ijeuFtSElyT0wEymV3TKLq8nP62n8+l0afaT/OJ7zLwmF31MtgrlScNyHmGZQKthSCuOc9BUb5kMK25FuYQwcdYSF4bMvjvNbO1AKBp/G67CRFsexVKiwgl7lUR6zxG+i03NBXUa2o6L0zYmh3YonN32Wtlxk1pDYs0B7MCvubg8hYLXN+dhoRArpr4qzi7p0VWZt/SMRnmIChxBxVKxzUUfvotoMXcPNh0G87bP5/ubzcqumKlHHPMZn2BrbXCOA+Fm61pJjow4d7Z+7yuU6kwPAXNkTIhmy8MeDa68FOrBKaTrS+itQkpn6EGAirnOtN3op4h1j/YJc2tnMk0nDqmLNp6wDXOZLXeitadqAqVIfuMJS3WRuxevydaX3U21YkFd71f1ypyrWHoahAB3d4xvbvCwEeDS18kpVLoZeCLTjGUmk4EVzT1oPIPjr/aq66OWuKjg2i6EAyGQBtPnQ0ZF+Fa9LptlfY06MAvEHeNsxeQ2EY8gnFgcXOR7O296HjaUJQiATE5sFBqaigOObcRN04uFp/TMTa3me5LXVKVUCNWMVsR5ssHmKyyiLnVjefjKBXyTX3R9SDdLGg+nMtPhCn8JS4EwD9uCuiroIesmwhyrXQnmxsTTJ4S1sciOI7QJ73F7vvFWq0txZWlxW6jbeLJAAXbZbW/xAPsq39VWwuLqunxd6p2Paxk5x3VAblAGP7t2p/cz/oIXtYICGzbNQAG0TMsWz6kHTA99MvZvRcLGYXCdTbZDyDhSAcRi6p37al4eWq7mw8kZUsVjFgj+JcAWRX1xt+1kOjB1O7UDOcGIGs9I5ereiBN1caOZLLYLapWT4pWBMTubaIQPF5Lp5eCrgahgvDf4R1PMF9hUp+hoNrUX64C+FIELFgyjWLv1SkzFrXbQQzlYVR3ZDSIjHTHGomxns6zmZE+hi0s1FabX2YalF+f1zmZof7uDusRcfciGbBcw4CT58QaflZclHfFbmxBQfLAaU1kpLF4csU7geC70JTYcPFSFNRBE4imqJhnKK2U7wWgGqN2cyDw/3mpswzsw4AOfnEcJNr/w0SE/tSYeBpcpvmb3e04lDHGBYTx2oI/aydqlUssNGq9Sqi1xLXVoo86E6xdUwepTRTf8auXpO3XWbanLAqemvS6uTjs64YL9ttpWt62S4iLNoP0Wnx7Dpp+e+nbn8WyTXFLbbPdpYkc3h6imKctZU9I4mfUl9xOnUIMZRvBLVr8NGxVvuVhaZeDGVtROS9eXWElhEVuKWU4fvCvfkoOOb47bS+7l+a7ZdO2VWdF111PnsD+zLPvzz0/PT/eT3aeXGTrHqOen8XDgbYv/724Qh0Ncvr5RwymceX76f7dv+dhDfD8EvG/5A8d/uXN/+XuC/vP5qfZiKNRjW7lJu/Btu/K/7dB++ld2jkcK/eOQejyzvLXv5yStE943t+Pc75q27l+bIu3uW9vQ5F0z/rFK8/p2yPB0Vy4rxxOL75W577pDLdri9f4HDe/z76fBGfDjx5jxMXw7EHh+8nvov9hrXvE5+QrqclT47VBq3M8dT6WefvsvumYi74EnAAA= -->
