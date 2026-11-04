# Citación de Obras Clásicas en Scripta Theologica

## Ejemplos de formato esperado

### CITATION (primera cita)

**Primera cita:** RUFINO DE AQUILEYA, *Historia ecclesiastica*, I, 6: Patrologia Latina 21, 473-475.

### CITATION (citas posteriores)

**Citas posteriores:** RUFINO DE AQUILEYA, *Historia ecclesiastica*, I, 7: PL 21, 477.

### BIBLIOGRAPHY

**Bibliografía:** RUFINO DE AQUILEYA, *Historia ecclesiastica*, Patrologia Latina 21, Paris, 1849, 461-540. Si la ficha tiene editor: RUFINO DE AQUILEYA, *Historia ecclesiastica*, en Vallarsi, D. (ed.), Patrologia Latina 21, Paris, 1849, 461-540.

Las páginas se escriben **sin «p.»**: el estilo imprime las páginas sin etiqueta.

## Configuración en Zotero

### 1. Crear un nuevo elemento de tipo "Book section = Sección de un libro"

En Zotero, crea un nuevo elemento y configura los siguientes campos:


| Campo                        | Valor Ejemplo          | Notas                                                                                        |
| ------------------------------ | ------------------------ | ---------------------------------------------------------------------------------------------- |
| **Title = Título**          | Historia ecclesiastica | Título de la obra clásica                                                                  |
| **Author = Autor**           | Rufino de Aquileya     | Autor antiguo                                                                                |
| **Collection Title = Serie** | Patrologia Latina      | Nombre completo de la colección                                                             |
| **collection-title-short**   | PL                     | Hay que ponerlo en el campo "extra = adicional". Sigla de la colección: sale solo en las citas posteriores |
| **Volume = Volumen**         | 21                     | Número del volumen de la serie                                                              |
| **Pages = Páginas**         | 461-540                | Rango completo de páginas de la obra en la edición (sale en la bibliografía; en la cita va el locator y, después, las páginas citadas) |
| **Publisher Place = Lugar**  | Paris                  | Lugar de publicación de la edición                                                         |
| **Date = Fecha**             | 1849                   | Año de la edición usada                                                                    |
| **Editor**                   | Domenico Vallarsi      | Editor de la edición (si aplica)                                                            |
| **Extra = Adicional**        | `type: classic`        | **CRÍTICO**                                                                                 |

### 2. Campo "Extra" - INDISPENSABLE

```
type: classic
```

Sin este campo, el elemento se formatea como un capítulo (título entre comillas, «en Vallarsi, D. (ed.)»…) y **se pierden la serie y el volumen**: RUFINO DE AQUILEYA, «Historia ecclesiastica», en VALLARSI, Domenico (ed.), Paris, 1849, 461-540.

### 3. Collection Title vs Collection Title Short

- **Collection Title**: Nombre completo (Patrologia Latina, Patrologia Graeca, etc.)
- **Collection Title Short**: Abreviatura (PL, PG, CSEL, ACW, etc.) - **Aparece en las citas posteriores**; la primera cita y la bibliografía llevan siempre el nombre completo.

Si solo rellenas "Collection Title" sin "Collection Title Short", las citas posteriores también llevan el nombre completo.

---

## Estructura de datos en Zotero - Ejemplo completo

```
Item Type:             Book section
Title:                 Historia ecclesiastica
Creator:               Rufino de Aquileya (Author)
Collection Title:      Patrologia Latina
Volume:                21
Pages:                 461-540
Publisher Place:       Paris
Date:                  1849
Creator:               Domenico Vallarsi (Editor)
Extra:                 type: classic
                       collection-title-short: PL
```

**Resultado esperado:**

- **Primera cita:** RUFINO DE AQUILEYA, *Historia ecclesiastica*, I, 6: Patrologia Latina 21, 473-475.
- **Citas posteriores:** RUFINO DE AQUILEYA, *Historia ecclesiastica*, I, 7: PL 21, 477.
- **Bibliografía** (con el editor de este ejemplo): RUFINO DE AQUILEYA, *Historia ecclesiastica*, en Vallarsi, D. (ed.), Patrologia Latina 21, Paris, 1849, 461-540. Sin editor: RUFINO DE AQUILEYA, *Historia ecclesiastica*, Patrologia Latina 21, Paris, 1849, 461-540.

---

## Cómo citar con locator

Con el complemento de Word de Zotero hay que proporcionar el **locator** cada vez que se cita (**esta indicación y la del sufijo no se han podido comprobar con el complemento; lo comprobado es la sección «Con Pandoc»**):

- `I, 6` - Libro I, sección 6
- `X, 5` - Libro X, sección 5
- `I-II` - Libros I a II (sale con raya: «I–II»)

Escribe solo el pasaje, **sin la palabra «libro(s)»**: Pandoc la toma por una etiqueta y no la imprime (`{libros X-XI}` sale «X–XI»).

En el **sufijo** van las páginas de la edición citada, sin «p.» y sin punto al final:

```, 473-475```

### Con Pandoc

El locator va entre llaves, pegado a la clave, y las páginas de la edición después:

```markdown
[@rufino{I, 6}, 473-475]
```

Dentro de una nota con texto propio: `@rufino [{I, 6}, 473-475]`. No se escribe `[@rufino, I, 6, 473-475]`: Pandoc no reconoce `I, 6` como locator y lo coloca detrás de la edición.

---

## Notas importantes

1. **`type: classic` es obligatorio añadirlo en el campo extra** - Sin él, se formateará como un libro normal
2. **collection-title-short** - Es lo que aparecerá en las citas posteriores (PL, PG, etc.). Si no existe, usa Collection Title
3. **Volume = número de serie** - El número del volumen dentro de la colección
4. **Pages** - El rango de páginas/columnas de la edición: sale solo en la bibliografía. En las citas van las páginas que escribas después del locator
5. **Editor** - Incluye el editor de la edición si está disponible
6. **Date & Publisher Place** - Referencia la edición consultada (salen solo en la bibliografía)
7. **No rellenes «Título del libro» (Book Title)** en una obra clásica: si lo hay, la **bibliografía** imprime ese título en cursiva en lugar del Título, mientras que las citas siguen usando el Título. Comprobado con Pandoc 3.8.2.

## Solución de problemas

**P: ¿Por qué aparece como un libro normal?**
R: Falta `type: classic` en el campo Extra (sale como un capítulo, sin serie ni volumen).

**P: ¿Las siglas PL no aparecen?**
R: Rellena explícitamente en el campo extra lo siguiente: "collection-title-short: PL". Solo salen en las citas posteriores.

**P: ¿El editor no aparece en bibliografía?**
R: Verifica que esté en "Creator" con rol "Editor".
