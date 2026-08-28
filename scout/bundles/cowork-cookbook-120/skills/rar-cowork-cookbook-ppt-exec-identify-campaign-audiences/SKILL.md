---
name: "rar-cowork-cookbook-ppt-exec-identify-campaign-audiences"
description: "Generates an executive-ready PowerPoint deck on identify campaign audiences status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_identify_campaign_audiences", "rar_sha256": "b9c20533fc77b8b534ee348c09e954a353b29d8c54e0fc5e1f5f6464f3359295", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_identify_campaign_audiences`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_identify_campaign_audiences_agent.py` and in the RCI capsule.

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

Identify campaign audiences Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on identify campaign audiences status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-identify-campaign-audiences
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_identify_campaign_audiences_agent.py` and embedded as the fenced Python below (sha256 b9c20533fc77b8b5…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_identify_campaign_audiences_agent.py` first:

```bash
python3 ppt_exec_identify_campaign_audiences_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_identify_campaign_audiences_agent.py   # or on stdin
python3 ppt_exec_identify_campaign_audiences_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Identify campaign audiences Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on identify campaign audiences status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-identify-campaign-audiences
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_identify_campaign_audiences',
    "version": '2.0.0',
    "display_name": 'Identify campaign audiences Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on identify campaign audiences status, complete with charts and talking-point notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'concept_to_market', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-identify-campaign-audiences',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-identify-campaign-audiences',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '0044bf674b8dd176',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/prepare-marketing-campaigns/identify-campaign-audiences'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/ppt-exec-identify-campaign-audiences', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class PptExecIdentifyCampaignAudiences(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecIdentifyCampaignAudiences'
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
    print(PptExecIdentifyCampaignAudiences().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8V6eZOjVrbnV+Hl+6Psp6oSq4Dq6IhBoA0hFoEW5HKULzti3xePv/tclMos+7m7X3tiIkZVmSnEvWc/v3PORb++gKYOsvLly4vughTZgDgOA7dEQOogfNZlZQT/ZJEFfxA7S+sytJo6K6uXjy+OW9llmNdhlsLtGzd1S1C7FdyKuL1rN3XYup9KFzgDomadW6pZmNaI49oRkqVI6LhpHXoDYoMkB6GfIqBxQje1IYWqBnVTfYQMkzx2axfpwjpA7ACUdfWQrAZxFKb+p/xBMs0g289QIrcH04bq5ctPP398CeH7ly+/vtgxqOBHL2per6Bcuydj/smXe2MLCcQg9eHKfIA2SeF17pZeVibwI8f1kOfVD5Ubex+R//qvqAOlX/345WuKPF9fX6Z/xyZF6sBF6gxUtetADXNghXFYD58RLu7AUCGlWzdlCpWBupZQk8+vO79TynLk79O9H16ZfPbd+oevL1k+2Rga/OvLj0hWQn5lM73/PFHJf/jxczwZ+ocfv9OpGuvu2vVEDEr9+dvz+kkWLvy+NPQeXP8Oqb661nK/vvxOuen1KvekJ9z58vkO7f/DK+G8zFo3BdCQP/z4z8jaAXR+HFb1v0X3p1fCAYwgqNNT8B8/Poz8MzJ7KvRO85+zzaFb/4omcPkbu4/I01D/jPbD/v+NdBymMIjfLP4Pyf2jDbO/Iz/9U93+1YaPiPf1RXBjmG8lsGL3C/LrN11d8T99cL5/+OHn3yDp/5GMnjWl/aDwLQFp6LlV/e3bTx+qx8cffv7pQ5PDWHNB8q0p439E8x/Z9cHnDxZ8rvrhj3sh/1MapVmXIu+Rjvya5f9R/vYZOYM4dL5/Xn1Bfp8v02uGTEq8MX01we9ypoKy/s6OP778BjEihdo09uM2zPL//E/kENplVmVejeh21tQIdHAdJu4kvBGEFQL/T7ldutCuVQgN+1wH43/y8CRx5iG//C/7AZ6f7Cd4zvO8/jbB4rc34Pv2Bnzf3oHvl8+IAWlnZeiHKYiRI6eqX1Pgww0T37x0K7dsIaJYQ+1+glj0aXqDhCnyy79D/tuD0ud8+OUBouErSh353YRQVRO7nyctL4GbPnWy36HcReLMhhJ5IYTXj1D7KotbiHCTRaoojGPECUuoflYOD9rQal8mYr/88osFquBr+gqpBPJaMqo5XPAuDvLpE1TNi0M/qL+mrh1kyIdff/uA/G/kX+16EJ94qBDenz6BEoq6IiMwx5oELoPugg6GAPLwya+/PQ0MycBihUAPhl7ovm6GMRq5zpu19S33CacWiOVCK0MLJ3lW1hCnkbD+jOw85F1eyHS6NSF5kFVTecvdFLrAHiBVANV5tySsUkgFA7Hyho9IU7kPrr9YJXiImMBkB/UvyIFXYd3IYvhrEvOxCG7O0hCa/z0WXj+HRMoPFbJ8I/EZkaeoRHJQgjwowZOHB179AuvF23ZIHCCp231NpyLpTqZ6pMirefyplIf206WfJp9PpRjigVO98faf5d5BjEeVK7+m1TP8QTm5woblADL1m9CZisLfniFVBVkTOw/7QUknSk8vOE+vPGJw9y+ag9Vbb/H7rkKYuoqvDY5iJPL/vROZNOA2m+NqwxkrAVnJxtF8tezUQU0eeG26YEOAwPB6zaLvTcIbxLwh7dc0DmGYlMPfXlc+/PFc84peTQnNd+SOD/owGKBlJ7qPWJ1iryynKAdf0zdI/wjd/8AvqD5MbBj4U7y9MZzuvkkawOydrr+X94dvS2fSHsYjkjdWDGPFc13HAtCgdTAZ+s0XMHDdKfe6ILSDP2iFQOowPiD9hw+gOSHsP0wnZ1BNmGpemSXfl4dT0wSlcBobSgtbVPczcoEpM4VNBfMUdj7TGmiFDw9SSOJCG0MR3y1cBSB/FWbqap8CgskXWQLD5fceeN78HuQPWSbxIVXggBraspuA13H7V8++y/n0FRQ2mdLysemP7n7qivy+9vzta/qQ8R3rYbbHU9n+nXEQmGXJa9RNYFVBwEncZwDBSHhU6M+vRfa1ir/L8uVPrfwPf63bf5TN0x899wUJ6jqvvsznr6XurdJ9hrkyhzES5m41Vb1PUwp+ekuyT29J9uk9yf5A+9VUX5C/Jt8fSDwD+wuCfUY/o9MtKbQnTm+VH5qD/7Q0P5HT3a/p0f3u52cwTGAbD7DMvleetyWw/Pil60+LXytRNRWwDtbMB/RCT3xN32PhmSkQLlJ/KptV9rsMfpRg6NlXx71XCHgrrSFvZ2rcfHcaa+JJ/Mp9+ZI2cfzxJQWJ+++NM1MhgAEL7THNQTB5YCtUh+7j6r0tmi7+OMo90grigZN9mbLrIzK1sBAD37rRj8jbfPAYutIGDkg/TZ3wxBIuhX/e177PiZb7Ameyesgn2V+HnqkBezbGfxZiSiooMVSkmmR5y9KJ45+IwDe+75Z/JqI83oD4CRUQzSfcDuu3BK+gnA5sfD4i0Hsw8WAuQYhs4IY/s4F8SrdoYE10JnW/2++7WtmrLr89zFC/To6/vrxBxtMHzy4RLoe5+amaquIcRipkCK9fYwre+7/qH580INDB3gUSsVgbRymC8GyathiLIkjXJUjGRlmXpUhAUISFsw5jU6SLejblYh7lLcgF6REExeIsBem9Rue3qfyHk1w4ADZj0xjpsDRY2C6BWoTtYjjm0ISLUizhMYxLQhO9b4Xl0Xkq+6rcZMn3VnYyylPnX1+sBQlXbslqx72++Dl7BrRJW3JgsfTC84s7w6BsPqAVnvC4k6JuHEU+oeWrjU6AvbkJsxg1TLoqwh22Ghi/2y5WW4JXq8QdOlaMc0xEq3OI6kvZum2YVuo8iqIkxSxC1JLteGU29TDeE7KUznZMRmh9vEX7kSHsEJADs2qGuAksTB/OUtcvJFqUWLZqWnofZUcblal2o4fGErv4jWvNK8mOC18PrRZfRZYVZKx5S8F5d+r8GJMq3LoltbvpFe/AKKIeF3V+O10ufN1uMnabowu3HfOZ297j+XigvHabYhozuiV3WcXczdKs/lZgBZDOTZHkCYbJ4YIsomqxTGabU9/sE9xnkttpkIyE9cAxocNToAXGYb8VjbUipRK68C7XtU0m44Xe6r0y3HyXX8SJvkdNcLXDBE0MQSkjvRZNyi2UTi9IrKgX6jFTXLAYz2yJQ4OeMsWnl+C2L5WFq93VzVzXklu1P+kw1O96eUg3mO/Ge/9sQCexcR0vqLE7RE1VDxbAgz49O1pitGeOvNJxOGA57LkiEuh457FUhG4PNQg2I816diVluXyq1xmgciEj53UmmceKx2fAx8o1PQ4wTEEA4VIZWtkPtbY+5zflJIiEs49kU+sJuZkpPjiH7Ajjnqrqq6p0zt5KlguKujnsPDPM8jyumaHZknhlpf36XFqu1BVuV26c480/sjZYX/itpDPEBYQy0x6EsSiikQNVz9b5zFpebtUox3eiSLDNZT9n70dArhh3l9Wi0qeitkijg1wm9q6qjcVm3M6bWVIqWHU7ufeFdbveAqr21sMuu+0i8aJVs2KIuhwHZpA+fm610p7Xk4o4cHKM8nyfuCt05RFkWpmzMwwrjhg9nN9Xs4hQ0c4ztwKqp4bLeovrTTVrnXYON/pS3cXFeq/FXnkp+qxKROe2V4oBCze2asZC14FQ5W6d5mfnTtztzpf2pMcktRRSa+5T/W7XGfpGz5Tani311tx5u05w96uYD0NTVPAVsRvzVS4dMDNsQLW4J2fjgi2qviOTe9hHzWx19B1vhjGHjlB2ph1RIhcpvCYKUQwCcmBXG3YftYd4YxyYcXFp+JKSuxDMeepombZ0wy9z1CO9PBNd6biWchTf9aXgMLm1XZj+wIEld8ZRvcyK9f0eOlUqmCDZ9xgX6EKRFxCplOTQAsPpRTZo+gMp1XAeNhan2hdPS4fbbXeiTl7bPXWXdWZG2Dvi4KhSGhCseFzj8hpb5IIqX4ua1qtrDs149eS876RxreN7VbDzJunFQ5cdb+0Gi6TUvA9htCCAhJm8tgwSsClQVc0AxJuLXWDjehiOW7q4zfr4MgYhmyvtPoqaSPcScdB2qwI0IAmJy3zN6Hd84E0PZewdHnGnK40ZS5hSBS3wzi52B528J1XKDShqXpTTWb3CET+8Ynv8MqyYkF5flzy6MeepNcs3hpT1cs9SFDdgEW7d59couGigt/FlcuptlNEolNaZPRvFKAr6jLAdjo5Wyy1LEydMYMmlyR6l1NN6jS503sYqasOBlXoXD4fmpm9VcX+XDuqaOoh9ssJE1bR2Z8zC4krz9YpWcMGeHzZ9eBpzozFxh2Lmbi+aRODk9WJen2L7jN8LX8jDcKXSfEiEy/M8wxcrO+TWtiJz3c6Osp0eWXnB6cSJkUCjYKYOuGumD83eX2UYuUkKPJBYG4KwEK78/GTuYiIOSLPAbuRJ6Ed0W4Z8pAPiLvPLijquK6e07vg6BsX2uLlRGDubjdX8cC3tfie6xQXt1wnRokwxGAKT6uX5Fs153+ZDjZnzczVIhWNI00aMrwct0xraceecfzVoZhFtF9g4zGF9E7ZDMDs5x7CMCWqsQ41bWct7bhxQxRQlWvML0ZByewBcwBEE4539QoVT9FLK5Ivdavy2h0B9cI1TIBhtCBotEPdJffSZpXZTefPgdIFqivRZP2azXNkGaNpnGOuGs8UBv29SkcT9fltc/Xq+tgszXK1Zd2jKdW9S2A4Vwcq8bxv/4EKcssCQOMo5N4C8x+kLOUZ0Lt+2O01eASdQrkwRZpzq3gWF1HFiUxf77mAPBp7KxPLGXCBmSEdldVgfesY21CS+Y1bEHK68lu/SWnDPByvjtw5NXS2eDmCG2g3Rm04k8cuYPuyiqjthtmNAsKUpNDtm82rEeX2pLvOezboZpu2AMCPXoArdAUsA2Gmac7mmVrjNpUZYBXkjrXONWCiSIEblchnSURmoAW1cfR5tVFxbboyYY7R8sz6u6zhYreb4fXlh9paCxZ0j7Vk90YObn+8Z+bq3TEnlnc21cbjbJQwvc987wPJ/NteWvTnW9Z3TaXGddsGAkXziB2pvhhEfY2k6G2WDo+SlN6JyHq573MmvVH2DnQzDxuPxLGm4MD/XTmrmK2dDbbN+sxobDIQL3C1Vb8eLiqXXl413UlSjSUVdGu6njaWiZ+3CJUS66i4rFbClw8uXKJVXNS64XXyAyd+L4ibQo6DPT/oY7JYGrWtt2rOYPYtkw8yzpRLN53jPVgtmKWJ4oRxDirxzu6Rzz0485pkKy71zls9L60pS+207J7aLvmZOl81dTLCcI3arC+65Or9bOOs01RekZEi328wD6UB7x8WtxE1FxAqLbVg5TwLjBA7+bmAXe/K0UVbDecd3ms62DU7WgSgHc3s9xJfVzeRJVwSsl+bsURyNRL4Fjr9PtTZuFWNnqDvXptBAuhz2+5Ds9mdyGxDESWJasnXz4tiPNzfMJNpp1vpIeSdR506HoF06zFCJ98gcyauxcg5k0QtnMcXCpT7aZ82kqeCSD/sZhzr8Em1MER32V1aUyUDEsOZEO6riN4SvDlSuHtPxvsSVIiZH6xp3rnBbWpdqv9hlfZDs40FoR9FVcBjHYkiKoaAMqESQpK20hbIX/SA/KAF9o2/aKqaAGnCkmbCxAsemNFDia6acDKWhT5ta8eL1aU9vZCnHYcEA+1mV71BOZK5jCBjs7C/wq5Mb7tILHf4ccUqQmrJ3LUEjXTgSn3kmcV+d4TzWJQlry85anpXqTlgSKlnghhE4YHcqK6OlTrKC0jgpDF3N3DlrkR87w6vozc7Qo73YDbIa7bZ7V0LvRcxkawrshkteAg0T60yn8NEXsjWvNnPYlmtt4mzkNhNT48SqYt/3unI94y3sNTOgc9uowDPe5fb4CDFO9qO7pJ0GjUDFsxyzQMjiELp4v13vC8s5577BzpOu2Gb3Y5LPzq4p6sVd61HPuR8OiXi3Fk7Ee7IybDUGekY+EcIduPnohZHZWbnaj+aV9k47B4uuVc1vhbwvRG4PC8J8fz4V6+MdzvfckFzlulyP4+Yw35sGNd9CI/kM07AtR4hK6tAG8HedOXYUlV3FBLT08XxoWOEqz1dKC/Bk3/Umzp/RNGAO7nZmXGADfLUZsQnP2PHA43mrn9PleudnVa2ksMbAWWMZ8INQHZZ+JxvakWw68bLuL7Dlr04H3Ao06lQawHPH0Dh3zmklFGqbmbA/0bdLvFY5mseX+2MZapesa2ufnHnLLF6sbysSpP5B3G7ubRKto5I/DOWyjBezkhthk3PplLkcMcIRNnxKk6lZsTmdj5Fy2LMLrYadvrki+VWZ9hp7EWmTAJ3YOoUtzWf3+ywit3e0rXKmwhSiIzFrTwyDMg7kYdZ6i5iohHCx2RN2M3Cm5OKq4BxNdXkWdZrt81qRT4oS8adzlB4pld1cOeJQAXJP4ZaQ37dlXhdwSPAubLC6KsfCSFfM7raXPKwh05LjsPuNOTpxpfqEq1EYIR843uq80Z2VNu+1EOHzfcV7OYuBDde3zrbk+xYTJBqcb2C2CQ5EVVp0w1mCwC6EuxteD1eXbpfufRxSdSCuxHx5pfiKCxtsPi+2M7mFnQWLjbTWluyqXZwpfEVu2KWyD0Sj2M/XPSqJq2rPNovjnl5W+VxTcOPoi5jHgF1w2wnGPR+7jayoO3VvEst63Y9bqhqzBRFHSYzTsXeYr325SaSayIC67JYLGo6TTlcIzRWjhzRdnYNTNciRIEmLDZP1hntZnZkDuc37DVFwc2V+tGU2Xi9vN3pN27tWqKu6mWktPVBb/NLHnKymBZ+2uMY66EbIbmgt+up4uhpGRJmLhcwO7HZWJeNqzppzOvD7cuZvZl14gcPsEFDYbNOjquV6Ccv0K1y6lrWmbnZ3yrcuJ9ggXTB2LobEImiuKSzeo1dsbU8mBFzFZyfJWsrQHjMK8+Sssyh/zTS76tjYg1CI17hfrMz26FJgLkhouFwOpjm7ijh1d1Z7b7Cb66oa692SuVlquo00ZjVcI85qWIY+rKiQIEhKp8dWUVvOBUtfAsq1FxKmEA8e7NSItu2Ge6ISvptz+5A40563rO9Dt9hx3dVcb/1iYGVmG/raQjJBYM69SlyD0opEiZwdvSM4AQIW17hJ6tClF7TJ1XhERBC40ZM9Kvce7LxYwSQ4/C1OuL0rMdQlHZaVVEtwrGMZUY3juIeZrW9XipUBQ+Wu88Cnt0FQLg68Ko5ACOw2K7d1YOFMTRXEtgkqfr+05TjAMPq6oTPZ7ulFacMWh26dBsuyS0DE+DkAcKY/LdtlN1u5Gu8vllc2yNauubXTo3/U1Mqc77HIrU975Y7ani4e2dOI3+s+cfWycqyAU3mFaMTjSWlLp2LZ67xdExePcFCKLrtrzshkdWAJjFlgwhCeRwk/mwOL1iVrwb8a2F6ck0p4qsmGdCu7iW6la3x+nM/jcjTCzBpbUgB0nC6O3TXct7x80AzDL5x92HTzsWUYcrO+0qG81eWrG1AsdZzj62zj+8kSJG1IsfM2tjUUFGuXZIUzVaS9cfVAwlysY527c2y7PZNaBnJ2Wwt3dEeq2WGb7VdrG+Wa9fZ+2t348oTDC40m6tvA1k4vLaqzduBXte8Is4sazZxuSSrbnjlhLFgJTESPy47j6RvvSqW2zu9C0q/Ps1PISiC6oWIiHOCQFTA5flDipe6ysaR5qu1728sJwPLXHoT2TsdUx8XMxVnVg5q7N8HaSrkS01XHjqHl12BmYNZMi7cawVUSWvPxeAtxEy/msS6cVFxaj1KbNi3FbdUFZS9Hf0MNtXKvlvp5EyUUz8v3nEXVbt1jehylYXq5zUG6RbtrA8gxiBypNUK7qUl2PecUktFQ/LbXOO7l48t0GP08Uv5LD5GnE77/ZweNr2eCb4+YHsfJLnC+PHh9+Wti/fzxpbRDKNTroWoVN/7z+PG/Hal++nceTkwUhtfns9MTsb5+O4WvgT99z+glTB04dJfDtyqLm8fB7scXq6mmbzxU354H2C8P5ZJ8Og1/U2Y6JM8gB3hZZ98SUMLEfJm+kDA95XGdENTu89J/njN/fHEG6KjQrr4RC+qbW+aTrs+nHdPR7PS44+W3/wPIHH2B0yUAAA== -->
