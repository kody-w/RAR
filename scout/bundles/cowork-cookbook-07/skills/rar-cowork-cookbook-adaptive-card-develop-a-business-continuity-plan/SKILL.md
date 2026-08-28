---
name: "rar-cowork-cookbook-adaptive-card-develop-a-business-continuity-plan"
description: "Produces a reusable Adaptive Card JSON snapshot of develop a business continuity plan status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_develop_a_business_continuity_plan", "rar_sha256": "3547907e2802bbe9b9ae66e6813ee1431926f0ff9349e9a9458a589470c064c6", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_develop_a_business_continuity_plan`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_develop_a_business_continuity_plan_agent.py` and in the RCI capsule.

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

Develop a business continuity plan Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of develop a business continuity plan status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-develop-a-business-continuity-plan
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_develop_a_business_continuity_plan_agent.py` and embedded as the fenced Python below (sha256 3547907e2802bbe9…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_develop_a_business_continuity_plan_agent.py` first:

```bash
python3 adaptive_card_develop_a_business_continuity_plan_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_develop_a_business_continuity_plan_agent.py   # or on stdin
python3 adaptive_card_develop_a_business_continuity_plan_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop a business continuity plan Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of develop a business continuity plan status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-develop-a-business-continuity-plan
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_develop_a_business_continuity_plan',
    "version": '2.0.1',
    "display_name": 'Develop a business continuity plan Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of develop a business continuity plan status for embedding in dashboards, emails, or Teams.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-develop-a-business-continuity-plan',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-develop-a-business-continuity-plan',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '4d2399e203219a3f',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-06-01', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/define-business-continuity-plan/develop-a-business-continuity-plan'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/adaptive-card-develop-a-business-continuity-plan', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class AdaptiveCardDevelopABusinessContinuityPlan(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardDevelopABusinessContinuityPlan'
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
    print(AdaptiveCardDevelopABusinessContinuityPlan().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/816WZebyJbuX9HNfrCrZadADBI+66zVaACBmMQkRLmWiyEYxCgGAapb//0GkjJd7jqn+1Z3P7RspwVE7Hl/e+8gf3tx2iYqqpcvLxpw8gnrpGkcgWri5P5kXXRFlcD/isSF/yZekTdV7LZNUdUvn158UHtVXDZxkcPtSlX4rQfqiTOpQFs7bgomtO/Ax1cwWTuVP+E1WZrUuVPWUdFMimDigytIixLucNs6zkFd31nEeRs3w6RMoTx14zRtPQmKagIyF/h+nIeTOJ/4Th25BaRaf4IPnDiF/8M1OnCy+hXKBnonK1NQv3z5+ZdPLzH8/vLltxcvdWp46+VNrlGszUMIevUUYf0ugQIFgKTgzxDuKQdop/G6BBUUJ4O3fBBMnlcfa5AGnyb/+q9J51Rh/dOXr/nk+fn6Mv5R23zSRGDSFE7dAH/iOaXjxilk8zqh084Zami2pq3y0YA1NHMevj52fqcETfX38dnHB5PXEDQfv74UUARndMLXl59GG3x9qdrx++tIpfz402tadKD6+NN3OnXrnoHXjMSg1K/fntdPsnDh96VxcOf6d0j14W4XfH35g3Lj5yH3qCfc+fJ6LuL844NwWRVXkDu5Bz7+9M/IehHwkjSum/8vuj8/CEfA8aFOT8F/+nQ38i+T6VOhd5r/nO0YXX9FE7j8jd2nydNQ/4z23f7/jnQ6Bte7xf8huX+0Yfr3yc//VLf/aMOnSfD1ZQNSGOXVmItfJr9905Tt+ucP/vebH375HZL+T8loRVt5dwrfMiePA1A33779/KG+3/7wy88f2hLGGky9b22V/iOa/8iudz4/WPC56uOPeyF/I0/yossn75E++a0o/0/1++vEdNLY/36//jL5Y76Mn+lkVOKN6cMEf8iZGsr6Bzv+9PI7RIscatN698cwy//lXyZi7FVFXQTNRPOKtplABzdxBkbh9SiuJ/DvmNsVhJKqjkfke6yD8T96eJQYwt2v/+bdAfWz9wTUmfPEoW8eBKJvTzj85nx7g8Nv3+HwHjK/vk50yKeo4jDOnXSi0oryNXdCkDejDGUFalBdIbq4QwM+Q1z6PH4Z8fLXv8rq253qazn8ei8F8QO91DU3IlfdpuB11P4YgfypqwfRGvTAayHDtPCgdEEMAfgTtEpdpLAGNKOl6iRO04kfV9AsRTXcaUNrfhmJ/frrry6E9a/5A2qxyaO81DO44F2cyefPUM0gjcOo+ZoDLyomH377/cPk/07+o1134iMPBRaAp6+ghPeKBHOvzeAy6EboeAgsd1/99vvT2JBMDush9GwcxOCxGcZuAvw3y2s7+vOcICcugBaH1s7Komrudap5nXDB5F1eyHR8NCJ8VNQNrH8lyH2QewOk6kB13i2ZwwJZwwCtg+HTpK3BneuvbuXcRcwgCDjNrxNxrcB6UqTwxyjmfRHcXOQxNP97XDzuQyLVh3qyeiPxOpHGaJ2UTuWUUeU8eQTOwy+wjrxth8SdSQ66r/lYRsFoqnvqPMwDF0HLeE+Xfh59Dot4BnHCr99439c4Y9XT79Wv+prXz7RwqtEVHiwTkGnYxv5YLP72DCnYJ7Spf7cflHSk9PSC//TKPQY3/3kXoT26iB/bka/tHEHxyf+ivmXUhmZZdcvS+nYz2Uq6enpYeSQ/euPRrI1cRsr3jPreSLzB0Bsaf83TGIZMNfztsfLum+eaB8K1FTSlSqt3+jAwoJVHuve4HeOwqsaId77mb7D/Cep8xzjoOpjkMAnG2HtjOD59kzSCio7X31uAu5+hOWFkwNiclK2bwrgJAPBdx0ugVNWYe0+vwCAGo6m7KPaiH7SaQOowViD9CRQihtkES8PddFIB1YRmDqoi+748Hhur8uFkfwJbW/A6OcL0GUOohjkLu6NxDbTChzupSQagjaGI7xauI6d8CDN2w08BndEXRQaj+o8eeD78HvB3WUbxIVUIwQ20ZTcCsg/6h2ff5Xz6CgqbjSl63/Sju5+6Tv5Yn/72Nb/L+F4DYOan9xj+bpwJzLisvkPtCFw1BJ8MPAMIRsK9ir8+CvGj0r/L8uVPI8DHvzYl3Eur8aPnvkyipinrL7PZoxy+VcNXCBszGCNxCer3yvh5LFefnwn32fn8lnCfvyfc53sr90c+D7N9mfw1WX8g8QzyLxP0FXlFxkdC7IExip8faJr159XpMz4+/Zqr4LvPn4ExgnA6wFL8XpHelsCyFFYgHBc/KlQ9FrYO1tI7JEOvfM3f4+KZNRDx83Asp3Xxh2y+l2bo5YcT3ysHfJQ3kLc/NnohGAeidBS/Bi9f8jZNP73kTgb+6iA0lgoYxtAy4ywFUwo2UU0M7lfvDdV48eNgeE82iBJ+8WXMuU93gPw0ee9jP03eJov74Ja3cLT6eeyhR5YPzu9r36dOF7zAua4ZylGLx7g0tm7PlvrPQoypBiX2RqweC9ozd0eOfyICv4QhqP5MRL5/cdIngECMH4t53LylfQ3l9GFrBKH9OqYjzDAInC3c8Gc2kE8FLi2smv6o7nf7fVereOjy+90MzWPm/O3lDUiePnj2l3A5zNjP9Vg3ZzBmIUN4/Ygu+Oy/3Xk+6UEohJ0OJIgR+IJCFmC+ROauCyiXcgBJAnKJYgCgOIZSczJAgoDCcApQDoUTS4dYUvgC8RAS90hI7xGz38ZmIR5lBEgAMAqdez5GzgkCp9DF3KF8B184jo8slwtkEfiwWnzfmkAcfSr+UHS06nsTPBroqf9vLy6Jw5U7vObox2c9o0yHxBduH1nTigSn+jxFMiQ2BDITht1RvVlV0xah303r+Xo1rHY2d3ZczoimzqFFT9Z6eoiWhUok+SK/KXSspUQQh3up9uyLrEv57YouCXS12nIduCCtmRk8t/X9I7EsncSOl0ieNRcSKcQyE5ZIeWxUI79o3SVw8u1F6/WlX1+v+MUqjbxSmcQTUrOx7aHsHHKWY7PZoYk8JrebfcYeuSvW+b7tNzctNfjmVDq5bCJCzpXmfKc2h0YVa43HImnmLM2cP3fUriDkXDfnvqKjZKCodi6g5Gx63hoVBfax0y631b5FL04i41HbQC+Y/WlAo4Tq0KUpNYCpjMuBnRukkB2JAIRz4Wwly7TtCoO8tKlWgp01xHUqxMx2OJpzBk8TpsuOpaa157N3Q40mvdB5cjWPGToYZpaErVcl/WLnIPNgj0e8gvqpbGuEzisMo7nsPtKINuFu0xpH8PS0Ly1WrBJaJzdhxbOuxbP7ijqRRzDjOGRNYCu+oQ82EpmUJZv6vEvo6X7n21kyx1h7f7zk60z34ACpFYZC9invFWQz7NmpQxSb5SEQB7Y3/FUjZ4XpUGDw+OG0LHg7IdVZTbAmmbW+CcUYauWGbpiVxcmezhqpigYHUJIXf0lqgjUDMktrekkv6ungoEjLIUvCM4SGklkBENwFuUmuIubuSY/l2GgtNrnwvYoRUe+Xdap41lFaGLazDyVtJ0+PijAwg8dGLoryscAqMwZxszV3mzGMWpEnvNoIR70zav+gzTMFahG0MH1izDQZ6zTNBnMpKru8q9XavtKcpYWL5LY4ltc17svlxhkuuX6MpJZaO0Z2Rits62R4o+ALVen0K2JJnbTAVaxW9r4eHYhKWe4au5evM7SfRsZRJSnDnufXNVGK9crqzSZO0K2Z2sv5UdsTx9KsVKIIJbuW4vVixooxnjp477izjZo4fXpNBW4tuUhYulsOiOR8ucvACUdsgTXMRUhGYLFnjp3DrVi5uIQ8OoTaeamjMXfgXGHP5p1529raEO72fK4mySa2W8X23Mi3emlJyMjSPlTWNhaTRXJWFf6yYWR0leRcK4uKwV7NC09s8As1v/VK4x3nrq96Uz7j2+GY55JLmQG1u7i3CNklhRj4pdJcvGqq7/Gr5oo2z22OM1tt7EQ6JMu8iHqnsxO5jhpSTaZucdkrLXK63bATyfSuzcUw97flfEuVBwAMydQuAJteazmG1ECXIkTtK7NVPvAm08oMMSxWs9Iom0ENFshNmPmNY5R7cX9BTyuMFq6+dmnMaYk1DmlubG2qmXx7PDfHOExuer9aOULe6UHSLKTTsZzjJ7paomdKmwU2w0f6bBkZhXa24otSWHQYrkz1lGZS25zPi2SX8zRXdcv6gBbdqVswrlIXEY7pe8CV4LAuxTzWN3Lr27a2TvDIUi0ykaViFYjtikduzSpZ3dCp1dglAgvIrGTTUqHPm2VATvmCZpVcDW0UzRqFPepSN0PlMK/TjCpyOchKXNle625DUO7mQAB0WU+hLxbZTdgvKLes6rxeUc65Ty1MsI9xIyqILZV93df28YSultFRQA5cBMRZeQnOcxVnBFk+6MmCVxRrNpczvUZ9ddaHkZ7MA1d2O1X2vBBGIjuESExK00Lq5uFpsx+8Ilkfyv2tK0SXWRjNJov70BDnG/2wWrElbx2zGhVXZNlEmpFL7HZNbo7bMvNgUmQOj/BpaZ+8vr8RYbXdp2fpwjNxeiU2G2+B6btBEAlRWUu2TS0p+YYuPItgeXqnnqXjwQ8awuRSlvenNsbe5vtV34kRT6JtpwQLl3PPHtVN8Wwz2x8qil9Qi9n02MwX3mwGMGeWzhwTY3bLwtmJQ471Vm3UoY+wCiPrIVHkYrXnxEvpC7mv2o2KKRQlNXzKtiwOhG51NG/6Fdsltysue+3CPxuMmmBcmJI2XW8vwG300wVwiansjeNCS1YMp12kCxhOcRJZ9N4xM/3EnKSdq82sbGY2+cXgWRNMpb5Jdyt5WC8MUmbOVgoTRBSnUqtD+8rCnoRdFgs0tmr0howlU7kNh9B1mDMg2duZVzvFIEKrEm1vbmgnMuztBqthbFeU5J/wGkOPG/5kk1faWm2R9CLQptlxml25G8u7bV1wQEQ9nE/7jbRyQvzSNF1sEF4cZdh6tpYQhC89fLu/hLSnu3NDglmqrUSaOfcqD+ZZbHdHCXbZe9RsHaMWEbZ1irKw9tJNp5O4O0bHm4kQvbc0oVPFqbkXjUtYgmTDWeFWW7mdCNYtiI3bEbjCnFrR7So6tsgq6eZYapbUhTueZGC33PJwwAW+IlJqjbWoXyY+Z24TumnZItQOHVjjJiawQ2Nvj2vRPuXzeHu72pqzTPHVTJ6jxmGqaY0zu1Yufsp1zGoko953W70ROpIJkwY79SzXr/0lmsu9gKfkdusUOmD22rUXdIQsNA+iBaGq2hHQlJ2tC6zd4tIyYJwjuctOyVna+vMN4M/i9lKEcURbZLiW4RhliCsx7BxbmXkusGYNe0x2Tug4q2CKNw1qnQ3JBefEksEQrzcdUH3r1hc+ge5dEzHYA2IOW242k7GksSnJU3gY9PsVxrEZtgNXjyP9Mr9p5OJ6Fk7E1JvvtEWgXvrUEXfbaYpOUXAaFodMlHa0nAJ/K4oHE/ZT3OZ02lV04BLm0DAhwM8Gv4nZLsrk4ipbNhkYLo6ma+t24vdodtpuoqHaqIR/ukXrNWI42bqXjmXY7nwYHREaKEC++Oie8C4Fkq4IYy/Fsy1EBrrYyOQiLT1H46h52w7eOlPp8kxEYdJiDIz7mZ2VxmB3YXQ+MXTEsq0X7hhByqnDot9rgmsX16042++01UKI82VkiqI7eMeKVFOJniN5ypyva542bikzqJ0fKhuGB6oYn1BB92Mg7Q55oGzCG3oITMNuBC7dgXMddefsnJKu0mfG1uzX5dlWD7NDFQaJEOtpZlspr7Ls2hSM5KqzvQm8zKiYRSrmIplo2G7esNPzsdnPzN5oBSOicW6R4ow/P9KobdKehFy9ZOlMK7HQMG1jbdPrTiFhE3fd4titukhbvrpy6nWZCmrTTgmI2HaOdlFIeCauX/N4ERvX1ZoihiOxSYTtUkW1lbFD7bXJiGpgbaOWkK0D6W33ISrOFmd10WvzErmQVDh3ql05iLJyOyA7betb5ZEs4hWd76tjoQUcmqRHD6fEvkP3wqFP1gVpMTkbH+V4yxXgBEqYPSaU6rS2rt2cOaC4E5fS8nZjBgQrWJD4Xn+NCTzPTrfLDo7QqcwnGXXRxbWB3TAPy6LV3kR3ONEICndQq0vhkMKh7UjxmCX4epPMUqc9rYt5Q4Nwawp5hh9wgPepfeMC5bSk7ZMyS62mm3d6ifnIvFivjKVmnoWKrhj5QJHzQp5eLylG8nRzUlfFnDaRLCIQsJkubuKwXxX7PVEJkrqV8tnas4vllr9VPresQoQZymsS0e6G5uarojOPeripU8fLiYRZRrnmHd0h1SAEkRKPblaoGrbFdBqzKaACTqhbv6Po9CQMh7ojlKYlKXm32W/5a3HjlA0HVhDqQ35qG8h5OG/b28U+KMFawAja1/mmx828csLl+riekmFVuQRYJbuDsTukgcQdFTQ47uFWKyDDWWEsC7055dbVbJkp3/czhczPyDUrqaupCBmaBmCJJj6WdAW4KltqVgsxyfIYYL2TvLm6ViR7pLrOmItPntKFXphGX/rs2V6KUh7Qqk8zjNked7rPg7Ynl4FzWSaBzFtrE+VuPDUFS66/cg2cEyJGojNgmXlGTV3NwCh1uuoQnLVAGeBT/4hcV8rl2Mptr06b/uKBdZx1IkldZDIV/b46Obu+HfyrnHh17c6LqdT1U9lfTBGSnO04fKYHwRVhlG4FWINwZtMAjoCehVGLyy5HA2vP7uoKwXl0tQi1gZPapFjurmp/OJDCIvbXsEr39uygD/qKFphguAzZjmbPOz2POfcUhODQw6GHOyfyYGMMct1JokBh0E0kn5yESsxBBQluck9DzfOeOdiol19F4BGDHessBn1dh4tpqDDLm5bjNw0OMRl5umrK0tnIlL+qkejWAoG9hdPd4lqKU30nTGe6xNv7k6TuSJlTHJ/ycWl/2KjurXDLYk5Ku6Ky1GvrLvntjnKn2Lmno/QAYYmbh2y5DYOrgmTyanG5tdj1ckoHlFyYmzgWRFqo4li+Ne4RW2Z8cIGj6KnjFZc66P0U81Iv8JfxsV1755VOYSVw6YOFF9iArDkHgSWnyg6xOvA9CKkeXc5nmsjtpPOGUlRpv8d5G8tI0HJQ8PDc3xRWVvZttw5PFwPzFodE1IKYyihlO13qtk50u3VzGsA2wXteIilGooglSYH59tSGlLGaC9JSCAIWk4ituF2dqhPdhBoN5lM6OoiASSTrFCwWtG8azbDFl8E1WK09XtdgFXKJyt21czCIR/xc9SAhSA7YMG8bBhtyF735i8M+EnGGXMgihGMzr9tpU5hDYMnTgA3Aas2CoPCqzep6E+j5laGPhrgJzkPHqr23ugQ+2tl4cmaugm9LG2/liZtojgqWuDgxgFlggncBjnvZYxfElA8LjGAccJZurYzFOPAUMaMPxyvJ1wYlw+zpYaQp29Ms65GgOWiyjoNAWx2o1ELPErkDzKZxq5hVlmu0pfxgu7td5zJubWW3qQPSvTBXRfKXxZaGPYM4w84dTmymcbqpZiKu76zF2UfAvlwvwMDa+WxZ1rbUrogBX0gVNV3PZnuCk/c6png31p6mC84Q2Hhz3e8DOGtszKOvi8NsmKshSqL5jXFa2WED2qwtPA82Rrfp1oecsqw+Hmbzdbx3mux09LKzCGzeHxwMhaXFsxSJS3YXKioOJZUz9AYRFwpHswUubk9Hp11vFEwUDhsDmVOut0qN+WyBGFdLgVW7NkOJ3rYbcrfYB3YHERBZBrvhYDG1riT6Vdzx9LGl9zhg1sc5LVuIfSA0hbBT+hZuxJ1j79cbwmrUi7Hbuwj8MhiE6oh11wH/psjCdYetCIoTisbdu/HVFee71ssYEov7fHqCY0F7IAMfIXTP29jSOSgZ3c8SykwHFw+XKS0ZM9tx9UWV+RuMl699j8MGudlEjn+tN1tNksRoxS0CS+SpmIt8lWCw7LzkT+RZJ87+jvMlV/AxJedV/3wjN9BpfUmj+5CmXz69jEfXzwPo//Jr6fEU8H/sMPJxbvj2oup+/Awc/8ud15f/uoi/fHqpvBgK+DiQrdM2fB5X/rvj2M9/9XXHSG14vAke37f1zdu5fuOE4+88vcS539ZNNXyri7S9HxB/enkX+HkQ/nJXOivHU/UflLxfZ3Eej+9qvzXFt8fpNHgZfzdifJkE/Pj7Zfg8uP704g/Qq7FXf8NI4huoytEAzxcpUO/5K/KKvvz+/wDM6BkFciYAAA== -->
