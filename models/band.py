from __init__ import CONN, CURSOR

class Band:
    def __init__(self,name,hometown,id=None):
        self.id = id
        self.name = name
        self.hometown = hometown

    def __repr__(self) -> str:
             return f"<Band {self.id}: {self.name} from {self.hometown}>"
    

    @classmethod
    def create(cls, name, hometown):
        """Create a new band and save it to the database."""
        sql = """
            INSERT INTO bands (name, hometown) 
            VALUES (?, ?)
        """
        CURSOR.execute(sql, (name, hometown))
        CONN.commit()
        return cls(name, hometown, CURSOR.lastrowid)
    
    @classmethod
    def find_by_id(cls, id):
        """Find a band by its ID."""
        sql = "SELECT * FROM bands WHERE id = ?"
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls(row[1], row[2], row[0]) if row else None

    def concerts(self):
        """Return all concerts for this band."""
        sql = """
            SELECT * FROM concerts WHERE band_id = ?
        """
        concerts = CURSOR.execute(sql, (self.id,)).fetchall()
        return concerts

    def venues(self):
        """Return all venues this band has performed at."""
        sql = """
            SELECT venues.* FROM venues
            JOIN concerts ON venues.id = concerts.venue_id
            WHERE concerts.band_id = ?
        """
        rows = CURSOR.execute(sql, (self.id,)).fetchall()
        return rows

    def play_in_venue(self, venue, date):
        """Create a new concert for this band."""
        sql = """
            INSERT INTO concerts (band_id, venue_id, date) 
            VALUES (?, ?, ?)
        """
        venue_id = venue.id
        CURSOR.execute(sql, (self.id, venue_id, date))
        CONN.commit()

    @classmethod
    def most_performances(cls):
        """Return the band that has played the most concerts."""
        sql = """
            SELECT bands.*, COUNT(concerts.id) as concert_count FROM bands
            JOIN concerts ON bands.id = concerts.band_id
            GROUP BY bands.id
            ORDER BY concert_count DESC
            LIMIT 1
        """
        row = CURSOR.execute(sql).fetchone()
        return cls(row[1], row[2], row[0]) if row else None

        
