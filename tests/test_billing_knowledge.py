from orchestration.platform_bootstrap import PlatformBootstrap

from knowledge.knowledge_query_service import KnowledgeQueryService

PlatformBootstrap.initialize()

print(KnowledgeQueryService.ask("What is telecom billing?"))
