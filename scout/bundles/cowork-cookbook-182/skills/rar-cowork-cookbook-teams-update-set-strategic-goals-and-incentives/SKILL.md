---
name: "rar-cowork-cookbook-teams-update-set-strategic-goals-and-incentives"
description: "Drafts a Teams channel post on set strategic goals and incentives status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_set_strategic_goals_and_incentives", "rar_sha256": "bb65865900d948ca317de144d9ee96c4382e9671950fe72869135678cca5f761", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_set_strategic_goals_and_incentives`. The original RAPP
agent is preserved byte-for-byte in `teams_update_set_strategic_goals_and_incentives_agent.py` and in the RCI capsule.

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

Set strategic goals and incentives Teams Channel Update — Drafts a Teams channel post on set strategic goals and incentives status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-set-strategic-goals-and-incentives
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_set_strategic_goals_and_incentives_agent.py` and embedded as the fenced Python below (sha256 bb65865900d948ca…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_set_strategic_goals_and_incentives_agent.py` first:

```bash
python3 teams_update_set_strategic_goals_and_incentives_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_set_strategic_goals_and_incentives_agent.py   # or on stdin
python3 teams_update_set_strategic_goals_and_incentives_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Set strategic goals and incentives Teams Channel Update — Drafts a Teams channel post on set strategic goals and incentives status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-set-strategic-goals-and-incentives
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_set_strategic_goals_and_incentives',
    "version": '2.0.1',
    "display_name": 'Set strategic goals and incentives Teams Channel Update',
    "description": 'Drafts a Teams channel post on set strategic goals and incentives status with an interactive Adaptive Card for quick triage.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'forecast_to_plan', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-set-strategic-goals-and-incentives',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-set-strategic-goals-and-incentives',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '8feb5f6a9a5f5e20',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/develop-business-strategy/set-strategic-goals-and-incentives'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/teams-update-set-strategic-goals-and-incentives', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class TeamsUpdateSetStrategicGoalsAndIncentives(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateSetStrategicGoalsAndIncentives'
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
    print(TeamsUpdateSetStrategicGoalsAndIncentives().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8V6aZOjSJPmX2FzPlT3UJUCcddrbbYISQhJHBI3XW3Z3CBOcQih3v7vG0jKrO7p953Znl2zVR0pIMLd43H3xz2C/O3F7bukal6+vqihW0K8m+dpEjaQWwYQVw1Vk4EfVeaBf5BflV2Ten1XNe3L55cgbP0mrbu0KsH0ZeNGXQu5kBa6RQv5iVuWYQ7VVdtBVQm1YQe1XeN2YZz6UFy5eXvXkZZ+WHbpJWzBY7frW2hIuwQ8Ak+6sHH96RnEBm59/8K5TQBFVQOd+9TPIGCOG4evwJjw6hZ1HrYvX3/+5fNLCr6/fP3txc/dFtx6uduk1wFQr4ad+m4HP5nBloHwYQSQlLtlDKbUI8ClBNd12ACFBbgVhBH0vPqhDfPoM/Tv/54NbhO3P379VkLPz7eX6c+xL6EuCaGuctsuDCDfrV0vzdNufIXYfHDHFmrCrm/KCTIATFrGr4+Z3yVVNfTT9OyHh5LXOOx++PZSARPcCfRvLz9CAIlvL00/fX+dpNQ//PiaV0PY/PDjdzlt751Cv5uEAatf357XT7Fg4PehaXTX+hOQ+nCvF357+cPips/D7mmdYObL66lKyx8eguumuoSlC9D84cd/JdZPQj/L07b7P5L780NwEroBWNPT8B8/30H+BYKfC/qQ+a/V1sCtf2clYPi7us/QE6h/JfuO/38QnaclCOl3xP+puH82Af4J+vlfru0/m/AZir69LMMcBHHjenn4FfrtTVVW3M+fgu83P/3yOxD9X4pRq77x7xLeCrdMo7Dt3t5+/tTeb3/65edPfQ1iDaTUW9/k/0zmP8P1rudPCD5H/fDnuUC/XmZlNZTQR6RDv1X1/2h+f4UMN0+D7/fbr9Af82X6wNC0iHelDwj+kDMtsPUPOP748jsgixKspvfvj0GW/9u/QWLqN1VbRR2k+lXfQcDBXVqEk/FakrYQ+DvldhMCXNsUAPscB+J/8vBkcRVBv/5P/06gX/wngc66iYbe+jsPvQFGfPtgxLc7I74BRnz7zoi/vkIaUFM1aZyWbg4dWUX5VgLCK7vJhLoJ27C5AHLxxi78Amjpy/QFECf069/U9HYX+lqPvz5J+b6+IydMvNX2efg6rd1MwvK5Uh8QdHgN/R7oyysfGBelgH0/A0zaKgdE3U04tVma51CQNgCUqhnvsgGWXydhv/76q+e2ybfyQbQY9Cgm7QwM+DAH+vIFrDLK0zjpvpWhn1TQp99+/wT9L+g/m3UXPulQAPs/PQUs3KqyBIHM6wswDDgRuB3Qyt1Tv/3+xBqIKUH1A35NozR8TAaRm4XBO/Dqhv0yJ0jICwHgAOyirpoOsDeUdq+QEEEf9gKl06OJ35OpCAZhHZZBWPojkOqC5XwgWVagNoLwbKPxM9S34V3rr17j3k0sAAW43a+QyCmgmlQ5+G8y8z4ITK7KFMD/ERaP+0BI86mFFu8iXiFpilWodhu3Thr3qSNyH34BVeR9OhDuQmU4fCunGhpOUN0T5wEPGASQ8Z8u/TL5HHQFBWCJoH3XfR/jTjVPu9e+5lvZPpPCbSZX+KBIAKVxnwZTqfjHM6TapOrz4I4fsHSS9PRC8PTKPQbV/7qPeDQg3LMBeVR96Fs/R1Ac+v/ZpUzmszx/XPGstlpCK0k72g9Yp8Zqgv/Ri4Ee4T75nkLf+4Z31nkn329lnoIYacZ/PEbenfEc8yC0vgHYHdnjXT6IBADrJPceqFPgNc0U4u638p3lPwNg7pQGoABZDaJ+CrZ3hdPTd0sTkLrT9feKf3csWDaACwQjVPdeDiCMwjDw3AmDpJmS7ekGELXhlHhDkvrJn1YFAekgOID8yR8p8BWoBHfopAosE+RZ1FTF9+Hp1EcBK4LeB9aCzjV8hUyQL1PMtCBJQTM0jQEofLqLgooQYAxM/EC4Tdz6YczU7D4NdCdfVMUUOX/wwPPh9wi/2zKZD6S6IM4AlsNEwEF4fXj2w86nr4CxxZST90l/dvdzrdAfy9E/vpV3Gz84H6R6PlXyP4ADgQAsHmE6MVUL2KYInwEEIuFetF8fdfdR2D9s+fqXDv+Hv7cJuFdS/c+e+wolXVe3X2ezR/V7L36vgCdmIEbSOmwfhfDLozx9AUn35SPpvtyT7gvQ/OV70v1JzQO1r9DfM/VPIp4x/hVCX5FXZHq0T4EuAM3zA5DhvizsL/j09Ft5DL+7/BkXE+nmI6i8HxXofQgoQ3ETxtPgR0Vqp0I2gNp5p2DglG/lR1g8k2bioXgqn231h2S+Mw9w8sOHH5UCPCo7oDuY2rrH7iefzG/Dl69ln+efX0q3CP/mrmeqDCCIATDTvgkkFOiYujS8X310T9PFn3d991QDHBFUX6eM+wxNne5n6KNp/Qy9byPum7SyB/uon6eGeVIJhoIfH2M/tpRe+AL2cN1YT4t47I2mPu3ZP//ViCnRgMV+OFX76iNzJ41/EQK+xHHY/FWIfP/i5k/6ADQ/1e60e0/6FtgZgE7oMwTcCJIR5BegzR5M+KsaoKcJAfcD/p2W+x2/78uqHmv5/Q5D99hg/vbyTiNPHzybSTAc5OuXdiqTMxCyQCG4fgQXePZ/22Y+xQEeBH0NkOd5JEGTBIMgAYPTvouhVBCiOB4wYciQPo7Rc/CTQhkCiUJqTpMMihEkRfu+S0QUiQJ5j4h9m1qDdDIxBCMxBp37AUbOCQJnUGruMoGLU64bIDRNIVQUgFLxfWoGSPS57sc6J1A/Ot4Jn+fyf3vxSByM3OCtwD4+3IwxXBKnvGtiwQ0Z2uIJRgok1XHGWeywcO9JToMiy5Zfk+XBY48FtyKy1Nn7ZiyTnkmaHKtkaiRmswPl4LalR3tST47rJReaMh/JpXIhbvlisRKG3uCM1vDrXWMdUiNzCqON6bVWK8aaqiX6vDOQum+WiTferlYRpbC6WrXRZYZKM77KxXZHbPGUPqrr1tGH3ltenDnSmIFhWnJ3Pqlma+zOOufOtwh6MGfyWszPuV3kO7opjXHr1upI6LsjqWhbhAnLE01ElgWr22EWzazxinK0mfZHXlkKu3EDMhzdWSZKuJRlZivaFDvbUXwZ49ojykZZDI8nzVfLPaVLm15SHTdLWJ0LDMut9cvyyozhmN9ya+ttdCM9+wa/DfPk5IzdliestPY0k9Ml8ozwhSdom90ac4z6RCrGsSXRjr+QVq0VJ7/KNU7a5ce0Wq5lid6Psogml7NxcFV0O1se8Lq40Vh/3BY7YKiclxeSU9g+GFRvtlsm1UwMDqSmaNFhj8Jbx8zmG22F7I+WrMHtyj8TxlnfXwe0Nqvz9bab74zC7NM4qk9OephzjSMdSTShjMrUkq1mNesq668XKTlUinvRxqxZhJs0lNO14DaclnIZ0VeeQaMqEzhES0SKHDusV0gk4QQhY2VKG/QkNw+x5crveVPgjXnUOdtCxLtGFg77Y2etroXcwKNdIPOx9fcKPzuL5zW7gnecQrncTTQd27CU077Y0Q6N9zkrYKOPH1oJvm3WwiHGL8FhvOWKbSv7WcQEht/s+nOrKM5e5qU0oK1tYd8OiFYdutw5Wtm80bJljaQX1+lCHSEvuwMJ+Ks0FFp3PA6HtY6FF9eZ4s/WecjBdEIYF+lAcmY0RKZstHA7VxCKif3oqAY2Na/c5ZZF26OHG5Kao3rQuYfjZofuOnOXcso8H+b7vS+44y3Vy+X6HNOrcsGYbg5CIdwVVoteA3x9KeUmpm8Del5tvZHLwlJc1dtOlVj82K11R+509ShfxbmQs0nbZq69sMRjvheqOr3Jy0W1WVFhOOIYR16ShiCdGh+jsqBPxLbaXqrOxlZRW8Tl4kgQ/ZWAQdlLb5eBJCKpZTTP7kTvrBSXFdwiI0IR9q0/zeqZ0RP8dhEetSZUUj8votGw1k17uZKxI7lacOycTDIzvKySq7XudddsT+u9vZoxwi2SBn1tYWcZ7+EDkhrq6sg56s4utWJQk95wM2aJoeGQanSM+QIqN5tjSTHkaleMPMDdYgvn5hw95DxiNWFRgTqv+cw1jPPArMqrRmAndbU97Jj0bJwMDU6So98t8XYt1qfyvLQQRYndoTma6tDZ1bCUIi4r8czytHZ79WEYRdT62Na6MkpWtuxyXd+RmEZVwMEJccXHUVO8eBGooEvH8nzO4bhWr/lCswQeRbfliQ98Uh0LG8mFy5lZlOvRL5JN5BD9LtYsnI5Qy3S7XSdHtVDTxEG+Zhh2Dpqs0A9K7FfkTTgNp+7slYxmEzPBuZg7pkQzQaMEcoakEb93FCxxG5oYZiGuOYYmNJ7k67SgNAtRuQTqZrZV08RXroSUXA84pp5pJ4adHeqyK8Xuo1bb3G4VzSal3G9VrUjLE8qstT3vXiraxvl69JRus+eFtBKzTmcZ4mBvGZ5G8tjGxUXn9IdqsVVzfeUxUiyd5xjl2wPH24tKYMlGbc87zuHrk7xe95za4puh1mWfy47zTeHujp26MhMkUWcbxYD7YafKc9s3OxPLVebSemK0aW/xjbavSGlhFCPfaNjXifZw0EXUWaLwHFRia9x2sIvxt7m8GAXR2ALC5DYXNNY7pg9tLNgvEEuwCP8cNUtavRCSksewroTeQeG9uLFtmiaxte2vdklkGCQg0U0hpmsDOMEYz45IHmDeo9DIO+3q6wpjj/X2vCdojjKlUl9rGSq0OUWx56xO3bE7bRXdKUpjmwek6/errcUbG0e0XLGGA2Wn7ctsj9UZum5lvUXVw3YvriW5uNxUot+izIEX+vme1vX1Rtv67tI97Xt1V3fDodQ7F5kXQ+c0Zl5r1KjsEyN2i7UYkubttFZhXo2GkinEPuIFMRyMdrRka9vtisIurqeOwdLSkvvN6KSDk1DSEt+BUFJDiVwn58jVHEwjqdKOKZOPVdiy5kqC7/1FQQmb7XgcyLm4NBYV55kKLG/Zq9vaEi8p2lE0jvvDyk90RbLz5RaPDwukCvN542ed4dh7F91rYi86K1XgtrsKEDDj03QUuudsXkSytMYZWd+bi6zB1wyb47yXGMpR9RplnVOgtCoxRpgkO7LMGRT0ObZqhPVWxPhjxdvr1Y3ewd0GDQtklDMhPVs8S9BHNo4WqEQ3vHoS7BNvblvbT4ewE+fcfDHbeG4hePbWvEQ3o6PEw5Wqq1Lfc+0CpsJRTlbbjTSXj6k4lJEUNs0QkjOfPUmcN9SqAQt2WAY7LbPO3nknqLcbFzpxtaR4eQmDTX6eJEWxlW7HfZCA9LwYHLpeiGnHRpzSiGfTX7DscD50TOsH+whJspqtRBY7KLN+7zk+TtqeifjxWpubhwRbEBJMy9c8KfW8tY66ay1CNdnMCAJum0i2lvm0Q4mD+cIOOqU+pHJprinQOpX4OJ9HJZojPYaErROetlex9qIOa9lO3LCnY7yMyzK0VvjuLGUHtqX5jhVnFyMtN/EMSfRaivlrnctC1Vv1GCEqi+apdbDXMlNULTvmOp+65FCmoBuy0d3aVXst0X1qJPpsvWPIHXozm2A8azuSdRP/XG5u0eEmsLaYRFI0ng5uLyAVvtH4II23Vy0YyttmWauLTVaJjFhqu6UOa2ydsSNy0iUk3RizVcEcdYqM7aAQEAuTqHEx2xcZs4hkcXWVhZzYj0zszJfjKbWCNbtzxqQWCHY/G0rVysS45GrVzrSrzW12Un9e7lwty4i2q+rWR5zzTTuJODEiqNsIwzhjay7K9ltNOlsAJ9HPxMIMFn7RnWt6IMbW6vXRv7rHxru5tEfsnb5aJmZT8BshqjfKGqXRnbc7iE6vbFM+ksx9IQurDtnyOFBJzHQ9B500jwbBrbbP43alUVsXMTJstmF3J2m2wa3UMtwVkQ8ZnnO7wc5ZFfFiYcX7GLdCl7fjUcoF3QfiDn4ijUzJ7uxVr8BwS+JLze3IiEbipXgeT9GQK8YN22IWL6iIAsqUZpDo1soXmmAyOg8LWkHEQ85jnNrFCi9IsLHTkpnZqlvivNLG9KASfL6LTJIgDlgoFOh5IzSuvr0VIcmrxc0xxSWIBtFT1gFDkceBLwn26jh7vbhVJ100SoWQLDXnHAYuHSIFwZilVqKjJlxwXDH2UrZbZ5ViGzosX6UDF8RcaUVCv7xiCa9ctJphY3zBJLPeiTZatJcxI9PcrBqE20jneWakcQ8jZobBJVlihQB38VGwed7C+ZwUWYvemEZhlNq1hk8wGjAlskn2Fp05SzMZEN11r6RJ6GWu5VKS6PvF1d7dhOFaHLpwS97U7eG25SSRkC97vqBKFE6Tc3szY1YeuLGdKQOHWSbRD3yxXh+APyliHrjGimDslWl7uVWu5NXYtbrEicfQIpICdSR/Bh8pwTrmwVk+p6yNKtxSDom+1NanVRg4mNnRdMwtznxzlkCzSFX96WbkhbfaUNoy42fp8uQ1Vqn0EuxdF0hLbpp5EzCzNlC8AhR8xvF2lLJPQWGkPavH+31lU8FIBYuko1xaYqylaGSd1mNbFSGZowv4R22lfjlq+JqNWcLYF/uq7vtQmAWSZIdasGHro3nM6oo4Ru7KXi5hjPCQ1Ix3chwiY3+RrpTJLuIMr8TlujfbdQjv/fmxmcuWFdjVTKsxV2GHKNg03PVCOntYPfddtDwU3jzoUJRFU3YmxwTGdtQaK8hhU9G0e5kxHTq7rm9sOyBUc5nhyeziqXPsEtgzvnGRq97VUbHY8BedFa/SAlmXiX3T3OUtrkJvENB4xpba8SiItNJ6RWDoQs8hAu3TCyU7mgtSC3EllrnjbJ1FG5m5IEg/9ykqsxde3PuUT/Knm382umZriDgql/k2pLdXzHQWG7HZisMIL3uXHtATIJQFa8x8KZc4uGLiUMZHd+lcJXBPuCyI+RyNBEDidErsbTJb2SdskW5mAtzjrIE7bbuNlZtuZNsxTJmAh4kwocsgOkdwG9WIXXFUZSn4Nh+Eph1CFRuizSGoSNgZ3bPldaE8Z9tDnLQ7mhLRLgJ9f8dUtzN5jc0QI0Gbd1Z81A8DOjZlTj2xN+bWhx57sPDT3lGXq6V2TLfMeq+3TCpazYYBjC2xGb+Yp3ZJ4dL1ME/2ImNpt1vIYpEermz7eMN1npVPnZBdwqFerjCSIdLbdV9acw4OF0mji1bC7mj3Kkfn5oJ5HUiZ65LBN+RhNzgzxS4dE1eEE7Bn4bB5tbhQyDj43HJpJ/F5v6FnldP0Unsoygs+yiusKqtthO/baweHlEqtDhJeYD4Dmirdd/YLj6n4a4SFt6Ragl2KjIHtFsM73ioCuRQUzK2lFhcsPnRGuRMxdgBFIl4010E6LY8YjoPmp92snHKjz5b9gjpZZdOGuMz6wjqeoxvssAy8/iSh+zYNSK+mLgFoepL8vAm9a2hVfhod5rS+tANcr2Q2nxkkh9ULjE9FbreYLS38Jp/QqrjS4YkZtd3lXIRI1x5OZBlwWigs8OOcgat92jPdfDZ3Bu8WoCUtBWEIE5UPMGEj6lLCgIUz1sNU3PCJSC5Q+Nb6l0JObMtZSviGLlsPlBcsa83Iouj1DLb7gy+eLjKVSgyzuyi4KmZWoOtXVgr5c0sWlDjjmcUy84yoNSrcOVN0eolhpKFtk3VZzl6fQUKXGNgjXdlre9MxwfZ7RYdvLlWgWDqax3kPC7sjyPh1kpaIj4jKYRkz8SDH8cFJHZfegzu3blhrmnfthnmkeRHIZV+NJGXhNqy5qFcSqvQ+o12phZXgIGOLjhouF3yj2/KOvfiCdvXdxUXEfVE4l2OMsdfzolwWwooe6R0/x5wTIuwCrKrdZd+NC9/xFhVMye14oWd2d1hvo3V5vPlLSikGpsmQ0qTnHHNLqbYblSvVXYTVkVbSYj3LjTXmpgsdqy+JxulLdE+UdbfpegKXQVdObzaxhFxFPm2v4YrnC3J13nDaiTnEDSOoDrrJLN+d4csTKUoXr6KW28byBITxs2SuzGKpijh/5MaKZdmffnr5/DIdYj+Pov+776OnA8H/Z+eSjyPE9xdW94Po0A2+3nV9/W9b+Mvnl8ZPgX2Pk9k27+PnweV/OJf98jffekzCxscL4Omt27V7P97v3Hj6PaeXtAx6IGJ8a6u8vx8Uf37x+nb6RYv27Xkg/nJfclFPp+t/XOLknqoJfbft3rrq7XkWf3+bWYRB+hgxXcbPo+vPL8EInJn67RtGEm9hU08rf75JAQuevyKvAOL/Dco96hxRJgAA -->
