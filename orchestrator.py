from __future__ import annotations
from datetime import datetime, timezone
from multi_agent import AffiliateMultiAgentSystem

class AffiliateOrchestrator:
    """Coordena o pipeline. Não inventa dados externos: recebe produtos/sinais de fontes reais."""
    def __init__(self):
        self.system = AffiliateMultiAgentSystem()

    def execute(self, request: dict):
        required = ["products"]
        missing = [k for k in required if k not in request]
        if missing:
            raise ValueError(f"Missing required inputs: {missing}")
        result = self.system.run(request)
        result["orchestrator"] = {
            "status": "completed",
            "executed_at": datetime.now(timezone.utc).isoformat(),
            "data_mode": request.get("data_mode", "external_input"),
        }
        return result

if __name__ == "__main__":
    from config import AffiliateProduct, Marketplace
    products = [
        AffiliateProduct(marketplace=Marketplace.SHOPEE, name="Fone Bluetooth X", url="https://example.com/shopee/x", price=89.90, rating=4.8, reviews=1200, commission_percent=8),
        AffiliateProduct(marketplace=Marketplace.AMAZON, name="Suporte para Notebook Y", url="https://example.com/amazon/y", price=129.90, rating=4.6, reviews=850, commission_percent=5),
        AffiliateProduct(marketplace=Marketplace.MERCADO_LIVRE, name="Luminária LED Z", url="https://example.com/meli/z", price=59.90, rating=4.7, reviews=2300, commission_percent=7),
    ]
    out = AffiliateOrchestrator().execute({
        "data_mode": "controlled_virtual_test_data",
        "products": products,
        "trend_signals": ["acessórios para home office"],
        "content_limit": 3,
    })
    print("ORCHESTRATOR_OK")
    print("STATUS:", out["status"])
    print("DATA_MODE:", out["orchestrator"]["data_mode"])
    print("PRODUCTS:", len(out["state"]["products"]))
    print("RANKING:")
    for item in out["state"]["ranked_products"]:
        print(f"- {item['product']['name']} | score={item['score']}")
    print("CONTENT_PACKAGES:", len(out["state"]["content_packages"]))
    print("APPROVAL_ITEMS:", out["state"]["approval_items"])
