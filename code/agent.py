import random
from typing import Dict, Any, List

# ==============================================================================
# PHASE 1: GAME STATE PARSER CLASSES (DAY 2 STRUCTURE)
# ==============================================================================

class PokemonState:
    """Parses individual Pokémon statistics on the field."""
    def __init__(self, data: Dict[str, Any]):
        if data:
            self.card_id: int = data.get("card_id", -1)
            self.hp: int = data.get("hp", 0)
            self.max_hp: int = data.get("max_hp", 0)
            self.energies: List[int] = data.get("energies", [])
            self.statuses: List[str] = data.get("statuses", [])
        else:
            self.card_id = -1
            self.hp = 0
            self.max_hp = 0
            self.energies = []
            self.statuses = []

class BoardSide:
    """Parses an entire side of the playing board (Yours or Opponent's)."""
    def __init__(self, data: Dict[str, Any], is_opponent: bool = False):
        self.active = PokemonState(data.get("active", {}))
        self.bench = [PokemonState(p) for p in data.get("bench", [])]
        self.prize_count: int = data.get("prize_count", 6)
        self.deck_count: int = data.get("deck_count", 60)
        self.discard_pile: List[int] = data.get("discard_pile", [])
        
        if is_opponent:
            self.hand_size: int = data.get("hand_size", 0)
            self.hand: List[int] = []  # Hidden track information
        else:
            self.hand: List[int] = data.get("hand", [])
            self.hand_size: int = len(self.hand)

class GameStateParser:
    """Combines all observations into a comprehensive game snapshot."""
    def __init__(self, observation: Dict[str, Any]):
        self.logs: List[str] = observation.get("logs", [])
        self.legal_options: List[Dict[str, Any]] = observation.get("legal_options", [])
        
        # Build independent environmental perspectives
        self.my_side = BoardSide(observation.get("my_side", {}), is_opponent=False)
        self.opponent_side = BoardSide(observation.get("opponent_side", {}), is_opponent=True)

# ==============================================================================
# PHASE 2: CORE KAGGLE AGENT & STRATEGY ENGINE
# ==============================================================================

def agent(observation: Dict[str, Any], configuration: Any) -> int:
    """
    Kaggle Engine call handler. Parses the observation and selects an action.
    """
    # 1. Transform raw environment input into safe object models
    state = GameStateParser(observation)
    
    # Validation fallback
    if not state.legal_options:
        return 0
        
    # 2. Heuristic Rule 1: Apply immediate offensive pressure
    for index, option in enumerate(state.legal_options):
        if option.get("type") == "attack":
            return index

    # 3. Heuristic Rule 2: Mitigate risk if the active Pokémon faces imminent KO
    if 0 < state.my_side.active.hp <= 20:
        for index, option in enumerate(state.legal_options):
            if option.get("type") in ["switch", "retreat"]:
                return index

    # 4. Heuristic Rule 3: Maintain tactical pace by loading active energy
    for index, option in enumerate(state.legal_options):
        if option.get("type") == "attach_energy":
            if option.get("target") == "active":
                return index

    # 5. Default Fallback execution
    return 0
