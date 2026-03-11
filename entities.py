import pygame

class Character:
    def __init__(self):
        self._age = 0  # Encapsulation: ซ่อนข้อมูลไว้ภายใน
        self.years_per_click = 1
        self.auto_growth_rate = 0 # อายุที่จะเพิ่มขึ้นเองต่อวินาที
    def grow(self, amount=None):
        if amount is None:
            self._age += self.years_per_click
        else:
            self._age += amount

    @property
    def age(self):
        return int(self._age)

    def get_stage_info(self):
        """Polymorphism logic: คืนค่าข้อมูลตามช่วงอายุ"""
        if self._age < 12:
            return {"name": "Child", "color": (135, 206, 235)} # สีฟ้า
        elif self._age < 20:
            return {"name": "Teenager", "color": (255, 105, 180)} # สีชมพู
        elif self._age < 60:
            return {"name": "Adult", "color": (34, 139, 34)} # สีเขียว
        else:
            return {"name": "Elder", "color": (169, 169, 169)} # สีเทา   
        
# entities.py
def get_stage_info(self):
    if self._age < 12:
        return {
            "name": "Child", 
            "color": (135, 206, 235),
            "bg_image": "home.png" # ชื่อไฟล์ภาพพื้นหลังตอนเด็ก
        }
    elif self._age < 20:
        return {
            "name": "Teenager", 
            "color": (255, 105, 180),
            "bg_image": "school.png"
        }
    elif self._age < 60:
        return {
            "name": "Adult", 
            "color": (34, 139, 34),
            "bg_image": "train.png" # เปลี่ยนเป็นรถไฟตอนเป็นผู้ใหญ่
        }
    else:
        return {
            "name": "Elder", 
            "color": (169, 169, 169),
            "bg_image": "park.png"
        }