---
name: "rar-cowork-cookbook-adaptive-card-recruit-new-talent"
description: "Produces a reusable Adaptive Card JSON snapshot of recruit new talent status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_recruit_new_talent", "rar_sha256": "326375bdd21fdeda89c48a7a23752ed1490a00b36bb1b07598057c4262592aa7", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_recruit_new_talent`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_recruit_new_talent_agent.py` and in the RCI capsule.

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

Recruit new talent Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of recruit new talent status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-recruit-new-talent
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_recruit_new_talent_agent.py` and embedded as the fenced Python below (sha256 326375bdd21fdeda…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_recruit_new_talent_agent.py` first:

```bash
python3 adaptive_card_recruit_new_talent_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_recruit_new_talent_agent.py   # or on stdin
python3 adaptive_card_recruit_new_talent_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Recruit new talent Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of recruit new talent status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-recruit-new-talent
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_recruit_new_talent',
    "version": '2.0.0',
    "display_name": 'Recruit new talent Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of recruit new talent status for embedding in dashboards, emails, or Teams.',
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
        "upstream_slug": 'adaptive-card-recruit-new-talent',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-recruit-new-talent',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'bff4c1bd4aad497b',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/recruit-and-onboard-talent/recruit-new-talent'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/adaptive-card-recruit-new-talent', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AdaptiveCardRecruitNewTalent(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardRecruitNewTalent'
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
    print(AdaptiveCardRecruitNewTalent().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8VaaZOjSJL9K9rcD1W9VKUkQCBqbMxWQtziECBAdLVVc4PEfQhQb//3DSRlVtf2zM6M2Zqt6kgBER7uz92fewT524vTtXFRv3x50QInnzFOmiZxUM+c3J+RRV/UF/CjuLjg38wr8rZO3K4t6ubl04sfNF6dlG1S5GC6Uhd+5wXNzJnVQdc4bhrMNr4DHl+DGenU/ozXZGnW5E7ZxEU7K0Iwzqu7pJ3lQT9rnTTI21nTOm3XzMKingWZG/h+kkezJJ/5ThO7BZDSfAIPnCQFP8EYPXCy5hXoEgxOVqZB8/Ll518+vSTg+8uX31681GnArZc3PSY11MeiUtDr9yXB5NTJIzCqHAESObgugxookIFbfhDOnlcfmyANP83+4z8uvVNHzU9fvuaz5+fry/RH7fJZGweztnCaNvBnnlM6bpIm7fg626S9MzbA4Lar8wmiBgCZR6+Pmd8lFeXsr9Ozj49FXqOg/fj1pQAqOBPMX19+mqz++lJ30/fXSUr58afXtOiD+uNP3+U0nXsOvHYSBrR+/fa8fooFA78PTcL7qn8FUh8OdYOvL38wbvo89J7sBDNfXs9Fkn98CC7r4hrkTu4FH3/6e2K9OPAuadK0/5Tcnx+C48DxgU1PxX/6dAf5lxn0NOhd5t9ftgRu/VcsAcPflvs0ewL192Tf8f8fotMkB9H/hvjfFPe3JkB/nf38d2373yZ8moVfX3ZBCuK6nrLty+y3b5pCkT9/8L/f/PDL70D0PxSjFV3t3SV8y5w8CYOm/fbt5w/N/faHX37+0JUg1kCyfevq9G/J/Fu43tf5AcHnqI8/zgXrH/NLXvT57D3SZ78V5b/Vv7/ODCdN/O/3my+zP+bL9IFmkxFviz4g+EPONEDXP+D408vvgB9yYE3n3R+DLP/3f5+JiVcXTRG2M80runYGHNwmWTApr8dJMwN/p9yuA4Brk0zc9hgH4n/y8KQxILRf/9O7U+Zn70mZc+fJPN88QD3fnoT3DRDetwfh/fo604Hcok6iJHfSmbpRlK+5E01cCNYs66AJ6itgE3dsg8+Ahz5PXyZG/PUfif52l/Jajr/eyTx5sJNKchMzNV0avE7WmXGQP23xAP8HQ+B1YIG08IA2YQIo9ROwuilSwOLthERzSdJ05idgQVAHxrtsgNaXSdivv/7qAqL+mj+oFJk9CkQzBwPe1Zl9/gzMCtMkituveeDFxezDb79/mP3X7H+bdRc+raEASn/6Amh4rykgt7oMDANuAo4FxHH3xW+/P8EFYnJQ0YDnkjAJHpNBbF4C/w1pjd18hlfYzA0AwgDdrCzq9l552tcZF87e9QWLTo8mBo+Lpp35QRnkfpB7I5DqAHPekcxBiWtAADbh+GnWNcF91V/d2rmrmIEkd9pfZyKpgHpRpOC/Sc37IDC5yBMA/3scPO4DIfWHZrZ9E/E6k6ZonJVO7ZRx7TzXCJ2HX0CdeJsOhDtTkf2aT4UxmKC6p8YDHjAIIOM9Xfp58jmo9BngAb95W/s+xpmqmn6vbvXXvHmGvVNPrvBAGQCLRl3iT8XgL8+QApW+S/07fkDTSdLTC/7TK/cYVP/cB2iPPuDHBuJrBy+W6Oz/sdOYtN0wjEoxG53azShJV08PFKfeaBL7aKdA0b9LvmfM90bgjUbe2PRrniYgJOrxL4+Rd+yfYx4M1dUAKnWj3uUDxwMUJ7n3uJzirK6niHa+5m+0/Qmgcuco4BqQxCDIp9h6W3B6+qZpDAydrr+X8LsfAXzA8yD2ZmXnpiAuwiDwXce7AK3qKbeeXgBBGkzQ9nHixT9YNQPSQSwA+TOgRAKyBVD7HTqpAGYCmMO6yL4PT6bGqHw41Z+B5jN4nZkgPaYQaUBOgu5mGgNQ+HAXNcsCgDFQ8R3hJnbKhzJTv/pU0Jl8UWQgav/ogefD7wF912VSH0gFlNoCLPuJYP1geHj2Xc+nr4Cy2ZSC90k/uvtp6+yP9eUvX/O7ju+cDjI7vcfsd3BmIKOy5k6lEzE1gFyy4BlAIBLuVfj1UUgflfpdly9/atI//mt9/L00Hn/03JdZ3LZl82U+f5Szt2r2CmhhDmIkKYPmvbJ9nsrP52eCfQYJ9vmRYD/IfcD0Zfav6faDiGdQf5ktXxevi+nRPvGCKWqfHwAF+Xl7+oxOTydS+e7jZyBMpJqOoJS+V5i3IaDMRHUQTYMfFaeZClUPauOdYoEXvubvcfDMEsDgeTSVx6b4Q/beSy3w6sNp75UgmSABa/tTYxYF05YlndRvgpcveZemn15yJwv+8VZlInsQqACLaX8Dkga0OW0S3K/eW57p4sfN2T2dAA/4xZcpqz7Npvb00+y90/w0e+v975upvAObn5+nLndaEgwFP97Hvu/83OAF7LXasZz0fmxopubq2fT+WYkpmYDGgLmbSZe37JxW/JMQ8CWKgvrPQuT7Fyd9UgRg8akcA2p/JnYD9PRBcwPI+zolHMghQI0dmPDnZcA6dVB1oO75k7nf8ftuVvGw5fc7DO1jV/jbyxtVPH3w7ADBcJCTn5up8s1BlIIFwfUjnsCzf7k3fM4H5AZ6EyAAgTEEX7m+Dy9DP/CdNeGhawd3YHAXDvwlSiycxcJFMNddugt8RawXK9xDYQxeEbDj4EDeIyq/TeU9mXQCt721hy9Rn8AdzAsQMN0LlvDSx5FgsSKQcL0OUADP+9QLYManoQ/DJhTf29QJkKe9v724GApGsmjDbR4fck4YDm5xbjtYxA3zN9KN4PhA1/R2CWtp4Atc3XSxiLOXtuUrqW/b2L9Q2sISesuUmEY9S6tkN8R5peebNlYWtaDrlaefB14loV2C5sCGETMPKikiRXKpBTXu/Gjob7LKIHbZCZeFvGhXp0BrT3Kw1qVcUeY4ZZVeVatCzJhBWu00RbwxJyIM9+4SHfJQIt2VGjuFsdpCwpLCCY1XFdcUtPIm+eIquaVBLNaaROs7lrRRPcysTQYtA7rwFXcN2d1+BfsWvYSGZOlbLo7uYd9gGkpP40Ifx2w4Ch4SjOejWxk5SQ74/szj8R5VeMOhJdJizrp4SvdzX0E8zRh2+ZqmxoJKZYPLjOsNmLM2bllRq0l5yG2yV7a2lvNkJbY3yBCcnUyr5oquHEswHUdjsB6u2kxWs4aQbtFlbsBHLHUvCrWmsuN56+8GRUXiYLBTEaYqTpJdfmdp5JYJCUs2SX1fuyOj63IP7VYsrzTx5XjZOHP/nIrEpY7D3a6rUt31z7xsFjXZ6XzKLBnhwsI4enIMw1nZ+52wLG4XdN5GwilttjDmnId6i/V9lydaea2ZysMFCEa4pFua6WVvbtYKBflUdVgOCnNkbrjTB+VKaNGVfnMx0KFstIO6xdub5mPrOWeccH/NNlCXc1jjWjZj1XNtvG380om3qeqejzaTXy/SqmyXtIsGHJsbxjHbpPYZl3jI3ap2w0rpGam6JQWLc+J8OV5JT/E8k7o6N6rw9VFm0jPDmMeS2KzOc+yaVv1ZZ2irueWJAZ8g1gAlz76p3KGJ+dUtXzY3le6xNXZZHMZasshyOejFfu9H1wXW1/0h7KPzQmZRUxEVYalvDnSlrFlxdVOu16EjIm0XcYjZEDhyuYyQPWcCzNGOsc/egktNLaFWq5l0tLfwpYcFRRZPvZRYNQD2CsEDJ52HkBzJjVEuLmUgH8QVfEVlcb1dD4XmuZsl6HRBdsZ9v9tIRZXIZ/ic8PDYDZTPtTt+m1PGno4P60o4mZaVySzV+4G4QvpKPNdEH5a5cc4yj7KpG9dBIiliXL5TGKvYINw6R/PNYCsLKN2fBegMFZIS82gGWaTpm/v5mSA9B1aTW6ytypC29kiw3lsM1jXDQSBJYh6oRprS22FQYD3pJHZrYX3MxZZUBYWjwOv9oVyhN0ykmTThRjJHB4hSFZvCy30q8I1wnVuJ6FzDYbFbhJxKBfM5JIZcSpkoZljCml0D9BB/v5Ozi9u2wzH3uU6kFbfXpLhNA4lXHOrojteiIGUVIfartFiwZM+g46Acd3kRhBSlyhwE7qf7ZL1V5qdDVWtrhQs7qx6WqlBS6ioluK2jMqatH+p0boUKt26djFYVlmzLDb2d25Xl59kecU43e2OMhyV1waD2tk8081hHmW2P9lEIlZ17LfbDno89RjfxM2QYdmJe8FVns2JuMlhiHSF2G+RqtcN2l7EZi1t2jTZxfrKWocP7NChePsxGilWg0fwKuQwaGup6ewMdOLLb6U3BJa5500/IVl3bfJze+NNqxR0tPTbzvd/xqIRv1XO8UA8dRhUJh9+8uZv6/ejCjCobTHledea+IsixqIsRhgriiGSwNe6ciDwJpwMUHDNM5a4EYzvx/qpau/NJ3LC8QFIq7cTYthNyVW9VJK+oy26kLmcn8YZjwdCVySuebIq3uIcdTig7sdb17fbQBE7jSRiK4v0yprXBtwsmEBaE3yBKsMD8YZUJK0Q3Id+73hIisAzsoPGbvNQsubsSy+MlY9CAONb1iaUKlKLVJWY1ayUkyE097+TT/BodtpRWL23l0vgDVOg3QszC+aDjB4XZR5Hd4l6JDMWJajYpXJIaIzUEWkbGtqTH1qb5NNq7NGevMpYzl7s64swEOQm37fHM9PVhgUmaIsvdZs/zcOpE+OJ2kiGxkfxYXtNrgyxTgj8LmwuL3YTEjudqag+CcU6k2yo3K87vD2ntkJCtuew6J0vrmKlH4hjNVyi5wc9+gdv0zfbhpD6uGBy42sEaZy7HCLURz4emNIlL2jI83pz4XJDh07JB4O2ZSeTlNsANX4aVI1GPEINI+6hatqfwwNEaT0M6A+sl6+xW13nYFAFF0nzvhnYMHxrOtBo0YQZal0Zc3Mv7ay4sGRZPHAtHKY65MnJ9Ro5jXChMpJmjje+PdnmKlvFwDZcd713WG/FgiUvl2NYtKZee6qLboqUrXENNn+15irdGQy21A61EQAsrFk5cuOX8yz69UpV+swM24f0ijI5iqlCjUx6Fs3MVPNizNGeTw7sKuu1CCUJhAdRLWeF0Bon5tir0JWirRjruD1jfrhID210FXAF9RLPRMWwJkIoFy2VvpRsMqeBLe81QjPG8O10J1qiOsbjK0QVzYYu+wpacXK581G/F/aU1mPyUzvXizGPisG8pmnOI7T4Ut/uatfvyEKSM6ZBjw8sB5zdM0jv0saajoxaSkcCXxcVBIo7Wb85JcXlo6UEXXz+Uxda+YPNd5Ln9jmjltauOG1M5HjZhtx9aKfKIcieDVrVICpALiqK3yBrrQlG6njSVvvTEoN5KHxm4RGYrHwcpdROBNxQkUSsLh81Vd1WjVX4srzAqdSnGuupp3IBGs3L702mjb4/RfrvVYMy1R5i6wCzRG4Jx2qaVdU6EfUqEOS3pInRKK7qRdAswSZ1WjL3cjYfuwjtDrFIsmzrZBiXgljSEisKXht7JTr1QGdz1h8p0a2wn99shElH3GrcDdzkzLomdzmW6NTlnxUHtgbfcpCJZ0MEZjmH223Q80U3EBJm8lbODdm35KyXJXTtmZblc0Bm6hSyJxjzIOwXD4pizbKuZGCdxtm8TNZrsGeZU5yc5FFM0P/TJIasTXXVr7pBtj4ZU0mq5SFgO6/yLf/YWBYalnmEOO/lQzo/2KYyWphIcd+fuVl713OaO5OifddjOhFaLr7V2aJe3XAGlFS0wYtHEcy0zyDnFWvohwHZ+tFoHPopKhWK72/YM6twpXfhBcWFu9lG11od1IlrgP9yW5XYJmgY68edCXmR5CEuYZs/RkZS3PpPw2T4WBsE7RnBDu2TcXxJJxEtZ2JJZJtGiCUe8c3KUZmn3EkLyeqO6Hs0hCH9m8MUuHCo5LzD0FJOq6h1sUfKFA5wCqjpKMrXeGqfcNC3XSAt5XrANXVU97PMH1T4ImbELLjR3PVZlVeFLHxXnIS8KA7NBbNNCD8w+rbhIkljduQ1SeBJGx+7xQRfjpXLJStf2NAaX0Ct0WkZbuYAYuxVb0IghsuHlJxHy5e2RG6iIVspjzXCViBckaNn6lecGObQZ8pJlQ4Vfb72CXNQoNkoFZqh+V4+ZUYgcTAxdkNlbH667o10xV7fjfDP1JWIjmn6XeeXF2yHpmrWzUvLhkazPda31jg3rc57RDdrb0zSPEntfU0amEJoe2W3gghm4DZEXok4WtWREpsC4/FiGAlK2XGgPZIXKlbg1WHhReRzCFlhIqO4m5Yaec09cDgEnK9EiacljIo76FaaSs4pcEw0+LkWo2OzbytRFhMtw6NYFBkwv7c05LjUsu54X1GG5473RRuHBwwzvIChdRwXL/fVg5Y1fe46PtV17lWU23XYKkgYKjtRGV6Oj06sKtJZ3CTbvWn9YhshmZUkZDlrEBud6abm8eDQV04jbVY7olJbESaCDlXeOw4rQNrO5cpBuBrLXSMVylaNLLaAWRFNAnY2o4xGtPZhzmIiCpqwuezsW5nwFrdvo6uBdfY3dHpDv/Ej6W4iFjjTvbg7oZe5XgsdoZ2gUYeLqXyp3sXfGfu0zdr6yFu5la2b6AietYsRhuWGxdc6JcyYM54WqYFuTMexqDvlXtAr0BWC2PJ2HuLRJseMqo2CY2PhCTNkFFSY4RrP6OjaXp03rm/BxXjA8H/Vieg2Mkyo025IavfWgHHiVxw4BqkQ8qc7pUtaRs7Dyksbajihzo+0Uv9hshHpEJRVc3ggxng7BGl2NdL7kRd0nx2okr9iGQpaXINzBGywwiFt406+9uwsNf3v14oS4ckFkQhZiecY69844Li7iS9UvaHEBdrkNfrN7UdB2K5Mv9mUJB03hsMPSOV8dK9AsqJ2vhqGPVwc11KllxBRNFPjXkvB2wiK3r6GoSrFBELWKDrQi7pwxszMUvl5XgRkffXgNR0aAVPGN3QW3cMCQEQ5PfLXZKEhQ02tGCz2nM3r67N8SNSCk7T7nkrRSkD1L+D4aHYDP5FQLrwfEZi2x3qeGomDJxmcYYjWIGhtlJhbtXLhjpSgXNQi0BmYgEcOuYG+aSDtbB+IdJFZLgrDOw4qY55dT3KG75Yk+gX2li1urNjB3Wwq0uxt2TWlWe42K44613d1xz4KGT67qbLWTu31u9X5O+gsC3oVJnVstJGPO3k99tIM9n96Lt8NojvDqIHWEvKtiJdPINXS+kVeCP7GFW1cMpHcEhnl2gFIyL7qRp8/ZBTRcUGaIC2wty/zN3MXCOb4iuOt2aEmjOAtb0U7YnqT0gp9KN7YXUKdBY7Us4XOHX+Nju2ONriJ7zwo98qpe1lR3Wm42BgiNhiM2DqboVBIp3AAKAh9KHCfrFzvUturugiyjdGUG27r163inkOQCRnxFVs7b5rrCoYV5q5XWAfuhJXFqV1IRKcR86DFjd4tAjwzvvJZIhHq+PpoBTJD7oDPda9g4A9j5z62jdPaJax/OV4bX9BWzdqEN3K0cSG9o9LwH21yKWqBCrhX1gl4voU7elkaMntXFzkDORrghUJews8ghyRNdOdA+R1bYcbtTy9ZCWM/rxAYaWZ+o3cFuGTjGsWPoW9qSpE/euhDlmFWJTUTQWnTe6jK0F9kD3o606rtwO5p+6LpXV/Mrf6kMzn5jMiXjI0jnETqPk7t+9NlBPy7RozKezyLbc0JL8WgnbawMFA/K0Feau2irba5nFdWP6z0zWvZ1UQk60pTO2UZAD4IBnidK/LZ10W4VuBs+TKNh70mrhXmAhxHTy4Bt9t46o/bm9eKb8wt/GSl0dfZWxbHRm2CQaXddHxxAW7pst818eSo2K8TaR/Jxg8tGAhMFp3GLDOE2ekNsjhHENbIQisX6gt0QjDwpbDT3hr0J+7fGA9UKAyzHjuW5KS+QcNhsXj69TAfOz2Pjf/pl8HSS9392oPg4+3t7fXQ/Mg4c/8t9rS//vEq/fHqpvQQo9Dg0bdIueh4x/o8j08//6KXDNHt8vF+d3nIN7dvpeutE0+8GvSS53zVtPX5rirS7H9p+enG7ZvpNhebb83D65W5UVk7SfjACXMdJHXxrC2BOC769TL9KML27CfzEad8uo+cp8qcXfwTuSbzmG4KtvgV1OVn6fI8xHb5OLzJefv9v/SY2xIMlAAA= -->
