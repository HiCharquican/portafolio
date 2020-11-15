CREATE OR REPLACE PROCEDURE sp_crear_editar_usuario(
    v_id NUMBER,
    v_username STRING,
    v_password STRING,
    v_nombre STRING,
    v_apellido STRING,
    v_email STRING,
    v_telefono NUMBER,
    v_direccion STRING,
    v_region STRING,
    v_rol_usuario NUMBER,
    v_is_active NUMBER,
    v_is_staff NUMBER,
    v_is_superuser NUMBER
)
IS
BEGIN
    IF v_id = -1 THEN
        INSERT INTO portafolio_usuario (username, password, nombre, apellido, email, telefono,direccion,region,rol_usuario_id, is_active, is_staff, is_superuser, date_joined)
        VALUES (v_username, v_password,v_nombre,v_apellido,v_email,v_telefono,v_direccion,v_region,NULL, v_is_active, v_is_staff, v_is_superuser, sysdate);
    ELSE
        UPDATE portafolio_usuario
        SET 
            username = v_username,
            password = v_password,
            nombre = v_nombre, 
            apellido = v_apellido, 
            email = v_email, 
            telefono = v_telefono,
            direccion = v_direccion,
            region = v_region,
            is_active = v_is_active,
            is_staff = v_is_staff,
            is_superuser = v_is_superuser
        WHERE id = v_id;
    END IF;
    
    COMMIT;
END;

CREATE OR REPLACE PROCEDURE sp_crear_editar_rol(
    v_id NUMBER,
    v_name STRING
)
IS
BEGIN
    IF v_id = -1 THEN
        INSERT INTO auth_group (name)
        VALUES (v_name);
    ELSE
        UPDATE auth_group
        SET 
            name = v_name
        WHERE id = v_id;
    END IF;
    
    COMMIT;
END;
