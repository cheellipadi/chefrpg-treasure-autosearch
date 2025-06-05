from enum import Enum, auto

class ChestRarity(Enum):
    NONE = auto()
    COMMON = auto()
    RARE = auto()
    EPIC = auto()
    LEGENDARY = auto()

# Initialize count storage
chest_counts = {
    ChestRarity.COMMON: 0,
    ChestRarity.RARE: 0,
    ChestRarity.EPIC: 0,
    ChestRarity.LEGENDARY: 0,
}

def increment_chest(rarity, count=1):
    if rarity in chest_counts:
        chest_counts[rarity] += count

def get_chest_summary():
    return (
        f"🟢 Common: {chest_counts[ChestRarity.COMMON]}\n"
        f"🔵 Rare: {chest_counts[ChestRarity.RARE]}\n"
        f"🟣 Epic: {chest_counts[ChestRarity.EPIC]}\n"
        f"🟡 Legendary: {chest_counts[ChestRarity.LEGENDARY]}"
    )
