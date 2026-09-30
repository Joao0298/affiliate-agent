from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any
from agent import AffiliateAgent
from config import AffiliateProduct

@dataclass
class AgentResult:
    agent: str
    status: str
    data: dict[str, Any] = field(default_factory=dict)
    notes: list[str] = field(default_factory=list)

class BaseAgent:
    name = "base"
    def run(self, context): return AgentResult(self.name, "ok")

class ProductHunterAgent(BaseAgent):
    name = "product_hunter"
    def run(self, context): return AgentResult(self.name, "ok", {"count": len(context.get("products", [])), "products": context.get("products", [])})

class TrendAgent(BaseAgent):
    name = "trend_agent"
    def run(self, context): return AgentResult(self.name, "ok", {"signals": context.get("trend_signals", [])})

class CompetitorAgent(BaseAgent):
    name = "competitor_agent"
    def run(self, context): return AgentResult(self.name, "ok", {"competitors": context.get("competitors", [])})

class AnalyzerAgent(BaseAgent):
    name = "analyzer_agent"
    def __init__(self): self.core = AffiliateAgent()
    def run(self, context):
        scored = []
        for product in context.get("products", []):
            if isinstance(product, AffiliateProduct):
                scored.append({"product": product.model_dump(), "score": self.core.score(product)})
        scored.sort(key=lambda x: x["score"], reverse=True)
        return AgentResult(self.name, "ok", {"ranked_products": scored})

class PriceAgent(BaseAgent):
    name = "price_agent"
    def run(self, context): return AgentResult(self.name, "ok", {"price_signals": context.get("price_signals", [])})

class CommissionAgent(BaseAgent):
    name = "commission_agent"
    def run(self, context): return AgentResult(self.name, "ok", {"commission_signals": context.get("commission_signals", [])})

class ContentAgent(BaseAgent):
    name = "content_agent"
    def __init__(self): self.core = AffiliateAgent()
    def run(self, context):
        packages = []
        for item in context.get("ranked_products", [])[:context.get("content_limit", 5)]:
            p = AffiliateProduct.model_validate(item["product"])
            packages.append({"product": p.name, "score": item["score"], "content": self.core.content_brief(p).model_dump()})
        return AgentResult(self.name, "ok", {"content_packages": packages})

class ApprovalAgent(BaseAgent):
    name = "approval_agent"
    def run(self, context):
        return AgentResult(self.name, "pending_approval", {"approval_items": len(context.get("content_packages", []))}, ["Publicação automática bloqueada até aprovação humana."])

class AnalyticsAgent(BaseAgent):
    name = "analytics_agent"
    def run(self, context): return AgentResult(self.name, "ok", {"metrics": context.get("metrics", {})})

class AffiliateMultiAgentSystem:
    def __init__(self):
        self.agents = [ProductHunterAgent(), TrendAgent(), CompetitorAgent(), AnalyzerAgent(), PriceAgent(), CommissionAgent(), ContentAgent(), ApprovalAgent(), AnalyticsAgent()]
    def run(self, context):
        state = dict(context)
        results = []
        for agent in self.agents:
            result = agent.run(state)
            results.append(result)
            state.update(result.data)
        return {"status": "completed", "results": [r.__dict__ for r in results], "state": state}

if __name__ == "__main__":
    from config import Marketplace
    demo = AffiliateProduct(marketplace=Marketplace.SHOPEE, name="Fone Bluetooth", url="https://example.com", price=89.90, rating=4.8, reviews=1200, commission_percent=8)
    output = AffiliateMultiAgentSystem().run({"products": [demo], "trend_signals": ["audio portátil"], "content_limit": 1})
    print("MULTI_AGENT_SYSTEM_OK")
    print("AGENTS:", [r["agent"] for r in output["results"]])
    print("APPROVAL:", output["state"]["approval_items"], "item(s) aguardando aprovação")
