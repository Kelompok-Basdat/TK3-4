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
BEFORE INSERT ON reservation_shuttleservice
FOR EACH ROW EXECUTE PROCEDURE cek_add_reservasi();

CREATE OR REPLACE FUNCTION cek_update_status()
RETURNs trigger AS
$$
DECLARE
    last_status varchar(50);
    new_status varchar(50);
BEGIN
    select status into last_status
    from reservation_status, reservation_status_history
    where rid = NEW.rid and rsid = id
    order by datetime desc
    limit 1;
    
    select status into new_status
    from reservation_status
    where NEW.rsid = id;

    IF(last_status != 'Menunggu Konfirmasi Pihak Hotel') THEN
        RAISE EXCEPTION 'Hanya dapat mengubah status dari ''Menunggu Konfirmasi Pihak Hotel''';
        IF(new_status not in ('Ditolak oleh Hotel','Terkonfirmasi oleh Hotel','Dibatalkan Customer')) THEN
            RAISE EXCEPTION 'Hanya dapat mengubah status ke ''Ditolak oleh Hotel'' atau ''Terkonfirmasi oleh Hotel''';
        END IF;
    END IF;
    RETURN NEW;
END;
$$
language plpgsql;

CREATE TRIGGER trigger_update_status
AFTER INSERT OR UPDATE ON reservation_status_history
FOR EACH ROW EXECUTE PROCEDURE cek_update_status();