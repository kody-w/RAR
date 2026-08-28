---
name: "rar-cowork-cookbook-demo-data-configure-and-manage-surveys"
description: "Generates and creates realistic demo records for configure and manage surveys in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_configure_and_manage_surveys", "rar_sha256": "53a44f7bb3f060e2e42eb81209c14448e6eab00875adb55aba0cd4cdb03fecce", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_configure_and_manage_surveys`. The original RAPP
agent is preserved byte-for-byte in `demo_data_configure_and_manage_surveys_agent.py` and in the RCI capsule.

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

Configure and manage surveys Demo Data Generator — Generates and creates realistic demo records for configure and manage surveys in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-configure-and-manage-surveys
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_configure_and_manage_surveys_agent.py` and embedded as the fenced Python below (sha256 53a44f7bb3f060e2…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_configure_and_manage_surveys_agent.py` first:

```bash
python3 demo_data_configure_and_manage_surveys_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_configure_and_manage_surveys_agent.py   # or on stdin
python3 demo_data_configure_and_manage_surveys_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Configure and manage surveys Demo Data Generator — Generates and creates realistic demo records for configure and manage surveys in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-configure-and-manage-surveys
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_configure_and_manage_surveys',
    "version": '2.0.1',
    "display_name": 'Configure and manage surveys Demo Data Generator',
    "description": 'Generates and creates realistic demo records for configure and manage surveys in a sandbox tenant for training and pilot scenarios.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-configure-and-manage-surveys',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-configure-and-manage-surveys',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'beaa1f31b4f3225b',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/administer-system-features/configure-and-manage-surveys'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/demo-data-configure-and-manage-surveys', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DemoDataConfigureAndManageSurveys(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataConfigureAndManageSurveys'
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
    print(DemoDataConfigureAndManageSurveys().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8166bOjRrbnv8K770PZj6rLjqTq6IhBgEBilUALcjmu2UHsmxB4/L9PIunesp+7+7Un5sNQUSUgM89+zu9kUr++2F0bFfXL1xfDt3NIsNM0jvwasnMPYou+qBPwUyQO+Au5Rd7WsdO1Rd28fH7x/Mat47KNixwsF/zcr+3Wb+5L3dq/34OfNG7a2IU8PyvAo1vUXgMFRT1RC+Kwq/37gszO7dCHmq6++kMDxTlkQw0YcIob1Pq5nbf3RW1tx3mch/c1ZZwWLdS4YLiOi+YVyOTf7KxM/ebl608/f36Jwf3L119f3NRuwKsXDsjA2a3NvrNmck+5MzYefAGF1M5DMLUcgFly8Fz6NWCcgVeeH0DPpx8aPw0+Q//1X0lv12Hz49dvOfS8vr1Mf3ZdDrWRD7WF3bQ+sIdd2k6cxu3wCjFpbw+TadquzptJT2DVPHx9rPxOqSihv09jPzyYvIZ++8O3l6KczAxs/u3lRwhY5NtL3U33rxOV8ocfX9Oi9+sffvxOp+mci++2EzEg9evb8/lJFkz8PjUO7lz/Dqg+vOv4315+p9x0PeSe9AQrX14vRZz/8CBc1sV1cpXr//DjPyPrRr6bTCHxb9H96UE48m0P6PQU/MfPdyP/DMFPhT5o/nO2JXDrX9EETH9n9xl6Guqf0b7b/7+RTuMcRP+7xf8huX+0AP479NM/1e1fLfgMBd9AeKfxFUSHk/pfoV/fDJ1nf/rkfX/56effAOn/kYxRdLV7p/AGsjIO/KZ9e/vpU3N//ennnz51JYg1387eujr9RzT/kV3vfP5gweesH/64FvDf50le9Dn0EenQr0X5H/Vvr9ABFBPv+/vmK/T7fJkuGJqUeGf6MMHvcqYBsv7Ojj++/AaKRA606dz7MMjy//xPSIndumiKoIUMt+haCDi4jTN/Et6MYlCcmntu1z6waxMDwz7ngfifPDxJXATQL//LvdfPL+6zfiJTCXzzQP15+6h9b6COvT1q39uz9v3yCpmAelHHYZzbKbRjdP3bNAGUQMC5rP3GBxM9yBla/wuoRl+mm6li/vLvMXi703oth1/uVTR+VKodu56qVNOl/uuk6THy86deLgAG/+a7HWCTFi6QKYhBjf0MLNAU6RVUuckqTRKnKeTFoMYDgBjutIHlvk7EfvnlF8duom/5o6wS0AM5GgRM+BAH+vIFKBekcRi133LfjQro06+/fYL+N/SvVt2JTzx0UOOffgESbgxNhUCedRmYNuEJKMO2d/fLr789TQzIAMyCgBfjIPYfi0GcJr73bm9DZL7gFA05PrAzsHFWFnU7wU/cvkLrAPqQFzCdhqZqHhVNC9Cu9HPPz90BULWBOh+WzCfIAsHYBMNnqGv8O9dfnAnXgIgZSHi7/QVSWB1gR5GCfyYx75PA4iKPgfk/ouHxHhCpPzXQ8p3EK6ROkQmVdm2XUW0/eQT2wy8AM96XA+I2lPv9t3xCSn8y1T1NHuYJJ0SfkPvu0i+TzwFoZyCYvOadd/hEfQ8y70hXf8ubZwrYtX/HeyDKAIVd7E3A8LdnSDVR0aXe3X5A0onS0wve0yv3GGT/VYswgTk0oTn0bD0mMOxwFCOh/w96kUl8RhB2vMCYPAfxqrmzHmaduqjJ/I/GC3QED2JTCn3vEt5rzHup/ZanMYiRevjbY+bdGc85j/IFhPdArdjd6QPBgFknuvdAnQKvrqcQt7/l7zX9M9DqXsCAr0BWg6ifgu2d4TT6LmkEUnd6/o7vT+NNmoNghMrOSYFZA9/3HNtNgFT1lGxPb4Co9afE66PYjf6gFQSog+AA9CEgRAzSB9T9u+nUAqgJTBvURfZ9ejw5EUjhdS6QFrSp/it0BPkyxUwDkhS0PtMcYIVPd1JQ5gMbAxE/LNxEdvkQZupsnwLaky+KDATJ7z3wHPwe4XdZJvEBVXuqst/yfqq7nn97ePZDzqevgLDZlJP3RX9091NX6Pfg87dv+V3Gj1IPUj2dcPt3xgHxV2ePsJ4qVQOqTeY/AwhEwh2iXx8o+4DxD1m+/qmd/+Gvdfx33Nz/0XNfoahty+Yrgjyw7h3qXkGdQECMxKXf3GHvy2SvLx9p9gUw+/JIsy/PNPsD9YexvkJ/TcI/kHiG9lcIe0Vf0WlIjkF2Aos8L2AQ9svS+kJOo9/ynf/d089wmGptOgCc/QCe9ykAfcLaD6fJDyBqJvzqAWTeKy/wxbf8IxqeuQIKex5OqNkUv8vhOwID3z5c9wEQYChvAW9v6t1Cf9rapJP4jf/yNe/S9PNLbmf+v7mlmYAAxCwwyLQZAvkD2qE29u9PH63R9PDHHd09s0BJ8IqvU4J9hqY29jP00ZF+ht73CPedV96BTdJPUzc8sQRTwc/H3I/touO/gI1ZO5ST8I+Nz9SEPZvjPwsx5RWQ2PUncC8+EnXi+Cci4CYM/frPRLT7jZ0+q0XT2hNUx+17jjdATg80Pp8h4D6QeyCdQHB2YMGf2QA+tV91ABO9Sd3v9vuuVvHQ5be7GdrH7vHXl/eq8fTBs1ME00F6fmkmVERAqAKG4PkRVGDs/7KHfFIB1Q50L4AMRdgkGcwchwhQGvVxn8R9Z47h6MLFSJKc+7RvOyg6n1G251CU7dio65Gu56BE4LuuD+g9AvRtagDiSTIfDXxigeGuR9A4RZELbIbbC88mZ7btofP5DJ0FHgCE70sTUCqf6j7Um2z50c5OZnlq/euLQ5Ngpkg2a+ZxscjiYM9OsqNGzqKmA6a5LJL2Jh9KjYD3nDXzdmieUUk2epfz7LRzuW1nJGvDXqcx20o65kuWjhpBk8ADtYJZUVLTTVcrI07enKHf9e6JR8YLejosGb7ANFNGjpVcHre+UeBK6dab4807VV27cpH9rYjyppTjyC0PktGacbtAEJugDCz1040h6bB6KjM85SnR6NJ1WiZDexQ2u3nLdFrkGUdm5KkSLw7sbIwj71B6BjWm/rxs2XNl7VRldausub6jNXMVI9q4GrzrSNGbZgF+ifn65nVYUaJhEUlD3doZpp6O8aGspdvmPKyifMHckMM5clczm8XKdld2qpG2Te50G+NMV+cwTLF9Io6HzRDkskra0kFaVV29l4dmLYeNuksv0UYvS0c+LFmfPlSnwybyz4ZN991Fbr2LadNydvQSDFnRR6qslHyIOs28EOx8rDVLFdJ9ljTJcC2WTFL6A090u00mHWdHLc2vOe8xbp2k+HYt0UyFOLlkzeTTEj5y2/MxwYnjTq0bHbbPGDPO9tXBiOHTvJVS8dDt7H5wUXV09f7G3tbO0uuyYmH3XozKJZmUNRZiRmARArlbEXCBNlcpSsYiNYRunQwZ64hbroJBd965c9yv83yrpOrILtx51/kIumm8imJxmzBRuxH6tXrInOuZyhTSu2jrMMbdTo01VafS3aFuMB4+dUtqT/mbsD3yncbqtbEZ3WNNVlIgnJQTad5unrTJ5NUiYnuCbFwzXomrWSUIVjkzVwmS66cDod3qqmbHzB+jpZsFKW5lCqrwNi+fj/7+gCkD5uzUis3xrK747FrxdNgSXlnJl4V2leeCOD/0c/Yy1/V5sG5v5YYVrmQwcgIdGI5InwMrX6L1pUbg8LI963Eby96aSNen9Ixi+0GijuWh2p2Vi1cqajzgseDqVir2vZ3pDIUaQ3pNJXybuSjaHrSQpjAxUfKGGvuwUKjdETcvJ772uQ0jhkRcrTPDVtf68kisx5K3NgpWxJ0V0+x+Z65S72iRrrm8kbPcldaDdiUcPzOdzjp7PLWRCm+f8IEhg/Ymnp1B+PuCZpSK21O0nvl22SZu2mLCODb2xR1SURtEWkd6zXUuuzHcR1Jw6Au1a+rO2ViBmQjbdruOMywxD465dV1TsaiaxVhcDSVlE0TqiCxve8xEq2C/QwzR5BwDM3S8UEq+xHkGLUSNZahTRbTzmtOLFgVhUNwUJwjEUz1sDqtOW2HDuEQ2+7IlDJwoy+McW1SGH54Oh/oGn8VtNtZigp/Z6kSXnp02pb6ptU6KvaMdMWuPCtuSHUntKpnnvHG2tLtNTFjKgpjzWnh7WZkzGt9JqVCnW2S9z7aqcNht66vXdd4CIQ2TA91gdERDEET4vr/Kcq3desKQAj7r1qu6GpVMsSk8XUogXc/egVY1SbnJUjfuxsRbZvqZRuRjg9Gu4yJ8nI8pM6tMx88XfjqgJCOeo3N6S9WAWV5gsrFhdItXmI/OGo1Z0Ox6ASNz149gd6P49WWpLAYvjdTgiNvpkg71y4ZXrgtDuJbsZetyGuV6o7JspErZG6BFXLf5XkjyDS05BLnFFWN5SRIqSOlFsGyGEK8qbRXQlZuNs92wW1JUmjByqGp7EN+bK7aGhVXNWEcz5XuWL5Wl0FY3x8my2j/kF9G8VSxjyGZc1ztBypc4P9w27m4oI1eTYjbdLS+5bVvrFt3NDnXUE6IesYlcZSssD4/7msOPI3ojTmMnKzdOoWl4dFLay+sB0QzWWKc1b58XBKzYSVJQ8tUUALze1lq0tDy/dRSOgPFQlmZ5phKhtY43q7OhpyU8Ny6we81X5NwLbia1RSQpXB4WPmzP4oRZar1F71GVyzoX1OX6sh/og0aHfa8uEBFLhhjhrOUKFeruFKpq0e3MA77b3zAXRkM+jRVddbHKOoWSsCENjuuSzYLVjUypNNqKUUuct5xsLrvt6eqkexOmA61rFu3hOseT4SRtZmuDa2cKl5xmgiJVVVyysAIHxTCbH0vHZc6YZ5cqhW6O9q2ga7UTyXDLH9OLceqSppjp/iVSyBEfhZOg84Jqg/qxy2c36aD5DerV9FzcXzPU7hforc04Otqleyt1byc8qBBX9sm+PyUkeSqAX2O8vQyzVOkq1t3pmTZwyMEM+aidVWu43Gihg0srsk5ax9yp/AVXUBBsFbGSJbNnXDM4Sva4u0gOfziqdtXZ7QWWk0hS4n1NCsX2XLKCJTecFa17RQ8vnZQOguFt8ObKzVb1flW4jZMVdLp1lGNDDujN3TDs3tKkmaLOMaK6Achs1+dlj883EnmOdHHmlGtqeUUTQzqSq7GRTovsnOlbAiUdlGLJs4bKNqBPJcZV5VFsQGsGqfDOTE6xdPIv6DZiqdlwtDwRxDx94sXSzOS1QSzYC08Uw76IZYD/V3SZZmxNXNxe7XW2ldXlthnMLD6Oy2tiHA7GbbWKV/h2xmpgP7R3oxVAy7NIdptWRvBIMjidGbT8hGSMTO7hWZDzqNusTMFlNieVxrJC0dAy32PJcbc/LzTxWsMi6EcC56onGyaOB67bbpBaQNf8DQUxBGdYc+WPxgyGlS7F/Yt6kdGzVi5kx6uQ08qPMN7Qw30Fz/x+tUyY4rAWxm0i6rWzOQxKGwbry36TVoIU2XpBNsRZMvejhWVsxp3W6NUMU+mqYLcxzg2+tSxMWk39nhmWF7kZt/saK+pAs71RKt2qgG3KrfJVGjAkvF1hbK06w7FQY3Tfk6IpqKtweTO9dS6LXFnG8lox56PnFqxZMlzWyxuDcxNj7e3nQ4Bxl7x0S9DFt5szSJtkHI7plWAF0s8SssBRQG6ZjHqlpQEvx2UOcJ/ze9DIGPxF5JUsOVYDL4dG27tnz4pQTZZt1srVbB+isjHg685mdIHQWEW79lKSe2pYZgsp2N+2Qius5PPNzdqqmp+T9FgT0lmzrutDirRnDk4UmEfJkSZW2ha2tYA5wHZr0VngUqi2OME3mTgO6bIRERmMYufNzvUurXgy6D1dxTvRH86wVOaEaNqmgqz2217umlioKEMxshWwSrgnvdBSePdUieTYdK4wJJLm2Ad8Had9mzOEu05VhCoUId5RO2uYj26jU8nhEsxEke78vJqNO/YQxWQ8SBZR2mSxObNYFRJX1mFmw5azLLFCRabncJtSei83k0TYcyW2FUv+KGNa5SoNCFowvNQve2UQyNgMWMp0243ArkLaUZxjCyubDTVyRMT3ZUKbPrbMb6I3m6XOzQgTzt+AjU92GoP1AdVU4M9tn2r1ZctGqbSMU085uwHI14ItU2LUt4VP3lIKZQNTGZktqsvpKbKIymwJH8WLjSIocw2kU7ov5GuklQeiqCiMjlDnsC6CdR/TCxTZhcz1IveghtPKWUXdY170J/cM/EqtB0GpI6ugdLF0UsPfqpsZx7iNuApr5cIJ+/hq1btsZUTZoNjn4eAfzboLTrYkAEC3GaZl9nQ5t0lhLG5IcNwuTbYBUbfkEXws+vkxORQ+ts18b+jnW1u7kXtltkVHOgw7UDbTMUXThe7DmzGhjSYDu2DtdsOwhbc/jQazFhKhuySIzXZRpQ0rCcUVPc64tYczokEY140eyPMgXggFJS6wU4VTKE2kQ9yCfOrmGmfMOHjnEemsW8adKIPmtesbzsVPiruuzuze63ypiPB8m5REWDieyI/4ec5FwyaXCI9zvZRZeAW268YDlZP8PjkLtrY/DREfXpF2zsL8Fp0r6LLWN/ScEBhisVvs+saKL9eQwPS830u9TGc1d+oMBOxaNZnbEVvegZHulmoIcwwbPfdSx/fc1XlNlLt5EJkVO8PVRsU6bUfBMYIgVh0kLK1UA4o0c+S2n19rhzjpoNJ1iYicxWtpWibOlrG46pJiLuq73mZn8iw+sIeRu52RrTGYy1DCgoHuM3vNmZdy7HlV09c6SIRlw98GkWrGENguy1J8lgYgAxl1oEeVKGx92S9p5GhU577iuhM2G3JRU3rJPwvGJk3nnLsnsTYbNi7Xr2auamJL+OqFnTYf7KV182Ok4/V4PpPoayLPxc5FDIGtlyZQjjSpJHD8ZTjwjqydOXchoCW6WNG0uhgWIqxVyAFZWMgsiiNZi1g4jI+hEQ9LFEZYkhbbXB993Ipnao3h4erCG2p4JFZZW8/wUzprhMVJtbExpCyMvhH86M2Ri3dNFLzf7knJ6xbmzYoVhKfM9ZaMrNyKgx2OhlfrItBnJHPK3OdDRh2PGxpm5/u2MYrrAZ3Pr6SKWlw/xrESsM2NYo5EvPcRRmMyBBWlI9CdhOdLqhCYNhwDXquHohyRY04gMCzyVtSRHGatLGWRt4v5wRWTXb8FO7ie3S0xmFIbkQ17fG1J1Q3RacGmL06yEWfw+cQaqITy1yElzCOhe5QXr4+k6cA+2MxuunO9tBZrbQiO/nAjEGmpCdgw6POKHFdBHWtehg3dTO0I1u0iLhIxUtkgHelbc5ezetSDNZEHNHrhfMMdWKRWme771TBTrOXQH7nz3nO7tm9pMTC6ocTKru3mJ6MZOP3U1VGsybnLXnfonAc7cIY55Qtlz/tx4OW7cLfVEwvJbmjQbiXNJP2r4e0WCYElKaX47Kz16milsyzaEZ6m6Re/aQkCDlT8GCxW6FqvszTArIgJZtccRisxYxzMIx23CpQjBpP70zUVIio/cAtiNh8a03MuRKRmwWk2XyGwd5Rd9nLVZrGKLeQTaGOU5OTzkhUKOnc4eoF3QZLmtKTVShxXdtdZHczU5DXaIEJZCGEC9hDdNS4ppFvtp505od5ovh5LvdlldKuS1/RQVleGzlc2alhWORcXXIySvVooXCnxgpNFl2i8oMpMaU97nDy76vWI5zMcBepmInk9hDKDXrSZSGh+yS8uHOlrHNlW9pyjqIhKOGvN15Hkyo7FU9dlugPbsH2G5mqokG7KJ4KeGrgATJmK26s9pmQauuR42YDUxHqv4YIrYvEd2/upxsKMuQ+sUpUxZBWLsHXksG5LBV5DGa7LufztOi82J69ar8C2GOabzfYKGmU/Q318ljPzsUx7XWecetPb0riitpbtFNL6yOZ1by5PxG6d7/2ddysRF5YLxHSxGy6YaIcdTQwbRAuBmcU+lFZtI20Z5uXzy3QO/TxN/osfkKezvf9nR4yP08D3L0z3o2Tf9r7eeX39q4L9/PmldmMg1uNItUm78Hn0+N8OVL/8e18nJhrD4/vs9FHs1r4fw7d2OP1no5c497qmrYe3pki7+8Hu5xcHtFC53zRvzwPsl7uCWfk4DX8qBO5tL4vzePp6+tYWb48T5enINc6nrz2+F39/DJ+HzYDAAHwWu80bQVNvfl1OKj+/eQBN8Vf0FXv57f8AflkITd8lAAA= -->
