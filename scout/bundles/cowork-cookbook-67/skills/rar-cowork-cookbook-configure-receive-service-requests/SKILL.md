---
name: "rar-cowork-cookbook-configure-receive-service-requests"
description: "Applies a bulk configuration change to receive service requests from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_receive_service_requests", "rar_sha256": "5c609b9b374f8488e26462ff1ffdc4a487005d2df897dd0545b13a2b17edafb7", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "configure_receive_service_requests_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/configure-receive-service-requests:1e9fb9bcfdab44cb2f5d2a391619024a87bd84ffa61549db7798c4fc02476c90", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/configure_receive_service_requests`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `configure_receive_service_requests_agent.py` is
retained temporarily as a byte-exact rollback backup.

When Scout can execute local files, resolve this skill directory and run:

```bash
python3 scripts/run_agent.py --preflight
echo '{}' | python3 scripts/run_agent.py
```

Pass the real JSON arguments instead of `{}`. The runner verifies the
`SKILL.md` and agent checksums, prefers the rollback backup while it exists,
and otherwise executes the exact vaulted agent bytes directly from the Grail
record. If preflight reports a host dependency that Scout cannot satisfy, use
the `brainstem_chat` MCP tool to run the canonical agent in the user's
Brainstem. Never paraphrase the factory or agent into a new implementation.

Receive service requests Configuration Bulk Setup — Applies a bulk configuration change to receive service requests from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-receive-service-requests
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_receive_service_requests_agent.py` and embedded as the fenced Python below (sha256 5c609b9b374f8488…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_receive_service_requests_agent.py` first:

```bash
python3 configure_receive_service_requests_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_receive_service_requests_agent.py   # or on stdin
python3 configure_receive_service_requests_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Receive service requests Configuration Bulk Setup — Applies a bulk configuration change to receive service requests from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-receive-service-requests
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_receive_service_requests',
    "version": '2.0.0',
    "display_name": 'Receive service requests Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to receive service requests from an input Excel file, with validation and rollback support.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'service_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-receive-service-requests',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-receive-service-requests',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'd940a21f8f71b390',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/manage-service-work/receive-service-requests'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/configure-receive-service-requests', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ConfigureReceiveServiceRequests(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureReceiveServiceRequests'
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
    print(ConfigureReceiveServiceRequests().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8VaeXOj2Hb/KsT5o2cityV24VevKhIgBEiAFhBiesrNvu+b0GS+ey6S7O7OvMnLpFIVdbkt4N6zn985h+vfnsy2CfLq6fXp4JoZxJlJEgZuBZmZA9F5n1cx+JXHFviB7DxrqtBqm7yqn56fHLe2q7BowjwD2xdFkYRuDZmQ1Sa3tV7ot5U5PobswMx8F2pyqHJtN+xcqHarLrRdcF22bt3UkFflKeAKhVnRNhB7sd0E8sLEfYb6sAmgzkxC505sFK3Kk8Qy7Riq26LIq+YFyONezLRI3Prp9Zdfn59C8P3p9bcnOzFrcOuJfgjk7u8SHO4C7B/8wf4EyAgWFgMwSAauC7fy8ioFtxzXgx5XP9Vu4j1D//ZvcW9Wfv3z65cMeny+PI3/9m0GNcGoq1k3rgPZZmFaYRI2wwu0SHpzqIHOTVtlo6lqYM/Mf7nv/EYpL6C/j89+ujN58d3mpy9PORDhZoEvTz9DeQX4Ve34/WWkUvz080uS927108/f6NStFbl2MxIDUr+8Pa4fZMHCb0tD78b174Dq3a+W++XpO+XGz13uUU+w8+klysPspzvhoso7NzMz2/3p5z8jaweuHSdh3fyP6P5yJxy4pgN0egj+8/PNyL9Ck4dCHzT/nG0B3PpXNAHL39k9Qw9D/Rntm/3/C+kkzEAWvFv8H5L7Rxsmf4d++VPd/rsNz5D35YlxExDSlWkl7iv029tBYelfPjnfbn769XdA+p+SOeRtZd8ovKVmFnogMd7efvlU325/+vWXT20BYs0107e2Sv4RzX9k1xufHyz4WPXTj3sBfzWLs7zPoI9Ih37Li3+pfn+BtDH9v92vX6Hv82X8TKBRiXemdxN8lzM1kPU7O/789DuAiAxo09q3xyDL//VfoW1oV3mdew10sHMAQ8DBTZi6o/DHIKyh4yOpvx5EfrN5SZ2vELg7pjuACLNNGoirzDCBQD6MHh81yD3o67/bNyT9bD+QdPqOju7bAw/fHnj49o6HX1+gYwAY51Xoh5mZQPuFokCm72bNyPIWHHWbfu5GrkCi8I46e5ofEaduE/dv0Nd/zubtRvGlGEZFvmTAMyZwlwM1bgpg1azCZIDMG6gPjfsZICxAkw/sHf9ri5fROqfAzR42swGIuxfXbhsXSnLbvMN4/QzcXucJgP5mtGQdh0kCOSEQDJST4Q7qbfY6Evv69atl1sGX7A7FKHSvM/UULPgQGPr8uahcLwn9oPmSuXaQQ59++/0T9B/Qf7frRnzkoYCqcLMYCOcEEg6yBIHcbFOwrIbGwADAc/Pdb7/fXTFKl4HCCDIq9MZC14zu+S4QRg3u/nl3DtB5FNGtHpx+tBvUB8AuUNgAa4Esr5+/ZCOJHCyt+rB2341433w3/bu373xGn9QPGwI/3SrouPYWg6Mz7bxyXiDegz4sBdQdy+Xo0SCvGxC2hZs5bmYPYKfZfHNhljdQDTKn9oZnqK2BqiPlrxYgPRonBfBkNl+hLa2ASpcnt9L+qHxgd56Fo+Mf4Xq/DYhUn0CMLd9JvECSC6wJFWZlFkFl1u5tnWfeIwJUuPf9gLgJZW4PjUXdHX10y+lb5O3/rKGgf+hAlmNTcgDAU0BfWmQGY9D/c8Myyr7guD3LLY4sA7HScX++B9rYZo163zsz0DhAoPG4Z823ZuIdd94R+UuWhMA51fC3+0rvFlv3NXeUAzDgABTZ3+iPWV7d6IYNiJDR5VV1s8aX7B36n4FpgH/qUQWQyPEIC/kHw/Hpu6QByNbx+lsbAN2Db1QdhDVUtFYS2pDnus7NCE1Qjfn18AQIF3fMNZAQdvCDVhCgDkIB0IeAECGwOigPN9NJIE9A63T3wsfycGyugBROawNpQSK5L9BpjGsQmzVkuaBDGtcAK3y6kYJSF9gYiPhh4Towi7swY+v7ENAcfZGnZuN+74HHQxCjY40B/D4SEFA1ge+BLXvgBJBfl7tnP+R8+AoIm47JcNv0o7sfukLf16i/jUkIZPxWBUC3Ppb374wDkLtK61vIgcIb1yDNU/cRQCASbpX85V6M79X+Q5bXP/T7P/21keBWXtUfPfcKBU1T1K/T6b0EvlfAFztPpyBGwsKtv1XDz49k+/xIts/vyfYD5buhXqG/Jt0PJB5h/QrBL7OX2fhoA9iNcfv4AGPQn5fnz9j4dASZb15+hMIIcAB0reGjzrwvAcXGr1x/XHyvO/VYrnpQIW9wd6sbH5HwyJM73oCCUeff5e+o0+jXu9s+YBk8ykbAd8b2znfH2ScZxa/dp9esTZLnp8xM3f/RzDNiL4hWYI5xVgKZA/qlJnRvVx+903jx47B3yykABk7+OqYWqHOgz32GPlrWZ+h9iLgNZlkLpqhfxnZ5ZAmWgl8faz8mSct9AnNbMxSj6PfJaOzSHt3zH4UYMwpIbLtjJc8/UnTk+Aci4Ivvu9Ufici3L2bywIm6McfqCIryI7trIKfTjqgOnAeyDiQSwMcWbPgjG8BnDFhQj51R3W/2+6ZWftfl95sZmvt4+dvTO16M3+/NwT1wwIa/0MKNRn0vvW8jaXMkcGu0bja+NahvQL9wLLHfPfLHfuHtHolPrwBu3Oen0ZJVCGrY9TZQP93lAYp8a20BBQAcn+uxZZiCRAKUQCEvRiViAHrfMRhvh85t/fjl9c/74T9FgFfYpTyLsmzPMS0Msy3Ewx3ERCmYgKkZgplz0nLmmOeZBIxjlGORJDW3Mc8Gz0jCpkbpRl+m5kOMKTx6ASjwYer/RZf+dKcAigaCE4AEbhMzCkiJkpg3x+ZzFyEwAvE82PMcGzOxOTmbAbEdb06RjjPDMdyCUROxYNJ1TM8iR3qPRuEu1tt7R/7ulzsUvAH4TMNRaMQ07blNwphDkSZhu+jMQm0XRmCHRN0ZTqEekAID+z+2Pnwzuu6u+Ri3oEEcdRv5/Pbw9RiLBAZWrrGaX9w/9JTSTOs0tfbBZlIlk8sFJXaoWgxxZ7hlgSmO1mcrYiksrg26d1mxo094DCCmpQe9EbdXRtmvqaWHJFR/rcla3duZPExWvSksEDYDlskMN7vEZVhulq1aal1i0WVbmMWsUInW4RCnFFVY2VKmWBgiLPEGhkyME6autWPYUJOJdrIT7tQme+0gbA47q+HSAxzXiehLqYQy3oowEoNezVjdgOVNbZnFsHVcnAMu1w/TVWNfYLyIBD6QtcGT2CLxaCnVijLLB07o5x6KT6juGl+dGMXaq5ZOt57QbiS1YO3mUJS80RDmoXCquW5rouCaYXM42QWLT3dbFMl3EnFqxEHTfbjPEvN60q8JzYbyzheXAkEYh/ToT+WTh6iBW54rk8hyX5f2gb4aW3FBXGWtRPBElJyS0+mypSQ3150Zq2JRYjIZ2xTJ9EBV2wEW0+NSjAspcTh4iUausEnkizYUkUx5mzkbnPtaLRKGvm51SS29TeXVvC2Sp8uqAW6GmxSvaREUGXtDhZh+9NhWTsEFfjIk+lqeSpjdzzv8AJdCRYfxMcFzI7eVWbC98NXSgVMfNi9OmGwELC2qxJ8dvBwV4bSqGqMwTM5XmKuSLRex5ARCusplq2RgPpG67KBZE+ty4eWdWGZOihzNrhtWiIxKS9Izq4VdpytinzQZ4Q79gUNPAQuLhXnyzE5fOroWXqVDloBarEkqoYqnQAn9aIL4cb/n9KumInLLdn3GhJiqKzEeNcxujSp1jDNLEYcXG0OllltqaklNCSIM1p2qmGlrkYPlqYWLJrxn57vCE9e56qvI1tNS8NNud1qCcsfYOc5P3OAcE2yFE+IFl9bxzDlP9kYWnztCgRmW8KKCmWy7mvdndcU1DQkMZFKrOjgjlb43EEJasHW3yhN+w+eksV8bh6pdC6etGRQKtTTRuccMRIYs2e2sT46tTxgzON5oISaqfbspzA0326eqRsP+ZRcKVsCseZWJTsthg/Qrh682BVtg2lHV1MHi7foarNs1O7PbdqXTac1UFJIE8XqGXLes3lwvEmbbR2Y92yh9GO7a4yzUMD1NLSPbOPtBnshLFWWEw7FWJrFCXW0fP8i7eewfye1yrkxOIVY7yVyO92fT3W6JJjQ6QroGh8VwvIT88XSpI4fQsQQnA4woa0KTqrWSH8iVaMmrLT7Z7Sh4pyYLQStabo112VLMy6nBpda+PM+mU2rrneGT1uOxLvY61Sf7qk2C7Dh0yBVDYm/p6adunbC2WBU1fdyxSwIuTkN9KFtCJ65wXiY7n6/VJpSz2PHime0KzqaEeU3A2XjKmlPLj9j9dLrRhC0248vjZAUMScNOsnRTRMRnSlHOMXi5wLImFrvl0jhRpw6pd9djECrsQS9WWrDJjq17MJVrJAmF1sa4WPEbIccZWp7QA5ksuUmDTUujhLnwirdBlB2TlbXTz7Zgt0u2UtypsZMSTQ4WVAy7RJoL0zNeo3Toia22adAJ2SieR9ld5y6OoYGj2zg+CvujUxmyMrAdCcfZOitbCo6j3ZByrp3M+xkteWLJbSJnOV+aWM9K8nGuH9f9TsbOS/loG5P5dLNK+yQqNLprTVM5GlxXTBcYT+cM3DtEqZ35GJ1EJ3+36LlLTDr8YhPHMn2YS1YagdYbPdm5wy6K3cLgEkM1sAGkcyE6NusaVzOwawVbbZbeua411KDzPdnS3VaSJ4bls+mxluKabSIaJybRbECu6/CEH84kKNOe10U+5aLaZR/2y/J81Vq5IzDSP0RwOZHOmkHqzBmDjRlhSgtlmgk8wEpnN5DZgeF3JN91qB9n18GdIvoEn3sCDs+5/ZSz8siK5jWBSlbNzgNlduDZrWmQAkoXYozmExhJjzwJSw4qlZtkVftzZRVzean7HHpOdQ3mjmpK7zw3pthF7M1NUyhnk/mZ0J0t4biJM69m9kndYvm23PWhieQXxigomBZTGmW36/Ci8+UJPcdqqZA5uuKMVvVoXyb0OUZqqtHBRHfoifMRwG9OuipliCcqjq5KFy8yup8ZJTXLGhm2cruIuP1pR2DB2Q8bYX2xqiaQWZXzEtJhBjs8O7vWuQz+gTsUu6t5Eo01fp7qdlTbciget7Q9B1Hhdoy8WOYVIjJg1Oo0ac22iVlFyNLX7NmEDhaHBW7P1sNpleyWHSUnjot4Z0U/ttl6s48GZN5uVlvdTvC1uWnZCR4sZLw8px3anFx4yfCr+VJXHE6v7HOxs+0Zf10hjWhNpJjWmFDFTEqIFq2vJ1uxTaskisgeTTrtiu9yii6HpO3tyF1wxapbXM6bFcHrjLFqu+OcFX2OshRVBqi5d+AYycPI35byhT2J5DKVvLVSpBPOKuysoLnYmOiJzLA936UTE5sdhbThsopftIOGUmCowg8hN13vPI3dNDPCWTHlQHHeYQ7HRoFvTGaqJeeMz7lLO1/5C9E4om3tl0idyDmo70ttqXacui7QXYytaFs4wC6fchLs5KExNzRevJYAQi7CYPPHs1WkM/Pq7O3LhuUSvosWRDfIu57dMUI5zMkgKKwJu01ZUVrWM2ZChghCyQ0x68/y0sZJk197NC7UctvYZxlXDwRn9seLRUzbeWZNe9WHJT/Id7STdaZDTbM+ShGkc/bFTFLgJiIoQxfgVrZ40ghJ7lB2HI6esnC5CrDJomYwM1JadrWb8gvxTLnnrbLk+kMUu9Zisk/3R0vd8Jk/jULKiQvqlDCn3YoKqt7c++127qdq61+mQUWzUlpos0yDi3SJSX1BH9aneTMkOWqX+JCmqbppdudL1IMgXNO5Qm7aE7zMsfgQ+I5SIAKb4RLKeltbxnnMPfjXGXLcnrfHy5Yu98xyyJCTeFS2GaUZR21+ospArWuUtwYBv9LZNFhtlViQRanhr9ps18XwatHRbKUdE27Y8dvA41PLFqqMiDlngcR8LzBlHda1w2QHxE8vm70PBy5m71GWFKia3HXsRlpgUdsOZ83NOlHNmWhzSNu+PaqcFh6Tc0cXMRnZwUlvYavvgYFSQSubBRp7sZ+p7aROQb86kxqUTy4OXucatYoFzW0nTZxO1DSRNEQBEBUdC7iZL9nJ4EzEYUNGqyRLvVpc4StUC+jWESbCbl5ze1XyYnnh74Spy4a+JcpDXRyraNAGJlZbaYbR2LJl1o1jrGfhAihb1FZSTFWijJSz6xI8aZPMCi/MrUHLFVKoS3XP5oEJWxVKb2LyanD94tQU8mSh5glixKWc7S0sXx/LRKb5Qk/3aj5xKrRl4NnO4pRi4oSCFF5gVpyhuThJdvYlCid4lJqbkmlZMzkUaXo1M5520CtyQNNkSWv4Gr80hsKDMpGfGWZd6LuEqyLVDmJxGSYObdg2shDOdJmgQ7gIlTlodAleKbjJoqNo5podfDk/NjAYG3KB5aRapg54p7G6QmOlhOYlDhM0cgnNI0YzVtdfK5FauMssqxJjRi/3s+NV73f8VBJWdbRYGJk43V8NRdTFOCzoHcLR2JkR/LzOFnIgzrETueVxRo4xqlfpWYui51k7sxlVPswWS5O5ahWh9A0MN9ZsWQYHVbhs5ImSmcIe9JXRitgIGilItVKJa2a3S7Oko7d0JVZZunIL78IScyFA9K1i7OZg5APjBB2Ki6DRL6rTTHcdU25n51yzaeF6tRG49eX+hJ+wYU3iy07ehN2hoVrYA6UbueARaeruVKbI7nqxs+YCNxNccpjKcoea8pyLk+z4w6aGfSTTy3N0KCUZVC9lv/FP20gPAapFpVPIaUBgjMXP0wHdHgLNiY24cBV6swinE3TQ63jXFine61sdhc+geMLojKWPtWwVm3l0zaXVWfCORUjWtlKd5Wqd5Zuakrsz0/PD2hMRbjK3anJztWRux8xzhRkM05JBy+40FuPbXtZNUYKeYrQt62fTQ3V0rnvHZEmWaKeCbpBB6wTxi25BLvVh7ZSRP4+OedYKLr+U1vBwvRjT3Z7Y7xkiueJY1AcNK6+VrTAspot5wWy52WkNMj1zdRprVFRBbbKI8nRvCW1piy2gLzfWRlO3ubRELWSOL9FAXrjHM0esAiFZezM16FJt5knJBq5kcgZ6Og/rCHxORDUfX6lJL0f11CKrnJ6c14pnVJzqa7Ub9q0xbWdkj/emHXA1kni6ukc8+mJyE7iMalLfm8qkmRpgiI34OLTaJbXYngR2kip9K7fX6tqsUJg94CbVlC6+X5n8Er4YawNpCsu1zEpjbf0oMzhzrHTbOFoUymUeb0R8tulV0iG5GmWNiTCs/eQSXtpL7PqrErEvHDVcp7qec6DuMT16naH20VZbfugUjcemTb+c4VmzZn3dXl2qhrdc4YLPRYy2JpmNlxh5LclQl5TeKNZVn1zclbVWrqayjmB8WyRbdOGWCyxJc6lrQiueh2CE3MI1vQdjIrpv/BjHtjVJVLVydfxFpVVnilcUOHGEzWHPC960arkmlcnDlT02RKbbVC5sVdu4ngynQC4e3SJ+NpQrF0EjWpm0RmVVVS41mXNpyX2D+LsmyXilWuer6eHMwT1ODBPfmHsIc0SuoXKM7OlGXgiX6gAjnGEuZC5EK5MB46tttcHsStWhBR+uqbtvTHwN6oDTXtwst+tuj8xVygqwg7reyx158rUJYnHzLSMusUy5JA5oobaMP1+Tfajq2onKGbtfxynJImTAoExzVWtYX18yZGooYGxqmpa0Kt9DA23uhwI+bWWXPE3bw366M0Nt7s31oJpc7bnCIsEl01ZbEHHSZJeeYOoSklJDTcLplNGFYjvtZDyUKIrv9th+y65dVZ0sJJcra6S+cgAqeCqrNKs2cszILbI49d4BnkjXhbQQZBuWvNXxOnXEc5TD2416pihsPhym8amr4JOIR66x5xkN889q4aCrxXK2JRV+wZ37rSBUKc7bV7t3FvKR1whuvkzKjecQoh5F8XaalL57XqQ8WYPoJ5II2WZMgHZGc9QD3bsifO/GYKTZrUNitjxZ0/Nur6GJ1C4jlZI3si4MCaZTsSw26IbQSLXu7JZBaNv1jpJRlfjBuzrxwT0Mk8uSafG17kgTK9sEcnFtiioz+ksRTwPYcc8i42V8XfmVuCnRdZg0x2nJgjYlz6Zmkc6pi+xe0+zUY/Nl4+/2pCx1IcPupK0fLHly6vACVQobIhTlzlljxcACbK4Oaxandxt7vba6nRxc50tyrVvWlhD9xeLp+el28vv0Cs/m8Oz5aTwreLzx/2uvi/1rWLw9aKEkTjw//d+9yby/VXw/D7y9/ndN5/XG/fWviPnr81Nlh0Ck+yvmOmn9x+vL//K+9vM/f4s87h/ux9fj0eWleT8waUz/9po7zJy2bqrhrc6T9vaSGxi7rcc/YanfHocNTzfF0mI8ufhgOVJ+qNDkb48/vXka/8ZkPJBzndBs3Mel/zgVeH5yBuC20K7fUAJ/c6ti1PVxNDW+2h3Ppp5+/086B46toycAAA== -->
