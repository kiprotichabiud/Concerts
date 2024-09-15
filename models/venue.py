

class Venue:
    def __init__(self, title, city, id=None):
        self.id = id
        self.title = title
        self.city = city

    def __repr__(self):
        return f"<Venue {self.id}: {self.title} in {self.city}>"

    @classmethod
    def create(cls, title, city):
        """Create a new venue and save it to the database."""
        sql = """
            INSERT INTO venues (title, city) 
            VALUES (?, ?)
        """
        CURSOR.execute(sql, (title, city))
        CONN.commit()
        return cls(title, city, CURSOR.lastrowid)

    @classmethod
    def find_by_id(cls, id):
        """Find a venue by its ID."""
        sql = "SELECT * FROM venues WHERE id = ?"
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls(row[1], row[2], row[0]) if row else None

    def concerts(self):
        """Return all concerts for this venue."""
        sql = """
            SELECT * FROM concerts WHERE venue_id = ?
        """
        concerts = CURSOR.execute(sql, (self.id,)).fetchall()
        return concerts

    def bands(self):
        """Return all bands that have performed at this venue."""
        sql = """
            SELECT bands.* FROM bands
            JOIN concerts ON bands.id = concerts.band_id
            WHERE concerts.venue_id = ?
        """
        rows = CURSOR.execute(sql, (self.id,)).fetchall()
        return rows

    @classmethod
    def concert_on(cls, date):
        """Find the first concert on a specific date at this venue."""
        sql = """
            SELECT * FROM concerts WHERE date = ? LIMIT 1
        """
        row = CURSOR.execute(sql, (date,)).fetchone()
        return row

    @classmethod
    def most_frequent_band(cls):
        """Return the band that has performed the most at this venue."""
        sql = """
            SELECT bands.*, COUNT(concerts.id) as concert_count FROM bands
            JOIN concerts ON bands.id = concerts.band_id
            WHERE concerts.venue_id = ?
            GROUP BY bands.id
            ORDER BY concert_count DESC
            LIMIT 1
        """
        row = CURSOR.execute(sql, (cls.id,)).fetchone()
        return row
