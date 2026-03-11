---
applyTo: "**/chicago2scripta.csl,**/pruebas-scripta.json,**/zotero-outputs.md,**/CHANGELOG.md"
---

# Instrucciones de trabajo: Chicago -> Scripta

Objetivo: adaptar `chicago2scripta.csl` desde una base Chicago hacia el estilo editorial de Scripta sin perder estabilidad funcional.

## Reglas principales
- Trabajar por fases: forma primero, logica despues.
- Hacer cambios pequenos y verificables.
- Evitar refactors amplios sin necesidad.
- Mantener compatibilidad con casos comunes de Chicago, salvo exigencia explicita de Scripta.

## Orden de intervencion
1. Presentacion tipografica y puntuacion.
2. Macros de nombres y titulos.
3. Notas al pie (`ibid`, forma corta, locators).
4. Bibliografia (orden, inversion de nombres, sustitucion de autor, puntuacion final).

## Seguridad de cambios
- No eliminar macros existentes sin reemplazo funcional comprobado.
- No mezclar muchos cambios de estilo y logica en la misma propuesta.
- Explicar siempre que macro cambia y por que.

## Validacion minima
- Verificar contra casos en `pruebas-scripta.json`.
- Contrastar salida con `zotero-outputs.md`.
- Registrar decisiones importantes en `CHANGELOG.md`.

## Criterio de listo
Un cambio esta listo cuando mejora la conformidad con Scripta y no introduce regresiones evidentes en notas o bibliografia.
