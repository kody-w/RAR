---
name: "rar-cowork-cookbook-dashboard-define-product-policies"
description: "Produces a self-contained interactive HTML dashboard for define product policies - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_define_product_policies", "rar_sha256": "5eabbc8a4aca2688163d7786093e0d763cd49b02d2b844a11f347620308c9e28", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_define_product_policies`. The original RAPP
agent is preserved byte-for-byte in `dashboard_define_product_policies_agent.py` and in the RCI capsule.

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

Define product policies Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for define product policies - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-define-product-policies
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_define_product_policies_agent.py` and embedded as the fenced Python below (sha256 5eabbc8a4aca2688…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_define_product_policies_agent.py` first:

```bash
python3 dashboard_define_product_policies_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_define_product_policies_agent.py   # or on stdin
python3 dashboard_define_product_policies_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define product policies Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for define product policies - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-define-product-policies
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_define_product_policies',
    "version": '2.0.0',
    "display_name": 'Define product policies Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for define product policies - opens in any browser, no D365 access needed by the viewer.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'design_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-define-product-policies',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-define-product-policies',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '00e901a3587309bd',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['design-to-retire'], 'process_tags': ['design-to-retire/develop-product-strategy/define-product-policies'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'design-to-retire/dashboard-define-product-policies', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DashboardDefineProductPolicies(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardDefineProductPolicies'
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
    print(DashboardDefineProductPolicies().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/816a5OjxtLmX2H7/TDjVzMt7pc54YhFQgIhbgIJEB7HmDuIq7hIAq//+xaSusc+Pn7PccR+WE30tICqrMwnM5/MKvrXF7fvkqp5+fJihG4J8W6ep0nYQG4ZQMvqWjUZ+FVlHviB/KrsmtTru6ppXz69BGHrN2ndpVUJpmtNFfR+2EIu1IZ59Hka7KZlGEBp2YWN63fpJYSEvSxBgdsmXuU2ARRVDRSEERgG1ff5HVRXeeqnQM5nqKrDsgXTgTID5DXVtQ2bT1BZQRxGEpDrg9VaqAzDACziDVCXhNAlDa9h8wq0C29uUedh+/Llp58/vaTg+8uXX1/83G3BrRfuTQXuvvpD+U57rg2m524Zg3H1ANApwXUdNkDZAtwC+kLPq4+TpZ+g//7v7Oo2cfvDl68l9Px8fZn+6X15V6ur3LYDWvpu7XppnnbDK8TmV3dooSbs+qa8wwbALePXx8zvkqoa+nF69vGxyGscdh+/vgBsGneC/uvLDxBA8etL00/fXycp9ccfXvMKAPHxh+9y2t47hQDgH+/+ef32vH6KBQO/D02j+6o/AqkPJ3vh15ffGTd9HnpPdoKZL6+nKi0/PgQDT17C0i398OMPfyXWT0I/y9O2+4/k/vQQnIRuAGx6Kv7DpzvIP0Ozp0HvMv962Rq49e9YAoa/LfcJegL1V7Lv+P+T6BzEVvuO+L8U968mzH6EfvpL2/6nCZ+g6OsLF+Yg1RrXy8Mv0K/fDG21/OlD8P3mh59/A6L/rRij6hv/LuFb4ZZpFLbdt28/fWjvtz/8/NOHvgaxFrrFt77J/5XMf4XrfZ0/IPgc9fGPc8H6hzIrq2sJvUc69GtV/6/mt1fIdPM0+H6//QL9Pl+mzwyajHhb9AHB73KmBbr+DscfXn4DDFECawAHTI9Blv/Xf0Fy6jdVW0UdZPhV30HAwV1ahJPy+yQFxNTec7sJAa5tCoB9jgPxP3l40riKoF/+t3+nUUCIDxqdv9Pftwf1fXtS37c36vvlFdoDwVWTxmnp5pDOatrX0o3DspsWrZsQEOHlTnpd+BkQ0efpy0SUv/xb2d/uYl7r4Zc7xacPftKXm4mb2j4PXyf7rCQsn9b4oCqEt9DvwQp55QN1ohTQ6idgd1vlgNK7CYs2S/McCtIGGF41w102wOvLJOyXX37xgFpfyweZYtCjbLRzMOBdHejzZ2BXlKdx0n0tQz+poA+//vYB+j/Q/zTrLnxaQwO0/vQG0FA0VAUC2dUXYNhUQQD5usHdG7/+9kQXiClBnQO+S6Op3EyTQXRmYfAGtSGwn1GChLwQQAzgLeqq6QBDQ2n3Cm0i6F1fsOj0aOLwpGo7UNFA4QrC0p9qkgvMeUeyrDqoBSHYRsMnqG/D+6q/eI17V7EAae52v0DyUgMVo8rBf5Oa90FgclWmAP73QHjcB0KaDy20eBPxCilTPEK127h10rjPNSL34RdQKd6mA+EuqJ7Xr+VUHMMJqntyPOABgwAy/tOlnyefg/pfACYI2re172Pcqa7t7/Wt+Vq2z8B3m8kVPigEYNG4T4OpHPzjGVJtUvV5cMcPaHov2w8vBE+v3GOQ+4u+YPPP7cR7LYe+9iiM4ND/V63IZArL8/qKZ/crDlope/34gHhSa3LFowMDPcFdh3s6fe8T3ljmjWy/lnkK4qUZ/vEYeXfMc8yDwPoG6KCzOvRmdnOXew/aKQibZjLJ/Vq+sfongNOdwoDfQIaDDJgC723B6embpglAa7r+XuHvTgbogbAAgQnVvQcggyIAhOf6GdCqmRLv6RcQweGUhNck9ZM/WAUB6SBQgHwIKJGCVALMf4dOqYCZIOeipiq+D0+nvunhJqAt6FfDV8gCuTPFTwsSFjQ/0xiAwoe7KKgIAcZAxXeE28StH8pMLe5TQXfyRVWAkP69B54Pv0f7XZdJfSDVDdwOYHmd6DcIbw/Pvuv59BVQtpjy8z7pj+5+2gr9vvz842t51/Gd8UHa51Pl/h04EAjkor3z7MRaLWCeInwGEIiEe5F+fdTZRyF/1+XLn/r6j3+v9b9XzsMfPfcFSrqubr/M549q91bsXgFnzEGMpHXYfi98nx+J9vmZaJ/fEu0Pgh84fYH+nnJ/EPGM6i8Q8gq/wtMjKfXDKWyfH4DF8vPi+Bmfnn4t9fC7k5+RMFFuPkw5/VZ/3oaAIhQ3YTwNftSjdipjV1A57wQM3PC1fA+EZ5oAfi/jqXi21e/S916IgVsfXnuvE+BR2YG1g6lxi8NpU5NP6rfhy5eyz/NPL6VbhP/JZmYqBiBWARrTHgigDhqhbnoErt6bounij1u6e0YBKgiqL1NifYKmBvYT9N6LfoLedgf3DVfZg+3RT1MfPC0JhoJf72Pf94te+AL2Y91QT5o/tjxT+/Vsi/+sxJRPQOM7wU4l65mg04p/EgK+xHHY/FmIev/i5k+WaDt3Ktdp95bbLdAzAM3PJwj4DuQcSCPAjj2Y8OdlwDpNeO5BXQwmc7/j992s6mHLb3cYuse+8deXN7Z4+uDZI4LhIC0/t1NlnIM4BQuC60dEgWd/v3t8CgAEB5oXIIEIXc/zaRd3fRclaRohsYCiaBJmsBAOKBLzA5zxYDRAPRrHXQSJMJwiURiDaZ8JURrIewTmt6n+p5NSqOv6tE8heMBQLumHGOxhfoigSEABmQSDRTQd4gCf96kZYMenpQ/LJhjfG9kJkafBv754JA5GCni7YR+f5ZwxXepIeUriMRQZxecTTcNMM9QKilpoOJLCbjB2MuzuOdHL+SzJarGTUVVaVqmia5fjhp3p4uy6p6SSzlTD8WcZZW0XnsOiXZaEdkdqPj3LhZWtk9L6OOTb6zl3iOyWW+eDWByKE9pwRkrUhW7iIjOPGkKZXW/IrDvQ+7q8zCl6iXU1gcqhg1SHAS0Ko5WTLR8MPbe4rAfCHKMNxdTtYB5z4ziWJ8Jx885rrKomr4dGEEpsRLeh7ASd2q6XkiD2hVV4Zmwiop+OVXg6kJHWwHiENeTscr2p2Pw26yWqkDBeXma50Sr4kXHPeeE0yn7RnM2S3xLUNq6phKfz87ZAztd9eNqdj0hD+RrmG7m0Mo5xXO56t0iusl0vdl3ZnJGja0nouFpc7UAhZvyJM6jsgGa3uBo63SXzrXk+tatzr4Am7wS7XMnXbkqNnJobCVHsciuFx4XfjLKOncJaYi2L3vBbn+4rXc5UYXZYZo5pYC6TdzlJjFc569tusJzdbtHQPoItnSV9GPOwRyXRKlB82OeVRNzGqtddJFVyDAT2EfNZ4mycDoqPLWg/sFZKu0G5Y9QdPdNFcGJv6oxr2idHmCH4wYObA37aXoUTbgPqXC67zZEqMY3TFfcWEv02oFGjKTFfzZWRZWS862cUItL6mRjIo72nfSvA8PR8ay8mfdA25knF26uuInxG8jcdK2rUrLtkQ9vhGkcCw4kV3wnR46zblApa9zd9JAxyr60iFavyUC7CY9yKM6QQr0OZ0etzIa/67jQIY0n1s6JREdmxwhF1Hds5EYHNF8pJWSXbYVU2Zq3Yh1qJwM8OrhEnavacXl7gGXKJd9HV1tANR4r7kRtO/nWlu6c5O/b+3puT0aW2uQ3e62rgUthNVDrGwPtzm9e23o5sjrudKZlHWPVWIVzyiG4sTrzYG7ND2M0wmHR4UEIqI7wuZ4y0tU8ZFwbtjMva3ODd3WAu8ku52+rkwgj4WEL0rNrT+4WEpgoqk4ulPnbHTcOf1KqubQDSWaZVscIzT5rn/FHY07WtyYqQFjTspRdxjXvDfsGj8uUa9Hoi3OQ8HjWfLJq4mO1bWbvcZqaVlazFNBfaHtYIrAjrDVlis2EzNFxA155Ajnp8hA2Q51Vu6QdFELL5UeVhWFFAW7FakjCn0Nja4LXeCq7RYu1K2XlFqoaVJM4SqwvK2+j9Qd8kPd3o27NdFvNkQ5T1YhMo+hpV1ghZc5pinzvKaO26sc52pNRDLI1rA93Kp2IMlNQIkl2KhUq3WIjklq46ubOq+RLnioEDahAMb69FdMz53ukdQ5wrO+3McRSa8KOAIYlhb0WPW803GbpTStPcUZegAi4lybWiDoa+ptyFxO+dfcq3PTPyXCfXcuqCxI/75eCPnmXoK0oqOnNw0WVojYesom6SsjjwHoOdZn1BrepFN9I31VFhrQOBgUcItSkyoRXEk4OwpnJhg3iG98tIFwNl2bkMQh0070TOncvMyXfzrUQL25ghK35Tro/7PZpn5UYzFr6zSfL5didh0sHhUrvkfLXF+fYYD/oa8S55u4q1llLRdRTJ6C3NxnzfH1GXoJnwRhzhxBe7dN4dct9ET2XMdeZmE/GLzeXAG/PFhV05Kbv2VSW+sn7WbnRZPy8Pkr++LLHzqd6s9rHQw9WZzJOk3inioTPsHidHVeAc1qiwWIqUJSnGhuZcTSy5YBcpXGZLF7E7mW0IW2i60jnlQem6gsE7CMK06NjOZbuhCVGUUhNOxBKL8NvZ2HO0EJ5NsWWWuzBNY5xZzrVTOe5YSvJKdI3gFRsTqr6OSm6MAd+THU3P1ShLub29lvDa7aRDg90yb5WxJSqC9ZSKxo8HayGKQ+/ozuHK+cSl31jl8oDpi+vSM9z25sft4uQoG9cvaq7Q7JUJZ3OjWzhMDXPR1uUvV8xdzlzdGvr4lu8OAomopzqhrDWF1CZ3Vce6yY+LYX3uztkVyUSYCseeEG9HG9nunN2KWcy1xWDzJ6LrnL1abGG9m+We36jooNlYeLoedxW6ukRGIcUZgcg0FW+ag4POm8XttBDdGBTIy2rv4GYMSAk7olTdBtqRZnWPAEFzS4714RLMBoZRUQ5ORb5EOrA3PbFWdlrDlSM5vphUOszHgB0daTVIKMu0m3gpO5moKlq3P/EsMVvMm00J+p4CLXhZUOV5AZ/IFElYij8clNFYVLDbGtw2GrCiaceEGs1ET9d0ejDELNmPq62+OJpJlsCrHt0rFr31ZCTHwzgfEjo3BlbtaMep/e3pKHm8x9uFyZbFKVXHfXQwyYt5WHv+dlcol6UBnFiuuhtSbMs4SRN/KDp4M9PbCHVSNylhhFFiPtnajY0FXojkaCCOhqmZ8IlN3Wxt14OkA0G6yxqJT10s/OyXBIeer6FRHBozsRn+dMCqYdXTw0EvUUFaO0vNMPc3fcdIQw/b66Ph4zp2FIklvNq4xDFbpbvKOJIAI3GxVa39utlqPVXCCemtFFY9lBHlCOhwm+eCbeAEL5WpzPYUS5iwp/ZxXx5y5IAc1rKJDbAQRCVFoeZ1ZWnYFp7fFljFRuhobJdH0hfKy97FBEOqTSY8l1fq4hCONDhqzTRecKY1p0+5laHGVjoj1avCo2xrbvhx1yg9asWXxFkn83YNGrCNM6zxmWEOc20kTx4fye5libCH/qRtTb8rbe0abkg44Sz5rKa4nATXi9Rpu0ODVI1fu+Y41kZayXu/R6yrGO2klN3ISaREtFFtF/BhEJx90awUP4uszVrqkMOCK4s12YjNcbEn5GWxO0kGtSuNjROhGZYKpWAQ+xCmSWP02YtUZt1mrixxuDQNmujOgy1xVdw1xjpY7fArKATIYiT6jvP4lbEiQkPlAodc7meUpGmeF+wOC0W8DSpVOlIMl1sVVs1UHoDhin416mTWudJsKYeBVWhkRp1VN+tLZ6jXS8zMRXMl4htrXFo0kmcUGpnVHl37KbMYsx1/KnExtBurlXgZx7Q+Ng4I7YQ+jDVlU4kXRHQ2rurMBctwfe98Y/MgDebbukEbC0bCcHVJYy7qjLVFFBu9QDaHfZJst/BG2IYSfDrndMU57mawaslpEbE7G0Qxxly1Pmshgx23u0sR8IrdLsf6HJYrHMdNYYft9i7dnK1EXC3D9OTGIsw1DbtYxde94desRkjBLvdRO0/D1NpyMuihNmfLJxDPykk0YmZBd1AXRi7v2465bjjb3m44TYdReRjsQr2U6E6kYWoTqGlSwMh+tbCGcJyXOb7RG62DPUHT7Wp9zbFDssSw6rrN+U3GVrNt7temXgWs7N4Kbtt5iHu1ZHqDzwlGyOQ2lvhLN0oosWx9KrKTTbUb2WTelHlyvHggmVV4iSHMajavzhXb8/wiyZkFEZ24eG6aSWU68HzwKr7b6WzQ4XAeDHrKilLjVQRfdFJ2cHZyTHKsL3PZdR16MSvcjlZJwts1p2Q4vDW3MAraVLpAWs5c7NCYOivS2qMaX7q1znUtD7vYPlSX2y3wFgk8Oy0WqLjlxo4fPAPl+AhZiWK4OuaoYktMIQn2ziLC2zjCJ3VekaQ/SypHN/kd3jZovUTwpt7to42hhgg3Hsu2DBo2ZYb6epmfVQoJLpp0brbdvEXU27Vi3G3ZX1WOpNazBuwnsaOwplVTZYI4xi2mDVdkih+WpJtgoMNzfePsBiu+ajbqaYhwuV80zrG75eMBFgZQySTP9DKG7pzlpvBPVsmL+O7q23OLBNtcljsoJejArNtMoAyB7+kqZu2A6yUMkTKbvvh5YJrxntlEza4SlKZijrwyNx3PIynOumZKyeReGMSCc9Qa3feue8Kg0KDSkFDdE7PtbD7fDPPNOl6bRTNnDvNbR0R7rO9DB3BahUTGJbgWdFmJ3UqmAkAVfZhYsCbaXYGKtqDkGrm+DNvNQqbmqX5QcXbrB2q4utUJCAqOJxT8rB7nYhnYBt3C1x7zG6Ks2kV3QIK+E3RcXanWFl6Ps/UuGMhLeKCJlF5mxaJNHMfTMYTnveHqRSeVJVuzw7U5oZFScmnbSpK2+MVL1rjS5R2GrueqvbEdjz+wcD+LT8zMEJr+Cvtg11bJ+sxNySMTtroLtkve6eLajqHNujlxu+EJodvRXqdYWRdXDKXtPVJIKnUM587gLZscvQh71vJ3oJoQvdO4Mya/RZRe2mMc9/RlLVxUniqosvSlhEkKPF7O5aErM19ikjXV4tdjT/NiI2pV4+7sVj8FbXTLyYWc4DLrg8oS3vqBn4mgCx7CED2sSFkhhtSQo2XtdWzXHEHbufB1iQrazsHP1IlitTI+bpHTGjew+TIVLtiuFG/0XFj5txnOIcf1waobj8LXXWhxOmvxJFv5q4PXjtdwu+CqLjmvAUbXzDx3/S7TToRHSqDJwGMK9MkIzaGRFvJSkChEj/qMKcnj8WqlGLHrzozGtIlWGjwdlMUqIvsbys5t2CUUr/SsU3RZJTpXknx1vZrz6ji74cftkLAYTbV61torp8QAN4SofPNGzMJ2BNtb6ZXaJg1AZn2xCMKc2aqiYArm4qa0GxHqnLWChDmgOUfp1fIIOsOt1MfC8mIs+1N721TcIEeEOETbam2LtCbUWtUPHpkUTBMtVmiPXGMsYV0hvJQYd71YFkXN7ZLypFlKgi4RtzGmuO6EGUXMu21CJDzjN/zF6m8I0uOaPRu7pWd1PNWc2hmjYyvM2jGXmNIqZpYy8zhZaYQNSx1TIIwgS7dcywRrta3itZbrXgD2uHPatxdnpRZOotv3fk8vGxyjVgwHw+x1e0gYOxqvVwpdpqtjhwmZ37c4LbkUYZb9iArRjOrP2qxp411uU9qWE0C3GO02mn44bvGDEq0Ku/XRmq8PPM31ALOunjGdgp5AU5Yfs8WRPWtUFekEGe9RXzvhlZSiYnPTsEIo2HV6XfvSPvE8VlBI+SzXF0TpjSLmA9VI95wwVB4b7oVah0W0JULRoVQZH8JuDBzbYzFqHi+kuKVqO47iDBHQ7d5gotsxmRfrS+DBcnNB/VpTF+flEcudVXOGV37Xm5pl89X+bFPDLowCHwTnER5ooYwVOCOVtTPQleyA6glL7L6htbiZV5kkyqAnhGeDuq3mkQ/ro7Bx5l6kk8TIVeF8F9klqI6RkbEs++OPL59epjPo50nyf/76eDra+392wvg4DHx7p3Q/RA7d4Mt9rS9/Q6efP700fgo0epyjtnkfPw8d/+kU9fO/fRUxTR8e72Snl1+37u3MvXPj6W+KXtIy6NuuGb61Vd7fD3I/vXh9O/19Q/vteWD9cjerqO+n328rPk7C07j81lXfmrBLm/Bl+vOD6YVOGKRu93YZP8+VwfgB+Cf1228YSXwLm3oy9PluYzqNnV5uvPz2fwGIXpD5yyUAAA== -->
