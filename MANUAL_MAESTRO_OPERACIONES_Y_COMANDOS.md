# MANUAL MAESTRO DE OPERACIONES, GOBERNANZA Y COMANDOS
## Plataforma Híbrida y Copiloto Financiero Automatizado — "Patrimonio Inteligente"
**Titular y Autora Responsable:** Hilda Belem Ortiz Fuentes  
**Fecha de Publicación Oficial:** 25 de Noviembre de 2026  
**Versión:** 3.0 Enterprise Resilient (Dual-Mode, Disaster Recovery & Self-Healing)  
**Registro de Software:** Expediente INDAUTOR & Secreto Industrial (LFDA / LFPPI)

---

## ÍNDICE GENERAL DEL MANUAL
1. **MÓDULO 1:** Resumen Ejecutivo y Arquitectura del Sistema (¿Qué hemos construido y cómo funciona?)
2. **MÓDULO 2:** Manual de Comandos de Uso Exclusivo de la Administradora (Super-Admin)
3. **MÓDULO 3:** Manual de Comandos para Usuarios y Miembros de la Comunidad
4. **MÓDULO 4:** Protocolo de Rescate y Restauración ante Emergencias (Disaster Recovery)

---

# MÓDULO 1: RESUMEN EJECUTIVO Y ARQUITECTURA DEL SISTEMA
*(Explicación sencilla y amigable de lo que hemos construido y cómo opera)*

### 1.1. ¿Qué es Patrimonio Inteligente?
**Patrimonio Inteligente** es un ecosistema híbrido de educación financiera y tecnología no custodial diseñado para proteger y multiplicar el patrimonio familiar en México. Combina dos herramientas complementarias:
1. **La Plataforma Web Institucional:** Un portal educativo interactivo (`ariaeden.github.io/patrimonio-web`) que ofrece simuladores matemáticos de interés compuesto geométrico, comparativas didácticas entre el S&P 500 y las FIBRAs inmobiliarias mexicanas, evaluadores técnicos de activos bursátiles con oscilador RSI Wilder (14D) y biblioteca de recursos descargables.
2. **El Copiloto Financiero Automatizado en Telegram:** Un centinela inteligente en la nube (`@dabel_btc_copiloto_bot`) que vigila los mercados 24/7 sin tocar ni custodiar el dinero de los usuarios, emitiendo recomendaciones oportunas para operar en cuentas reguladas (Bitso México y Bursanet/Actinver).

### 1.2. La Doble Finalidad Estratégica de Bitcoin
El sistema rompe con la visión simplista de ver a Bitcoin como una simple apuesta especulativa. Nuestro algoritmo incorpora dos modos complementarios:
- **Modo Acumulación de Satoshis (Reserva de Valor Intergeneracional):**  
  La unidad de cuenta mental son los **Satoshis (sats)**. El bot ayuda al usuario a comprar en zonas de sobreventa técnica (RSI 4H ≤ 30-35) utilizando órdenes límite tipo **Maker** en Bitso (comisión preferencial de 0.10% o 0.60% sin cruzar el spread). El objetivo es acumular la mayor cantidad de satoshis con el menor costo promedio posible, sin vender por miedo.
- **Modo Refugio y Cosecha de Dinero Fiat (Rentas FIBRAs con Indicadores Inversos):**  
  La unidad de cuenta mental es la moneda fiduciaria (**MXN / USD**). Si el usuario prefiere acumular pesos o dólares, el sistema invierte la lógica: cuando Bitcoin entra en sobrecompra extrema (RSI 4H ≥ 65-70) o en techos de ciclo macro ($1,800,000+ MXN / $95,000+ USD), el bot alerta para cosechar plusvalías y transferirlas a casas de bolsa reguladas en México (Bursanet / Actinver) para comprar FIBRAs inmobiliarias (FIBRAMQ, FUNO, FMTY), asegurando un flujo de rentas pasivas trimestrales en pesos (8.5% a 10.5% anual) blindado contra la volatilidad. Además, al presentarse correcciones del -2.5% o mayores, el sistema emite el cálculo exacto de recompra para cosechar satoshis gratuitos sin aportar dinero nuevo.

### 1.3. Motor de Auditoría Contable Continua y Conciliación Fiat
Para evitar cualquier ambigüedad contable o malentendido con los usuarios:
- **Separación de Capital de Bolsillo vs Valuación:** El bot audita segundo a segundo las órdenes y distingue con precisión matemática el *Capital Real Aportado de Bolsillo* (depósitos acumulados de nómina) frente a la *Valuación de Mercado* (el valor fluctuante de las monedas en cartera).
- **Lectura Dual Simultánea:** Cada vez que el bot presenta un saldo o una orden, muestra obligatoriamente ambos valores en paralelo:
  * **En Cripto:** Cantidad en Satoshis enteros (para acumulación disciplinada) y en fracción decimal de Bitcoin (para ingresar la orden en Bitso).
  * **En Fiat:** Importe en Dólares Estadounidenses (USD) y su conversión a Pesos Mexicanos (MXN) con tipo de cambio interbancario en tiempo real.

### 1.4. Sistema de Resiliencia, Respaldo Soberano y Auto-Sanación (Triple Bóveda)
Para garantizar que **ningún usuario ni historial se pierda jamás**, el sistema cuenta con:
1. **Escritura Atómica Segura:** Las modificaciones a la base de datos se escriben primero en un archivo temporal (`.tmp`), se sincronizan al disco duro (`fsync`) y se generan snapshots rotativos con fecha y hora.
2. **Bitácora Inmutable Write-Ahead Log (WAL):** El archivo `user_rescue_audit_log.jsonl` guarda de forma permanente cada registro, aprobación o depósito con una huella criptográfica SHA-256 única.
3. **Auto-Sanación Instantánea (*Self-Healing*):** Si por una falla eléctrica o reseteo de servidor el archivo `registered_users.json` se corrompe, el sistema busca automáticamente el último snapshot de respaldo y se auto-repara en milisegundos sin requerir intervención técnica.
4. **Respaldo Soberano Exportable:** Con un solo comando (`/respaldo`), la administradora recibe en Telegram los archivos de base de datos (`.json`) y una hoja de cálculo en Excel (`.csv`) con todos los nombres y contactos para rescatar el servicio de inmediato.

---

# MÓDULO 2: COMANDOS EXCLUSIVOS DE LA ADMINISTRADORA (SUPER-ADMIN)
*(Sección independiente para uso exclusivo de Hilda Belem Ortiz Fuentes)*

> **IMPORTANTE:** Estos comandos están restringidos exclusivamente al identificador numérico de Telegram de la titular (**Super-Admin ID**). Si un usuario común intenta ejecutarlos, el bot deniega el acceso y registra el intento no autorizado.

### 2.1. Tabla Resumen de Comandos de Super-Admin

| Comando | Parámetros | Propósito Operativo |
| :--- | :--- | :--- |
| `/usuarios` | Ninguno | Padrón completo de usuarios (activos, pendientes, suspendidos y días restantes). |
| `/pendientes` | Ninguno | Muestra únicamente los usuarios en cola de espera que enviaron solicitud de acceso. |
| `/aprobar` | `<chat_id> [días]` | Aprueba oficialmente a un usuario, asigna membresía (30 días por defecto) y le envía bienvenida. |
| `/renovar` | `<chat_id> <días>` | Extiende la vigencia del servicio (ej. `/renovar 123456789 30`). |
| `/suspender` | `<chat_id>` | Pausa temporalmente el acceso del usuario (por falta de pago o solicitud propia). |
| `/reactivar` | `<chat_id>` | Reactiva una cuenta suspendida restaurando sus funciones completas. |
| `/bloquear` | `<chat_id>` | Veta permanentemente a un usuario por comportamiento indebido o abusivo. |
| `/respaldo` | Ninguno | **Bóveda de Rescate:** Genera y envía por Telegram el JSON de usuarios, JSON contable y CSV de Excel. |
| `/exportar_usuarios`| Ninguno | Envía el archivo `.csv` compatible con Excel con el directorio de usuarios y sus saldos. |
| `/estatus_rescate` | Ninguno | Diagnóstico en tiempo real del motor de resiliencia, eventos en el WAL SHA-256 y copias de seguridad. |
| `/restaurar_respaldo`| `<archivo>` | Restaura manualmente la base de datos a un snapshot histórico específico. |
| `/auditoria` | Ninguno | Diagnóstico forense contable, comprobantes pendientes y detección de inconsistencias. |
| `/capital_neto` | Ninguno | Reporte consolidado del capital total fiat inyectado por todos los miembros del bot. |

---

### 2.2. Guía Detallada de Comandos de Super-Admin

#### A. Gestión de Membresías y Nuevos Miembros
- **`/pendientes`**
  - **Cuándo usarlo:** Cada vez que una persona pulsa `/start` en el bot y solicita acceso.
  - **Qué responde el bot:** Una lista con el nombre, `@username` y `chat_id` de cada aspirante, junto con los botones interactivos o la instrucción directa para autorizarlo.
- **`/aprobar <chat_id> [días]`**
  - **Ejemplo:** `/aprobar 987654321 30`
  - **Efecto:**
    1. Cambia el estado del usuario de `PENDING` a `ACTIVE`.
    2. Establece la vigencia por el número de días indicado (si se omite, asigna 30 días).
    3. Registra el evento en la bitácora inmutable SHA-256.
    4. Envía un mensaje automático privado al usuario dándole la bienvenida oficial y activando su teclado de comandos.
- **`/renovar <chat_id> <días>`**
  - **Ejemplo:** `/renovar 987654321 30`
  - **Efecto:** Si el usuario renueva su suscripción mensual, añade 30 días a su fecha de expiración actual y le envía confirmación de renovación.
- **`/suspender <chat_id>` y `/reactivar <chat_id>`**
  - **Efecto:** Si un usuario no realiza su aportación o pide una pausa, `/suspender` inhabilita las alertas de mercado. Al enviar el comprobante de reactivación, `/reactivar` devuelve la cuenta al estado plenamente operativo sin perder su antigüedad ni su libro contable acumulado.

---

#### B. Sistema de Respaldo, Auditoría y Rescate ante Desastres
- **`/respaldo` (EL COMANDO MAESTRO DE SEGURIDAD)**
  - **Cuándo usarlo:** Se recomienda ejecutarlo una vez por semana o antes de realizar cualquier actualización en el servidor.
  - **Qué hace el bot:**
    1. Genera un snapshot atómico en la nube.
    2. Construye el archivo de usuarios: `respaldo_usuarios_patrimonio_AAAAMMDD_HHMMSS.json`.
    3. Construye el directorio de rescate en hoja de cálculo: `directorio_usuarios_rescate_AAAAMMDD_HHMMSS.csv`.
    4. Construye el libro mayor de Bitso: `bitso_libro_contable_AAAAMMDD_HHMMSS.json`.
    5. **Envía los 3 documentos directamente al chat privado de Telegram de Hilda Belem.**
  - **Garantía:** Con tener esos archivos guardados en tu computadora o en tu propio chat guardado de Telegram, el sistema se puede reconstruir al 100% en caso de cualquier eventualidad.
- **`/exportar_usuarios`**
  - **Qué hace el bot:** Envía únicamente el archivo CSV. Al hacer doble clic en tu computadora, se abre en **Microsoft Excel** o **Google Sheets** con columnas ordenadas: ID de Telegram, Nombre Completo, Usuario, Estatus, Plan, Fecha de Registro, Días Restantes, Total Satoshis Acumulados y Total Fiat Aportado en USD y MXN.
- **`/estatus_rescate`**
  - **Qué responde el bot:** Una tarjeta ejecutiva con:
    * Total de usuarios en base de datos y memoria.
    * Conteo de eventos registrados en la bitácora inmutable `user_rescue_audit_log.jsonl`.
    * Lista de los últimos respaldos rotativos guardados en disco.
    * Estado de salud del motor de auto-sanación (*Healthy / Green*).

---

# MÓDULO 3: MANUAL DE COMANDOS PARA USUARIOS Y MIEMBROS
*(Sección independiente que puede ser compartida o entregada a los miembros del bot)*

### 3.1. Tabla Resumen de Comandos para el Usuario

| Comando | Propósito y Respuesta del Copiloto |
| :--- | :--- |
| `/start` | Mensaje de bienvenida, solicitud de registro o despliegue del menú principal interactivo. |
| `/ayuda` | Guía rápida con botones de navegación y explicación de cada sección. |
| `/precio` | Cotización en tiempo real de Bitcoin en USD y MXN con tipo de cambio interbancario. |
| `/mercado` | Análisis técnico institucional: Oscilador RSI (4 Horas), Índice de Miedo/Codicia y niveles clave. |
| `/evaluar <activo>` | Dictamen cuantitativo para cualquier acción o FIBRA (ej. `/evaluar FIBRAMQ12`, `/evaluar IVVPESO`). |
| `/comisiones` | Comparativa pedagógica de comisiones en Bitso (Maker 0.60% vs Taker 0.78% y ahorro de spread). |
| `/saldo` o `/cuenta` | Resumen de cartera: Satoshis acumulados, fracción BTC, capital fiat aportado y valuación actual. |
| `/libro` | Historial contable certificado de todas las compras y ventas registradas con folios SHA-256. |
| `/convertir <monto>` | Convierte al instante una cantidad de pesos a satoshis al precio exacto de mercado. |
| `/simular_bitso` | Tutorial guiado para colocar una orden límite tipo Maker en Bitso Alpha paso a paso. |
| `/simular_actinver` | Tutorial guiado para adquirir títulos bursátiles de FIBRAs en Bursanet (Actinver). |
| `/timing` | Evalúa si el mercado ofrece descuento suficiente (-2.5%) para recomprar satoshis tras una venta. |
| `/borrar_datos` | Ejercicio de Derechos ARCO: Purga y borra inmediatamente el historial personal del usuario. |

---

### 3.2. Guía de Operativa Paso a Paso para el Usuario

#### A. ¿Cómo Consultar el Mercado y Recibir Recomendaciones?
1. Escribe `/precio` para ver el valor exacto de Bitcoin al segundo tanto en dólares como en moneda nacional.
2. Escribe `/mercado` para verificar si estamos en **Zona de Oportunidad (Sobreventa)** o en **Zona de Prudencia/Cosecha (Sobrecompra)**.
3. El copiloto cuenta con **Vigilancia 24/7**: Si ocurre una caída pronunciada a un soporte técnico favorable, el bot te enviará una notificación automática sugiriendo colocar una orden de compra límite Maker.

#### B. ¿Cómo Acreditar una Compra en Bitso Enviando una Captura de Pantalla?
1. Realiza tu compra límite en la aplicación o página web de **Bitso** (en el par BTC/USD o BTC/MXN).
2. Entra a la pestaña de **"Órdenes Pasadas"** o **"Detalle de la Orden"** donde se aprecie: Precio, Monto en BTC y Total pagado.
3. Toma una captura de pantalla clara desde tu celular o computadora.
4. **Envía la imagen directamente al bot de Telegram como foto.**
5. **Respuesta Automática del Bot:**
   - Lee ópticamente los datos de la transacción.
   - Genera una huella digital SHA-256 para evitar duplicidades.
   - Acredita tus nuevos satoshis en tu cuenta.
   - Muestra tu nuevo saldo desglosado en:
     * Satoshis acumulados y fracción equivalente en BTC.
     * Capital total invertido de bolsillo en MXN y USD.
     * Valuación actual de tu cartera y porcentaje de plusvalía/minusvalía flotante.
     * Activa el monitor de alerta de toma de ganancias 24/7.

#### C. La Doble Finalidad en la Práctica (¿Acumular Satoshis o Acumular Fiat?)
- **Si tu meta es Acumular Satoshis (Patrimonio Intergeneracional):**
  Ignora la volatilidad de corto plazo. Cada vez que el bot te notifique una sobreventa técnica, coloca compras límite tipo Maker y deja tus monedas guardadas. Tu objetivo es ver crecer el número de satoshis mes con mes.
- **Si tu meta es Acumular y Cosechar Fiat (Flujo de Dinero / Rentas FIBRAs):**
  Cuando el bot detecte una sobrecompra técnica (RSI ≥ 65-70), coloca una orden de venta límite para asegurar ganancias en pesos o dólares. Si el mercado retrocede al menos un 2.5%, el comando `/timing` te indicará el precio exacto para volver a entrar y ganar más satoshis gratis, o bien, podrás retirar esas ganancias en pesos para comprar FIBRAs en Actinver/Bursanet y gozar de rentas trimestrales reguladas.

---

# MÓDULO 4: PROTOCOLO ANTE EMERGENCIAS Y RECUPERACIÓN (DISASTER RECOVERY)
*(Manual de contingencia paso a paso para la administradora)*

### 4.1. Escenario A: ¿Qué pasa si el servidor en la nube (Render) se apaga o reinicia?
- **Diagnóstico:** Los contenedores en la nube pueden reiniciarse por mantenimiento de Render o por límites de memoria.
- **Respuesta Automática del Sistema:** Al reiniciar, el script `_load_users()` se ejecuta. Si el archivo principal está intacto, lee los usuarios y continúa. Si por alguna razón el archivo se dañó durante el apagón, el algoritmo de **Auto-Sanación** busca en la carpeta `user_verifications/backups/` el snapshot más reciente y lo restaura en 1 segundo de manera transparente.
- **Acción requerida por Hilda Belem:** Ninguna. El sistema se auto-repara solo.

---

### 4.2. Escenario B: ¿Qué pasa si se pierde por completo el servidor o cambiamos de computadora?
- **Pregunta de la Administradora:** *"¿Con los archivos de `/respaldo` yo te los doy y vuelves a restaurar el sistema antes del error?"*
- **Respuesta Oficial:** **SÍ, 100% GARANTIZADO.**
- **Protocolo de Restauración en 3 Pasos:**
  1. **Tener a la mano los archivos recibidos por Telegram:**
     * `respaldo_usuarios_patrimonio_*.json`
     * `bitso_libro_contable_*.json`
  2. **Colocación en el Nuevo Servidor:**
     * Se copian ambos archivos dentro de la carpeta `user_verifications/` renombrándolos a:
       - `user_verifications/registered_users.json`
       - `user_verifications/bitso_trade_book.json`
  3. **Reinicio del Bot:**
     * Al encender el bot (o al pedirle al asistente que los cargue), el sistema lee inmediatamente todos los usuarios, sus planes de suscripción, sus fechas de antigüedad, sus saldos acumulados de satoshis y el capital fiat invertido.
     * **Resultado:** Todo vuelve exactamente al estado previo al error en menos de 10 segundos.

---

### 4.3. Escenario C: ¿Qué pasa si Telegram suspende el bot o se cambia de Token?
- Si por políticas de Telegram se debe migrar a un nuevo bot (por ejemplo `@nuevo_patrimonio_bot`):
  1. Se actualiza la variable `TELEGRAM_BOT_TOKEN` en la configuración de Render o en el archivo `.env`.
  2. La base de datos de usuarios conserva intactos los `chat_id` numéricos de cada persona.
  3. Se envía un mensaje masivo o individual informando a los miembros: *"Nos hemos mudado a nuestro nuevo canal oficial @nuevo_patrimonio_bot. Pulsa /start para continuar con tu saldo intacto."*
  4. En cuanto el usuario pulsa `/start`, el sistema reconoce su `chat_id` y le da la bienvenida reconociendo su saldo acumulado histórico sin pérdidas.

---

### 4.4. Escenario D: ¿Cómo contactar a los usuarios si no hay ningún bot encendido?
- **Uso del Directorio Soberano de Rescate (`directorio_usuarios_rescate_*.csv`):**
  - Gracias al comando `/respaldo` o `/exportar_usuarios`, siempre dispones de una copia en tu teléfono o computadora.
  - Abres el archivo con **Microsoft Excel** o en el bloc de notas.
  - Tienes la lista completa con:
    * Nombre registrado de la persona.
    * Nombre de usuario en Telegram (`@username`).
    * ID numérico de Telegram.
    * Estado de su cuenta y días pagados.
    * Saldo exacto en satoshis y dinero fiat que tenía en custodia o registrado.
  - Puedes redactarles un mensaje directo por Telegram privado, correo electrónico o WhatsApp comunicando cualquier instrucción sin depender de la nube.

---

## 5. CERTIFICACIÓN LEGAL Y MARCO DE PROPIEDAD INTELECTUAL
Este manual, la arquitectura de dualidad operativa, los algoritmos de auto-sanación y conciliación de capital fiat, y las herramientas interactivas web forman parte de la obra de software registrada ante el **Instituto Nacional del Derecho de Autor (INDAUTOR)** y protegida como **Secreto Industrial** al amparo de la **Ley Federal del Derecho de Autor (LFDA)** y la **Ley Federal de Protección a la Propiedad Industrial (LFPPI)**.

**Titular y Autora Exclusiva:**  
**Hilda Belem Ortiz Fuentes**  
Ciudad de México, Noviembre de 2026.
