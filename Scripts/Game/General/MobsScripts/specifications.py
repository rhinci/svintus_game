from Scripts.Game.General.statistics_collector import run_stats


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
        return hasattr(self, 'alive') and self.alive and self.curr_hp > 0

    def change_hp(self, change):
        self.curr_hp += change
        if change < 0:
            run_stats.increment_stat("4. Damage taken", abs(change))
        if self.curr_hp > self.max_hp:
            self.curr_hp = self.max_hp
        self.is_dead()

    def change_max_hp(self, change):
        self.max_hp += change
        if self.is_dead():
            self.death()

    def get_curr_hp(self):
        return self.curr_hp

    def get_max_hp(self):
        return self.max_hp

    # atk
    def change_atk(self, change):
        self.atk += change
        if self.atk <= 0:
            self.atk = 0

    def get_atk(self):
        return self.atk

    # spd_atk
    def change_spd_atk(self, change):
        self.spd_atk += change
        if self.spd_atk <= 0:
            self.spd_atk = 0

    def get_spd_atk(self):
        return self.spd_atk

    # spd
    def change_spd(self, change):
        self.spd += change
        if self.change_spd <= 0:
            self.change_spd = 0

    def get_spd(self):
        return self.spd

    # EXP
    def change_exp(self, change):
        self.EXP += change
