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
    total = get_total_chests()
    if total>0:
        return (
            f"🟢 Common: {chest_counts[ChestRarity.COMMON]} ({(chest_counts[ChestRarity.COMMON]* 100) / total:.1f}%)\n"
            f"🔵 Rare: {chest_counts[ChestRarity.RARE]} ({(chest_counts[ChestRarity.RARE]* 100) / total:.1f}%)\n"
            f"🟣 Epic: {chest_counts[ChestRarity.EPIC]} ({(chest_counts[ChestRarity.EPIC]* 100) / total:.1f}%)\n"
            f"🟡 Legendary: {chest_counts[ChestRarity.LEGENDARY]} ({(chest_counts[ChestRarity.LEGENDARY]* 100) / total:.1f}%)\n"
            f"📊 Total: {get_total_chests()}"
        )

def get_total_chests():
    return sum(chest_counts[rarity] for rarity in ChestRarity if rarity != ChestRarity.NONE)
