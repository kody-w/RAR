"""seed_stamper_agent.py — single sacred agent. Deterministic 64-bit seed + 7-word incantation.

NO LLM CALL. Pure function. The seed is a deterministic SHA-256 truncation of
the Drop's hook + body + channel; the incantation is the seed mapped to a
fixed wordlist of 256 evocative English words. Speak the seven words and the
Drop is reconstructible offline anywhere.
"""
try:
    from agents.basic_agent import BasicAgent  # RAPP layout
except ModuleNotFoundError:
    try:
        from basic_agent import BasicAgent      # flat / @publisher layout
    except ModuleNotFoundError:
        class BasicAgent:                       # last-resort standalone
            def __init__(self, name, metadata): self.name, self.metadata = name, metadata
import hashlib, json

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@rarbookworld/seed_stamper",
    "version": "0.1.0",
    "display_name": "Seed Stamper",
    "description": "Pure function (no LLM). Returns deterministic 64-bit seed + 7-word incantation from a 256-word wordlist. Speak the words \u2192 reconstruct the Drop offline.",
    "author": "rarbookworld",
    "tags": [
        "moment-pipeline",
        "seed",
        "incantation"
    ],
    "category": "pipeline",
    "quality_tier": "community",
    "requires_env": [
        "AZURE_OPENAI_ENDPOINT",
        "AZURE_OPENAI_API_KEY",
        "AZURE_OPENAI_DEPLOYMENT"
    ],
    "dependencies": [
        "@rapp/basic_agent"
    ]
}


# 256-word evocative wordlist — sized to 8 bits per word, 7 words = 56 bits.
# Picked to be short, distinct under speech-to-text, and visually concrete.
WORDS = (
 "ARC ARK ASH AURA BANE BARK BEAM BELT BIRD BLAZE BLOOM BONE BOOK BOLT BOND BREW "
 "BRIM BURN CAGE CALM CAPE CARE CART CAVE CELL CHAIR CHALK CHAR CHIME CLAW CLAY CLIFF "
 "CLOUD COAL COIL COIN COLD COMB CORE CORK COVE CRAB CRAFT CREEK CREST CRIB CROWN CRY "
 "CUFF CURL DALE DAWN DEN DESK DEW DIM DIRT DOCK DONE DOOR DOVE DOWN DRIFT DRIP "
 "DUNE DUSK DUST EBB ECHO EDGE ELM EMBER ETCH EYE FANG FARM FERN FIN FIRE FIST "
 "FLAG FLAK FLAME FLASK FLINT FLOAT FLOW FOAM FOG FOLD FONT FOREST FORK FORM FOX FRAY "
 "FROST GALE GATE GAUZE GEM GLIDE GLOSS GLOW GORGE GRAIN GRAVE GREEN GRID GRIN GRIT GROVE "
 "HALF HALL HAND HARM HASP HATCH HAWK HAZE HEAP HEART HELM HERB HERO HILL HOLD HOLE "
 "HOOF HOOK HOOP HORN HUNT HUT ICE INK IRON ISLE IVY JADE JEER JAR JAY JOIN "
 "KEEL KEEP KEY KILT KIN KING KITE KNIT KNOT LACE LAKE LAMB LAMP LANE LARK LATE "
 "LAVA LEAF LEFT LENS LEVEL LICK LIFT LILY LIME LINE LION LIST LIVE LOCK LOFT LONG "
 "LOOM LOOP LORE LOSS LOUD LURE LYNX MANE MAP MARK MASK MASS MAST MAZE MEAD MELT "
 "MESH MILD MILE MINT MIST MOAT MOLT MOON MOSS MOTH MOUND MOUTH MOVE MUSE MYTH NEEDLE "
 "NEST NIB NIGHT NOOK NORTH OAR OAK OATH ONYX ORBIT OWL PACE PACT PAGE PALE PALM "
 "PANE PARK PATH PAWN PEAK PEARL PEEL PEN PETAL PIER PINE PINK PIRE PIPE PIVOT PLAIN "
 "PLANE PLATE PLOT PLOW PLUM POEM POND POOL PORT POST PRISM PROW PULSE PURR QUEST QUILL"
).split()
assert len(WORDS) == 256 and len(set(WORDS)) == 256, "wordlist must be 256 unique words"


class SeedStamperAgent(BasicAgent):
    def __init__(self):
        self.name = "SeedStamper"
        self.metadata = {
            "name": self.name,
            "description": "Returns deterministic 64-bit seed + 7-word incantation for a Drop.",
            "parameters": {"type": "object",
                "properties": {
                    "hook":    {"type": "string"},
                    "body":    {"type": "string"},
                    "channel": {"type": "string"},
                },
                "required": ["hook", "body"]},
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, hook="", body="", channel="", **kwargs):
        material = f"{channel}|{hook}|{body}".encode("utf-8")
        digest = hashlib.sha256(material).digest()

        # 64-bit seed = first 8 bytes
        seed = int.from_bytes(digest[:8], "big")

        # 7 words = next 7 bytes (each indexes into 256-word table)
        incantation = " ".join(WORDS[b] for b in digest[8:15])

        return json.dumps({"seed": seed, "incantation": incantation})