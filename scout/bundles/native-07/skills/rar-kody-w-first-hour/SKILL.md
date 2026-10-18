---
name: "rar-kody-w-first-hour"
description: "Walks someone through their first hour with their Brainstem, one step at a time. Call it when they ask to learn, get started, take the tour, or want the next step. Give the step back in your own short words and end by offering the next step."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/first_hour_agent", "rar_sha256": "61dd52033a67e19c2c88909a379cfd2a855a1c18f76065ecde2bb330a3681997", "source_kind": "rar-agent", "source_commit": "4d986fee1ec211bc0a1357f4df8671625bbf45a6", "author": "@kody-w", "tags": ["first-hour", "learn", "getting-started"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@kody-w/first_hour_agent`. The original RAPP
agent is preserved byte-for-byte in `first_hour_agent.py` and in the RCI capsule.

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

FirstHour: your first hour with your Brainstem, as one agent.

Drag this file onto your Brainstem window and click OK. Then say: teach me my first hour.
It is one file that does one job, like every agent. Read it: the six steps are below, in plain words.

Your AI, as files you own.
1. Learn it in an hour. It thinks the way you do, so you can see how it works.
2. Run it on any computer. Mac, Windows or Linux. Its memory stays in your own folder.
3. Hand it to anyone. It is just files. One agent is one file.

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "step": {
      "description": "Which step, 1 to 6. Use 1 to start.",
      "maximum": 6,
      "minimum": 1,
      "type": "integer"
    }
  },
  "required": [],
  "type": "object"
}
```

<!-- toaster:generated:end -->

<!-- toaster:generated:begin -->

## Run this — do not improvise

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `first_hour_agent.py` and embedded as the fenced Python below (sha256 61dd52033a67e19c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `first_hour_agent.py` first:

```bash
python3 first_hour_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 first_hour_agent.py   # or on stdin
python3 first_hour_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""FirstHour: your first hour with your Brainstem, as one agent.

Drag this file onto your Brainstem window and click OK. Then say: teach me my first hour.
It is one file that does one job, like every agent. Read it: the six steps are below, in plain words.

Your AI, as files you own.
1. Learn it in an hour. It thinks the way you do, so you can see how it works.
2. Run it on any computer. Mac, Windows or Linux. Its memory stays in your own folder.
3. Hand it to anyone. It is just files. One agent is one file.
"""
try:
    from agents.basic_agent import BasicAgent
except ImportError:  # outside a Brainstem, for example the registry's own tests
    from basic_agent import BasicAgent

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@kody-w/first_hour_agent",
    "version": "1.0.0",
    "display_name": "FirstHour",
    "description": "Walks you through your first hour with your Brainstem, one step at a time.",
    "author": "@kody-w",
    "tags": ["first-hour", "learn", "getting-started"],
    "category": "core",
    "quality_tier": "community",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
}

STEPS = [
    ("Get your Brainstem.",
     "You already did: you are talking to it. It runs while its Terminal window is open. "
     "Paste the install line again any time to bring it back, memory and all."),
    ("Talk to it.",
     "Tell me one thing to remember about you, like your favorite coffee. "
     "Tomorrow, ask me what I remember. My memory is a file in your Brainstem's folder."),
    ("See what it can do.",
     "Click the circled plus at the top right (it says Manage installed agents when you point at it). "
     "Each one listed is an agent: one file that does one job. I am one of them: FirstHour."),
    ("Read an agent.",
     "Click Export next to ManageMemory. Your browser saves a small file, usually in Downloads. "
     "Drag it into a chat with any AI and ask: Explain this in plain words. "
     "It is a short program for one job: saving what you ask me to remember."),
    ("Make your own.",
     "In that same chat, ask for a new agent just like it, for a chore you repeat, as a file you can download. "
     "Drag that file onto this window and click OK when it asks. I use it on your next message. "
     "If it says the agent did not load, paste that message into the chat and ask for a fix."),
    ("Hand it on.",
     "Export your new agent and send the file to a friend. They drag it onto their Brainstem and it works "
     "the same way. Or share it in the registry: https://github.com/kody-w/RAR"),
]


class FirstHourAgent(BasicAgent):
    def __init__(self):
        self.name = "FirstHour"
        self.metadata = {
            "name": self.name,
            "description": (
                "Walks someone through their first hour with their Brainstem, one step at a time. "
                "Call it when they ask to learn, get started, take the tour, or want the next step. "
                "Give the step back in your own short words and end by offering the next step."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "step": {"type": "integer", "description": "Which step, 1 to 6. Use 1 to start.",
                             "minimum": 1, "maximum": 6}
                },
                "required": [],
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, step=1, **kwargs):
        try:
            step = max(1, min(len(STEPS), int(step)))
        except (TypeError, ValueError):
            step = 1
        title, text = STEPS[step - 1]
        after = (f" When you are ready, say next for step {step + 1} of {len(STEPS)}."
                 if step < len(STEPS) else
                 " That is the hour. Tomorrow I am still here, on your computer, remembering. "
                 "Your AI, as files you own.")
        return f"Step {step} of {len(STEPS)}: {title} {text}{after}"
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/61ZaZPayJb9Kwreh7YfVSXEIlDNdMSwCBBCrEIsXR3tlJRaQFIKLYDw83+fmymqbPfzvE9DRBmUZN7l3HOXxF8rKM88klReK/9zInbxfK08VWycWokfZz6JYH2LglPKpSTEJMJc5iUkdz14x37COX6SZpxH8oS7+tn7ai9BfpRmOHzi6BH4FHMo4xCX+SF+4fooCDg/464ejuiJgkPpicsIF2CURE+cizM4g5IM209chk5UKfyBEpAHilCUsZUI3zIm/IUb+ZdyF9NlIuvE+RFXULvINeJS8BD0kcROORTZHIY/s+CI4+DEj9y/SQME8A2FcYDTyusffz5VfPhcef1asQKUwlJlSL0eg/Cui6MMtgcocmE9LgDKCJ5jnDgkCWHJxg73ePqU4sB5Yip+F564f/7zdEWJm35+fYu4xytLih+e6Iv58zsXotsnOBP60acAR5/WurxYf34CH7NPdMfnz5+/H8M3C8cZ90kvYiwnCQHUDBTk5efPv5Yv/GCDnwUYcKdw/M4xTX+wXc+c8Of3bcjJcAIbPjlvFW5LIwlocyjBXIKRXYCfqCgxBd9LNV/Zv1VO+AbIc1+/O/Lt5a3ys1ns5Tvluf/mvm/lcJDiX+wFI3QPOOanLJiUkS+cTkICTl85hUMhyPKBdx5OMKVlSQ6LhHEOjjyB1SEOTUaHF+6X5rxV9vRIV3kCvgLzgR7MZyAY2P9DABKc5UnEATDrD7f/zeVX7itD+hu8A0rfvjJAv71VgD70AKXeH5URpAIz9COlKDv3FOmA4czZvv36AX0Gqcr4TCC/Xjgl45I8SiHRwFhYSTkdJ8AhFEC2RjYAA3CRGEcv3AKBcAYdVUMTNPAhdZELaiFlCpa6VK7JEgaylyYZMBIDxAVLKjj0Uvnz6Y+KDlY8TABjdQzC4GxZPB7WvaPNIZPkzMUnUAiZzpx10IUkPthj0QzF3wP5xCoFCLvSWCsfYl44rXg3BVxCLDofFeADu98gbCSwYT+zc40fgsAbC0WcTai9/cCH6kGRsPzECrDNxUGe0vpVVqGYS3zXg/yCU8DxlNNQhNwP3GA/olUhLcsbjUxMIE85pufzCycjy2NgBD7YZDN7o/LMK1tntmfULpsAxejSkZgvJYnpEzAJTAlfuY86VPqzAkJ8yPruinyLafVjuQjQl+ZqDKwXjlHaBGhTCEaKLpiil4aUANSOJy5Pc3goKJgDYHpAkJ2+cIMEMRKAYwQOWNRa1gAoVbpKyYf09EqVB5RCEPmUyiifWCVm/GTRKstznBA3ARdpvXg4/UpNopRhYWIsL+P/A4VK3zX0Th6ajuC7EpUYpgi2U/tK7lDhCLC4lihxxxz6F2OeDzvKby0whwkDHTEuT75ziq6WXCmxeEDBVLENhCLCvH2kGIXCYoGYqyUnADcwhfoP6FLFH+WIxSjEaQrGwdcO984xSr3SYMh3LiJgMyh/4uJH2qKPY2VIGH3p6iMQD88c/1bCNabrTDHF6sGQhwnv0NAtKe2UVFhJShprJ/FhEXKSNm77wYOH1z81f+6hA4J9Kj1gsbgioN0cyObRisU4xL5MsAsJAQ2Q87IsTl953gVC5eYL1Gi+HE34VXdV+fPPb9CRQUOSW3RCoQ35H//gNN9KSEqcjFtbtKRA4aMl6y16i3TGvfSh5YKT1DfBm3IfsO6ImSCaV18eQxDPBpu/aBv5i6HxhTkM44fvsvq56i4Wb1EJFIiOEwwJdMF0rMjwM6D9TD9Q3778XdRLXHwpsSkdX/UVoFSc5gF+oeayZloaR5mGb9iCFgUBt1CZlCntVikJ2MgDytMTbWy2n4Af78UY3H+lwr58+WKi1HuLytmkwZWTXcrDhg9zuOdncMAJaF17izDwn/vt67ffuH9x/+kUE051QO94BxcsnKznM2hGbh6yKsi4AHWJgvv12wNGEBNBvYFQ+I6Py8PQb07Yfsd0Pe4+11siZ2KHJiNMYMDQsvOwxPiwl+YofEUT1COQyzakbGTjyCpYWrxFH0jSrElR5qdO8cQSj2r9Yr7T9S+aL184rb8AnpOAlZi8jBAcJpEP8H9EvFwHIQn0lO+9mZtRekFWJij2EvTQ4aAyLjQFH8dZJkGqvUV0tsQUKkQ5WMIDmwAZ6xHSZ5Z7kAUhBDZ91832INpAdEKLQPIWpQ8el0OYRcCUgnNz30aRhf/rQSmotXlgM/zAUirpEQX7ERXGwY/O8vroyH+b83/uq6xAkuhRopiAR1X00x+q4s+HflUfmfsRLXmvMIDSRgkFIyx+UA/Cy67xf3fKxySBmfulRRxrjT40WFaG/BsbLFOGlIkDOlj8rTdRH/7DuBcJL9yU3lYeBQzytBw5lYwNOY+CB7WOnbEJzMPko3mkmE6o14/iCPLqYGMePXoBbaLvkymMNsh64rYMrJRyaOpH+Y1qSt9HHhg8ivSnC89jzHmLGi/ce62nnIsKAOm98bLexxyDgvwevR+xpb0BIoOBWZXXKA+Cp0oEJfzHGxC97ADbQwympvSOBPUU7juZj9kThZm+/+1G6fkQWvrdEydQu8QXbgPJwj6zmx/VDHceP8zhEiXCZz8qPwtPlQzuNSAEkgi7OKl8g3aQ4HMOuWKX17XHBmLSwl6BryGwWXkf+1oBS5GNMvSw9VH7YXuCkueUpggvvNRAPTyXpe771fjfusJjG7QyqFWwTxRsu1WvNRpIbGNBsupWpyPVJNRoS5Zj11Gn1UKCJXSctlgTW9iycd00G40aaogdQZLadPYH4Rb+i6a7T1U3bakjwhAsYKsuCKZVQ0Kj1XaattMR24JYb5mm02wh8ftRuAHYD39KIylCHw2K+v1w62vFFJuwc9xMlW756vNNYVevt82V15NagqXVFVtVN43d9NAdk6XpT0Ytfyajfn0kLHsKuirE8Vf+etcwBCS7dx7X7XCNY38muo5MIis/1CStbm1u/PhSPyZ8I1rVe8FFHF6T6sA3+N0oczyCL4mtzjqCG5Fese+d5Cx1hvFwWheQG1YFpamp4mrX8IrDaZKGs3q21JetQ2xqhrO4Hj07XY8avfP8Ol+ofu6tzn4Dd8a6qJ0Hg2Qsp0XV8KSbixf6bNpTidQlvbY0zKsN3dVEYmV9HE32U30kduWt66iKX1y1PJXt7ixbHaJePTtam+WQt9rKzhCUfa+hWovYE061Q6Tubt3D6lIUY3TuH069w2ZvzIo02tuHs1qg1trqTTqHwWqzt5WbBIaKw+1wTnbFuaMfmsg21/LdtrPWROF36uni+tWeLBlRk0yy/NqUra6hmWrWa2W7reXte1NxM/TO8S0lgqRjjd+fAr4fXa7rRawciYMz5e4HZ29ZHSS4Pqin6LaTLWzm9mrT4z3dEOZzfe3tFDHkra29zVNPAh4pqrOaHifpwrhO1p080XfymHd7+hzbdz9aLsKNenbdxjlsByNPTqfJ9hgOOqJqrY+denPHX7Ib4cOOQWp5MdpXvcasKWuL/WG926pxq2cOd2ZEjoJoRKLVKmSpWT+f7Gp1Gwcd3FaqQzSdVfV4EM9l62QFcY3vrdKsfWhJZGWa5v1q8fsZ1nr2JDISXJ1dRO88PBxP63ouHpyID0l+8dan6W28Ge4yvB+4w02rlh2lOtnvIl+wF3oTFfe5Xosn/VxVQyt1gtyXzHgf3fqDRNvz0CsyDRvXdWZ7wcG/zvlLOzbUnWTnTaF+6edJko8i9zqeLto62mf5Ma1JvXbTVLb+rTDHk5mC5N1laEfztj3p2NWjqpr1TraYNVaNXcfI5UQaOE1d3gx2sjARXfWUSZe9YbXu6imedCRlcws0yPJhu20m0eg6jYI9Gp2tbXstmMFSuPekcLHe7pdZ0ebPSxL0+mtXPJ8Jkf0FmtREmR9FfO0y7WKfD87EnGy0sXWSVrVDvJAb4jxsxrEuOpojmZNpRyjSRlGb9OXpQV30jHjZB6ym55NzIPJJzFp7uMMHse8u7WvkjNw4xXsSZ3U1Qi1xYohaO/QXpqLnZ4PsenOr0GTjds4brXp7qPJXu2kaVqSrd9yWs7ZSGyFLC+v3fjRHZCIc/YtyN4XzFQeBGE76WbMIhGR1Ftvu0Jh7nbDvGt1iaSAihq2JHdcMqRmI18HRmA1rSj/NyTKsp1WedGc16Tw8V8P9RD+H1jXLbewjZeZ2FkfRbza00EUNzd0MVobVby1jX16m/bE3NqrmZqGr9SQ0R5ZMJrbSEuOMFMJIiklgjE7mWrP3gewT/eooSOu3Bvmh2bJ33Y2f21vtdOvF8vEkyedktb0d0+GUP3nDLAlidG7dxmbzPj4OJzCvx/x6SuQMd3TTrRpoYN6O9xXcabakXyPNUXReWqDpNtRGtfbZkHsyIudGY33p1IjWGE6aBtECVzv0GjsNt/z5ZqIu85rRd8de6Cw9TTm58cRyGo17lNrG5nyCfK7pgWq51VbXRSMtGg66+kong+GmW2z15Sxf9AZb5Amp3rksdP7cFtduLtU3s2IzGt179cXifBeTrr6piiNv62d8F4WH0V7fSMGsrnhBYxF6TUVYpImxkiZDkt8WWdCqTmOiFKPWRDxvF/3joJOol/yukcuWt9uLVW2t6+nQD2fV2QyPBpLjzJHaPiuk8JOgoYrGatyJ5kWIvXjj3a7T0KrV+tpBWoyHhyHfuvPV0UU9naKBc+oUA4nfQQnNL71k6CxcczW+1E5eUV3EulVYw+l81ZPrkxO68svZ0iuui6HpK821E2xVJeocmldh3k2aykF0YKDotWoHpPL9w0Bcnqud/jba9i+5By1MHrah96TKfmjFxWWEj5fZonEFWu69k7jt7gbTSa+n2CsX+fX6daF4tWizb84GvNQ9GkYmd5Z2rG4tzYnOpp+JQrocmbeBOfPMe1Lby0GULCXzOoQiaVSPq8UxE5U2Gkyg63cuNzUwzjV3U1/P+9ppVz9cY37T5ieQmnWnwMp13K/187x1tiJ71N2eBdGsSs745lcXnrZyGqNTVcrmnY7V4INivJSvITocd/de+96wOh4Z31tXy9aUxujoT9qj40iYDZf+7SDpLV/CycxUp5mA/WY9qd58c7RT5sZ8Lk/V43W9381WQ5SrDt/prLSqdhDmKzGrBgfeqgU7ZRLz3Z2YnK+5E6dSe2FfRsLhuqvd1db9NOg5Lbs7iWb1WSysep46bZwKdTTtaNurNpsMk1z2GoqrapKh7apLp1HtpzV7K+1te7DnoSc0u7vlOmnUew152oOAr4g+nxn+/lAYzaVjazN/qO8nrftOsJXT9iQMV14snYu17wnAlAwu2MmCv7n3Kd5v2yub1wcp8S63UHWGcpIp2K3WLlX5jucDsnD3K77TF9tW62ruFzAX/Q7jFZ2IH+PvL670dP76fxsDy4kNLnARvbrBVFuhP/a+lj8S/ko5TL2J5YPqcnZNg9x9jIDl5PrMDj175cSeFuWFF25l+Ja9j/YZcumPzpWftrL/koF3F2f0+v38+H8ZqpD9kMJGZ1AKar/9L2EZ76xMGgAA -->
