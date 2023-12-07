CREATE OR REPLACE FUNCTION cek_add_reservasi()
RETURNs trigger AS
$$
BEGIN
    IF(NEW.rsv_id in (SELECT rsv_id from reservation_room where isactive = false)) THEN
        RAISE EXCEPTION 'Kamu harus memesan kamar dahulu sebelum memesan shuttle service!';
    END IF;
    RETURN NEW;
END;
$$
language plpgsql;

CREATE TRIGGER trigger_cek_add_reservasi
AFTER INSERT ON reservation_shuttleservice
FOR EACH ROW EXECUTE PROCEDURE cek_add_reservasi();

CREATE OR REPLACE FUNCTION cek_update_status()
RETURNs trigger AS
$$
BEGIN
    IF(NEW.rsv_id in (SELECT rsv_id from reservation_room where isactive = false)) THEN
        RAISE EXCEPTION 'Kamu harus memesan kamar dahulu sebelum memesan shuttle service!';
    END IF;
    RETURN NEW;
END;
$$
language plpgsql;