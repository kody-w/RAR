---
name: "rar-cowork-cookbook-demo-data-develop-communication-strategy"
description: "Generates and creates realistic demo records for develop communication strategy in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_develop_communication_strategy", "rar_sha256": "48880be8f707625dccaafbfdea7280ff9785f9295ef2e217847b1e1337e0c60c", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_develop_communication_strategy`. The original RAPP
agent is preserved byte-for-byte in `demo_data_develop_communication_strategy_agent.py` and in the RCI capsule.

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

Develop communication strategy Demo Data Generator — Generates and creates realistic demo records for develop communication strategy in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-develop-communication-strategy
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_develop_communication_strategy_agent.py` and embedded as the fenced Python below (sha256 48880be8f707625d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_develop_communication_strategy_agent.py` first:

```bash
python3 demo_data_develop_communication_strategy_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_develop_communication_strategy_agent.py   # or on stdin
python3 demo_data_develop_communication_strategy_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop communication strategy Demo Data Generator — Generates and creates realistic demo records for develop communication strategy in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-develop-communication-strategy
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_develop_communication_strategy',
    "version": '2.0.1',
    "display_name": 'Develop communication strategy Demo Data Generator',
    "description": 'Generates and creates realistic demo records for develop communication strategy in a sandbox tenant for training and pilot scenarios.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'hire_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-develop-communication-strategy',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-develop-communication-strategy',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '0750c9e98f5bb113',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/develop-people-strategy/develop-communication-strategy'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/demo-data-develop-communication-strategy', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class DemoDataDevelopCommunicationStrategy(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataDevelopCommunicationStrategy'
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
    print(DemoDataDevelopCommunicationStrategy().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/816Z7ebWLrmX9E994OrruxDkEju1WuNUACBCCIKyrVciJwRQQJq6r/PRtI5tm919+2aNR8G+0iEvd/wvHFv9PuL07VRWb98flF9p5gxTpbFkV/PnMKbrctbWafgq0zP4G/mlkVbx+euLevm5eOL5zduHVdtXBZgOuMXfu20fnOf6tb+/Rx8ZXHTxu7M8/MSXLpl7TWzoKzBjauflRWgmuddEbvORGjWtBORcJjFxcyZNYDWuexnrV84RXufBp7HRVyEdzZVnJXtrHHB4zoum1cgld87eZX5zcvnX379+BKD85fPv7+4mdOAWy8bIMXGaZ3Ng/n6e97qkzUgkjlFCEZXA8CmANeVXwPeObjl+cHsefVT42fBx9l//Vd6c+qw+fnzl2L2PL68TP+Urpi1kT9rS6dpfQCKUznnOIvb4XW2ym7OMOHTdnXRTKoCaIvw9THzGyUA0N+nZz89mLyGfvvTl5eymrAGMn95+XkGQPnyUnfT+etEpfrp59esvPn1Tz9/o9N058R324kYkPr16/P6SRYM/DY0Du5c/w6oPkx89r+8fKfcdDzknvQEM19ekzIufnoQruryOlnL9X/6+Z+RdSPfTSe/+Lfo/vIgHPmOB3R6Cv7zxzvIv87mT4Xeaf5zthUw61/RBAx/Y/dx9gTqn9G+4//fSGdxAULgDfF/SO4fTZj/ffbLP9XtX034OAu+AA/P4ivwjnPmf579/lWVt+tfPnjfbn749Q9A+n8ko5Zd7d4pfM2dIg78pv369ZcPzf32h19/+dBVwNd8J//a1dk/ovmPcL3z+QHB56iffpwL+OtFWpS3Yvbu6bPfy+o/6j9eZwbIKN63+83n2ffxMh3z2aTEG9MHBN/FTANk/Q7Hn1/+AHmiANp07v0xiPL//M+ZELt12ZRBO1PdsmtnwMBtnPuT8FoUNzPwf4rtGiSSuokBsM9xwP8nC08Sl8Hst//l3pPoJ/eZRKEpD371QAr6+kyAX39IgF/fEuBvrzMN0C/rOIwLJ5spK1n+UjihD/Ig4F3VfuPXV5BVzkPrfwL56NN0MqXN3/5dFl/v1F6r4bd7Mo0f2UpZ76dM1XSZ/zppa0Z+8dTNBRXC7323A4yy0gVSBTFItR8BCk2ZXUGmm5Bp0jjLZl4Mkj2oFMOdNkDv80Tst99+OztN9KV4pNbF7FFCGggMeBdn9ukTUC/I4jBqvxS+G5WzD7//8WH2v2f/atad+MRDBqn+aRsgIadK4gzEWpeDYcBswNAgkdxt8/sfT5ABGVC8ZsCScRD7j8nAV1Pfe0NcZVefUAyfnX2ANEA5r8q6napQ3L7O9sHsXV7AdHo0ZfSobFpQ5Sq/8PzCHQBVB6jzjmQxVS5gkCYYPs66xr9z/e08lTcgYg6C3ml/mwlrGdSPMgMfk5j3QWByORkze/eHx31ApP7QzOg3Eq8zcfLOWeXUThXVzpNH4DzsAurG23RA3JkV/u1LMRVMf4Lq7ioPeMKptE8l/G7ST5PN71UbGLZ54x0+y7830+7Vrv5SNM8wcGr/XviBKMMs7GJvKg5/e7pUE5Vd5t3xA5JOlJ5W8J5Wufvg5l/3ClNVn01lffbsQqaS2KEwspz9f9GWTCqsGEbZMittu5ltRU2xHtBOLdVkgkcXBjqDB7EpjL51C2+55i3lfimyGPhJPfztMfJukOeYRxrraoCfslLu9IFgANqJ7t1ZJ+er68nNnS/FW27/CLS6JzKgK4hs4PmTw70xnJ6+SRqB8J2uv9X5J3yT5sAhZ1V3zgCwge97Z8dNgVT1FHBPewDP9afgu0WxG/2g1QxQBw4C6M+AEDEIIZD/79CJJVATQBvUZf5teDyZEUjhdS6QFvSs/uvMBDEz+U0DAhW0QNMYgMKHO6lZ7gOMgYjvCDeRUz2Emdrcp4DOZIsyB9b+3gLPh9+8/C7LJD6g6ky59ktxm7Kv5/cPy77L+bQVEDaf4vI+6UdzP3WdfV+E/valuMv4nvBBuGdT/f4OHOB/df5w7ClbNSDj5P7TgYAn3Ev166PaPsr5uyyf/9Tb//TX2v97/dR/tNznWdS2VfMZgh41763kvYJQgoCPxJXf3MvfpwmvT89A+/RDoH16C7Qf6D/g+jz7azL+QOLp3J9nyCv8Ck+PDjGIT4DJ8wCQrD/R1qfl9PRLofjfbP10iCnjZgOot+/l520IqEFh7YfT4Ec5aqYqdgOF855/gTW+FO/+8IwWkN6LcKqdTfldFN/rMLDuw3jvZQI8KlrA25u6uNCf1jnZJH7jv3wuuiz7+FI4uf/vr2+migAcF2AyLY5AEIHeqI39+9V7nzRd/LjGu4cXyAte+XmKso+zqaf9OHtvTz/O3hYM95VY0YEV0y9TazyxBEPB1/vY9wXk2X8BC7V2qCb5H6ugqSN7dsp/FmIKLiCx609VvnyP1onjn4iAkzD06z8Tke4nTvZMGU3rTDU7bt8CvQFyeqAD+jgDQIIABDEFUmUHJvyZDeBT+5cOFEdvUvcbft/UKh+6/HGHoX0sJX9/eUsdTxs820YwHMTop2YqjxDwVsAQXD/8Cjz7v24on3RA0gONDCC0JEkSPvtkQMAEjmKe6zpOcA483yFQEg4CiiCxgEIpzA9QH0UIckmcER9ZLAgfdnHYBfQeXnrnF0+y+XDgLygEdb0FoIgtKYRAHcpzloTjeDBJAk6APoDpfWoKMuZT4YeCE5rvve0EzFPv31/O+BKMZJfNfvU41hBlOPjicO6j03zEA2ufUHtOVUoOXpzhnV7E8UAUZeol8yOaItslvuKsNOpoc3U8xIyF5E22wVbFyMkL6VSsktpLKo8/9zzN7BYaQlDZMCcxeBcOK0tWzMU+E3YqpaDm3B2WtqFLnmgMatcvaqmwLldLR7CeysZ0FVLGcCIw3AygjFoL2JAd1Hw7XyJu7qm6lrU8rsfqRdsYZ8tgcXKzHGysr4Z9bZiIwxWSb5iW3eduS57PVmXz1qWKBCFDDpW7OeI+RJBkd8BQuztU8zFG7OuBgA+oHUs35bZUdr6ItAaT1bJtIlv7kl3X637kExuK61un4iHNr8+wbyfb1icqyIrVzl5r5G47v6SXtFOaphvVQfBNkDNizjCGHaZvd4OZNrcevXJgXaR2VZIotRoihSZqwxExDby2k9ShiqjrREhZ6E51lgqw/gIfyFog67kgiBnMpa5FdtZOSrmVI8+Plx08tCizTFJ4cZVXgzqMC87O6JVxjZEBZQbjVhchvDtV3gVNBx3bQF3hHfeUiO/1fdCit6E1kTrLBWNYlGO6hNpwb2UNjeJO0tc0frt1daxW14S5uAQ/R0kGOuGJOngNo5mxsXeWScK7XNPuZYNEVLK1sYZiZSm0uXMu4njlU74H803b4Ws0MLXUY8SaLPj+2gIDCcu21vfhZeGicSLZLJ6gut1GVnPyd4Rhq1wouk43Ch6THnXCmDslBtdeL8ey5iy3I3CW83oXyYPYS3vdPTWlZccFsja1eTmf17TX6oazPZGLLN7Fdney4jRXhdhes3Cx4Wrl4jidrTqUwV2wTLrwFOY4zXauCVJH08F+DVnLgD7Ob01y2ubp3iciSBACjOCvV7uAtkspUlsaQwV1w1FsYxIYM6/U20UOPG1fY36GcmI6yAlPw6ZPHseo3la+yerKnj3EubYhiRPQCnQeeA+zLH+hlIwsfH+7ixKeRwdPLaPzDXNpnSF1RcPEchl7Td0orHo4Dsdzv1N7S5f5OKczBEuiXjicEskj+WSPQ62M2/7RtStYSzMhxDi/xLiAkxitpcfqluKIYFGHHVSklWezt2BuwXOWg8+qu3fQbjEES/Z0StxzctHM6GamJwTqW/d8wUfmWJY2P4fjul5bux4R0CRvRFe08FV1y+bbhUyyu7MhqxWpaFRjM1m8Lo3MOay5RRm75H6T6qULQ3PqUOenAoDK2EWJHwQoUHCuicJroZdcrpuGP1a6DaMJWZIIB8UHPi6Em43YlwGE3HWXbBQE5mTuLLXdQJpCFO49LOy49bgUrrymFYLnDk2Qqh2fBo3nidAxsa9I38cGzxl8MY+UHmCh7Nb+Ao/cOQZZBSeZ6nFLOLsDr1h1H5tnk0siKhVw++AeN+opt3UbGbnD2lho+gW/wIxpqHpYnglZiNK1RrHJvLqMu5ZGR3KQbDOVESFHSEmAiiGmh6QZmmF5y+VwPSz0ky9XrIQnZusjUCqrdYpAwVzfr6AuhVlz1ave4GW0WDhoc9lQ9q5P492JrKJCz5Sq4ypXCpxxdebiDceclCvKwAPtjA1kGxTZn5l9r+B6HmX43KcFh+mMQ6cWCwEzivnNjDf9OklXVih2uskH4jWjN/LGulmnLF3e1ttKopkev52dYJtdh/qW8TaWhQIMl4Wl7kejzIcapXeBORfGmOZVfS3p5HhU6V1+ldaxL0kw5h7h0GPmXrUCOiy9hLxKgevboKpvsaI4QdTyCvKvp+/io3bWszqu5WvAVUZqyEM7tCf0KPDKkuc2I7QgyZUrSofrVTpY8i46RgnI43NHTtcQuzshTtBDbNJjc+zIMocwtLHRvSyyY8pZ9KlRt6l4toleW3Vr7ZA5g6NJK9Y8HBejKK0vtw0R7s14YfEI7STMCDqd/tJ41W5frtxOjSojlHcCvOkTHiCU3KIgO14MP+2NY7Se7/LMDokowxDO2JrSyBVEve62fHJQKvFKGgTXO3bPT0FsJZsubJwl60BopOc2aDGQuXG9ObnoSp5WBdqWbhK1qXIqzVq2JxqLY3kTtRBRQ+nYjF20OlDLfF8LDKk51DVqxyM2iMtGyQ+73UpzypSv3LbyIfQmLwY2khqxv8Y3vHUmkidEn+OgXhI0plc3rkIlUIn06+7m2Su6TUfTry5ZTKsHtsAa5ZwVLUesq80NUS8dfEIzZduGxho225yIbNirilt2IhF65PZ6S0sgu2+9MEq3BnrsTFKrZDFd+stMjbJdyLjIybgYSkM0BVfs4Gy1p0K8LTtkOHdifEkOWjys+2apOjazxY0WJS1LaQzbFPpDSycpf/JyK1txlOiO575UM7R39+aisd1EVuFMQ5wqbth5ckFMxRcKytmoa3hv2M6wOcJ+I3koPZh4PFgZpJSjiAsRv49xLj5QW94OD+IyEXb7w61UoaOsVByiHNoQdug9n1lNnG6gG58WZn6spVWM+N4lJNKUyCBCyTg6D/cbrSZlmr5gMnqze/FwoPUhW9HI6FOVs8laxjFEb5cau0SLCJzqqOKM9NAZWYWKTsqu7jom5dL7JMITH4Vh4sr4w0iRqZPNqaw71zfLtBHeproNVjkRCFkh3HSUE5NrRtgWxn59Ox69zs/1NuIMUKh2amaubCD7Mr5g/gnrNWI85JwVW3R/Cryd1DEFlh/95do5ZrXB8+ESLlfqhW24Y6ZeIonydCLJL9RWaRHUNmTREHbFRYZvjMAtbiiZ8fRJjERBgecbPGY6VU50kBatSxiNo4CYhdKsbE+RV4Yo8nsaUR0N51oy4nLqqpeYLN3iZRjgyxKyUyThMonv8KVYH412EydcIYoazw9Rt8e6jT3yNOlEgrzN1KOqKdb6MHLUcWuJewWVatZmrELcMMXIxhcU9LC0DClZNN/oS4o7StIo5Z7kpdGR26GibOfWBeGZucitFyfJnTfKKU5qQh1YirfdQ3m8lnpIwVtiTSzJc98farttHScxYgRBlsMpMLvNyQsG4F0lXqS7M4/BXXkahJxbuBczcUTcDjAuJ+a33TLrTwofdRzKKbErVMcwWi1Vel17YzwXiZPIrHNe89IatDj6Gm02/i3SF4IZlg7HZru41iRUgHLFlKBGDS5L3G+v4pYzeSJa7Ku6VY3qqA67WomAB6Eckq6Y4SZlpSSWu0YkdFcHsR9R+2hLlgnccTs1MrpWcw/FBnX6TWg2w5YYbuSaMzyx4unshjpMn53zKC1yQfZ1Tci1SiRM5rQ9N5B3CGLBCs/9YYytcQx0ph2L0qX43bbqXfV4BBrujRpL+ORC0Jc+ErqRPXFFLNhzhc7gXj5q2OpmuKzp95qHsos847gwKqLFbSFfKtrL1U63L0ztdfuWySSRXe8PKKRIMC5wS2a5EQgz50ebFjHU3FXxPL0uU3uR8BYjiVqEn/D0nLIVL9wW9IogaSvdu+N210eweCmPm91GbDAdtJ4w2siNlRhu4W1X5mrt6BLrrIUO9sM2VFNruVWu2xGyTG3XO4oZ9opkl4vNuu8ri+2PtgNthMtwsHG4hsWT1y1xbDEeKp9wM6WDK9syRn+zl9fDeZ0HYno6ZoW73nmUuZlXocPgVJKdKy07dUan9fMhxNgarU9gvXqpc0gyGzSXHZYGa9OF12E4RIRg7T14JImYYmgz+HKU1vkxr6sF8BtBH/MshumsoBFhgwYrwo3doSUOi4O5ks9Oqx8EpLfWtE4q7CWy9BGR4us1glZzUcNS1o0O7B6fo+ztjF+hynKZLd0tA2pVHIPDzWHSFoCoypd258t75eqxZ6nveoMbScqwfCkRxqYmxJiuNW4OaCFWS7CnDeVoqSlfrtBIbhfY6qrxDSIR8oI0ZI6QPKRfQNc2j2KK9zZrz/EHWYB8OHVZWenxdXCA+82WitFh0a8VbLtdkdh8ICQHXu2kHEmivWPLe5nfLuhmyw0s1mCxS3FnLjNQTGJXvXVwO3dscCYZm6NnMyR9lFrfG/LC1wU0EuI2VfTcMiBaz+YuccOkhj6voWtg+kcohi2ibnhozW+WbkvQB8z2WrAmFRHyKlxVZl3TegopXjQfr+1idatWIOS6qAOxj6tZHbBKKXlVgNWn5QKqWTaWU9pANhq6suM1R+RSsbi5xdEr7HkPD9vTCb2y2tYkj1zCY5KdOHMvw3xWqU/jddW51x1bSKydQ2OPZvD8pukrOsix02G5z+ZLxatvB4YoVvFyUPC1n20P2+BqyoTjYaujy6hSqgbX48JmF0IN8JFZMl55DEMtQcTuwpyZh5sz2rFiWAgqaBp50xe9flOyoyrsHNqZc/4YKRUFnUBzRc3z1Iqu1gaxdhbT1GfCwkTf3NBbk8FXHLl1Tm0RlvqGtc8b8ImDxRpvEMAtTuxYL6Uxkpb5uGoHlKrQgA3ErLt17smWpDjL7dv5YGtumY9uRvdqqdG0HyhEdMpXzYYUEeQQcCcT8rpt667Zbd4uBY6oLd8aXNCUwd5cJrZ2Td929rA4UJB4ckF1NCLifNtkYcMMqtfA4q3Bg5MSYJ4FEzbiL5YlEyXlwlw5Ul109CK8+euTIB+FbRYoc/qUqgsOtrb6BmfkIba1voy4wU9OcK4fEYkqd66SpMSZ9ZfHzS1pqRTWNgV+q2XSCahtgxME6Z/WXjBCMn3dRUVPdqxZ+rDc6GRP7E6shlznXkxkZhl5C5WwKUw1D9eOwy37Elyp+RqCBHsncdpi4/U50vILvgcOdfK3vBUy8s5w2oOXAn81FVy+bDdbp8ud6/xYL685DzFYyYRpRuNgGd/3ZLDbqrADEfMlFe0wJEeXi2s78px4ROGOdooDOXC664YbKRodMtzCzBrO1hsJ2ZOEu/TAylrOcJzMs5oIPII/tVoBQ7uyoa2AEYjr1cWc1EAFNkpxOc6r+uZAvCTcglV4SY9JvIRp/7y0U8VYZOL1iJaMJzmltjncmvOh1U6VDietPVDMKAt0bzSsRlX4SAdEh6nByg7ykJavu4rUjzk64Enls8LBI0HFZ8ACzzw3XLreE5imEyWcHpsOkXcsXB4vBTRo/Ll1CdiytviC3YQSDFbv2QWlSkHZwzm8X2ktBew3L1OZl/cXFybHBaeer55BjdvrpTkXFtEGGSJcS7mXl/7JLKvVavX3l48v08bzc/v4L785nnby/p9tKD72/t5eK923jn3H+3zn9fmvi/brx5fajYFgj03UJuvC51bjf9tC/fTvvpSYqAyPl7PT27C+fdt9b51w+sHRS1x4HRg8fG3KrLtv5n58OXfN9LOH5utz0/rlrmRePXbAn0qB8yiu/a9t+bX2W3D2Mv0mYXq/43sx4P28DJ87y2DmAEwWu83XBY599etq0vb5jgMoib7Cr8jLH/8HGdY6vN4lAAA= -->
