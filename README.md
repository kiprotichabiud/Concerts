# Concerts  Project
This is a project for creating a Concerts management system using raw SQL queries in Python. 



The project uses raw SQL queries to interact with the database for the following tasks:

- Retrieve concert details.
- Manage relationships between bands, venues, and concerts.
- Aggregate information, such as counting the number of performances by a band or finding a band's concerts at specific venues.
Database Schema
1. Bands Table
- Column	Type
- id	INTEGER (Primary Key)
- name	TEXT
- hometown	TEXT
2. Venues Table
- Column	Type
- id	INTEGER (Primary Key)
- title	TEXT
- city	TEXT
3. Concerts Table
- Column	Type
- id	INTEGER (Primary Key)
- band_id	INTEGER (Foreign Key)
- venue_id	INTEGER (Foreign Key)
- date	TEXT
Setup Instructions
## Prerequisites
- Python 3.x installed
- SQLite3 library (comes pre-installed with Python)
## Steps to Set Up the Project
1.Clone the Repository:


- `git@github.com:kiprotichabiud/Concerts.git`
- `cd concerts`





## Contributing
If you'd like to contribute to this project:

### Fork the repository.
- Create a new branch for your feature (git checkout -b feature-branch).
- Commit your changes (git commit -am 'Add new feature').
- Push to the branch (git push origin feature-branch).
- Open a pull request for review.
## License
This project is licensed under the MIT License. See the LICENSE file for more details.
## Author
Abiud kiprotich

