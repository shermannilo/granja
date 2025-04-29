Este repositorio ha sido creado con el objetivo de demostrar mis habilidades utilizando Python.

Aquí se puede observar el uso de APIs, comandos ADB, manejo de archivos en formato JSON y variables de entorno mediante archivos .env (no incluidos por motivos de seguridad).

Cabe mencionar que varias partes del código contienen prácticas intencionalmente mejorables: por ejemplo, existen líneas de comandos repetidas que podrían haberse encapsulado en funciones, y algunas funcionalidades no están completamente automatizadas, sino estructuradas de manera esquemática.

También se mezclan comentarios y nombres de variables en inglés y español, a propósito, para que quien estudie el repositorio pueda notar estas inconsistencias y corregirlas.

El propósito adicional de este repositorio es servir como material de práctica para personas que están comenzando a programar en Python. He procurado mantener el código sencillo, evitando la abstracción excesiva, para que los principiantes puedan identificar errores comunes y mejorarlos por sí mismos.

Algunas secciones del código podrían estar ubicadas en lugares no ideales dentro de la estructura del proyecto, también de forma intencional, para fomentar el análisis crítico y la reorganización del mismo.

En resumen, este proyecto no solo demuestra mis habilidades, sino que también está pensado como una herramienta de aprendizaje para quienes desean mejorar sus buenas prácticas de programación en Python.

                                                      ######### Ahora hablemos del codigo que necesitas para probarlo #########

                                                      Necesitas descargar un emulador como Andoid studio y crear un nuevo device en el cual recomiendo 
                                                      un pixel 5 : Como hacerlo ? Facil, Abre Andoid studio , click on  More Action , on virtual device manager 
                                                      en la parte superior izquierda en el signo de mas busca pixel 5 , go next , haz click en api , en el final pulsa
                                                      api 30 "R"... luego en  system image selecciona la opcion con la estrella a su lado , antes de seguir en la 
                                                      parte superior dice additional setting has click alli , luego haz scroll down , para probar puedes dejar los 
                                                      cpu cores como estan y la ram , pero puedes bajarlos hast 1 cada uno y funciona sin problemas , paso final 
                                                      en preferred ABi pulsa ahi y selecciona armeabi-v7a luego finaliza .
¡Bien hecho! Ya tienes un dispositivo Android emulado. Para verificar que todo funciona correctamente, abre PowerShell con el emulador aún activo (ni se te ocurra cerrarlo… ¡sería un desastre! 😅).

Escribe el siguiente comando:


adb devices
Deberías ver algo como:


List of devices attached
emulator-5554   device

Si te aparece eso: perfecto, todo marcha sobre ruedas.
Si no aparece… bueno, YouTube será tu nuevo mejor amigo.Na no creas todavia no  😂

🧠 ¿El problema? ADB no está en tu PATH
Si no se reconoce el comando adb, es probable que no hayas agregado ADB al PATH del sistema. No te voy a dar la respuesta completa (¡tampoco puedo hacer todo el trabajo por ti!), pero aquí va la pista:

Abre Android Studio.

Haz clic en More Actions y luego en SDK Manager.

Dentro verás la ruta donde está instalado el SDK.

Copia esa ruta, navega a ella con tu explorador de archivos.

Entra a la carpeta platform-tools.

Copia esa ruta y agrégala al PATH de tu sistema.

👉 No sabes cómo agregarlo al PATH? YouTube lo explica mejor que mil palabras. ¡Busca un video y listo!

🎯 Prueba final
Una vez hecho eso, abre PowerShell otra vez y ejecuta:

adb devices

Ahora sí debería aparecer emulator-5554.
¿Aún no sale? Entonces te toca investigar un poco más, soldado. 💻🪖
¡Ánimo, que ya casi llegas!



⚠️ Sobre los errores al abrir el proyecto
Cuando abras este proyecto en VS Code (o cualquier editor que uses), es posible que te aparezcan errores relacionados con algunos import.
No te preocupes, no es el apocalipsis: simplemente abre la terminal y ejecuta:

pip install <nombre_del_paquete>
Y listo, problema resuelto. 💥

🧠 Sobre el código (sí, el código de verdad)
Antes de ejecutar el proyecto, asegúrate de modificar los paths de instalación de las APKs en el script.
También te recomiendo borrar todo menos la carpeta de iconos: esto es para que veas cómo el código reconstruye automáticamente lo que necesita. Te ayuda a entender cómo funciona el proceso desde cero. 🧱

📲 Sobre las APKs
El repositorio no incluye las APKs (por razones legales y de peso), así que debes descargarlas manualmente desde tu navegador.
Luego, coloca el path correcto donde se encuentren. Pero atención: aunque las APKs se instalen correctamente, Instagram y Facebook no se abrirán automáticamente. ❌📱

Eso te toca investigarlo a ti. Pero no te dejo sin una pista:
👉 armeabi-v7a

¿Qué hacer con eso? No te lo voy a decir todo… ¡sorpréndeme! 😉

👨‍🍳 Bon appétit… o mejor dicho: ¡Bon code!
                        #### Dudas comunicate , ofertas de trabajo comunicate , lo que necesites comunicate .  #########

                  ####   The repository is not also in English because there is always the option to translate it.   ####
###################    _______________________________________________________________________________________________________. ##################

