from agent_frameworks.load_frameworks import load_frameworks

from orchestration.framework_manager import FrameworkManager


class FrameworkBootstrap:
    @staticmethod
    def initialize():

        print("\nInitializing Framework Layer...\n")

        FrameworkManager.load()

        load_frameworks()

        print("Frameworks Loaded")

        print("\nFramework Layer Ready\n")
