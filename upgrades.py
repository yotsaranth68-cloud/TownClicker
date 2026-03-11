from abc import ABC, abstractmethod

class BaseUpgrade(ABC):
    def __init__(self, name, base_cost, multiplier):
        self.name = name
        self.base_cost = base_cost
        self.multiplier = multiplier
        self.level = 0

    def get_cost(self):
        # ราคาเพิ่มขึ้นแบบ Exponential (ความซับซ้อนที่อาจารย์ชอบ)
        return int(self.base_cost * (1.2 ** self.level))

    @abstractmethod
    def apply_effect(self, player):
        pass

class GymMember(BaseUpgrade):
    """คลิก 1 ครั้งได้อายุเพิ่มขึ้น (Manual Click Boost)"""
    def apply_effect(self, player):
        player.years_per_click += self.multiplier
        self.level += 1

class TimeMachine(BaseUpgrade):
    """อายุเพิ่มขึ้นเองอัตโนมัติทุกวินาที (Passive Growth)"""
    def apply_effect(self, player):
        # ในระดับนี้เราอาจจะเก็บค่าไว้ในตัวแปรอื่นใน Character
        player.auto_growth_rate += self.multiplier
        self.level += 1