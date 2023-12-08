CREATE OR REPLACE FUNCTION cek_rating()
RETURNs trigger AS
$$
BEGIN
    IF(NEW.rating > 5 OR NEW.rating < 0) THEN
        RAISE EXCEPTION 'Rating hanya boleh antara 0 dan 5';
    END IF;
    RETURN NEW;
END;
$$
language plpgsql;

CREATE TRIGGER trigger_cek_rating
BEFORE INSERT ON reviews
FOR EACH ROW EXECUTE PROCEDURE cek_rating();

CREATE OR REPLACE FUNCTION avg_rating(nama_hotel varchar(50), cabang_hotel varchar(50))
RETURNs float AS
$$
DECLARE
    rata_rata float;
BEGIN
    SELECT avg(rating) into rata_rata
    from reviews
    where hotel_name = nama_hotel and hotel_branch = cabang_hotel;
    RETURN rata_rata;
END;
$$
language plpgsql;