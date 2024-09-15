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

        
