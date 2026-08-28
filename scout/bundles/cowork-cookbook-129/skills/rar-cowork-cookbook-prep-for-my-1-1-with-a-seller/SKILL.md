---
name: "rar-cowork-cookbook-prep-for-my-1-1-with-a-seller"
description: "Walk into every 1:1 with the full picture on your seller's book - and a coaching plan, not just talking points."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/prep_for_my_1_1_with_a_seller", "rar_sha256": "ca7e2bb4468fa9fe9dce2f0ebe2933959594e9a144facc4608af84d1f08b1820", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "prospect_to_quote", "intermediate", "integration", "dynamics_365_sales"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/prep_for_my_1_1_with_a_seller`. The original RAPP
agent is preserved byte-for-byte in `prep_for_my_1_1_with_a_seller_agent.py` and in the RCI capsule.

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

Prep for my 1:1 with a seller — Walk into every 1:1 with the full picture on your seller's book - and a coaching plan, not just talking points.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/prep-for-my-1-1-with-a-seller
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `prep_for_my_1_1_with_a_seller_agent.py` and embedded as the fenced Python below (sha256 ca7e2bb4468fa9fe…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `prep_for_my_1_1_with_a_seller_agent.py` first:

```bash
python3 prep_for_my_1_1_with_a_seller_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 prep_for_my_1_1_with_a_seller_agent.py   # or on stdin
python3 prep_for_my_1_1_with_a_seller_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Prep for my 1:1 with a seller — Walk into every 1:1 with the full picture on your seller's book - and a coaching plan, not just talking points.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/prep-for-my-1-1-with-a-seller
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/prep_for_my_1_1_with_a_seller',
    "version": '2.0.1',
    "display_name": 'Prep for my 1:1 with a seller',
    "description": "Walk into every 1:1 with the full picture on your seller's book - and a coaching plan, not just talking points.",
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'other', 'prospect_to_quote', 'intermediate', 'integration', 'dynamics_365_sales'],
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
        "upstream_slug": 'prep-for-my-1-1-with-a-seller',
        "upstream_url": 'https://coworkcookbook.com/recipes/prep-for-my-1-1-with-a-seller',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '309c9ee888e989b6',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-sales', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/analyze-sales/provide-insights-into-sales-strategies-and-performance'], 'recipe_category': 'other', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/prep-for-my-1-1-with-a-seller', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Meetings'], 'plugin': []}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.5, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class PrepForMy11WithASeller(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PrepForMy11WithASeller'
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
    print(PrepForMy11WithASeller().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/71655LjRrbmq3Dr/mjporrgQaAnJmJBwtIAJAgaUK0owSQMCW8J6OrdN0Gyq6XRjHYmYmPBMjCZx5/znUzw1xe7qcOsfPnysgN2OpHtOI5CUE7s1JvMsy4rr/BfdnXg78TN0rqMnKbOyurl9cUDlVtGeR1lKZx+tOPrJErrbAJaUPYT/As+6aI6nNQhmPhNHE/yyK2bEkyydNJnTTmpQByD8lM1uRP/fGdpQya2G0ZpMMljO32dpFk9uTRVPakh/fvtDDKp3iB/cLOTPAbVy5effn59ieD5y5dfX9zYruCtl00Jcikr1z2OH6EY/O7ODU6DZAP4PO+h3im8zkHpZ2UCb3nAnzyvfoDC+a+T//7va2eXQfXjl6/p5Hl8fRk/RpPeNaszu6qBN3Ht3HaiOKr7twkfd3ZfTUoA1U0rqFMFzZYGb4+Z3yll+eTv47MfHkzeAlD/8PUlgyLYo1G/vvw4yUrIr2zG87eRSv7Dj29x1oHyhx+/06ka5wLceiQGpX57f14/ycKB34dG/p3r3yHVh/sc8PXld8qNx0PuUU848+XtAg3+w4NwXmYtSO3UBT/8+K/IuiFwr3FU1f8W3Z8ehENge1Cnp+A/vt6N/PMEeSr0QfNfsx2j5T/RBA7/xu518jTUv6J9t/8/kI6jFFQfFv+n5P7ZBOTvk5/+pW5/NeF14n99EUAcweSynRh8mfz6vtuI858+ed9vfvr5N0j6/0pmB7PPvVN4T+w08kFVv7//9Km63/7080+fmhzGGrCT96aM/xnNf2bXO58/WPA56oc/zoX89+k1zbp08hHpk1+z/H+Vv71NDnYced/vV18mv8+X8UAmoxLfmD5M8LucqaCsv7Pjjy+/wcqQQm0a9/4YZvl//ddkHbllVmV+Pdm5WVNPoIPrKAGj8GYYVRP4M+Z2OVayKoKGfY6D8T96eJQ48ye//G/3XiA/u88Cieaw5rzD8vGe9O84/Iz1791+fxS6X94mJiSalVEQpXY8MfjN5mtqByCtR4ZwbgXKFpYSp6/BZ0jl83gCS+rkl7+k+34n8Zb3v9wraPSoS8ZcHWtS1cTgbdTrGIL0qYUL6zy4AbeB1OPMhaL4ESyjr1DfKotbWNNGG1TXCNZsLyqhwhms5yNtaKcvI7FffvnFsavwa/ooouTkAQQVCgd8iDP5/BnK7cdRENZfU+CG2eTTr799mvzP5K9m3YmPPDawjD+9ACVc7HRtArOqSeAw6CDoUlgy7l749benZSGZFCIX9FnkR+AxGUblFXjfzLxT+M8EzUwcAI0JTZvkWVmPoBLVbxPVn3zIC5mOj8baHWYQfDyQg9QDqdtDqjZU58OSIz5VMPQqv3+dNBW4c/3FKe27iAlMb7v+ZbKebyBSZDH8M4p5HwQnZ2kEzf8RBI/7kMgIirNvJN4m2hiHk9wu7Tws7ScP3374BSLEt+mQuD1JQfc1HcEQjKa6J8XDPHAQtIz7dOnn0ecQbBNYAbzqG+/7GHvEM/OOa+XXtHoGvF2OrnCzO7gHTeSNMPC3Z0hVYdbE3t1+UNKR0tML3tMr9xgcIXkCLT9Jftce2M8+YPK1ITCcmvx/7iNGuXhZNkSZN0VhImqmYT3sNXY7o10fDRIE9rvo99z4DvbfSsW3ivk1jSPo/LL/22Pk3crPMY8qBCX3YO4bd/rQxVDzke49AseIKssxdu2v6bfS/AqVudchqC9MVxjOYxR9Y/h6V/UhaQhzcrz+DtN3j5XeaBIYZZO8cWIYAT4AnmO7VyhVOWbR0/IwHMGYUV0YueEftJpA6tAVkP5o9AjmBSzfd9NpWX03sl9myffh0dj8QCm8xoXSwnYSvE2OMBHGYIBuArCDGcdAK3y6k5okANoYivhh4Sq084cwYwf6FNAefZElMD5/74Hnw++he5dlFB9StT27hrbsxjrqgdvDsx9yPn0FhU3GZLtP+qO7n7pOfo8hf/ua3mX8KN0wh+MRfn9nnAnMnaS6h+JYgipYRhLwDCAYCXekfXuA5QONP2T58qe2+4f/rDO/w9/+j577MgnrOq++oOgDsr4h1hssACiMkSgH1R297riT9J9x+Bmz7rP9+ZFefyD6sNGXyX8m2B9IPCP6ywR/w96w8dEqcsEYss8D2mH+eWZ9psanX1MDfHfwMwrG2hn3EC4/gOTbEIgmQQmCcfADWKoRjzoIgfdKCl3wNf0IgmeKwEKdBiMKVtnvUveOqNClD499FHz4KK0hb2/svAIwrkbiUfwKvHxJYY16fUntBPzVKmSs5jA+oRXGRQvMFdjB1BG4X310M+PFP6yyxiyC6e9lX8Zken1Wt48m8nXyra2/r5DSBq5rfhob2JElHAr/fYz9WMI54AUuoOo+HyV+rFXGvunZz/5ZiDGHoMQuGBE6+0jKkeOfiMCTIIAa/4mIfj+x42dlqGp7xNuo/pbPFZTTg93L64gDMM9G2LDTBk74MxvIpwRFA4HNG9X9br/vamUPXX67m6F+LPh+fflWIZ4+eDZ3cDhMxc/VCG0ojE/IEF4/Igk++8/avudkWNBg5wFnu/YUEI5DUQzr25wPOM8FhI8BBxAcSXI0/FCAs3GKggjvUgzG2j5LebiPsQ7OEqMwj2B8H8E7GgUCmA9IDidcj2QImqY4fErYnGdTU9v2MJadYlPfgzX/+1SIgN5Ty4dWowk/OtDRGk9lf31xGAqOVKhK5R/HHOUONkpNHS1cISSGzvYo2jlJuyL8s12vpzGm4wTWtdtclHcNs1AFA4sx0x6qIlIPgtNYmYgYC6QzyZUvzONznOMawa49TN7NOAsWJyFA2zaR3dCQMgbgRWXucHk5SEd/WJNyTR5y1TocjEIqWaRdt1Ran0987OnRZi/jJ/JcJrhYNclS3MVrzt/v8nDniLgZsofLEl9cysrY98JS6deD6izJVWwHy+OeFu3zjcIPQaro5mBRmuYInZ2e0GFwNiuHpf2TQtWrHGHB5iysJDrI2X5v5ge9X9u1aZNeXB4Im8ClRdScmWwJqB23K5ikKuiTe+ELDy9XgGxdM57m26lhrG3pUp+EbuqzTpTv6Ns5XJanXQf0bdTYDFFdl7q22hx2R9OfbY+8VJDKsUuM05EnhVqrNWQRgmF6xGy0mBYV5hzcrN8zi2Nix8O6ctWBbjBsEVvL/Jiuy2Zu5vNtxR5We3Zp7UiZw+uYmQ7d/NqI835+vtiU5+P9Yc1VW0priF7LW++86PZkgWtkYm5dBi8kq21xbrloojRUpKNl04VAUdz5qgUZIVi+Z9m4jce0ub9xNztfVCV63i195lAAI7ZWN1YYyF0uHMW5NzDAzOTYal30dATTlbkaAmWX0AFokKPvA1kklrh389dOg2yOAqDVqBk4qp7n2ak47rfU4chWN5wI+74q8cS+bMuBZ6mLYa6lYnsZ0guNRS4phcgyOM2lTifzTbrLnUgm+tAykaO+uM2FgsPn5WbPhdsenaZtMY0tHffPyLE/sq5alWo1VPQ1VNNdPF3285Rxts60PJsV2qXoolwWLnL1s749pQnVghw/u9ssdZuhWUxZk1j7y2owPPGMVqIscXrr5xdEsvTLmShTvJlRpu+AKN2WjuSUfR2f9f5oFPixPly2tAVQq9GyKBLktemmWMZOcdU49vXuduqv0+CKMzKWKuqVow1XmS0sWbwdhLxKj416ZOWZ6M/KeG7UTmQvwHzWGOlO7eVzOZP2mISLdUGUS6a6dVRyiW5YQ++NwPORxFsnBNfltEqp8bXCSJ1dsOzVDa5bKbeU403lL4wsuahNTxOCX3k1di1QEe+nhps5WNCs0YrriFspzm5Wjvr1vBgI6do3K3yHKjvFqPYEa9pUIQuXI4gUxT7K87LeptvlWmtBZm8StjQWFH9KrLVP7PN4lYoJ8DArR4IQF7dEgQ8r0mPLm1Rt0yMXOmfyTC82m82VqFaLrbeiFrp8sCtzRcR79HD0zAJ1InN2QJYYla8v6uBp0c6vQ6ngnHRXO8vVUiN3lAFAvwuUTR8MUnCmlRO+3A+HRe6Bs7DpcnNzm210tN/cHE5w92F/sUMSxWxKRYeyiM6nKa9zJi1MU4FWw2hW8XiqxiUeHRqul4R6nVMXdsoXMNcZdliZhrGfGtfaYxiw3KqLm7PXqPSiIrNVit5Q8eQV67gZ1tzG0ymtPrsYxWq0s7XW28ZXh6XV2LrqqVrs4xpsSvfHIUsPpNr4RgxQnxVAyMbKeXOcBUDHN8sgTEvHW0bTmXK7JvKpyS+bKjRMRNq7dUGlB3wXX4XrmrNp64aoEVWtWG+/4fO6ExI3oYmQRvVQGtRdunJyN1mCZLU6D7dZnF33Cs/300I4ry4LZIYc2T1XXiIfMYNruJOiqsMQ4nbyy2g21Wul5/25bobGGbtsg+PSscUwpKOu2szPs51KXFbK6uruqYI8U6f0diE35W5+3XnxRcojfJ7zeMNdBmbe1aZQXCqWQfyTcUOASS+sRDxT5EHXW+KCXWN5zyCafTorYkCJsYQx0nW6IemYPxDkxvWbrltI/dwn2ypC9no5DAN3OpEDYvj5eb7YdUs95yGCI57R7bbzk3X11BNx6ffhYS9eyILGpdjkNTMJ8dDeLUxNa/idLexPJsYja2eRK8IVV118SkXFNbXPuQJoPXBq8zKtQLdN/SuXWWdoZAHP1+mQDdw5Qpg1calSiSWu/bGqL0i+GirZk2CjVOXb2G7xitaLvclUu2u13Qeb9YKKjAIcitzdt9nMJatKOXCLI48vkWIIw0HGyqFYeCbId02+aBTLgtlGKUokCF0mELvQlVJfStK1lJ4vm2QbqN5FbGlmAfEjWyUb3FmqBlw347OSOYPVER3y9Gzc+H1V+ZpmcVcVogij5VvEOhUboA8FuvEsWufTJFyprdKUdpMkMr/hWeS0F6qrdO7xbRiJlVMLaGBFhziPD8OJvHQuRp5Py3BbSzymifvLTItLV7XVEFOc21wz+qWzxq8iwOhstUeuc0ff0Ta5qG/LPpaGzW3DrxNjsdly1BaZnvJ6XudzNUm67VkQjbOT0Tbd7uijuImXV7Hu1dKY6ia/rQKUJoi8kG/yqdzz1ykYJA7Yt7yIr0zgXBpvsy/EUqYUC5dFoUxr61bBlpaISnQLa9XeTG8SzOy830fccDDjm7zBrOwwr1Fny2tsw9xyN40OtIF0x0Gou1477BbqVV7tk53ImkcxoOfuGccsBXYLWIvaYr5eY3OZ8fzQUv25QFoekVyuAeueVX7htknbzC6EozFxXRRFMOQBy20wdIgRcZa3ph64dOgEl/R4yDqDdwFNxrnmsnlcVai/WtJam3NWzyVK5DGJ4AQIvctWtXhRBXajxTiVLbbiLueJJS/RiXNYNoe4EjjRuajVFimlDDFpjK1WTLSRq8A27UwOp6csN89xALwdc1YzfbrLmFXLLy4tICUxyk/tllhYuNMctlLttHp+y0415al+shqKQ7nS6JLayM6csS75iReWx00hznZT7sBvaToESX9Ief20CPa9eGb21Jw5z0q0MIEaeZwT66YpZGVLCWxjm5jEUd1mge/bhX0EO49y9qJGUpkatLp8jU5qFUSdYmpzCyx2Ylclc45YbWCHknV5MTRhd14dBjGueomIpgbRHZpCIC6CwM4jg9pmwKuiVNA9Oco2i5YBwzyXnIODBzt2hhwsY2Wn0tmfHk9+bmqhU5xsJRPcGUJQ9lISmPDmdPLgHsiZE2fnfnFsaHY3axJ0e+gD3rtwynHHeE4mnGWw9LplXhKK7xFQ5tOqE1oilBw2l1Vzd5UXnNmop3l2PO44ChVrvHchXC56wi6cvWxzgt+FexGiyZlRufl+QGopZZdtyYBEUrtM4/zbtUNqW8ey2XmZFl16nZdraskLpirvMGW5n8EOTLvVqckK9mF+prdkrm0vN3Vl9j3WznW/FRvJuqydqBU69aItsKslgjld3WTywOa2tkoUb57n2hlPejuIguUUxa1TFM+yGbOr3Fps42K7aXxb4fuQZ1zmsp2H2NKL4sPyXG3J7GrxOU7e4sD1KCOkVr2/xue8bnEbNbC5ep/6DbeId3NLdCi3x1YS1aa+QhqrLcxEB/biRGKsCSNMWZr2L2bQoQfHOpyxnDlldq2YvEyJzJ7rjWtl+PJg9N7GPi2TPtzNCJmfwk5tdqB1cb6R9je9XEMPaleKXfIXbZYLU22hKTN8u9UzpAnsAwhkV7GwQalWlpjPmgXfd6HnCDcqvBgLbF5kKioX1k7ebAC+lK+tdZaOM38FYoK25Vwh0M1QThXXZfw1KjKEcTL2s+SylPMTQqgc4xbuCuFFmSBTnQmxtcfeFJsUWqd0yml6oYhCMxCk6ExvKjkFl4BcNFsbSuitUa9pY7QRIkRZtqcm6dwVIBQeVmpujtQJR1CLJhWz6+nQnb0kwPRzN8N7dZqu2KrxkhmrheTKI4+0DOTd2uDhKm5f0Vrne4cZi+2wbt2HRZUnLNoE7ZLM2oYfep0K0P3c03sF2Wuqzm3ZK+qJhSvvLkS/JoTYO+gHTvEMC+ilTrKpdbryRJLSgww4pbYIFj2KnBKcSBSp2g3Cy96yFHbhBUUlAeFOPA0EemCYsPCugIw1STksGd5JcsRcrm+SQ62ODaImC39ZSwo3j+mZxN+miBFaGrWVXa9ZSjc6RPhcTmmNyvSMXKTcacF4VN/625Lu3GZWbgkPxIpB6Qro5zhcQSpblKCDxoJdd3jbmSK6rbIqmyLhVKM6jsToQIfdvNsS7JRTOpI47Z1GdU/5LWKF9Ox4XOiq8c2pqost2sNmPdNr/IK3rgNmUY8dVUSbeRpAZ7wnUEw9G+qSrWX0iHIUxRo9VTbhlQtkK4gAKmAEEmK2UKEt4SZdQXPlDbtJ9QGpw0N6bvyS0k9SdlC4VrOkrcdk3q1DXZRl/RxsKhEX+dM0PLDIJfRDtZVu8rYeAkPvrqBcn4z5TZ7iF6TWsaUKBFVZ2KlDaLct2uW9djQ7fRsoxmVD6uI15JfDEYOQrFeePPfDGjOB2LDMEEmdEsVWj8DlslUFTCVvBgefKiTr3qYKulX2Ab6/lcgNa+PONRRDknHsLA4ac7Y2Eh+y++4gXVD/usTxI1z+rFdszEm00boaqjnnmqk4cort56Rszsw6bQ1zWDMbKQuRPQmaFc8tzHMXtb5BGWSUVUKl4bWMmMkUx6mBvqnulgambonz6XF9spi15mwDB/EIvjuuCn1FGnXd5ojl3aYOuT3wzTHqprJ5miswgUry1kLPY8jQML5d94Kwb+hDpCsFLSEXj1qIndOJGbhaLQJiaYpMxQhi2w2NDhg4LBaIiXmbHTCEK4bvNMa+8WqtoeGslWEDxHBopcwE2qnbW+N7bMusCL85aQBBb7aAbISNQLu6ZqEZvgUo2wirAsXaCzrz5s4xl6elQaHuGa2nxebiYgjJbNCqadeuIQAPnTlOf2xLNTirBatit5mmz/PqmJPs7Yh0Co8VAWVkjFaiTaGTaLPcdLg2p30629EIokuz7X4n4DV9U1YNu5kjDe1ZcoWHTdIm0QUtmEMGV/lpzF8wbbrJeNnC3AVVLVwR6uAew01e5wxBr1Z1PSUqGhCAEwiLudoixGzMx63wMuB8WlG+ku9PkmuSkd/qyppfKXNpruzC5SAoWq8XbNji5xi2qoKmnM/L2YU+1XhhKAuHMGuj4/ob5p5vMdc6zZTkJRTFVJNaLak9tUK1WmIjEUNOLlhtYcdEyvgsrpHhcA67dWAqbJFdPf0aHereYiIWn2tH9LxUBvK0nirETG9vHWwH544yxwkuU3cqRpJKZ1acgDmIWumFW13n++llNchuq2s6fTEadhqZKDtLcT3NNlQkziwgL3mef3l9Gfebn7vG/9773nE77//ZruJjA/Dbe6P7pjGwvS93Xl/+TXl+fn0p3QhK89gzreImeG4y/sOO6ee/fNUwTu0fL0/HF1u3+tueem0H45d9XqLUgyuSsn+vsri5b9i+vjhNNX4BoXp/bky/3NVJ8nGXO6vDx557mVU5cOv3OnsvmqwGL+OXA8Y3NcCL7I/L4Ll5/Pri9dAhkVu9kwz9Xtnjd42gjs9XF1A14g17w19++z+CohbaRSUAAA== -->
