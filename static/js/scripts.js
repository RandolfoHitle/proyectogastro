$(document).ready(function () {
    // Modal logic
    function openModal(content) {
        $('#modal-body').html(content);
        $('#modal').removeClass('hidden');
    }

    function closeModal() {
        $('#modal').addClass('hidden');
    }

    $('#propuestas-btn').click(function () {
        // Simulate check if user is logged in or not
        let loggedIn = false; // Cambiar esto según tu lógica de login

        if (!loggedIn) {
            openModal('<p>Necesitas registrarte para poder realizar propuestas.</p><button class="close-btn">Confirmar</button>');
        } else {
            openModal('<form><label>Nombre de la receta</label><input type="text" name="nombre_receta"><button>Enviar Propuesta</button></form>');
        }
    });

    $('#register-btn').click(function () {
        openModal(`
            <h2>Registro</h2>
            <form>
                <label>Nombre de Usuario</label>
                <input type="text" name="nombre_usuario">
                <label>Correo</label>
                <input type="email" name="correo">
                <label>Contraseña</label>
                <input type="password" name="contrasena">
                <label>Confirmar Contraseña</label>
                <input type="password" name="confirmar_contrasena">
                <button type="submit">Registrarse</button>
            </form>
        `);
    });

    $('#login-btn').click(function () {
        openModal(`
            <h2>Login</h2>
            <form>
                <label>Nombre o correo</label>
                <input type="text" name="nombre_correo">
                <label>Contraseña</label>
                <input type="password" name="contrasena">
                <button type="submit">Entrar</button>
            </form>
        `);
    });

    $('.close-btn').click(function () {
        closeModal();
    });
});
