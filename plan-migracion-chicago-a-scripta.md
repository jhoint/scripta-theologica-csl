# Plan de migracion: Chicago -> Scripta

## Objetivo
Partir de `chicago2scripta.csl` (basado en Chicago) y adaptarlo de forma incremental hasta obtener un estilo conforme a Scripta, manteniendo estabilidad funcional en notas y bibliografia.

## Principio de trabajo
Aprovechar la cobertura de casos complejos de Chicago (tipos de item, nombres, fechas, locators, ibid, etc.) y modificar primero la forma, despues la logica fina.

## Fases de migracion

### 1. Congelar base y alcance
- Usar `chicago2scripta.csl` como base unica de trabajo.
- Definir "Scripta v1" por escrito: puntuacion, mayusculas/minusculas, versalitas, comillas, abreviaturas (`ed.`, `eds.`, `p.`, `pp.`), reglas de notas y bibliografia.
- Resultado esperado: checklist de aceptacion breve y verificable.

### 2. Normalizar metadatos y estructura
- Ajustar `<info>` del estilo: titulo, `id`, `summary`, derechos/autor si procede.
- Revisar opciones globales de locale/terms y sorting.
- Resultado esperado: estilo identificable y consistente para pruebas.

### 3. Capa de forma (sin cambiar logica)
- Cambiar solo presentacion: puntos, comas, espacios, uso de mayusculas, cursivas/versalitas.
- Mantener intacta la logica de nombres, fechas, locators y sustituciones.
- Resultado esperado: salida visual cercana a Scripta en casos sencillos.

### 4. Macros criticas de nombres y titulos
- Adaptar macros de:
  - autor/editor/traductor,
  - titulo de obra y titulo de contenedor,
  - edicion/volumen/tomo.
- Resultado esperado: coherencia en libro, capitulo y articulo (notas y bibliografia).

### 5. Notas al pie (comportamiento)
- Ajustar reglas de citacion repetida (`ibid`, forma corta, primera/subsecuente).
- Verificar locators y delimitadores de nota.
- Resultado esperado: secuencias de notas correctas en casos reales.

### 6. Bibliografia (comportamiento y orden)
- Ajustar orden de campos, inversion de nombres, repeticion/sustitucion de autor y puntuacion final.
- Verificar claves de ordenacion.
- Resultado esperado: bibliografia estable y conforme a Scripta.

### 7. Matriz de pruebas y cierre
- Validar con conjunto minimo representativo:
  - libro (1 autor, 2+ autores, editor),
  - capitulo de libro colectivo,
  - articulo de revista,
  - tesis,
  - recurso web,
  - documento clasico/archivo (si aplica).
- Comparar contra ejemplos esperados en `zotero-outputs.md`.
- Resultado esperado: lista cerrada de diferencias pendientes y version "Scripta v1.0".

## Orden recomendado de archivos
1. `chicago2scripta.csl` como archivo principal de edicion.
2. `pruebas-scripta.json` para validacion de casos.
3. `zotero-outputs.md` para snapshots de salida esperada.
4. `CHANGELOG.md` para registrar decisiones y cambios.

## Ritmo sugerido de trabajo
1. Bloque 1: fases 1-3.
2. Bloque 2: fases 4-5.
3. Bloque 3: fases 6-7 y cierre documental.

## Criterio de exito
El estilo se considera listo cuando:
- la salida coincide con los ejemplos objetivo de Scripta en la matriz de pruebas,
- no hay regresiones graves respecto de la cobertura de Chicago,
- las diferencias residuales quedan documentadas en `CHANGELOG.md`.
