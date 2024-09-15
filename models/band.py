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


        
