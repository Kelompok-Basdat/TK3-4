CREATE OR REPLACE FUNCTION cek_add_fasilitas()
RETURNs trigger AS
$$
BEGIN
    IF(NEW.facility_name !~ '^[A-Za-z ]+$') THEN
        RAISE EXCEPTION 'Nama fasilitas hanya boleh terdiri dari huruf!';
    END IF;
    RETURN NEW;
END;
$$
language plpgsql;

CREATE TRIGGER trigger_cek_add_fasilitas
BEFORE INSERT OR UPDATE ON hotel_facilities
FOR EACH ROW EXECUTE PROCEDURE cek_add_fasilitas();

CREATE OR REPLACE FUNCTION check_duplicate_facilities()
RETURNS TRIGGER AS $$
BEGIN
    IF TG_OP = 'UPDATE' THEN
        IF OLD.facility_name = NEW.facility_name THEN
        RAISE EXCEPTION 'Nama fasilitas baru harus berbeda dengan yang lama!';
        END IF;
    ELSIF EXISTS (SELECT 1 FROM hotel_facilities
                WHERE hotel_name = NEW.hotel_name AND hotel_branch = NEW.hotel_branch AND facility_name = NEW.facility_name) THEN
        RAISE EXCEPTION 'Fasilitas sudah terdaftar. Tidak boleh ada nama fasilitas yang sama';
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trg_prevent_duplicate_facilities
BEFORE INSERT OR UPDATE ON hotel_facilities
FOR EACH ROW EXECUTE FUNCTION check_duplicate_facilities();