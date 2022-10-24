#Задание 1
#https://stepik.org/lesson/297508/step/8?unit=279268

CREATE TABLE book(
    book_id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(50),
    author VARCHAR(30),
    price DECIMAL(8, 2),
    amount INT
);


# Задание 2
# https://stepik.org/lesson/297508/step/9?unit=279268

INSERT book (title, author, price, amount)
VALUE ("Мастер и Маргарита", "Булгаков М.А.", 670.99, 3);
INSERT book (title, author, price, amount)
VALUE ("Белая гвардия", "Булгаков М.А.", 540.50, 5);
INSERT book (title, author, price, amount)
VALUE ("Идиот", "Достоевский Ф.М.", 460.00, 10);
INSERT book (title, author, price, amount)
VALUE ("Братья Карамазовы", "Достоевский Ф.М.", 799.01, 2);

#Задание 2
# https://stepik.org/lesson/297509/step/2?unit=279269
SELECT * FROM book;

# Задание 4
# https://stepik.org/lesson/297509/step/3?unit=279269
SELECT author, title, price FROM book;

# Задание 5
# https://stepik.org/lesson/297509/step/4?unit=279269
SELECT title AS Название, author AS Автор FROM book;

# Задание 6
# https://stepik.org/lesson/297509/step/5?unit=279269
SELECT title, amount, amount * 1.65 AS pack FROM book;
