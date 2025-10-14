# Sistema de Mantenimiento - Documentación

## 📋 Resumen de Correcciones Realizadas

### 1. **Modelo de Datos (mantenimiento_model.py)**
- ✅ Corregido el nombre del método `update_matenimiento_fin` → `update_mantenimiento_fin`
- ✅ Añadido campo `fecha_creacion` para tracking
- ✅ Campos nullable correctamente configurados
- ✅ Valores por defecto en `__init__` ahora son `None` en lugar de strings vacíos
- ✅ Añadido ordenamiento descendente por fecha de creación

### 2. **Controlador (mantenimiento_controller.py)**
- ✅ Corregido el nombre de la función `update_ticket` → `update_ticket_ini`
- ✅ Implementado manejo correcto de archivos con `werkzeug.secure_filename`
- ✅ Añadida validación de tipos de archivo permitidos
- ✅ Creación automática del directorio de uploads
- ✅ Manejo de errores con try-except
- ✅ Validación de existencia de tickets antes de operaciones
- ✅ Corrección del atributo `enctype="multipart/form-data"` en formularios
- ✅ Mejorado el PDF con tabla formateada y estilos

### 3. **Vistas (mantenimiento_view.py)**
- ✅ Eliminada variable `users` no definida
- ✅ Corregido el nombre del template `base.html` → `list_tickets.html`
- ✅ Nombres de funciones consistentes con el controlador
- ✅ Corregido el blueprint en `url_for` de `ticket` → `mantenimiento`

### 4. **Templates HTML**
- ✅ **base.html**: Añadido sistema de mensajes flash, URLs dinámicas con `url_for`
- ✅ **list_tickets.html**: Nuevo template con tabla completa de tickets
- ✅ **actualizar_ini.html**: Formulario completo con valores prellenados
- ✅ **actualizar_fin.html**: Añadido `enctype` para subida de archivos
- ✅ **generate_ticket.html**: Vista completa del ticket con evidencia fotográfica
- ✅ **crear.html**: Formulario de creación corregido

### 5. **Estilos CSS (style.css)**
- ✅ Sistema completo de estilos modernos
- ✅ Estilos para tablas, formularios, botones
- ✅ Sistema de colores para prioridades y estados
- ✅ Diseño responsive
- ✅ Estilos para mensajes flash

### 6. **Configuración (run.py)**
- ✅ Creación automática del directorio de uploads
- ✅ Límite de tamaño de archivos configurado
- ✅ Mejor mensaje de confirmación de base de datos

### 7. **Dependencias (requirements.txt)**
- ✅ Añadidas todas las dependencias necesarias
- ✅ werkzeug para manejo seguro de archivos

## 🚀 Instalación y Ejecución

### Paso 1: Crear entorno virtual
```bash
python -m venv venv
```

### Paso 2: Activar entorno virtual
**Windows:**
```bash
venv\Scripts\activate
```

**Linux/Mac:**
```bash
source venv/bin/activate
```

### Paso 3: Instalar dependencias
```bash
pip install -r requirements.txt
```

### Paso 4: Ejecutar la aplicación
```bash
cd app
python run.py
```

La aplicación estará disponible en: `http://localhost:5000`

## 📁 Estructura del Proyecto

```
app/
├── controllers/
│   └── mantenimiento_controller.py
├── models/
│   └── mantenimiento_model.py
├── views/
│   └── mantenimiento_view.py
├── templates/
│   ├── base.html
│   ├── crear.html
│   ├── list_tickets.html
│   ├── actualizar_ini.html
│   ├── actualizar_fin.html
│   └── generate_ticket.html
├── static/
│   ├── css/
│   │   └── style.css
│   └── uploads/
│       └── evidencias/
├── utils/
│   └── decorators.py
├── database.py
└── run.py
```

## 🔐 Sistema de Permisos

### Roles disponibles:
1. **Usuario normal**: Puede crear tickets y verlos
2. **Mantenimiento**: Puede iniciar y finalizar tickets
3. **Admin**: Puede hacer todo + eliminar tickets

## 📝 Flujo de Trabajo

### 1. Crear Ticket
- Cualquier usuario puede crear un ticket
- Debe especificar descripción y prioridad

### 2. Iniciar Mantenimiento (Solo Mantenimiento/Admin)
- Asignar responsable
- Establecer fecha de inicio y fin estimada
- Estimar costo
- Puede modificar la prioridad

### 3. Finalizar Mantenimiento (Solo Mantenimiento/Admin)
- Indicar si el trabajo fue completado
- Subir foto de evidencia (obligatoria)

### 4. Ver y Descargar
- Ver detalles completos del ticket
- Descargar reporte en PDF

## 🎨 Características del Sistema

✅ CRUD completo de tickets
✅ Sistema de roles y permisos
✅ Subida de imágenes como evidencia
✅ Generación de reportes PDF
✅ Interfaz moderna y responsive
✅ Sistema de mensajes flash
✅ Validación de formularios
✅ Manejo de errores

## ⚠️ Notas Importantes

1. **Seguridad**: Cambiar `SECRET_KEY` en producción
2. **Base de datos**: Por defecto usa SQLite (cambiar para producción)
3. **Archivos**: Las evidencias se guardan en `static/uploads/evidencias/`
4. **Límite de archivos**: 16MB máximo por archivo
5. **Formatos permitidos**: PNG, JPG, JPEG, GIF

## 🐛 Solución de Problemas

### Error: "No module named 'flask'"
```bash
pip install -r requirements.txt
```

### Error: "Template not found"
Verificar que estés en el directorio `app/` al ejecutar

### Error al subir archivos
Verificar que el directorio `static/uploads/evidencias/` tenga permisos de escritura

## 📧 Soporte

Para más información o reportar problemas, revisar el código fuente y comentarios en cada archivo.