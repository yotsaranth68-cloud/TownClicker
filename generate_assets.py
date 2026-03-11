import pygame
import os

def create_assets():
    pygame.init()
    if not os.path.exists('assets'):
        os.makedirs('assets')

    # ตั้งค่าสี
    colors = {
        "home": (255, 235, 205),   # สีครีม (บ้าน)
        "school": (200, 230, 255), # สีฟ้าอ่อน (โรงเรียน)
        "train": (50, 50, 70),     # สีเทาเข้ม (รถไฟ)
        "park": (150, 210, 150)    # สีเขียว (สวนสาธารณะ)
    }

    for name, color in colors.items():
        surface = pygame.Surface((800, 600))
        surface.fill(color)
        
        # วาดดีเทลแบบง่ายๆ ให้ดูออกว่าเป็นที่ไหน
        if name == "home":
            pygame.draw.rect(surface, (150, 75, 0), (300, 200, 200, 250)) # ประตู
        elif name == "school":
            pygame.draw.rect(surface, (255, 255, 255), (100, 100, 600, 100)) # กระดานดำ
        elif name == "train":
            pygame.draw.rect(surface, (100, 100, 120), (0, 150, 800, 300)) # หน้าต่างรถไฟ
        elif name == "park":
            pygame.draw.circle(surface, (34, 139, 34), (600, 200), 50) # ต้นไม้

        pygame.image.save(surface, f"assets/{name}.png")
        print(f"Created: assets/{name}.png")

    pygame.quit()

if __name__ == "__main__":
    create_assets()