from configs.enemy_projectiles_config import BULLET, LASER,FIRE,LASERBEAM

MASHINEGUN = {
    "image": "Assets\guns\gun3.png",
    "atk_spd": 100,
    "size": (50, 50),
    "projectile": BULLET,
    "sound" : "Assets\Sound\Weapon\MashineGun.mp3",
    "channel": 1
}
BLASTER = {
    "image": "Assets\guns\gun4.png",
    "atk_spd": 100,
    "size": (50, 50),
    "projectile": LASER,
    "sound" : "Assets\Sound\Weapon\Blaster.mp3",
    "channel": 3
    }
FIRETHROWER = {
    "image" : "Assets\guns\gun5.png",
    "atk_spd": 100,
    "size" :(55,25),
    "projectile" : FIRE,
    "sound" : "Assets\Sound\Weapon\Firethrower.mp3",
    "channel": 4
}
LASERGUN = {
    "image": "Assets\guns\gun7.png",
    "atk_spd": 1000,
    "size": (50, 25),
    "projectile": LASERBEAM,
    "sound" : "Assets\Sound\Weapon\LaserBeam.mp3",
    "channel": 5
}
