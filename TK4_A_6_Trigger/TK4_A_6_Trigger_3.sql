CREATE OR REPLACE FUNCTION nama_function()
RETURNs trigger AS
$$
DECLARE
    nama_var1 type_var1;
    nama_var2 type_var2;
BEGIN
    -- IF() THEN
    --     RAISE EXCEPTION '';
    -- END IF;
    -- RETURN NEW;
END;
$$
language plpgsql;

CREATE TRIGGER nama_trigger
AFTER INSERT ON nama_tabel
FOR EACH ROW EXECUTE PROCEDURE nama_function();