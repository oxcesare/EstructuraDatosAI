/**
 * CLIENTE LONG POLLING (long_polling_client.js)
 */

let lastKnownTimestamp = Date.now();

async function iniciarLongPolling() {
    console.log("Cliente: Conectando al servidor para esperar cambios...");

    try {
        // Simulamos la petición AJAX/Fetch al servidor
        // En un escenario real sería: fetch('/api/updates?since=' + lastKnownTimestamp)
        const response = await ServerMock.checkUpdates(lastKnownTimestamp);

        if (response.status === 'success') {
            console.log("Cliente: ¡Datos recibidos!", response.data);
            
            // Actualizar la interfaz
            actualizarDashboard(response.data);
            
            // Actualizar nuestro timestamp para la siguiente petición
            lastKnownTimestamp = response.data.lastUpdate;
        } else {
            console.log("Cliente: Timeout alcanzado sin cambios. Reintentando...");
        }
    } catch (error) {
        console.error("Cliente: Error en la conexión", error);
    } finally {
        // LA CLAVE DEL LONG POLLING:
        // En cuanto termina una petición (bien o mal), lanzamos la siguiente.
        // Ponemos un pequeño delay de 500ms solo para no saturar el navegador en el dummy.
        setTimeout(iniciarLongPolling, 500);
    }
}

function actualizarDashboard(data) {
    // Animación simple de cambio
    const updateElement = (id, value) => {
        const el = document.getElementById(id);
        if (el && el.innerText != value) {
            el.style.transition = "color 0.3s";
            el.style.color = "#3b82f6"; // Color azul temporal para notar el cambio
            el.innerText = value;
            setTimeout(() => el.style.color = "", 1000);
        }
    };

    updateElement('count-disponibles', data.disponibles);
    updateElement('count-ocupadas', data.ocupadas);
    updateElement('count-limpieza', data.limpieza);
    updateElement('count-mantenimiento', data.mantenimiento);
}

// Iniciar el proceso al cargar la página
window.onload = iniciarLongPolling;