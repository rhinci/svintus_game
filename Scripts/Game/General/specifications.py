class specifications:
    def set_stats(self, atk, spd_atk, spd, max_hp,tag):
        super().__init__()
        self.atk = atk
        self.spd_atk = spd_atk
        self.spd = spd
        self.max_hp = max_hp
        self.curr_hp = max_hp
        self.tag = tag

    # HP
    def death(self):
        self.kill()

    def change_hp(self, change):
        self.curr_hp += change
        if self.curr_hp <= 0:
            self.death()
        elif self.curr_hp > self.max_hp:
            self.curr_hp = self.max_hp

    def change_max_hp(self, change):
        self.max_hp += change
        if self.max_hp <= 0:
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
