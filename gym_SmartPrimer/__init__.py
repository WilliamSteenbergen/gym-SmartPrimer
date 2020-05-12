from gym.envs.registration import register

register(
    id='SmartPrimer-v0',
    entry_point='gym_SmartPrimer.envs:SmartPrimerEnv',
)
register(
    id='SmartPrimer-extrahard-v0',
    entry_point='gym_SmartPrimer.envs:SmartPrimerExtraHardEnv',
)