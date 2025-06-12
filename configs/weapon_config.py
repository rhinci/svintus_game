from configs.projectiles_config import BULLET, LASER, ROCKET,FIRE,LASERBEAM

MASHINEGUN = {
    "image": "Assets\guns\gun3.png",
    "atk_spd": 20,
    "size": (50, 50),
    "projectile": BULLET,
    "sound" : "Assets\Sound\Weapon\MashineGun.mp3",
    "channel": 1
}
ROCKETLAUNCHER = {
    "image": "Assets\guns\gun1.png",
    "atk_spd": 1,
    "size": (50, 50),
    "projectile": ROCKET,
    "sound" : "Assets\Sound\Weapon\RocketLauncher.mp3",
    "channel": 2
}
BLASTER = {
    "image": "Assets\guns\gun4.png",
    "atk_spd": 200,
    "size": (50, 50),
    "projectile": LASER,
    "sound" :"Assets\Sound\Weapon\Blaster.mp3",
    "channel": 3
}
FIRETHROWER = {
    "image" : "Assets\guns\gun5.png",
    "atk_spd": 50,
    "size" :(55,25),
    "projectile" : FIRE,
    "sound" : "Assets\Sound\Weapon\Firethrower.mp3",
    "channel": 4
}
LASERGUN = {
    "image": "Assets\guns\gun7.png",
    "atk_spd": 1000,
    "size": (50, 50),
    "projectile": LASERBEAM,
    "sound" : "Assets\Sound\Weapon\LaserBeam.mp3",
    "channel": 5
}
