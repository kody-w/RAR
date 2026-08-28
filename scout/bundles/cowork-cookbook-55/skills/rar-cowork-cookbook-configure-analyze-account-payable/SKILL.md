---
name: "rar-cowork-cookbook-configure-analyze-account-payable"
description: "Applies a bulk configuration change to analyze account payable from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_analyze_account_payable", "rar_sha256": "9a6d355cbe7a8d14f8b8dd980820c460de047c7675eb488fcad373c4535ee2e5", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_analyze_account_payable`. The original RAPP
agent is preserved byte-for-byte in `configure_analyze_account_payable_agent.py` and in the RCI capsule.

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

Analyze account payable Configuration Bulk Setup — Applies a bulk configuration change to analyze account payable from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-analyze-account-payable
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_analyze_account_payable_agent.py` and embedded as the fenced Python below (sha256 9a6d355cbe7a8d14…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_analyze_account_payable_agent.py` first:

```bash
python3 configure_analyze_account_payable_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_analyze_account_payable_agent.py   # or on stdin
python3 configure_analyze_account_payable_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Analyze account payable Configuration Bulk Setup — Applies a bulk configuration change to analyze account payable from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-analyze-account-payable
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_analyze_account_payable',
    "version": '2.0.0',
    "display_name": 'Analyze account payable Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to analyze account payable from an input Excel file, with validation and rollback support.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-analyze-account-payable',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-analyze-account-payable',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '1da31eed370b12ec',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/analyze-procurement-and-sourcing/analyze-account-payable'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/configure-analyze-account-payable', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.8, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class ConfigureAnalyzeAccountPayable(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureAnalyzeAccountPayable'
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
    print(ConfigureAnalyzeAccountPayable().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8VaeZOjRpb/KmztH26vuktcEqgnJmKR0IFAnEJCuB3dHMkl7ht5/d03kVTV9nq8M47YiFV3RQl4+e73ey+T+uXFauogK18+v2jASpGtFcdhAErESl1klXVZeYW/sqsNfxAnS+sytJs6K6uXjy8uqJwyzOswS+FyJs/jEFSIhdhNfKf1Qr8prfEx4gRW6gOkziBfKx5uALEcJ2vSGsmtwbJjgHhllsCHSJjmTY2sewfEiBfG4CPShXWAtFYcug9eo2ZlFse25VyRqsnzrKxfoTqgt5I8BtXL559+/vgSwu8vn395cWKrgrdeVk99APNQgHnIlx/i4fIYagjp8gG6I4XXOSi9rEzgLRd4yPPqQwVi7yPyH/9x7azSr378/CVFnp8vL+M/tUmROhgttaoauIhj5ZYdxmE9vCJM3FlDhZSgbsp0dFQFvZn6r4+V3zllOfL38dmHh5BXH9QfvrxkUIW7A768/IhkJZRXNuP315FL/uHH1zjrQPnhx+98qsaOgFOPzKDWr1+f10+2kPA7aejdpf4dcn1E1QZfXn5j3Ph56D3aCVe+vEZZmH54MM7LrAWplTrgw49/xtYJgHONw6r+l/j+9GAcAMuFNj0V//Hj3ck/I5OnQe88/1xsDsP6VyyB5G/iPiJPR/0Z77v//wfrOExhDbx5/B+y+0cLJn9HfvpT2/63BR8R78sLC+KwhdkBE/kz8stXTV6vfvrB/X7zh59/haz/KRsta0rnzuFrYqWhB6r669effqjut3/4+acfmhzmGrCSr00Z/yOe/8ivdzm/8+CT6sPv10L5enpNsy5F3jMd+SXL/6389RU5jdX//X71GfltvYyfCTIa8Sb04YLf1EwFdf2NH398+RUiRAqtaZz7Y1jl//7vyCF0yqzKvBrRIDjUCAxwHSZgVP4YhBUC/4+1XQLo1yocUetBB/N/jPCoceYh3/7TuePmJ+eJm9M3LARfn+j39Yl+X5/o9+0VOULGWRn6IaRAVEaWv6SWDyBAQqF5CSpQthBO7KEGnyAQfRq/QKxEvv1T3l/vbF7z4dsdOcMHPqkrbsSmqonB62jfOQDp0xoHojDogdNACXHmWA8crj5Cu6ssbiG2jb6ormEcI25YQsOzcnigcpN+Hpl9+/bNtqrgS/oAUwJ59IlqCgne1UE+fYJ2eXHoB/WXFDhBhvzwy68/IP+F/G+r7sxHGTKE9Wc0oIZ7TRIRWF1NAslgoGBoIXTco/HLr0/vQjYpbGwwdqE3NqpxMczOK3DfXK3tmE/4bI7YALoYujcZWwtEaCSsXxHOQ971hULHRyOGB1lVIy7IQeqC1BkgVwua8+7JNKuRCqZg5Q0fkaYCd6nf7NK6q5jAMrfqb8hhJcOOkcVjgyyfHQQuztIQuv89ER73IZPyhwpZvrF4RcQxH2EjLa08KK2nDM96xAV2irflY/dFUtB9ScfmCEZX3Yvj4R5IBD3jPEP6aYw5bOIJRAK3epN9p7HGvna897fyS1o9E98qx1A4sBFAoX4DmzVsB397plQVZE3s3v0HNR05PaPgPqNyz0HmT0aD1e9GieU4XWgQQ3LkS4OjGIn8/04ed823W3W9ZY5rFlmLR/Xy8Og4Lo2ef0xYcARAYFo9quf7WPAGKm/Y+iWNQ5ge5fC3B+U9Dk+aB17BWnchQqh3/jAJoEdHvvccHXOuLO/O+JK+gfhH6Jk7YkETYEHDhB/d8SZwfPqmaQCrdrz+3tDvMS3d0XSYh0je2DHMEQ8A9+6EOijHOnsGAiYsGGuuC0In+J1VCOQO8wLyR6ASIawcCPR314kZNBOW2D0K7+ThOCZBLdzGgdrCeRS8ImdYKmO6VLA+4awz0kAv/HBnhSQA+hiq+O7hKrDyhzLjCPtU0BpjkSUwg38bgefD78l912VUH3K1YOyhL7sRbV3QPyL7ruczVlDZZCzH+6Lfh/tpK/LbbvO3L+ldx3eAh1Ue33Pxu3MQWF1JdU+5EaQqCDQJeCYQzIR7T359tNVH337X5fMf5vYPf220vzdK/feR+4wEdZ1Xn6fTR3N7622vECKmMEfCHFTf+9ynZ619etbap2et/Y7xw0+fkb+m3O9YPLP6M4K9oq/o+EgIHTCm7fMDfbH6tLx8IsenX1IVfA/yMxNGhI0H2Fjf280bCew5fgn8kfjRfqqxa3WwUd7xFobhS/qeCM8yeaAN7JVV9pvyvfddGNZH1N7bAnyU1lC2O85pPhj3MPGofgVePqdNHH98Sa0E/Ct7lxH7Ya5Cb4xbHlg3cO6pQ3C/ep+Bxovfb9nuFQWhwM0+j4X1ERnn1Y/I++j5EXnbDNz3V2kDd0M/jWPvKBKSwl/vtO/7QRu8wO1XPeSj5o8dzjhtPafgPyox1hPU2AFjP8/eC3SU+Acm8Ivvg/KPTKT7Fyt+okRVW2N3Duu32q6gnm4zYjqMHaw5WEYQHRu44I9ioJwSFA1sg+5o7nf/fTcre9jy690N9WOb+MvLG1o8Y/AcCSE5LMtP1dgIpzBPoUB4/cgo+OyvD4tPBhDg4KwCOSysuUvMZo4NKIt2MdKjbdp1FzRK46hDzlEXoCTlUHNqBmySpj3HcgmKcMgZMQMABzPI75GYX8d2H45K4Zbl0A6Fke6CsuYOIFCbcACGYy5FAHS2IDyaBiT0z/vSK0THp6UPy0Y3vs+to0eeBv/yYs9JSLkjK455fFbTxcmyz1NbDYRJGU/6npgrhJ7r15q0sUMTRE2LMqWaXyWt4TfDsh5UA60vejzRG8oKt74356aVMLmmdeJeYzWWOFRSO4l1e2tWUdKtosoDKm70ozLn8XM/1a/75HxOeBPPZhsrCVQhzeNbcTqJQo6ieRodN7ERxsZG2hvEdKKa/elkbU+bE3+t92yNns3ybM11Z21z9XQJsMRiVWsnFOkuJK94sip3emAW3HZCnMk4O0stoM19IuCBuuHLQ3kxm+JQngV1Lt0EakEDbxfjoBEE+rihF07bku1mTunhwbytDva+tzCxrPuToHcNgcXmtcr5XGh8c5pyvh2WcBLUiQzl4TQwECkRr9bFIWb07bGxzHNjBLNFLpgahhdJHRcbsk7Z7FYmkd7jVaAJsxO2xqP4XJ/P/WpxcDPD1dcnasfjuFPMY8OVvdMZb05aKhy52DItW5q7WSRvp5qSuGFxOkoLwi2dQ2QyvJ7Hx6Xg2PIZN8pW9nlnPhD9Jlgy0nSY89Z2mHU2wWMuWPRob8dZme5pYgtUp8BKqFqDufy+0cJaO5m+nVU7rKd7zl6qaELS896FVEJ3zctZiGrHnMCHq07gNUrnvGLEZJpCg7ZFd72tsJ2IMXP83BBpILgttyFRlmNPx/Zm71siXbKUbCd+XdbmIJ2P1owb8NsiS9gdjsdraXNqBbk2Mqcq+YWZZCQ/7WQ+KY6HTamkfRgtcL/q1O3udnJwqdHbLj3GZN7IvCGt96xH97225rYlofO1e8Q37G3anCdlc/Kp0yKd2Xu778NbFd6kW+KsI5c3qpJDe1HB1LcfDHjl6agY1AAnaVTuSCEmt+yE2+FszM/QnK7ZjiUyMr1RM7vNdwI3A0WO5f50jc2NrkQLvDtbaGniTq1pe6PAijpkg2C1SEi84tXq0rOah0e3tgt2u35bqfIlV0HsLvEhj5xztBnOvZ8IuSsE883AEkq+jfZsrF5TrU+AFh680L1qRrgd8CARN06/O1VFkQgH8iCSZOKVuL4ljRNMbnAQ5fMhqsv9YW1p9nK7LrqeDYbVLkv33GJ/ndxuRh2WVzGJZSDSKCFvVKOcBpG8aC/JfEM3sx1dDh5D2VR66k1KIB1u0FGHO9WXK6GiQhqFaphGun6uI3NJVGWXzKiAnJvDgk9urEwEhib2QdWvWELdO9ZiYD23nGKz2cJdeRPVxtF9LMotcUv7/ek0ETfXlc9OnVI/U/nRRumUvkzEnNUMiSdIIouc40kONb1Wip62Da2xC5mHk7edURsnnwno4C+MDHgKhFiuik9mKkdDqMiFCsTdKTxFtNRr6l4EHCu7bcIkONy4WWiDGs1yuU6JLcedmVXVYSRnCXgYzxchLjmHPRpKJVdWe2tOs7ejGjgz093S2LXSL8FiXW4VjiJlHqCMQRLRpEko3RRgLPn9rZyHi26ZeWipq4d05XAzVTRUNpCdBG3n6emI84LZnDZAB1vZLini4k1mfj+Jd3TrH2/VXmUSPvTT83ziikHlnTUHgCKRcW2/m15O/WBEURzk5okjlnRoCIS1Pk0O3qwxoiF1mGB3SMzBjcs2pXApsRhsaUIMU496b9uS14mHQ8nQysac+/hqtvL0ULCLQ9/mnnyLro0m0eLuvDpjRilUK6rZ7MJ+wui3/BzzzOEam0kREsGOX2CkemAbUe2IiGtjDs1RsaG6tIzS9nS+iPzVZs/CTdD58FzjbQKh7VRc3LVJpAaBUfItnFiVcPGvjmndtobteH1+IiU53cZb89ZJW+602MbmgC2mnLhhyrbcGpepbLPETBaOAbnS0ikVK17ZXZ1ilZGqqJtuAYBj98N8STHKQg8CNinAUHGFlm/IxnUvuralbh3ZW9r+eMGataaxunHrNufK3ue75RXjnHTXqZLaqJsFNHQ+Y+sNnWMa3Z5m6WlP60EbUfuA97MpBjFKF51Ilvqi2MLNXnWzLyFzW9bk5rzm2FnMpz5vS4QKpFWk5yAWjrl367zNPuyo8nIK6KFhd0Z/RhMiL06LzJixgs/IK5wweQzVXX5qO8qFTRz8UpDORRkOuTHzhFp01wXdCji1ufKHfh7Y5DHmHKd23P6q7XMK8xaErjjVNixSibEP6BYDsAwU0bJ7nj3vj0vmioepGEyZDjbQqZ9er8rqIC7pa2AaBl9sZGpRUJ0E28DkfBgILCSdrWiC3BJi1HZU2FE6jp6RYS27liwp12pV+GXalFaTJNuDvHN7ciIWdRqu8SNXR2HKmjmfiY1G5+7JwSYJbYisZC2UzNGiflvw5+NqEOmlsdZodsXVaZYvxcRCWbnTcgWcK5fZrqeHDGuOZohd+T4x/A1GyOp+px0zr1mczWYV5aszeaL8fr9aM3LTbNH5yeU60rwQUuh2GLFP5oVyG3A8KbcJb5SK2Mzl40aXFuXRUpO5ckQJOi1UTbm4kWNFzhK9pdXi2Bqi0tHFykaD3aoAKH+4gWivrTiKD62pSqoXXvaWx+UGTkmul0V5eBRptemoXsjs2ArDo8rsNnsn2Z+qi7Zk1npiONcZ4e40eeD3oSLUSw+dGzCRMCC6xK2y4K6/X6bX476eYDdOlHC+0a/shfUEQamnNAl6YrvJO9aZKMeKbbWS9Labat5j84UMQmzWVMb5Nl8c2pwANzHkQxg8tswWc/G6AalNrng2pBcYrWBs7TOBLwZ+RTMRwzenWcViazvaV0rPSyqdlJveS7F9IpoK4eBnW3dzm0H3lF+sp/2mCwTrIOVhMS+dzmAni6usFGXa6th+jl2ak75hl5LLRtqO0TvG45lb08xsY1snJr/doJOd0vCtjzkm3XVzPQ1MiW2jpXjzb9KakexVteNaU88dGvewZbvOuUW9jXDldshbblc1vDdsTt1wvJI+gUZ7Xu1dRWeaBRdEccvvr6FrroJlZjizMiWv6wWDp5ni9UZRJUW2swy+A5jvaLh5OOqL5kCGaUXiLqqG8SQwzUgxLVAN6VLW1dTPBsI1zEgv2sKSTslCKYhhm2/dli1Rf+pxx8O50BNip0oW67LUbCi5m81sMUeZbndnopjjdGxRaY9BY+YKXTiEsriVFpBgiDrdI/MdU3Jts8XxvRns1+dr6tWrjTg/0low4w7HzKL2jsr4RjO/hP6Fl4Yq1+w0wQb2qjciRq7oZcuuvQU3RUNmX57hXBfnU31exF5XzZs95UzZzSy3+HwllXiuq7q6zgILs1NiKVwpfrbqmHOcS3NGz2LcDAspVSg025klw8IgnXUSA2Uas/raM86MQy/iS7rXd1HMW7dYVjLAdX27kpY4mAdClubrkokT+7hhjtVEGtqZqWuxpLLOzlIH52DPz1IXOamvRasBJZjLytcLI0xOO7diTkyRuRXGcsfb9kDt/RV/aX3hpnhDJ2elLxL2dWqhXLw6F2vPBYMjbMhekUI7kTK3ycSKizfsfrv1jCiduGtmtZalrugzpwgyX6oDxQx1jTW3qz6hy8VORBe5U9h7UTt3nSEw2IUvuc43lBbsq5vGK7fZSlphUiOIBH4QsvWBPzQWs84YFidWEapTBVVOFUzJLYa+GsJWoC6T5KJ1GqzsQtv7+HbjR0dU0qIEqw+TjJPbAnfm2WkZhKlxzSY0F+Gm6DoKejqQRRhnVUvmUjMVdLYQCfqyYZaXGZXsLEJujdIpaSOa0LodLWbnDJ8SsNVQq0l/OU4tY9lJi2l565100R/cYSbSHGz8Qw3nMLgPUDiVqggwSc/F5ahZotT5lrznlNMhOge916pwNGq1y2JKuTo4Esdk04XucBgcLw1Yp/cmFMaiqg32CdYZHEH1XgFd2PrOOuVUgvcWTLqrhW61TY2TTpKyFpyAwCmGu3OX3da7XeXFLRNZkjBxIiEc2t/OViClzbkBFlPbXdhHXWfTdkoNB4Jk6q6samknE/RJFuYWiyly0pb5coZDK3RMWfilyVaEqqlqhtr1WhakhKWoE3mdZly5z3xRmtmoSna4n6bp9UAHUievjJtab/KjbFXHK0XUTRITt+v0wG40+yQZXqqjQAiNUjT5WbTKWgwo7cpxTJzRbvxEORzazB4itiYHUejG9xE7w/XlGTGXg8ZpMsJRZ4BY7/qJW7sEvuyKKLXNcqv72HUSB46QzXKin/robCVuWilosqiiz7KKg0BxCG0iBC3WUme5RS8VPyvQFGVul7Uxv8g8Nd9pmYROPb2X4zLFy91pfb4ou/NGdxNzUvsz5xzoEeZapMDYC42KCs9pSXo6Uw/OerZl02nr0rgfyMHWGNCQOy8GLtKPrd5JQg/8GscmqKEdLjt+E3ht1mxKsM67vScrKcfWg0r2sZAyqnERNAFbXcAinB+S6ZKSrMm+xoj0sFsD/hQJc8YIIoctaM8T/Q7Iu+rUU+xC2UEndIt+otK3WNHVXSJe+e1yz1AWutz4i+uZ6d0AGO0SU23iYjF7cempPuMVqUCX9YSoboRtXIpNc8BXaSmCcJfylrDLJNwgDo3PTEXFJLaVB5syIXI16/ZEPZ+ouL2YkCzWZeSsd9guWs27pEqVuS4ej77dObhPEsJ8dyNkhQcG3VHhBEuWKtNsk47CjwZPXExAUV1LX0msuaWgDS4z1jsnp3yQhNZx2lNFk41ZM1kO0Ngp56Ixpyq7Y7hyN2FANMwkaQBpPl/iS6cIC3N6bPbKMvdorp7yWze0XVwWQ3xK4mtgg3o6K0siJWqxo9YdO6VpWqoV+hqBbLcWyBnZCMY0hhmTn1hbq0RqitncjdInZGemxIRSvWkaX42Io/rmEnmetkHPazigEPFG9lkjKEoxF/tKMNRsNsfOu+1cWlm7CXaqBPTYwjXLbLk/BmVBVo6369W1uC3rmyRfHFmqmv3G3i7UsLmkiaKxmDuggt4Tob+cbxepz7DORVpX2qbRdgfiICu7Kxzi7csmxvEFpTvtzgMk5biaqDCVYAlU6/dwiE1xumVz3TDdo+Eb7UTmmHOy5FGNWWH4UjLIi2IaHs8CNvG3juQUx81uqGzBKWSnzEsriucboumOMPe41rV3kjGRK/Y4aEZvo850B8hZJTuzg4i1bHBwyJaCszsNqIxfrjx2tglAbKqulNGnem7PlQ5jFtp0zlVE05io7Fzn0x2jHKqVJG2ieqFcQjWPrtzesOdmIFeq6emmya2z6cZQrhQ4WIdZ5NYkVc1m1EouXVnxzqJcSMOlYBjm7y8fX8bz6uep87/+Znk8Bvw/O418HBy+vX+6HzgDy/18l/X5L+j088eX0gmhRo8z1ypu/OcB5f84cf30T19bjMuHx+va8UVZX7+dz9eWP/650UuYuk1Vl8PXKoub+6Hvxxe7qcY/fai+Pg+3X+5mJfl4Uv4u8fsBap2NJryMf5YwvvkBbmjV4HnpPw+gP764AwxO6FRfifnsKyjz0crnS5Dx2HZ8C/Ly638DBGnOGtQlAAA= -->
