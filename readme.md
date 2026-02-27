# Scripta Theologica CSL

En este repositorio se ofrece la hoja de estilos CSL para la revista *Scripta Theologica* de la Facultad de Teología de la Universidad de Navarra.

De momento no es un proyecto oficial, sino un desarrollo personal que todavía está en fase de pruebas.

Se ha seguido como referencia la [documentación de CSL](https://docs.citationstyles.org/en/stable/index.html)

## Archivos
scripta-theologica.csl: es el archivo del estilo que hay que usar.

pruebas-scripta.json: es la bibliografía que aparece en los ejemplos de las normas para los autores que se ha empleado para probar el estilo

Lorem ipsum dolor sit amet.docx: es el documento de word en el que se están haciendo las pruebas.

## Particularidades del estilo

### dir./dirs. en vez de ed./eds.
Si en una obra colectiva hay director/es en vez de editor/es, se usará la variable "editorial-director" en vez de "editor".

En Zotero esto hay que hacerlo poniendo en el campo Adicional lo siguiente: "editorial-director: Apellido || Nombre". 


### Documentos de Archivo

Para citar documentos de archivo en Zotero con este estilo:

#### Configuración en Zotero

1. **Tipo de documento**: Selecciona **Manuscript** (Manuscrito)

2. **Campos a rellenar**:
   - **Archive** (Archivo): La abreviatura del archivo (ej: `ACB`)
     - Se mostrará en VERSALITAS
   
   - **Title** (Título): El título del documento (ej: `Comunicado de prensa`)
     - Se mostrará en *cursiva*
   
   - **Date** (Fecha): La fecha del documento (ej: `1946-06-21`)
     - Se mostrará como texto (ej: 21 de junio de 1946)
   
   - **Loc. in Archive** (Signatura): Carpeta, legajo o signatura (ej: `Carpeta 1428`)
     - Se mostrará tal cual

#### Formato resultante

La cita aparecerá como:

**ACB, *Comunicado de prensa*, 21 de junio de 1946, Carpeta 1428**

#### Notas importantes

- Los manuscritos **NO** aparecerán automáticamente en la bibliografía final
- Las notas a pie de página con información completa del archivo (ciudad, nombre completo, fondo) debes crearlas manualmente como fuentes primarias
- Todas las citas posteriores usarán el mismo formato (no hay versión acortada automática)
