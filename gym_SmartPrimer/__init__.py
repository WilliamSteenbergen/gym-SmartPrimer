from gym.envs.registration import register

register(
    id='SmartPrimer-deterministic-v1',
    entry_point='gym_SmartPrimer.envs.V1:SmartPrimerEnv',
)
register(
    id='SmartPrimer-medium-v1',
    entry_point='gym_SmartPrimer.envs.V1:SmartPrimerMediumEnv',
)
register(
    id='SmartPrimer-realistic-v1',
    entry_point='gym_SmartPrimer.envs.V1:SmartPrimerHardEnv',
)
register(
    id='SmartPrimer-dynamic-v1',
    entry_point='gym_SmartPrimer.envs.V1:SmartPrimerDynamicEnv',
)

register(
    id='SmartPrimer-realistic-v2',
    entry_point='gym_SmartPrimer.envs.V2:SmartPrimerDynamicEnv',
)