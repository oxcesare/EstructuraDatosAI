/**
 * SIMULADOR DE SERVIDOR (server_mock.js)
 * Simula una base de datos y un endpoint que soporta Long Polling.
 */

const ServerMock = (() => {
    // Estado inicial "en la base de datos"
    let estadoHabitaciones = {
        disponibles: 6,
        ocupadas: 4,
        limpieza: 2,
        mantenimiento: 2,
        lastUpdate: Date.now()
    };

    // Simulador de cambios aleatorios cada 5-8 segundos
    // Esto simula que "otro usuario" o un proceso externo cambia los datos
    setInterval(() => {
        if (estadoHabitaciones.disponibles > 0) {
            estadoHabitaciones.disponibles--;
            estadoHabitaciones.ocupadas++;
            estadoHabitaciones.lastUpdate = Date.now();
            console.log("--- SERVIDOR: Se ha ocupado una habitación (Cambio en BD) ---");
        }
    }, 7000);

    /**
     * Simulación de un Endpoint de Long Polling
     * @param {number} clientTimestamp - El timestamp que el cliente ya tiene
     */
    const checkUpdates = (clientTimestamp) => {
        return new Promise((resolve) => {
            const maxWaitTime = 20000; // 20 segundos máximo de espera (timeout)
            const checkInterval = 500; // Revisar cambios cada 500ms
            let timeWaited = 0;

            const poll = setInterval(() => {
                // ¿Hay datos nuevos desde la última vez que el cliente preguntó?
                if (estadoHabitaciones.lastUpdate > clientTimestamp) {
                    clearInterval(poll);
                    resolve({
                        status: 'success',
                        data: { ...estadoHabitaciones }
                    });
                } 
                // Si llegamos al timeout, respondemos con "no hay cambios"
                else if (timeWaited >= maxWaitTime) {
                    clearInterval(poll);
                    resolve({ status: 'timeout' });
                }

                timeWaited += checkInterval;
            }, checkInterval);
        });
    };

    return { checkUpdates };
})();