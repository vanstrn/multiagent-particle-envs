from gym.envs.registration import register

import multiagent.scenarios as scenarios

# Multiagent envs
# ----------------------------------------

scenario = scenarios.load("simple.py").Scenario()
register(
    id='MultiagentSimple-v0',
    entry_point='multiagent.environment:MultiAgentEnv',
    max_episode_steps=100,
    kwargs={"world":scenario.make_world(),
        "reset_callback":scenario.reset_world,
        "reward_callback":scenario.reward,
        "observation_callback":scenario.observation}
)

scenario = scenarios.load("simple_speaker_listener.py").Scenario()
register(
    id='MultiagentSimpleSpeakerListener-v0',
    entry_point='multiagent.environment:MultiAgentEnv',
    max_episode_steps=100,
    kwargs={"world":scenario.make_world(),
        "reset_callback":scenario.reset_world,
        "reward_callback":scenario.reward,
        "observation_callback":scenario.observation}
)

scenario = scenarios.load("simple_tag.py").Scenario()
register(
    id='PredPrey-v0',
    entry_point='multiagent.environment:MultiAgentEnv',
    max_episode_steps=100,
    kwargs={"world":scenario.make_world(),
        "reset_callback":scenario.reset_world,
        "reward_callback":scenario.reward,
        "observation_callback":scenario.observation}
)

scenario = scenarios.load("simple_spread.py").Scenario()
register(
    id='CooperativeNavigation-v0',
    entry_point='multiagent.environment:MultiAgentEnv',
    max_episode_steps=100,
    kwargs={"world":scenario.make_world(),
        "reset_callback":scenario.reset_world,
        "reward_callback":scenario.reward,
        "observation_callback":scenario.observation}
)

scenario = scenarios.load("simple_speaker_listener.py").Scenario()
register(
    id='CooperativeCommunication-v0',
    entry_point='multiagent.environment:MultiAgentEnv',
    max_episode_steps=100,
    kwargs={"world":scenario.make_world(),
        "reset_callback":scenario.reset_world,
        "reward_callback":scenario.reward,
        "observation_callback":scenario.observation}
)
