class PlayerData:
    def __init__(self):
        self.gold = 500  # 기본 재화
        self.inventory = None  # Inventory 객체 연결

    def add_gold(self, amount):
        self.gold += amount
        print(f"골드 +{amount} → {self.gold}")

    def spend_gold(self, amount):
        if self.gold >= amount:
            self.gold -= amount
            print(f"골드 -{amount} → {self.gold}")
            return True
        else:
            print("골드 부족!")
            return False


player_data = PlayerData()
