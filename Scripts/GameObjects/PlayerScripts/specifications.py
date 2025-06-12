from Scripts.GameObjects.PlayerScripts.statistics_collector import run_stats

class specifications:
    def set_stats(self, stats):
        super().__init__()
        self.atk = stats['atk']
        self.spd_atk = stats['spd_atk']
        self.spd = stats['spd']
        self.max_hp = stats['max_hp']
        self.curr_hp = self.max_hp
        self.EXP = 0
        self.tag = stats['tag']
    # HP
    def death(self):
        pass
    def is_dead(self):
        if self.curr_hp <= 0:
            self.death()
            return True
        return False
    def is_alive(self):
        return self.alive and self.curr_hp > 0
    def change_hp(self, change):
        self.curr_hp += change
        if change < 0:
            if self.tag == 'Player':
                run_stats.increment_stat("4. Damage taken", abs(change))
            else:
                run_stats.increment_stat("5. Damage dealt", abs(change))

        if self.curr_hp > self.max_hp:
            self.curr_hp = self.max_hp
        self.is_dead()
    # EXP
    def change_exp(self, change):
        self.EXP += change
