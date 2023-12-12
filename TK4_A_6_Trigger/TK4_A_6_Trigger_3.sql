CREATE OR REPLACE FUNCTION cek_add_kamar()
RETURNs trigger AS
$$
BEGIN
    IF(NEW.floor <= 0) THEN
        RAISE EXCEPTION 'Nomor lantai harus bilangan positif di atas 0!';
    END IF;
    IF(NEW.price <= 0) THEN
        RAISE EXCEPTION 'Harga kamar harus bilangan positif di atas 0!';
    END IF;
    RETURN NEW;
END;
$$
language plpgsql;

CREATE TRIGGER trigger_cek_add_kamar
BEFORE INSERT ON room
FOR EACH ROW EXECUTE PROCEDURE cek_add_kamar();

CREATE OR REPLACE FUNCTION cek_del_kamar()
RETURNs trigger AS
$$
BEGIN
    IF(EXISTS(select * from reservation_room where rnum = OLD.number and isactive = true)) THEN
        RAISE EXCEPTION 'Tidak dapat menghapus kamar tersebut karena masih terdaftar dalam reservasi aktif!';
    END IF;
    RETURN NEW;
END;
$$
language plpgsql;