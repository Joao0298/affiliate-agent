from config import AffiliateProduct, ContentPackage

class AffiliateAgent:
    """Orquestrador: descoberta -> normalização -> análise -> conteúdo."""

    def score(self, p: AffiliateProduct) -> float:
        score = 0.0
        if p.rating is not None:
            score += min(max(p.rating / 5, 0), 1) * 30
        if p.reviews is not None:
            score += min(p.reviews / 1000, 1) * 20
        if p.commission_percent is not None:
            score += min(max(p.commission_percent / 20, 0), 1) * 25
        if p.price is not None and p.price > 0:
            score += 25 * (1 - min(p.price / 1500, 1))
        return round(score, 1)

    def content_brief(self, p: AffiliateProduct) -> ContentPackage:
        return ContentPackage(
            hook=f"Achado: {p.name}",
            caption=f"Encontrei este produto na {p.marketplace}. Confira preço e condições pelo link.",
            cta="Veja o produto pelo link e confira o preço atual.",
            hashtags=["#achadinhos", "#ofertas", "#afiliados", f"#{p.marketplace}"],
        )

if __name__ == "__main__":
    print("Affiliate Agent: multi-marketplace core OK")
