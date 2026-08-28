---
name: "rar-cowork-cookbook-adaptive-card-allocate-goods"
description: "Produces a reusable Adaptive Card JSON snapshot of allocate goods status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_allocate_goods", "rar_sha256": "e792db7a8773776ba8983c5a8dd2cde181ee80f1108d78d43b9b4a7683407aad", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_allocate_goods`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_allocate_goods_agent.py` and in the RCI capsule.

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

Allocate goods Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of allocate goods status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-allocate-goods
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_allocate_goods_agent.py` and embedded as the fenced Python below (sha256 e792db7a8773776b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_allocate_goods_agent.py` first:

```bash
python3 adaptive_card_allocate_goods_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_allocate_goods_agent.py   # or on stdin
python3 adaptive_card_allocate_goods_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Allocate goods Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of allocate goods status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-allocate-goods
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_allocate_goods',
    "version": '2.0.1',
    "display_name": 'Allocate goods Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of allocate goods status for embedding in dashboards, emails, or Teams.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'inventory_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-allocate-goods',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-allocate-goods',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '02aa0e3f940f63e5',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/process-outbound-goods/allocate-goods'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/adaptive-card-allocate-goods', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AdaptiveCardAllocateGoods(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardAllocateGoods'
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
    print(AdaptiveCardAllocateGoods().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8Va+bObSJL+V9i3P9i92E8IcUiemIjlFkJCCNAB7Q43932IU9Db//sWkt5ze3tmdiZiI1Y+JKAqK/PLzC+zSvrtxWqbsKhevrxonpVDgpWmUehVkJW7EFP0RZWAtyKxwT/IKfKmiuy2Kar65dOL69VOFZVNVORgulIVbut4NWRBldfWlp16EOVa4HHnQYxVudBG28tQnVtlHRYNVPgQWKtwrMaDgqJwa6hurKatIb+oIC+zPdeN8gCKcsi16tAugIT6E3hgRSl4B2N0z8rqV6CHd7OyMvXqly8///LpJQKfX7789uKkVg1uvbzpMKlAPRcUpvXAzNTKAzCkHAAEObguvQqsnoFbrudDz6uPtZf6n6D/+I+kt6qg/unL1xx6vr6+TH/UNoea0IOawqobz4Ucq7TsKI2a4RWi0t4aaoBI01b5hE0NEMyD18fM75KKEvrr9OzjY5HXwGs+fn0pgArWhO/Xl58mk7++VO30+XWSUn786TUteq/6+NN3OXVrx57TTMKA1q/fntdPsWDg96GRf1/1r0Dqw5O29/XlD8ZNr4fek51g5strXET5x4fgsio6L7dyx/v4098T64Sek6RR3fxTcn9+CA49ywU2PRX/6dMd5F8g+GnQu8y/v2wJ3PqvWAKGvy33CXoC9fdk3/H/H6LTKAdh/4b43xT3tybAf4V+/ru2/aMJnyD/6wvrpSCoqynNvkC/fdMUjvn5g/v95odffgei/1cxWtFWzl3Ct8zKI9+rm2/ffv5Q329/+OXnD20JYg1k2re2Sv+WzL+F632dHxB8jvr441yw/jFP8qLPofdIh34ryn+rfn+FTlYaud/v11+gP+bL9IKhyYi3RR8Q/CFnaqDrH3D86eV3QA45sKZ17o9Blv/7v0O7yKmKuvAbSHOKtoGAg5so8ybl9TCqIfB3yu3KA7jW0URqj3Eg/icPTxoDJvv1P507V352nlw5s560880BvPPtjem+3Znu11dIBzKLKgqi3EohlVKUr7kVeHkzrVdWXu1VHWASe2i8z4CDPk8fJir89R+J/XaX8FoOv97ZO3qwksqIEyPVbeq9TladQy9/2uAAwvduntMC4ZOgFPIjwKOfgLV1kQLabiYE6iRKU8iNKmBuUQ132QClL5OwX3/91Qbs/DV/UOgCelSEegYGvKsDff4MTPLTKAibr7nnhAX04bffP0D/Bf2jWXfh0xoK4PGnD4CG9yICcqrNwDDgHuBQQBh3H/z2+xNYICYHJQx4LPIj7zEZxGTiuW8oa2vqM4oTkO0BdAGyWVlUzb3cNK+Q6EPv+oJFp0cTc4dF3UCuV3q56+XOAKRawJx3JHNQ02oQeLU/fILa2ruv+qtdWXcVM5DcVvMrtGMUUCeKFPw3qXkfBCYXeQTgf4+Bx30gpPpQQ/SbiFdInqIQKq3KKsPKeq7hWw+/gPrwNh0It6Dc67/mUzX0JqjuKfGABwwCyDhPl36efA5Kewby363f1r6PsaZqpt+rWvU1r5/hblWTKxxA/2DRoI3cqQj85RlSoLS3qXvHD2g6SXp6wX165R6D1I+FX3sU/h+7ha8tiswx6P+prbhrKQgqJ1A6x0KcrKvGA72pCZpQfvRNoMjfJd8z5Xvhf6ONN/b8mqcRCIVq+Mtj5B3z55gHI7UVgEil1Lt84HCA3iT3Ho9TfFXVFMnW1/yNpj8BRO6cBFwC7AXBPcXU24LT0zdNQ2DodP29ZN/9B6ADHgcxB5WtnYJ48D3PtS0nAVpVU049PQCC05tg7cPICX+wCgLSQQwA+RBQIgJZAqj8Dp1cADMBzH5VZN+HR1MjVD4c6kKgy/ReoTNIiyk0apCLoJuZxgAUPtxFQZkHMAYqviNch1b5UGZqTJ8KWpMvimzy+B888Hz4PZDvukzqA6mARhuAZT+RquvdHp591/PpK6BsNqXefdKP7n7aCv2xnvzla37X8Z3HQUan93j9Dg4EMimr7xQ6EVINSCXzngEEIuFedV8fhfNRmd91+fKnbvzjv9aw30vh8UfPfYHCpinrL7PZo3y9Va9XQAczECNR6dXvlezzVHI+vyXX53ty/SDzAdEX6F/T6wcRz4D+As1fkVdkerSNHG+K2OcLwMB8po3P2PT0a6563/37DIKJSNMBlM73qvI2BJSWoPKCafCjytRTcepBPbzTKvDA1/w9Bp4ZAlg7D6aSWBd/yNx7eQUefTjsnf3Bo7wBa7tTExZ4094kndSvvZcveZumn15yK/P+lz3JxO4gQgEQ0y4GZAvoZ5rIu1+99zbTxY/br3seAQJwiy9TOn2Cpj70E/TeUn6C3pr8+5Ypb8Eu5+epnZ2WBEPB2/vY972d7b2AHVUzlJPSj53L1EU9u9s/KzFlEdAY0HU96fKWltOKfxICPgSBV/1ZyP7+wUqf3ADoe6q/UfOW0TXQ0wXdDGDtbso0kDyAE1sw4c/LgHUq79qCQudO5n7H77tZxcOW3+8wNI/t328vbxzx9MGz1QPDQTJ+rqdSNwMhChYE149gAs/+pSbwORcwGmhEwGSPXKGuTVpLklyQJGFby9Vy4eDW0nVRx/Xmy7nnLRF/PkeWLrl0sYW9sjGLJJYLDCEtywXyHuH4barl0aSPh/jeYjUH0xcEiuPYak6i1sq1sGk8slySCOm7gPS/T00AHT6NfBg1Ifjej05gPG397cUmMDByjdUi9Xgxs9XJIlDSVkMbrgjPMC8r0Y6OV12bUVLb8BfX35iNkATewi1yiidLytFOsr4WTRZtOIvuioPviPBwwfNtddu4jdjyRS3Y0Xw0a8LZm37nC14hUqGwmWcZl2KbJjWuc2+IsPTcoMdcipDKY9a2NOD6Cu52HcmhJRIXapbz5yitxj29Z88XeAbvsTkyJt2KM0+6hBgk1p1PnSqlx1tt4EK2S5djZu+PBILWIscrO4dOwwY2nCHHToUXI0625WE33yJYO5J4aBLLblwsRdQ7CTWnp6kTVLe2uRZIaZLG6FjRbq4tYtrAc3U3u52My8YlpCvX8lyG4dKlRV0US6qIFTBp06ibk+lEpufkOGIsUzIp4lNoht4tpR0+lZyEKYaFgh+rwgrKaiGGmoYfx1w5WtehO9mcF1/qpcwm6YwnzgSn5wrXc+MmKDNskRB9tyPGTGdOiZTsjnBbqLvkvOtyKXSTsWllnbVWy5EWt7mTZAhHn731xT4QencysDU2kFJzRnNj0NOr1NvJaKrlITLlVeftLtK+cWq+zIhST7BZE4hGWtMoYcW3iib6vq0i7drF56tDSjCK7/f7+TlNtmdqqXBww10P85siHE+LG8IQXX69hLni5gWO9+xG5bj2ctouyEUb8mGzOJxHAnXi4tb4CX6WV6SyowW34k7Wxrl2G0QO4m5l1gVpM7dDvazgYuBsyjJufmYQihiUyNVZqXpp4fFs52Q8ts1J6owmW8ZP9Mg5BFhnHoYxVQpx183U1erM2Nb1iogdrrDcliOdVpdVFGw9D6FLj2S3uYZFuDVHQjYjS24jqXFVu27Q/JR6DOMuOZg1YU4f2aE69hxt+SR92ztjRcKGb+B04udFd74uyTpx4JXRCTtCOp9Uws58rlvP21CtsrA3cTjqUUYQdsZNHnwpvnW7lsNFeVw5DMjt0wZZl/u9KhKDj8nLJb29laxnnJvjKiovO3lGOXTNc0dYtvbi2t6TnIpEyC4RduqxPvPsUJSB6XoG5ujMHBtzHwTaviNFOLtkuSwS4kALqouoyZrl0QhHNpY/1wWF12fjcGrrGNt2W0bp6SIjLsy52W9m+oquVr6ghkm5bLpolOAO5st45R4N7TRjMbIRr8SQ9Ria2/R4EeKocg9q0ofJXHGUtX1aqyWOsYS43lEmfOiK+spbx0iEZzaO64lYHrFGWZGxHiItcSBbjsv2XVUPwzI6qnZcnvb7eKsJe7b0TASNZ3JrcYTJp6ou0Fys2+YijszVAVSI+VY879U1zpbzHlWinjswuHJk14XnU6ebiy3xtMjkiGPk2TG+XtFWEvX6QuARYA1um+qzQygGknONwrW9slpbw8t0I101kSMtfruNbid4Lcn5/tajg+BzUSuaxdLOdKFxblpQD0gq1VdXSONdQEroqA29SyeyiftpdTaaTEb9SNUtIvSkYrHAZzkn7PRDYKbzzF1zKs6M7TK2N6uN2VnmPF6uy964dAt4xSbKNSAo3BJ2caPXheiR53l09F0K3iUHgkzEA5xIW76X7LQmBYfdOkdDrGF5CJDwcNKcvJI6H2WNm6QORSrqErHyLoUlULOEsIVqru8vpl1wBYUbRcg2hmanvNX1duNQFzfaC6ebQTlcIB0SLWPHhTvf7zM1bQVMS5grF8REakYlZecgAvf9rrByPk0QStUcE80zjTGMem5idni7LfiKkdIYGymZ4AsS31z9VdgT8bg7jXBWL9GVn5fEqouDOLFoSUtaVt6utlKdFTDbnq4w6oXUjlYNz4Nneajfrr3rrm42vTxKnOQp+8sy8sN65flKTgzwjLstscOW3x7ALpE9Vov5MduI9KZmdumWVPEx3jUMXaVWdNb3wT7Z+uZN3u+KUicDMYvmhjSj1VEYKq0ZrESz3CVAky03yK3a5Qd+NDEN55tkg0uydj1eFfvE9wFLVPNdz8KVOKZOtQ5GJbcbY1erYqWKqtz5ScDhvlCoKp0c/OVSpYxbi4Ke1zNSIa+Om/2MtpboPMHW6TpxWI3m+zlJnDPDzL2wzXc0b8U1ejL2smFujfVWvaDEYohP546sbYfjV7FhBvAhn4vHS389EidxCXZrDrsCwEeHcs/a5BoZ0pIamlRQs3Vhng0zNEt3efLzYOaEB19hAqa5xdd+Nd/ejmv/sCPN3Sq9Wo0ZFNF4UebN1inc3jkcjf2+Os+HmD62m3ZJ4efoVueOomwdfr1JB1kVUY1XsEMpzOjTQRzZPSleKmk3X2SD44sHsr+mJU6ZkSzzJ8vVahvw1EVGE43pg2tedaeh87aNKpwXdGJdjJ5LBtlEMLupyVuxudzkMrpct4q4hcndbadqBDPL81xPtmGC9WVnDCs2m+Ob7FqeeUNZCXO0iWo1JhMv5oxDO/IFWxp455KBkKwaJlUvZBYSLrLZq97GE4tM6noGGQODvO2ti3I+ZVGhM1rFKBZt1EJ8km5GyiW9IUWWtOGbQmKPuzZnL4XfXJRyjQCOPRjG3l9Ya/QWzMi44RInFgDfUoFO42eU3XuBXR3T+UU9AO72k8KbzUBnUmZ5z3JMYnlYQCIySsghSyNe05Y4IsgNHhIn/yI1C9lufSHC16frRUMXXtMLeuncqAibtx0qF5TKcjueoVsEs8xwnmwMwTH8LX/cpNf1EFpKgdULU9KPozEnmHad9ssSWeBWFTrAshFnzjVnpEx8bXXq6NjoSkp4CfQ+81Fo3OVG31xbrQWl1bKUwFsHO+7QgUZLRNa0xVhOXIb7syFgmzbVxQWdlsNW3Okr3T0XXM5Q6yY4a4mH8wlFlPJmxu1hLRnP8+ucS3ND9Q7K3DvO6t66JT3oAGFcjg8Xmb3GVS7LsaQNYSviLZuOtEYhOzHbSEiWZEPP+cklHc/iuDaI2k02kYPsYJ9qt5URNiI3WwnnNSbr8SKlMHJHmAgOwpRqLgbiZmZUHQsb65Ot6+AjceM9ad81W9FH8PTQ3RgY19jFQa+3Haje601H25K12Z3n4Va48RhztmReFlx6MdtsJCnO/MM8uebZEPgiauTucLVW5aLcXvJsW1DUIjvxq91NEGMrFTh1q7HnfbuxT3tCjwK1LGNa58tCO2dCeM3IM60cVGl13drBRoBNziC9gJidQmRVXWiusKQtTW5DW0sqLeCT6zlmvMO11qut1UgEsmZ6DtXmR8OWUtHoC16Xwo4R0svVPM5PBlkvGbdDMu4wclZdysvtSA/z40E4x2VttmFnWsTJpMhRr1NE4fKrbSLqZtyQHby9BKFQtKha75q1Yy8Y2xmx9cWLqat54gKeLY6kIF2dsRDyYdebB9tBYea2CIV1rmyW/VxkiJi0olXlW0VL8rguJQJv+dRCkRrGzdbtcXPlq+q6cdHQkV1OOctR5uCFx67DBQ3Kj+yiFWNX3op25F0sz5J4t1RB66hqnqItjo0TrOhbxmHF2g22u5gVjOi224f1SWIMUW1yKV1V+3YOyxVnVTVeUPzR162yJw/+Pu6IZdMzmSketvVxjdmCT/fESQ1lkzNFEmZVubTXqWJLLKcQO8aW2tREcW6h3FZj30Q+vkfjqooECpA5ylYrWyvdrSVwiy12yZsDyW3G+eLc82tXskm/jsPZ0WZvxJXe+ivvinSDWpUcSfaYUlUtzi/408xhUwe1u0aIxjqmFhfhcDhq3NZtiU1xu6YHpET9XYbJZVePmMAmmnDqrD1uSTRpm9fczKpbE9CSmkgFr3rEUWMW8KJnkXSdYnLAVcu8ItGedeeLk70KAIA1A5dLIj5sl93VucDKMZs1N8NB9zEciAsXBOGVrCmL6WEXPaX4ojeT2Mv0gqQuGGujcM0T8lp0ZrLr+7WhaPxZSN1qBZpnjLC0cUmW8bzxFoS4QjYEuql5jMVWFKMfxAV/Q0AGkkzDXGnbineb2UHSdDrARmd57RMN22obXsUjODhE8TJaHS7UMYnh7XDiu+w0mqlRr/heDohRWhSEQvc3fG8fVAU7gWy5urg6ZmxLaMZa49NTzfvH9dix1B4WAhZZNvg467Suv7D+yaMugq16i0jpR3tLVsm2tdtDqKH7glZAKc8beFBKlOobdp8GbdhakeX460pZq117Knw8v2D5rFov2l1Cu4ioo7SpMRIpCNmid9eHVWfCKjJyF3veXWzqvDtQsTTfmbEFuynukWF3GsF+wVE2Qu4pRuYvRpRH4F43aNoH+wMbEdO2193qKAnbjo28G8nmksrbnKPY7DL2lrLosdSakZVFAeIsjY7J0OZxvaL3MevtxGjDAEOdA9+QsrIPLpy2XG6lcyuFGNyzOCYwzaHyuF3TFwU+qzbLpecXCIh6MvBKakuhOOkDeouHHhOp/mJQeFBiq0xgw4Popzte280alFs2p2bgLs5M6oKNxNv0TIHR0WrW7sqttTOp4YObIISEmjntNIk8tJY7qGQnqXvuhK/WLe+Yw2zer/1T4zSuLcOYxiOSMzjzIKg6kHWx2vOgWC4wrFaT+kKdc9Ju5g7S3ix2PC+CkGrPTG/LEtovUUYvfOdEJnP90thz0osCa71fmBpdEI1XsB5LL7cONad7PV0uirW/J41EpUxNwY4rCS9lYZDXKsGCmM3gazoDfX/OF+1y52KBEC5sfOzr9SLtLj4SwZbpzi+HAm6XxCxCNQomFWVVHhWZWlSx0RBIxrT1rHGNUUQ2stXYbQO2mPN1TbrHEVnZyEwll+kcLhjRH7pCsUe+IpaBHu98ab+jLmoguVI0s+FhgZ6wjD6SmiwcVn5NnzB6MfdrFlH0A0uVGj93Z0ocd4YkruuF79ID0cfjxu7S/Z6UC2S82sSIX0m7F0/eOAYUsW7ynmKP5pZxNruFusnJnC40wlx2/iVBGt+2O1tzaw9eYx0fbGlM7dyY7LZHph2DpczTznEuext42S97uhaoayjttrrB4R2dqulhdkRxxqJAKZY2O2BOWHv4zkuVQ2CNKZYmDjZGFVZWC9oWhZlHIBuHT2Cp5uEKTW43xrKrVkmVum/WoComLnxLzboXjE3sl4jexgd1gPHj0nK0cH/1lY1cwvO+o8tY3x68PUVqeoCequ0Q3BLQ3B9qen+ZZXQHR4ddsYzwUR9HI9/0ozOqBK/gZ2tr4M1RJZQZxVT0yg9C6UBRL59ephPm5znxP/Vt73R69392iPg473v7nuh+ROxZ7pf7Wl/+OXV++fRSORFQ5nFAWqdt8DxS/B/Ho5//0TcL08zh8cXp9DXWrXk7Qm+sYPqlz0uUu23dVMO3ukjb++Hspxe7raefHtTfnofQL3djsnI60f5B+ZfppwDT6XEBBDTFt+cPJ+63p69oPDcCmjwvg+eZ8acXdwCOiZz624LAv3lVOdn6/MoCmIi+Iq/zl9//G2R439JTJQAA -->
