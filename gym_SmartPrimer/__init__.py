from gym.envs.registration import register

register(
    id='SmartPrimer-v0',
    entry_point='gym_SmartPrimer.envs.Deterministic:SmartPrimerEnv',
)
register(
    id='SmartPrimer-medium-v0',
    entry_point='gym_SmartPrimer.envs.Medium:SmartPrimerMediumEnv',
)
register(
    id='SmartPrimer-realistic-v0',
    entry_point='gym_SmartPrimer.envs.Realistic_Hard:SmartPrimerHardEnv',
)