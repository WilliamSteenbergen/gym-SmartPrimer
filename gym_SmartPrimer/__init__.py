from gym.envs.registration import register

register(
    id='SmartPrimer-v0',
    entry_point='gym_SmartPrimer.envs:SmartPrimer',
)
register(
    id='SmartPrimer-extrahard-v0',
    entry_point='gym_SmartPrimer.envs:SmartPrimerExtraHardEnv',
)