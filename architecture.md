# Arquitetura

USER -> Dashboard/API -> Affiliate Agent -> Provider Adapters
                                  |-> Shopee
                                  |-> Mercado Livre
                                  |-> Amazon
                                  |-> Shopify/Collabs
                                  -> Opportunity Scorer -> LLM Content -> Human Approval -> Channels

Princípios:
- credenciais somente em .env/secret manager;
- links de afiliado gerados por fonte autorizada;
- preço/comissão/estoque tratados como dados temporais;
- publicação automática somente após aprovação e integração autorizada;
- logs de origem para cada produto.
