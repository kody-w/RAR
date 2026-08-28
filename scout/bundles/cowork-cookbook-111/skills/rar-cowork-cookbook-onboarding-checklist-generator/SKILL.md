---
name: "rar-cowork-cookbook-onboarding-checklist-generator"
description: "Generates a role-tailored onboarding checklist as a Word document for a named new hire."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/onboarding_checklist_generator", "rar_sha256": "46a1641e2170cc807c00a02864c4111c7a49aaed168586e88aff8dd8a3a366e9", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/onboarding_checklist_generator`. The original RAPP
agent is preserved byte-for-byte in `onboarding_checklist_generator_agent.py` and in the RCI capsule.

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

Onboarding Checklist Generator — Generates a role-tailored onboarding checklist as a Word document for a named new hire.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/onboarding-checklist-generator
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `onboarding_checklist_generator_agent.py` and embedded as the fenced Python below (sha256 46a1641e2170cc80…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `onboarding_checklist_generator_agent.py` first:

```bash
python3 onboarding_checklist_generator_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 onboarding_checklist_generator_agent.py   # or on stdin
python3 onboarding_checklist_generator_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Onboarding Checklist Generator — Generates a role-tailored onboarding checklist as a Word document for a named new hire.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/onboarding-checklist-generator
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/onboarding_checklist_generator',
    "version": '2.0.1',
    "display_name": 'Onboarding Checklist Generator',
    "description": 'Generates a role-tailored onboarding checklist as a Word document for a named new hire.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'hire_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'onboarding-checklist-generator',
        "upstream_url": 'https://coworkcookbook.com/recipes/onboarding-checklist-generator',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '538f671449e451e0',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-23', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/recruit-and-onboard-talent'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/onboarding-checklist-generator', 'uses_skills': {'custom': [], 'ootb': ['Word', 'Email'], 'plugin': []}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'review', 'checks': ['Every finding cites a rule ID and an exact location.', "Coverage is stated as a fraction of the inventory, not as 'reviewed'.", 'Severity reflects consequence, and blocking items are listed first.', 'A clean result explicitly says what was checked and found compliant.'], 'confidence': 0.286, 'deliverable': 'A findings report: inventory, per-finding rule/location/severity/fix, coverage fraction, and a re-check delta.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'criteria': 'Optional. The standard to review against, if narrower than the default.', 'subject': 'What is being reviewed — a file path, URL, document or system.'}, 'refined_by': 'rules', 'signals': ['tag:audit'], 'steps': ['Establish the standard first. Name the specific rule set being applied and its version; a review with an unstated bar is an opinion.', 'Inventory the artifact. Enumerate every reviewable unit (page, slide, endpoint, control) so coverage is measurable rather than asserted.', 'Assess each unit against the standard, recording rule ID, location and observed value — never a bare verdict.', 'Classify severity by consequence, not by how easy the fix is. Blocking, major, minor.', 'Propose a concrete remediation per finding, with the corrected value where one exists.', 'Re-check remediated units and report the delta, so the fix is evidenced rather than claimed.'], 'subject_label': 'artifact under review', 'verb': 'Review'}


class OnboardingChecklistGenerator(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'OnboardingChecklistGenerator'
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
    print(OnboardingChecklistGenerator().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/7V6abPiSJLtX9Hc+ZBVw82LJLSRbW32hAAJgQCtSFSWZWnfdwkt9eq/vxBwb1ZNV/V0m80jFxCK8HA/7n7cI8SvL2bbBHn18uVFds0MYs0kCQO3gszMgZi8y6sYvOWxBf5Bdp41VWi1TV7VL68vjlvbVVg0YZ6B6aybuZXZuDVkQlWeuJ8bM0zyynWgPLNys3LCzIfswLXjJKwbyJzGXfLKgZzcblM3ayAvB8tCmZmCOZnbQUFYuW9gHbc30yJx65cvP/38+hKCzy9ffn2xE7MGX72cPqQz78KfqgCrXl8SM/PBqGIAVmbgunArsE4KvnJcD3pe/VC7ifcK/dd/xZ1Z+fWPX75m0PP19WX6I7UZ1AQu1ORm3QD1bLMwrTAJm+ENopPOHGqocpu2yiaragBS5r89Zn6XlBfQ36d7PzwWefPd5oevL3kxqQog/PryIwQA+PpStdPnt0lK8cOPb0neudUPP36XU7dW5NrNJAxo/fbtef0UCwZ+Hxp691X/DqQ+nGW5X19+Z9z0eug92QlmvrxFeZj98BBcVPnNzczMdn/48a/Efjj0X5L700Nw4JoOsOmp+I+vd5B/hmZPgz5k/vWyBXDrv2MJGP6+3Cv0BOqvZN/x/2+ikzADgf2O+J+K+7MJs79DP/2lbf9swivkfX1Zu0l4A9FhJe4X6Ndv8nnD/PTJ+f7lp59/A6L/RzFy3lb2XcK31MxCz62bb99++lTfv/7080+f2gLEmmum39oq+TOZf4brfZ0/IPgc9cMf54L11SzO8i6DPiId+jUv/qP67Q3SzCR0vn9ff4F+ny/TawZNRrwv+oDgdzlTA11/h+OPL78BfsiANa19vw2y/D//ExJCu8rr3Gsg2c7bBgIObsLUnZRXgrCGwN8ptysX4FqHANjnOBD/k4cnjXMP+uX/2Hc6/Gw/6XD+nde+u/Wb/849v7xBCpCaV6EfZmYCSfT5/DUz/YnpwIpF5dZudQNcYg2N+xmw0OfpAxRm0C//XPC3u4y3YvjlTtLhg5kkZjexUt0m7ttk2SVws6cdNuB1t3ftFohPchvo4oWATl+BxXWe3ACrTSjUcZgkkAM41waLDHfZAKkvk7BffvnFMuvga/ag0QX0IP56DgZ8qAN9/gyM8pLQD5qvmWsHOfTp198+Qf8X+mez7sKnNc6Azp9+ABry8ukIgby6VwbgIuBUQBp3P/z62xNaIAZAAgGvhV7oPiaDuIxd5x1nmaM/ozgBWS7AF2CbFnnVTHUobN6gnQd96AsWnW5N7B3koDo5buFmjpvZA5BqAnM+kMzyBqpB8NXe8Aq1tXtf9RerMu8qpsBhZvMLJDBnUCvyBPw3qXkfBCbnWQjg/4iCx/dASPWphlbvIt6g4xSJUGFWZhFU5nMNz3z4ZSqSz+lAuDlVyq/ZVBTdCap7WjzguQdMaD9d+nnyOajgKeAAp35f+xlUIAqVe2Wrvmb1M+TNanKFDUoAWNRvQ2cqBH97hlQd5G3i3PEDmk6Snl5wnl65x+D30gx91GboozhDX1sURjDo/1PjMClAs6y0YWlls4Y2R0UyHsBMbcw07dH5gBp+F3BPgu91/Z0V3snxa5aEwMvV8LfHyDuczzEPwmknlSVaussHvgTATHLvoTaFTlVNQWp+zd5Z+BUofaccgDbISxC3U7i8Lzjdfdc0AMk3XX+vyHfXAAyAM0E4QUVrJcDVnus6lmnHQKtqSpcnwiDu3Cl1uiC0gz9YBQHpwL1APgAbqAreuuwO3TEHZgLgvSpPvw8Ppz4HaOG0NtAW9InuG3QBET95vQZpBpqVaQxA4dNdFJS6AGOg4gfCdWAWD2Wm1vKpoDmRbwg89zv8n7e+R+hdk0l5INN0zAYg2U186bj9w68fWj49BYSmU07dJ/3R2U9Lod8Xi799ze4aflA0SNVkqrO/gwYCKZLWd26cmKYGbJG6z/ABcXAvqW+Pqvgoux+6fPmHbvqHf6/hvtc59Y9++wIFTVPUX+bzR216L01vIM/nIELCwq1/V6Y+f2TR549q8gepD5C+QP+eZn8Q8QzoLxDyBr/B061DaLtTxD5fAAjm88r4jE13v2aS+93DYPk8BQw2AT+AuvhRMN6HgKrhV64/DX4UkHqqOx0odXfGBD74mn1EwTNDACFn/lTt6vx3mXuvnMCnD5d9EDu4lTVgbWfqsfz77iOZ1K/dly9ZmySvLxPL/M+7jom7QZgCLKatCkgY0LE0oXu/AjaBG6E5ff7jFup0/2Amj3CuG6AkWONeQx7pYfr3GvE6tasZIJRpazAVqAeZgw2N2SbNpHQzFJOWj53I1BV9tEz/uOo9f8EaTv5lSuNXaGpvX78z7iv0vne4b8ayFmyefpq65MlOMBS8fYz92BVa7svPf6LGs2n+CyXCiUIm0nmY6zrf+eHutMJsAA2q0uH1O/eD1KuHe9n8R7PBgpVbtqAaOJPK3zH4rlr+0Oe3uynNY2f468s7wzyd9+wCwXCQyp/rqQLOQXiDBcH1IxDBvX+zP3zOBnwIOhQwHSNMhMAQF0VI2LYpmLRh2IRRisBsDEEQmzSxpWm6DkJQOEW4FGV6HuU4lLkwFwThLoG8RzB/m4p8OGnkwp67WCKo7SwIFMexJUKi5tIxMdI0HZiiSJj0HFAyvk+NAZ0+zXyYNWH40apOcDyt/fXFIjAwksPqHf14MfOlZhKLg9UH+mwkPCOPljtelvITaVpwomZ1uceyOLajWQfHyAYbaN6I03ZFH3aHlDWQtE7WOJ2N/Hlx0jM6OsjOkRoElzf3XYt656VS6wIdMrDj4DrHaEM2HsfIDlubiKvGH2Pxti3hfa8vSAL1qOR4Ogrba2poWp8G0q7YL6u1rJ8MmMRvDH4Zmk1UVrYPpu6SMdvP+mtik8eA3QfsSUq9c5Yg7nndkJ63wdtF1M9uezI+LFyGN1RXvXDuFmmY8FLdlMS1TCll5CV+WB+JoKJKa48fdDlbNcRR6POymksn0pbVEbMcX8QR9ehtSVe/FgMn8KHYXy+GXruizshxLNsHJWm1jtfVxYratkHD9EMS6PxRxXVJF5xKz2dHpL8Rp6W8vSy34+24ERhVjot5RojRmRhDhdFqPrYNqhWv55ynzdG9bg9J2BtVe1TWxtKV/LwcF1JQHFa8TjZ2GdWSyOH5idD2ldVc47BcnfAz0UmU5cvwQJIOtSuLU2PX2yTt8xEWPbTb1SZKW81RypFwiZl6UmzXehBdjEs1aPVW4/C5RJHXLmjkThyHNasiZA+LGDEi535syh6zievKlxfqoUPkZoYpEWE3tcnAt4sSu6xQwRnX367XPj0ZjaNyJaaYZrIbyTq8HZ1avcxYaqUbN7O4iOnIoUPW1+w27Shqt3MTTEVGbmbgR91vvZo1CRHmieB07Bk8MYYq2GgzX4RvswTsbjaopullrw9uujvxp95Oe904eTiTwGcB1dPr8SaMl3MTEtIemW3bYUE5lwTj+0XnEtyS4snLOZH5fG/Dc3S9qfFMIWfW2VZCYruHnVrX+utVjwN5dp2zLqEqfN3w423QQ4JUZXOZ26x3zuvjuA5IVpDhbJFTFnoI9vLanutivAySDUHHURDLaV1c1tE5xIricFK1KsaSYY8EnUhjRyMPObyQ+g15HY1ww6wVuD3pK9+/7JOZLtTrE9cLnFoF59TgdCq19P3It4mBlbmg6mrKHuooqpNNrnLq6bicj4PW1iN2vh1iErYkvJC7MhPV+bCyl5Zz3RL7g1fUyswTNB1t7VuQR0XaGnY/L3Zly888Vo3co0nDMhL5NMnopCIsRjsJtCWWqeUoeuF+X+7lXbzPZiE/MkkpyXnQektyrahY28YuVgcbCacoLxB5zSD0qIA3s6W7RYsjnSnCsR3nl2xDl2UpdmJ9hO1Q2xKNq80OG5YZc3mm1QDf2Cgkka6UbjVvziO2Pg8FlwmNOtRu57QEMr8OnRWKc3Pdzak88dY14bvYcdvbiVgJS/2kMNgu42PFp3aksa1EcWMhVOHkWE/DY9jv/LXtdoBzzGsreoedBmtuyHSCeE4PzsowF17PhO4NMZH0cK2cjIrNS0wxu7HHFPKG06fsZO1HLUiaGy3wLeZSABkHudSEM9oUFy0ITGrmnGe4vEPwnn8KFyp8zc0UdW8bzE3FJZXimLnTVPUwKOMSFeYX0s/6cI3vtaAN4x5bZRk+GwunG/T0HBzDRsEGxDvrYHZ5Y3HEVbzLdZvNOpVaW+qZ2sjRmKwsSXDm9EqYXaR6uB14aT1w/MZlHaIzFW+HN1RJNKw+mtKCk+JjwVdHOc/zYlDwINFsrOZ2zN5vbqkpX2F5xbVXQy/6YKFUKhtH+YI/nlcl6a5Kr8FGQhlPYRac6pqYexw+o9yDtrpuN5R2zBktW8z7RssTrncAuhZN5Ry3KTZZ1S4x53bk11WTno1zxIjBOBL48axh5Nzx5lFHzg5BPr8xJywnt2uRNmFiVmL9geZdX+oK3z4L25EUfYeXq0Qdy+pYnreYI6YZFwunZbexwrDh9Fvnnq831R1X+FyMUsSJ9U0Ul6t1E4u0XJ2dbkYJ1LqOZodLp/i+V5r7fMn7A11yRMUU6bq56JmKqkeDrHNlpTZmn9qH9srAenyiKhivAiS1w/X5wMn4illoLXLY9E2TpDHTuIrWTycPM5cTA0w98nJQoZfLxhEWWCeh+8M1inuClmBVY5E4J5YHlBkD91rrCFs15iLGl3WcCFKew862U26KwS28XBBztd/n9j7V2ypCdGqreryPlXtP3mjtBvFV5BbME/8AeiI6Y/a2JxK8SYrNfs8PTGQ028i0MNbh6GvOJ1gqMrKIs3RUcGpJd8wQLdLD+WJb1fkYY+6NyWl/5eU+UaD7er8NI2OxtQ/23CjFq8+pS/fWnvGygbnGD2sM82n9tMlTG+Ed9Hy1apfWEIXuNSI6yW5yuoZFtLkxtyuCIRJDXtuzciFAVu+QJY8mZb33Dd3SQ+Sw3ff2ujYjdQUbNmaCoETM0I0EMm4Y5NIXcyWPeELoD80mWekkEyEq36wST9vQdUioYrBt99tk3dD2RbGGzKgvoXwy5MBNNiHaIUdJvzYCx8UL4zY3hWbnIvRWbefrwLaMNdK4xE0a1sVZk9c7w9ujB6mBL4iZtCF5iNaFWTfMYj4WJCkBewijSFNWPC13Utsa/NhwFbN3nSacu9gsyBD4QmSzBSjCpYSrMb6QSDgQ++VO7zZbGz00+TFdcZJP2yILWs1CIFUxyc1+hVyo0+5Kr2NPKnFbx5ciaLISRuMaFdBmuTJj3jGa1baL6LOkpU0hX6rGSMOamjd93F1nO0cZqpJSF7Ca5/sxYc29Gqz3JZ8XJbFTShCTFFwQxgWLQUMlqjnJh9cimgnrnUSFSrLCN52kIue2FQqOnkubE1uouXPhlQ7eCnCnhetlLwlEmyujmurBhkl5CV/d3IgNCJw7+uco3VryTnBl77Rk5oYD2veQGY+Yz2iVOgR1fbWjLY3UmGdqBbvXHc64eed1YcB5uSuPp5BktkcuS7cXk2X8UJE076SW4VUb/MJuMS2Y9+X1it7wQ10cMqNcrssRbnijM3Y9FppVu2Jv+516w+ukLCOQEMJuZs16fh+BeL2kgVE4Y3virdVywFjLUdSgmVtKXmdNRvvnxbDdpnQfOW0hcLrGNJo6XPVws97MBAKuNLpjJb0fQaB1eNpio92xyAaheomHe8nCEn9skZQvHapg4MX1iDue0tSntcvGoFqmx2D00kRkF/Jm0Q8WcDMuYISSsLfeJK5bejtaSGz42CUqvCCke+Sw6sUBzhJdlZf5oeuZQR34605yLJDrvt0tR190KnixB+20szu5ZbjPF2Fuz7yhY2OZ3VF0XaWHyAPU2TVoVApla+xX4sKURHTPMMxVQLZpWWT72jeQWq13VhH3GXWgCpXJGwaVrfICL8PZsJH8I8/PCFRmQsRWc7YMmtvOZDr1KLqpFdEcvEqGQEc3qXfN8jKtbvOBy29iNlqBdZOkfr/Gt8F+jmtJQ9nuSUiGtqsdkMNGNIbxeVip4Yg56O1EcUd5s8pSdM9JkaLF8I6xfbUu7RblN/aMbxjs6mysC7bLSWezkW+1sd6uVqqAI9J10bMOT8O15SDHqqwrQQ4um7KvLk53pU0zB/BsQ0vYLgn5fIKpIwqDPeseHYQTteSkQ34FW8krUsl07FmCz4l5g8rbqwT6LS/fGJciI/sLxtcXflu0Qd1E6HFm8PiltC7HeiVHwty0jSwerapNRHMlsMka1VZKK495vVjUbKXMRUw20CCVVU9xQufoIGd4xpCXvjwveJew9KRa2ETIUgd5fub9zLk4jjZfbHFvFVuEAZ+OwZXFsRGl40wl88URjS57cy5f9jCokmgajK3YnFg1kVBruVpj12bAZ95MGNakhy4OtM+WyjnHHetCW1tC3/qlFahEOaM8Ki1FptLVvMdpTSQPdpLLgtBoWXRat3Meq+3W49CQ4+yGqZENgbCiKtwIfqAsBcX7m8XLjn9Yty3sydSctRJzjrtgC7w7h5Ut8KROUvC8h7ENcx0lvdPmN3jnFetQEg29a5aNVCrifrHtVde9eXKzkVeWMwo8oRz4VaDOJdNTZkmDCKK8JrdLuthlV0ArJzrjs1aPC84WqMvqdPBxIaJ7qVwObeQbZ7cPFxup88mTNGScawjE6hgdY80A2845I9zQHVo0e4olDgS1tJDtrF767okqqZ0twMzythG5FGVRfad4icvP0hqkzoAToDUjUk9vV71MOYeVs3YcFoWR8wU9BaK9kOcjSOp+WXFhwIZkvG8EbJuKuwo2LMtbhc564WRLTlGl5VlunFi6suIikDU7FYLGOg31bY1r5XIRKyeujKIoQK8I5brUjWsZY6dwTayEM4b3WkM3YaZPMT9WNvJSlU89d4CzVrh5IrUHQYyyXDUcU3GhnTuiDfh9t52xbUjBPIVpyg4WTBZs5jte2ZWsLmuGQvbnbLMOz9dDoVE8v99uvHJ5vhGLCubW1K5rVlTe2mI+0tbyqIDOYR0w1T4TF73jYwbD4c5KW5/njn8+8KYWce0ZAb5OGLhbjFZTon2/sHRrk7RwamcF4Ptj6nT64erYVbq2g9VoinK7dec0t7nxhcmRUVUSMzl1UNKudH9ny9fbqm/sJbZHYowdAt+ilpIuYSe6PLFzz+ObYtjv+8u6wWnuvMKOYWxZe4vG0VlLLYcSB21NE+l5zgajPwrdcauNS9bq5WNL+pu83cs3ulmT2PYauvR6a8x9NnPCeKfzg3Ar6Hw1lESULp0MNA3kIljdMBpBSW+34TofPS+dWXjAk2ixtAkHn/eVHVnden6jqFMoUtjaza7Bgk+voGWb7cNLqjWompZg+3+AlTo5DXypVqTjL2f40na6kF1W6Aa1cXOG1issOviRstssMCZGwhq1R30hYWagczLPqgR5FU2u6JrUAxy+9tXkRNwOodRTDr+RyvWlrVr2FMHVsZZ6YSx7wySstN9Vl20WSxLXGKtMqkzEP+frZQlK+JAbbqquKsKgbtlli9uzxcKMEgIjlwZiH2hjGxLz/FYDKLYlw0ndDBTqdhBjL89cyvbpOqXHYMjVtJOGebQpNbCbXewvOYvbvZSWim+gmVXOxbzwnMtBdZLWPLMX8eI1yFna3kIyR/b0MOdPoHu0JLDJPDZJx8nU2bjgeNMZx7lBtIudxW9W02ZiFAtvazjJSfWQTV6eyaOAp+g410J/nTnOaVX63HWs2RFZyVc2ro1sdRphRwK7cExWXUnEczy7ierYcqfWDtaEmSLNydIGJzpjBy7q1Ate5zRN//3l9WU67nyeNP+LD4OnM7z/taPEx6nf+7Om+3Gvazpf7mt9+VcV+vn1pbJDoM7jqLROWv95tPjfDko///MnFNPc4fFsdXoc1jfvR/GgR5l+E/QSZk5bN9Xwrc6T9n5Q+/pitfX0C4V6+hGLDd5f7galxXRCbbZOOL1Pjwm/Nfm3ym3Ap5fppwPT4x3XCc3m/dJ/nhi/vjgDcEho198WBP7NrYrJvufDDmAW+ga/IS+//T+ddHkcTyUAAA== -->
