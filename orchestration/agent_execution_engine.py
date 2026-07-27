from agent_registry.agent_factory import AgentFactory

from event_bus.events.agent_events import (
    AgentStartedEvent,
    AgentCompletedEvent,
    AgentFailedEvent,
)

from event_bus.publishers.agent_event_publisher import AgentEventPublisher


class AgentExecutionEngine:
    @staticmethod
    def execute(agent_name, task):

        agent = AgentFactory.get_agent(agent_name)

        AgentEventPublisher.publish(AgentStartedEvent(agent_name))

        try:
            result = agent.execute(task)

            AgentEventPublisher.publish(AgentCompletedEvent(agent_name))

            return result

        except Exception as error:
            AgentEventPublisher.publish(AgentFailedEvent(agent_name, error))

            raise
