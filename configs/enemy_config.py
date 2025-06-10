MELEE_ENEMY = {
    "animation": {"idle":
                      ["Assets\Animations\Melee_enemy_anim\melee_idle\spider-0001.png",
                       "Assets\Animations\Melee_enemy_anim\melee_idle\spider-0002.png"]},
    "atk": 1,
    "spd_atk": 5,
    "spd": 3,
    "max_hp": 100,
    "scale": (100, 100),
    "tag": 'enemy'
}
RANGE_ENEMY = {
    "animation": {"idle":
                      ["Assets\Animations\Range_enemy_anim\enemy-0001.png",
                       "Assets\Animations\Range_enemy_anim\enemy-0002.png",
                       "Assets\Animations\Range_enemy_anim\enemy-0003.png",
                       "Assets\Animations\Range_enemy_anim\enemy-0004.png"]},
    "atk": 1,
    "spd_atk": 5,
    "spd": 3,
    "max_hp": 100,
    "scale": (100, 100),
    "tag": 'enemy',
    "attack_range" : 250
}

LIST_OF_ENEMYS = [MELEE_ENEMY, RANGE_ENEMY]
