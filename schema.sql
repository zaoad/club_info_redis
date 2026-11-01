-- Create clubs table
CREATE TABLE clubs (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    location VARCHAR(200) NOT NULL,
    capacity INTEGER NOT NULL
);

-- Insert demo clubs
INSERT INTO clubs (name, location, capacity) VALUES
('Sunset Club', 'Downtown Miami', 500),
('The Grand Hall', 'Los Angeles', 1000),
('Blue Moon Lounge', 'New York City', 300),
('Starlight Arena', 'Las Vegas', 2000),
('Ocean View Club', 'San Diego', 400);
