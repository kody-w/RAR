# ORAPPTER — The Offline-First AI Runtime

> Real-time AI fluidity without an internet connection. The brainstem that never needs the cloud.

---

## What ORAPPTER Is

ORAPPTER is a pure LisPy AI runtime that connects every agent in the Rappter ecosystem to local AI. It runs in the browser (RappterVM), on the CLI (lisp.py), or on any device with an Ollama endpoint. No cloud. No API key. No internet required for core operations.

The name: **O**ffline **RAPP**ter **R**un**T**im**E** fo**R** agents.

---

## Architecture

```
┌─────────────────────────────────────────────────────────┐
│                    YOUR DEVICE                           │
│                                                          │
│  ┌──────────┐    ┌──────────────┐    ┌───────────────┐  │
│  │ Agent    │    │  ORAPPTER    │    │ Local Model   │  │
│  │ (.lispy) │───>│  Runtime     │───>│ (Ollama)      │  │
│  │          │<───│              │<───│ Gemma 4 / etc │  │
│  └──────────┘    │  - Memory    │    └───────────────┘  │
│                  │  - Knowledge │                        │
│  ┌──────────┐    │  - Pipelines │    ┌───────────────┐  │
│  │ Card     │───>│  - Tools     │    │ IndexedDB     │  │
│  │ Registry │    │  - Offline   │───>│ Local State   │  │
│  └──────────┘    │  - Sync      │    └───────────────┘  │
│                  └──────────────┘                        │
│                         │                                │
│                         │ (only when online)             │
│                         ▼                                │
│                  ┌──────────────┐                        │
│                  │ Cloud Sync   │                        │
│                  │ (optional)   │                        │
│                  └──────────────┘                        │
└─────────────────────────────────────────────────────────┘
```

**Key principle:** Everything above the cloud sync line works with zero internet. The cloud is optional. The device is the computer.

---

## Offline-First Layers

### Layer 0: Deterministic Card Engine (always works)
No AI needed. No internet needed. Pure math.

- `seed-hash` — deterministic integer from any string
- `mulberry32` — seeded PRNG producing identical sequences everywhere  
- `resolve-card` — complete card from name alone
- `card-value` — floor price from tier
- `search-agents` — text search across local registry
- `binder-status` — portfolio summary

**These work on a phone in airplane mode.** The registry is a local JSON file. The card generation is a math function. No server. No model. No network.

### Layer 1: Template Intelligence (no model needed)
When no LLM is available, ORAPPTER uses rule-based responses:

- Pattern matching on question type (what/how/why/who/when)
- Registry-aware answers (pulls descriptions, tags, categories)
- Card-aware responses (resolves card, describes attributes)
- Binder-aware status reports
- Decision framework (the Three Rules applied as logic)
- Pre-built response templates for common agent operations

**This is the fallback.** It's not AI — it's structured data answering questions. But it's useful, instant, and works everywhere.

### Layer 2: Local LLM (Ollama / Gemma)
Full AI when a local model is running:

- Text generation
- Multi-turn conversation with memory
- Embeddings for knowledge base similarity search
- Agent persona roleplay (card → system prompt → character)
- Tool calling (AI invokes LisPy functions)
- Multi-model comparison

**This requires Ollama running locally.** No internet — the model is on the device. Gemma 4 is the default. Any GGUF model works.

### Layer 3: Cloud Brainstem (optional, online only)
When the device has internet AND wants more power:

- Route to a remote Ollama instance
- Larger models (70B+) not practical on device
- Sync conversations and knowledge base across devices
- Push provenance entries to the chain

**This is the ONLY layer that needs internet.** And it's optional.

---

## Core Specs

### Conversation System

```
State: Dictionary of conversation IDs → message arrays
Each message: {role: "system"|"user"|"assistant", content: string}

conversation-new(id, system-prompt)
  → Creates new conversation with system prompt as first message

conversation-say(id, message)
  → Appends user message
  → Calls orappter-chat with full history
  → Appends assistant response
  → Returns response text

conversation-history(id)
  → Returns full message array

conversation-clear(id)
  → Removes conversation state

conversation-fork(id, new-id)
  → Duplicates conversation state for branching

conversation-export(id)
  → JSON string of full conversation (for sneakernet transfer)

conversation-import(json-string)
  → Restores a conversation from export
```

**Persistence:** Conversations save to local storage (IndexedDB in browser, JSON file on CLI). They survive app restarts. They survive device reboots. Your digital twin remembers.

### Knowledge Base

```
State: List of {key, value, embedding, timestamp} entries
Embedding: float vector from orappter-embed (or null if offline)

kb-store(key, value)
  → Stores text + its embedding vector (if model available)
  → If no model: stores with null embedding, text-search only

kb-query(question, n)
  → If embeddings available: cosine similarity search, top N results
  → If no embeddings: keyword text search, top N results
  → Always returns results — degrades gracefully

kb-load(path) / kb-save(path)
  → Persist to/from JSON file

cosine-sim(vec-a, vec-b)
  → Dot product / (magnitude-a × magnitude-b)
  → Returns similarity score 0.0 to 1.0
```

**Graceful degradation:** Knowledge base works in three modes:
1. **Full AI** — semantic embedding search (best)
2. **Offline + prior embeddings** — uses cached embeddings (good)
3. **Pure offline** — keyword text matching (still useful)

### Agent Pipelines

```
pipeline(steps, input)
  → Chains functions: step1(input) → step2(result) → step3(result)
  → Each step can be an agent function or a lambda

parallel-ask(agent-personas, prompt)
  → Same question to multiple agents simultaneously
  → Returns list of {agent, response} pairs

chain-ask(agent-names, question, registry)
  → First agent answers
  → Second agent receives: original question + first answer
  → Third agent receives: original + first + second
  → Each agent refines the previous answer

round-table(agent-names, topic, rounds, registry)
  → Multiple agents discuss a topic for N rounds
  → Each agent sees all previous responses
  → Returns full discussion transcript
```

### Card-Powered Agents

```
activate-card(name, registry)
  → Resolves card from registry
  → Builds system prompt from card attributes:
    "You are [display_name], a [type_line].
     Rarity: [rarity_label]. P/T: [power]/[toughness].
     [description]
     Flavor: [flavor]
     Respond in character."
  → Starts a conversation
  → Returns a function: (question) → response

activate-deck(card-names, registry)
  → Activates all cards
  → Returns a router function that picks the best card
    based on question → category matching

card-battle(name1, name2, question, registry)
  → Both agents answer the same question
  → Returns both responses side by side
  → The user decides who wins (this is the card game)
```

### Tool System

```
*tools* — dictionary of registered tools

register-tool(name, description, function)
  → Adds to the tool registry

orappter-ask-with-tools(prompt)
  → Formats available tools into the system prompt
  → Sends to LLM
  → Parses response for tool calls: [TOOL: name(args)]
  → Executes the LisPy function
  → Feeds result back to LLM
  → Returns final response

Built-in tools:
  resolve-card   — look up any card by name
  search-agents  — search the registry
  binder-status  — check portfolio status
  seed-hash      — get deterministic seed for a name
  kb-query       — search the knowledge base
  card-value     — check a card's floor value
```

### Offline Template Engine

```
offline-generate(prompt)
  → Pattern match on prompt:
    "what is @name"    → resolve-card, describe it
    "search for X"     → search-agents, list results
    "how many agents"  → binder-status, report count
    "value of @name"   → card-value, report floor
    "who owns"         → report binder address
    contains "decide"  → apply Three Rules framework
    contains "should"  → apply decision framework
    default            → "Running offline. Essentials available.
                          Connect Ollama for full AI."

smart-generate(prompt)
  → if orappter-ping: orappter-generate(prompt)
  → else: offline-generate(prompt)
  → Always returns something useful. Never fails silently.
```

---

## Device-to-Device Sync (Sneakernet)

When two devices meet without internet:

```
1. Export conversation:
   (conversation-export "session-42")
   → JSON string, small enough for QR code

2. Transfer via:
   - QR code scan
   - NFC tap
   - Bluetooth
   - Type the agent name (card self-assembles)
   - Copy-paste a JSON blob

3. Import on receiving device:
   (conversation-import json-string)
   → Full conversation restored with history

4. Transfer a card + its knowledge:
   (export-agent-state name)
   → Returns: card data + conversation history + knowledge entries
   → All in one JSON blob

5. Import on receiving device:
   (import-agent-state json-string)
   → Card resolves, conversations restored, knowledge loaded
   → The agent arrives fully formed
```

**The digital twin travels between devices.** No server. No internet. Just the name and its state.

---

## Battery-Aware Operation

Mobile-first means battery matters:

```
(battery-level)
  → Returns 0-100 (or nil if not available)

(battery-mode)
  → "full"    (> 50%): use local LLM, embeddings, full AI
  → "eco"     (20-50%): template responses, no embeddings
  → "minimal" (< 20%): card operations only, no AI
  → "dead"    (< 5%): save state and sleep

(auto-mode prompt)
  → Checks battery level
  → Routes to appropriate response mode
  → Always returns something useful
  → Saves state before battery dies
```

**Battery is the timer.** The system degrades gracefully. At 5%, it saves everything and sleeps. You pick up where you left off when you charge.

---

## Model Support

| Model | Size | Use Case |
|-------|------|----------|
| gemma3:1b | 1GB | Phone, low battery, fast responses |
| gemma3:4b | 4GB | Default. Good balance of speed and quality |
| gemma3:12b | 12GB | Laptop. High quality responses |
| gemma4 | TBD | When available. Hook at the endpoint. |
| llama3.2:3b | 3GB | Alternative. Good for conversation |
| mistral:7b | 7GB | Alternative. Good for code/analysis |
| phi3:mini | 3GB | Microsoft model. Small and fast |

**Model selection is automatic.** ORAPPTER checks what's available and uses the best option. No configuration needed.

---

## The Full Stack

```
Person types "@wildhaven/ceo-agent"
  ↓
Card self-assembles from name (deterministic, offline)
  ↓
Card attributes become system prompt (personality, expertise)
  ↓
ORAPPTER activates the card as a conversational agent
  ↓
Local Gemma 4 powers the responses (on device, private)
  ↓
Conversations persist in local storage (survives restarts)
  ↓
Knowledge base grows with every interaction
  ↓
Digital twin gets smarter over time
  ↓
Transfer to another device via sneakernet (QR, NFC, name)
  ↓
Twin arrives fully formed on the new device
  ↓
Battery dies → state saved → charge → pick up where you left off
  ↓
Your digital twin lives on.
```

---

## File Structure

```
RAR/
  rapp_sdk.py       ← Python SDK (CLI + library)
  rapp_sdk.lispy    ← LisPy SDK (browser + VM)
  orappter.lispy    ← ORAPPTER runtime (local AI)
  ORAPPTER.md       ← This spec
  HELLO.md          ← 10-command tutorial
  CONSTITUTION.md   ← The law
```

Three files. Three runtimes. One ecosystem. Everything offline.

---

## The Sentence

When someone asks "what is ORAPPTER?" — you say:

> **"It's the AI that runs on your device. No cloud. No internet. Your digital twin, powered by local AI, in your pocket. Battery is the timer."**

---

*ORAPPTER: Offline Rappter Runtime for Agents.*
*No cloud. No API key. No rate limits. No internet.*
*Your AI. Your device. Your twin. Lives on.*
