from enn_trainer.train import State, init_train_state, train
from enn_trainer.config import TrainConfig
import hyperstate
from env import Env

@hyperstate.stateful_command(TrainConfig, State, init_train_state)
def main(state_manager: hyperstate.StateManager) -> None:
    train(state_manager=state_manager, env=Env)

if __name__ == "__main__":
    main()