import pygame
import sys
from entities import Character
from ui import ClickButton
from upgrades import GymMember, TimeMachine

# 1. ต้อง init ก่อนเสมอ! (สำคัญมาก)
pygame.init() 

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("LifeClicker")

font = pygame.font.SysFont("Arial", 24) 
large_font = pygame.font.SysFont("Arial", 40, bold=True)

# 2. ย้ายการสร้าง Object ที่ใช้ Font มาไว้หลัง init
player = Character()

# สร้างไอเทมอัปเกรด
upgrades = [
    GymMember("Gym Membership", base_cost=10, multiplier=0.5),
    TimeMachine("Time Machine", base_cost=50, multiplier=1.0)
]

# สร้างปุ่ม (ตรงนี้แหละที่เคย Error เพราะมันเรียกใช้ Font ใน ui.py)
upgrade_buttons = []
for i, upg in enumerate(upgrades):
    btn = ClickButton(550, 100 + (i * 100), 220, 60, f"Buy {upg.name}", (100, 100, 100))
    upgrade_buttons.append(btn)

# ปุ่มคลิกหลัก
click_btn = ClickButton(300, 450, 200, 80, "LIVE 1 YEAR", (70, 130, 180))

last_update_time = pygame.time.get_ticks()

# ในส่วน Setup ของ main.py
try:
    bg_images = {
        "home.png": pygame.image.load("assets/home.png").convert(),
        "school.png": pygame.image.load("assets/school.png").convert(),
        "train.png": pygame.image.load("assets/train.png").convert(),
        "park.png": pygame.image.load("assets/park.png").convert()
    }
except pygame.error:
    # ถ้าโหลดไม่สำเร็จ ให้สร้าง Surface เปล่ากันโปรแกรมพัง (Fallback)
    print("Warning: Asset images not found, using placeholders.")
    bg_images = {k: pygame.Surface((800, 600)) for k in ["home.png", "school.png", "train.png", "park.png"]}
    
while True:
    current_time = pygame.time.get_ticks()
    
    # --- 1. Event Handling ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            # คลิกปุ่มหลัก
            if click_btn.is_clicked(event.pos):
                player.grow()
            
            # คลิกปุ่มอัปเกรด
            for i, btn in enumerate(upgrade_buttons):
                if btn.is_clicked(event.pos):
                    cost = upgrades[i].get_cost()
                    # สมมติว่าเรามีระบบเงิน หรือใช้ "อายุ" แลก (ในที่นี้ลองใช้คลิกสะสมแลก)
                    upgrades[i].apply_effect(player)
                    print(f"Bought {upgrades[i].name}! Level: {upgrades[i].level}")

    # --- 2. Logic (Auto-Growth) ---
    # เพิ่มอายุอัตโนมัติทุกๆ 1 วินาที (1000 ms)
    if current_time - last_update_time >= 1000:
        if player.auto_growth_rate > 0:
            player.grow(player.auto_growth_rate)
        last_update_time = current_time

    # --- 3. Rendering ---
    screen.fill((240, 240, 240)) # 1. ล้างหน้าจอด้วยสีพื้นหลัง (ต้องทำทุกเฟรม)

    # 2. วาดสถานะตัวละคร
    stage = player.get_stage_info()
    # วาดสี่เหลี่ยมตัวละคร
    pygame.draw.rect(screen, stage["color"], (350, 200, 100, 150), border_radius=15)
    
    # 3. วาดข้อความ (Text)
    # ใช้ font ที่เราเพิ่งประกาศแก้ Error ไปเมื่อกี้
    age_text = font.render(f"Age: {player.age} Years", True, (50, 50, 50))
    screen.blit(age_text, (20, 20))
    
    stage_text = font.render(f"Stage: {stage['name']}", True, stage["color"])
    screen.blit(stage_text, (20, 70))

    # 4. วาดปุ่ม
    click_btn.draw(screen)
    for btn in upgrade_buttons:
        btn.draw(screen)

    # 5. แสดงผลที่วาดทั้งหมด (สำคัญมาก! ถ้าไม่มีหน้าจอจะดำ)
    pygame.display.flip()