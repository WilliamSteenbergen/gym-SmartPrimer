from gym.envs.registration import register

register(
    id='SmartPrimer-deterministic-v0',
    entry_point='gym_SmartPrimer.envs:SmartPrimerEnv',
)
register(
    id='SmartPrimer-medium-v0',
    entry_point='gym_SmartPrimer.envs:SmartPrimerMediumEnv',
)
register(
    id='SmartPrimer-realistic-v0',
    entry_point='gym_SmartPrimer.envs:SmartPrimerHardEnv',
)