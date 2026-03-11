# Copilot Instructions - Migracion Chicago -> Scripta

## Contexto del repositorio
Este repositorio mantiene estilos CSL para Scripta Theologica. La estrategia actual es partir de una base Chicago y adaptar de forma incremental hasta cumplir las reglas editoriales de Scripta.

Archivo base principal:
- `chicago2scripta.csl`

Archivos de apoyo:
- `pruebas-scripta.json` (casos de prueba)
- `zotero-outputs.md` (salidas esperadas/referencias)
- `CHANGELOG.md` (registro de cambios)

## Objetivo de Copilot
Al proponer o editar cambios, priorizar estabilidad funcional y cambios pequeños, verificables y reversibles.

## Flujo obligatorio de trabajo
1. Mantener una unica base de edicion: `chicago2scripta.csl`.
2. Aplicar cambios por fases: primero forma tipografica/puntuacion, luego logica de macros.
3. Evitar refactors masivos sin una necesidad clara.
4. Documentar decisiones relevantes en `CHANGELOG.md`.

## Prioridades de modificacion
1. Presentacion:
- Puntos, comas, espacios, uso de mayusculas/minusculas, cursivas y versalitas.
- No tocar logica de citacion si no es necesario.

2. Macros de alto impacto:
- Nombres: autor/editor/traductor.
- Titulos: obra y contenedor.
- Datos editoriales: edicion, volumen, tomo.

3. Comportamiento de notas:
- Primera cita vs citas subsecuentes.
- `ibid` y forma corta.
- Locators (`p.`, `pp.` y otros terminos aplicables).

4. Bibliografia:
- Orden de campos.
- Inversion de nombres.
- Repeticion/sustitucion de autor.
- Puntuacion de cierre.

## Reglas de seguridad
- No eliminar macros existentes si no hay reemplazo funcional comprobado.
- No cambiar varias decisiones de estilo y logica en el mismo commit.
- Mantener compatibilidad con casos comunes de Chicago salvo cuando Scripta exija lo contrario.

## Criterios de aceptacion por cambio
- El cambio incluye una justificacion breve.
- El impacto esperado esta descrito (que salidas deben cambiar y cuales no).
- Se valida contra ejemplos representativos en `pruebas-scripta.json`.

## Convenciones para propuestas de Copilot
- Proponer diffs pequenos y concretos.
- Explicar siempre que macro se toca y por que.
- Si hay incertidumbre, ofrecer 2 alternativas y recomendar una.
- Priorizar claridad sobre ingenieria compleja.

## Definicion de listo (v1)
Un cambio se considera listo cuando mejora la conformidad con Scripta y no introduce regresiones evidentes en notas o bibliografia.
