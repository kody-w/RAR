---
name: "rar-cowork-cookbook-teams-update-allocate-headcount-to-business-units"
description: "Drafts a Teams channel post on allocate headcount to business units status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_allocate_headcount_to_business_units", "rar_sha256": "9d58024b8c3edba7e7dfd1995f6efe6810efc6a28e7979711d90f5c303920783", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_allocate_headcount_to_business_units`. The original RAPP
agent is preserved byte-for-byte in `teams_update_allocate_headcount_to_business_units_agent.py` and in the RCI capsule.

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

Allocate headcount to business units Teams Channel Update — Drafts a Teams channel post on allocate headcount to business units status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-allocate-headcount-to-business-units
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_allocate_headcount_to_business_units_agent.py` and embedded as the fenced Python below (sha256 9d58024b8c3edba7…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_allocate_headcount_to_business_units_agent.py` first:

```bash
python3 teams_update_allocate_headcount_to_business_units_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_allocate_headcount_to_business_units_agent.py   # or on stdin
python3 teams_update_allocate_headcount_to_business_units_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Allocate headcount to business units Teams Channel Update — Drafts a Teams channel post on allocate headcount to business units status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-allocate-headcount-to-business-units
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_allocate_headcount_to_business_units',
    "version": '2.0.0',
    "display_name": 'Allocate headcount to business units Teams Channel Update',
    "description": 'Drafts a Teams channel post on allocate headcount to business units status with an interactive Adaptive Card for quick triage.',
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
        "upstream_slug": 'teams-update-allocate-headcount-to-business-units',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-allocate-headcount-to-business-units',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'adb9027c266c675c',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/conduct-financial-planning/allocate-headcount-to-business-units'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/teams-update-allocate-headcount-to-business-units', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class TeamsUpdateAllocateHeadcountToBusinessUnits(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateAllocateHeadcountToBusinessUnits'
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
    print(TeamsUpdateAllocateHeadcountToBusinessUnits().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8V6aZPiyJLtX9HL+VDVo6oE7aiuXbMBBFoASaCdrrZq7RJa0YKWfv3fXwjIrOrpe+dNz4zZkJWWSIrwcD/uftwjVL+92G0TFdXLlxfFt3OItdM0jvwKsnMPWhddUSXgT5E44Bdyi7ypYqdtiqp++fTi+bVbxWUTFzmYzlR20NSQDam+ndWQG9l57qdQWdQNVOQQkFu4duNDkW97btHmDdQUkNPWce7XNdTmMZhcN3bT1lAXNxFQAIrzxq9st4lvPrT07PL+ZW1XHhQUFXRtYzeBgEJ26L8CdfzezsrUr1++/PzLp5cYfH/58tuLm9o1uPVy10orPaDC8qkK96aJWqyeemiTGkBWauchmFQOAJscXJd+BZbMwC3PD6Dn1cfaT4NP0L/+a9LZVVj/9OVrDj0/X1+mn1ObQ03kA0PtuvE9yLVL24nTuBleoWXa2UMNVX7TVvkEWw0sycPXx8zvkooS+vv07ONjkdfQbz5+fSmACvYE/NeXnyCAxdeXqp2+v05Syo8/vaZF51cff/oup26di+82kzCg9eu35/VTLBj4fWgc3Ff9O5D6cLHjf335wbjp89B7shPMfHm9FHH+8SG4rIqbn9u563/86Z+JdSPfTdK4bv5Tcn9+CJ4CB9j0VPynT3eQf4Hgp0HvMv/5siVw61+xBAx/W+4T9ATqn8m+4//vRKdTTL0j/g/F/aMJ8N+hn/+pbf/RhE9Q8PWF8VOQJpXtpP4X6LdvirxZ//zB+37zwy+/A9H/XzFK0VbuXcK3zM7jwK+bb99+/lDfb3/45ecPbQliDSTVt7ZK/5HMf4TrfZ0/IPgc9fGPc8H6Wp7kRZdD75EO/VaU/6f6/RXS7TT2vt+vv0A/5sv0gaHJiLdFHxD8kDM10PUHHH96+R3QRQ6sad37Y5Dl//Iv0CF2q6IuggZSAEk0EHBwE2f+pLwaxTUE/k25XfkA1zoGwD7HgfifPDxpXATQr//m3kn0s/sk0VkzEdG39s5E395Y8ds7K35rim9vrPjtzoq/vkIqWKio4jDO7RQ6LWX5aw5ID1AoUKKs/NqvboBenKHxPwNi+jx9AeQJ/fqX1/p2F/taDr/eC0D84K/Tmp+4q25T/3Wy34j8/GmtC2ja7323BStO4lMoiAEHfwK41EUK6LqZsKqTOE0hL64AMEU13GUDPL9Mwn799VfHrqOv+YNsMehRVOoZGPCuDvT5M7AzSOMwar7mvhsV0Ifffv8A/V/oP5p1Fz6tIYMa8PQW0FBQJBEC2ddmYBhwJHA9QOTurd9+f6INxOSgCgLfxkHsPyaD6E187w16hVt+RgkScnwAOYA7K4uqAQwOxc0rxAfQu75g0enRxPHRVAw9v/Rzz8/dAUi1gTnvSOZFA9UgROtg+AS1tX9f9Vensu8qZoAG7OZX6LCWQUUp0ql+Vs8KAyYXeQzgfw+Mx30gpPpQQ6s3Ea+QOMUrVNqVXUaV/VwjsB9+AZXkbToQbkO5333Np0rqT1Ddk+cBDxgEkHGfLv08+Rx0BxlgCq9+W/s+xp7qnnqvf9XXvH4mhl1NrnBBoQCLhm3sTeXib8+QqqOiTb07fkDTSdLTC97TK/cYXP5n+olHK7J+tiKP6g99bdE5gkP/u/3K3QSWPW3YpbphoI2onqwHtFOTNbng0ZeBXuE++Z5G3/uHN/Z5I+GveRqDOKmGvz1G3h3yHPMgtrYC+J2Wp7t8EA0A2knuPVin4KuqKcztr/kb238C0NypDYABoACRPwHwtuD09E3TCKTvdP298t+dC8wG4QACEipbJwXBEvi+59gTBlE1JdzTESBy/Sn5uih2oz9YBQHpIECA/MkjE+CgItyhEwtgJsi1oCqy78PjqZ8CWnitC7QFXaz/ChkgZ6a4qUGigqZoGgNQ+HAXBWU+wBio+I5wHdnlQ5mp8X0qaE++KLIpGH7wwPPh9yi/6zKpD6TaINIAlt1Ew57fPzz7rufTV0DZbMrL+6Q/uvtpK/RjWfrb1/yu4zvzg3RPp4r+AzgQCEAQzBO/TmxVA8bJ/GcAgUi4F+/XR/19FPh3Xb78qdv/+Nc2BPeKqv3Rc1+gqGnK+sts9qiCb0XwFXDFDMRIXPr1oyB+fhSpz29p9/k97T43xee3tPt8T7s/LPTA7Qv015T9g4hnlH+BkNf563x6tI9dfwrj5wdgs/68sj7j09Ov+cn/7vRnZEzUmw6gAr/XobchoBiFlR9Ogx91qZ7KWQcq6J2IgVu+5u+B8UybiYvCqYjWxQ/pfC/IE+k8HPdWL8CjvAFre1OD99gJpZP6tf/yJW/T9NNLbmf+X94BTRUCBDKAZtpFgaQC3VMT+/er905quvjjLvCeboAnvOLLlHWfoKnr/QS9N7CfoLctxX3LlrdgT/Xz1DxPS4Kh4M/72PctpuO/gB1dM5STGY990tSzPXvpPysxJRvQ2J2Ieqpjz+ydVvyTEPAlDP3qz0Kk+xc7fVIIoPqphsfNW+LXQE8PdESfIOBIkJAgxwB1tmDCn5cB61Q+4H/AwZO53/H7blbxsOX3OwzNY7P528sblTx98GwswXCQs5/rqVzOQNCCBcH1I7zAs/9+y/kUCNgQdDhAIu0RizmKOwsXmyic8ikv8BCaJgISFGlygcz9wCVtdOFTNPhBEI+eB4SLzTEanVMLDMh7RO23qUmIJyVR23YXLoXgHk3ZpOtjcwdzfQRFPArz5wSNBYuFjwO83qcmgEqflj8snWB9734nhJ4A/PbikDgYyeE1v3x81jNatymDck6RQ1ekb53NGe/EGjkahFrthTPCsa64WaurgqRO/mZHCUtX0UVVOBwiygjFJYbycsYG5wNMH+aikkrCYr+y96ssvSSjiFGtTxA4rq0OXCEd2t1JPO8q4XRIyL1gIxuTz8jDWGp9UaeI4ypEktUXNbWGEdGyII5U9MZwDgXvBUJ38T0y3/U7rIj7w94q3WG5ODlZeRbnZ5fEivS8JubmtdkJlQFrLY+nijlz17tKXw87pepLj+NLMqn25bHkCljMxwUh5T0a5CN+KoeZPGL4rg/SXWwrS0bo0gwrdX1f+QvxTJY2G+1Zoz5gVxZDi9pJSlWnV3AqZXjSmFmho/hcyAeFWoeKf820a4JLI3FZnHhDX/cGQm5xMxE73Ui2Oj4ah8bdn/1CwLhdurvK0Xp/iTZVE90YWMLygtbpXU3K/rC7Etr+Jm5irUhX2mD4arVeDI7krXlDuRq9IItmIqyGpczHOilYsdTqanp26DDiq4uVZIOwusRk61KX+nzkqMVVt/SDQRpdv9/h5jgf7BWIbP2qM4tW2CFXoXLjbZT2qtGEQXrZxqqxrgjxRCKXUbsaeinFbabqgpzNjK2M+wiZi/N6S8Bbwi61sFK2En+9JeSq9EdERpDEHhB3sV3Nry1uFk7aYp0Utj2KW3vn4sonsnPcUPeJNsozqzuhB/yybDJ25I2Lq51h2wVWrltzj0eLuX4UhHNxrGY5p5fsWVrnFiIAffixz8cIr85reMTWm+hGW3i+FFbOqBy8Xsk0mZ+xG0q/SP21vSkjT0qbhrRaDom06yAnK5bUJbsok6sjpgOjIXQ4p5xlmWs9fdRQ4rivclT0xOgQlGgZhPWtyIJwuK0CvyNuN2/HFxZIbFjSE/gW56Q369xcydp0TZ3FpRbiKC8u+CRViMqFFfPE7YhKVJRt4rqHk2SwwxE1W/G4rv1CPXomVxwxBdWyeCvd7DpxV5Hl1EfFAmm3xre6j8OhFm55UG6V5Q3ZaLB5Ffnblsf4kY8Py2Q3nOzDSlwJbjMMbeF2vhBazSx3r1jn3QaR8VTttChZgdqfYrOfFxeL1HRkI1+K0wkNaoG5zpKGoYhtPpNFIxulY7aIPfiQktiy1JEbc6tn+C0048xJSVXuUSPDkNm+dLk2HtmumLOSsxbU8xI7SwLJu37TL7fDOoCTc5AOphhgGtPnNBPrOh9i3PpK5GtjVIyrCYorF6TzyPbma/JoRnPrupvJt/CqpRqRX1p64Mx90VyPZ2dOVx5xY5OsYEXdrgOtoBmT8KSDqS8r+Foqgs4R21VNOTvB2h2EJCeZfC7LMbu5gWRKrLzJi3UzO44LsCPZkRzeB4a7E7Uilwsgo7te10Vl7wOPQVBR9o+7EzMnLOPGH+ttQ7vxdYdJ7kFAY18Q9rFgkfW4v5wytyx10SY1zWuj6rIo1KFpzzVXHY+hFOS6fcgwtaXkZld63snALARAl61ZW5VzMDH1uLVErbHbIqeEUTjX5InmOoz3SYM28VR2whU1wrdoPLv0TdpuWY0la48arT2Vy25+XFPzmx7ntmQJcnfCKOS4ikTL4Q+UfRHUGZ8TB3URhHmoSThWHmLC7slF0C3Oeyr1R2oMs+x0JurzImKLcM4j1obR2cScO9TRUgfBuuy6RqlXvJIGSb2hlfnMgdOQtsRWLtdsJO/wclkZlyWFl8ORUoVTsrVgfq2t68wriWTgj+yq6UEKyH7cWspRaK2CbRlnXnPO3E2NlJ/FFR/Lg2hfKIIM8j2xAK6Nj269K1CuIhopOdSq0Mx1v+LchDokw+FW8VVHz0AG4ShChA3MModEyRbe7AbKJdkGs/AY7EOSXCjpELUavVwfWnphYOJuuZ/zFsJlc8kuR76LN6KxjzTSZiRQ2eame1kxZwHpNpXhxIIT3rDr4GQFbye+RbuKudNoadiWaH6U3LJwpG0AFxtN17TdirlyKwq9mrhFtz599k4BfSXXa3Qbagm8KuYra6+KcL4W9cuFLMTWda36Wg6Mv18cV1rfoIqfigNjmt51wAqtsSofAIsrQbhyj7Yvnlwy7i4tOmPXlmBVh8ANXeCj4nbmFB81BwO+4mxAr1pYtGGxP5iiwfA9QYahuWIX6XUHupGOGUDXssRcamP6/HynDhnc04fWPh4q+3yWDWnPzSLEVdjgIMz6+MAH2wtTou3oUNercA6TeFfi17jF5Q1roGkeq7Z0ZTRuv1oyqY8GrrU5bsTFXJCLwUYVcnej3Y10TgfuFHraVhaOwppYhckOZvSi4sL20OTJ4FbCEZ9rNjukY726mbQnXsOmJ+RcScxYhEVn1R9Q1ilt2ow0YO9GrJ2bqxh79sgpVIYiF+GcmH21X3Mb5YyzXbYpvWUwykgVb/vBvSK0dw7Gg+fb29Les8VqRoEMiwxB8FDpBOzMg60fpTQ3M5vDqY0QQ1cQfzPIlzYXlD0i6ttsvyUi84AbAh0ng6Siza7u0P0hYYum7ux+U+vH+nQ6lQSXaNwp0wAm0cHy+HiWsVh6o45JuTIsJg4D7Bw0VyzWVIBuYqG+X6xTKz56ndxZOxLZX3TRMM5zf748wTfOwTERW7tcl4y2HlYhPadcRyM2rkHLWMl4Yd+DfZZvDwoTqOQgSVZ2Qq5lf/OGcxceE1c68hlN7ajqtNxg+nLVhY65YsYjSxo1w5OcwtcbtFuvcCUiZ341jyT7Wtv9cj0iMHyuV9dUz+L+7KkIayw2dqNcBLPsrqtmdIndLvXpi0XcVG8o1B25uUbN1dxwAdjsLS03CvRgUAo5nGvFhlMzL44EQvX4fM+tonTYC7WKV1l53HK7A4vExi7xiWYtzpEZqfpFfG4cT9wu26ymlvaOwPc7E7lwC05QFnphC822WPegydo08cHRkfQwrma8Xu0HjhFWVitut+QiWuKso29Sj+2U2j4hOCE4B3LTazNVOlwl00ZFV+6UC0cAUdQ5dQlp5JRQ6NvBPCm95mm6Mgpk5t4OfqKgcFZU8EB61yOsDeFivmWI4rzgTCbB6nLZt3jPCv2CsFALD3ezY+LEQxabtK5oWHbwSptUTwkcjVFC9Hoj9VSeIikRk8VSJHT1rErnmJfK0+CuOX0bW4d1bV45BPjq1KSC5vZiUwtrJ62MFW3xjVyeCQTb56U9zuoVty1XFyooxtO+am2DlI8IbnjrZm1WaOttkG3olLoD6kQoEsKqDtmSVBuc2RUeYmgms2goTR3ny1TfxPkg7zS4oS/dqvVPzUVFzwZoG26Spx+yvZi63bHlO6HZICaurHpR7bhzVybk6Sz2Sb8bKSpyei3MGD81PCfDRoLP5joo0vPBOnYIutqYy1G7ZcJV3lmray92hFXcvGBpjUPMVuXgh1IaLreXGtlvbliZ0PZcENcGsYm27nCdy30W0zhaoC1GZhgrHMXNScDR1RnPWrxZml6ZnfR9G6aat+aq/eVcjFc92J1iXxSjml/cLtcq0tqjmzJReKCX7GGrafiSQoyL6NfLVjvAalgtrlpkY0Gl4GubtHo/XHrhbntuY55r2gbE99bdHYurdVBnjsFEfXTSo27LnnF8ZOZR6QjRcWzlKEcEoZnBx4o3G4rYwd7tZswXTo9Tm8uFWRzPDFX6ZF8Wm+XJLyVgLWU56IWQSWmXz7Qtw8jp1clgiqrMPMhqP8CVFqdZCr4Fop4HWIONjXSWGwSXqjYgRLw20WGWdgRteRgLYoJGOg6WsuOVtSujVekLiujUdb5nLvPOOGGrM7/0dNUxSMlhaobz4r66kPbB4qJtc1W3l71AHdOjNUPpKFD4xZUTlSvVnwOkcxbsuExC0JTscI/agTYFu1mpd0IuK0TI6XJFR/28XQQcVeMtYbYEUsuMJZ9RLLcE1GCIzmDxNOBRsPlVaZBFmVwHtxnM3shVzJqWTcNtgGfwrdtigFTh2e1w1s7mdateVGxzifnOT0KXrXukO5J7LF+u/c7qL3TUJfF6afmzJE0ZnmdDTr9E/NkKjtIxilSXZxJpd8bSrt3r4h4eJVQj+aUrgH6sxYoFx+x9Jd6d6lVjWsRo3nYH1VatmyXunAM/KzZs4EoL2OCX+E105CFLZt3AEgO+vuHJKTDJfS95TYOhW2yNHdpxEPVetwA3H+CgXTgd3B1YZQ0bY7FPK5QUtoVFqZWklgGBYyS2cLgs4nZJTAkMvDzHa2G2kPcOzjGFRLUwMTjrqkULytwY9VFFt7qXsWhtEkHWavCc5Do+d+jj2JOU29S+vwgNaa1cVio8toa6NE083p8UZsMoY8yLm7ycU5tAViTKni1Oy2Tl03Ync3MnjprYSMg2v1ykFZwvfdY6rwZcz5Yug9aKKVtitDZn8fmC9ftcRENTlDuk2FR4LEhbVg4yqsWcZiZ3PQN34mx7Nc5L2c/PBi7zTXgZhVOYkquOGobO3TFMIITXioNnBddjLMWrzQyPpQ1VVAU/Qxz/4sQ0ukX51on2OUGeTCs/p6BNwRJqT3Osz611TZhnrXOiYlmHbYpUK5uucxGpiD6nwiMe9S5zsnG1ozoqZ8KK3SxlYrQYxmrDUm7ZTlw047biacfj52vC2jNNsWpjtEPp1iwdwsUR7IQFTeSeo7zAjLDntkgrYBXlJrDlhzw/whG/DYyLb1jdoeCKQzAg86BZ7iS1c2+2d/RSDMkZ3HDt0c7zNRNsVlePgJkuWHuOdwvkc4ygs2ugiCgxYrB5XI5DN1IBplaavGNk7xaOnEPh6I0YmAYe55s1VTbNclYzLJYnNCFucwmmVsEsQRJzWVBYu7kEgaLPd5vLdotF65xfXbrmIpXt6HXmST5niELEDaeK5q3VY27ezC7HOXNU1KRRkd5dzDA04zOxWjhuDMeL2YXalu2Fk/Z4wNr7Li1R+RDH+c5czY54I2kMyyxJJVplvar3RERyTabuaKSR9zk6o3T3xgUBP6JSz0ZLAwAGjynqGcWG5hjK3ZFUs/ZhtSEWxHJl48cxJueMbc0s96QH6fJ2zjVGuhzMMk9wDmlQqplX5AkUX5tumnHlnpxVAlN+3cnwLNOKjtXhslMpx8bOG6GpW4vK23GJ3eiW2e9n+Y4KQmsZS7ChS6QoZNU+LIeK1vitOkvKVGphLxPrtRtcmo7brRzu0FHBnBUS+7zfHAUUrnEFT3SWvAw7U2RwtO84DhMpt7+QeIbLgaHuKY6Zc5hwJlM324XL5cunl+kg+3kc/V9/Nz0dCf6PnUw+DhHfXlzdD6OBCl/ua335b+j4y6eXyo2Bho/z2Tptw+fh5b87nf38l99/TOKGxwvh6Q1c37wd9Dd2OP3vp5c499q6qYZvdZG29wPjTy/vej4Pxl/uZmfldMr+o5mTk4rKd+36bt7zTP7+ZjPzvfgxYroMn0fYn168Abg0dutvGEl886tysv35TmU66J1eqrz8/v8A9s9H02kmAAA= -->
