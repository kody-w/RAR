---
name: "rar-cowork-cookbook-dashboard-send-knowledge-article-to-customer"
description: "Produces a self-contained interactive HTML dashboard for send knowledge article to customer - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_send_knowledge_article_to_customer", "rar_sha256": "17a3c3c6b5be20f80a55f189c14231503ccc14723d4692c7d9e3f21cb8afad79", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_send_knowledge_article_to_customer`. The original RAPP
agent is preserved byte-for-byte in `dashboard_send_knowledge_article_to_customer_agent.py` and in the RCI capsule.

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

Send knowledge article to customer Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for send knowledge article to customer - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-send-knowledge-article-to-customer
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_send_knowledge_article_to_customer_agent.py` and embedded as the fenced Python below (sha256 17a3c3c6b5be20f8…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_send_knowledge_article_to_customer_agent.py` first:

```bash
python3 dashboard_send_knowledge_article_to_customer_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_send_knowledge_article_to_customer_agent.py   # or on stdin
python3 dashboard_send_knowledge_article_to_customer_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Send knowledge article to customer Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for send knowledge article to customer - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-send-knowledge-article-to-customer
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_send_knowledge_article_to_customer',
    "version": '2.0.0',
    "display_name": 'Send knowledge article to customer Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for send knowledge article to customer - opens in any browser, no D365 access needed by the viewer.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'case_to_resolution', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-send-knowledge-article-to-customer',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-send-knowledge-article-to-customer',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '468f32be08458c18',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/manage-and-work-on-cases/send-knowledge-article-to-customer'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/dashboard-send-knowledge-article-to-customer', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DashboardSendKnowledgeArticleToCustomer(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardSendKnowledgeArticleToCustomer'
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
    print(DashboardSendKnowledgeArticleToCustomer().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/816abOb2JblX6FufbCzsC+DhBB+8SIaISQhBiEQg0hn2MwgRjGL7PzvfZB0rzNfvldVWd0fWg6HhThnD2sPax/wry9220RF9fLlRfXtHNraaRpHfgXZuQcxRV9UCfinSBzwF3KLvKlip22Kqn759OL5tVvFZRMXOdguV4XXun4N2VDtp8HnabEd574HxXnjV7bbxJ0P7U6iAHl2HTmFXXlQUFRgNVCV5EWf+l7oQ3bVxG7qQ00BuW3dFBkw5jNUlH5eA0nArhvkVEVf+9UnKC+g9WxBQLYLFNdQ7vse0OfcoCbyoS72e796BYb6g52VqV+/fPn5l08vMfj+8uXXFze1a/DTy/rNGhUYwr/ZQT/MOBXM0wggJ7XzEGwobwCxHFyXfgUcyMBPnh9Az6uPk/efoP/4j6S3q7D+6cvXHHp+vr5Mf5Q2v9vXFHbdAHNdu7SdOI2b2ytEp719q6HKb9oqv0MJAM/D18fOH5KKEvr7dO/jQ8lr6Dcfv74AkCp7CsfXl58ggOzXl6qdvr9OUsqPP72mBUDk408/5NStc/HdZhIGrH799rx+igULfyyNg7vWvwOpj8A7/teX3zk3fR52T36CnS+vlyLOPz4El1XR+bmdu/7Hn/6VWDfy3SSN6+a/Jffnh+DItz3g09Pwnz7dQf4Fgp8Ovcv812pLENa/4glY/qbuE/QE6l/JvuP/D6JTUBT1O+L/VNw/2wD/Hfr5X/r2n234BAVfX9Z+Csqvsp3U/wL9+k2VWebnD96PHz/88hsQ/V+KUYu2cu8SvmV2Hgd+3Xz79vOH+v7zh19+/tCWINd8O/vWVuk/k/nPcL3r+QOCz1Uf/7gX6NfyqVHk0HumQ78W5b9Vv71Cup3G3o/f6y/Q7+tl+sDQ5MSb0gcEv6uZGtj6Oxx/evkNtIoceNO699ugyv/93yExdquiLoIGUt2ibSAQ4CbO/Mn4UxSDDlXfa7vyAa51DIB9rgP5P0V4srgIoO//y723VtAkH60VeW+J36Z2+O29HX57tsNvTfHtrR1+f4VOQEdRxWGc2ymk0LL8NbdDP28m/WXlg+bY3Rth438GPenz9GVqnt//ippvd4mv5e37nQziR9dSGG7qWHWb+q+T10bk508fXcAf/uC7LVCWFi6wLIhB1/0E0KiLFDT/ZkKoTuI0hby4AnAU1e0uG6D4ZRL2/ft3B1j4NX+02Bn0IJgaAQvezYE+fwYuBmkcRs3X3HejAvrw628foP8N/We77sInHTLo+s8YAQv36kEClBO2GVg2EQxoybZ3j9Gvvz2BBmJyQEIgonEQ+4/NIGcT33tDXd3Rn3FiATk+QBsgnZUFwDMPobh5hbgAercXKJ1uTZ09KuoG8nzAa56fuxNl2cCddyTzooFqkJh1cPsEtbV/1/rdqey7iRkofrv5DomMDHikSCe2rJ68AjYXeQzgf8+Jx+9ASPWhhlZvIl4hacpSqLQru4wq+6kjsB9xAfzxth0ItwG59l/ziTv9Cap7yTzgAYsAMu4zpJ+nmINJIQP9wavfdN/X2BPbne6sV33N62c52NUUChfQA1AatrE3kcTfnilVR0Wbenf8gKV3Vn9EwXtG5Z6D6n89QXD/OIO8sz70tcVRbA79/zq/TA7S263CbukTu4ZY6aScH8BPFk4BekxwYH64m3Mvsh8zxVtHemvMX/M0BllU3f72WHkP13PNo9m1FbBBoRXoDYHqLveeylNqVtVUBPbX/I0BPgHI7u0ORBPUPaiLyfk3hdPdN0sjANx0/WMauIceAAmSBaQrVLZOClIpAEA4tpsAq6qpHJ8hAnntT6XZR7Eb/cErCEgH6QPkQ8CIGBQYYIk7dFIB3ASVGFRF9mN5PM1Y5SPiHgTmXf8VMkBFTVlVgzIGg9K0BqDw4S4KynyAMTDxHeE6ssuHMdOI/DTQnmJRZCDRfx+B580fNXC3ZTIfSLU9uwFY9lN/9vzhEdl3O5+xAsZmU9XeN/0x3E9fod9T1d++5ncb3ykBNIN0YvnfgQOBnM7qe/edelkN+lHmPxMIZMKd0F8fnPwg/XdbvvzpXPDxrx0d7iyr/TFyX6Coacr6C4I8mPGNGF9BJ0FAjsSlX/8gyc9TzX1+r7nPz5r73BSf32ruDzoekH2B/pqdfxDxTPAvEPaKvqLTLSF2/SmDnx8AC/N5df48n+5+zRX/R7yfSTH15PQ2lfcbQb0tASwVVn44LX4QVj3xXA+o9d6hQUS+5u858awYQAB5OLFrXfyuku9MDSL8COA7kYBbeQN0e9O8F/rToSidzK/9ly95m6afXnI78//SYWiiDZC/AJbpMAVqCQxSTezfr96Hqunij8fEe5WB9uAVX6Zi+wRNA/An6H2W/QS9nS7uJ7e8Bcern6c5elIJloJ/3te+n0Ed/wUc7JpbObnwODJN49tzrP6zEVONAYvvTXcit2fRThr/JAR8CUPg8Z+EHO5f7PTZOerGnog9bt7qvQZ2emBM+gSBIII6BKUFOmYLNvxZDdBT+dcWMKg3ufsDvx9uFQ9ffrvD0DzOnb++vHWQZwyeMyZYDkr1cz1xKAISFigE14/UAvf+r6bPpyzQ/8DEA4RhpD1zZ+7CIRwfR4MlahNEgC0pF5vjM4xAZ64LvpL4zJsvKNwlPcqfBTjmOks7sD2SAvIeyfptGhriyT7ctt2lS2JzjyLthevPUGfm+hiOeeTMRwlqFiyX/hxA9b41Ac3z6fTDyQnR90F4Aufp+68vzmIOVu7mNUc/PgxC6fYCJx0lcuBq4Z8tE+GcWFuo6pJLRTyu2kPSn6wy2aozfnNb7SzuYhtXvl/ejnqlbsMTwebkSq4b2GLQVInLA2psaefA5WJ2Skeydclofo1tWeHTdUYKkpGxcqqKPFFlisFg5zK92LluZBe84W8bIk2aqj+RVGeMJBVenNQu55cy7xBksZ21ke4RSX9ZHy5MaKDoTZcsP73tE3dXj07Yt2kdtJSOwtY1Ucojlw9u3ajVydou6KTamB0K614glmR0riWeMwU3xQmrU4RaLa4SKm8KT66Sm9uN+4XfjQM8LGG/M5H5uaa8874jWOMk+xjTppaDY6N0rGz9suUJkg+BTGkh6DrvGOGV2kVaj2FUvXNaiQnTLbJSWrvaztHtLiLgktssHS3l4fYs29jK2DZ7Pro2vpqYfXM8XQ8NbzOSfjteddPn0BWNmKhRhW5vpKgP63rqx8RWy7KVbYXRnsjOSN+xiZA57Mbbr2/kiluGZ2482Snfeyrj6OebAc+4Hl1ZzjzB6f5wG3LYYeOSrOJV0BpHofIcz0riq+KbdS4cdJTZZ/JimI/mcT1fqLG26mwa2e3SaOUwcIjvSIOX1MY/aAutq9Ta9XjE6CSbEvQDj9Yrwt8QZAk6e7I9EOSYFT2Omq0TV46U3IjlbF1G7hExD4LQZZQixM1aNLHt3L8wQxewoMibc8eUJFPvse12Ncwd7aK0/GEpbftNg5xgum4rJXMZI5PrNJidxcv+Yi2vvH91NOt8RchDrM8ZnQzjOqG2brmu/GPv6GKhWM0l2Y0m2eJZtdFN3cu8nFfx88GSBw/MZShzIRhdZLwmYtGyvVqNx2IU+FtJx5mCOQhjG91WLkhBDs1uXEu4RM5Ps+WO90buRPAjvMaUm9TNsgFOTGN1ozZ7XO8UitM62Dg3UWKkNnY4pg5bEWCi3CbjOcHSIqsEs7dvZKwJ681Vdjc7pXJiQufPjDZqDBaqUT9WJG2R6cK4Zu5GNXz5CiLCC/hOZnbpkDLHSN8fWNk4mdzAxWKT8HLkSAavELqGNoebfzzsr3PK4ruV7uzMsXZO54NyqMXE2seJpI3x2pI1Psy2W7OJzavOksO8lE6jXNoJ3yUzxjKX14j02Mg7kB2yRiS73nnlbH1oE2TIzDVsFd1aI4LLfiP3+8DfJ2d9rSVIXq0GPLpwdnJjStZfomtpaW5cLHALcuZshqFAsTyyKDq19jaxEfztbB4c05yqO2JT2adMS0In3qOSRZDNRajN25Xau5uFhV3x2ai6bKarKr7dKPCty4a93IfnZnY5qh2jxh0jEMQVI4qAc+lzclNE+FIts9UJ27fWwY75bu/Iiy1Pxo007kjcUi/7/ZG/IlGmROJFTY/WrL2Z6kDN11si40SUqtd6wQ17/HZ1un7oZyf+zF3bXimFsNmJOJYkuuiPle5iwlaWlRY/S+SmyA9r6WKGsNF5MZvNiO6ci7nP40W+WwYLmGXRNSiVvqbYjeP06S5w5VWAJmUWG96BuLidsjq2MILMYS2cSyalC8eZPufrsubVbr1dqLeECuVKYcWWYFiBsC+VuM4sD0DP3QxB1GK4YXiUp8EQMXO2XZcpc4VziH3OV+qS8pFi0dR0tdktBZa3r4JwHn1mF2YaN+eEoJA0IZfRsKA17CxWA349bpiklBl3LlVZdGYbcU331pVW5yvESAGNWNr2yFK6sdzLY7gWieNwRM11KcYwG6v5Mlz0PSFE+Y0xOIlPsIIFOY1cXVCP+BlmTs1mXTJuulg2s1ONyHm1XOz3MmOJEX9zuuVZt/fKkvSv+qGmmNB1L9wRZoLuYvajiiczuRaafTiOSbxAWmFcIOm8ICkSmS9zAqdIYgb8BLx/6OUgw5t4scppjdJyZp0t/aXI7dUS62tLOmvqLhuR0+C40qma7+h9u78ORL9eGZtkJikJxrkESTAFW9pK42gLn4s9mVd9MmeRUqY2PGZYInEWVFnTJYGayf7QlpUwXHboYLhhQa14QVLsq4vGxLgMt8PBcbN9SfHHIjmPva3feMTEl8VW2/gdnsWtL+BxeZTFQL9lNIv2eRkJhnJMSMQ8V2esGYzN5cq0mJ1fhoWwO52w9TgExtlALg3OU0RY8GqBVXpz7RWS9BzCcBgnZqPYrmdD0BQju0lJqU/qXsPFgDkMzcXLYuQ6F/EAZ89rm6+3TZo5xxHTxiNrh1punRepJLuzMLwSF18Suc42lkc3zFLxgB5VieO48hYO7KgPl6FebJZaGAX6ZqftRW3NAOR3kWNZ6sqgyqPeMdmY2v6O3jCFbmk1vdUDTEPbzaneM4eY7dzrMbX5PdmvqIEsreuZb+d05JgHujSUFX0Tquq8kVc2yHTeCwqvvpzN7Mz4UT6XqEO4jXmzMm+p0+kp651HVe/0IjuzZMh3l0Rj5It/QY8RayF2PdqoTwQBzVhypbaZHWgH+dTme1UYJWVjjNaSKSNtHcBpGPUEUV1OzlbLeTBvkCLeqVrc6wIb5ueUUXbRloi41QlRre5wIVuK4nx8EI7r4LimGhI5Y8V2Z9rLxfaS51dFv7HJ6DdOtiYbo8TWiq57jBgyI9qTfl4heNEbgIkkliFoEsWFuRWZck1J8cmMWs/Jd+gCbXVn4Tss3m0GeZt0BjmDs9tWjmqYztd4t2/2olgJZ3rHrmqRxsmzwym9ZPewce3HnUZXFy0QrkOQWI2+ulTFDj3mcx5xlhv0eKTBbLJUsIjZkkahbm4WM1z80aiP2mXWOVppS7M+YrJqaQ/eFQx18Ooa033LwPxsnoZeWuznQ4sTLh8kM21PgPEtwzcJLiGFVbnsJdqs+b5aMZJkDfShddRg2HRsyTXNFowO45LzuF3d8vLN0uajd4qHthW2860Qk8WGmKkKk3pFFe9derkktEuTJep28FVtXZYMxwiLEi2uzDKda1FVoirebMNEEhfzuKV388uJY0StSylFOXpxqduGmWAaj28lob4c9KLNFnWpiubeXrqrKhIcREWdhWShFZYeQ4opE3km5Mlt2Rk1bWpWVfs4zmd9qrFVl9vYkTyVAsxVjDM4goVhfJqu10TsIHsgx+kcC+GZEd4eO8GQfBYj5tk83Q19Xx/1w3HODDLraciGzhyFV9O9czxpON45h4VL70O1gBczrx4YuERtHI42s2pXwoeDAHqvE6894aLU1/PxuFd5rETzm6Rb4fEI1Fx2tFYfQSR0KS3tFZeq3OnAb3HhamuE7vjs4sxQyLaPd8FayUrY8M8LpluXxGo0s1ZYLVrSXAnAky7aqLuqaiypN1b7XTcTZ/Nyy+jYbj40e+laMrk7bHDh2KLExqbZw/FKyIN6TcVMtOn1cavbZN3Qtrw89zVRyDlr0kItD7GAl+urSLqmIl6POn0hhTxWFHzUZ9YNHUgU0/Bl6bPMSfXDsxIcfJM8zgM0rNOVkLXz/bbiFltwNtGDq35ZsWHYgQnpMuqLlNe4I8AB3dFncaUlnCZwWz2qSSkNzdvW29wKN0s5vMOKc4iJpkcz18tiYbQ7knXjQ5STOb057XkGTqRaNA3CXQarMF1sdHau7EJxv96uOz+RSoO1MJU2Hb0uUQ7VujLvOSZfhzysZ65PrwhM9wzzFsc8fUnNTvWamSnqebDnbEnblSqML0l7HTmpGcvNxpdvq4AjduSiUrGxxmRubPBLnbXLdh3qDSLtQFGMYZA3N+saogeqsbcEPuAbOjrWo9zZkl/GEqdpaXZSCJnanWh4fvXwOUFWQoLLphHoZoL7571YdIxiiohwZY4bH5HqjOwT4erVi/oWO5TrpjDgmJ2q9rYTCXDe1bNNwVJxinnGVkYjuGF7t20vWXgeqfoGY3TlmT26jynQ4rzj6JyD/OiSZEwuScyzRtT3zRGGcRiZhz59Xa728xlCqciIhk3jzGy5vfXYYk+JghvyY7qMEJuDD1y1NGdaDeruiovWpmraPqdWG0ti11edHAqe3dE26x98gJNyWxGngy0V7eFMbhJv5y/dpG9mbmXl5/gUKKXXeidl3u4PmF4IucjHpxug7vOSzKytIFYKPcbwpePF0dxEWLDeCzOEcVAaSZCi3VLxLXTrMl0Gobxrll4LhyNxdK+kxKHp2hgXrDxbgPZPMlhvi81mKaVH0zG7eSKAWm5cd6YigtINHenLbLxLNyiMXmzaTtQVhcMohsqS6uEUdWJhozXt2tNWdkQv6grMp03l4DqBNID6WoY53ShNW7rNTDJ3eSBYZJhxoYu4Cy9HrYEa4rnBGrKZiKEdewvAkcKIntpD10cU14cuvpXLm9WeTUVmlvkpHbYipQEMG/gS34SWGRyKc8BAc8JX3DmFowOoQZUYqWEHYs3g8Wau0DKf7WRQpWRzIzdLf4DRFcbtNQOWLfKc1r6xU+mMz2g+3HmzKA2XZ2YHeytdkBEqpCvdOUciIi+ExVq9xGeFOsJLGy/JRmhi1zQ8f8SSbpDGg70muwNuknR2lld+IpKVIXDIQCZBBrdzAvdMnnJx0l3dFpp7XrSrqFsuV1Q19FK6Ps7mc3eVuTtayU29Q2CUPVOWXe1rIxTSwj3cCpswHZqctb4VpKeL6e23lBmPZ4nyLUOKMI9cR4t2dqFHTWTilASUKBSCGebi6UbPLztYcfPbldFvwXpYnBbr+goXZeflfSxVnktjSLhtZgJJh7C0GGb+Uhml8oIE3r4h5uBoSIQ0QvUj4svrCziay4YYqNhlwEDbJdUBHZSrJbnokpQ7UxqSxXzT+KbTgPa7r2Yje5xVQY+PuLDDqRBhNVdziZW3oMvllXMuTtbBw4DyHS6iZwGjhr6aC42N2GZoJHR2UJMuJmC4Tf2jdtptrucwWtpOuTS2zhwzYwTlQ6XeaFfRVPnouusDVBROaxoP+0MSHjegb2dCtisU/Mx0Gh6KzdFBOkWlXGotY2c+tOm9yixytAjKOREK/TLY3U4mVpxmIBfF3Z42HM7sXR4cMTi34xaXW2gOjrY+0GLvlUnByamPh2hx0GZFaq/r8sYsLUvhYNCkbROW68vpppqwjWqztd9ZtewS4h6TJUp2ERkckC8lNTulEkgEMH/sq2XEY3lRt5ijz8YjjTkUwQVy21qJ5CYLZAdaOrrFD0SJw72ocGjCsOyloZhjjnPxJs3Uk2/LVrVl3eBQacQlkcJmcGGP2eCyXHSwFWXEsb/SNP33l08v07Pr5xPo/9Er6ulJ4P+zB5KPZ4dvb6juj5992/ty1/Xlf2beL59eKjeejLs/jK3TNnw+rvyHR7Gf/8o7jknS7fE2eHrBNjRvD/MbO5z+s9NLnHtgaXX7Vhdpe38w/OnFaevp/1vU354PwF/uzmbl/Wn6m/LpKbtd3525v7x/23x/FZr5Xmw3/vMyfD6pBrtvIISxW3+bLYhvflVOXj9fm0wPdaf3Ji+//R9bt/pFcSYAAA== -->
