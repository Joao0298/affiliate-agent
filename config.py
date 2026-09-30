from enum import StrEnum
from pydantic import BaseModel

class Marketplace(StrEnum):
    SHOPEE = "shopee"
    MERCADO_LIVRE = "mercado_livre"
    AMAZON = "amazon"
    SHOPIFY = "shopify"

class AffiliateProduct(BaseModel):
    marketplace: Marketplace
    external_id: str | None = None
    name: str
    url: str
    affiliate_url: str | None = None
    price: float | None = None
    old_price: float | None = None
    rating: float | None = None
    reviews: int | None = None
    commission_percent: float | None = None
    category: str | None = None
    image_url: str | None = None
    stock: bool | None = None

class ContentPackage(BaseModel):
    hook: str
    caption: str
    cta: str
    hashtags: list[str]
    disclosure: str = "Conteúdo com link de afiliado. Posso receber comissão pela compra."
