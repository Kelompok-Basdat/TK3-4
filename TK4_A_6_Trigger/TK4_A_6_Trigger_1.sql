CREATE OR REPLACE FUNCTION cek_password()
RETURNs trigger AS
$$
BEGIN
    IF(NOT(NEW.password ~ '[A-Za-z]' AND NEW.password ~ '[0-9]')) THEN
        RAISE EXCEPTION 'Password harus terdiri dari kombinasi huruf dan angka!';
    END IF;
    RETURN NEW;
END;
$$
language plpgsql;

CREATE TRIGGER trigger_cek_password
BEFORE INSERT ON sistel.user
FOR EACH ROW EXECUTE PROCEDURE cek_password();