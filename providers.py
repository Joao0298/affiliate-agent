"""Adaptadores para programas oficiais de afiliados.

Cada marketplace terá um conector separado. O agente deve consumir APIs,
feeds ou links oficiais autorizados, nunca depender de scraping proibido.
"""
from abc import ABC, abstractmethod
from config import AffiliateProduct

class Provider(ABC):
    name: str
    @abstractmethod
    def search(self, query: str, limit: int = 10) -> list[AffiliateProduct]: ...

class ShopeeProvider(Provider):
    name = "shopee"
    def search(self, query: str, limit: int = 10):
        raise NotImplementedError("Conectar credenciais/API ou ferramenta oficial da Shopee")

class MercadoLivreProvider(Provider):
    name = "mercado_livre"
    def search(self, query: str, limit: int = 10):
        raise NotImplementedError("Conectar aplicação/credenciais oficiais do Mercado Livre")

class AmazonProvider(Provider):
    name = "amazon"
    def search(self, query: str, limit: int = 10):
        raise NotImplementedError("Conectar Amazon Associates + Product Advertising API")

class ShopifyProvider(Provider):
    name = "shopify"
    def search(self, query: str, limit: int = 10):
        raise NotImplementedError("Conectar programa/loja/Collabs autorizado")
