# Citación de Obras Clásicas en Scripta Theologica

## Ejemplos de formato esperado

### CITATION (primera cita)
```
Rufino de Aquileya, Historia ecclesiastica, i, 6, PL 21, 473-475
```

### CITATION (citas posteriores)
```
Rufino de Aquileya, Historia ecclesiastica, i, 6, PL 21, 472
```

### BIBLIOGRAPHY
```
Rufino de Aquileya, Historia ecclesiastica i-ii, en Domenico Vallarsi (ed.), PL 21, 461-540, Paris, 1849.
```

---

## Configuración en Zotero

### 1. Crear un nuevo elemento de tipo "Book"

En Zotero, crea un nuevo elemento y configura los siguientes campos:

| Campo | Valor Ejemplo | Notas |
|-------|---------------|-------|
| **Title** | Historia ecclesiastica | Título de la obra clásica |
| **Creator (Author)** | Rufino de Aquileya | Autor antiguo |
| **Collection Title** | Patrologia Latina | Nombre completo de la colección |
| **Collection Title Short** | PL | Abreviatura (CSL 1.0.2+) - aparece en citas |
| **Volume** | 21 | Número del volumen de la serie |
| **Pages** | 473-475 | Páginas/columnas de la edición |
| **Publisher Place** | Paris | Lugar de publicación de la edición |
| **Date** | 1849 | Año de la edición usada |
| **Creator** | Domenico Vallarsi | Editor de la edición (si aplica) |
| **Extra** | `type: classic` | **CRÍTICO** |

### 2. Campo "Extra" - INDISPENSABLE

```
type: classic
```

Sin este campo, se formateará como un libro normal.

### 3. Collection Title vs Collection Title Short

- **Collection Title**: Nombre completo (Patrologia Latina, Patrologia Graeca, etc.)
- **Collection Title Short**: Abreviatura (PL, PG, CSEL, ACW, etc.) - **Esto es lo que aparece en las citas**

Si solo rellenas "Collection Title" sin "Collection Title Short", el estilo mostrará el nombre completo.

---

## Estructura de datos en Zotero - Ejemplo completo

```
Item Type:             Book
Title:                 Historia ecclesiastica
Creator:               Rufino de Aquileya (Author)
Collection Title:      Patrologia Latina
Collection Title Short: PL
Volume:                21
Pages:                 473-475
Publisher Place:       Paris
Date:                  1849
Creator:               Domenico Vallarsi (Editor)
Extra:                 type: classic
```

**Resultado esperado:**
- **Primera cita:** `Rufino de Aquileya, Historia ecclesiastica, i, 6, PL 21, 473-475`
- **Citas posteriores:** `Rufino de Aquileya, Historia ecclesiastica, i, 6, PL 21, 472`
- **Bibliografía:** `Rufino de Aquileya, Historia ecclesiastica i-ii, en Domenico Vallarsi (ed.), PL 21, 461-540, Paris, 1849.`

---

## Cómo citar con locator

Proporciona el **locator** cada vez que cites:

- `i, 6` - Libro I, sección 6
- `x, 5` - Libro X, sección 5
- `i-ii` - Libros I a II
- `libros x y xi` - Forma textual

En Zotero, especifica el locator en el campo correspondiente durante la cita.

---

## Notas importantes

1. **`type: classic` es obligatorio** - Sin él, se formateará como un libro normal
2. **Collection Title Short** - Es lo que aparecerá en citas (PL, PG, etc.). Si no existe, usa Collection Title
3. **Volume = número de serie** - El número del volumen dentro de la colección
4. **Pages** - El rango de páginas/columnas en todas las citas
5. **Editor** - Incluye el editor de la edición si está disponible
6. **Date & Publisher Place** - Referencia la edición consultada

---

## Ejemplos adicionales

### San Agustín, Confesiones
```
Item Type:             Book
Title:                 Confessiones
Creator:               Augustinus (Author)
Collection Title:      Patrologia Latina
Collection Title Short: PL
Volume:                32
Pages:                 659-868
Publisher Place:       Paris
Date:                  1841
Extra:                 type: classic
```

### San Jerónimo,Commentarii in Evangelium Matthaei
```
Item Type:             Book
Title:                 Commentarii in Evangelium Matthaei
Creator:               Hieronymus (Author)
Collection Title:      Patrologia Latina
Collection Title Short: PL
Volume:                26
Pages:                 15-218
Publisher Place:       Paris
Date:                  1845
Extra:                 type: classic
```

---

## Solución de problemas

**P: ¿Por qué aparece como un libro normal?**
R: Falta `type: classic` en el campo Extra.

**P: ¿Las siglas PL no aparecen?**
R: Rellena explícitamente "Collection Title Short" con "PL".

**P: ¿El editor no aparece en bibliografía?**
R: Verifica que esté en "Creator" con rol "Editor".
