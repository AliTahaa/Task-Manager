-- Create the 'user' table
CREATE TABLE IF NOT EXISTS `user` (
  `id` INT AUTO_INCREMENT PRIMARY KEY,
  `username` VARCHAR(150) NOT NULL UNIQUE,
  `email` VARCHAR(255) UNIQUE NOT NULL,
  `password` VARCHAR(150) NOT NULL
);
-- Create the 'task' table
CREATE TABLE IF NOT EXISTS `task` (
  `id` INT AUTO_INCREMENT PRIMARY KEY,
  `title` VARCHAR(255) NOT NULL,
  `description` TEXT NULL,
  `is_completed` BOOLEAN NOT NULL DEFAULT FALSE,
  `user_id` INT NOT NULL,
  `priority` ENUM('Low', 'Medium', 'High') NOT NULL DEFAULT 'Medium',
  FOREIGN KEY (`user_id`) REFERENCES `user`(`id`) ON DELETE CASCADE
);
-- Sample user insertion
INSERT INTO `user` (username, password)
VALUES ('sample_user', 'hashed_password');
-- Sample task insertion (for the sample user)
INSERT INTO `task` (title, user_id)
VALUES ('Sample Task 1', 1),
  ('Sample Task 2', 1),
  ('Sample Task 3', 1);
