# PDR — Affiliate Agent Multi-Agent System

## 1. Visão
Plataforma de agentes de IA para descoberta, análise e produção de conteúdo para marketing de afiliados em Shopee, Mercado Livre, Amazon e Shopify.

## 2. Objetivo do MVP
Permitir que o usuário informe um nicho, faixa de preço ou objetivo e receba produtos candidatos, análise de oportunidade, pacote de conteúdo e uma fila de aprovação humana.

## 3. Arquitetura
Orchestrator coordena:
- Product Hunter
- Trend Agent
- Competitor Agent
- Analyzer Agent
- Price Agent
- Commission Agent
- Content Agent
- Approval Agent
- Analytics Agent

## 4. Fluxo
Input → descoberta → normalização → análise → score → conteúdo → aprovação → publicação autorizada → métricas → otimização.

## 5. Marketplaces
- Shopee
- Mercado Livre
- Amazon
- Shopify/Collabs

Cada integração deve usar APIs, feeds, programas de afiliados ou mecanismos oficialmente autorizados. O sistema não deve depender de scraping proibido.

## 6. Requisitos funcionais
- RF01: cadastrar nichos e filtros.
- RF02: receber produtos de conectores.
- RF03: armazenar origem e timestamp dos dados.
- RF04: calcular Opportunity Score.
- RF05: gerar hooks, legendas, CTAs e hashtags.
- RF06: manter aprovação humana antes de publicação.
- RF07: registrar links de afiliado autorizados.
- RF08: acompanhar cliques, conversões e comissão quando a fonte fornecer esses dados.
- RF09: executar tarefas por agendamento.
- RF10: manter histórico e auditoria.

## 7. Requisitos não funcionais
- Segredos somente em ambiente seguro.
- Dados externos tratados como temporais.
- Logs estruturados.
- Testes automatizados.
- Arquitetura modular por marketplace.
- LGPD: minimizar dados pessoais e permitir exclusão quando aplicável.

## 8. Segurança
Nunca versionar .env, tokens, chaves ou cookies. Credenciais devem ser fornecidas pelo usuário e armazenadas fora do código-fonte.

## 9. Human-in-the-loop
A publicação automática fica bloqueada por padrão. O usuário aprova o conteúdo antes de qualquer ação de publicação.

## 10. Métricas
- produtos descobertos
- produtos aprovados
- CTR
- conversão
- comissão
- receita
- desempenho por marketplace
- desempenho por conteúdo

## 11. Roadmap
### Fase 1 — Core
Orchestrator + agentes + testes.

### Fase 2 — Dados reais
Conectores oficiais para marketplaces.

### Fase 3 — Dashboard
Web app, autenticação, banco e fila de aprovação.

### Fase 4 — Automação
Scheduler, alertas, geração em lote e publicação autorizada.

### Fase 5 — Intelligence
Trend detection, histórico de preços, concorrentes e otimização por métricas.

## 12. Critério de sucesso do MVP
Uma solicitação deve percorrer o pipeline completo com dados de fonte identificada, produzir conteúdo reproduzível e parar na aprovação humana sem inventar atributos do produto.
