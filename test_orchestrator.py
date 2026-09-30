from orchestrator import AffiliateOrchestrator
from config import AffiliateProduct, Marketplace

def test_empty_input():
    try:
        AffiliateOrchestrator().execute({})
    except ValueError as e:
        assert "products" in str(e)
    else:
        raise AssertionError("Expected validation error")

def test_pipeline():
    p = AffiliateProduct(marketplace=Marketplace.SHOPEE, name="Teste", url="https://example.com", price=100, rating=5, reviews=1000, commission_percent=10)
    out = AffiliateOrchestrator().execute({"data_mode":"controlled_virtual_test_data","products":[p],"content_limit":1})
    assert out["status"] == "completed"
    assert len(out["state"]["ranked_products"]) == 1
    assert len(out["state"]["content_packages"]) == 1
    assert out["state"]["approval_items"] == 1

test_empty_input()
test_pipeline()
print("ALL_TESTS_PASSED")
