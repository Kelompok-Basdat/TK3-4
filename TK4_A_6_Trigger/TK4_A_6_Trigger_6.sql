CREATE OR REPLACE FUNCTION cek_add_complaint()
RETURNs trigger AS
$$
BEGIN
    IF(NOT (select isactive from reservation_room where rsv_id = NEW.rv_id)) THEN
        RAISE EXCEPTION 'Hanya bisa membuat komplain jika dalam masa reservasi.';
    ELSIF((NEW.complaint is null) OR (NEW.complaint = '')) THEN
        RAISE EXCEPTION 'Kolom deskripsi komplain wajib diisi.';
    END IF;
    RETURN NEW;
END;
$$
language plpgsql;

CREATE TRIGGER trigger_add_complaint
BEFORE INSERT ON complaints
FOR EACH ROW EXECUTE PROCEDURE cek_add_complaint();