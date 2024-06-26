CREATE TABLE book (book_id int, book_title text, book_author text, publisher_id int);
INSERT INTO book VALUES 
(1, 'Преступление и наказание', 'Ф.И.Достоевский', '1'),
(2, 'Белые ночи', 'Ф.И.Достоевский', '1'),
(3, 'Искупление', 'И.Р.Макьюэн', '2'),
(4, 'Амстердам', 'И.Р.Макьюэн', '1'),
(5, 'Театр', 'У.С.Моэм', '3');
SELECT * FROM book;
SELECT * FROM book WHERE book_author='Ф.И.Достоевский';
SELECT * FROM book WHERE publisher_id='1';
SELECT book_id FROM book WHERE book_title LIKE '%е%о%' OR book_author LIKE '%а%';
