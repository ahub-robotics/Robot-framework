rom random import random

from robot_manager.base import Bot
from robot_manager.flow import RobotFlow
from .flow import Nodes

class Robot(Bot):
    def __init__(self, **kwargs):
        # Initialize the base class (Bot)
        super().__init__(**kwargs)

    @RobotFlow(node=Nodes.StartNode, children='initial_check')
    def start(self, *args):
        print("Starting nested conditional workflow")

    @RobotFlow(node=Nodes.ConditionNode, children={True:"first_condition_true", False:"first_condition_false"}, condition=lambda x: x < 5)
    def initial_check(self, *args):
        # The lambda function evaluates and returns a boolean value
        condition = random.randint(0, 5)
        print(f"First check evaluation for {condition}")
        return condition

    @RobotFlow(node=Nodes.OperationNode, children="secondary_check")
    def first_condition_true(self, *args):
        print("Initial condition met, proceeding with first true branch")

    @RobotFlow(node=Nodes.OperationNode, children="end")
    def first_condition_false(self, *args):
        print("Initial Not met, proceeding with first true branch")

    @RobotFlow(node=Nodes.ConditionNode, children={True:"second_condition_true", False:"second_condition_false"}, condition=lambda x: x > 5)
    def secondary_check(self, *args):
        # Secondary condition check with a lambda function that returns a boolean value
        condition = random.randint(0, 10)
        print(f"Second check evaluation for {condition}")
        return condition

    @RobotFlow(node=Nodes.OperationNode, children="end")
    def second_condition_true(self, *args):
        print("Secondary condition met, executing specific task")

    @RobotFlow(node=Nodes.OperationNode,  children="end")
    def second_condition_false(self, *args):
        print("Secondary condition not met, executing alternative task")

    @RobotFlow(node=Nodes.EndNode)
    def end(self, *args):
        print("Ending nested conditional workflow")
