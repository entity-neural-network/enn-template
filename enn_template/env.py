from typing import Dict, Mapping
from entity_gym.runner import CliRunner
from entity_gym.env import *
import random

class Env(Environment):
    def reset(self) -> Observation:
        return self._observe()

    def obs_space(self) -> ObsSpace:
        return ObsSpace(
            global_features=[],
            entities={
                "Dummy": Entity(["x", "y"]),
            }
        )

    def action_space(self) -> Dict[str, ActionSpace]:
        return {
            "EndEpisode": GlobalCategoricalActionSpace(["yes", "no"]),
        }


    def act(self, actions: Mapping[ActionName, Action]) -> Observation:
        if actions["EndEpisode"].label == "yes":
            done = True
            reward = 1.0
        else:
            done = False
            reward = 0.0
        return self._observe(done, reward)

    def _observe(self, done: bool = False, reward: float = 0.0) -> Observation:
        return Observation(
            global_features=[],
            features={
                "Dummy": [[0, 0]],
            },
            done=done,
            reward=reward,
            actions={
                "EndEpisode": GlobalCategoricalActionMask(),
            },
        )

if __name__ == "__main__":
    env = Env()
    CliRunner(env).run()
