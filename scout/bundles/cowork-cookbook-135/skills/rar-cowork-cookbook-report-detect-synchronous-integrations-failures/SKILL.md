---
name: "rar-cowork-cookbook-report-detect-synchronous-integrations-failures"
description: "Builds a structured summary report of detect synchronous integrations failures activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_detect_synchronous_integrations_failures", "rar_sha256": "19a4cd17a8e9700ac7bd25e774c30301eac94dcb7d4c095a6de5378e327ab13e", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_detect_synchronous_integrations_failures`. The original RAPP
agent is preserved byte-for-byte in `report_detect_synchronous_integrations_failures_agent.py` and in the RCI capsule.

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

Detect synchronous integrations failures Summary Report — Builds a structured summary report of detect synchronous integrations failures activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-detect-synchronous-integrations-failures
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_detect_synchronous_integrations_failures_agent.py` and embedded as the fenced Python below (sha256 19a4cd17a8e9700a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_detect_synchronous_integrations_failures_agent.py` first:

```bash
python3 report_detect_synchronous_integrations_failures_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_detect_synchronous_integrations_failures_agent.py   # or on stdin
python3 report_detect_synchronous_integrations_failures_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Detect synchronous integrations failures Summary Report — Builds a structured summary report of detect synchronous integrations failures activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-detect-synchronous-integrations-failures
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_detect_synchronous_integrations_failures',
    "version": '2.0.1',
    "display_name": 'Detect synchronous integrations failures Summary Report',
    "description": 'Builds a structured summary report of detect synchronous integrations failures activity with totals, trends, and breakdowns.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-detect-synchronous-integrations-failures',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-detect-synchronous-integrations-failures',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '93276d22e7a4ab66',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/monitor-systems-environments-and-capacity/detect-synchronous-integrations-failures'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/report-detect-synchronous-integrations-failures', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ReportDetectSynchronousIntegrationsFailures(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportDetectSynchronousIntegrationsFailures'
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
    print(ReportDetectSynchronousIntegrationsFailures().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8V6abOiWJfuX7FPf8isJvPIqJBvvBFXEAVEBhFQKyuyGDaDjDKIULf++92o52RWd1V3V98bcc046cBmzet51t7624vTNlFRvXx5MYCTT9ZOmsYRqCZO7k+4oiuqBD4ViQv/Jl6RN1Xstk1R1S+fXnxQe1VcNnGRw9vZNk79euJM6qZqvaatgD+p2yxzqn5SgbKomkkRTHzQAK+Z1H3uRVWRF209ifMGhJUziqkngROn8FYox2via9z0ky5uoklTNE5af5o0Fch9+Dxa51bASfyiy+tXaAy4OVmZgvrly8+/fHqJ4euXL7+9eKlTw49edncDlnflxnfd4g+qV0/NUFbq5CG8qexhZHL4vgRVUFQZ/MgHweT57mMN0uDT5N/+LemcKqx/+vI1nzwfX1/Gf7s2nzQRgLY7dQOD4Tml48Yp9Ol1skg7p69hXGCc8mfQ4jx8fdz5XVJRTv45Xvv4UPIagubj15cCmnA3+uvLT5Oigvqqdnz9OkopP/70mhYdqD7+9F1O3brnMe5QGLT69dvz/VMsXPh9aRzctf4TSn0k2AVfX35wbnw87B79hHe+vJ6LOP/4EFxWxRXkTu6Bjz/9lVgvAl6SxnXz35L780NwBBwf+vQ0/KdP9yD/MkGeDr3L/Gu1JUzr3/EELn9T92nyDNRfyb7H/9+JTuMc1vFbxP9U3J/dgPxz8vNf+vaf3fBpEnx9WYI0vsLqcFPwZfLbN0PjuZ8/+N8//PDL71D0fynGKNrKu0v4ljl5HIC6+fbt5w/1/eMPv/z8oS1hrQEn+9ZW6Z/J/LO43vX8IYLPVR//eC/Ub+ZJDjt78l7pk9+K8l+q318nlpPG/vfP6y+TH/tlfCCT0Yk3pY8Q/NAzNbT1hzj+9PI7hIv8AVrjZdjl//qvk23sVUVdBM3E8Iq2mcAEN3EGRuP3UQxBq773dgVgXOsYBva5Dtb/mOHRYoh2v/4v7w6hn70nhE4fSPjtAYPffoDBbz/C4Lc3GPz1dbKHaooqDuPcSSe7haZ9zZ0Q5M1oQgmXgOoKwcXtG/AZwtLn8QWE1Mmvf1PTt7vQ17L/9Q6u8QO7dpw44lbdpuB19N2OQP701INsAW7Aa6G+tPCgcUEM8fcTjEldpFeIe2Oc6iRO04kfV9CIAjLBKBvG8sso7Ndff3WdOvqaP4CWmDzopJ7CBe/mTD5/hl4GaRxGzdcceFEx+fDb7x8m/3vyn911Fz7q0CD+PzMFLZQMVZnAzmszuGxkHgjMjn/P1G+/P2MNxeSQ/2Be4yAGj5th5SbAfwu8ISw+49Rs4gIYcBjsbAw0RO9J3LxOxGDybu+T90Z8j4q6geRXQvoCuddDqQ505z2SeQE5EWakDvpPk7YGd62/upVzNzGDEOA0v062nAbZpEjhf6OZ90Xw5iKPYfjfy+LxORRSfagn7JuI14ky1uqkdCqnjCrnqSNwHnmBLPJ2OxTuTHLQfc1HFgVjqO618ggPXAQj4z1T+nnMOZwLIM1DXn7TfV/jjJy3v3Nf9TWvn03hVGMqPEgSUGnYxv5IFf94llQdFW3q3+MHLR0lPbPgP7Nyr8Hlf3eEMJ7Tx4P8J19bHMXIyf/POWU0f7Fe7/j1Ys8vJ7yy3x0fYR1HqzH8j2lslAdr69FC3+eGN9R5A9+veRrDGqn6fzxW3pPxXPODd7vF7i4fVgIM6yj3Xqhj4VXVWOLO1/wN5aHJkzukwVzBroZVPxbbm8Lx6pulEWzd8f13xr8ntvJHp2ExTsrWTWGhBAD4ruMl0KpqbLZnGmDVgjHQXRR70R+8mkDpMBdQ/gQaEcP2gbG7h04poJuwz4KqyL4vj8c5Clrhtx60Fs6u4HViw34Za6aGTQqHoXENjMKHu6hJBmCMoYnvEa4jp3wYM467TwOdZy5+jP/z0vf6vlsyGg9lOr7TwEh2I/z64PbI67uVz0xBU7OxI+83/THZT08nP5LRP77mdwvfER82ejry+A+hmcAGy+p7qY04VUOsycCzfGAd3Cn79cG6D1p/t+XLf5jwP/69TcCdR80/5u3LJGqasv4ynT647436XiFKQPrz4hLUTxr8/Oiyzz902ecfu+zzW5f9Qc0jal8mf8/UP4h4VviXCfaKvqLjJTn2wFjCzweMDPeZPX4mx6tf8x34nnKovsigfWMmesi77/zztgSSUFiBcFz84KN6pLEOMucdgGFSvubvZfFsGYjveTiSZ1380Mp3IoZJfuTwnSfgpbyBuv1xqAvBuPtJR/Nr8PIlb9P000vuZOBv73pGZoBlDEMz7pxgQ8GJqYnB/Z3T+vEYn/H1H7d96v2Fk449V4wsO9LAO9jeffEraOjYpGE8ksGnCbQ/hGA5uteNjTqOEi50t4Y4DPzRn6YvRwceu6JxQnsf3/6jBfdehyDlF1/Glv80GUftT5P3qfnT5G0fc98n5i3cyP08Tuyjz3ApfHpf+76rdcHLL39ixnOA/2sjnjj0QH7HHVltdPFPfILSKnBpIY36oz3fHfyut3go+/1uZ/PYgv728gY1zyw9x024HPb053ok0iksa6gQvn8UILz2fzuIPsVBpISTD5SHMQ7p+djcoQEzR1HHm7s+ToH5nPQIlEAx4HgM6Xvu3Cc9lKGcmQ8oYk4DAp87LkYAKO9R1d/G4SEeTQRoAAgGwz2fmOEURTLYHHcY3yHnjuOjND1H54EPyeT7rQkE2qffDz/HoL7PxPe6fbj/24s7I+FKgazFxePBTRnLmeGkq9xcpJoF4T6fiu4F22X5bl/JEsAE23PFBb4EQ71KzMt+k5yMTGTWyVxc+43ToYsAxvEoMflVEMS2PccHuShXiznAo3YfkW5KU0Pt7SweBZviklouVx0b1DGxyIl91HSyVXoy8WinDJdAczax184aa4NXJmnN7FsanJsUm66w+UHd9iDxJLtBu2q/bQVOUds8c3NRy3Uhs9yZkfqV5+BV6URb6aAQEneBO4Z+ejqtpcw69NuzdoiOtRBSWj7QUy0vEVrL68uQzhDtSkerC3IwLvq6LppNL5fOOrkaVO1snEvmG2uzPA2X/DSNzONB8vV8m1qk4g19jwatmA+53WZxxhQUHuSyQl70JrWdvj1e13GYsZWyw8Ja2qzyuDnoFnYrnWG5MK0WTdq6Svq5cERxEM9Sm5FzFNak5YWxtWd9J7ut2ds8BHtC9o0qMzJzyCyKk9CziGv9arPTT4hwKVHksAa6nnQd0GWHW1TXZdUWS+kQXbwKi8V2b1fuWVK5jDkljFkyq+5yweXb1JLsrjl1AzqkVFllpBYtV/HO5ipXYS9YRFgb+xApZxlLsDUYgmZImEMfH/epe4xSM8yN1fZUbYwQvx6v27N5DvzzBcO6pbXzumAJNqerugTB0mnpOr4U+YI5beX6vJ5rNZ0OKtm4qnCRdr56nFUHFhz28aAYhVWEPqO41naVdemtOyB4nAz8BayXeVQOqqdMyZblelOkb7ejg2WqhGOaSFiuNqvLo9/FpylToRiv15dZiSZTnqSOVmmzID+drbWmRkbrrrTLSdBKjL/mqMsEbIEh/j647ZpaPFMq6s54fovu6UNOi8JskdgMeokjpxuYI3XYo4yOnOVhQaor4BfzNWabPEbXrDMoLldaziHd1YR521D2KsaKbSIh9HUl7dkwtle1UZPHZsvrZqz4fbaJFotKZZYb+5yoCOPMlj155RaC11mr/VFttnpDsrJIL4HIZ86BRw3PuLUsYYj9xpKjVYLyp7V12qex7x1J77BPbl1LmVHoB+3BV9YVvRL6PVDoRPPpJIB/ZxtZ69as2xQpzckNQpwHreGaoTVnzvRA5kYFeXfpz3C1msZ+qxhnMjZOrRbTaRYY5mF5uQZLkT8p3uy2LwfJYaQacMa6Zgq2lDB5sa7LoNkOUzm5bKaVzLaqWHg3u20WqiGxpnTmU7bXFZTPGyOzZ8yQefmSyhwiWpc9RTEa3Eu4cuqxlWmcV9Mj6J1l4xDWRcNxrDDWnGNZ+Y2kNHCRr1yS2UsLx6rlpUguVRvRKOOsJNBDNWpUgGBn3YyIpFJUvVolT9plTkYH18Clm4lEKGecdvXJhK1kJcsL3ihsW3fxmhIq7nL0ea6W7IQ/tHPWX+OISfhRrCTLQ0mZtMdb8+zMbbb10hlAOl+JbkLKszW9H44BmxEtOU0re9ae3XrQ9sQ+W7r2zttqPjDx1uUPEH8ybLDzWO054jqLb3tEhggnVFq0ERi6nF27y5SfHoh54yzXR/c6vRiep9yofjDFawa8kxpTROvlF95RJdpTMyZdHM423wtbZOc1OL9sIcTJldDpOGnttL133DEAl7GB31cbd7u9mcfMkIL9jZN1rlyaq+2xRUVuqoMFFizWq3hbLW8LUhLNC1l5kqkAG6GOHNAqY8suu3x1NBenuNRBtG0NB1ACGmqCtIgTK1xhWcttTzzAXNJrzgOlS9wsyufoQnBWoXC6XTxXi+aad966KJYLxLwjtUNDef4xTJgtOZtWhGGYp9S9scHmhktqL233FdpKSTBFuoWbe8wNpzgWPYjEjWSmmnRjrlyEpBIi2kATSH/BHdt4VTQUZRIrUReSMELLmyMoW0Zf73TuQhGqj52zhTvfyE2V8rZNcnKxsvkpb5xY73yZF3HZOwkwGS/296aywVZUtNaBuRfn0jqIEzY+wy1fIpbraNqe+6JzCGmKU6nEtIcphCtz40VazxvbSukkx5nBJm3PMsfylNhu3EUTCALVk+b0OGWtwbAkISpXSN1lHCafM6zNK5vKk/LSm8rcD6iC4vkkwuq5QWF5ub25hVcS68bWZ5R8DKNhaKL1aQBlXxHUOgF0u8M2ZSvXKyGsdCDA/JkXOWfQKA/mc0CJV17lpYoAVIvst0fbLHQkSUUEEu1Omx9iPA3USxz4WqsmC2pW6YvN4F2z2SXJOE3cBHHmOu36YopmQzPXDW4ddmovLNZBVonUheGNsKDtiKXU/aFjbx6Nieas1a+rFe2r5na3TKpkNRUjcu3vzOuOo6qWO4shWW+d9FJ6xNKJZ5XasMI5ijPlZpobQryoekwfQRNUpZeWHJnzt/DE8uUWpjny5aHZ17GIqNLWznWEUqn+1F54E6ma3fFWGGlPLXf2tLmZQ22j2H5wO6MWkOqCgR2nyP5xyS3QRXY9Bbriy4xwLHZgG0zpLJr5qKSyes5ZaRDaUztr0S2PbOlluMWvu2G+SOZk1HaOvqr5QdnpIlfVwm1JDRuKWOjGVtpx01ggrGG2w5Q4K9brUJg3y8qxyOpc2Z23FIbeWtgVS1mE3DIHCZTqrI1vQxuj4ZIgpgOlHUh/w4aGvyQTwcszcq5sjuK5wFpkdj6Y9dS2tcoqvdwukPoGBuGmNmmIUziwZ8t8V/SLm0zUbuzx4t43Q5mDw9uqJU+YcQjduY7r2W0vmj0R6we5m6kzCzhx2KzX66VJzUtzduz3gVH0qYe1/o5GUFgSB3XFbunyauplBWeP1GzUzWW+NTpLMTzytI0ua2vRqcfYkndzr7IM1aDmfW0NaifU/G5w9StNGuemdOMccXS+kfwkrC5sQrKHvMa7o1gW+HatGPvNgdWI8rqlY5ZmQKJbe/VgmopYq60p8fa1SZt4HXomoc9Fat036+HELvL2BAdSVj45yLG4hgjnqb7YwjEx2BfDHuXX3tyOdI+xXT0bdD4iJKvLBk+O9G59EHIzTSAcaESnIiR3MqmDJjqG6mgN7m69KF7WpSQIEoz6YnVYhQnJMVZZZ6Xgo0v+Mu+Yw0DM1ls0pInblV0bq7arVtluUxa+2XfnRFzbs3U3ED2r36JbfVjNFt6B3lorRJoJPWqvQ6NNBLhPcxdS13MIGgfeTV+TeXxrN7xebTK9vSk5m2dnyyYVkZWzKvfNjUCzJ3zWOQJlsEGi5PQOjm8qjnOrKbKYl2R4LEE0rBTR0NfNLvEWh5Mr4Cu82zScbsvIKcEhdJvYccHsSiw91SXGXhrz4iAKb+R2oK2J4RCh+rWIrYXLO7Run8O5qCfbmzY7OwMnkJrraIgp3lQhV4KjKmSDKNuhvfHag4Sgq8Uy2SZH2Bt4MU8ZYodftjhPxEt0Xl4UYSe6Z66/VMSVEVc+6iS7UkrkSOrOlrW8cWwfzJVdpuqnmnSTmR61ygZBjIKQZztV1mfTxG8Zt9gut0uCQUOAbhzDqUTxQK/QzJVW6BmFIBjSbOKL5xOrz7ijJHg3lHZbdLUVjuczKPjt5SjPHUStraBvBnS3LlcDChhj0C+i2m4Lq+dROOCyC0ZbF3LUIxIqH5rY9S87uiMsooa8jxiMcz3S3NYU9Hm7IWxiTdpdq+8qZsghC81mLQLHJJk4CdKtrZieLJvSwdmre6h9PeoVpyHWFCpSe8kRIVEq6pmk8BO9TEMl3xAzrF6oblPLwSB0drh3cjQ96be6ODCwvNGN1J44izAETFBJjWm2+9DYG2lIO5fCujEHTTsWmCjQV1B53LScS8q8oc0NidAVGVxqrJOdOeiv17bkmm1AhFuFEiG7+hmyotVFiCKyHwQ0rwEeA3wy7YQpbWoDHB54UqI0t1/H+GaG8qznneTGcXp/x61aOzTQDTgQHBy6L0F0RZcHFI9lfjWVrtzxGPpb9aotjmhHh3S5uOwj3b+1e41u2e5IZQCh7L2w893IlvaIIrBYvVXcVd0Poj+wHjbvz6s2wSUkkuBMR9DXsxyl/LXMOITL/Y5ohiu5cwE9P1Pl6qy5exXVSXl+rTa3Xauos0ERj3Vc07d1qzDY1XPBhu3Rg9G7xszx8662o2ljF3McQ+1mmp6nyFrj68tepkLlyF5kUTgPjHyuvKbEA2LY7nWvzbDp8Rh3oYqTxVBPLYzWJBSbRcihVTlxPdVVcgbH9ARc6SbHOSdeLKfYpYczq9BlRN2dRZu6ifnRuB7CrXhxloBypk5TDJwSDlBK2WJnj09NxTsfbnxq9z6/6Bo8EcSdcUThTvCmAmaBbJPpttrYyAYhkY6jqJmhFAzgLV4qCmpasTQNtLA7Z9qUnQnYfqkQ8woAZhVvHJHuLFJEB8KauaS8sody26DqigF0bq0UurmmcqbRmZpkJQ38A1lRw1zL2/Mp3uAD3L8APM0k+rR3AqZYD0GE3DrpVMfXpXPa5ZGy9VEFo9fZ3iYJLCTmmHjUKYS9OKgY9mw4J5ay3YTbaa6VtXy6CSWDyv6cLDJZBzOq7Des38j7awGaG64704awDGqLYsTRPZW7oxMRkJw6Zu2eTfbKTgEPdGWB7lNmQQpAzb18F+50rT5O1xjqNbyoLrvgCqvHN+d4aHU9609rWHC8xqlEG+xE9VopNc0cmHJF2ME8GIb8oEDOvK1206jIdvnMdTPeRXMy8M6B2KKIh9pBmCGbZl2ivuko2B5ZtInUoIgbFFPkhjOnm3Ltr4XmAg5jClIsSNY6cxeR3c+ykzNDwu7qVUziWnK2Qf0tERSnQxcYB0RZ6goLt/SKsl/th6m/OZ6L2W1ZupLPNGSYI67ltThn08oMuE1fCPaNzwRIpVOdbFRvSWq0Lx2jwUNxr/VApJ3SyyzDlnLZzHBIs3g7I2d+lDlF2yni0N56uKHbBccOEZZXIDvZdYGAoD0tcI7doEbI4TiLu/TJhNspTGqkYef4uNHul3J/dZdeRhjX8tA4PdPDTlyeh9k6JTZ+wsKBPuPbRR84Hj/F7bzfH3HkoPv73I/ca9lyc5nOLwQXiUrjcV3LoZuDksmrysinx2RdTGMMpuGgEbYue9MqFQUO7g9EdA66laQ7TpWgIq6msjZdHARLPBi7jXdrkI2qxceeIpYtn7d+o5xz3BHCKc2RmYvMVxCBFot/vnx6GQ+hn0fJ/9Nvk8fDuv9nZ4aP4723r5vup7jA8b/cdX35H1v4y6eXyotH++6npnXahs9DxX93Zvr5b35rMQrrH1/fjt+Z3Zq34/nGCcffKb3Eud/WTdV/q4u0vR/ifnpx23r8mUQ9/pLGg88vd5ezcjyafuiHLxw/i/P7Yfq3pvj2ODoej1RHM6oM+PH3t0+rxoPtHuYy9upvxIz6BqpydPz5RQj0F39FX7GX3/8P8ZBlXBAmAAA= -->
