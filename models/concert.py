



class Concert:
    def __init__(self, band_id, venue_id, date, id=None):
        self.id = id
        self.band_id = band_id
        self.venue_id = venue_id
        self.date = date

    def __repr__(self):
        return f"<Concert {self.id}: Band {self.band_id} at Venue {self.venue_id} on {self.date}>"

    @classmethod
    def create(cls, band_id, venue_id, date):
        """Create a new concert and save it to the database."""
        sql = """
            INSERT INTO concerts (band_id, venue_id, date) 
            VALUES (?, ?, ?)
        """
        CURSOR.execute(sql, (band_id, venue_id, date))
        CONN.commit()
        return cls(band_id, venue_id, date, CURSOR.lastrowid)
    

    @classmethod
    def find_by_id(cls, id):
        """Find a concert by its ID."""
        sql = "SELECT * FROM concerts WHERE id = ?"
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls(row[1], row[2], row[3], row[0]) if row else None

    def band(self):
        """Return the Band instance for this concert."""
        return Band.find_by_id(self.band_id)

    def venue(self):
        """Return the Venue instance for this concert."""
        return Venue.find_by_id(self.venue_id)

    def hometown_show(self):
        """Return true if the concert is in the band's hometown, false otherwise."""
        sql = """
            SELECT bands.hometown, venues.city FROM concerts
            JOIN bands ON concerts.band_id = bands.id
            JOIN venues ON concerts.venue_id = venues.id
            WHERE concerts.id = ?
        """
        row = CURSOR.execute(sql, (self.id,)).fetchone()
        return row[0] == row[1]  

    def introduction(self):
        """Return the introduction string for this concert."""
        band = self.band()
        venue = self.venue()
        return f"Hello {venue.city}!!!!! We are {band.name} and we're from {band.hometown}"