from prompt_optimizer.poptim import (
    Sequential, 
    PunctuationOptim, 
    LemmatizerOptim, 
    AutocorrectOptim
)
from prompt_optimizer.poptim import LemmatizerOptim
from prompt_optimizer.metric import TokenMetric, BERTScoreMetric





prompt = """Write a story for a game which is decribed as follows:
Elden Ring is presented through a third-person perspective, with players freely roaming its interactive open world. The six main areas are traversed using the player character's steed Torrent as the primary mode of transportation, while linear hidden dungeons can be explored to find useful items. Combat is facilitated by several types of weapons and magic spells, including non-direct engagement enabled by stealth mechanics. Checkpoints located throughout the world allow for the player to improve their attributes using an in-game currency called Runes, as well as acting as locations that enable fast travel. Elden Ring features online multiplayer, with players able to join each other for both cooperative and player versus player combat.
"""

p_optimizer = Sequential(
    LemmatizerOptim(verbose=True, metrics=[TokenMetric(), BERTScoreMetric()]),
    PunctuationOptim(verbose=True, metrics=[TokenMetric(), BERTScoreMetric()]),
    AutocorrectOptim(verbose=True, metrics=[TokenMetric(), BERTScoreMetric()]),
)
optimized_prompt = p_optimizer(prompt)

print(optimized_prompt)