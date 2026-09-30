# AGENTS.md — Affiliate Agent

## Objetivo
Este projeto implementa um sistema multi-agente para descoberta, análise e criação de conteúdo de afiliados.

## Regras
- Não inventar preço, comissão, avaliação, estoque ou links.
- Usar apenas APIs, feeds ou mecanismos oficialmente autorizados pelos marketplaces.
- Nunca versionar segredos, tokens, cookies ou arquivos .env.
- Manter aprovação humana antes de publicação.
- Tratar preço, comissão e estoque como dados temporais.
- Preservar origem e timestamp quando dados reais forem integrados.

## Estrutura
- `config.py`: modelos e enumerações.
- `agent.py`: scoring e geração de briefing.
- `providers.py`: adaptadores dos marketplaces.
- `multi_agent.py`: agentes especializados.
- `orchestrator.py`: coordenação do pipeline.
- `test_orchestrator.py`: testes do fluxo.
- `PDR.md`: requisitos e roadmap.
