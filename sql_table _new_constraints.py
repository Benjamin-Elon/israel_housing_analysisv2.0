import sqlite3

conn = sqlite3.connect('yad2db.sqlite')
cur = conn.cursor()

cur.execute("""PRAGMA foreign_keys = 0;

CREATE TABLE temp_table AS SELECT * FROM Listings;""")

rows = cur.fetchall()

cur.execute("""DROP TABLE Listings;

CREATE TABLE Listings (
    top_area_name         TEXT,
    top_area_id           INTEGER,
    area_name             TEXT,
    area_id               INTEGER,
    city_name             TEXT,
    city_id               INTEGER,
    neighborhood_name     TEXT,
    neighborhood_id       INTEGER,
    street_name           TEXT,
    street_id             INTEGER,
    building_number       INTEGER,
    price                 INTEGER,
    date_added            TEXT,
    entry_date            TEXT,
    updated_at            TEXT,
    customer_id           INTEGER,
    contact_name          TEXT,
    listing_id            TEXT    PRIMARY KEY
                                  UNIQUE
                                  NOT NULL,
    category_id           INTEGER,
    subcategory_id        INTEGER,
    ad_number             INTEGER,
    like_count            INTEGER,
    realtor_name          TEXT,
    apt_type              TEXT,
    apartment_state       TEXT,
    balconies             INTEGER,
    sqmt                  INTEGER,
    rooms                 INTEGER,
    latitude              REAL,
    longitude             REAL,
    floor                 INTEGER,
    ac                    INTEGER,
    b_shelter             INTEGER,
    furniture             INTEGER,
    central_ac            INTEGER,
    sunroom               INTEGER,
    storage               INTEGER,
    accesible             INTEGER,
    parking               INTEGER,
    pets                  INTEGER,
    window_bars           INTEGER,
    elevator              INTEGER,
    sub_apartment         INTEGER,
    renovated             INTEGER,
    long_term             INTEGER,
    pandora_doors         INTEGER,
    roommates             INTEGER,
    building_floors       INTEGER,
    vaad_bayit            INTEGER,
    furniture_description TEXT,
    description           TEXT,
    arnona                REAL,
    scanned               INTEGER,
    extra_info            INTEGER,
    id                    INTEGER UNIQUE,
    UNIQUE (
        street_id,
        building_number,
        customer_id,
        sqmt,
        rooms,
        floor,
        ac,
        building_floors
    )
    ON CONFLICT ABORT,
    UNIQUE (
        city_id,
        price,
        customer_id,
        balconies,
        sqmt,
        rooms,
        floor,
        ac,
        storage,
        parking,
        elevator
    )
);""")

for row in rows:

    cur.execute("""INSERT INTO Listings (
                             top_area_name,
                             top_area_id,
                             area_name,
                             area_id,
                             city_name,
                             city_id,
                             neighborhood_name,
                             neighborhood_id,
                             street_name,
                             street_id,
                             building_number,
                             price,
                             date_added,
                             entry_date,
                             updated_at,
                             customer_id,
                             contact_name,
                             listing_id,
                             category_id,
                             subcategory_id,
                             ad_number,
                             like_count,
                             realtor_name,
                             apt_type,
                             apartment_state,
                             balconies,
                             sqmt,
                             rooms,
                             latitude,
                             longitude,
                             floor,
                             ac,
                             b_shelter,
                             furniture,
                             central_ac,
                             sunroom,
                             storage,
                             accesible,
                             parking,
                             pets,
                             window_bars,
                             elevator,
                             sub_apartment,
                             renovated,
                             long_term,
                             pandora_doors,
                             roommates,
                             building_floors,
                             vaad_bayit,
                             furniture_description,
                             description,
                             arnona,
                             scanned,
                             extra_info,
                             id
                         )
                         SELECT top_area_name,
                                top_area_id,
                                area_name,
                                area_id,
                                city_name,
                                city_id,
                                neighborhood_name,
                                neighborhood_id,
                                street_name,
                                street_id,
                                building_number,
                                price,
                                date_added,
                                entry_date,
                                updated_at,
                                customer_id,
                                contact_name,
                                listing_id,
                                category_id,
                                subcategory_id,
                                ad_number,
                                like_count,
                                realtor_name,
                                apt_type,
                                apartment_state,
                                balconies,
                                sqmt,
                                rooms,
                                latitude,
                                longitude,
                                floor,
                                ac,
                                b_shelter,
                                furniture,
                                central_ac,
                                sunroom,
                                storage,
                                accesible,
                                parking,
                                pets,
                                window_bars,
                                elevator,
                                sub_apartment,
                                renovated,
                                long_term,
                                pandora_doors,
                                roommates,
                                building_floors,
                                vaad_bayit,
                                furniture_description,
                                description,
                                arnona,
                                scanned,
                                extra_info,
                                id
                           FROM temp_table;""")

cur.execute("""DROP TABLE temp_table;

    PRAGMA foreign_keys = 1;""")
