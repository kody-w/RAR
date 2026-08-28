---
name: "rar-cowork-cookbook-campaign-narrative-architecture-board"
description: "Turn a campaign narrative into a structured visual the team can pressure-test before any copy gets written - so the story holds together across every audience, channel, and asset."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/campaign_narrative_architecture_board", "rar_sha256": "cd11bbd026ebac6308b3cea4564b341615b46400720aedb6c5afbca2c29a7c6c", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "concept_to_market", "advanced", "integration", "miro"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/campaign_narrative_architecture_board`. The original RAPP
agent is preserved byte-for-byte in `campaign_narrative_architecture_board_agent.py` and in the RCI capsule.

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

Build a campaign narrative architecture board — Turn a campaign narrative into a structured visual the team can pressure-test before any copy gets written - so the story holds together across every audience, channel, and asset.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/campaign-narrative-architecture-board
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `campaign_narrative_architecture_board_agent.py` and embedded as the fenced Python below (sha256 cd11bbd026ebac63…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `campaign_narrative_architecture_board_agent.py` first:

```bash
python3 campaign_narrative_architecture_board_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 campaign_narrative_architecture_board_agent.py   # or on stdin
python3 campaign_narrative_architecture_board_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Build a campaign narrative architecture board — Turn a campaign narrative into a structured visual the team can pressure-test before any copy gets written - so the story holds together across every audience, channel, and asset.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/campaign-narrative-architecture-board
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/campaign_narrative_architecture_board',
    "version": '2.0.0',
    "display_name": 'Build a campaign narrative architecture board',
    "description": 'Turn a campaign narrative into a structured visual the team can pressure-test before any copy gets written - so the story holds together across every audience, channel, and asset.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'other', 'concept_to_market', 'advanced', 'integration', 'miro'],
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
        "upstream_slug": 'campaign-narrative-architecture-board',
        "upstream_url": 'https://coworkcookbook.com/recipes/campaign-narrative-architecture-board',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'a763243606223948',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'advanced', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'miro', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/prepare-marketing-campaigns/develop-campaign-themes-and-messages'], 'recipe_category': 'other', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/campaign-narrative-architecture-board', 'uses_skills': {'custom': [], 'ootb': [], 'plugin': []}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.667, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class CampaignNarrativeArchitectureBoard(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'CampaignNarrativeArchitectureBoard'
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
    print(CampaignNarrativeArchitectureBoard().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/9V6aZOb2JbtX+Flf7CrZSdITMI3bkQDGpAYJRACyhUu5lGAGAXV9d/7ICnTrr51+9168b607IyUxGHPe619Dvnbi902UVG9fHlRfTuHtnaWxZFfQXbuQWzRF1UKfhWpA34gt8ibKnbapqjql08vnl+7VVw2cZGD27W2yiEbcu1LacdhDuV2VdlN3PlQnDcFuFI3Ves2beV7UBfXrZ1BTeRDjW9fwE05VFZ+XYOrnxu/biDHD4rKB1YMQGs5QKHf1FBfxU3j59BnqC7uN9fAkgGKisyroaYAa+6Wu1VR15Df+eCa3Xqxn7v+J8iN7Dz3s093z+y69ptX4IN/A/Zmfv3y5edfPr3E4P3Ll99e3AwsAD6xT2ekN1/oyo3ixr+7wRR25QERmZ2HYG05gDjm4HPpV8D2C/jK8wPo+elj7WfBJ+jf/z3t7Sqsf/ryNYeer68v079jmz/iUdh1A0Lk2qXtxFncDK8QnfX2UEOVD9Tm9SOUcR6+Pu78Lqkoob9P1z4+lLyCgHz8+lIAE+wpSV9ffoKKCuir2un96ySl/PjTa1b0fvXxp+9y6tZJgI+TMGD167fn56dYsPD70ji4a/07kPooB8f/+vKDc9PrYffkJ7jz5TUp4vzjQ3BZFZ2f2yA/H3/6Z2LdyHfTLK6bf0nuzw/BkW97wKen4T99ugf5F2j2dOhd5j9XW4K0/hVPwPI3dZ+gZ6D+mex7/P+b6CzO/fo94n8q7s9umP0d+vmf+vY/3fAJCr6+rPwMFHVlO5n/Bfrtm6qs2Z8/eN+//PDL70D0/1WMWrSVe5fw7WLncQAa+Nu3nz/U968//PLzh7YEtQYa/VtbZX8m88/ietfzhwg+V338471A/ylP86LPofdKh34ryv9T/f4K6XYWe9+/r79AP/bL9JpBkxNvSh8h+KFnamDrD3H86eV3gBL5A8qmy6DL/+3fIDGeMKcIGkh1i7aBQIKb+OJPxmtRXEPg/9Tb1YRJdQwC+1wH6n/K8GRxEUC//od7B9zP7hNw4Tcw/fYOpt/sHxDomzNB0K+vkAaEF1UcxjlA1SOtKF9zO/TzZlI84apfdQBSnKHxPwMw+jy9AagM/fovyf92F/VaDr/eoTN+4NSR3U0YVbeZ/zr5eY4AMD+8mtDcv/luC7RkhQtMCmIAsZ+A/3WRAUJoppjUaZxlkBdXQNeE4pNsELcvk7Bff/3Vsevoa/4AVRR6EE0NgwXv5kCfPwPfgiwOo+Zr7rtRAX347fcP0H9C/9Ndd+GTDgVA/DMrwMK9KksQ6LL2ApaBhIEUAwi5Z+W3358RBmJywC8gh3EQ+4+bQZWmvvcWbpWjPy9w4o29AJ0UVQOQGoqbV2gXQO/2AqXTpQnLowLQneeXfu4BohqAVBu48x7JvGigGqSmDoZPUFv7d62/OpV9N/EC2t1ufoVEVgHMUQBKLSYz74vAzUUeg/C/F8PjeyCk+lBDzJuIV0ia6hIq7couo8p+6gjsR14AY7zdfqfx3O+/5hNR+lOo7k3yCA9YBCLjPlP6eco54O4LQASvftN9X2NP/Kbdea76mtfPBrCrKRVucaftsI29iRb+9iypOirazLvHD1g6SXpmwXtm5V6DTBuDRX86g/xY1tC9rKGv7QKZY9D/wrll8pXebo/rLa2tV9Ba0o7mIwfThDbl6jHUgeEBAuY8+u37QPEGR2+o/DXPYlBQ1fC3x8p75p5rfnD+SB/v8kHZAGsnufeqnqq0qqZ+sL/mb/APrIXuWAcSCyAAtMhUmW8Kp6tvlkagz6fP30eBexWA/AB/QeVCZetkoKoC3/cc202BVdXUmc/sgRL3py7to9iN/uAVBKRPQbZrCBgRgzQAiriHTiqAm6Apg6q4fF8eTwMWsMJrXWAtSIj/Cp1Bc00FVoO8gilpWgOi8OEuCrqAtBXAxPcI15FdPoyZpuangfaUi+ICav7HDDwvfm+Huy2T+UCq7dkNiGU/VaDn3x6ZfbfzmStg7GVq4PtNf0z301foR57629f8buM7LQBcyCaK/yE4oKarS32vswnWalCgF/9ZQKAS7mz++iDkB+O/2/LlH7YKH//abuJOsac/Zu4LFDVNWX+B4QctvrHiKwAVGNRIXPr1O0N+fm/bzz+2+ud7q/9B+CNWX6C/ZuAfRDwr+ws0f0VekemSELtTt76NCSAe7GfG/IxNV7/mR/97op/VMOFyNgBKfieptyWAqcLKD6fFD9KqJ67rAb3eURqk4mv+XgzPVpkwIpwY9o4vby18Z2uQ2kfm3skEXMoboNubprzQn3ZB2WR+7b98ydss+/SS2xf/X939TKwBahZEZNo4gf4Bk1MT+/dP71PU9OGPu8V7ZwFI8IovU4N9gqaJdwK75/D6CXrbTtx3aXkL9lM/T4PzpBIsBb/e175vRR3/BWzimqGcrH/skaZ57TlH/6MRU18Bi11/mgSK90adNP6DEPAmDP3qH4XI9zd29kSLurEnXo+btx6vgZ0emJI+TcgOeg+0E0BJQCN/ogboqfxrCwjUm9z9Hr/vbhUPX36/h6F5bDR/e3lDjWcOnkMlWA7a83M9USgMahUoBJ8fVQWu/b+Nm08hAOzApAOkuN587jgesiB8gM8Eiiwd1PVtDCcwB8XmxBx3MAJDEHKB2ADCCRe3A8e1F+6CskmXcIG8R4F+m4aFeDJsYdvu0iXnmEeRNuH6KDKJnC/mHon6CE6hwXLpY773/dYUIOXT24d3UyjfJ98pKk+nf3txCAys5LB6Rz9eLEzpNmkJThMZVEV49OUI25qq8bUu57pfyvOynRN4bi69qBVvGddju3TPboT14caQWeUtrHR53GO9Ru1HoWf5olU7TymSvDvXWUi3Qktyre+z8XVfUMJKP6pEOsjqJc1LPc6Ec3MekezID2NjEyc91+bpNT02Nj6TF4axPIN2IhSBYjJzZOILWWVH54Ihla1H5+SsJkfeqdhiszk3lWgUzWa7WNuZvS1iA9ettGyufHa+1i2PzxEiUrXdad5J4aJsCL5Rs4G/XVfyudFZPNdv2TWqIm1r7ZtKP1vXXcXPhXWjayytMaR0loJN4SkOtjRb4bbwO6HCjpsl5XdBGG2uy1BKxKy5XPp2kzqkkOon2nTssJF4PL+GJRkJFB9VBt1z2/2JENQzFZiVhG5L9na+UGtyhrX9JsZ9IuKLVE/ADkLa0+5mXlnmyXXOapmRNCMxJyykzpfNztgL1dr2wtFBzsnBHdDm0hGtncuZWuRJnJUZU5DM+eRh6NXejPVRvWqDvlB1JAy1vPH4k1rGWbshK0eYo1zI7a3NrWSO2kEUZrhw2Q5W7+T83IvPVic5yV4+x12dk65F7Q6Ozg4zY9ls59t5ibkoa0iiy3GwGNaH7ZgIOIhqbbgdb5+Fqzq3pLRDpWNiXx30ZJ/V1FwtqbHsj+XKWA8ZhriGLi9x/yotF2qeo66cSSNNiVgzm5Hz/fJ4xQfCRA1sbjZoGl9HEY2X/MXlbzJWh6HcSrhNXz0uK9cm4uC+uMkTr8nVzNTM2ICFjWaxpLw6wnN0nwgbBd4Mp3YjcbEoaConqge5xFcrG0dZQThRkXuDya65Co0lnagcd/bOra+HLh7l8aKuY483aoHVimbdHWxtlpT4eAy8XNY45eb61XwfhEVedAo2djfOvC2vo8SrLQf3RydHMBfWBJjG5HizqHKDwehLu6A2bXRaXFFDX2wuZlon+jUzq0s59NmiF2sh8s1b7KRhszUOCZaxtHtmU9I9hqpYnuXDDZ+vYonmUyQRdg7PZF0ubmQqjMXElMVCPfHyvsiw3RbfertkZ13qtT4ejJO6ALud6jpyq9iWha1KZsctM4dJqx9XHlkq+z3CpTkBfszdQuxuXqsyEpLZmJO3jqXvHG+/kM8JLfQamPUZ+GDBh3Wo7NENo2IB1gq0RNxavM4Syg/73jY40TnvJcTaR7dIvGlZLcCCuaD9fTZbo8qS22hSoO1TkURoczfqmr43b3RP2UZ8srJgfRJyAAMXna2H61EmEedkCWS/3Zp7gtG7w9aoRjmcw1F1YYzTJdlYS0128FId+/16Uc1doovCk6rrqHo6+kGqhuto6McsKnHOmMvLMduXnm+rvLLXlBuntFihxihMuqWSbrtcg5l2HyLq9XqrAF56bL4oA1fdxZUz9KvzISJhhzdJVPDavs9VnqvTdpdVZS9msmzOmMZo60ytLEFycZWXKXVEL8tDv1sG8zNqVzvHhUUt15oVaRvBjGP8gd8wBTNYC8/caEbPkYppMEGdNpfIqMQrZyqbI+vDwYxXergNfcVO8I525wqfhowQyGq4JRNs0FYCerqhg1oshNXga2vXCqVxoycxNzJtHiyZfDMEMebDMduzZ6+3cl7Or55i1Lp4Pe0tnNrB0vl8y1Wl3a5H+noqNQena7jfiIxFhjteuvkmtTplYaynYr+4EktvMIK15dCyyNRyxhnbWGp6ItqOYmQZSUSH+4N90MdL5OxueyPF+LHHyDzrGXUDiJ4YD/ygM8RozSw8txZZhEQXzwucJoVlwRqWncqqZkZu7VBRUFU9WYlxS9RKxFOOTus2OdQjDcN1ynZbnEyaBceaxWHmG5SP+nDLBfDYLUhvBlOU2cKz9eoWEzvZzPPsglkrOg438nxHHPCGq6sVPUO3bYa0XnPQaacilHKnr8UDyWQpm7RGuLXTNlwkTorsVIQsLtd0x9tlkp+8AyOf9+TplhwXmpR0S6OzL3zOkYjeceV5h1HS5SQs1IFF0f1iH28r4TDm+1Pt7k+oJZb0ZZaQDBDi6h3bq4tutxSKQTvROj+/DrdZJWXnnJ2Ri0bMnOHsUEbYJnGChiZNn4+gywGX8HLsSjNRNBLeES1XJba8LXFjmygZ4Zo1nB+XQ5X5+yjInHWykm0yqw/XaNl3vZvxJ4anEtMk5txu0cWssMHKbedoKwVbMFyTz7ueXlc8q+9Ife8jx2C5Xqc+0s/DuYeetgrln6qdMUiHYn7I5P5gsRQTb3f+PjGHSDoOgiPOM8w/4bfxNEvZo8JkNAWwgb31EZ5hF5XLCgyAGTckXo/6h6zZ4fRhsdzzWBntOlTTZ1dLOByx4nRSBfOmkOJ8FfZgHtkiOIs5MiIYC7fDY0uRTsh8QBy3heFcAxuAXbfdAdgtGH4zGnVH41o2VJQpdHYmombMUXIs5sV42mKFuTxqksFzBzJBhpCfCW1qav2ed3eoKeAZ2uKLokxTdQWmi32sG5t1iLOCNUfO3IW4IB1sr0tRXLIx4QWRSfvDCgUsdknS8OreVO6KBZLrrcpiZs0FR890ptJ0nFAaOBfQgdOq3DWJXUSGSWXnHXakXZ9Ay1LyqDKrazioVFzqSsocqMsq9uwL7ISwdSpWSOZE9So3LGLdRgxzCB1KWrkkYJacHhfRMpKii0FnXHzquNvMPWHSsA/VM31C2C0yngCjnHriIpQhdSBbPrk2I+P6pN0Tqc5SxAIXtpU+XMOuym7Xkw0GRO4qJa7Ex2C+4sPD6qBpqSfixJ41AOQfl77hxFeWU0QBmZk1Rvd4zV8OCaeWoaHtJINSHZzVhMovh8H2Mr2h4eymzsIm3+5xmc9wYRgPmiTYYHrZbCiHukXlLmvUnV8uxO0Jubl2zFMWvyaXAUoa8x1+Ohhzzzgs66a2WJXAF7tgu8abo3fyL1GmsBTb9miYet6y2lKsq2enTYlSQhmdLs31SplpaKhDw8YeU1Z7uPHOkbLW4+shyHdhI4uE7saDu0CYHkNxXlLx0i11fpMLIAr1gjBh2gtKfzegWlJ6+92pwCx0eT0ntkeNs8EVArRnZ2CTUKS7ZuOsy6PMb/wVv11tuA1xm0mOkDZ1yWqZnenJrvK2Y+i0az62lyjpHOCruvXQgkVjsPHIy4gV5at5va1sQGfskc6vRVuwHk0QPX3cSRRi7E9Bq6JiZOQqEhxO7A05ltlKTeaMtDoSrXFqrmMDZ33FFcnhbM10xtyrl7jvEd2LReLsrBqEJyIwDFirq2X5i4sA+mQp4Qpun1RGrmec07j4pt4Tzq4FeVA4LZ4jh/DA5thVH1J92zRtvZLE1necVTJuRZg3NZzqekaiM8vl/GOrej65uGT0MYzyaCRP9SWLl/i+VZwrAJ5ZIZ1TT9j0bF+vu0JZLe2lgm2rka7ayNLWJNjUsAKdH2FKdbHdXuQ2mxJZVu4i40NxV7tS38srWt9vOfbGHG9BIvLZSkx3iHAisDoPzP6CHAQdVjJGLmaLVMsIjZSTEMcdwHX8ITROtYOZbRf2hHcMM4veWPhtdZRKch8pQ0arebbee50xoJLcWthmngf6bo4oscH6ZNpWlcUcNwdrV6GW3BJCNmgRrS4anEHNDr+2ZaH7uI4Z2IarqOAWcIXjGbh1pUC/tq3W3dIAjfozdYZPXEspZGhWzUAWUVGTO0Saj+sLf1Uz1AHlJ9qlLwleft5wR1xZbQ0ar6/WrRlMVEZpv0XtbIFXy5Fi9wsxkaYmO6QqCkpbrmM3plc2V7OVM7oeE/DJPAmLfiYTIZyynocIcGEfPUmLDxTXVj2+lZwCNhcSZeFG3831DCPE0R+axjsItgn6xSaRMxGTKGWuEM/XydmCmMEY7a2vS4YnYHh5gEdk2ZQk6ijNsOgQTbANFDnGArYh7F0j75KlYRwagiwqJ1uG83PQ7+GTeF4dEyJTb3YfmhjpHvbJyFEMu1cGZ370mKumEK2GkPPMb7PzGFLuSoyz8+LkcwfEJ0PufK5TF4BkviwrNNuK6R7sWlj2MiYKsXXzcVUpyZwWdkZDrJVBWfqrwPOOl/URg4N4U3DKsCBJtsud2PGsbSrOZTldUeKKq+Tlwl0xabHUlzZL2FTLMgR3Q+xVbhu438w6mLjdkCSLdG9dwrQYMRuqXZUNxZUIZ7VBTYnRBuBY0sSCvFs7bCePImmgdSscCJnw3fUGGFV4tx514eXSKQOlXs/XtEG2ej1LoiASuw2+PTRjeJT71L8q0VG9bZ15PlMUVVhzTLqqO60ht9hOJzOw99pbaHxYFbdcy7n4gG0sgWCkQMJIcU2yAk64ew9f5GslVDZ8nzWbEYvm/nwnBouxQcmGkDAqoorV9WBfbRLWCXPAQNrCeNw4YcpKjbMeep8QaDMKqwpFZsVJWmxLUVOC28KzjIPWqzPEUBVnSc2r+kijF8cb52l9k0bJFpSSWTgoJ7MM7ZlOv2jdI9wZLJYw4E29aL3MkWaYtkF4NyU6huFmSVJxWuhst6vu1puJZLa7UfYGWJj5VozmWe0hNY3bAlMDMo2pviE4Q5oNVacJMtl7LbqrpQNJEjzmJ3PjyqAhErAKzRyoHT9TkFWX5G5+DI8HpTbhrb7wvfVe1pCgU63j6gQodt6ffU2oPSeiFVZGPX+gXXi7suBLh/qOX8Ooc8n9juXBeB7TMApzq/KkyDs0z/u2J2bzpoKNsAqKbEW21y2p5MQROxNI1+63FgV3SABjKzPDeHlJtjvUQCo3itbD0cMOZUybS0l3GrLWwCwuy8fmFJn5ERl19KoHDJjosV6ikXWKCaf5UleUESnibXLuG5Srz51Uz/a2c0XQGNU7tE3jEL0ud+L+FI1DeCPWHoewq9oW1+5528aagsrCITkRnM/kOwsMPTCgB5Ih1oFKnemaPm6phVIuqcOelLme0Dc34zTHcnJMRnrb94zBIti57ZkxSPiEZ8BkW24t2sJIfk+LAU91TLl2s846z7kVKshjIotdefEIH6dhcnZUA9oKNjILqkvtxEiqMoRTl7J5Jm9O2A7wnmjgnarttPicDedIvfk3rLZOAVEyVwVsp3G0y5sOpzmFwF1mDCU0tYXtuMEPpu0Uwu7M5tWMpA30uDNUe+/dSvgy41J6hl+1Vj4g1NxfzW+L3CRnLKyZxXHP8Aeafvn0Mp1DP0+T/9qz5ulo7//bCePjMPDt+dL9INm3vS93XV/+ol2/fHqp3BhY9ThPrbM2fB48/rfT1M//0qOJScTweJA7PRC7NW9n8I0dTn+U9BLnXls31fCtLrL2fqj76cVp6+mPI+pvz8Prl7t7l3I6CS+mZ4nT6XgBXC2bb03x7WJXqT9ds71uCsCkNAbKwufh8qeXS1wVk2fPBxvTEez0ZOPl9/8CIu/Sgx8mAAA= -->
