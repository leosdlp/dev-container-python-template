CREATE TABLE IF NOT EXISTS links (
    id INT AUTO_INCREMENT PRIMARY KEY,
    country VARCHAR(255) NOT NULL,
    country_link VARCHAR(255) NOT NULL
);


-- cost_of_life
CREATE TABLE IF NOT EXISTS data_cost_of_life (
    id INT AUTO_INCREMENT PRIMARY KEY,
    country VARCHAR(255),
    description TEXT,
    value VARCHAR(255),
    unit VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS clean_data_cost_of_life (
    id INT AUTO_INCREMENT PRIMARY KEY,
    country VARCHAR(255) NOT NULL,
    description TEXT NOT NULL,
    price FLOAT NOT NULL,
    unitPrice VARCHAR(255) NOT NULL
);


-- crime
CREATE TABLE IF NOT EXISTS data_crime (
    id INT AUTO_INCREMENT PRIMARY KEY,
    country VARCHAR(255),
    description TEXT,
    value VARCHAR(255),
    unit VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS clean_data_crime (
    id INT AUTO_INCREMENT PRIMARY KEY,
    country VARCHAR(255) NOT NULL,
    description TEXT NOT NULL,
    value FLOAT NOT NULL,
    unit VARCHAR(255) NOT NULL
);

-- pollution
CREATE TABLE IF NOT EXISTS data_pollution (
    id INT AUTO_INCREMENT PRIMARY KEY,
    country VARCHAR(255),
    description TEXT,
    value VARCHAR(255),
    unit VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS clean_data_pollution (
    id INT AUTO_INCREMENT PRIMARY KEY,
    country VARCHAR(255) NOT NULL,
    description TEXT NOT NULL,
    value FLOAT NOT NULL,
    unit VARCHAR(255) NOT NULL
);