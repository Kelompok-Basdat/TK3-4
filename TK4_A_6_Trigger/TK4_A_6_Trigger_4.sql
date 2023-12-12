CREATE OR REPLACE FUNCTION cek_add_reservasi_kamar()
RETURNs trigger AS
$$
BEGIN
    IF(EXISTS(select * from reservation_room where rhotelname = NEW.rhotelname AND rhotelbranch = NEW.rhotelbranch 
                AND  rnum = NEW.rnum AND datetime = NEW.datetime AND isactive = true)) THEN
        RAISE EXCEPTION 'Mohon maaf, kamar sedang dalam masa reservasi.';
    END IF;
    RETURN NEW;
END;
$$
language plpgsql;

CREATE TRIGGER trigger_cek_add_reservasi_kamar
BEFORE INSERT ON reservation_room
FOR EACH ROW EXECUTE PROCEDURE cek_add_reservasi_kamar();

CREATE OR REPLACE FUNCTION cek_batal_status()
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

    IF(new_status = 'Dibatalkan Customer') THEN
        IF(last_status != 'Menunggu Konfirmasi Pihak Hotel') THEN
            RAISE EXCEPTION 'Hanya dapat membatalkan reservasi dengan status ''Menunggu Konfirmasi Pihak Hotel''';
        END IF;
    END IF;
    RETURN NEW;
END;
$$
language plpgsql;

CREATE TRIGGER trigger_batal_status
AFTER INSERT ON reservation_status_history
FOR EACH ROW EXECUTE PROCEDURE cek_batal_status();