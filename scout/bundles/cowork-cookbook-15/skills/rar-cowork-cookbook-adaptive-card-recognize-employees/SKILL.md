---
name: "rar-cowork-cookbook-adaptive-card-recognize-employees"
description: "Produces a reusable Adaptive Card JSON snapshot of recognize employees status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_recognize_employees", "rar_sha256": "426759bf3006f0af5779ff2e1278fddc4df296593911bdb1ef223e669f06d89d", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_recognize_employees`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_recognize_employees_agent.py` and in the RCI capsule.

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

Recognize employees Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of recognize employees status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-recognize-employees
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_recognize_employees_agent.py` and embedded as the fenced Python below (sha256 426759bf3006f0af…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_recognize_employees_agent.py` first:

```bash
python3 adaptive_card_recognize_employees_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_recognize_employees_agent.py   # or on stdin
python3 adaptive_card_recognize_employees_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Recognize employees Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of recognize employees status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-recognize-employees
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_recognize_employees',
    "version": '2.0.1',
    "display_name": 'Recognize employees Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of recognize employees status for embedding in dashboards, emails, or Teams.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'hire_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-recognize-employees',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-recognize-employees',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '6c48a376936c7297',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/manage-performance-and-growth/recognize-employees'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/adaptive-card-recognize-employees', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class AdaptiveCardRecognizeEmployees(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardRecognizeEmployees'
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
    print(AdaptiveCardRecognizeEmployees().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8V6eZOjSJLvV9Hm/tHdq6oUN6LGxuwJhBCHhA4kEF1j1RzBTYA4BKhff/cXKJVZ3TszO9Nma/ZURwrw8Nt/7hHkry9O20RF9fLl5QgcOJGcLIsjUE0c6E+EoiuqFP0oUhf9m3gFbKrYbZuiql8+vfig9qq4bOICouW7qvBbD9QTZ1KBtnbcDEwWvoMe38BEcCp/ohz17aSGTllHRTMpAkTnFSGM72AC8jIrBoBW143TtPUkKCp00wW+H8NwEsOJ79SRWyA29Sf0wIkz9BPRGMDJ61ekDOgdxAPUL19+/tunlxh9f/ny64uXOTW69fKuyKjH4V2q+C4ULc8cGCK6ckDOgOi6BBVSIUe3fBBMnlc/1iALPk3+67/SzqnC+qcvX+Hk+fn6Mv45tHDSRGDSFE7dAH/iOaXjxlncDK+TRdY5Q41sbtoKjl6qkS9h+Pq28junopz8dXz245uQ1xA0P359KZAKzujpry8/jXZ/fana8fvryKX88afXrOhA9eNP3/nUrZsArxmZIa1fvz2vn2wR4XfSOHhI/Svi+hZTF3x9+Z1x4+dN79FOtPLlNSli+OMb47IqbgA60AM//vTP2HoR8NIsrpt/i+/Pb4wj4PjIpqfiP316OPlvk+nToA+e/1xsicL6ZyxB5O/iPk2ejvpnvB/+/2+ssxiiFH73+D9k948WTP86+fmf2vY/Lfg0Cb6+LEGGMrsaC+7L5Ndvx50o/PyD//3mD3/7DbH+l2yORVt5Dw7fcgfGAaibb99+/qF+3P7hbz//0JYo11C5fWur7B/x/Ed+fcj5gwefVD/+cS2Sf4IpLDo4+cj0ya9F+R/Vb6+Ts5PF/vf79ZfJ7+tl/EwnoxHvQt9c8LuaqZGuv/PjTy+/IYSAyJrWezxGVf6f/znZxF5V1EXQTI5e0TYTFOAmzsGovBHF9QT9HWu7AsivdTzC2xsdyv8xwqPGCNN++T/eAzU/e0/UnDlP7PnmIfD59oF53z4w75fXiYEYF1UcxtDJJofFbvcVOiGAzSi0rEANqhuCE3dowGcERJ/HLyMo/vIveX97sHkth18eiB6/4dNBkEdsqtsMvI72mRGAT2s81ARAD7wWScgKD6kTxAhWPyG76yJDUN6MvqjTOMsmfowkomYwPHgjf30Zmf3yyy8uAuuv8A1Myclbl6hniOBDncnnz8iuIIvDqPkKgRcVkx9+/e2Hyf+d/E+rHsxHGTsE689oIA0fjQVVV5sjMhQoFFoEHY9o/Prb07uIDURtDcUuDmLwthhlZwr8d1cf14vPBM1MXIBcjNybl0XVPLpP8zqRg8mHvkjo+GjE8Kiom4kPSgB9AL0BcXWQOR+ehKjP1SgF62D4NGlr8JD6i1s5DxVzVOZO88tkI+xQxygy9N+o5oMILS5gjNz/kQhv9xGT6od6wr+zeJ1sx3yclE7llFHlPGUEzltcUKd4X46YOxMIuq9wbI5gdNWjON7cg4iQZ7xnSD+PMUftPkdI4Nfvsh80ztjXjEd/q77C+pn4TgUe3RypMkzCNvbHdvCXZ0qhdt9m/sN/SNOR0zMK/jMqjxw8/INh4Pg2DPxxjPjaEhhOTf5/zhujvgtJOojSwhCXE3FrHC5vfhxHpNHfb1MVavwPzo+a+T4MvEPJO6J+hVmMkqIa/vJG+fD+k+YNpdoKOeuwODz4o9AjP458H5k5ZlpVjTntfIXv0P0JueWBUyg4qIxRmo/Z9S5wfPquaYQMHa+/t/GHn5D/UOxR9k3K1s1QZgQA+K7jpUiraqyuZxhQmoLRt10Ue9EfrJog7igbEP8JUiJG9YLg/eG6bYHMRG4OqiL/Th6Pw1H5FlV/gmZQ8DoxUYGMSVKjqkQTzkiDvPDDg9UkB8jHSMUPD9eRU74pM46tTwWdMRZFjvL29xF4Pvye0g9dRvURV4SqDfJlN2KsD/q3yH7o+YwVUjYfi/Cx6I/hfto6+X2P+ctX+NDxA9ZRbWePpP3unAmqqbx+gOkITTWClxw8EwhlwqMTv74107du/aHLl7+b1X/8c+P8oz2e/hi5L5Ooacr6y2z21tLeO9orAoYZypG4BPVHd/s8dqDPHxX2+aPC/sD4zU9fJn9OuT+weGb1lwn+ir1i4yMt9sCYts8P8oXwmb98psanI658D/IzE0ZczQbUTj+azDsJ6jRhBcKR+K3p1GOv6lB7fKAsCsNX+JEIzzJBIA7DsUPWxe/K99FtUVjfovbRDNAj2CDZ/jidhWDcuWSj+jV4+QLbLPv0Ap0c/Ds7lhHxUa4ib4wbHVQ3aNppYvC4+ph8xos/btMeFYWgwC++jIX1aTJOqZ8mHwPnp8n7FuCxq4It2gP9PA67o0hEin580H7sAV3wgjZdzVCOmr/ta8YZ6zn7/r0SYz0hjRF616Mu7wU6Svw7JuhLGILq75nojy9O9kQJBORjT46b99qukZ4+mnAQft/GmkNlhNCxRQv+XgySU4Fri5qfP5r73X/fzSrebPnt4YbmbXP468s7Wjxj8BwEETkqy8/12P5mKE+RQHT9llHo2Z8fEZ8MEMChCQVxoAiGpTk3IDGMCTAnoFmWCwIC4AQ7D3zfo/yA4BiaIzkcd30XBwFBkIBhuABj/DnnI35vifltbPLxqBTAAoDICc8nGYKmKQ5nCYfzHYp1HB+bz1mMDXzUA74vTRE6Pi19s2x048e0OnrkafCvLy5DIco1VcuLt48w484Oa8lu01vcnfEX2zsnK2A/eGcVFk6jr8QzQV5SP5meiBQXKXPatUdBcbTmolVSJBV0Oj8oVGdwyn0BOuj4mVJyunKg8oK3+N4zZvruEGjyIpI0zIzxCs6PhtBrhoqvMPV+nG+3pZ/ZQ1gnbrdnacJSgxtJr2ZOfJby82Vhw9IJseS+6fOduRuIabChyfs+n54u5nUFLsHQ2PrsFJ9AHytb26XzTe6VON1c9pcBXIqlttTmPU1bodkT+iH3d7Aa5mCtEUyrVP5tPce9220/s68yHsdevB06Msq21+vJzmdZXpAnTRdXCXGW7jPB6sDxiqmO2K7EnKJVa4r5LZVWsbymVCU7KtfT9VCXPtQYnNLg9mBW62OkD2UIhCGTjhJmu9CLTSz35HTLaKdTe6pP8xQ/R7ezK4KksSl3rWhTLS1xmVSBMtccQUM5b1TCfKh0e6OY++u+NxgmEoc9NZ961xVhGOTpkuccTUvC0QK0ti3kBTbVLO3ialBowdI7g4yoHMPzleNqw1iq38qnwqjbDiMrtR/upnq4HshtF6zX52jpCk1IrA1Twg8N0EX8BEz8TBGHWQPOkq/iukzUPDVd0Uy5D6ujpJfcvcP2tHnHd30P8wHz5iyPFbGw1mBW0exsn/dElWp2A3aH7ELe4ktlTjmYX8g9HmubeK1Wg7+8yOzMdFWd6GpP26nT6yaSOinXLS7Xk0FWfZW8nTzGbC+z+1opgUBPO6UphQ7SJwqKsq4Rp01NGwy/1GZEEJzDnNiowSHepbO6q483oddxeNzEtrDG4O6W5vE6xrLcOLKbPGPLAV5Sk9VAiZdWKJMJvwvT2TKZScPSG8TDMZpFs9pbsixzu9l2H4pedWw5j7Hs3YaLZ/5GYU51orDWaVCnVunHhr1JmEH0V7AWN4XTq3Y2w7UkKDF9oILMWSxUjMn35foC5ozdrZSpR4einajL4KIXZj8kpictlu4hW51owjvV5y2hM8qSX1a2rAkCv29UK9rfr3PKUzomd5M7NKn1YW4H+sbdORsKI+WbIuHrMHGqrucidb4+QXmBJ0M6K2kVmoe5hZ/YmTCltm29mjOtdXNnIkVX2fm+Tw1npoH7lbs4t+3ZDpK9KK72Srgm8vPZMoS5fdxSWLEErKmHqwt1VW041cJmuSav08sGuNK+lK+7UCq2O0408mwnx9klnk/bOb5oNM2Y+V106jFOh8sdBlAm2FqFO8LUbM5sm4XQMLfEdV4ZYWhJR1hTtoQRQ7VOyVJQz7SFiau1XE2j+YC5q/4ipIoHr/wM2+3iYwgXwBswI+tzHs4KPjs3gZxqhIvPZ0W2j1VvmKV7Uk4quSjOxKy5wTkwj3eBhXFkYpHQsTXutoNhruuNUkcbW6liwQ5MOusVVz8tlvuG9q7iDnI1k67oDJu3S6XC+tvWso9mztqxu57Dk+RcrdN0twTWeViqGhw2w/UuJfHOSBzrbLgKp9iNY+NsZ1gFcwtuIGPDmX+YHsi6FhIP2vvDWmogPFzlhBqMpZYfe3I4FDcDlfZx7hmYuxAqaVkQoY9tTyI/g/R0qNg+JWqQe9ftQbq7OqwwTUtAxbjSjTJ0yw6KFbWgqYJfspdjla3S2yDOs4UVCK0kdZ6gC8eVTKjYMtV8XM9zP7nlp/NmfVIOEi7ScbmQrdPcBItNY0Mjw7DF4eTZJsyPQnGpcYRkeN+TTSWoWczcT9vpqmQ55RpwbMcgPD/fp3k9J6YAZvP5je3C1OH3x7T1/GDGloq86bhpYUnYTuEHRU0q7KZQwewa8pe15/czNwqPWnoJNNuaxRDeZ3Oq0dcD8Ha3W+LxVBmslgfKwcF0Y1zSUGQ6mTn1zRpuNgMmK/r5qtib64JFuRqJOMXEre/xK0yqeFjo8JIfXMlSrgelJHv+LO8waEi3o7+wcBhplE7uYVHgclnM/ZO0SE425m53anjTab0A/GAv8CALt4ote8WZP4oLX3blnMG1xtDdqbvaWKvr+hQeVtvguIv6Re+2qJOZK6O84isjoExSGmp1Vl9ve++yl2OpDY74fSkzeItR4SU4+fld4/vbUq5EznVmks5hboGzflLBrOPcRb0exH0pxUKUuVWa3KYk3m0Ji4wVIaX0W20ZqpkuFWJvry9dlNJpvoIZ2WdMk3DdUpmlgrKEjbbOo2q5B8lixWWJaRb3Y893CdKsSo+0Qh8vi/yGMNq3mE1/LOJZlxwu2nm27Ophhw3y/oZ2FmZ6lYPwttd9wew6QjBYAWpAOUFpmO8oh96H3dUOT7yfx9dzXOOVnWyREWmnKgmT1QOZau12yEMtiY0VnzFHDbAiaFpzE7meuG41cIFEOLu3d6z3NHk9BWhDF9X7TMKnvEQ2Nn07bLDsiG/CO+GSB1yN1Kg9tNtDJDC1VDcpLCQyFn1DorTzoSJWBsYUg5fMj5dDZK533VK8hyd3qPcqsMp9ZoZdNRh5bLl80QnhWe3tlQj3RRzbji3UlCCeOaJYkkejtWaNdEolZ1Fw+q2bixJ3mrk0FDGvXiUrfiFr+Yy9pyLLnIbrldHkq5TCJUmSHLu1bjdAmooakxSgZIxAJUId0NiS+1xVOtMNl0GarnyNc5eAtJDCxtUk2dM6GbglJaf2oi0ZMuuOmxMfXvfbONRZn2t4Vxjc5fSiZmq9GFZa36+yYd7erzknBZvjUmUlNEBHJT7g/Ybm6b11FJtLV1yXyRDtF+W2WwmZehVZ/Gy0ulNhBwm6UX81HY0xt3uBDzeUe4u2veIlkiswl6TMFiusCo7lyo2GU79Oc2VaqtVJuJeLZbfE+UFclqlYsUe3542q8sob4/u83S6C7H4AcAelde2vlL5nraydLg0pQDuNQU77KFfpYVnet0DFNnKqXKm0NqeDqIfnswEQGHFyNOgVRDlOrtVde4Wrc7onUjXAJXNNbb2EzBYUWzMuRhPH1aLZXTAut+PqVLhMh1DPo+90vwKqfvM17YbR2f7W8ziLrduQvOjBGgJ96SwJsyMv3G1JbH3Zuiq7mjiL55m0k5MVtpNbwkhK/7Q99RcYDCWDAIUrQEoEUytMQutQxvZAHesjXMlaJUhd4SlyYuiMEYcIfJKDsWoK1cylqMpZndc748pdNTe2paktXshppEy3B4yDFi8WjloJmhZV5VE6hbytlmUHQ7VKmWEgj3XDdxnvh82ZkPpyKihqdOoKF4vLckCd0beAdltCt9ciUx4kVuhmgtx7W1viyZBxzcCuWIkw7tIaqHauK1iOV4YaH9buzZ51jmVEC/LoJykFib7QWag2d0z2dCgV6aI4CJAqz4Z0ls4MnyxV1yOU+rTbXO7zMtrB64w3PTSidr5tMsG1azG8PCgngqdn3X1j1GnDXjm55rbn7U0U11cqm3YbuYX+DnM2SzafrzYVyBnDFxqbJC15uWOVe56UYdg2bZJ6Tt4ezvQyXZ8uyyxkN7ybUvthbq4irInL/V0RthvavG1tktgozYU/+3ArC9eEoM9TnV2KrgEWZXwUj6y4aqX7bb/ZQexy0CP9AIILaajHnroTfWRrjHQ4h+cBr+jUFSsXzlsnLCl135QVLfDpan8kVyvAXU86HsgICa932OznJ4XlLQdbw+DqsgGRtJzl3nvGxIgpe7bqaag2okE2y45rO/dq+auA68C5s8Fs6qBAbe62Z7OrvczjOMs5seSA4zFAXSgpqJxn9VBtD5pn+0QzIFjqCeus37cB9PexHcvZSYtbscTOt/mNWl9Vp+WJwmkH9da41I5oa5ld5DzfUBa1IK02Cvrl0cTOurLEAHMT0gvZJk1yseg847JrXQfLfW4TZ5/AF+cynOr7jD0BOq76aa0Mu10PZxxtBvMQjUumCjlITmWI0TpgODaBBLdnQKqz2RbfnRxH9nOH16gWRGdsV1hNniqW1GQ7ZlUdZZnX2FlknkxqofpbuFvsscHbg5PWLi+qke562xBpZpgaanXuvJaP9iZt0lKPbdc3d+HEW0ooAOORcKvPS5sX3BW5CMu6q6ZxoswdFnb4XrhmpIdPsdlsFd5Ja2/hcnFzh3st3jKcwHFLtmh1fvfli1qvRIOTijWrT4n5kk8XjBkzEu1sq1I1m7kvhTSRzfIsSIJp7fnydL8iz6vdhc9lGd4ujBXwg88TLmTXhnzwA2fubw52vzDrKqfzbcUSVkb5kh9srysyoos53ZOb+xT4XbsmJDdcaHNSxQEv3gjRbRz+cvep1GjLPaAHObskDTPMRMtXTtoiNTITVp1GHMlePXKWkRD3kDyg4eV0FPu5mrWYQDQhhPtdouzsLKt2IkHRd0Hp10JzuQJxNe+ompk5a2aqb9bLudz5/LRY1sYRa3qUQHdt0bU6qqoVmiFlIqsNjb8XNT9IcWPOcpzH/UN9FJPZTE0ijdmx/C3mSda8rX3crweTMtwpSFNCae2K9/xCRxt5fNivWZXX12e6X09Zzx02q34d2DePa5xtOz+uRMkfNnQSarNL7ydyhzcCz2JczYeN1VmQnTckOA+dk7BncoEvWgl1wkbG+5pZGurMP7spiarshldmFF3XW80G6+IaBcUdCIeNOufVdaSQGAg5bt3EB5HP5FmUYFWeYq48eLBYX7LBUa+Q27qCSORkN5Dxwln7t8IVuv3U5M6zRKPLjDz4IscwlcXp9701UDTlayiia06vVjeo9hkOOZaFl7bfXk3Wxzq0kS3ZiK1EQHQAsjs0Td1I8bBsz5zABnYTGI1Q2wnN45FwlXmDPpnsibjMGHaFOSFzQHheVXl1W6jT7bTb7bnd3OmiYIVm5rm6CItMqtj7oFumA2yjneIcVROJe+BadTetGicSCh2chPX+jqBo4STl/hCV0BVzo/aIUirbhjVpTW0bjqxLgOsMSdWrcCecEp1Zkyra69IhT/m7pCgrp1ZZpCdcFouVibYblhmq9916G6vXeckxJr64F/eVZNs6n9huTTDnleISp+Yw54bl3Lf585T06bSZr72bvhDbgayzVphPtYt7obcKflsOYgssblUZg866gzjYS28z3DxMtZRcs6tjNT3Lyn52aeAmJwJmflp4bJV1a33hQ7VzdWylnJwjm4oygbZM+93CWp+1/ASOvl1xm40F12sPV0zdv9fzaTkwg4FZ8wXvbfaLTCwXi8VfXz69jGfPzxPkf//d8Hik9792svh2CPj+LulxeAwc/8tD1pc/odPfPr1UXow0ejs/Rd4On4eN/+309PO/fAUxLh/eXriOL7365v2svXHC8ReGXmLot3VTDd/qImsfB7ifXty2Hn95of72PKh+eZiVl+Op9x/MQNdRXIFvTYEMatC3l/G3C8ZXOcCPneb9MnyeKH968QcUodirv5EM/Q1U5Wjq860GspB4xV7xl9/+H5yL0qaZJQAA -->
